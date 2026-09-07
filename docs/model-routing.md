# Astra, Sol, Terra, and Luna Model Routing

This repository assigns explicit models to custom Codex agents so copied projects have predictable defaults. The routing follows current OpenAI guidance as verified on 2026-09-05.

## Official model roles

- `gpt-6-astra`: most capable model for the hardest complete workflows across multiple steps and tools.
- `gpt-5.6-sol`: model for complex, open-ended work that needs deeper analysis, judgment, or polish.
- `gpt-5.6-terra`: balanced everyday model for strong reasoning and tool use, including exploration, read-heavy scans, and supporting parallel work.
- `gpt-5.6-luna`: fast, low-cost model for clear, narrow, repeatable, or high-volume tasks with an explicit definition of done.

GPT-6 Astra supports `low`, `medium`, `high`, `xhigh`, and `max`; it does not support `none`. This starter keeps `low`, `medium`, and `high` in custom agents because those levels cover its roles without making maximum-effort execution a standing default.

## Repo assignment

The main Codex agent uses `gpt-6-astra` with explicit `low` reasoning in `.codex/config.toml`. The five complex specialist roles retain Sol and their existing reasoning levels. Terra and Luna remain the lower-cost tiers. This assignment is a project choice informed by OpenAI guidance, which continues to recommend all four models; it is not an OpenAI requirement to replace Sol.

| Model | Agents | Why |
| --- | --- | --- |
| `gpt-5.6-sol` | `architect`, `database_reviewer`, `debugger`, `reviewer`, `security_auditor` | These roles handle ambiguous cross-cutting decisions or high-impact correctness and security analysis. |
| `gpt-5.6-terra` | `accessibility_tester`, `backend_developer`, `context_manager`, `dependency_reviewer`, `devops_engineer`, `docs_researcher`, `eval_engineer`, `frontend_developer`, `performance_optimizer`, `product_manager`, `react_reviewer`, `technical_writer`, `typescript_reviewer`, `ux_researcher` | These are bounded specialist tasks that still require dependable reasoning, tool use, or synthesis. |
| `gpt-5.6-luna` | `evidence_collector`, `minimal_change_engineer`, `test_automator` | These roles are deliberately narrow, repeatable, and governed by concrete evidence or acceptance criteria. |

Reasoning effort remains role-specific. Start from the configured level and raise it only when task complexity or failed verification justifies the added latency and usage.

## Selection rules

1. Prefer the agent's checked-in model for normal use.
2. Escalate a Terra or Luna task to Sol when the scope becomes ambiguous, cross-cutting, security-sensitive, or difficult to verify. Select Astra for specialist tasks that need the strongest capability across a sustained workflow with multiple steps and tools.
3. Move work toward Luna only when the prompt has a narrow scope, deterministic inputs, and a concrete output contract.
4. Do not use model count as a reason to delegate. First decide whether specialization or parallelism improves the outcome.
5. Recheck official documentation before changing model IDs, reasoning levels, or retirement guidance.

## Official sources

- [Codex models and Astra/Sol/Terra/Luna selection](https://learn.chatgpt.com/docs/models#recommended-models)
- [Codex subagent model and reasoning guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents#choosing-models-and-reasoning)
- [GPT-5.6 Sol API model page](https://developers.openai.com/api/docs/models/gpt-5.6-sol)
- [GPT-6 Astra API model page](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [GPT-5.6 Terra API model page](https://developers.openai.com/api/docs/models/gpt-5.6-terra)
- [GPT-5.6 Luna API model page](https://developers.openai.com/api/docs/models/gpt-5.6-luna)

The Codex model page also says GPT-5.4 and GPT-5.4 mini retire from Codex with ChatGPT sign-in on 2026-08-31 and recommends replacing them with Terra and Luna respectively. API-key-authenticated Codex and the OpenAI API are not affected by that retirement.

## Migration compatibility

Verified against the [Astra migration and prompting guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#migration-quickstart). This starter has no application API calls or sampling parameters to migrate. Existing instructions already bound delegation, verification, and response length, so role prompts are preserved.

Astra tool calling requires the Responses API and rejects custom `temperature`, `top_p`, and log probabilities. Availability depends on the Codex client, account, and rollout; the Codex model page currently lists Astra as unavailable in Codex cloud. Validate access in a new local Codex session before adopting this starter. This migration does not change agent sandbox permissions or enable experimental features.
