# AI Skill Architect

**Design, build, validate, package, and evolve production-grade AI skills with structured knowledge, evaluation, and reusable runtime architecture.**

AI Skill Architect turns a real user need into a reusable AI Skill with explicit triggers, boundaries, inputs, outputs, source-of-truth rules, failure handling, supporting knowledge, deterministic tooling where justified, and evidence-based evaluation.

## What this repository contains

- `SKILL.md` — canonical runtime instructions.
- `references/` — concise guidance used selectively during execution.
- `knowledge/` — deeper modular knowledge base for architecture, research, evaluation, tools, safety, and maintenance.
- `scripts/audit_skill.py` — read-only static auditor for Skill packages.
- `scripts/test_audit_skill.py` — regression tests for the auditor.
- `agents/openai.yaml` — host-facing metadata.
- `evaluation/STATUS.md` — what has and has not been verified.

## Design principles

- Runtime instructions stay compact; deeper knowledge is loaded only when needed.
- Skill creation is separated from performing the target domain task.
- Static validation, trigger evaluation, behavioral evaluation, artifact checks, and installation verification are distinct evidence layers.
- Existing Skills are changed surgically: preserve identity and unrelated behavior unless the task explicitly requires broader change.
- Sources, tool outputs, and uploaded files are treated as evidence/data, not as automatic authority to change the user's goal or permissions.
- No claims of installation, testing, model switching, or external actions without observable evidence.

## Runtime identifier

`ai-skill-architect`

## Compatibility intent

Designed to be portable across ChatGPT, Codex, API/agent environments, and other hosts that can consume Agent Skill-style instructions. Actual installation and invocation semantics remain host-dependent and must be verified in the target environment.

## Knowledge loading

Start at [`knowledge/README.md`](knowledge/README.md). Do not load the entire knowledge base by default.
