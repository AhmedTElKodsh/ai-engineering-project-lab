# The first four weeks: 20 sessions, 40 hours

Revised 14 October 2026 to implement the [independent audit](../review/from-scratch-audits/python-to-llm-audit-2026-10-12.md). The audit remains the historical reviewed snapshot; this package and the project route were corrected without learner completion awards.

Prepared 11 October 2026. These are relative study weeks; start date has not been selected. Each session is two hours, five sessions per week. Gate results govern movement, so these are session targets rather than promises.

## Starting mission

**Build a command-line tool that finds relevant passages in a small document collection and tells you exactly where each passage came from.** This is the retrieval foundation of the later RAG assistant. The first release performs search and extraction; real generated answers are introduced in S2.

Use three learner-authored short text files initially, then expand to 10–30 permitted non-sensitive documents after the ingestion contract works. Do not begin with PDFs, OCR, web scraping, private documents, or a large downloaded corpus.

If the existing learner project already implements these features, replace construction sessions with explanation, fresh independent contract changes or unfamiliar bug repairs, and missing features. Reuse demonstrated knowledge and preserve prior evidence.

## Week 1 — Find the next reachable task

| Session | Mission and mechanism | Learner action | Checkpoint |
|---|---|---|---|
| 1 | Frame the search problem; strings/functions/dictionaries | State success/no-match behavior; predict and attempt a word counter. | Explain repeated counts and empty input. Save the diagnostic result. |
| 2 | File I/O, sorting, mutation, testing | Sample one file or mutation probe; stop at a blocking gap and repair that mechanism. Observe unsampled areas later in their actual project slices. | Complete a fresh variation with less help. Locate the actual project workspace. |
| 3 | Text normalization and function contracts | Write the normalizer and counter for a new small fixture. | Case, punctuation, repeated words, and empty text behave as specified. |
| 4 | Paths, UTF-8, and context managers | Load the three files and attach source IDs. | Explain missing-file behavior; read a Unicode example. |
| 5 | Integrate a simple local search | Score token overlap and display the best excerpt/source. | Add an unfamiliar document and predict the result as execution/trace evidence. For independent construction, make a fresh small ranking/normalization contract change or fix an unfamiliar bug with the teaching example closed. |

Expected result: an intentionally small search function or script you can trace. It may have no persistent index or polished CLI yet. If loops/dictionaries remain blocking, use the next week for repair and keep the same project mission.

## Week 2 — Make the data reliable

| Session | Mission and mechanism | Learner action | Checkpoint |
|---|---|---|---|
| 6 | Data records and module boundaries | Separate file reading, text processing, and ranking. | Identify side effects and test one pure function independently. |
| 7 | Paragraph chunking and offsets | Convert document text to passage records with IDs and source positions. | Use half-open character offsets into one UTF-8-decoded, LF-normalized snapshot identified by hash; test Arabic CRLF text. Empty/long paragraphs have a bounded policy. |
| 8 | Sorting and deterministic ties | Implement top-k results, duplicate-query-token policy, and tie breaking. | Explain why a set/dict/list fits each step; repair a supplied tie bug. |
| 9 | Persistence and validation | Save/load a small JSON index and validate expected fields. | Round trip; reject/rebuild after source edit/deletion or normalization/chunk-version changes. Store raw/snapshot hashes and reject corrupt/incompatible indexes. |
| 10 | Review and failure testing | Add missing/empty/Unicode/tie tests; write a small README run command. | New-document handling without logic edits is execution evidence. For independent construction, repair an unfamiliar file/ranking bug and add a regression test. |

Expected result: a reliable data pipeline and ranking contract. Add dataclasses/type hints if repeated unstructured records obscure the code. Do not add inheritance or generic repositories just to imitate a production architecture.

## Week 3 — Measure retrieval

| Session | Mission and mechanism | Learner action | Checkpoint |
|---|---|---|---|
| 11 | CLI boundaries and error messages | Add `argparse` query/corpus options and a self-terminating demo. | Unknown/missing arguments and no-match results are understandable. |
| 12 | Inverted indexing | Map query tokens to candidate passage IDs. | Compare results with exhaustive search on a tiny corpus. |
| 13 | Evaluation fixtures | Create 20 development cases with expected source IDs and label answerability. | Freeze the cases before retrieval changes; preserve paraphrase failures. |
| 14 | Vector bridge | If ready, compute a tiny TF-IDF example and explain cosine similarity. | Hand calculation agrees with the simple implementation; otherwise repair vectors first. |
| 15 | Baseline comparison and retention | Compare overlap and candidate retrieval; record rank/recall failures and runtime. | Fresh retrieval task plus one delayed Python task. Keep only a justified improvement. |

Expected result: an evaluated search release, or clearly recorded remaining work. A weak paraphrase result is useful evidence for the later semantic-embedding comparison. Do not repair it by hard-coding the evaluation questions.

## Week 4 — Establish A1 readiness and approach the model boundary

| Session | Mission and mechanism | Learner action | Checkpoint |
|---|---|---|---|
| 16 | Integration and logging | Run the A1 gate, add targeted logs, and repair the largest failure. | Code revision, command/result, and limitations recorded. |
| 17 | Independent release task | Extend a ranking or ingestion requirement selected after teaching. | Pass G1 with no supplied implementation; five meaningful core tests minimum. |
| 18 | Local versus hosted models | Trace a fixture request/response and define a generation adapter interface. | Explain where inference happens and what a fixture proves. |
| 19 | Prompts and JSON contracts | Define an answer/source/status contract; parse and validate fixture responses. | Reject malformed JSON, unknown source IDs, and wrong field types. |
| 20 | Review and next release planning | Demonstrate A1; revisit an early Python mechanism; select the smallest S2 question. | Remaining gaps and actual pace recorded; no unearned S2 live-generation completion. |

If G1 is not ready, use sessions 18–20 for A1 repair/retention rather than adding an API. If G1 is ready early and you explicitly authorize a budgeted provider call in the teaching session, session 19 can include real generation after current official setup checks. Credentials are entered locally; never paste them into the tutor conversation.

## Task 1, ready for the next guided session

Start with this prompt, not a supplied implementation:

> We want to find information in a few documents. For the text `Python helps. Python teaches!`, what word counts would your search tool need? State your rules for case and punctuation. Then write a function that returns those counts for any small text string.

The tutor first waits for your prediction. It then reviews the attempt and selects one next action. If normalization itself is unfamiliar, teach it with a different short example before assigning a fresh variation. Do not grade a hidden expected punctuation policy; specify it together. Follow the [hint ladder](01-LEARNING-METHOD.md#tutor-conduct): guide the learner rather than supplying the word-counting solution. If an attempt and useful hints leave a persistent blocker and the learner asks for more help, reveal only that tricky part and leave the remaining implementation to the learner. A complete solution requires an explicit request for the complete solution.

The first session should not require you to install a model, create a cloud account, learn matrix calculus, or read this entire planning package. The documents are reference material for the tutor and for reviewing the route.

## Weekly exit evidence

| Week | Evidence to save | What it does not establish |
|---|---|---|
| 1 | Diagnostic, learner function, explanation, changed input | Intermediate Python broadly mastered |
| 2 | Passage/data contract and failure tests | Semantic retrieval or generation quality |
| 3 | Frozen retrieval cases and baseline/candidate results | A generalizable production benchmark |
| 4 | A1 independent readiness with delayed retention state and model-boundary readiness | Retained closure with missing delayed/live evidence; real RAG if only fixtures ran |

## Adapt the schedule

- If a prerequisite blocks two sessions, shrink the task and insert a focused bridge. Update effort after the bridge.
- If a mechanism is already independently demonstrated, shorten its teaching but keep the later retention check.
- If an environment problem consumes more than 20–30 minutes, identify the interpreter/path issue, use a small runnable local task where possible, and keep environment repair separate from conceptual grading.
- If you miss a day, continue the next session in sequence. Do not double the next day's conceptual load.
- If the project stops being motivating, change the corpus/domain while retaining the same data and evaluation contracts.

## Hardware information to collect when needed

During S0, record OS, Python executable/version, available RAM, and disk space using local checks. During S6/S7, measure actual step time and memory for the tiny model. Only then investigate the GTX 1050 Ti's memory and supported software configuration. Hardware speed changes model/run size, not whether you can learn the mechanisms.
