# Releases driven by problems

These contracts describe the proposed teaching order, not a currently executable
replacement route. See the [adoption map](05-COMPARISON-AND-ADOPTION.md) before changing
stage boundaries. The existing S0–S6 contract still governs current progress.

## Session pattern

Start with a user need and a visible limitation. Teach one necessary mechanism,
invite a prediction or bounded attempt, wait, and review the actual result. Split
every release below into small actions; do not hand its entire checklist to the
learner as one assignment. Teach Python, testing and configuration when that action
requires them. A concept check follows teaching, rather than preceding it.

The first sessions should yield a useful sourced search and then a small
retrieve-then-answer path. This is a design target to pilot, not a guaranteed time
estimate or permission to skip a blocking skill. Reserve review time within the
existing ten-hour week. Measure coding, setup, repair and hint use before revising
the total schedule.

## R0 — Understand one employee's difficulty

**User problem:** the employee needs an answer, but a plausible unsupported answer
could cause a missed policy deadline.

**Before code:** show the employee's question and the needed excerpt from one
starter passage. Introduce policy, evidence and source in ordinary language.
Ask the learner for one supported fact and its source. Later contrast a missing
fact and trace one local question-to-result path after teaching its boundaries.

**Learner owns:** explanation of the user, desired response and cost of error;
one prediction compared with an observed result.

**Check:** the learner distinguishes a supported statement from an unavailable
personal fact. Do not require private Mushir access, a provider account, or full
retrieval vocabulary to begin this release. Separately repair configuration
confusion when configuration becomes relevant.

## R1 — Find a passage and show where it came from

**User problem:** employees currently open several files for a simple question.

**Smallest behavior:** load the nine supplied records; retrieve a passage; show
its text, policy ID and section. The first learner-authored change can be a tiny
record loader with a useful missing-file result. Use the existing lexical app as
an observed reference, not as evidence that the learner built retrieval.

**Teach when needed:** paths, UTF-8, JSON records, functions, lists/dictionaries,
types, stable IDs and a normal/empty/missing-file check. Use a BM25 library for the
first learner-integrated lexical retriever; do not require a handwritten ranking
algorithm. Adding this library earlier requires the library-map adoption change.

**Check:** a normal result has a resolvable source; empty/malformed input is handled;
an unsupported query can abstain. A rank or similarity score is not proof that a
passage supports the question. If abstention calibration is premature, state the
candidate retrieval result separately from the supported-answer decision.

**Fresh task later:** integrate an unfamiliar same-format record and diagnose an
ID or file boundary defect. Reading inherited code is not independent construction.

## R2 — Give a useful answer from the retrieved evidence

**User problem:** a search result is long; the employee wants a concise answer
without losing the conditions in the policy.

**Smallest behavior:** question → R1 retrieval → bounded evidence context → answer
proposal → validated answer, source references and answer/clarify/abstain status.
Begin with a deterministic fake proposal so each boundary can be inspected. Then
use an explicitly authorized and budgeted provider through its official SDK.

**Teach when needed:** model request/response, tokens/context, secrets and process
environment, Pydantic, untrusted output, timeout and total retry budget. Explain
what schema validation guarantees and what it cannot establish about factual support.

**Check:** reject malformed output and unknown source IDs. A real citation with an
unsupported sentence still fails the support rubric. Exercise a transient failure
and a permanent error with fakes. Live work records model, prompt, evidence IDs,
tokens, latency, cost and tested revision; fake work remains local integration proof.

**Comparison:** for this tiny corpus, compare retrieval with passing all eligible
passages on the same development questions. State whether retrieval earns its cost.
Keep the main path simple. Add a narrow LangChain adapter comparison after the
direct SDK path, not a second application.

**Fresh task later:** reject a new malformed proposal or diagnose a citation failure
without the tutor supplying the fix. Live access can remain pending while supported
local practice continues; it cannot silently satisfy the current S2 live gate.

## R3 — Find the right policy despite different wording

**User problem:** “money for setting up my home desk” may miss a passage that says
“home-office stipend.” Observe a lexical failure or use a clearly labelled teaching
counterexample; do not invent a benchmark result.

**Behavior:** embed the same passages and query using a suitable existing
`sentence-transformers` model, store/query through Chroma, and compare with R1.
Keep original policy, version, passage ID and section attached. For an asymmetric
model, follow its documented query/document encoding requirements.

**Teach:** embeddings, similarity, top-k and relevance with one small trace;
approximate neighbors are candidates, not factual authority. Use the library's
search; no manual vector-store implementation is required.

**Check:** report hit@k and answerable-only MRR with denominators on exposed dev
cases. Include an exact policy-code lookup, a paraphrase and an unsupported query.
Record losses as well as wins. A useful lexical result must not disappear merely
because dense retrieval was introduced. Reject duplicate IDs and incompatible
embedding/index versions; inspect update/delete behavior before persistent reuse.

## R4 — Handle longer documents without losing meaning

**User problem:** staff add complete policies and mixed file formats; short JSON
passages no longer describe ingestion.

**Behavior:** first ingest complete Markdown, then one digital PDF, then DOCX/HTML
as separate increments. Use the original source files/manifest described in the
data plan. Compare two library splitter settings on fixed development cases.

**Teach:** extraction versus source text; headings, chunk boundaries, overlap,
context budgets and source offsets. A complete rule may span a table and its scope.

**Check:** retrieved text retains conditions and source location. Missing extraction,
broken tables, hidden HTML and scanned images are reported explicitly. Do not claim
OCR support from a PDF parser that extracts nothing. Track stable document/chunk
identity and repeat ingestion/update/delete. Keep one main pipeline; compare only a
narrow adapter in LlamaIndex after the direct path and LangChain behavior are clear.

## R5 — Answer from the applicable sources

**User problem:** older rules, different offices, restricted files and contradictory
documents make a relevant-looking result unsafe.

**Behavior:** expand the selected corpus in increments: date/version first, then
trusted role/region, then a conflict, then Arabic and cross-language questions.
Before any restricted or superseded document enters the searchable pool, implement
and test eligibility selection **before ranking/top-k**. Earlier releases accept
only their explicit safe allowlist; they never index everything and filter later.

**Teach:** trusted identity versus question text; applicability versus relevance;
historical intent; conflict versus missing evidence; multilingual retrieval and
answer support. Version and access metadata are part of ingestion, not prompt wishes.

**Check:** a forbidden source cannot reach the model, output or unredacted trace;
future/superseded rules are excluded except for an authorized historical query.
Conflicting active sources are surfaced without invented precedence. Source text
cannot instruct tool use, credential collection or permission changes. Arabic has
its own reported cases and denominators. A known source ID alone is insufficient.

## R6 — Decide which improvements are worth keeping

**User problem:** a retrieval tweak looks better on two examples but may cost more
and break other questions.

**Behavior:** freeze the baseline; add hybrid fusion, reranking or query rewriting
one at a time only for a diagnosed error. Compare on the same eligible development
cases. Record retrieved IDs, answers, failures, latency and model/embedding costs.

**Teach:** hit@k, MRR, refusal/support error rates, paired outcomes, practical
tolerance and uncertainty. Use a calibrated judge only after a human rubric and
reviewed labels; an LLM judge is not ground truth. Teach the selected eval library
and tracing platform at the point they solve a real measurement problem.

**Check:** predeclared hard gates always block; “not statistically significant”
does not mean equivalent. Report improved, inconclusive/no detected difference,
or regressed. Rejecting an expensive change can demonstrate evaluation competence.
Release and learner assessment pools follow the separate data contract.

## R7 — Handle follow-ups and ask useful clarifications

**User problem:** “What about next year?” needs conversation context; “Can I take
leave?” lacks information needed for a personal answer.

**Behavior:** distinguish supported general policy answers, relevant clarification,
and a personal-data lookup. Add bounded session state, then evaluate follow-up
rewriting against the original standalone-query baseline.

**Teach:** session state versus retrieved knowledge; missing slots; ambiguity;
why a policy cannot reveal an employee's actual remaining balance.

**Check:** no cross-user state leakage, invented personal facts or stale identity.
Clarification addresses a decision that changes the answer. Context has an explicit
owner/expiry/reset rule. A deterministic workflow remains a valid design choice.

## R8 — Optional next product: look up a balance and prepare a draft

This is the S5 agent extension after core retrieval, not a requirement for calling
R2–R7 useful RAG. If the full existing S0–S6 route is retained, it remains required
for **route completion**, even when the RAG product checkpoint is already useful.

**User problem:** policy describes an entitlement; the employee now requests an
authenticated balance or a draft request.

**Behavior:** read-only fake HR lookup first, then a deterministic local draft
workflow, then compare a bounded LangGraph tool loop on the same scenarios.

**Teach/check:** typed allowlisted proposals, trusted actor/object IDs, total step
and time limits, checkpoint/restart, duplicate action IDs and unknown write outcomes.
Separate draft creation, employee submission confirmation and manager approval.
An interrupt pauses execution; deterministic code validates authorization bound to
the exact proposal before any effect. Test replay, changed arguments and crashes.
MCP is a bounded read-only exercise. Other SDK comparisons need a concrete question
and time cap; no framework is added merely to enlarge the stack.

## R9 — Defend and reproduce the local release

**User problem:** a teammate must reproduce the assistant and understand its limits.

**Behavior:** fresh-checkout instructions, fixed fixture/context, versioned run
manifest, CI checks, redacted diagnostics and a documented error analysis.

**Check:** a guard-removal negative control fails; an injected defect is diagnosed;
the learner implements/explains an unfamiliar change. Separate system release
results from independent transfer and delayed retention. If R8 is selected, include
its agent gates. Use a simpler workflow if the evidence favors it; multi-agent
complexity has no automatic credit. Real deployment is a separate later branch.
