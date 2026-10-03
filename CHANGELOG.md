# Changelog

## Initial canonical migration — 2026-10-03

- Established the canonical identity **Skill Builder** with runtime identifier `skill-builder`.
- Migrated runtime instructions, host metadata, references, audit tooling, tests, and icon assets.
- Converted the research knowledge base into modular retrieval-friendly files.
- Added explicit authority ordering between runtime instructions, references, knowledge, and historical provenance.
- Added repository-level architecture, maintenance guidance, verification status, and CI validation.

## OpenAI Skill Creator integration — 2026-10-03

- Vendored the official OpenAI `skill-creator` source under `vendor/openai-skill-creator/`.
- Preserved the upstream Apache-2.0 license and recorded the exact upstream commit.
- Made the official creator an optional accelerator rather than a hard dependency.
- Added a self-contained fallback path for hosts where `@skill-creator` or `$skill-creator` is unavailable.
- Added the official upstream quick validator to CI alongside Skill Builder's own audit and regression suite.

Future changes are tracked by Git history and may be summarized here without numbered release labels.
