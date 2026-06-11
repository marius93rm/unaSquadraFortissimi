# Source Curation

This skeleton draws from multiple agent and skill repositories, but it intentionally does not copy them wholesale.

## Import Rules

- Import principles before files.
- Prefer small repo-local instructions over global setup.
- Avoid duplicate roles with different names.
- Add a skill only when the workflow is repeated and stable.
- Add a subagent only when specialization changes the quality or safety of work.
- Do not vendor large catalogs, installers, generated assets, telemetry, or framework-specific stacks.

## Current Source Decisions

- Codex official docs define the local shape: `AGENTS.md`, `.codex/config.toml`, `.codex/agents/*.toml`, and `.agents/skills/*/SKILL.md`.
- Paseo informs the orchestration playbook: advisor, committee, handoff, and loop.
- awesome-codex-subagents informs the five role choices, but the repo does not import the full catalog.
- Superpowers informs planning, TDD, systematic debugging, and verification discipline.
- ECC informs repo-local skills, security posture, and the preference for minimal/manual profiles over layered installs.
- last30days informs the recent-research workflow, but its engine and scripts are not vendored.
- taste-skill informs frontend quality guidance, but only a compact general-purpose skill is included.
- pm-skills and agency-agents inform product and specialist-agent vocabulary, but the essential profile excludes broad product, sales, marketing, and agency catalogs.

## When to Add More

Add new material only when all are true:

1. The same need appears in multiple projects or tasks.
2. Existing instructions do not cover it cleanly.
3. The new file has a clear trigger and boundary.
4. It does not require global machine state.
5. It can be verified with a simple repo-local check.

If the addition is domain-specific, keep it in that project rather than this skeleton.
