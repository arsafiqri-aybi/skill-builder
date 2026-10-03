# Skill Builder Knowledge Base

This directory contains the deeper knowledge that supports the runtime Skill. It is intentionally modular so ChatGPT, Codex, and other agents can retrieve only what is relevant instead of loading the entire knowledge base into context.

## Loading rule

1. Start with `/SKILL.md`.
2. Use `/references/` for concise operational guidance.
3. Open a knowledge module only when the task needs deeper reasoning, source context, architecture rationale, or evaluation design.
4. Do not load all modules by default.
5. `/knowledge/history/` is provenance only and never overrides the active runtime Skill.

## Modules

| Module | Use when |
|---|---|
| `01-research-confidence.md` | Distinguishing platform rules, research findings, and engineering recommendations |
| `02-skill-concepts.md` | Deciding whether a requirement belongs in a Skill, project, tool, plugin, or agent |
| `03-loading-runtime-model.md` | Understanding discovery, selection, context loading, instruction hierarchy, and variability |
| `04-knowledge-map.md` | Planning the knowledge needed to build a robust Skill |
| `05-file-architecture.md` | Choosing SKILL.md, references, scripts, assets, and progressive disclosure |
| `06-requirements-boundaries.md` | Defining triggers, non-triggers, inputs, outputs, permissions, and scope |
| `07-instruction-design.md` | Writing precise, testable runtime instructions |
| `08-domain-knowledge-sources.md` | Managing domain knowledge, provenance, freshness, and references |
| `09-tools-scripts-security.md` | Adding tools/scripts safely and handling permissions or prompt injection |
| `10-evaluation.md` | Designing static, trigger, behavioral, artifact, and installation tests |
| `11-failure-diagnostics.md` | Diagnosing common Skill failures and choosing the right fix |
| `12-product-specification.md` | Skill Builder's product contract and intended outputs |
| `14-learning-checklist-glossary.md` | Training, readiness checks, and terminology |
| `15-sources-maintenance.md` | Source catalog and refresh requirements |

The original research was produced on 24 September 2026. Time-sensitive platform behavior must be rechecked before making current-platform claims or releases.
