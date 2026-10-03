# Repository Architecture

Skill Builder is stored as one capability repo: runtime Skill + supporting knowledge + references + deterministic tooling + evaluation.

```text
skill-builder/
├── SKILL.md                  # canonical runtime instructions
├── agents/openai.yaml        # host-facing display metadata
├── assets/                   # reusable UI/output assets
├── references/               # concise operational references
├── knowledge/                # deeper modular knowledge base
│   └── history/              # provenance only, never runtime authority
├── scripts/                  # deterministic audit tooling + regression tests
├── evaluation/               # verification status and test guidance
├── scripts/
│   ├── init_skill.py          # scaffold generator
│   ├── build_metadata.py      # metadata generator
│   ├── validate_skill.py      # validation entry point
│   └── audit/test tooling
├── docs/                     # repository architecture and maintenance
├── .github/workflows/        # automated validation
└── README.md
```

## Authority order inside this repository

1. `SKILL.md` — active runtime behavior.
2. `references/` — operational detail explicitly linked from the Skill.
3. `knowledge/` — deeper design knowledge and source context.
4. `knowledge/history/` — historical provenance only.

No file in this repository grants additional account permissions, tools, credentials, or platform capabilities.


## Integrated authoring layer

Skill Builder owns its authoring lifecycle directly. Design knowledge, scaffolding, metadata generation, static validation, evaluation guidance, repair logic, and packaging decisions live in this repository under one runtime identity. Platform-native tooling can supplement compatibility checks but is not an architectural dependency.
