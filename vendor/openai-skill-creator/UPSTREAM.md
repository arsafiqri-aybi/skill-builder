# OpenAI Skill Creator upstream snapshot

This directory vendors the official OpenAI `skill-creator` source so Skill Builder can retain platform-native authoring guidance even on hosts where `@skill-creator` or `$skill-creator` is unavailable.

- Upstream repository: `openai/skills`
- Upstream path: `skills/.system/skill-creator/`
- Snapshot commit: `49f948faa9258a0c61caceaf225e179651397431`
- License: Apache License 2.0; see `LICENSE.txt`.
- Vendored files are kept separate from Skill Builder's own runtime so upstream provenance stays clear.

## Update rule

When refreshing this snapshot, compare the upstream directory at a specific commit, copy the upstream files without silently rewriting them, preserve the license, update the snapshot commit above, then rerun Skill Builder validation and regression tests.

Skill Builder may summarize or operationalize upstream guidance in its own files, but the vendored directory remains an identifiable upstream snapshot.
