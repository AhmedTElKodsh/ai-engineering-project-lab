---
title: Merged improvement plan for the learning workbench
plan_date: 2026-10-20
based_on_commit: 835d97ec9137962807852859494e68bf90a4bd43
sources:
  - "Audit A: external audit dated 2026-10-19 (Downloads/AUDIT.md, not committed; its probe scripts were not supplied)"
  - "Audit B: docs/review/AI-ENGINEERING-AND-LEARNING-AUDIT-2026-10-19.md"
  - "Panel re-verification on 2026-10-20 against the same commit"
  - "Plan review on 2026-10-20 against the local working tree; validation limits recorded below"
status: proposal
implementation_authorized: false
learner_credit_awarded: false
---

# Merged improvement plan

This plan merges the best verdicts of two audits of the same commit into one ordered backlog. It is a proposal, not an authority: when an item is accepted, its acceptance wording must land in its real owner (`learning/route.json`, `docs/learning-path/02-PROJECT-ROADMAP.md`, `learning/PROTOCOL.md`, `gates.json`), not in this file. Nothing here changes learner progress. The ledger still holds one maintainer `context` event and every S0–S6 gate is unresolved.

The two audits share an origin (same date, commit and framing), so their agreement is treated as one finding verified twice, not as independent corroboration. Where they disagree, the panel's re-run decided.

**Plan revision, 20 October:** review findings are incorporated into this proposal. This revision authorizes no implementation or learner credit. During the review, learning-state validation passed with S0 unstarted, and the HR structural validator passed for 21 documents and 125 golden items. The focused state suite reported **39 passed, 3 failed** on the existing local candidate: context exposure still received transfer/retention credit, including invalidated exposure. A separate temporary synthetic-fixture probe also reproduced supplied-case reuse through `focus`. These observations apply to the reviewed working tree, not to a completed repair. The historical register below retains the earlier audit claims and their original verification limits unless explicitly updated.

## 1. Merged verdict

| System | Verdict | Basis |
|---|---|---|
| Technical curriculum coverage | **4/5** design | Both audits agree. Strong RAG/agent/evaluation coverage; too many full framework rebuilds. |
| Repository implementation | **3/5** | Real CI, lockfile, atomic ledger and stale-writer protection; reproduced integrity defects below. Application components are design 4 / implementation 0 because they are the learner's job (Audit B's split, adopted). |
| Pedagogy and assessment design | **3/5** (instruction 4, assessment 2) | Scaffolding and ownership rules are strong; enforcement and granularity are weak. |
| Observed teaching effectiveness | **Not scored** | No learner series and no recorded mentor-host run. |

Keep the project, repair evidence integrity and the evaluation contract first, cut redundant rebuilds, and verify the mentor's actual behaviour before trusting any mastery claim. Do not add topics.

### Preserve (do not touch while fixing)

One route, one append-only ledger, derived views, the revision-checked writer; learner authorship and assistance labels; fake-first tests and honest strict xfails; S0–S6 / G0–G6 identities; the HR corpus's hard cases (Arabic, access, versions, conflicts, canary); deterministic tool authority; the optional T1–T5 boundary; the Mushir privacy boundary.

## 2. Totals and calendar

| Phase | Maintainer | Learner change |
|---|---:|---|
| 0 | 6–10 h | no added learner implementation; prerequisite work also includes the relevant P1-A contract and P1-B pilot |
| 1 | 8–14 h | proposed within S0–S2 budgets; initial capability work and pilot move before first mastery |
| 2 | 8–12 h | possible 12–25 h savings through bounded comparisons; unmeasured |
| 3 | 6–10 h | ≈ 6–10 h added for the local release defense; offset depends on measured savings |
| Housekeeping | 1–2 h | none |
| **Total** | **≈ 29–48 h, provisional** | net effect on the current 174–256 h core is unmeasured; time neutrality is not established |

These are inherited planning estimates, not a fresh sizing of the expanded evidence representation, pilot isolation and provenance checks. Moving P1-A/P1-B prerequisites earlier does not count their hours twice. Re-estimate maintainer work when those designs are specified. The 21–31-week core forecast remains a provisional envelope; re-estimate learner work after S0/S1, the first provider boundary and the first RAG evaluation using measured time.

## 3. Decisions before implementation

1. **Exposure marking (before P0-1):** choose a consistent exposure rule across proof and non-proof records. Either define case-bearing `context`/`focus` as exposure with explicit neutral identifiers, or add a validated exposure field. Specify correction semantics and examples; changing record kind or assistance must not erase supplied-case exposure.
2. **Dependency selection (before P0-2):** select sections of existing authoritative documents through the route or a small manifest that contains only references. Define every stage's consumers, shared rules and gate dependencies without introducing another acceptance authority.
3. **Capability representation (before P1-A and first mastery):** specify stable IDs, evidence/assistance qualification, correction and contract-change scope, aggregation and compatibility with historical stage records. No old observation becomes independent capability proof by migration alone.
4. **Evaluation policy (before P2-1):** predeclare grouping units, all development/release selectors, branch-aware gate applicability, practical regression tolerance and the treatment of inconclusive results before candidate runs. Resolve any departure from source/document separation explicitly in its owner contract.

## 4. The plan

Effort figures are planning estimates. "Maintainer" means platform/curriculum work; "learner" means work that must be learner-authored to count. Per AGENTS.md, no learner acceptance test is weakened to make anything green.

### Phase 0 — integrity and S0 routing before new proof (≈ 6–10 h maintainer, 0 h learner)

Supported practice can continue without awarding readiness. Before the first new mastery decision, complete P0-1–P0-3, the relevant capability-evidence contract from P1-A, and the isolated mentor pilot P1-B. Later-stage contracts and gate dependencies must be bound before that stage's first proof; they do not block S0 while still being specified.

**P0-1 · Close non-proof exposure reuse (U1, U15).**
- Change: define case exposure consistently across proof and non-proof records, including case-bearing `context` and `focus`. Choose the marking policy in section 3 before implementation. Keep neutral navigation and migration records distinct from supplied-case practice; assistance labels or a change of record kind must not hide exposure. Document representative exposure and neutral records in the protocol and mentor guidance. Case IDs remain an identity check; tutors still inspect provenance so a renamed supplied answer cannot count as fresh.
- Files: `scripts/learning_state.py`, `tests/test_learning_state.py`, `learning/PROTOCOL.md`, mentor recording guidance in `.agents/skills/project-mentor/SKILL.md`.
- Acceptance: transfer and retention reject previously supplied cases recorded through either `context` or `focus`, including invalidated and older-contract exposure. A truly fresh case still passes. Neutral migration/navigation records do not block unrelated cases. Include controls for every allowed non-proof record kind, documenting whether it can carry exposure or only refer to earlier records.
- Preserve: append-only history, assistance labels and existing regression behavior. Use the current candidate's full maintenance checks; the historical 81-pass count is not a current completion target.

**P0-2 · Bind each stage's acceptance dependencies before its first proof (U2).**
- Change: define a stage-to-contract dependency map and register scoped `additional_contracts`. Include applicable mastery policy, evidence rules and required library behaviors as well as stage-specific acceptance. Bind S0's dependencies now; register later-stage dependencies before their first proof. Prefer sections of the existing authoritative documents. A manifest may select owner paths/sections but must not duplicate acceptance wording as a second authority.
- Sequence: P2-1 defines the evaluation gate subsets before they can be registered. S3/S4 bind the RAG gates applicable to their declared behavior, S5 binds agent gates plus applicable RAG gates, and S6 binds its combined required gates. Screening dependencies apply only when that optional branch is selected. Include shared selection and decision rules wherever they affect a consuming stage; no registration may refer to a missing future file.
- Files: `learning/route.json`, authoritative acceptance sections, `scripts/learning_state.py` if scoped dependency selection is needed, and tests.
- Acceptance: changing a bound requirement invalidates the consuming stage's own matching proof; dependent readiness/retention recomputes through the route. Unrelated proof survives, and history stays unchanged. Test policy changes, gate changes for S3/S4/S5/S6, unrelated edits and stale-session rejection separately.

**P0-3 · Give S0 a non-private fallback (U10).**
- Change: S0's trace may use the workbench's own answer path when Mushir access is unavailable or too large. Keep the trace bounded to one request, and teach each boundary before it is assessed. Separate the `.env`/model-ID repair from orientation so it cannot block S0.
- Files: roadmap S0, `docs/learning-path/04-FIRST-FOUR-WEEKS.md`, S0's title/next action in `learning/route.json`, and the S0 application exception in `.agents/skills/project-mentor/SKILL.md`.
- Acceptance: S0 can be completed with no private checkout or provider access, and no confidential text enters the repository. Use the state writer to rebuild derived views; verify `status` and the resumed mentor instruction select the bounded fallback without making configuration repair a prerequisite. Later private-project requirements remain separately pending unless explicitly revised in their owners.

### Phase 1 — during the next four study weeks (S0 → S2 opening) (≈ 8–14 h maintainer)

**P1-A · Capability evidence and review queue (U9).**
- Change: identify the critical capabilities in each stage contract; use the mechanisms needed for its exit rather than a fixed count. Define stable capability IDs, event/artifact references, assistance, applicable contract identity and qualification rules in the existing route/protocol/writer. `status` derives unfinished capabilities and due delayed reviews from the same ledger. No second tracker.
- Readiness requires qualifying execution, explanation and fresh independent transfer establishing M3 for every introduced critical capability; retained completion requires qualifying delayed fresh evidence establishing M4 for each. One task may support several capabilities only when its artifact explicitly demonstrates each one. Assisted observation alone cannot fill independent coverage.
- Acceptance: a broad artifact with independent transfer on one capability and assisted observations on the others cannot close the stage. A failure reopens the affected capability's qualification; stage aggregation and dependent readiness/retention recompute while unrelated observations survive. Define compatibility with existing records, correction scope and changed-capability contracts without rewriting history or promoting old stage-level claims automatically.
- Sequence: land S0's minimum capability contract and writer support before its first mastery decision; extend later stages before they award proof. Re-estimate the work after the representation is specified.

**P1-B · Mentor behavioural pilot.**
- Change: run the six synthetic cases (unfamiliar mechanism, Python slip with a correct concept, stuck after hints, explicit full-solution request, confident wrong explanation, forgotten mechanism), plus stale state and missing provider access, in the actual mentor host against an isolated repository fixture with a synthetic ledger. Keep the real checkout outside the pilot's writable target. Save host, model, instruction version, fixture revision, full transcript, assistance and advancement decision as maintainer validation.
- Acceptance: no invented real progress; no serial-hint leak of an active algorithm; requested full solutions are given and labelled assisted; a second read of the borderline cases. Verify the real ledger and derived views are unchanged. Synthetic outcomes never establish learner competence.
- Sequence: complete the pilot on the candidate mentor/state instructions before the first resumed mastery decision. Earlier sessions remain supported practice. Repeat affected pilot cases when subsequent instruction or state changes alter the behavior they tested.
- Files: a test pack under `docs/teaching/` (maintainer-owned), not learner work.

**P1-C · S1 exit sharpening.**
- Replace "at least five tests" with a contract checklist: normal, empty, missing file, Unicode, malformed boundary, secret absent from logs, HTTP budget termination, one meaningful mutation caught.
- Add one small Git task: branch, reviewed diff, regression fix.
- Learner time: inside the existing 20–30 h.

**P1-D · S2 failure matrix and run manifest** (land before S2 closes).
- Exit adds deterministic fake tests for malformed JSON/schema, unknown citation, authentication failure vs rate limit vs timeout, and total budget exhaustion. It also adds one recorded transient-vs-permanent decision and a small fixed-case model comparison.
- Start a run manifest (code revision, prompt, model, config) that S3–S6 extend.
- Resolve U11: LangSmith is the S2 tracer, Langfuse is an optional S4 comparison. Redact before any private trace leaves the machine.

**Measure while doing it:** record coding vs setup vs repair time per session, so the 21–31-week forecast can be re-estimated after S1 and after the first provider call.

### Phase 2 — before S3 (≈ 8–12 h maintainer)

**P2-1 · Evaluation contract repair (U3, U4, U5, U6, U7, U8).**
- **Splits and provenance:** define explicit disjoint `dev_ids` and `release_ids`, retaining source/document and case-family provenance. Follow the project's source/document separation rule before generating related examples; a paraphrase or renamed case is not fresh. If the fixed corpus cannot support that split, explicitly revise the owner contract and label the narrower same-corpus release claim rather than silently weakening it. Preserve development coverage for security, access, version and conflict behavior; obtain release coverage from independently grouped cases/sources. Keep unseen learner transfer separate from system release evaluation.
- **Selectors:** every routine development, smoke, S3 slice and regression selector intersects with `dev_ids`; log release runs and keep their cases out of prompts, demonstrations and tuning. Once a release case informs debugging, record its exposure, move its entire related family out of the unseen pool, and replace that coverage before the next claimed unseen release. Test the consumers' selections, not only the lists' disjointness.
- **Gate applicability:** give every hard gate a stable `id`, behavior scope (`rag` / `agents` / `screening`) and optional-branch applicability. Gates follow the behaviors exercised by the stage/run: S3/S4 apply their declared RAG gates; S5 adds agent gates while retaining applicable RAG checks for retrieval/generated policy answers; S6 applies the combined required set. Screening stays optional, but its gates bind a run that selects that branch. Add a negative control where correct tool calls and request counts cannot hide a canary or restricted-content leak in `search_policy` output. Register each consumer's dependencies through P0-2 before awarding its proof.
- **One decision rule:** hard gates block unconditionally. Then predeclare a practical tolerance; report paired wins/losses and effect size; and label each result *improved*, *no detected difference / inconclusive*, or *regressed*. Use McNemar for binary outcomes only and a paired analysis for continuous scores. Rewrite the eval README's "must beat" line and the roadmap's "beats or ties" line to match.
- **MRR:** compute it on answerable items only. Score `out_of_scope` with refusal accuracy and leakage checks.
- **Validator:** check unknown IDs, split disjointness, source/case-family grouping and gate applicability. Fix numeric boundaries for decimals, percent signs, units, signs and Arabic digits, with tests for `"2.5"`, `"2%"` and `"12"` against `"2"`. Add the validator to CI with `uv run python resources/corpora/hr-policy/scripts/validate_data.py` from the repository root. Structural checks do not replace runtime selector/gate negative controls.
- Files: `resources/corpora/hr-policy/eval/gates.json`, `resources/corpora/hr-policy/eval/README.md`, `resources/corpora/hr-policy/scripts/validate_data.py`, `.github/workflows/checks.yml`, the project README's split policy if explicitly changed, roadmap S3–S6, and their registered contract dependencies.

**P2-2 · Verify U14, then separate citation from support.** Reproduce the unsupported-sentence probe with a committed script. If it holds, add a labelled negative control: a real citation plus an unsupported claim must fail the support check.

**P2-3 · Bound framework comparisons.** Every compare-once item states its question, inputs, time cap and keep/defer/drop exit. S3 keeps one main pipeline. The LangChain and LlamaIndex exposure becomes the same narrow path behind an adapter, not two full rebuilds. Proposed savings are roughly 12–25 learner hours, an unmeasured estimate; measure them before treating them as capacity for the S6 local release defense. Update the roadmap, library map and project summary consistently.

**P2-4 · S3 acceptance additions.** Minimum trusted eligibility (role, region, version) applies before ranking, from the first HR index. Add index lifecycle checks (stable document/chunk IDs, duplicate ingestion, update/delete, embedding-version mismatch). Report hit@5 and MRR with explicit denominators and corpus/index versions.

### Phase 3 — before S4, S5, S6 (≈ 6–10 h maintainer)

#### S4 — judge calibration and engineering decisions

Judge calibration records the rubric version and agreement, and inspects false acceptance of unsupported claims separately. A well-run experiment that rejects a change (for example reranking not worth its latency) counts as evaluation competence.

#### S5 — authorization and recovery (U13)

Separate *draft created*, *user confirmed submission* and *manager approved*. Approval is bound to the exact proposal hash and revalidated before execution. Treat a LangGraph interrupt as a pause, not authorization: side effects before an interrupt must be idempotent.

Add operational scenarios for crash after write before acknowledgement, replay after restart, altered approval arguments, cross-session confirmation and a stalled tool. Pair checkpointing with a small persistence/SQL exercise rather than a separate database course. MCP stays read-only. A second agent SDK is optional. Applicable RAG checks continue alongside agent gates.

#### S6 — integrated comparison and local release defense

A multi-agent design is not required to win; a simpler workflow that wins the measured comparison is the shipped result. Define memory ownership, expiry, deletion and contamination tests. CrewAI and screening stay optional.

The core local release defense requires a fresh-checkout run; a manifest covering code, prompt, model, corpus, index and eval set; tests in CI; redacted diagnostics; an injected-failure diagnosis; a guard-removal negative control; and an unfamiliar change the learner makes and explains. Selected exits also use an unfamiliar fictional corpus, so transfer is not just familiarity with two related codebases. Apply the combined required gate set, including optional-branch gates when that branch is selected.

### Phase 4 — optional, after the core

- **Delivery branch** (recommended before any broad job-ready claim): minimal API service, health check, container, persisted state, failure drill and rollback. About 16–26 learner hours. No Kubernetes, Terraform or multi-cloud.
- **Role-dependent extras:** SQL depth, classical-ML comparison literacy, model adaptation (prompting vs RAG vs fine-tuning on a measured failure).
- **T1–T5:** only as a deliberate separate commitment (220–320 h before reserve). Measure CPU throughput before promising training durations.

### Housekeeping (any time, ≈ 1–2 h)

- U12: fix the lab stage mappings to the current optional-phase references, remove the dead `hints.md` pointers, and relabel M1/M3 as historical.
- Add a "dated record; S0–S6 is current" banner to the top of `docs/review/CONSOLIDATION.md`.
- Decide whether to commit Audit B. If committed, consider removing the learner's name from its research section. Audit A's probe scripts (its Appendix C) were never supplied, so its reproductions rest on the panel's re-run.

## 5. Unified finding register

One ID scheme replaces Audit A's F1–F6 and Audit B's F0–F6.

| ID | Finding | A | B | Re-verified 2026-10-20 | Severity |
|---|---|:-:|:-:|---|---|
| **U1** | Case exposure recorded as `context` or `focus` is ignored by the freshness check, so a supplied answer can later count as fresh transfer (and retention) | F1 | F0 | Context reproduced by the existing local tests; focus transfer and retention reproduced in a temporary synthetic fixture during plan review. The original execution control remains historical evidence. | **P0** |
| **U2** | Stage hashes bind only the roadmap section; no stage declares `additional_contracts`, so mastery rules and gate changes leave old credit valid | F2 (P0) | F2 (P1) | Confirmed in code and `route.json` | **P1, blocks the first learner proof append** (resolves the P0/P1 split: no credit exists to go stale yet, but the first S0 proof must not be bound to an incomplete contract) |
| **U3** | Smoke and holdout share 8 IDs (q10, q30, q45, q65, q80, q85, q95, q120); S3 slices contain 12 holdout items; the full-set regression rule also touches holdout | F3 | F1 | Confirmed (59 S3 IDs, 12 held out) | **P1** |
| **U4** | S4 "every hard gate" imports the **Agent** gate (an S5 capability) and both **Screening** gates (optional in S6) | F4 (both) | F3 (screening only) | Confirmed; Audit B missed the Agent gate | **P1** |
| **U5** | Three conflicting improvement rules: eval README "must beat", roadmap S4 "beats or ties with a stated test", `gates.json` "merge unless McNemar p < .05 loss". A 5-loss/0-win change has p = 0.0625 and passes | F6 (partial) | F4 (partial) | Confirmed; the three-way conflict was found by the panel | **P1** |
| **U6** | S3 asks for MRR on the `out_of_scope` slice, where MRR is undefined | S3 review | — | Confirmed (roadmap S3 step 5) | **P1** (small) |
| **U7** | The HR validator is not run in CI and does not check split disjointness | F3 | F1 | Confirmed ([checks.yml](../../.github/workflows/checks.yml)) | **P1** |
| **U8** | The "whole number" matcher accepts `"2.5 days"` and `"2% raise"` for gold item `"2"` | — | F5 | Reproduced both | **P2, but fix before the S3 harness** (it defines correctness) |
| **U9** | Stage-level proof (one execution/explanation/transfer per stage) cannot show coverage of each critical capability | F5 | B3 | Confirmed by design (`derive()`) | **P1** |
| **U10** | S0 requires a full Mushir trace with no fallback when private access is unavailable | B9 | S0 review | Confirmed (roadmap S0). **S0 is the active stage** | **P1, now** |
| **U11** | Tracing authority conflict: roadmap says "LangSmith or Langfuse"; library map says LangSmith core from S2, Langfuse comparison in S4 | ✓ | — | Confirmed | P2 |
| **U12** | Stale labels: labs map to S6/S7 (S7 does not exist); `hints.md` pointers to missing files; eval README says "milestone M1", tool contract says "M3" | partial | F6 | Confirmed | P2 |
| **U13** | Approval wording: project README's "independent approver" conflates user confirmation with manager approval; LangGraph interrupts re-run the interrupted node on resume, so code before an interrupt is not exactly-once | ✓ | ✓ | README wording confirmed; LangGraph behaviour is from official docs (cited by Audit B), not re-run | P1 before S5 |
| **U14** | Current answer assertions may accept a real citation plus an unsupported added sentence | — | adversarial table | **Not re-verified** (Audit B gives no script) | Verify, then P1 before S3 |
| **U15** | The non-proof exposure bypass also grants retention | ✓ | ✓ | Reproduced during plan review: the existing context-retention regression fails; the temporary focus-retention probe also grants credit. | Covered by U1's tests |

## 6. Out of scope

No new curriculum, tutor or progress tracker. No reset of the learner's history. No framework added for coverage. No tests weakened to turn TODO scaffolds green. No Mushir corpus or AAOIFI text copied into this repository.
