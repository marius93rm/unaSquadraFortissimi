# unaSquadraFortissimi

<p align="center">
  <img src="assets/agent-fellowship-medieval.png" alt="A realistic medieval oil painting of specialized coding agents as armored knights around a planning table" width="100%" />
</p>

<p align="center">
  <strong>Uno scheletro repo-local, curato e copiabile per progetti gestiti da agenti.</strong>
  <br />
  Codex per esecuzione e skill. Paseo per orchestrazione. Zero rumore inutile.
</p>

<p align="center">
  <img alt="Codex" src="https://img.shields.io/badge/Codex-project_agents-111827?style=for-the-badge&logo=openai&logoColor=white" />
  <img alt="Paseo" src="https://img.shields.io/badge/Paseo-orchestration-7c3aed?style=for-the-badge" />
  <img alt="Agent Skills" src="https://img.shields.io/badge/Agent_Skills-repo_local-0f766e?style=for-the-badge" />
  <img alt="Markdown" src="https://img.shields.io/badge/Markdown-docs-334155?style=for-the-badge&logo=markdown&logoColor=white" />
</p>

## Table of Contents

- [Vision](#vision)
- [Stack](#stack)
- [What's Included](#whats-included)
- [Repository Map](#repository-map)
- [Start a New Project](#start-a-new-project)
- [Codex Agents](#codex-agents)
- [Local Skills](#local-skills)
- [Paseo Workflows](#paseo-workflows)
- [Source Philosophy](#source-philosophy)
- [Non-Goals](#non-goals)

## Vision

**unaSquadraFortissimi** is a starter skeleton for future projects where AI agents are first-class collaborators.

The point is not to install every hook, command, provider, and research pipeline on the internet. The point is to preserve a **useful repo-local operating system**:

- clear project instructions
- a strong but bounded Codex subagent roster
- compact repo-local skills with clear triggers
- lightweight Paseo workflow guidance
- explicit source curation and attribution
- rules against duplicate roles, global config, and tool sprawl

## Stack

| Layer | Tool | Role |
| --- | --- | --- |
| **Agent runtime** | Codex | Main coding agent, project instructions, subagents, repo-local skills |
| **Orchestration** | Paseo | Advisor, committee, handoff, bounded loops |
| **Knowledge** | Markdown | Human-readable operating contract and workflow docs |
| **Configuration** | TOML | Small project-local Codex agent config |
| **Assets** | Generated image | Project identity and README hero |

## What's Included

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Main operating contract for agents working in this repository |
| `.codex/config.toml` | Project-local Codex subagent limits |
| `.codex/agents/` | 22 Codex subagents across implementation, review, product, ops, QA, and evals |
| `.agents/skills/` | 25 compact repo-local skills |
| `docs/agent-workflows.md` | Practical Paseo playbook |
| `docs/agent-catalog.md` | Agent and skill activation matrix |
| `docs/source-curation.md` | Rules for importing ideas without copying entire catalogs |
| `assets/agent-fellowship-medieval.png` | Generated medieval fellowship hero image |

## Repository Map

```text
.
|-- AGENTS.md
|-- README.md
|-- assets/
|   `-- agent-fellowship-medieval.png
|-- docs/
|   |-- agent-catalog.md
|   |-- agent-workflows.md
|   `-- source-curation.md
|-- .codex/
|   |-- config.toml
|   `-- agents/
|       |-- accessibility_tester.toml
|       |-- architect.toml
|       |-- backend_developer.toml
|       |-- context_manager.toml
|       |-- database_reviewer.toml
|       |-- debugger.toml
|       |-- dependency_reviewer.toml
|       |-- devops_engineer.toml
|       |-- docs_researcher.toml
|       |-- eval_engineer.toml
|       |-- evidence_collector.toml
|       |-- frontend_developer.toml
|       |-- minimal_change_engineer.toml
|       |-- performance_optimizer.toml
|       |-- product_manager.toml
|       |-- react_reviewer.toml
|       |-- reviewer.toml
|       |-- security_auditor.toml
|       |-- technical_writer.toml
|       |-- test_automator.toml
|       |-- typescript_reviewer.toml
|       `-- ux_researcher.toml
`-- .agents/
    `-- skills/
        |-- accessibility-audit/
        |-- brainstorming/
        |-- branch-finish/
        |-- code-review/
        |-- dependency-review/
        |-- design-taste-frontend/
        |-- eval-design/
        |-- evidence-qa/
        |-- feature-request-triage/
        |-- frontend-taste/
        |-- incident-response/
        |-- performance-audit/
        |-- planning-contract/
        |-- prd-writing/
        |-- recent-research/
        |-- release-notes/
        |-- repo-discovery/
        |-- security-review/
        |-- subagent-driven-development/
        |-- systematic-debugging/
        |-- technical-writing/
        |-- tdd-workflow/
        |-- using-git-worktrees/
        |-- verification-loop/
        `-- writing-plans/
```

## Start a New Project

1. **Copy this skeleton** into a fresh repository.
2. **Replace this README** with project-specific product, setup, and run instructions.
3. **Update `AGENTS.md`** with real build, test, lint, deploy, and safety rules.
4. **Prune the roster** if a project does not need all specialists.
5. **Use Paseo deliberately** when a second opinion, committee, handoff, or loop reduces risk.

## Codex Agents

Project-local Codex agents live in `.codex/agents/`.

| Lane | Agents |
| --- | --- |
| Context and design | `context_manager`, `architect`, `minimal_change_engineer` |
| Implementation | `backend_developer`, `frontend_developer`, `devops_engineer`, `technical_writer` |
| Review | `reviewer`, `typescript_reviewer`, `react_reviewer`, `security_auditor`, `database_reviewer`, `dependency_reviewer`, `accessibility_tester` |
| Verification | `test_automator`, `evidence_collector`, `debugger`, `performance_optimizer` |
| Product and research | `docs_researcher`, `product_manager`, `ux_researcher`, `eval_engineer` |

These agents are **project-local** and **explicitly invoked**. They are not meant to replace careful repo reading. See `docs/agent-catalog.md` for activation guidance.

## Local Skills

Repo-local skills live in `.agents/skills/`.

| Skill | Use |
| --- | --- |
| `repo-discovery` | First pass through an unfamiliar repo |
| `brainstorming` | Clarify substantial product, UX, creative, or architecture work |
| `planning-contract` | Decision-complete plans for risky or multi-step work |
| `writing-plans` | Implementation plans with sequencing, affected files, and verification |
| `subagent-driven-development` | Delegate independent workstreams to bounded specialist agents |
| `using-git-worktrees` | Isolate branch work when the workspace is dirty or parallel |
| `verification-loop` | Final checks before declaring work complete |
| `branch-finish` | End-of-branch diff review, verification, and handoff discipline |
| `tdd-workflow` | Behavior changes protected by tests |
| `systematic-debugging` | Bugs, failing tests, flakes, and regressions |
| `code-review` | PR-style diff review |
| `security-review` | Trust boundaries, secrets, input handling, and unsafe defaults |
| `dependency-review` | Package, plugin, license, and supply-chain changes |
| `performance-audit` | Latency, Core Web Vitals, memory, bundle, or query bottlenecks |
| `accessibility-audit` | Keyboard, semantics, focus, labels, and WCAG-oriented checks |
| `evidence-qa` | Screenshot, command, log, and reproduction proof |
| `frontend-taste` | Polished UI, hierarchy, spacing, responsive behavior |
| `design-taste-frontend` | Stronger taste-skill workflow for landing pages, portfolios, and redesigns |
| `recent-research` | Time-sensitive external facts and current community signals |
| `prd-writing` | Product requirements and acceptance criteria |
| `feature-request-triage` | Backlog and customer-request prioritization |
| `release-notes` | User-facing and stakeholder-facing release summaries |
| `technical-writing` | README, runbook, API, troubleshooting, and migration docs |
| `eval-design` | Evaluation scenarios, rubrics, and gates for AI workflows |
| `incident-response` | Production incident stabilization, evidence, and recovery |

## Paseo Workflows

Use Paseo as orchestration, not as a vendored dependency.

- **Advisor**: one second opinion without handing off ownership.
- **Committee**: root-cause analysis and planning for hard or risky work.
- **Handoff**: pass complete context to another agent when continuity matters.
- **Loop**: repeat only against a clear verifier and stop condition.

See `docs/agent-workflows.md` for the full playbook.

## Source Philosophy

This skeleton is inspired by:

- Codex official docs
- Paseo
- awesome-codex-subagents
- Superpowers
- ECC
- last30days
- taste-skill
- pm-skills
- agency-agents

The rule is simple: **copy the best operating patterns, not the entire catalogs**.

If a source contains 200 useful ideas, this repo should still keep only the roles and workflows that are stable, repeated, and generally useful across future projects.

## Non-Goals

- No global Codex configuration
- No tokens, credentials, provider settings, or personal paths
- No uncurated imported skill catalog
- No vendored research engines
- No framework choice before a real project needs one
- No agents that differ only by branding or personality

## Italiano

Questo scheletro e curato ma ancora copiabile: istruzioni operative, un roster Codex solido, skill essenziali, playbook Paseo e una linea estetica chiara.

La squadra deve rimanere forte perche resta ordinata.
