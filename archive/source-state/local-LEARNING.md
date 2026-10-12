---
learner: Ahmed
weekly_pace: 5-7 hours
active_project: projects/grounded_support_assistant
active_slice: 0-transparent-baseline
active_checkpoint: quest-orientation
status: in_progress
last_verified_code_commit: 26d479e550a0918a592a138592f81146e8db66e5
---

# Learning State

This file is the resumable state for `$project-mentor`. It records completed evidence and one
next checkpoint; project specifications remain in their project README.

## Mission and learner profile

- Become job-ready as an AI engineer by building and defending recurring real-world project
  cases, not by collecting framework tutorials.
- Practice common tools deeply enough to configure, debug, evaluate, compare, and explain when
  not to use them.
- Learn theory just in time and only to the depth required by the current engineering decision.
- Work at roughly 5–7 focused hours per week.
- Treat Python experience and AI-engineering familiarity separately. Introduce AI-engineering
  ideas in plain language until the learner demonstrates the relevant vocabulary and mental
  model.
- Prefer learner-written implementation with prediction, hints, review, verification, and
  reflection over AI-generated project completion.
- When provider work begins, prefer accessible low-cost routes such as OpenRouter or Groq unless
  project evidence or the learner selects another provider.

## Current position

- **Project:** Grounded Support Assistant
- **Slice:** 0 — inherited transparent baseline
- **Checkpoint:** Quest orientation
- **State:** An inherited baseline is published, but the learner has not yet completed the
  project briefing or demonstrated its purpose and success conditions.
- **Learner familiarity:** Project context and AI-engineering vocabulary are unassessed. Begin
  in plain language and introduce one necessary term at a time.
- **Demonstrated understanding:** None yet.
- **Support needed:** In the configuration-test detour, distinguish exact Python/Pydantic
  identifiers and case-sensitive text: `_env_file` is valid, `_get_file` is not, and
  `"Field required"` does not equal `"field required"`. In the Groq model-call detour,
  distinguish a client library from its exact provider-owned model IDs and verify current IDs
  against the provider catalog before rebuilding the container. Also distinguish a `.env` file
  from the running process environment: load it explicitly before reading `GROQ_API_KEY` from
  `os.environ`.
- **Known limitation:** Exact-token retrieval misses the semantic paraphrase case and produces
  one strict expected failure.
- **Blocker:** None.

## Latest verified evidence

| Date | Proof | Tree/commit | Command or run | Result |
|---|---|---|---|---|
| 2026-08-04 | Local | `26d479e` | `uv lock --check`; Ruff; `uv run pytest -rxX -q`; CLI query | 19/20 evaluation cases passed; 1 strict expected failure; 2 contract tests passed; lint, format, lock, and CLI succeeded |
| 2026-08-04 | Hosted CI | `26d479e` | [GitHub Actions run 30909751250](https://github.com/AhmedTElKodsh/ai-engineering-project-lab/actions/runs/30909751250) | Success |

## Decisions carried forward

- Keep this portfolio lab separate from the from-scratch curriculum.
- Use AI Engineering Hub as an MIT-licensed idea catalogue; copy no code, prose, notebooks, or
  assets without explicit attribution and licence handling.
- Start every case with a transparent baseline and fixed evaluation.
- Use two framework gates: measured gaps for production adoption and bounded roadmap exercises
  for learning comparisons.
- Treat local, CI, live-provider, GPU, deployment, and production evidence as different claims.
- Preserve learner ownership and require runtime evidence before mastery or completion claims.

## Progress log

| Date | Project/slice | Evidence | Learner note | Outcome |
|---|---|---|---|---|
| 2026-08-04 | Grounded Support Assistant / reference baseline | 19/20 evaluation cases, 2 contract tests, commit `26d479e`, hosted CI success | No learner comprehension evidence yet | Inherited baseline ready; quest orientation pending |

## Next checkpoint

After a plain-language project quest briefing, explain why the support assistant should refuse to
answer when the approved handbook does not contain the answer. No coding or AI vocabulary is
required yet.
