# The first four weeks: 20 sessions, 40 hours

Prepared 11 October 2026; revised 15 October 2026 for the RAG/agents route. These are relative study weeks; the start date has not been selected. Each session is two hours, five sessions per week. Gate results govern movement, so these are session targets rather than promises.

## Starting mission

**Understand how a grounded assistant turns a question into a cited answer, then make the workbench assistant a reliable Python program that a model can sit behind.** Weeks 1–3 cover S0 and S1; week 4 opens S2 with the first model call.

Use the inherited handbook corpus in the workbench. Read Mushir in its own private checkout; do not copy its corpus or AAOIFI text here.

## Week 1 — Frame the quest and trace one answer (S0, then S1 begins)

| Session | Mission and mechanism | Learner action | Checkpoint |
|---|---|---|---|
| 1 | Frame the quest; the carried-forward `.env` versus process-environment confusion | State who the user is, what a useful answer is and when to refuse. Predict the workbench CLI result for one answered and one unanswerable question, then run both. | Prediction compared with output; the configuration distinction explained in your own words. |
| 2 | Follow one Mushir answer | Trace one request from HTTP entry to retrieval, generation, citation validation and response, naming each step's input and output. | A learner-written trace; one step you cannot yet explain marked as a question. |
| 3 | Read code you did not write | Pick one function from the trace; explain inputs, outputs and side effects; predict its result on a new input. | S0 exit: trace, prediction and the Python gaps observed. |
| 4 | Records and files | Read the handbook into passage records with IDs and offsets using `pathlib` and UTF-8. | Missing and empty files handled explicitly. |
| 5 | Review and transfer | Add an unfamiliar document; predict the records produced before running. | Fresh-case result recorded. |

## Week 2 — Typed boundaries and tests (S1)

| Session | Mission and mechanism | Learner action | Checkpoint |
|---|---|---|---|
| 6 | Dataclasses and type hints | Model passages and answers as dataclasses. | Explain what a type hint does and does not check. |
| 7 | Pydantic at the boundary | Validate an incoming query and an outgoing answer; produce a clear error for bad input. | A malformed input is rejected with a useful message. |
| 8 | pytest | Write tests for normal, empty, Unicode and tie cases. | One deliberate wrong implementation fails a test. |
| 9 | Errors and logging | Typed exceptions and `logging` instead of prints. | A failure can be located from the log alone. |
| 10 | Review and transfer | Fix a fresh validation or file bug without supplied code. | Regression test added for it. |

## Week 3 — Configuration, HTTP and tooling (S1)

| Session | Mission and mechanism | Learner action | Checkpoint |
|---|---|---|---|
| 11 | Settings and secrets | Load settings from the environment; prove a secret never appears in output or logs. | Explain where each setting comes from. |
| 12 | HTTP with `httpx` | Call a small public JSON endpoint with a timeout and error handling. | Timeout and non-200 responses handled. |
| 13 | Async, just enough | Fetch three endpoints sequentially and concurrently; compare time. | Explain when async helps and when it does not. |
| 14 | `uv`, Ruff and a clean run | Reproduce the environment from the lock file; lint and format. | Documented commands run from a clean checkout. |
| 15 | Apply to Mushir and close S1 | Read Mushir's settings and answer models; predict a missing-field failure. Run the S1 exit task. | G1 attempted on a fresh bug; remaining gaps recorded. |

## Week 4 — The first model call (S2)

| Session | Mission and mechanism | Learner action | Checkpoint |
|---|---|---|---|
| 16 | What a chat request contains | Read an example request and response; predict what changes with temperature and max tokens. | Tokens and cost explained with one worked number. |
| 17 | First live call | Call an OpenAI-compatible provider through the `openai` SDK with a timeout; record model ID, tokens and latency. Check the model ID in official docs first. | One budgeted live call with recorded metadata. |
| 18 | Structured output | Request answer, citations and status; validate with Pydantic; reject an unknown citation. | Malformed response test passes on a fake model. |
| 19 | Tracing | Send the same call through LangSmith or Langfuse and read the trace. | Trace explained step by step. |
| 20 | Review and plan | Rebuild the call with LangChain; compare. Revisit one week 1–2 mechanism on a fresh case. | Actual pace recorded; S2 next step chosen. |

Live calls need explicit session authorization and a small budget. Enter credentials locally; never paste them into the tutor conversation.

## Task 1, ready for the next guided session

Start with this prompt, not a supplied answer:

> Mushir refuses to give a binding fatwa, and the workbench assistant abstains when its handbook does not support an answer. In your own words: who is the user of each, what does a useful answer look like, and what would go wrong if the assistant answered anyway? Then predict what the workbench CLI prints for "How long is an export link valid?" and for "What is the capital of France?" before running either.

The tutor waits for your answer, reviews it and selects one next action.

## Weekly exit evidence

| Week | Evidence to save | What it does not establish |
|---|---|---|
| 1 | Quest framing, one traced answer path, observed Python gaps | That you could build that path yet |
| 2 | Typed records, Pydantic validation, meaningful tests | LLM or RAG skill |
| 3 | Settings, HTTP client, reproducible environment; G1 attempt | Async mastery beyond the basic case |
| 4 | One live call with metadata, validated structured output, a read trace | RAG quality |

## Adapt the schedule

- If a prerequisite blocks two sessions, shrink the task and insert a focused bridge.
- If a mechanism is already independently demonstrated, shorten its teaching but keep the later retention check.
- If an environment problem consumes more than 20–30 minutes, separate environment repair from conceptual work.
- If you miss a day, continue in sequence; do not double the next day's load.
- If live provider access is blocked, keep the fake-model work going and leave the live gate visibly pending.
