#!/usr/bin/env python3
"""Repo-local integrity checks for unaSquadraFortissimi.

The goal is not to prove every sentence in the docs. The goal is to catch
high-signal drift between the canonical files:

- .codex/agents/*.toml
- .agents/skills/*/SKILL.md
- AGENTS.md
- README.md
- docs/agent-catalog.md
- index.html
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
REPO_BLOB_PREFIX = "/marius93rm/unaSquadraFortissimi/blob/main/"

AGENT_REQUIRED_FIELDS = {
    "name",
    "description",
    "model",
    "model_reasoning_effort",
    "sandbox_mode",
    "developer_instructions",
}

ALLOWED_REASONING = {"low", "medium", "high"}
ALLOWED_SANDBOX = {"read-only", "workspace-write"}


@dataclass(frozen=True)
class CheckResult:
    path: str
    message: str


class LocalHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[tuple[str, str]] = []
        self.images: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value or "" for key, value in attrs}
        if "id" in attr_map:
            self.ids.add(attr_map["id"])
        if "href" in attr_map:
            self.links.append((tag, attr_map["href"]))
        if "src" in attr_map:
            self.links.append((tag, attr_map["src"]))
        if tag == "img":
            self.images.append((attr_map.get("src", ""), attr_map.get("alt", "")))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def fail(failures: list[CheckResult], path: str | Path, message: str) -> None:
    failures.append(CheckResult(rel(path) if isinstance(path, Path) else path, message))


def parse_simple_toml(text: str) -> dict[str, str]:
    """Parse the simple top-level string assignments used by agent TOML files."""
    data: dict[str, str] = {}
    lines = text.splitlines()
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        index += 1

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if value.startswith('"""'):
            collected: list[str] = []
            value = value[3:]
            if value.endswith('"""'):
                data[key] = value[:-3]
                continue
            collected.append(value)
            while index < len(lines):
                current = lines[index]
                index += 1
                if current.rstrip().endswith('"""'):
                    collected.append(current.rstrip()[:-3])
                    break
                collected.append(current)
            data[key] = "\n".join(collected).strip()
            continue

        match = re.fullmatch(r'"(.*)"', value)
        if match:
            data[key] = match.group(1)

    return data


def parse_skill_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    frontmatter: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()

    return frontmatter


def find_agent_files() -> list[Path]:
    return sorted((ROOT / ".codex" / "agents").glob("*.toml"))


def find_skill_files() -> list[Path]:
    return sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))


def assert_text_mentions_all(
    failures: list[CheckResult],
    doc_path: Path,
    names: Iterable[str],
    label: str,
) -> None:
    text = read_text(doc_path)
    for name in names:
        if f"`{name}`" not in text and name not in text:
            fail(failures, doc_path, f"missing {label} reference: {name}")


def check_agents(failures: list[CheckResult]) -> list[str]:
    agent_files = find_agent_files()
    agent_names: list[str] = []

    if not agent_files:
        fail(failures, ".codex/agents", "no agent TOML files found")
        return agent_names

    for path in agent_files:
        data = parse_simple_toml(read_text(path))
        missing = sorted(AGENT_REQUIRED_FIELDS - data.keys())
        if missing:
            fail(failures, path, f"missing required fields: {', '.join(missing)}")
            continue

        expected_name = path.stem
        actual_name = data["name"]
        agent_names.append(actual_name)

        if actual_name != expected_name:
            fail(failures, path, f"name must match filename stem: expected {expected_name}, got {actual_name}")
        if data["model_reasoning_effort"] not in ALLOWED_REASONING:
            fail(failures, path, f"invalid model_reasoning_effort: {data['model_reasoning_effort']}")
        if data["sandbox_mode"] not in ALLOWED_SANDBOX:
            fail(failures, path, f"invalid sandbox_mode: {data['sandbox_mode']}")
        if not data["model"].startswith("gpt-"):
            fail(failures, path, f"model should be an explicit gpt-* value, got {data['model']}")
        if len(data["developer_instructions"].split()) < 20:
            fail(failures, path, "developer_instructions look too short to guide the agent")

    return sorted(agent_names)


def check_skills(failures: list[CheckResult]) -> list[str]:
    skill_files = find_skill_files()
    skill_names: list[str] = []

    if not skill_files:
        fail(failures, ".agents/skills", "no SKILL.md files found")
        return skill_names

    for path in skill_files:
        frontmatter = parse_skill_frontmatter(read_text(path))
        expected_name = path.parent.name
        actual_name = frontmatter.get("name")

        if not actual_name:
            fail(failures, path, "missing frontmatter name")
            continue

        skill_names.append(actual_name)

        if actual_name != expected_name:
            fail(failures, path, f"name must match directory: expected {expected_name}, got {actual_name}")
        if not frontmatter.get("description"):
            fail(failures, path, "missing frontmatter description")

    return sorted(skill_names)


def check_docs(failures: list[CheckResult], agent_names: list[str], skill_names: list[str]) -> None:
    agents_md = ROOT / "AGENTS.md"
    readme = ROOT / "README.md"
    catalog = ROOT / "docs" / "agent-catalog.md"

    for path in [agents_md, readme, catalog]:
        if not path.exists():
            fail(failures, path, "required documentation file is missing")
            return

    assert_text_mentions_all(failures, agents_md, agent_names, "agent")
    assert_text_mentions_all(failures, catalog, agent_names, "agent")
    assert_text_mentions_all(failures, readme, agent_names, "agent")

    assert_text_mentions_all(failures, agents_md, skill_names, "skill")
    assert_text_mentions_all(failures, catalog, skill_names, "skill")
    assert_text_mentions_all(failures, readme, skill_names, "skill")

    readme_text = read_text(readme)
    expected_map_entries = [
        "index.html",
        "styles.css",
        "favicon.svg",
        "scripts/validate_repo.py",
        "assets/agents/",
        "assets/skills/",
    ]
    for entry in expected_map_entries:
        if entry not in readme_text:
            fail(failures, readme, f"Repository Map should mention `{entry}`")

    expected_count_phrases = [
        f"{len(agent_names)} Codex subagents",
        f"{len(skill_names)} repo-local skills",
        f"{len(agent_names)} agenti Codex",
        f"{len(skill_names)} skill repo-local",
    ]
    for phrase in expected_count_phrases:
        if phrase not in readme_text:
            fail(failures, readme, f"count phrase is stale or missing: {phrase}")


def is_external_reference(value: str) -> bool:
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "mailto", "tel", "data"} and REPO_BLOB_PREFIX not in parsed.path


def repo_blob_path(value: str) -> Path | None:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"}:
        return None
    if not parsed.netloc.endswith("github.com"):
        return None
    if REPO_BLOB_PREFIX not in parsed.path:
        return None
    raw_path = parsed.path.split(REPO_BLOB_PREFIX, 1)[1]
    return ROOT / unquote(raw_path)


def check_html(failures: list[CheckResult]) -> None:
    html_path = ROOT / "index.html"
    if not html_path.exists():
        fail(failures, html_path, "static landing page is missing")
        return

    parser = LocalHtmlParser()
    parser.feed(read_text(html_path))

    for tag, value in parser.links:
        if not value or value.startswith("#"):
            if value.startswith("#") and value[1:] not in parser.ids:
                fail(failures, html_path, f"broken anchor link `{value}` in <{tag}>")
            continue

        blob_path = repo_blob_path(value)
        if blob_path is not None:
            if not blob_path.exists():
                fail(failures, html_path, f"GitHub blob link points to missing path: {rel(blob_path)}")
            continue

        if is_external_reference(value):
            continue

        local_path = ROOT / value.split("#", 1)[0]
        if not local_path.exists():
            fail(failures, html_path, f"local <{tag}> reference points to missing path: {value}")

    for src, alt in parser.images:
        if src and not alt.strip():
            fail(failures, html_path, f"image `{src}` is missing alt text")


def run_checks() -> list[CheckResult]:
    failures: list[CheckResult] = []
    agent_names = check_agents(failures)
    skill_names = check_skills(failures)
    check_docs(failures, agent_names, skill_names)
    check_html(failures)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate unaSquadraFortissimi repo-local agent skeleton.")
    parser.add_argument("--quiet", action="store_true", help="Only print failures.")
    args = parser.parse_args()

    failures = run_checks()

    if failures:
        print("Repo validation failed:\n")
        for item in failures:
            print(f"- {item.path}: {item.message}")
        return 1

    if not args.quiet:
        print("Repo validation passed.")
        print(f"- agents: {len(find_agent_files())}")
        print(f"- skills: {len(find_skill_files())}")
        print("- docs, landing links, local assets, anchors, and count phrases checked")

    return 0


if __name__ == "__main__":
    sys.exit(main())
