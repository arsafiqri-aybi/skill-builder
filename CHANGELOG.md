# Changelog

## Initial canonical migration — 2026-10-03

- Established the canonical identity **Skill Builder** with runtime identifier `skill-builder`.
- Migrated runtime instructions, host metadata, references, audit tooling, tests, and icon assets.
- Converted the research knowledge base into modular retrieval-friendly files.
- Added explicit authority ordering between runtime instructions, references, knowledge, and historical provenance.
- Added repository-level architecture, maintenance guidance, verification status, and CI validation.

## Integrated authoring — 2026-10-03

- Merged skill-authoring capabilities directly into Skill Builder.
- Added native scaffold, metadata generation, unified validation, and dedicated tooling regression tests.
- Integrated progressive disclosure, resource selection, authoring lifecycle, and acceptance-floor guidance into the existing runtime, references, and knowledge base.
- Removed the separate vendored creator layer so Skill Builder operates under one runtime identity and one repository architecture.
- Host-native builders and validators remain optional compatibility checks, not dependencies.

Future changes are tracked by Git history and may be summarized here without numbered release labels.
