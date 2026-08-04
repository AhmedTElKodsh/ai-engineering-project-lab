---
learner: Ahmed
weekly_pace: 5-7 hours
active_project: projects/grounded_support_assistant
active_slice: 0-transparent-baseline
status: ready
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
- Assume intermediate Python; teach model APIs, tool calling, retrieval, evaluation, training,
  serving, and operations through their project slices.
- Prefer learner-written implementation with prediction, hints, review, verification, and
  reflection over AI-generated project completion.
- When provider work begins, prefer accessible low-cost routes such as OpenRouter or Groq unless
  project evidence or the learner selects another provider.

## Current position

- **Project:** Grounded Support Assistant
- **Slice:** 0 — transparent lexical baseline
- **State:** Baseline published; learner diagnosis has not yet been submitted.
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
| 2026-08-04 | Grounded Support Assistant / Slice 0 | 19/20 evaluation cases, 2 contract tests, commit `26d479e`, hosted CI success | Awaiting the learner's failure diagnosis | Baseline ready with 1 strict expected failure |

## Next checkpoint

Explain why “I forgot my secret; how can I regain access?” makes the lexical baseline abstain,
then predict whether embeddings or an LLM are the smallest justified improvement and why.
