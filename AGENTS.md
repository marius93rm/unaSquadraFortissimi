# Agent Operating Contract

This repository is a starter skeleton for future projects managed by Codex and Paseo. Keep it small, repo-local, and easy to copy.

## First Principles

- Read this file before doing non-trivial work.
- Explore the repository before asking the user questions. Use local evidence first.
- Prefer `rg` and `rg --files` for search.
- Keep changes scoped to the request. Do not refactor unrelated files.
- Preserve user work. Never revert changes you did not make unless explicitly asked.
- Verify before reporting completion. State what was and was not checked.
- Do not add global machine configuration, credentials, telemetry, providers, or personal paths to this repo.

## Expected Workflow

1. Identify the task goal and affected surface.
2. Inspect relevant files, configs, tests, schemas, and docs.
3. Choose the smallest defensible implementation.
4. Make focused edits.
5. Run targeted verification.
6. Summarize changes, checks, and residual risk.

For large or ambiguous work, produce a short plan before editing. For small fixes, proceed directly after inspection.

## Codex Subagents

Project-local Codex agents live in `.codex/agents/`. Use them explicitly when the task benefits from parallel or specialized work:

- `context_manager`: map repo structure and package task-relevant context.
- `docs_researcher`: verify APIs, framework behavior, versions, and official docs.
- `reviewer`: review diffs for correctness, regressions, security, and missing tests.
- `security_auditor`: inspect auth, input handling, secrets, config, and supply-chain risk.
- `debugger`: isolate bugs, failing tests, runtime traces, and root causes.

Do not spawn subagents reflexively. Use them when they reduce risk or isolate work that would otherwise pollute the main context.

## Skills

Repo-local skills live in `.agents/skills/`. Load them when their description matches the task:

- `repo-discovery`
- `planning-contract`
- `verification-loop`
- `tdd-workflow`
- `systematic-debugging`
- `security-review`
- `frontend-taste`
- `recent-research`

Keep skills concise. Add a new skill only for repeated work that benefits from a stable workflow.

## Paseo

Paseo is the orchestration layer, not a vendored dependency here. Use it for:

- second opinions with an advisor
- committee planning for hard or risky work
- handoff when another agent needs full context
- bounded loops with clear acceptance criteria

See `docs/agent-workflows.md` for the repo playbook.

## Quality Bar

- Findings and claims should be grounded in files, commands, logs, tests, docs, or clearly marked inference.
- Security and compatibility risks should be called out explicitly.
- Tests should match risk. Narrow changes need targeted checks; shared behavior needs broader validation.
- Documentation should preserve decisions and gotchas that future agents need.
