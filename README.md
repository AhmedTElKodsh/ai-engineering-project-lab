# AI Engineering Workbench

One cumulative, learner-owned project: grow a grounded support assistant from intermediate Python into evaluated RAG and bounded agents, then build its small language-model laboratory from raw math and random weights.

**Pace:** two hours/day, five days/week. **Required hardware:** CPU. The GTX 1050 Ti is optional and unverified. **Current learner state:** S0 unresolved; no new competence is awarded by repository consolidation.

Start with the [project plan](docs/learning-path/00-START-HERE.md), [current checkpoint](LEARNING.md), and [project quest](projects/grounded_support_assistant/README.md). Ask `$project-mentor` to resume one meaningful action at a time. The assistant and model laboratory are components of this same workbench, sharing data provenance, interfaces and evaluation discipline.

## The route

| Stage | Cumulative outcome | Focused hours |
|---|---|---:|
| S0 | Frame the problem and diagnose Python through a fresh document task | 4–6 |
| S1 | Build a reliable document-search CLI; demonstrate intermediate Python | 26–38 |
| S2 | Validate model output; build and evaluate RAG | 36–52 |
| S3 | Own a bounded tool/agent loop, approval and an educational MCP bridge | 20–30 |
| S4 | Implement count baselines, probability, vectors and gradient learning | 50–70 |
| S5 | Write manual gradients/backprop and a small neural network | 45–65 |
| S6 | Write tokenization and a complete causal transformer architecture | 60–85 |
| S7 | Train from random weights; evaluate, checkpoint, reload and generate | 45–70 |
| S8 | Compare/integrate models, harden the assistant and study tiny adaptation | 20–30 |

The plan totals 306–446 focused hours; with a 20% reserve, about 37–54 study weeks at ten hours/week. These are estimates, not measured learner timings. Re-estimate after actual diagnostic and compute evidence. The [detailed roadmap](docs/learning-path/02-PROJECT-ROADMAP.md) owns acceptance behavior; [route.json](learning/route.json) owns stage IDs, dependencies and budget facts.

The final model is a complete **small decoder-only language model**, with learner-written architecture and lifecycle. First prove gradients and a small network manually, then use tensor/autograd machinery for practical CPU training. Calling a hosted LLM, fine-tuning pretrained weights, or completing a toy forward block does not satisfy this endpoint. See the [model build specification](docs/learning-path/05-LLM-BUILD-SPEC.md).

## Run the inherited baseline

```powershell
uv sync --locked --all-groups
uv run python scripts/learning_state.py status
uv run python projects/grounded_support_assistant/app.py "How long is an export link valid?"
uv run pytest -rxX -q
```

No API key, GPU, model download or network call is needed to run the baseline after environment setup. It retrieves English handbook sections using token overlap. The original evaluation has twenty cases and a declared paraphrase failure. Newly exposed unsupported and multi-intent cases are tracked separately; citation and lexical relevance alone do not establish answer support. This is inherited reference code to inspect and improve, not a finished reliable assistant or learner achievement.

## Find the right document

| Need | Owner |
|---|---|
| Session method and gradual help | [Learning method](docs/learning-path/01-LEARNING-METHOD.md), [mentor skill](.agents/skills/project-mentor/SKILL.md) |
| Required skills and ownership gates | [Skills and mastery](docs/learning-path/03-SKILLS-AND-MASTERY.md) |
| First twenty sessions | [First four weeks](docs/learning-path/04-FIRST-FOUR-WEEKS.md) |
| Reference lesson bridges | [Curriculum map](docs/learning-path/06-CURRICULUM-MAP-AND-STATE.md) |
| Safe factual progress recording | [Evidence protocol](learning/PROTOCOL.md) |
| Selected primitive exercises | [Mechanism shelf](resources/README.md) |
| Review of the six source repositories and merge choices | [Consolidation report](docs/review/CONSOLIDATION.md) |
| Versions, validation and contributor rules | [Project context](project-context.md) |
| Curriculum route, resolver and edited lessons from the from-scratch clone | [From-scratch](from-scratch/README.md) |

Only one installed mentor and one factual event log are active. The same S0–S8 plan also exists as [`from-scratch/route.json`](from-scratch/route.json), moved here on 15 October 2026 with the curriculum resolver; the two route files still need to be reconciled into one. Historical state is labelled under archive; full source histories and unpublished local experiments are privately backed up. Superseded repository handling and its exact status are recorded in the consolidation report.
