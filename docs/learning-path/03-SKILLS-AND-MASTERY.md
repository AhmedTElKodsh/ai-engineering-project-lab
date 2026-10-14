# Skills, diagnostic, and mastery evidence

Revised 14 October 2026 to implement the [independent audit](../review/from-scratch-audits/python-to-llm-audit-2026-10-12.md). The audit remains the historical reviewed snapshot; this package and the project route were corrected without learner completion awards.

Prepared 11 October 2026. This is an exercise specification, not completed assessment evidence.

## Diagnose Python inside the first project

Use up to 60–90 minutes for selective probes, guided repair, and a fresh check in S0. Start with counting/explanation and one file or mutation probe. Stop sampling when a specific blocking mechanism appears and teach that gap. Observe the remaining areas in the project slices that actually use them; unsampled means unobserved, not failed or mastered. These are low-stakes observations; basic knowledge is self-reported, and precise gaps have not yet been demonstrated.

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

If the task is unfamiliar rather than a known skill, introduce a small teaching example of a different problem first. Guide the active task through the [hint ladder](01-LEARNING-METHOD.md#tutor-conduct). Only after an attempt, useful hints, persistent difficulty, and a request for more help may the tutor supply the smallest tricky part. A complete solution requires an explicit request for a complete solution. Record partial or full supplied code as assistance. The assessment variation must differ from the teaching example or supplied part. A syntax lookup is allowed; assistant-authored implementation is not independent evidence.

## Python progression

| Area | Initial project use | Later reinforcement | Required evidence |
|---|---|---|---|
| Functions and decomposition | Normalize/count/rank | Loss and attention subroutines | Explain inputs, outputs, side effects; change a contract. |
| Lists, dicts, sets, tuples | Documents, counts, IDs | Vocabulary, merges, run metadata | Choose a structure and identify a mutation/lookup bug. |
| Iteration and comprehensions | Transform corpus records | Build batches and token windows | Predict iteration and handle empty input. |
| File I/O and Unicode | Text/Markdown ingestion | Dataset and tokenizer persistence | Correct UTF-8 round trip and explicit error policy. |
| Modules and imports | Split CLI/core logic | Model/data/train/generate boundaries | Run from a documented root without path hacks. |
| Type hints and dataclasses | Passage/search records | Configuration and run manifests | Distinguish hints from runtime validation. |
| Exceptions and validation | Missing file, invalid query | Provider/tool/checkpoint failures | Useful typed failure with a bounded recovery policy. |
| Iterators and generators | Stream files | Stream examples/batches | Explain lazy consumption and avoid accidental exhaustion. |
| Object-oriented design | State that cannot remain a pure function | Parameterized modules and optimizers | One clear responsibility; explain state lifecycle. |
| Standard library tools | `argparse`, `json`, `logging`, `unittest` | `sqlite3`, `hashlib`, `time`, `urllib` | Use each for an actual project need. |
| Numerical computing | TF-IDF vectors and similarity | NumPy/PyTorch tensors | Shape, dtype, broadcasting, stability, device awareness. |
| Environment and Git | Reproducible local run | Tagged experiments and results | Identify interpreter/version and tested code revision. |

Defer advanced decorators, metaclasses, async programming, multiprocessing, and elaborate packaging until a measured project need arises. Broad Python mastery is not a prerequisite for the first useful AI-related feature.

## AI engineering coverage

| Capability | First appearance | Cumulative reinforcement | Depth required in this route |
|---|---|---|---|
| Data ingestion, provenance, splits | S1 | S4/S7 | Build and test; preserve source IDs and avoid leakage. |
| Model APIs and local/hosted boundaries | S2 | S8 | Implement a small adapter and report actual execution mode. |
| Prompt design and structured outputs | S2 | S3/S8 | Compare on cases; validate types and citations. |
| Tokens and context budgets | S2 | S6/S7 | Estimate app budgets; later implement tokenization. |
| Lexical/vector/semantic retrieval | S1/S2 | S4/S8 | Implement lexical and similarity; compare genuine embeddings when available. |
| RAG and grounding | S2 | S3/S8 | Build retrieval-to-generation flow and separate retrieval/answer metrics. |
| Tools and agent loops | S3 | S8 | Validate actions, bound work, persist state, enforce approval. |
| Memory and orchestration | S3 | S8 | Distinguish current context, persisted state, and retrieved knowledge. |
| MCP | S3 | Later production depth | Educational read-only stdio slice; protocol limitations reported. |
| Evaluation and observability | S1 | Every stage | Baselines, frozen cases, failure analysis, trace IDs, runtime/cost. |
| Classical ML and statistical reasoning | S4 | S5/S7 | Transparent algorithms, data split, generalization, metrics. |
| Backpropagation and optimization | S4/S5 | S7 | Derive, implement, gradient-check, compare with library. |
| Transformers and causal attention | S6 | S7/S8 | Own architecture; verify mask, shapes, loss, and generation. |
| Pretraining | S7 | S8 | Random initialization and genuine parameter updates. |
| Fine-tuning/adaptation | S8 | Later larger-model depth | Required tiny SFT/LoRA mechanism comparisons; production adoption depends on benefit; record separately from pretraining. |
| Reliability and security | S2/S3 | S8 | Boundary tests, timeouts, retries, redaction, cache/version invalidation. |
| Delivery and reproducibility | S1 | S7/S8 | CLI/demo, tests, pinned environment, model/results documentation. |

This is substantial core coverage. It does not establish mastery of computer vision, speech, RL, distributed systems, large-scale training, multimodal agents, or every commercial stack. Coverage is demonstrated by tasks and evidence rather than a list of imported packages.

## The mastery rubric

Use these levels per capability, rather than one score for the whole learner:

| Level | Evidence |
|---|---|
| M0: Not observed | No current learner evidence. |
| M1: Guided understanding | Trace a supplied example and explain it with support. |
| M2: Guided construction | Build/change a component with recorded hints and passing checks. |
| M3: Independent transfer | Solve a fresh small task or diagnose a new fault without supplied code. |
| M4: Retained and integrated | Repeat after a delay and use the mechanism in another project context. |

**Ready to advance** requires execution, explanation, and M3 on introduced mechanisms. **Retention pending** carries a dated fresh task; **retained** requires a delayed independent implementation/debug pass for M4. **Closed** requires every core/live/quality gate ready and retained. A failed review triggers targeted repair while other reachable work continues. A complicated integration may still need help. Exact expectations are agreed before the exit task; the rubric is a local mentoring policy, not a standardized qualification.

## Critical readiness tasks and separate closure obligations

| Gate | Fresh learner task | Failure that prevents closure |
|---|---|---|
| G0: Python readiness | Count/rank/read a changed fixture | Tutor has to provide the complete function. |
| G1: Reliable text application | Repair a tie/empty/path bug and add a regression test | Correct output depends on unhandled input or lost source identity. |
| G2: Grounded RAG | Trace retrieval, context, model output, and citation support | Mock output presented as real model evidence; unsupported citation accepted. |
| G3: Bounded agent | Explain a failed tool run and enforce a limit/approval case | Model text can bypass the application control boundary. |
| G4: Probability and gradients | Calculate a smoothed probability and one update by hand | Wrong unit/normalization or update direction remains unexplained. |
| G5: Backpropagation | Repair a shared-node gradient bug | Only a single-chain example works. |
| G6: Transformer architecture | Trace shapes and repair a future-token leak | Outputs change when only future input changes in evaluation mode. |
| G7: Training system | Resume a run and explain held-out loss versus train loss | Updates/checkpoint state are not verified; test data influences tuning. |
| G8: Integration | Compare models fairly and change one bounded requirement | Capability claims exceed measured results. |

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
Fresh independent implementation/debug task:
Evidence category / eligible scope:
Ready to advance / retention pending / retained / closed:
Support supplied:
Retention check date/result:
Remaining gap and next action:
```

[The evidence protocol](EVIDENCE-PROTOCOL.md) stores attempts, exact-stage focused bridges, eligible full completion, and project gates separately. A quiz is recognition evidence and cannot assign M3/M4, erase skills, select a different numeric phase, or trigger automatic whole-phase restart. New-input behavior alone does not establish independent construction. The original six-question lesson quizzes remain part of full curriculum lesson completion. Project transfer tasks add evidence; they do not alter quiz schemas or automatically close mapped lessons.
