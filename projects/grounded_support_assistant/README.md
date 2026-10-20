# Employee policy assistant: learner-owned project

## S0 briefing

You are the junior AI engineer helping the employee help desk at the fictional
Nilebyte Solutions. An employee needs the right published rule and a source they
can check. A wrong deadline can cause lost leave or an invalid request. Your first
job is to explain the problem and identify what evidence supports an answer.

The [single plan](../../docs/learning-path/02-PROJECT-ROADMAP.md) owns acceptance.
Read S0 and the first unresolved capability from [the state](../../LEARNING.md).
No provider, new dependency, model download, private codebase or implementation task
is needed to start. Configuration support notes are preserved for S2, not an S0 gate.

Use passage `pf-leave-carryover` in [the starter fixture](data/starter-corpus.json):
Leave Policy HR-LV-01, version 2026.1, section 2.6, at fixture date 2026-09-24.
The tutor shows its approved excerpt, frames the employee's risk and asks one action,
then waits. Later S0 traces a manual source-based answer path and distinguishes it
from software execution. Do not open every development answer to begin tutoring.

## What exists and what remains learner work

Nine supplied English passages from three policy families and twelve exposed
[development cases](eval/starter-dev-cases.json) support the initial releases.
They are not unseen assessment or evidence of learner authorship. The HR retrieval,
model boundary and later ingestion/agent modules remain learner implementation work.
No complete active solution is supplied by this preparation.

`app.py` and `data/handbook.md` are the older inherited lexical reference: token-overlap
ranking with source citations/abstention. Its twenty original cases include a known
paraphrase failure; four challenge cases are also strict expected failures. It is
not the new HR pipeline or evidence that the learner built a RAG system. A returned
section/citation cannot establish support for every requested claim.

```powershell
uv run python scripts/check_s0_readiness.py
uv run python scripts/learning_state.py status
```

If explicitly inspecting the reference: run `uv run python
projects/grounded_support_assistant/app.py "How long is an export link valid?"`.
Label the domain and inherited status; do not make this a private/provider prerequisite.

## Growth and trust

S1 integrates library-based lexical search; S2 connects retrieved evidence to a
validated fake/live model boundary; S3 adds semantic retrieval and real ingestion;
S4 tests applicability, security, conversation and measured improvement; S5 adds
fake authenticated lookups/drafts; S6 defends a reproducible integrated local release.
Full-route completion still includes S5/S6 even though useful RAG arrives earlier.

Use the starter safe allowlist until expanded eligibility is implemented before
ranking/top-k. A model cannot grant permissions or approve a request. Later actions
separate draft, employee confirmation and manager approval bound to exact arguments;
replay, changed targets and unknown outcomes must be handled. Real integrations and
private Mushir changes remain separately scoped. model/ is a dormant optional shelf.
