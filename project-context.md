# Implementation and document authority

The product is the Problem-first RAG Workbench. The active project is
projects/grounded_support_assistant. Its existing lexical handbook app is inherited
reference code; the learner has not implemented the new HR retrieval/generation
pipeline. Supplied starter JSON is practice data, not parser/chunker or learner proof.

## Owners

- docs/learning-path/02-PROJECT-ROADMAP.md: the single active plan, detailed stage
  acceptance, library placement, data/eval rules and remaining maintenance backlog.
- learning/route.json: S0–S6 IDs/dependencies, stable capability IDs, assessment
  blockers, current contract references, pace/compute and provisional effort.
- AGENTS.md and .agents/skills/project-mentor/SKILL.md: agreement and single tutor.
- learning/PROTOCOL.md: factual record schema and qualification/persistence policy.
- learning/evidence.jsonl: append-only observations; LEARNING.md/state.json are derived.
- Project README: current implementation claims and the local S0 briefing.
- docs/maintenance/: dated maintainer verification, never learner progress or a plan.
- archive/: immutable historical plans/research/reviews, not current instruction.

S0 needs no private checkout/provider. S1–S6 apply relevant mechanisms in Mushir's
own authorized checkout; private code/corpus and AAOIFI text stay there. Optional
from-scratch resources remain dormant, with no second mutable route or tutor.

## Check a maintenance candidate

Python 3.12 is canonical; pyproject.toml's broader floor is not verified here.
Stage libraries enter only when their stage starts; default imports/tests do not
call providers or download models. Retain pinned GitHub Actions.

```powershell
uv sync --locked --all-groups
uv run python scripts/check_mentor_contract.py
uv run python scripts/check_s0_readiness.py
uv run ruff check .
uv run ruff format --check .
uv run pytest -rxX -q
```

These checks establish structural/local behavior only. An actual mentor-host pilot,
learner independence, retained mastery, live-provider and deployment proof are separate.
The route keeps pending assessment prerequisites visible; supported practice may begin.

## Engineering boundaries

Validate typed inputs/outputs. Select eligible role/region/date/version sources before
ranking/top-k, model context or external traces. Source offsets in str are Unicode
code-point indices; byte spans require declared conversion. A citation does not prove
entailment. Use deterministic fake providers/tools, total time/retry/token/step limits
and meaningful negative controls. Serialize before atomic file replacement. External
writes require deterministic authorization, idempotency and reconciliation after an
unknown outcome; model text is never authority. No real external effect is a baseline.

Preserve unrelated local work, test scaffolds and secrets. Current APIs/model IDs
must be verified in official docs when used. No secret appears in chat, traces or
progress records. Archive operations must stay within verified repository paths.
