# Problem-first RAG: one learner-owned project plan

Adopted 20 October 2026. This is the single active detailed plan. It merges the
problem-first proposal and the 20 October improvement plan. Their original files,
the previous route documents, audits and consolidation research are preserved under
[the dated archive](../../archive/planning/2026-10-20/README.md).

## Authority and working agreement

Route IDs, dependencies, capability IDs, effort estimates and assessment blockers
belong to [learning/route.json](../../learning/route.json). This plan owns detailed
acceptance, teaching order, library placement and the remaining maintenance backlog.
[AGENTS.md](../../AGENTS.md) and the [single mentor](../../.agents/skills/project-mentor/SKILL.md)
own interaction rules; [the evidence protocol](../../learning/PROTOCOL.md) owns records.
LEARNING.md and state.json are derived, never edited by hand. Product release labels
are descriptive only; S0–S6 remain the only route. No second progress tracker.

Planning, inherited implementation, fixture generation and maintenance checks do
not establish learner competence. This adoption prepares S0; it awards no progress.
No provider spending, external actions, commits, pushes or private-corpus access are
implied. Actual learner implementations remain the learner's work.

## The employee problem

You are the junior AI engineer helping the employee help desk at Nilebyte Solutions,
a fictional company. An employee needs the right policy rule and its source. The
answers are scattered; wording differs; rules change; some material belongs to a
particular office or role. A plausible wrong answer can cause a missed deadline,
an invalid request or disclosure of restricted information.

Build a small local policy assistant, then improve it as these problems appear.
Begin with a passage and its source. Add concise generation when it helps. Introduce
meaning-based retrieval when different wording causes misses; longer documents,
versions, access, conflicts and conversation each create the next engineering need.
A personal balance needs an authenticated lookup, not a guess from policy text.

Retrieval means finding relevant material; generation means composing an answer.
RAG gives retrieved evidence to a model to help answer. A relevant passage, a valid
citation and a supported answer are separate claims. A deterministic search or
workflow remains a valid design when it solves the problem better.

The product starts in English, on CPU, as a local CLI. The fixture context is a
Cairo employee at the fixed date 2026-09-24. Synthetic policies are practice data,
not real employment/legal guidance. Deployment and model training are later choices.

## Shared learning and evidence rules

Use the actual user problem to explain why today's mechanism is needed. Introduce
vocabulary before assessing it. Show a small trace or unrelated example when useful,
ask for one prediction/attempt/diagnosis, then wait for the real response. A release
checklist is for the tutor to decompose, not a multi-task assignment for the learner.

Increase help from a conceptual clue to a diagnostic question, decomposition or
incomplete pseudocode, then a tiny different example. Do not reveal the whole active
algorithm through serial hints. After an attempt and useful hints, an explicit
request for more help permits the smallest blocker fragment, with learner integration
and explanation. A complete solution requires an explicit complete-solution request.
Supplied partial/full code is assistance; it never proves independent ownership.

Confusion needs repair, not an unfamiliar surprise quiz. Preserve valid evidence
separately and leave the confused mechanism unresolved. Source comprehension shows
the needed approved excerpt. Independent transfer uses a fresh variation of a taught
mechanism without supplied active answers/code/hints; disclosed syntax docs are allowed.

Each declared critical capability needs execution/task performance, learner explanation
and fresh independent transfer under its current contract. All are required for stage
readiness; delayed fresh retention is separate and requires at least 24 elapsed hours,
normally 2–7 days. Time alone is not retention. One artifact may cover several
capabilities only if it explicitly demonstrates each; assistance is recorded honestly.
At S0 task performance can be a manual evidence trace, with no invented code command.

Keep inherited, supported, local deterministic, live-provider, deployed and independent
proof separate. Maintainer validation and synthetic tutor pilots never award learner
proof. The actual mentor-host pilot must be observed before the first mastery decision;
until then supported S0 practice is allowed and the route assessment blocker remains.
Capability failures/corrections reopen the affected qualification, while unrelated
observations survive. A changed stage/shared contract conservatively requalifies that
stage's capabilities; historical records remain immutable and are not promoted.

Every case-bearing context/focus event counts as exposure, even if later invalidated
or under an older contract. Neutral maintainer navigation must use a navigation: case
and no assistance; it cannot hide a supplied answer. A correction only invalidates
an earlier observation; new help requires its own exposure record. Renaming related
material does not make it fresh; the mentor inspects provenance as well as IDs.

Pace remains five two-hour sessions weekly, CPU first, with 20% reserve for review and
repair. Route hour ranges are provisional estimates for the reorganized work, not a
completion promise. Record coding/setup/repair time and assistance; re-estimate after
S1, first provider work and first RAG comparison. No measured time saving is claimed.

## Data and evaluation rules

Start with [nine supplied passages](../../projects/grounded_support_assistant/data/starter-corpus.json)
from three existing fictional HR policy families. They are verbatim extracts with
source pointers, hashes, dates, role/region metadata and stable IDs. These boundaries
are supplied scaffolding, not learner parsing/chunking work. Their
[twelve development cases](../../projects/grounded_support_assistant/eval/starter-dev-cases.json)
are exposed, including their rubrics. Keep all three families and related extracts,
versions, translations and paraphrases in development. Never call them unseen transfer.

S0 reads only the one needed passage; it does not read all dev answers. S1–S2 search
only the selected safe allowlist. S3 expands first to complete clean Markdown, then
matching mixed-format files from the original corpus; compare parser output with
clean authoring sources without indexing both copies. This explicit early teaching
use supersedes the former blanket prohibition on reading clean sources for ingestion.
The original HR manifest owns metadata for the full corpus, not the starter snapshot.

Before expanding beyond the safe allowlist, filter trusted actor/role/region/date and
version eligibility before ranking/top-k, model context and external traces. A user
question cannot grant access. Historical questions select the appropriate period;
active conflicts need explicit source-backed resolution or escalation, never invented
precedence. Add Arabic, conflicts, hidden instructions and hard extraction one at a time.

Four pools stay separate: displayed teaching, exposed development, system release
holdout and learner transfer/retention. Partition source/document families before
question generation. Actual selectors must enforce disjointness. No clean release
holdout is supplied by this adoption. The original HR selectors have known overlap
and are blocked for new unseen claims until P2-1 is repaired. If a release case informs
debugging, expose its related family and replace reserved coverage before a new claim.
If the corpus cannot support disjoint coverage, explicitly narrow the acceptance
claim; never silently call same-corpus tuning independent generalization.

A response distinguishes answer, clarify and abstain; it identifies evidence and
retains relevant conditions. Check support separately from citation existence. Test
valid source IDs plus unsupported extra sentences as well as invented IDs. Numeric
checks must respect decimals, signs, units, dates, percentages and Arabic digits.
Development rubrics are human-readable, not an implemented automated judge.

Report hit@k and MRR only on answerable items with explicit denominators; unsupported
items use refusal/leakage checks. Report factual support, completeness, applicability,
retrieval, latency and cost separately. Freeze code/prompt/model/corpus/index/eval
identities. A fake does not establish live-model quality, cost or latency.

Hard gates block unconditionally. Predeclare a practical comparison tolerance; inspect
paired wins/losses and effect size; report improved, inconclusive/no detected difference
or regressed. Non-significance is not equivalence. McNemar is for paired binary outcomes;
continuous scores need a paired continuous analysis. Human labels/rubric precede a
calibrated judge, whose false acceptance of unsupported claims is reviewed separately.

Gate applicability follows behavior, not old stage numbers: early generated RAG
needs its support/citation gates from S2; expanded HR indexing needs eligibility from
S3; tool-enabled policy answers retain RAG/leakage gates alongside agent gates.
Screening is optional and does not block a route that does not select it.

## S0 — Understand the problem and trace supported evidence

**Product outcome:** explain one employee's problem and follow one local evidence
path before implementing the assistant. No provider, model download or private
Mushir checkout is required. Do not make configuration repair an orientation gate.

**Critical capabilities:**

- S0.user_problem: explain who needs help, what a useful response contains and the
  consequence of an unsupported answer; identify the learner's engineering role.
- S0.support: identify a supported fact and its source from a displayed passage;
  distinguish a general rule from an unavailable personal fact and justify abstention.
- S0.trace: trace question → selected evidence → proposed answer → support/citation
  check → response, naming inputs/outputs and diagnosing a prediction mismatch.
  Label this a manual/conceptual path until software actually implements it.

**First interaction:** explain the employee situation and show passage
pf-leave-carryover with HR-LV-01, version 2026.1, section 2.6. Ask one meaningful
question about what could go wrong if the assistant invents a deadline; wait.
Next teach/display the source needed for supported-fact comprehension, and later
contrast missing personal information. Teach each trace boundary before assessing it.
Do not reveal answers to fresh transfer or retention tasks in advance.

**Exit G0:** actual learner problem framing, supported fact/source and refusal
reasoning; a local trace with inputs/outputs and a prediction compared with an
observed source-based result. Use unfamiliar fictional source material for later
independence. A clear response can satisfy several criteria without artificial
turn quotas. Inherited CLI behavior is reference evidence, not learner authorship.

**Before awarding proof:** P0-1 exposure policy, P0-2 bound shared contracts and
P1-A capability checks must pass; P1-B needs an actual isolated mentor-host pilot.
Preparation checks alone do not discharge the pilot. Supported practice may begin
while that assessment blocker remains visible. All learner capabilities start unresolved.

**Libraries:** none beyond the existing local environment. The carried-forward
.env/process-environment and client/model-ID support notes remain preserved for S2.

## S1 — Find and cite a useful passage

**User problem:** an employee opens several files for a simple rule. Build a small
loader and lexical search over the supplied safe fixture, with a source or explicit
no-supported-answer outcome. Introduce Python inside these concrete changes.

**Critical capabilities:**

- S1.records: pathlib, UTF-8, JSON, iteration, functions/modules and stable source IDs;
  handle missing/empty files and preserve input records/Unicode correctly.
- S1.validation: dataclasses/type hints versus Pydantic boundary validation; useful
  typed errors for malformed records/queries; no path traversal or escaping symlinks.
- S1.lexical_search: integrate rank_bm25 through its documented API; deterministic
  result ordering, source resolution and an unsupported query. A score is a candidate
  relevance signal, not factual support. Handwritten retrieval algorithms are optional.
- S1.tests_git: pytest checks for normal, empty, missing-file, Unicode, malformed and
  tie behavior; meaningful mutation caught; reproduce with uv/Ruff, review a diff and
  independently repair a fresh file/validation bug with a regression test.

**Exit G1:** learner-owned search slice with these behaviors and fresh independent
change. The inherited handbook app is available only as a labeled reference. Its
known failures are not weakened or relabeled as success.

**Libraries:** pathlib/json/logging as needed, dataclasses, Pydantic, rank_bm25,
pytest/Ruff/uv. Install stage dependencies only when this stage starts. Broader HTTP,
retry budgets, secret-safe settings and async are explicitly owned by S2/S3 below.

**Private application:** inspect Mushir settings/answer models in its own checkout;
explain one validation rule and predict a missing-field outcome. No private text here.

## S2 — Answer from the passages the system found

**User problem:** the employee wants a concise explanation without losing policy
conditions. Connect S1 retrieval to bounded context, a model proposal and a validated
answer/clarification/abstention. Begin with deterministic fake responses, then an
explicitly authorized budgeted live call. For the tiny corpus compare retrieving
with giving all eligible passages; retain the simpler adequate path.

**Critical capabilities:**

- S2.configuration: environment versus .env, client library versus provider/model
  ID, loading settings before reading secrets, and a test proving no secret in logs.
- S2.provider_io: use the official openai SDK for the selected compatible endpoint;
  verify current official model/API docs at implementation time. Teach httpx against
  a local fake JSON endpoint, timeout, transient versus permanent errors and a total
  retry/token/cost budget that actually terminates. Distinguish authentication failure,
  rate limit, timeout and exhausted budget using deterministic tests.
- S2.structured_support: Pydantic schema/status/citation validation; reject malformed
  JSON, unknown citations and valid citations with unsupported claims. Explain the
  limit of schema validation. Compare prompts/models on small fixed dev cases.
- S2.tracing: LangSmith is the core tracer; redacted local diagnostics first. Record
  code/prompt/config/model, context IDs, tokens, latency and cost; explain a trace.
  A narrow LangChain adapter comparison follows the direct SDK and keeps one pipeline.

**Exit G2:** full failure matrix, one observed authorized live call with manifest,
explained trace, and fresh malformed-response repair. If live/tracing access is
unavailable, continue local practice and keep that gate pending. No fake live proof.

**Before proof:** P1-D and the behavior-relevant parts of P2-1/P2-2, including support
negative controls and disjoint assessment policy, must be implemented/verified here,
earlier than the previous plan's before-S3 deadline. Do not import broken HR holdout
selectors merely to get a score. No provider or tracing credential is needed at S0.

**Private application:** inspect its provider/citation validation, predict an unknown
retrieved-chunk ID result, and keep any private trace local/redacted.

## S3 — Retrieve across wording and document boundaries

**User problems:** a paraphrase misses exact words; whole documents exceed useful
context; PDF/DOCX/HTML extraction differs from clean text. Add one difficulty per slice.

**Critical capabilities:**

- S3.semantic_search: sentence-transformers query/document encoding, similarity and
  top-k; Chroma; compare semantic versus lexical retrieval on the same dev inputs,
  including exact-code lookup and a paraphrase. Nearby vectors are not authority.
- S3.parsing_chunking: full Markdown first, then digital PDF, DOCX and HTML with
  pypdf or PyMuPDF, python-docx and BeautifulSoup; library splitters at two sizes;
  retain section/version/source offsets and rule scope/table conditions. Diagnose
  two-column, scanned-image and hidden-element failures without claiming unsupported OCR.
- S3.index_lifecycle: stable document/chunk IDs, duplicate ingestion, update/delete,
  persisted index/embedding-version mismatch and reproducible configuration.
- S3.eligibility: trusted role/region/date/version selection before ranking/top-k
  from the first expanded HR index. No restricted/superseded data reaches the model
  or unredacted traces. The earlier safe allowlist is not a general filter proof.
- S3.retrieval_metrics: hit@5 and answerable-only MRR, explicit denominators/slices,
  frozen corpus/index/eval identities; layer diagnosis of a fresh failure. Teach
  bounded batch/async I/O with httpx here; compare sequential/concurrent behavior and
  explain where async helps, with timeouts and cancellation.

**Framework comparison:** official libraries first; one main pipeline. LangChain
loaders/splitters/retriever and LlamaIndex each get one narrow adapter experiment on
fixed inputs, a concrete question, a two-session cap and a keep/defer/drop decision.
Do not build multiple applications. Add no framework merely for coverage.

**Exit G3:** all capabilities, refusal on unsupported requests and a fresh diagnosed
retrieval defect; reports separate retrieval from answer support. P2-1 selectors,
gates/validator/CI and P2-4 eligibility/lifecycle checks are prerequisites to proof.

**Private application:** inspect its multilingual chunking/retrieval and explain an
embedding choice and actual metric; no corpus is copied.

## S4 — Use the applicable rules and justify improvements

**User problems:** older/foreign-office rules appear, current documents conflict,
Arabic wording differs, follow-ups omit context and tweaks trade quality for cost.

**Critical capabilities:**

- S4.applicability_security: historical intent, regional precedence only when sourced,
  active conflicts surfaced, role/region isolation, retrieved text as data, injection
  and canary controls, Arabic and cross-language support reported separately.
- S4.hybrid_rerank: BM25+dense reciprocal-rank fusion, cross-encoder reranking and
  rewrite candidates introduced for diagnosed failures; paired comparison of quality,
  losses, p50/p95 latency and cost. Rejecting an unhelpful change is a valid outcome.
- S4.conversation: bounded follow-up rewriting/clarification; identify a missing slot
  that changes the answer; separate session context from facts and personal lookups;
  no cross-user leak, invented identity or stale-session context.
- S4.evaluation: clean development/release selectors and provenance, one declared
  hard-gate/paired-decision policy, RAGAS or DeepEval (choose one), judge rubric and
  calibration against 60 learner labels with agreement/false-acceptance review.

**Exit G4:** independent measured improvement or justified rejection, applicable RAG
hard gates and a useful negative control. No MRR for unanswerable items, no tuning on
release cases, no claim of equivalence from a non-significant test. Langfuse and
another vector store/eval library are optional bounded comparisons, not required rebuilds.

**Private application:** propose and measure one authorized retrieval/answering
improvement in that checkout with its QA evidence, keeping confidential sources local.

## S5 — Look up personal state and draft an action safely

**User problem:** policy cannot tell an employee their current balance or submit a
request. This is a product extension beyond useful RAG, but remains required for
completion of the selected full S0–S6 route. Screening remains optional.

**Critical capabilities:**

- S5.tool_authority: read-only fake HR lookup first, typed allowlisted proposals,
  trusted actor/object IDs; deterministic authorization. Separate draft creation,
  employee submission confirmation and manager approval bound to exact arguments/hash.
- S5.recovery: total step/time/token limits; idempotency, replay, stale/changed
  approvals, cross-session confirmation, crash after write before acknowledgement,
  unknown write outcomes and stalled tools. Reconcile ambiguous writes before retry.
- S5.workflow_agent: fixed workflow versus bounded LangGraph state graph, checkpointer,
  conditional edges and restart. An interrupt pauses; it is not authorization and
  code before it can rerun. Pair persistence with a small SQL/state exercise.
- S5.mcp: expose and call one read-only tool through the official MCP Python SDK,
  validating arguments and limits. A second agent SDK is an optional bounded comparison.

**Exit G5:** all 20 original agent scenarios plus negative controls, correct budgets,
restart/replay/approval behavior and a fresh independently repaired tool failure.
Applicable RAG/leakage gates still apply to policy-search tool results. No real HR
integration or external side effect is part of this baseline.

**Private application:** design an approval/source-gap review workflow there and
explain where it must refuse. Actual external/client changes require their own scope.

## S6 — Reproduce and defend the integrated local release

**User problem:** another engineer must reproduce the assistant, diagnose a failure
and trust its operational limits. A multi-agent design is not required to win.

**Critical capabilities:**

- S6.integration: retrieval, workflow/agent tools and guardrails; task success,
  trajectory/order errors, regression gates and end-to-end redacted traces; compare
  one-agent/workflow versus supervisor/handoff only where the scenario needs it.
- S6.memory: distinguish session, persisted and retrieved state; explicit ownership,
  expiry, reset/deletion and contamination tests. Long-term memory is bounded and
  stores no unneeded private data. CrewAI remains an optional comparison.
- S6.release_defense: fresh-checkout run, CI, manifest covering code/prompt/model/
  corpus/index/eval, injected-failure diagnosis, guard-removal control and unfamiliar
  learner-authored change explained against an unfamiliar fictional corpus.
- S6.private_transfer: one independently implemented and measured agentic improvement
  in Mushir's own checkout, with permitted commit references and no private corpus here.

**Exit G6:** combined applicable RAG+agent gates; honest design/latency/cost comparison;
independent integration and delayed retained ownership. Optional screening gates bind
only a selected screening branch. Local reproducibility is not deployed/production proof.

## Remaining maintenance work and acceptance

These are maintainer tasks within this one plan, not learner achievements. A written
requirement is not implementation. The [dated preparation record](../maintenance/S0-PREPARATION-2026-10-20.md) contains executed
checks; route assessment blockers protect stages whose prerequisites remain pending.

| Item / original findings | Trigger and acceptance | State after S0 preparation |
|---|---|---|
| P0-1 / U1,U15 | Before any independent proof: context/focus exposure, older/invalidated records, neutral navigation and correction semantics tested; true fresh controls pass | Implemented in state writer; regression-tested |
| P0-2 / U2 | Before a stage's first proof: bind its stage and relevant shared policies/gates; policy edits invalidate consumers, unrelated sections do not; stale writer rejected | S0 shared/fixture/mentor/protocol binding implemented; future gate dependencies pending |
| P0-3 / U10 | S0 uses a bounded local trace with no private/provider/configuration prerequisite; derived resume follows it | Adopted; state refreshed without learner credit |
| P1-A / U9 | Per-capability execution/explanation/fresh transfer/retention, failures/corrections, legacy compatibility and derived review queue; no stage-only migration credit | Writer support and route IDs implemented; actual learner observations absent |
| P1-B | Before first mastery: real mentor-host isolated synthetic transcripts for unfamiliar term, syntax slip with correct concept, stuck learner, full-solution request, wrong explanation, forgetting, stale state, missing provider; second review of borderline cases | Pending actual host pilot; S0 assessment blocker remains; supported practice allowed |
| P1-C | Before S1 proof: behavior checklist and meaningful mutation import learner code; reviewed Git change | Acceptance assigned to S1; learner implementation/test evidence pending |
| P1-D / U11 | Before S2 proof: provider failure matrix, small fixed-case model comparison, run manifest; LangSmith core/Langfuse optional | Acceptance resolved here; support implementation and proof pending |
| P2-1 / U3–U8 | Before early RAG release/proof: split/group/selector consumers, branch-aware gates, unified paired decision policy, numeric boundaries and validator in CI; no score-only substitute | Pending; moved earlier with S2 generated-RAG behavior; full corpus checks before S3 |
| P2-2 / U14 | Before S2 support proof: reproduce valid-citation+unsupported-sentence failure with retained probe and negative control | Pending verification/implementation; not called fixed |
| P2-3 | Each framework comparison: question, fixed inputs, metrics, two-session cap and keep/defer/drop; one main pipeline | Adopted in stage acceptance; measured savings unknown |
| P2-4 | Before expanded HR index: trusted eligibility/lifecycle checks and denominator/versioned metrics | Owned by S3; implementation pending |
| Phase 3 / U13 | S4 calibrated evaluation, S5 deterministic approval/recovery, S6 fresh local defense with combined gates | Specified above; implementation and evidence pending |
| U12 | Retire old route/lab labels and dead hint references; use one active plan | Prior plans/reviews archived; supporting resource references checked during preparation |

Future proof stays blocked until its listed maintainer prerequisites are tested and
its bound dependencies are registered. Do not remove an assessment blocker merely
because a plan paragraph or helper test exists. Supported work is not automatic credit.
No broad prerequisite reset: bind/pilot the active stage first and prepare later stages
before their first proof, rather than delaying S0 for every later repair.

## Later branches and reference shelf

After the selected core, delivery may add a minimal API, health checks, container,
persisted state, failure/rollback drill and an explicit deployment target. Model
adaptation compares prompting, RAG and fine-tuning on a measured need. Neither branch
is implemented or a current S0 prerequisite.

The optional from-scratch T1–T5 material remains a dormant reference shelf: manual
gradients, tokenizer, causal transformer and training from random weights. Its
[historical specification](../../archive/planning/2026-10-20/docs/learning-path/05-LLM-BUILD-SPEC.md)
and existing labs/lessons do not define another active route. Selecting it later
requires explicit activation and current acceptance, without promoting supplied code.
No hand-built vector store or model internals are required for this core project.

## Agent entry and S0 resume

Use this prompt with the existing mentor:

```text
Use $project-mentor. Read AGENTS.md and project-context.md, run
uv run python scripts/learning_state.py status, read LEARNING.md and only the active
section of docs/learning-path/02-PROJECT-ROADMAP.md plus the current source passage.
Resume the first unresolved capability. Frame the employee problem in ordinary
language, show the required source excerpt, teach one mechanism, ask one meaningful
learner action and wait. Do not implement my code or disclose fresh assessment
answers. Keep actual assistance, support needs and assessment blockers visible.
Use the single revision-checked writer for actual observations only; verify readback.
No paid calls, external writes, commits or pushes are authorized by this prompt.
```

S0 begins with the employee problem and pf-leave-carryover, not archived planning,
all dev answers, setup quizzes or a private codebase. Carry forward configuration
support notes for the stage that uses configuration. Do not record this preparation
or the supplied opener as learner completion.
