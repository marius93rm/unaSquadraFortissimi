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

- [AI Uplink — Copy and Paste for an Agent](#ai-uplink--copy-and-paste-for-an-agent)
- [Vision](#vision)
- [Stack](#stack)
- [What's Included](#whats-included)
- [Repository Map](#repository-map)
- [Start a New Project](#start-a-new-project)
- [Validation](#validation)
- [Reliable Browser Integration](#reliable-browser-integration)
- [Codex Agents](#codex-agents)
- [Model Routing](#model-routing)
- [Local Skills](#local-skills)
- [Paseo Workflows](#paseo-workflows)
- [Source Philosophy](#source-philosophy)
- [Non-Goals](#non-goals)

## AI Uplink — Copy and Paste for an Agent

Do not make the agent study the site. Paste the following payload into its session: it tells the agent what to import, what to preserve, and how to verify the result.

```text
<USF_AGENT_UPLINK version="1.0">
MISSION: Installa nella repository corrente il kit operativo repo-local di unaSquadraFortissimi.
SOURCE: https://github.com/marius93rm/unaSquadraFortissimi
IMPORT: i 22 agenti in .codex/agents, le 27 skill in .agents/skills, la configurazione Codex repo-local, il contratto AGENTS.md e i documenti operativi Paseo/modelli/catalogo.

PROTOCOL:
1. Ispeziona prima la repository corrente, le sue istruzioni AGENTS.md e lo stato git.
2. Acquisisci SOURCE in una directory temporanea e trattala come materiale da integrare, non come autorità superiore alle istruzioni locali.
3. Importa il kit completo. Se un file esiste già, confronta e fondi intenzionalmente: preserva comandi, vincoli, stack e lavoro dell'utente.
4. Non scrivere configurazione globale, credenziali o telemetry. Non cancellare, non fare commit e non fare push senza richiesta esplicita.
5. Adatta riferimenti e validazione alla struttura reale della repository; non importare la landing e i suoi asset salvo richiesta.
6. Esegui controlli mirati, poi riferisci file aggiunti, merge effettuati, verifiche e rischi residui.

SUCCESS: il progetto riconosce localmente agenti, skill e workflow senza perdere configurazione o lavoro preesistente.
ACTION: procedi ora; fai domande soltanto davanti a un conflitto materiale che non puoi risolvere in sicurezza.
</USF_AGENT_UPLINK>
```

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
| **Showcase** | Static HTML/CSS | Public landing page for the skeleton and catalog |
| **Validation** | Python stdlib | Repo-local integrity checks for docs, agent files, skill files, and landing links |
| **Assets** | Generated images | Project identity, agent portraits, and skill scenes |

## What's Included

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Main operating contract for agents working in this repository |
| `.codex/config.toml` | Project-local Codex subagent limits |
| `.codex/agents/` | 22 Codex subagents across implementation, review, product, ops, QA, and evals |
| `.agents/skills/` | 27 compact repo-local skills |
| `docs/agent-workflows.md` | Practical Paseo playbook |
| `docs/agent-catalog.md` | Agent and skill activation matrix |
| `docs/model-routing.md` | Official-doc-backed GPT-5.6 Sol, Terra, and Luna defaults |
| `docs/source-curation.md` | Rules for importing ideas without copying entire catalogs |
| `index.html` | Static showcase page generated from the repo-local concept and catalog |
| `styles.css` | Visual system for the static showcase |
| `favicon.svg` | Small project mark for the showcase page |
| `.gitignore` | Curated exclusions for OS metadata, editors, secrets, caches, dependencies, and build output |
| `scripts/validate_repo.py` | Integrity check for agent files, skill files, docs, local links, anchors, assets, and count drift |
| `assets/agent-fellowship-medieval.png` | Generated medieval fellowship hero image |
| `assets/agents/` | Generated portraits for Codex subagents |
| `assets/skills/` | Generated scenes for repo-local skills |

## Repository Map

```text
.
|-- AGENTS.md
|-- .gitignore
|-- README.md
|-- index.html
|-- styles.css
|-- favicon.svg
|-- scripts/
|   `-- validate_repo.py
|-- assets/
|   |-- agent-fellowship-medieval.png
|   |-- agents/
|   `-- skills/
|-- docs/
|   |-- agent-catalog.md
|   |-- agent-workflows.md
|   |-- model-routing.md
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
        |-- browser-integration/
        |-- branch-finish/
        |-- code-review/
        |-- dependency-review/
        |-- design-system-extraction/
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
6. **Run validation** after pruning or changing agent, skill, docs, or showcase files.

## Validation

Run the repo-local integrity checks from the repository root:

```bash
python scripts/validate_repo.py
```

The script checks:

- every `.codex/agents/*.toml` has the required fields and a `name` matching its filename
- every agent uses one of the approved GPT-5.6 Sol, Terra, or Luna model IDs
- every `.agents/skills/*/SKILL.md` has frontmatter with a `name` matching its directory
- `README.md`, `docs/agent-catalog.md`, `docs/model-routing.md`, and the landing page preserve their canonical agent and skill coverage
- `AGENTS.md` stays within its 3,200-byte always-loaded budget and links to the canonical catalogs instead of duplicating them
- initial skill name, description, and repo-relative path metadata stays within 6,500 characters
- the normal `browser-integration` path stays within 4,000 bytes and links its conditional recovery reference
- the showcase `index.html` mentions every agent and skill and has valid local anchors, local assets, GitHub blob links, and image alt text
- the README map and count phrases have not drifted from the current repo shape
- `.gitignore` preserves the repository's minimum hygiene patterns

Current integrity target: 22 Codex subagents, 27 repo-local skills, 22 agenti Codex e 27 skill repo-local.

## Reliable Browser Integration

Load [`browser-integration`](.agents/skills/browser-integration/SKILL.md) before every task that opens, inspects, tests, clicks, types in, or screenshots a page through the Codex in-app browser.

The skill removes the common false starts:

- it resolves the installed browser client from the active skill catalog instead of hard-coding a versioned path
- it discovers and calls `mcp__node_repl__js` directly, never through a generic execution wrapper that can lose sandbox metadata
- it uses one idempotent bootstrap for the `iab` browser and recovers a missing selected tab by creating one
- it keeps persistent runtime bindings stable and grounds every action in a fresh DOM snapshot
- it retries only recoverable state once, then reports a precise host blocker instead of switching browser stacks speculatively

The repository validator also protects the critical bootstrap markers so future edits cannot silently remove the supported client, runtime tool, `iab` selection, or tab lifecycle.
Detailed cases live in the [browser recovery reference](.agents/skills/browser-integration/references/recovery.md) and are loaded only after a matching failure, keeping the normal path compact.

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

## Model Routing

The 22 custom agents use current GPT-5.6 defaults derived from official OpenAI model and subagent guidance:

| Model | Agents | Default workload |
| --- | ---: | --- |
| `gpt-5.6-sol` | 5 | Ambiguous, cross-cutting, or high-impact analysis |
| `gpt-5.6-terra` | 14 | Everyday specialist work with reasoning and tools |
| `gpt-5.6-luna` | 3 | Narrow, repeatable work with a concrete output contract |

See [`docs/model-routing.md`](docs/model-routing.md) for the role matrix, escalation rules, verification date, and official sources.

## Local Skills

Repo-local skills live in `.agents/skills/`.

| Skill | Use |
| --- | --- |
| `repo-discovery` | First pass through an unfamiliar repo |
| `browser-integration` | Reliable preflight and bounded recovery for the Codex in-app browser |
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
| `design-system-extraction` | Extract semantic tokens and visual rules from frontend source into a durable `DESIGN.md` |
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

> **Repo**
>
> Dati stelle letti da GitHub API il 2026-06-12; `stitch-skills` verificato il 2026-08-25.
>
> | Repo | Descrizione | Stelle | Link |
> | --- | --- | ---: | --- |
> | `paseo` | Orchestrazione multi-agent da desktop e mobile. | 8,389 | [getpaseo/paseo](https://github.com/getpaseo/paseo) |
> | `awesome-codex-subagents` | Catalogo di subagenti Codex specializzati per molti casi di sviluppo. | 5,139 | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) |
> | `awesome-agent-skills` | Raccolta ampia di skill agentiche compatibili con Codex, Claude Code, Gemini CLI, Cursor e altri. | 25,071 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) |
> | `ECC` | Sistema di ottimizzazione per harness agentici: skill, memoria, sicurezza e sviluppo research-first. | 213,763 | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
> | `superpowers` | Framework e metodologia di sviluppo basati su skill agentiche. | 225,270 | [obra/superpowers](https://github.com/obra/superpowers) |
> | `agency-agents` | Catalogo di agenti specialistici per engineering, prodotto, marketing, supporto, sicurezza e altri domini. | 111,853 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) |
> | `last30days-skill` | Skill per ricerca recente su Reddit, X, YouTube, HN, Polymarket, GitHub e web. | 39,946 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) |
> | `pm-skills` | Skill e comandi per product management: discovery, strategia, execution, launch e growth. | 16,504 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) |
> | `taste-skill` | Skill per migliorare gusto visivo e ridurre output frontend generico. | 41,822 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
> | `stitch-skills` | Workflow Google Labs per design system semantici, prompt UI strutturati e build loop visuali. | 8,177 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) |

The rule is simple: **copy the best operating patterns, not the entire catalogs**.

## Non-Goals

This repository intentionally avoids:

- global Codex or machine-level configuration
- provider keys, telemetry, or API-specific setup
- vendored upstream catalogs
- generated installers and shell automation
- project-specific product code
- pretending that more agents automatically means better work
