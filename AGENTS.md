# Agent Operating Contract

This repository is a starter skeleton for future projects managed by Codex and Paseo. Keep it curated, repo-local, and easy to copy.

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

Project-local Codex agents live in `.codex/agents/`. Use them explicitly when the task benefits from parallel or specialized work.

Core context and planning:

- `context_manager`: map repo structure and package task-relevant context.
- `architect`: analyze architecture, boundaries, tradeoffs, and sequencing.
- `minimal_change_engineer`: keep narrow fixes small and prevent scope creep.

Implementation specialists:

- `backend_developer`: implement scoped backend behavior and failure paths.
- `frontend_developer`: implement scoped UI, state, and user-facing flows.
- `devops_engineer`: update CI, release, deployment, and environment configuration.
- `technical_writer`: write README, runbook, migration, API, and release docs.

Review and verification:

- `reviewer`: review diffs for correctness, regressions, security, and missing tests.
- `typescript_reviewer`: review TS/JS type, async, and runtime correctness.
- `react_reviewer`: review React hooks, rendering, accessibility, and RSC/client boundaries.
- `security_auditor`: inspect auth, input handling, secrets, config, and supply-chain risk.
- `database_reviewer`: review schema, SQL, migrations, indexes, RLS, and locking.
- `dependency_reviewer`: review package, plugin, license, and supply-chain changes.
- `accessibility_tester`: audit keyboard, semantics, labels, focus, and WCAG risk.
- `test_automator`: add focused regression tests.
- `evidence_collector`: gather screenshots, logs, command output, and proof.

Specialist analysis:

- `debugger`: isolate bugs, failing tests, runtime traces, and root causes.
- `docs_researcher`: verify APIs, framework behavior, versions, and official docs.
- `performance_optimizer`: analyze latency, bundle size, memory, Core Web Vitals, and bottlenecks.
- `product_manager`: frame scope, prioritization, PRDs, and acceptance criteria.
- `ux_researcher`: synthesize user research, journeys, personas, and usability risk.
- `eval_engineer`: design evals for prompts, retrieval, tools, and agent workflows.

Do not spawn subagents reflexively. Use them when they reduce risk, isolate work, or produce evidence that would otherwise pollute the main context. Keep prompts narrow and verify their claims against files, diffs, commands, logs, or screenshots.

## Skills

Repo-local skills live in `.agents/skills/`. Load them when their description matches the task.

Execution discipline:

- `repo-discovery`
- `brainstorming`
- `planning-contract`
- `writing-plans`
- `subagent-driven-development`
- `using-git-worktrees`
- `verification-loop`
- `branch-finish`

Engineering quality:

- `tdd-workflow`
- `systematic-debugging`
- `code-review`
- `security-review`
- `dependency-review`
- `performance-audit`
- `accessibility-audit`
- `evidence-qa`

Product, research, and docs:

- `recent-research`
- `prd-writing`
- `feature-request-triage`
- `release-notes`
- `technical-writing`
- `eval-design`
- `incident-response`

Frontend taste:

- `frontend-taste`
- `design-taste-frontend`

Keep skills concise. Add a new skill only for repeated work that benefits from a stable workflow and a clear trigger.

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
