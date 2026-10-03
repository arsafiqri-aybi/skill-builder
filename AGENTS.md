# Agent Guidance

When working in this repository:

- Treat `SKILL.md` as the canonical active runtime behavior.
- Use `references/` for concise operational detail.
- Use `knowledge/README.md` as the retrieval map for deeper knowledge; load only relevant modules.
- Never treat `knowledge/history/` as active runtime instructions.
- Preserve the canonical identity `Skill Builder` / `skill-builder`.
- Treat `vendor/openai-skill-creator/` as an upstream snapshot, not as the canonical Skill Builder runtime. Preserve its license and provenance; do not silently edit vendored files.
- Use `references/skill-creator-integration.md` to decide between a host-provided creator and the vendored fallback.
- Run `python scripts/audit_skill.py . --portable`, `python vendor/openai-skill-creator/scripts/quick_validate.py .`, and `python scripts/test_audit_skill.py` after structural or tooling changes.
- Do not claim host installation or automatic-trigger behavior unless actually verified in that host.
- Do not add secrets, tokens, credentials, private memory, or unrelated project state to this repository.
