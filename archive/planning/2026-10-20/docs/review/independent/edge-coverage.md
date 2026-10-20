# Independent blind edge-case coverage: projects A-C

Reviewed 2026-10-11 with the supplied edge-case-hunter skill, full-content scope for native executable paths. Only anonymized snapshots were opened. No mapping, originals, other reviewer reports, providers, network, installs, Git mutations, or source edits were used. Findings carry the skill's four fields; there was no diff, so deletion review did not apply.

## Scope and path enumeration

- **A:** native `tools/validate_workspace.py`, `tools/sync_tutor_skill.py`, canonical tutor skill, current/skills/evidence fixtures, migration, evidence protocol, teaching/lesson shapes, route and assessment contracts. Traced initialization, exact schema keys, provider/version metadata, timestamp ordering and mixed precision, source containment, setup milestones, gate/skill references, readiness and historical prerequisites, corrections, overlapping evidence freshness, cross-stage failure reconciliation, final capability coverage, assistance levels, app location, review queues, snapshot/log revision agreement, document links/anchors, mirror copies, and self-test/CLI error paths.
- **B:** native application, fixed evaluation and tests, mentor-contract checker, mentor skill, learner state, active-project contract/handbook, contributor authority and adoption rules. Traced absolute/escaping source paths, malformed linked assets, fixed case schema, request length/whitespace, termless and non-Latin input, empty sections, lexical overlap/abstention, multiple-topic requests, invalid output fields, confusion/attempt precedence, independent orientation criteria, support repair, exact-tree runtime evidence, concurrent-state reread and failed-write guards.
- **C:** standalone and installed coaching skill/helper, helper tests, bundle validator, template filenames, backlog/progress protocol, records/assessment/review contracts and current project architecture/data/API/RAG/evaluation/security contracts. Traced JSON loading, schemas and enums, graph cycles/dependencies/release levels, evidence files and assistance, recommendations after errors, init refusal/copy/validation branches, derived-copy drift, checkpoint concurrency, failure and regression handling, scoped model tools, approval expiry/version/hash/separation, case/proposal transitions, replay/unknown outcomes, worker retry and activation boundaries. The SupportOps reference starter's validator, tutor/progress contracts and fixture tests were read as reference material, never mixed into the active project. Bundled vendor skills and frozen archive builders were excluded from active execution.

## Actual offline executions

| Project | Command | Observed result |
|---|---|---|
| A | `python -B tools/validate_workspace.py --self-test` | Exit 0; native state/evidence + 22 owned documents pass; 104 in-memory fixtures pass. |
| B | `python -B scripts/check_mentor_contract.py` | Exit 0; written package/contract passes. |
| B | `python -B -m unittest discover -s projects/grounded_support_assistant -v` | Zero tests discovered; these tests use pytest, so this is no test evidence. |
| B | `python -B -m pytest -p no:cacheprovider -rxX -q` | Exit 0; 21 passed, 1 strict expected failure. Evaluation itself: 19/20 pass, documented paraphrase xfail; 2 output/input contract tests pass. |
| C | `python -B -m unittest discover -s tests -v` from standalone skill | 45 tests: 42 pass, 1 failure, 2 skips. Failure: initialized template lacks `docs/09-backlog.md`. Symlink tests skip because this host cannot create the symlinks. Temporary test directories were cleaned by tests. |
| C | `python -B skills/commerce-ai-coach/scripts/coach.py validate --project projects/commerce-support-copilot --json` | Exit 0; 30 task records, no errors/warnings. This is structure evidence only. |
| C | `python -B tools/validate_bundle.py --skip-tests` | Exit 1; 13 checks pass, 70 problems: 9 installed-skill differences and 61 template differences. No `--sync` was run. |

Available interpreter was existing `C:/Users/Asd/anaconda3/python.exe`, Python 3.13.9. The `py` launcher was unavailable. Bytecode/cache writes were disabled. One probe's output initially hit the host's cp1252 stdout limitation when printing Arabic; it was rerun with UTF-8 output. No provider or application quality claims follow from validator/test success.

## Minimal reproduction details

### A: partial supersession of multi-capability proof

Loaded the frozen initial fixture in memory. Appended a passing `execution` event `multi` at milestone 0.3 tagged E03 and E04, set only E03 to practiced referencing it, and appended `only-E04-fails` with the same kind/milestone but only E04. Snapshot revision fields were updated consistently. `validate_state` rejected E03 with `stale evidence cannot support status: skill E03 references multi, but only-E04-fails is a later overlapping execution`. No E03 failure occurred. The protocol permits genuinely multi-tagged evidence and says claims should remain current for their specific capability. Milestone-wide/gate overlap behavior can remain separate from capability-specific reference freshness.

### B: unsupported matched subject and empty content

The actual corpus answers `What is the subscription refund interest rate?` and `Can my refund subscription cure chest pain?` with the Refund policy body, a citation and `abstained: false`; neither requested fact exists. This differs from the explicitly documented paraphrase false negative. A no-file-write `load_sections` mock containing `Section('fixture.md', 'refund subscription', '')` similarly returns an empty cited answer and `abstained: false` for `refund subscription`. The real parser admits that section shape because it checks the heading, not a nonempty body. Stopword-only and Arabic-only questions raise the explicit no-searchable-term ValueError; these were treated as handled rejection paths, not findings. Multi-topic questions return only the top section; no additional finding was emitted beyond the unsupported-answer boundary.

### C: structure does not make invalid status safe for routing

Deep-copied actual progress/backlog and mocked only `load_project`. Marking T001 done with no evidence produces two validation errors, yet `cmd_status --json` returns exit 0, recommends T002, and considers T002/T003 ready. Replacing `current_task` with `[]` produces an uncaught TypeError, `unhashable type: list`, instead of a Report/LoadError. The normal current project validates, so these are controlled input probes, not assertions that current learner records are corrupt.

### C: derived artifact and concurrent checkpoint failures

On the actual active project, installed references `learning/LEARNER_PROFILE.md`, `learning/PROGRESS_PROTOCOL.md`, and `docs/02_ARCHITECTURE.md` do not exist. `learning/CURRICULUM.md` does resolve on this case-insensitive Windows filesystem; it was not counted as missing. Standalone template canonical paths `docs/09-backlog.md`, `docs/02-architecture.md`, and `learning/progress-protocol.md` are absent because the supplied template uses underscores. The existing init unit test reproduced the first missing path.

For the write protocol, two copies of the same initial progress were made in memory. First added an independent mastery entry for T001. Second added T001 implementation experiment evidence, leaving the initial unassessed mastery. Taking the second whole-file checkpoint loses the first entry; validation reports zero errors. Neither protocol nor learning-specific instructions requires writer serialization, compare-before-save, revision binding, or validated readback. This is a demonstrated representable lost-update path, not a real write to the snapshot.

### C: specification-only transition/tool gaps

The case transition table explicitly rejects unlisted transitions. `POST /cases/{id}/messages` promises an accepted employee message without a resolved-state guard, but only awaiting_information, escalated and failed cases have a new-message continuation. A resolved read-only case has no continuation path. Separately, the tool table calls `order_line_id` a model-visible `propose_replacement` argument while the contract and project agent rules forbid model-supplied internal IDs. Case-to-order checks already prevent a foreign-order write; the remaining finding is the reachable incompatibility between tool input and the identity boundary. These are planning-contract findings; no commerce application exists to execute them.

## Handled paths deliberately excluded

A already enforces separate execution/understanding, legal setup evidence, assistance-sensitive ownership, delayed transfer rather than midnight, durable readiness, historical prerequisite timing, corrections, conservative failure reconciliation, final route retention, source containment, snapshot/log revision agreement, readback and single-writer instructions. Its validator explicitly cannot prove the truth of an observation.

B already defines mixed-confusion priority, three separate orientation turns, source grounding in the current message, validated relative active-project paths, runtime-versus-conceptual evidence, before-write state comparison and failed-persistence stopping. The paraphrase xfail is intentional and not a new finding.

C already differentiates implemented work, learner mastery, observed versus reported evidence and fake versus live evaluation. Its written regression rule requires reopening done work and retaining failed review evidence. An in-memory done record with older passing reviews plus a later failing review does validate and routes forward, but the documented reopening rule handles that tutoring action; therefore it is recorded here as a machine-enforcement limit rather than duplicated as an unhandled-contract finding. Schema-v1 compatibility and missing assistance defaults are also intentional compatibility behavior, not reported defects. Order/tenant binding, immutable approval/hash, manager separation, stock and duplicate constraints, expiry, replay and ambiguous-write reconciliation have explicit planning guards. No speculative runtime defect was inferred for these unimplemented features.

## Reusable protections

Retain A's event log, scope-specific evidence references, independent/supported distinction, durable readiness and final retention checks, while making shared proof freshness capability-specific. Retain B's learner-owned orientation and concurrent state reread; add abstention tests where a question overlaps the subject but requests an absent fact. Retain C's task graph, separate completion/mastery and fake-adapter-first policy; fail closed on validation before recommending dependent work, reject malformed scalars, verify canonical paths in every shipped copy, and serialize checkpoint writes with readback. Planning status transitions and model-visible arguments should each have one mechanically checkable source.

The new 10-hour CPU-first, cumulative Python/RAG/agents/ML/DL and random-weight small-LM objectives were treated as context. This edge review does not claim these existing tracks fulfill all those curriculum objectives; comparing or extending curriculum scope belongs to the separate synthesis. Host tutoring behavior, learner retention, live APIs, paid models, and application runtime for unimplemented plans remain unmeasured.
