# AI Engineering Workbench

One cumulative, learner-owned project for learning AI engineering: grow a grounded assistant from a typed, tested Python program into evaluated RAG and tool-using agents, with each mechanism learned through existing frameworks and applied to a real product.

**Pace:** two hours/day, five days/week, CPU first. **Depth:** RAG systems, then AI agents and agentic engineering. **Floor:** Python, evaluation, observability, cost, security. **Current learner state:** S0 unresolved; no competence is awarded by repository maintenance.

Start with the [project plan](docs/learning-path/00-START-HERE.md), [current checkpoint](LEARNING.md) and [project quest](projects/grounded_support_assistant/README.md). Ask `$project-mentor` to resume one meaningful action at a time.

## The route

| Stage | Cumulative outcome | Focused hours |
|---|---|---:|
| S0 | Frame the quest; trace one Mushir answer from question to citation | 4–6 |
| S1 | Python floor for AI apps: typed records, Pydantic, tests, HTTP, configuration | 20–30 |
| S2 | LLM calls, structured output and tracing (SDK, then LangChain; LangSmith) | 20–30 |
| S3 | RAG core: parsing, chunking, embeddings, Chroma, citations; LangChain and LlamaIndex rebuilds | 30–45 |
| S4 | RAG depth: hybrid search, re-ranking, filters, injection defense, evaluation with statistics | 35–50 |
| S5 | Tool-using agents: tool calling, LangGraph, approval, MCP | 35–50 |
| S6 | Agentic engineering: multi-agent patterns, memory, guardrails, agent evaluation | 30–45 |

The plan totals 174–256 focused hours; with a 20% reserve, about 21–31 study weeks at ten hours/week. These are estimates, not measured timings. The [roadmap](docs/learning-path/02-PROJECT-ROADMAP.md) owns acceptance behavior; [route.json](learning/route.json) owns stage IDs and dependencies; the [library map](docs/learning-path/08-LIBRARY-MAP.md) says which libraries each stage teaches and why.

After the core: deployment/LLMOps and model adaptation as later branches, and an optional from-scratch track (manual gradients, transformer, training from random weights) defined by the [model build specification](docs/learning-path/05-LLM-BUILD-SPEC.md).

## Where things live

| Path | What it is |
|---|---|
| `projects/grounded_support_assistant/` | The learner's code. Inherited lexical baseline to improve, not finished work |
| `resources/corpora/hr-policy/` | Fictional HR corpus and eval sets used from S3 on |
| `resources/labs/`, `resources/from-scratch-lessons/` | Optional from-scratch track material |
| `explorations/` | Side quests and tutorial follow-alongs; no stage credit |
| `learning/` | Route, append-only evidence log, derived state |
| `docs/learning-path/` | The plan; `docs/review/` the consolidation record |
| `archive/` | Historical state and retired routes, never current instruction |

**Mushir** (the client's Islamic-finance RAG assistant) lives in its own private repository. Each stage applies its mechanism there; nothing from Mushir's corpus is copied into this public repository.

## Run the inherited baseline

```powershell
uv sync --locked --all-groups
uv run python scripts/learning_state.py status
uv run python projects/grounded_support_assistant/app.py "How long is an export link valid?"
uv run pytest -rxX -q
```

No API key, GPU, model download or network call is needed to run the baseline after environment setup. It retrieves English handbook sections by token overlap. Its evaluation has twenty cases with a declared paraphrase failure, plus four challenge cases tracked as strict expected failures. This is inherited reference code to inspect and improve, not a reliable assistant or learner achievement.

## Find the right document

| Need | Owner |
|---|---|
| Session method and gradual help | [Learning method](docs/learning-path/01-LEARNING-METHOD.md), [mentor skill](.agents/skills/project-mentor/SKILL.md) |
| Skills and mastery gates | [Skills and mastery](docs/learning-path/03-SKILLS-AND-MASTERY.md) |
| First twenty sessions | [First four weeks](docs/learning-path/04-FIRST-FOUR-WEEKS.md) |
| Libraries by stage and tier | [Library map](docs/learning-path/08-LIBRARY-MAP.md) |
| Why the plan looks like this | [Round tables and decisions](docs/learning-path/07-ROUND-TABLE-AND-DECISIONS.md) |
| Safe factual progress recording | [Evidence protocol](learning/PROTOCOL.md) |
| How earlier repositories were merged | [Consolidation report](docs/review/CONSOLIDATION.md) |
| Versions, validation and contributor rules | [Project context](project-context.md), [tooling policy](TOOLING.md) |

Only this route, one installed mentor and one factual event log are active.
