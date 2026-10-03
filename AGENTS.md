# Agent Guidance

When working in this repository:

- Treat `SKILL.md` as the canonical active runtime behavior.
- Use `references/` for concise operational detail.
- Use `knowledge/README.md` as the retrieval map for deeper knowledge; load only relevant modules.
- Never treat `knowledge/history/` as active runtime instructions.
- Preserve the canonical identity `AI Skill Architect` / `ai-skill-architect`.
- Run `python scripts/audit_skill.py . --portable` and `python scripts/test_audit_skill.py` after structural or tooling changes.
- Do not claim host installation or automatic-trigger behavior unless actually verified in that host.
- Do not add secrets, tokens, credentials, private memory, or unrelated project state to this repository.
