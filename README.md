# unaSquadraFortissimi

<p align="center">
  <img src="assets/agent-fellowship-medieval.png" alt="A realistic medieval oil painting of specialized coding agents as armored knights around a planning table" width="100%" />
</p>

<p align="center">
  <strong>Uno scheletro repo-local, minimale e curato per progetti gestiti da agenti.</strong>
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

The point is not to install every agent, skill, hook, command, and research pipeline on the internet. The point is to preserve the **minimum useful operating system**:

- clear project instructions
- a few focused Codex subagents
- compact repo-local skills
- lightweight Paseo workflow guidance
- explicit rules against duplication and tool sprawl

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
| `.codex/config.toml` | Minimal project-local Codex subagent limits |
| `.codex/agents/` | Five focused Codex subagents |
| `.agents/skills/` | Eight compact repo-local skills |
| `docs/agent-workflows.md` | Practical Paseo playbook |
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
|   |-- agent-workflows.md
|   `-- source-curation.md
|-- .codex/
|   |-- config.toml
|   `-- agents/
|       |-- context_manager.toml
|       |-- debugger.toml
|       |-- docs_researcher.toml
|       |-- reviewer.toml
|       `-- security_auditor.toml
`-- .agents/
    `-- skills/
        |-- frontend-taste/
        |-- planning-contract/
        |-- recent-research/
        |-- repo-discovery/
        |-- security-review/
        |-- systematic-debugging/
        |-- tdd-workflow/
        `-- verification-loop/
```

## Start a New Project

1. **Copy this skeleton** into a fresh repository.
2. **Replace this README** with project-specific product, setup, and run instructions.
3. **Update `AGENTS.md`** with real build, test, lint, deploy, and safety rules.
4. **Keep the agent set small** until repeated work proves a new role is worth it.
5. **Use Paseo deliberately** when a second opinion, committee, handoff, or loop reduces risk.

## Codex Agents

Project-local Codex agents live in `.codex/agents/`.

| Agent | Role | When to Use |
| --- | --- | --- |
| `context_manager` | Scout and cartographer | Build compact repo context before implementation or delegation |
| `docs_researcher` | Scholar | Verify APIs, versions, release notes, and official docs |
| `reviewer` | Shield-bearer | Review diffs for correctness, regressions, security, and missing tests |
| `security_auditor` | Paladin | Inspect auth, secrets, inputs, config, dependencies, and exposure |
| `debugger` | Ranger | Isolate failing tests, runtime traces, and root causes |

These agents are **project-local** and **explicitly invoked**. They are not meant to replace careful repo reading.

## Local Skills

Repo-local skills live in `.agents/skills/`.

| Skill | Use |
| --- | --- |
| `repo-discovery` | First pass through an unfamiliar repo |
| `planning-contract` | Decision-complete plans for risky or multi-step work |
| `verification-loop` | Final checks before declaring work complete |
| `tdd-workflow` | Behavior changes protected by tests |
| `systematic-debugging` | Bugs, failing tests, flakes, and regressions |
| `security-review` | Trust boundaries, secrets, input handling, and unsafe defaults |
| `frontend-taste` | Polished UI, hierarchy, spacing, responsive behavior |
| `recent-research` | Time-sensitive external facts and current community signals |

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

The rule is simple: **import principles, not catalogs**.

If a source contains 200 useful ideas, this repo should still keep only the few that are stable, repeated, and generally useful.

## Non-Goals

- No global Codex configuration
- No tokens, credentials, provider settings, or personal paths
- No large imported skill catalog
- No vendored research engines
- No framework choice before a real project needs one
- No agents that differ only by branding or personality

## Italiano

Questo scheletro e volutamente piccolo ma presentabile: istruzioni operative, pochi agenti Codex, skill essenziali, playbook Paseo e una linea estetica chiara.

La squadra deve rimanere forte perche resta leggera.
