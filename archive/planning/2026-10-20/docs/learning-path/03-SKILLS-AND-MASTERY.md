# Skills, diagnostic, and mastery evidence

Prepared 11 October 2026; revised 15 October 2026 for the RAG/agents route. This is an exercise specification, not completed assessment evidence.

## Diagnose Python inside the first project

Use these tasks in S0/S1: a 60–90 minute first attempt, followed by guided repair and a fresh check. These are low-stakes observations; basic knowledge is self-reported, and precise gaps have not yet been demonstrated.

| Task | Observe | A useful starting criterion |
|---|---|---|
| Count normalized words in a short string | Strings, loops, dictionaries, functions | Correct repeated-word counts; input remains unchanged; learner explains each update. |
| Return the top three scored records | Lists, tuples, sorting, slicing | Explicit descending score and stable deterministic ties. |
| Read UTF-8 text from a supplied path | File context, `pathlib`, exceptions | Correct content and useful missing-file behavior. |
| Predict two functions that modify a list | Aliasing, mutation, return values | Explain a surprising side effect and repair it. |
| Save/load a tiny record collection | JSON types and file boundaries | Round trip and explain why a custom object needs conversion. |
| Write a test for an empty query | Assertions and edge behavior | Test detects a deliberate fault and avoids depending on formatting alone. |
| Explain a traceback from a tiny script | Debugging and decomposition | Locate the cause, distinguish cause from symptom, propose a minimal fix. |

Record each task as **independent**, **with hints**, or **needs a bridge**, with the actual result. Do not turn the total into a course level or award progress automatically.

If the task is unfamiliar rather than a known skill, introduce a small teaching example first. The assessment variation must differ from that example. A syntax lookup is allowed; assistant-authored implementation is not independent evidence.

## Python progression

| Area | Initial project use (S1) | Later reinforcement | Required evidence |
|---|---|---|---|
| Functions and decomposition | Normalize/rank/format | Retriever, chain and tool functions | Explain inputs, outputs, side effects; change a contract. |
| Lists, dicts, sets, tuples | Passages, counts, IDs | Chunk metadata, eval results, agent state | Choose a structure and identify a mutation/lookup bug. |
| Iteration and comprehensions | Transform corpus records | Batch embedding, eval loops | Predict iteration and handle empty input. |
| File I/O and Unicode | Text/Markdown ingestion | PDF/DOCX/HTML parsing, Arabic text | Correct UTF-8 round trip and explicit error policy. |
| Modules and imports | Split CLI/core logic | Ingest/retrieve/generate/agent modules | Run from a documented root without path hacks. |
| Type hints, dataclasses, Pydantic | Passage/answer records | Structured LLM output, tool argument schemas, graph state | Distinguish hints from runtime validation. |
| Exceptions and validation | Missing file, invalid query | Provider timeouts, malformed model output, tool failures | Useful typed failure with a bounded recovery policy. |
| HTTP and async | One JSON endpoint with `httpx` | Provider SDK calls, concurrent embedding or eval runs | Timeout, retry policy and when async helps. |
| Configuration and secrets | Settings from environment | Provider keys, tracing keys | Keys never printed or committed; `.env` versus process environment explained. |
| Testing | pytest with edge cases and a mutation | Fake models and tools, eval harness as tests | A test that fails for a meaningful wrong implementation. |
| Logging and tracing | `logging` instead of prints | LangSmith/Langfuse traces | Find a failure from logs or a trace alone. |
| Environment and Git | `uv`, Ruff, reproducible run | Dependency groups per stage, tagged experiments | Identify interpreter, versions and tested revision. |

Defer metaclasses, multiprocessing and elaborate packaging until a measured project need arises.

## AI engineering coverage

| Capability | First appearance | Reinforcement | Depth required in this route |
|---|---|---|---|
| Model APIs and provider boundaries | S2 | S3–S6 | Call through the SDK with timeouts, retries and recorded model ID/cost. |
| Prompting and structured output | S2 | S3–S6 | Compare prompts on fixed cases; validate output with Pydantic. |
| Tokens, context and cost budgets | S2 | S4, S6 | Estimate and report tokens, latency and cost per query. |
| Document parsing and chunking | S3 | S4 | Parse mixed formats; keep source metadata; compare chunk sizes. |
| Embeddings and vector search | S3 | S4 | Explain similarity; build and query a vector store with metadata. |
| RAG and grounding | S3 | S4, S6 | Retrieval-to-answer flow with citations; refusal when unsupported. |
| Hybrid search, re-ranking, query rewriting | S4 | S6 | Measure each addition against the baseline. |
| Access control and versions in retrieval | S4 | S6 | Filter by role, region and version before ranking. |
| Orchestration frameworks | S2–S3 (LangChain, LlamaIndex) | S5–S6 (LangGraph) | Build with each; explain what the framework hides. |
| Tools and agent loops | S5 | S6 | Validated tool calls, budgets, persisted state, approval. |
| MCP | S5 | S6 | Expose and call one tool through the official SDK. |
| Multi-agent patterns and memory | S6 | Later branches | Choose a pattern by evidence; bounded memory. |
| Evaluation | S3 | Every later stage | Golden sets per slice, judge validation, paired comparison. |
| Observability | S2 | Every later stage | Traces, latency and cost per call and per scenario. |
| Security | S2 | S4–S6 | Output as untrusted data, injection defense, canary, redaction, approval outside model text. |
| Delivery and reproducibility | S1 | Later deployment branch | Pinned environment, tests, documented commands. |

This route does not establish mastery of model training internals, computer vision, speech, RL, distributed systems or production deployment platforms. The optional from-scratch track and later branches cover some of these. Coverage is demonstrated by tasks and evidence, not a list of installed packages.

## The mastery rubric

Use these levels per capability, rather than one score for the whole learner:

| Level | Evidence |
|---|---|
| M0: Not observed | No current learner evidence. |
| M1: Guided understanding | Trace a supplied example and explain it with support. |
| M2: Guided construction | Build/change a component with recorded hints and passing checks. |
| M3: Independent transfer | Solve a fresh small task or diagnose a new fault without supplied code. |
| M4: Retained and integrated | Repeat after a delay and use the mechanism in another project context. |

Stage readiness requires M3 on the introduced mechanisms and permits advancement while delayed retention is pending. Retained completion requires M4 on a different fresh case without AI hints/solutions, with disclosed syntax references allowed. Assisted integration or revisit is useful practice and does not by itself grant retained completion. Exact expectations are agreed before the exit task; the rubric is a local mentoring policy, not a standardized qualification.

## Critical exit tasks

| Gate | Fresh learner task | Failure that prevents closure |
|---|---|---|
| G0: Orientation | Trace a different question through Mushir or the workbench and predict its outcome | Steps named without their inputs and outputs. |
| G1: Python floor | Repair a validation or file-handling bug and add a regression test | Correct output depends on unhandled input or an unvalidated boundary. |
| G2: LLM boundary | Explain a trace and reject a new malformed model response | Mock output presented as live evidence; unknown citation accepted. |
| G3: RAG core | Diagnose a new retrieval failure to its layer | Answer quality claimed without retrieval metrics per slice. |
| G4: RAG depth | Show one change's effect with a paired test | Improvement claimed from a small average difference; held-out set used for tuning. |
| G5: Agents | Explain a failed scenario and enforce a budget or approval case | Model text can bypass the control boundary. |
| G6: Agentic system | Prove a guardrail with a counterexample and compare two designs | Capability claims exceed measured scenario results. |

## Evidence integrity

Set success thresholds before implementing the candidate. Never move difficult evaluation cases into prompts, training data, or demonstrations simply to improve the score. Preserve baseline failures. If a requirement changes, update the contract first and compare old/candidate behavior explicitly.

Use command output plus a code revision or hash. A learner explanation is separate from a generated explanation. Track whether a check used fixtures, a real provider, or a locally trained model. A helpful reference implementation is learning material; it is not learner authorship evidence.

The first evaluation collection is for development, not an inviolable scientific benchmark. Use separate unseen transfer tasks for learning assessment, and later create a locked model test split that is used only at the final report. Small test sets support local decisions, not broad production-performance claims.

## Templates

```markdown
Capability:
Current mastery level:
Date / project / slice:
Learner-authored artifact and revision:
Execution command and result:
Explanation:
Fresh transfer task:
Support supplied:
Retention check date/result:
Remaining gap and next action:
```

Project transfer tasks are the evidence for this route; upstream curriculum lesson quizzes are not required and are not closed by project work.
