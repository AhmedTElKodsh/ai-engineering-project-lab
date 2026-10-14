# Accelerated AI Engineering Milestones

This is an application-first overlay on the complete 503-lesson curriculum.
It changes study order, not curriculum scope: deferred theory remains in
`LEARNING.md` and returns in later milestones.

The machine-readable order and current milestone status live in
[`route.m1-superseded.json`](../../from-scratch/route.m1-superseded.json). AI tutors must use that manifest before falling
back to numeric phase order.

## Operating contract

0. **Superseded 2026-10-14.** The project route (`route.project-candidate.json`,
   S0-S8 at 10 h/week) is now live; this M1 overlay is kept for reference.
1. Keep the learner's pace at 5-7 hours per week.
2. Use one loop for every lesson: understand, run or modify, save evidence.
3. Build the milestone artifact incrementally; do not postpone all project
   work until the final lesson.
4. Keep human notes in `LEARNING.md`; scheduling reads eligible scoped/full
   evidence under [the evidence protocol](EVIDENCE-PROTOCOL.md), never mere row presence.
   Readiness requires execution, explanation, and fresh independent implementation
   or debugging. Quiz recognition and changed-data reruns do not prove authorship.
5. Advance with visible delayed-retention/live obligations; close only when all
   required gates are ready and retained and every exit criterion has evidence.
   A failed review triggers targeted repair rather than automatic phase restart.
6. Use just-in-time theory when a practical lesson exposes a real knowledge
   gap. Record the detour, then return to the manifest.
7. Do not silently expand the route. Recommend optional depth separately and
   let the learner choose.

## Milestone 1 - Applied LLM Engineer

- **Status:** Active
- **Expected effort:** about 35-45 hours, or 5-9 weeks at the stated pace
- **Outcome:** Ship an evaluated, grounded LLM application using RAG, LoRA,
  MCP, and LangGraph.

### Route

| Stage | Lessons | Purpose |
|---|---|---|
| Readiness gate | Phase 0 lessons 01, 04, 06, 07, 09, 12 only when a local check fails | Repair setup without repeating completed tooling work. |
| Model interaction | Phase 11 lessons 01-03 | Prompting, few-shot reasoning, and structured outputs. |
| Knowledge grounding | Phase 11 lessons 04-07 | Embeddings, context engineering, basic RAG, and advanced RAG. |
| Adaptation bridge | Phase 10 lessons 01, 04, 06 in focused mode; then Phase 11 lesson 08 | Learn the tokenization, pretraining, and SFT concepts needed to run a LoRA comparison without completing all earlier theory first. |
| Tools and orchestration | Phase 11 lessons 09, 14, 16, 17 | Function calling, MCP, LangGraph state, and framework selection. |
| Reliability | Phase 11 lessons 10-12 and 15 | Evaluation, caching and cost, guardrails, and prompt caching. |
| Integration | Phase 11 lesson 13 | Complete the production-application capstone last, despite its directory number. |

`Focused mode` is a declared fast-track exception. Teach the concepts named by
the stage through learner-owned attempts, administer the scoped post-quiz, and
record `focused_bridge` for that exact stage. It cannot close a later full lesson.
Defer the full derivation explicitly. The mapped Phase 10 pretraining update loop
is partial, the SFT updates are random perturbations, and the evaluation scores
are simulated: use them only for qualified concept tracing, never correctness
parity, real training, or model-quality claims. A candidate project route has
been validated separately and was adopted on 2026-10-14.

### Portfolio artifact

Build one document-grounded assistant over a real corpus. The default corpus is
this curriculum, unless the learner selects a business corpus such as SalesFlow.
The same application evolves through every stage.

### Milestone 1 exit criteria

- Answers cite retrieved source passages and refuse unsupported claims.
- Structured outputs are schema-validated.
- Basic RAG is compared with at least one advanced retrieval strategy.
- One MCP server exposes a useful, narrowly scoped tool.
- LangGraph provides explicit state, checkpointing, and a human approval point.
- LoRA/QLoRA is evaluated against the prompt/RAG baseline; the adapter is
  deployed only if the evidence justifies it.
- At least 20 fixed evaluation cases and 5 adversarial prompt-injection cases
  run reproducibly.
- Cost, latency, cache behavior, failures, and limitations are reported.
- A clean-machine README and self-terminating demo reproduce the result.

## Milestone 2 - Tool and Agent Systems Engineer

- **Status:** Queued
- **Expected effort:** about 85-100 hours, or 13-20 weeks at the stated pace
- **Outcome:** Ship a bounded, observable, terminal-native agent that operates
  on a real repository.

### Route

| Stage | Lessons | Purpose |
|---|---|---|
| Tool ecosystem | Phase 13 lessons 01-23 | Tool contracts, MCP servers and clients, transports, security, authentication, observability, routing, skills, and the tool-ecosystem capstone. |
| Agent foundations | Phase 14 lessons 01-22 | Agent loops, reasoning patterns, memory, orchestration, SDKs, benchmarks, computer use, and voice-agent foundations. |
| Reliability pair | Phase 14 lessons 23 and 24 as one unit | Resolve the lessons' circular metadata by learning OpenTelemetry conventions and observability together. |
| Agent reliability | Phase 14 lessons 25-30 | Collaboration, failure modes, prompt-injection defense, orchestration, runtimes, and eval-driven development. |
| Workbench sequence | Phase 14 lessons 31-42 | Build the reusable workbench in order, ending with its capstone. |
| Coding-agent proof | Phase 19 lessons 20-29 | Implement the harness contract through the end-to-end coding-agent demo. |

### Milestone 2 exit criteria

- The agent discovers and invokes schema-validated tools through MCP.
- The loop has explicit budgets, termination conditions, and failure handling.
- Consequential actions require human approval.
- State survives restart and supports a clear multi-session handoff.
- Tool execution is sandboxed with path and command boundaries.
- Prompt-injection defenses are tested at tool and retrieved-content boundaries.
- Traces expose model, tool, latency, token, cost, and error information.
- A fixture-based evaluation harness detects a meaningful regression.
- The agent completes a bounded task on a real repository and produces a
  reviewable evidence artifact.

## Deferred depth

The following remains required for the broader learning mission but is not a
prerequisite for beginning Milestones 1 and 2:

- Full mathematics, classical ML, and deep-learning foundations in Phases 1-3.
- Full NLP, transformer, and LLM-from-scratch depth in Phases 5, 7, and 10.
- Vision, audio, generative, multimodal, RL, autonomous, and multi-agent
  specializations in Phases 4, 6, 8, 9, 12, 15, and 16.
- Infrastructure, safety, and governance depth in Phases 17 and 18.
- Additional Phase 19 projects, selected as portfolio capstones rather than
  treated as one 620-hour linear sequence.

Deferred means postponed, not skipped. An AI tutor should pull in one precise
lesson when it unblocks current work, not redirect the learner through an
entire phase by default.
