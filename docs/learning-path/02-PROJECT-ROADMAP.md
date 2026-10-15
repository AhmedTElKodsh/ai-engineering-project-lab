# The cumulative project roadmap

Revised 15 October 2026; replaces the 11 October S0–S8 route. Read the [mastery rules](03-SKILLS-AND-MASTERY.md) and the [library map](08-LIBRARY-MAP.md) alongside these stages. Effort ranges are estimates for learner work; a stage can take longer without changing its exit criteria.

## Direction of this route

**Depth:** RAG systems, then AI agents and agentic engineering. **Floor:** Python, evaluation, observability, cost, security and reproducible delivery, which show up inside every stage instead of as separate subjects. **Deferred:** deployment/LLMOps and model adaptation come after the core route. **Optional:** the from-scratch track (manual gradients, transformer internals, training from random weights) is a separate later shelf.

**Learn as needed, as much as needed.** Each mechanism gets the theory needed to use it correctly with an existing library or framework: a plain-language idea, one concrete trace, its limits and the engineering consequence. Plain-Python reimplementation of a framework mechanism belongs to the optional track unless the learner asks for it at that moment.

**Three working surfaces.**

1. **This workbench** (public): `projects/grounded_support_assistant` holds the learner's code. Its inherited handbook corpus serves S1–S2; the [HR policy corpus](../../resources/corpora/hr-policy/README.md) (fictional company, PDF/DOCX/HTML/Markdown, English and Arabic, 125 golden questions, 20 agent scenarios) serves S3–S6.
2. **Mushir** (private, client-approved for learning): each stage ends by explaining and then changing the matching Mushir mechanism in its own checkout. Evidence records written here describe what the learner did and point to Mushir commits by ID. AAOIFI standards text is never copied into this public repository; link to the official download instead.
3. **Explorations** (`explorations/`): side quests and tutorial follow-alongs. They earn no stage credit and need no state file.

Frameworks enter in the order **official library first, then the orchestration layer**. For example, a stage uses the provider SDK and Chroma directly before rebuilding the same behavior with LangChain or LlamaIndex. The aim is reading Mushir (built mostly from libraries) and job-market frameworks (LangChain, LangGraph, LlamaIndex, LangSmith) with equal confidence.

## S0 — Frame the quest and trace one answer

**Effort:** 4–6 hours. **Dependency:** a working Python interpreter and basic syntax.

Mission: understand what a grounded assistant must do before changing one.

- State in ordinary language who the user is, what a useful answer looks like, and what should happen when the sources do not support an answer. Use Mushir's refusal of binding fatwas and the workbench's abstention as examples.
- Run the inherited workbench CLI on two questions, one answered and one abstained. Predict each result before running it.
- Trace one Mushir request from HTTP entry to retrieval, generation, citation validation and response. Name each step's input and output; reading code is enough, no change is required.
- Read one short Python function from either project and explain its inputs, outputs and side effects.
- Repair the carried-forward configuration confusion: a `.env` file versus the process environment, a client library versus a provider model ID.

**Exit:** a learner-written trace of one answer path with each step's input/output; a correct prediction or a diagnosed wrong one; Python gaps for S1 identified by observation, not by a placement label.

## S1 — Python floor for AI applications

**Effort:** 20–30 hours. **Dependency:** S0. **Corpus:** inherited handbook.

Mission: make the workbench assistant a reliable, typed, tested command-line program that a later LLM layer can rely on.

### Slices

1. **Records and files:** read Markdown/text with `pathlib` and UTF-8; produce passage records with IDs and source offsets; handle missing and empty files explicitly.
2. **Typed boundaries:** model passages, queries and answers first with dataclasses and type hints, then with Pydantic where outside data arrives. Explain the difference between a hint and runtime validation.
3. **Errors, logging and configuration:** typed exceptions with useful messages, `logging` instead of prints, settings from environment with secrets never printed.
4. **Tests and tooling:** pytest with normal, empty, Unicode and tie cases; one meaningful mutation that a test catches; `uv` for the environment; Ruff for lint and format.
5. **HTTP and async literacy:** call a small local or public JSON endpoint with `httpx`, with timeout and error handling; explain when `async` helps an I/O-bound program. This prepares S2 provider calls; no provider account is needed yet.

**Python growth:** comprehensions, sorting with a key, generators for file iteration, context managers, modules and imports, classes only where state requires them. Defer metaclasses and elaborate packaging.

**Apply to Mushir:** read Mushir's settings and answer models; explain one validation rule and predict what happens when a required field is missing.

**Exit:** the CLI runs reproducibly with at least five meaningful tests; Pydantic rejects a malformed input with a clear message; the learner repairs a fresh file-handling or validation bug without supplied code.

## S2 — LLM calls, structured output and tracing

**Effort:** 20–30 hours. **Dependency:** S1. **Corpus:** inherited handbook.

Mission: put a real model behind the assistant safely and see every call.

### Concepts, just enough

What a chat completion request contains (messages, roles, temperature, max tokens); tokens and context windows as a cost and length budget; why model output is untrusted data; what structured output and function schemas guarantee and what they do not.

### Build

- Call an OpenAI-compatible provider (Mushir uses OpenRouter; Groq also works) through the official `openai` SDK with timeout, bounded retries for transient errors and secret-safe configuration. Verify current model IDs in official provider docs before use.
- Request a structured answer (answer, cited passage IDs, status) and validate it with Pydantic. Reject unknown citations and malformed output.
- Rebuild the same call with LangChain (chat model, prompt template, structured output) and compare code size, transparency and failure messages.
- Trace calls in LangSmith or Langfuse; record tokens, latency and cost per call.
- Keep a deterministic fake model for default tests; live calls are explicit and budgeted.

**Apply to Mushir:** read its provider client and citation validation; explain what happens when the model cites a chunk that was not retrieved.

**Exit:** one live call with recorded model ID, tokens, latency and cost; structured output validated, with a malformed-response test passing on the fake model; a trace viewed and explained; a fresh validation bug repaired independently.

## S3 — RAG core with frameworks

**Effort:** 30–45 hours. **Dependency:** S2. **Corpus:** HR policy corpus.

Mission: answer HR policy questions only from retrieved sources, with citations, and measure retrieval.

### Concepts, just enough

Embeddings as vectors where nearby meaning gives nearby vectors; cosine similarity in one small worked example; chunk size versus context budget; why retrieval quality caps answer quality; hit@k and MRR.

### Build

1. **Load and parse:** Markdown and HTML first, then PDF (`pypdf` or PyMuPDF) and DOCX (`python-docx`). Note the two-column PDF, the scanned table and the hidden HTML element as parsing failures to record, not to solve all at once.
2. **Chunk:** LangChain text splitters at two sizes; keep document key, section and version metadata on every chunk.
3. **Embed and store:** `sentence-transformers` (try a multilingual model because of the Arabic documents) into Chroma, with metadata.
4. **Retrieve and answer:** top-k retrieval, a context-bounded prompt and structured cited answers from S2.
5. **Evaluate:** run the golden set's `typical`, `code_lookup` and `out_of_scope` slices; report hit@5 and MRR per slice and per language.
6. **Framework rebuild:** rebuild the pipeline once with LangChain (loaders, retriever, chain) and once with LlamaIndex; compare results on the same questions and say what each framework hid or exposed.

**Apply to Mushir:** read its chunking and retrieval code; explain why it uses BGE-M3 and what its dialect hit@5 table measures.

**Exit:** hit@5 and MRR reported per slice and language with the eval set version; refusal on out-of-scope questions; the two framework rebuilds compared on identical cases; a fresh retrieval failure diagnosed to a layer (parsing, chunking, embedding or ranking) without hints.

## S4 — RAG depth and evaluation

**Effort:** 35–50 hours. **Dependency:** S3. **Corpus:** HR policy corpus, all slices.

Mission: make retrieval and answers trustworthy on the hard cases, and prove improvements statistically.

### Build

- **Hybrid search:** BM25 (`rank_bm25`) plus dense retrieval, fused with reciprocal rank fusion; show where `code_lookup` needs keywords.
- **Re-ranking:** a cross-encoder re-ranker over the fused candidates; measure gain and latency.
- **Query handling:** rewrite follow-up questions to standalone queries (`follow_up` slice); route personal-data questions away from search (`tool_route`).
- **Filters before ranking:** role and region filters built from the session, never from question text (`abac`); prefer current versions and surface conflicts (`version`, `conflict`).
- **Security:** treat retrieved text as data; defeat the hidden FAQ injection; keep the canary token out of answers (`security`).
- **Evaluation:** RAGAS or DeepEval faithfulness and relevance; an LLM judge validated against 60 learner labels with Cohen's kappa; McNemar's test when comparing two versions; held-out IDs from `gates.json` used only before a release.
- **Observability and cost:** traces per question in LangSmith or Langfuse; p50/p95 latency and cost per query reported next to quality.

**Apply to Mushir:** explain its hybrid search fix and quote-repair change from recent commits; propose and measure one improvement on its QA pack in the Mushir checkout.

**Exit:** a results table where each change beats or ties the baseline with a stated test; every hard gate in `gates.json` checked; injection and canary cases passing; one independent improvement with a before/after comparison.

## S5 — Tool-using agents with LangGraph

**Effort:** 35–50 hours. **Dependency:** S3 (S4 may still be in progress). **Corpus:** HR policy corpus, `hris_seed.json`, `leave_rules.json`, `agent_scenarios.jsonl`.

Mission: an HR assistant that looks up leave balances and drafts requests through tools, under rules the model cannot override.

### Concepts, just enough

Tool calling as a model proposing a function name and arguments that the program decides whether to run; the agent loop (propose, execute, observe, stop); state; why deterministic code, not model text, authorizes actions; the ReAct idea as background.

### Build

1. **Native tool calling:** two read-only tools through the provider SDK, with Pydantic argument schemas and allowlisted names.
2. **LangGraph:** rebuild as a state graph with nodes, conditional edges, a step budget and a checkpointer; resume after restart.
3. **Human approval:** a confirm flow for any write (leave request draft), using a LangGraph interrupt bound to exact arguments and an idempotency key; reject replay and changed parameters.
4. **Workflow versus agent:** solve the same scenarios with a fixed workflow and with the agent; record where each is simpler or more reliable.
5. **MCP:** expose one read-only tool through the official MCP Python SDK and call it from the agent.
6. **Comparison:** one bounded rebuild in the OpenAI Agents SDK or PydanticAI; note what changed.

**Apply to Mushir:** design (on paper first) how its scholar-review queue could become an approval step; explain where Mushir must refuse instead of acting.

**Exit:** all 20 agent scenarios run with pass/fail recorded; budgets stop runaway loops; approval cannot be bypassed by model text; restart resumes correctly; an independent fix to a failed tool scenario.

## S6 — Agentic engineering: workflows, guardrails and evaluation

**Effort:** 30–45 hours. **Dependency:** S4 and S5.

Mission: combine retrieval and tools into a multi-step assistant that is safe, observable and measured.

- **Patterns:** router, supervisor with specialist agents, and handoff in LangGraph; decide by evidence when one agent is enough.
- **Memory:** distinguish conversation state, persisted state and retrieved knowledge; add one bounded long-term memory and show what it must not store.
- **Guardrails:** input and output checks, tool allowlists, rate and cost budgets, redaction of personal data in traces.
- **Agent evaluation:** task success, trajectory checks (right tools, right order) and failure classification on the scenario set; regression gating before changes.
- **Observability:** end-to-end traces across nodes and tools; a cost and latency report per scenario.
- **Comparison:** one bounded rebuild of a multi-agent flow in CrewAI; record token overhead and control differences.
- **Fairness slice (optional):** the screening expectations and 32 counterfactual résumés test whether a screening agent scores irrelevant attribute changes identically.

**Apply to Mushir:** implement one agentic improvement in the Mushir checkout with its own eval evidence, such as a clarification-question tool loop or a source-gap guard.

**Exit:** a multi-step assistant passing its scenario gates with traces; one guardrail proven by a counterexample that fails without it; an honest workflow-versus-multi-agent comparison; an independent agentic change shipped in Mushir with before/after evidence.

## Later branches

These are not stages in `learning/route.json`. Each one becomes a route stage only when the learner chooses to start it after the core.

**Deployment and LLMOps.** FastAPI service, Docker, CI with eval gates, prompt and model versioning, caching, monitoring and alerting, local serving (Ollama or vLLM), and a cloud target. Mushir's deployment, readiness and metrics endpoints are the worked reference.

**Model adaptation.** Fine-tuning and parameter-efficient adaptation (LoRA/QLoRA) with existing libraries, compared against prompting and retrieval baselines on a narrow task.

**Optional from-scratch track.** Learner-written count models, manual gradients and backpropagation, tokenizer, causal transformer, and training a small model from random weights. Its contract is the [model build specification](05-LLM-BUILD-SPEC.md); its materials are the [mechanism labs](../../resources/README.md) and the folded [from-scratch lessons](../../resources/from-scratch-lessons/README.md). Plain-Python versions of any core-route mechanism also belong here.

This workbench follows [TOOLING.md](../../TOOLING.md): each library enters at the stage that teaches it, with official documentation checked at that time.
