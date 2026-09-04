# Agent Operating Contract

This repository is a curated, repo-local starter for projects managed by Codex and Paseo. Keep it easy to copy and scoped to project concerns.

## Core Rules

- Explore the repository before asking questions; prefer local evidence and `rg`/`rg --files`.
- Keep changes limited to the request. Preserve user work and never revert unrelated edits.
- Verify before reporting completion. State checks run, checks skipped, and residual risk.
- Do not add global machine configuration, credentials, telemetry, providers, or personal paths.
- Call out security and compatibility risks explicitly.

## Workflow

1. Identify the goal and affected surface.
2. Inspect only the relevant files, configs, tests, schemas, and documentation.
3. Choose the smallest defensible implementation.
4. Make focused edits.
5. Run verification proportional to the risk.
6. Summarize changes, evidence, and remaining uncertainty.

Plan first for large, ambiguous, or risky work. Small fixes can proceed after inspection.

## Context Discipline

- Map with filenames and targeted search before reading file bodies.
- Read the smallest useful section; do not dump whole catalogs, logs, or generated files when a focused query answers the question.
- Shape command output at the source with filters, line ranges, and explicit output budgets. Preserve a path or command for follow-up instead of embedding raw noise.
- Do not reread unchanged material. Keep stable decisions in repo files and retrieve details just in time.
- Stop exploring once the implementation decision is supported by enough evidence.
- Keep handoffs and final reports compact: conclusions first, then decisive evidence and gaps.

## Agents and Skills

Start with the main Codex agent. Use a project-local subagent only when specialization, independent parallel work, or context isolation is worth the coordination and token cost. Give it a bounded goal and require a distilled result with file, command, log, or screenshot evidence.

Agent selection lives in `docs/agent-catalog.md`; model defaults and escalation rules live in `docs/model-routing.md`. Preserve the checked-in model and use the lowest reasoning effort that meets the verifier.

Repo-local skills live in `.agents/skills/`. Load a skill when its description matches the task, and read conditional references only when their stated trigger applies. Add a skill only for repeated, stable work with a clear boundary.

Load `browser-integration` before any browser-driven task. It selects exactly one session lane: explicit `@Chrome` or `@Browser`, otherwise Paseo when its native tools are exposed. Never treat those host-specific lanes as automatic fallbacks. Other Paseo use remains limited to an advisor, committee, handoff, or bounded loop whose benefit is explicit; see `docs/agent-workflows.md`.

## Quality Bar

- Findings must be grounded in files, commands, logs, tests, docs, or clearly marked inference.
- Narrow changes need targeted checks; shared behavior needs broader validation.
- Documentation should retain decisions and gotchas future agents need, without duplicating discoverable catalogs.
