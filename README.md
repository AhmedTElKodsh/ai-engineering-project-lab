# Problem-first RAG Workbench

Build one employee-policy assistant as its users' problems grow. You write the
important implementation; the AI tutors one meaningful action at a time.

Start with the [single project plan](docs/learning-path/02-PROJECT-ROADMAP.md),
[current checkpoint](LEARNING.md), and [project briefing](projects/grounded_support_assistant/README.md).
Use `$project-mentor` to resume. S0 needs no provider account, model download or
private checkout. It begins with an employee question and one approved policy excerpt.

## Progression

S0 understand the problem/source boundary → S1 find a cited passage → S2 answer from
retrieved evidence → S3 handle different wording and document formats → S4 applicable
rules, conversation and measured improvements → S5 authenticated tools and safe drafts
→ S6 reproduce and defend the integrated local release.

The [route](learning/route.json) owns IDs, dependencies, capability IDs, effort and
assessment blockers. Five two-hour sessions weekly, CPU first. Stage ranges are
provisional, not demonstrated pace. Learner progress remains unresolved until actual
observations qualify. Preparation, passing maintenance tests and supplied fixtures
never award competence. S0 supported practice can begin; the actual mentor-host
behavioral pilot remains required before its first mastery decision.

```powershell
uv sync --locked --all-groups
uv run python scripts/learning_state.py status
uv run python scripts/check_s0_readiness.py
```

## Working surfaces

- `projects/grounded_support_assistant/`: learner-owned project; the existing lexical
  handbook app remains an inherited reference, not the newly implemented HR system.
- `projects/grounded_support_assistant/data/starter-corpus.json`: nine supplied policy
  passages; development-only cases are under `eval/starter-dev-cases.json`.
- `resources/corpora/hr-policy/`: full synthetic HR data for later expansion.
- `learning/`: one append-only evidence history and derived views.
- `archive/planning/2026-10-20/`: superseded proposals, route documents and reviews,
  preserved with original-path hashes. They never override the current plan.
- `resources/labs/`, `resources/from-scratch-lessons/`, `explorations/`: optional
  references/side quests with no automatic stage credit.

Mushir stays private. S1–S6 apply relevant mechanisms in its own authorized checkout;
no private corpus/AAOIFI text enters this public repository. S0 uses a local fallback.
See [AGENTS.md](AGENTS.md), [project context](project-context.md),
[evidence protocol](learning/PROTOCOL.md) and [tooling](TOOLING.md).
