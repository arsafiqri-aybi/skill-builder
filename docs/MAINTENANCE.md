# Maintenance

## Change workflow

1. Identify the observed failure or required capability change.
2. Decide whether the fix belongs in metadata, `SKILL.md`, references, knowledge, scripts, or tests.
3. Update the smallest authoritative layer that solves the issue.
4. Run static audit and regression tests.
5. For behavior or trigger changes, run representative positive, negative, and edge tests in a fresh context when the host supports it.
6. Record material changes in `CHANGELOG.md`; Git history is the canonical change record.

## Knowledge refresh

Platform-sensitive claims must be rechecked against current authoritative documentation before release. Research findings should retain population/model/task limitations rather than being promoted to universal rules.

## Naming

The canonical identity is **AI Skill Architect** and the runtime identifier is **`ai-skill-architect`**. Active files should use only this identity.
