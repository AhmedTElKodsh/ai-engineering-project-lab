---
title: 'Implement Python-to-LLM audit corrections'
type: 'bugfix'
created: '2026-10-12'
status: 'in-progress'
baseline_commit: '7157ca74a135fad2165f680ec4b4e592f075ec21'
review_loop_iteration: 0
context: ['AGENTS.md', '_bmad-output/planning-artifacts/python-to-llm-audit-2026-10-12.md']
---

<frozen-after-approval reason="User authorized all required audit modifications on 12 October 2026">

## Intent

**Problem:** The reviewed project plan has inconsistent progression and assessment rules, unsafe route-state interpretation, and mapped references that cannot establish the intended learning/training claims.

**Approach:** Implement all fifteen audit corrections across the plan, resolver, evidence protocol, tutoring instructions, and reference qualifications, with focused regression checks. Provide a validated candidate project route without silently activating it or awarding learner progress.

## Boundaries & Constraints

**Always:** Preserve existing learner ownership, source history, working changes, dependency allowlist, tagged fences, and original implementations. Keep attempts, focused bridges, eligible full completion, ready-to-advance, and retained evidence distinct. Use CPU-first scoped work and original small fixtures. Qualify incomplete demonstrations rather than expanding the learner scope into repairing all curriculum implementations.

**Ask First:** Actual route activation, learner workspace creation, provider spending, publication, and complete learner exercise solutions remain separate actions unless already authorized explicitly.

**Never:** Reset the working tree, install forbidden dependencies, create learner implementation files, claim current mastery, or present random updates/simulated metrics as real training/evaluation.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|---|---|---|---|
| Existing route | Valid lesson manifest, no completed rows | Same next lesson; existing route remains active | Explicit JSON errors for invalid state |
| Project candidate | Required S0-S8 project stages | Every required stage resolves through its own evidence category | Reject empty/unknown stages, invalid flags/modes, duplicates |
| Study evidence | Attempt, failed/incomplete row, focused bridge | Does not satisfy full completion or project readiness | Explain missing evidence without erasing prior work |
| Retention | Independent transfer passed, delayed check pending/failed | Advancement and retained status remain separate | Targeted repair; no automatic whole-phase restart |
| Tokenizer | Arabic, mixed Unicode, literal control spelling | No lost ordinary text; declared normalization/control policy | Reject invalid IDs; controls require explicit opt-in |
| Reference comparison | Partial backward, random-noise SFT, simulated scores | Clearly excluded from training/measurement correctness comparisons | Point to stronger learner verification gates |

</frozen-after-approval>

## Code Map

- `scripts/next_learning_route.py` resolves and validates scheduling/state.
- `docs/learning-path/` contains active route, candidate route, and evidence policy.
- `.agents/skills/learn`, `check-understanding`, `find-your-level` drive tutoring and assessment; inspect installed mirror copies too.
- `_bmad-output/planning-artifacts/python-to-llm-2026-10-11/00-07` contain the reviewed proposal and mappings.
- `phases/10-llms-from-scratch/{02-building-a-tokenizer,04-pre-training-mini-gpt,06-instruction-tuning-sft,10-evaluation}` contain affected reference routines.

## Tasks & Acceptance

**Execution:**
- [ ] Harden `scripts/next_learning_route.py`, add resolver tests, and create a validated candidate project manifest plus evidence protocol (A1-A2).
- [ ] Align tutoring/assessment skills and AGENTS.md with evidence categories, advancement/retention, and targeted repairs (A2-A5).
- [ ] Update proposal 00-07 for diagnostic sampling, data identity/offsets, exact-action approvals, graph bridge, scoring/batching/adaptation contracts, assistant practice, and S8 slices (A3-A9, A13-A15).
- [ ] Correct stdlib tokenizer coverage/control policy with tests; qualify partial training, invalid SFT, and simulated evaluation in source/docs and mappings (A10-A13).
- [ ] Record each A1-A15 resolution, verify local links and consistent scope, and preserve the historical audit as the reviewed snapshot.

**Acceptance Criteria:**
- Given the current active manifest, when normal resolution runs, then it preserves lesson selection and learner progress.
- Given unsupported or empty required stages, when validation runs, then it fails explicitly rather than silently dropping work.
- Given attempts or bridges, when resolving a full requirement, then only eligible completion evidence closes it.
- Given the candidate project route, when validated and resolved with empty evidence, then it schedules S0 and includes all nine project gates.
- Given delayed retention pending, when an independent gate passes, then the tutor can advance with visible pending retention and no retained-mastery claim.
- Given changed data without learner construction, when assessed, then it is not recorded as independent construction.
- Given reference comparison tasks, when preparing instruction, then unsafe routines are explicitly excluded and correct mechanism tests are specified.
- Given all fifteen findings, when the resolution report is read, then each has a concrete modification and appropriate verification, without invented learner results.

## Spec Change Log

## Design Notes

The user's implementation instruction supplies approval for the reviewed corrections. Existing dirty work was documented during the audit and is preserved. Formal adoption is distinct from repairing and validating the candidate route. Numeric quizzes remain useful diagnostics; they do not substitute for authorship/retention evidence. Reference qualification fulfills the audit's minimum correction without expanding into a complete manual-transformer training rewrite.

## Verification

- `python -X utf8 -m unittest discover -s scripts/tests -v` -- scheduling/evidence regressions pass.
- `python -X utf8 scripts/next_learning_route.py --project-root . --validate` -- current manifest valid.
- Candidate route validation/resolution -- all required project stages supported, S0 next with no learner evidence.
- Tokenizer canonical demo and stdlib tests -- Unicode/control regressions pass.
- `python -X utf8 scripts/audit_lessons.py` and `python -X utf8 scripts/check_readme_counts.py` -- inspect results and distinguish pre-existing curriculum issues.
- Link, fence, source-warning, and A1-A15 coverage checks -- no missing local references or unresolved required corrections.
