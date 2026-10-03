# Skill Creator integration

Skill Builder is self-contained. The official OpenAI `skill-creator` is an optional platform-native accelerator, not a hard dependency.

## Runtime selection

1. If the host exposes the official `skill-creator`, use it for host-specific scaffolding, metadata generation, and validation where appropriate.
2. If it is not exposed, use the vendored snapshot in `../vendor/openai-skill-creator/` as the platform-authoring reference and use its deterministic scripts when the environment can execute them.
3. In either case, Skill Builder remains responsible for task contract, trigger and boundary design, knowledge architecture, evaluation design, regression awareness, migration/repair, and evidence-based completion.
4. Host permissions still govern installation, persistence, external actions, and available tools. Vendoring the creator does not grant capabilities that the host does not expose.

## Vendored components

- `vendor/openai-skill-creator/SKILL.md` — upstream authoring guidance.
- `vendor/openai-skill-creator/references/openai_yaml.md` — upstream UI metadata guidance.
- `vendor/openai-skill-creator/scripts/init_skill.py` — upstream scaffold generator.
- `vendor/openai-skill-creator/scripts/generate_openai_yaml.py` — upstream metadata generator.
- `vendor/openai-skill-creator/scripts/quick_validate.py` — upstream lightweight validator.
- `vendor/openai-skill-creator/LICENSE.txt` and `UPSTREAM.md` — license and provenance.

Load the vendored `SKILL.md` only when creating/updating a Skill or when platform-format details matter. Do not load it for ordinary target-domain execution.
