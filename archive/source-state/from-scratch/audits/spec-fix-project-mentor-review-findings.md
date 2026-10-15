---
title: 'Fix Project Mentor Review Findings'
type: 'bugfix'
created: '2026-08-05'
status: 'done'
review_loop_iteration: 0
baseline_commit: '09b22566d942124ffb6d1acdd5b1eefa9d97dae4'
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** The mentor now opens in plain language, but it can mark orientation complete too
early, ask about unseen handbook content, bundle multiple learner outputs, forget confusion, load
unneeded evaluation answers, and pass hosted CI without any mentor-package contract check.

**Approach:** Make orientation a small sequence with project-owned acceptance criteria, persist
support needs separately from progress, reveal only evidence needed for the current question,
and add one standard-library structural contract check to required CI.

## Boundaries & Constraints

**Always:** Work only in `D:/AI Projects/ai-engineering-project-lab`; preserve learner ownership,
one-question turns, fixed evaluation evidence, current application behavior, stdlib-first checks,
and explicit separation between conceptual and runtime proof.

**Ask First:** Any change to learner-owned application code, evaluation cases, dependencies,
provider calls, costs, secrets, or the portfolio-wide tool policy.

**Never:** Modify `app.py`, its tests or evaluation data; mark confusion as mastery; reveal an
expected answer before the checkpoint permits it; run live-provider calls; add a dependency or
LLM call to CI; weaken the intentional paraphrase failure.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Fresh start | Bare `continue`; orientation pending | Plain mission and one refusal-risk question | No code, tools, or progress update |
| Mixed confusion | Attempt plus `I still don't understand` | Acknowledge useful part, persist support need, repair one idea | No grading, mastery, or advancement |
| Partial orientation | Correct refusal-risk answer | Keep orientation open; show one relevant handbook excerpt and ask one answer-only question | Never test unseen content |
| Supported path | Correct answer from shown excerpt | Advance to one source-identification question | Do not bundle answer and source |

</frozen-after-approval>

## Code Map

- `D:/AI Projects/ai-engineering-project-lab/.agents/skills/project-mentor/SKILL.md` -- mentor behavior.
- `D:/AI Projects/ai-engineering-project-lab/AGENTS.md` -- interaction contract.
- `D:/AI Projects/ai-engineering-project-lab/LEARNING.md` -- learner state.
- `D:/AI Projects/ai-engineering-project-lab/projects/grounded_support_assistant/README.md` --
  project-owned orientation rubric and capability sequence.
- `D:/AI Projects/ai-engineering-project-lab/scripts/check_mentor_contract.py` -- stdlib validator.
- `D:/AI Projects/ai-engineering-project-lab/.github/workflows/checks.yml` -- CI gate.

## Tasks & Acceptance

**Execution:**
- [x] `SKILL.md` and `AGENTS.md` -- make mixed confusion win, persist only support state, require
  shown evidence, one learner output, project-owned rubric, checkpoint-scoped evaluation reads,
  named errors for missing project assets, and no advancement after a failed state write.
- [x] `LEARNING.md` -- add stable `Demonstrated understanding` and `Support needed` fields while
  keeping the refusal-risk question as the sole current checkpoint.
- [x] Project README -- replace generic risks, separate orientation checkpoints from
  implementation slices, and express later work as capabilities; keep named tools in roadmap
  and tooling authorities.
- [x] `scripts/check_mentor_contract.py` -- validate skill frontmatter/interface and the four
  routing/progression contracts without third-party packages.
- [x] `checks.yml` -- run the contract validator before existing lint and tests.

**Acceptance Criteria:**
- Given mixed attempt and confusion, when routed, then confusion repair wins and only support
  state may change.
- Given only the refusal-risk answer, when reviewed, then orientation remains incomplete and a
  displayed handbook excerpt precedes one answer-only question.
- Given the supported answer passes, when advanced, then source identification is the sole next
  question.
- Given a future fresh session with support needed, when continued, then repair resumes before
  the ordinary next checkpoint.
- Given an orientation question, when composed, then every required fact is visible in that
  turn, project evidence is copied verbatim from its named source, and no expected evaluation
  answer is leaked early.
- Given the project guide, when scanned, then orientation checkpoints and implementation slices
  are distinct and future tools are not presented as predetermined production choices.
- Given CI, when the skill contract is broken, then the stdlib validator exits nonzero before
  lint or pytest.
- Given a missing active-project README or required evaluation asset, when state is loaded, then
  the mentor stops and names the missing or malformed artifact.
- Given a verified checkpoint whose `LEARNING.md` update fails, when closing the turn, then the
  mentor reports the failure and does not announce completion or advance the checkpoint.
- Given completion, when the diff is inspected, then no learner-owned application or evaluation
  file changed.

## Design Notes

CI validates the written contract and package shape, not nondeterministic LLM quality. Isolated
behavior probes provide the latter evidence; writable probes use only a temporary clone.

## Verification

**Commands:**
- `uv run python scripts/check_mentor_contract.py` -- expected: package and scenario contracts pass.
- `uv lock --check; uv run ruff check .; uv run ruff format --check .; uv run pytest -rxX -q` --
  expected: existing baseline remains 21 passed and one intentional xfail.
- System `quick_validate.py` against `.agents/skills/project-mentor` -- expected: skill is valid.
- Fresh read-only `continue`, confusion, mixed-input, and partial-orientation probes -- expected:
  matrix behavior above.
- Writable correct-answer probe in a temporary clone -- expected: only `LEARNING.md` changes and
  advances to the supported-answer checkpoint.

## Suggested Review Order

**Mentor behavior**

- Mixed confusion wins before grading or onboarding.
  [`SKILL.md:46`](../../../ai-engineering-project-lab/.agents/skills/project-mentor/SKILL.md#L46)

- Orientation advances through three separately demonstrated criteria.
  [`SKILL.md:81`](../../../ai-engineering-project-lab/.agents/skills/project-mentor/SKILL.md#L81)

- Project questions require verbatim evidence from validated sources.
  [`SKILL.md:95`](../../../ai-engineering-project-lab/.agents/skills/project-mentor/SKILL.md#L95)

- State writes stop on concurrent changes or failed verification.
  [`SKILL.md:165`](../../../ai-engineering-project-lab/.agents/skills/project-mentor/SKILL.md#L165)

**Learner contract**

- Repository-wide rules mirror routing, evidence, and write safeguards.
  [`AGENTS.md:28`](../../../ai-engineering-project-lab/AGENTS.md#L28)

- Canonical fields separate demonstrated knowledge from support needs.
  [`LEARNING.md:41`](../../../ai-engineering-project-lab/LEARNING.md#L41)

- Orientation criteria are distinct from learner-owned implementation slices.
  [`README.md:46`](../../../ai-engineering-project-lab/projects/grounded_support_assistant/README.md#L46)

**Deterministic validation**

- Active-project paths and linked assets are resolved inside the repository.
  [`check_mentor_contract.py:71`](../../../ai-engineering-project-lab/scripts/check_mentor_contract.py#L71)

- Evaluation JSON is parsed and checked against the fixed contract.
  [`check_mentor_contract.py:268`](../../../ai-engineering-project-lab/scripts/check_mentor_contract.py#L268)

- CI runs the mentor contract before lint and application tests.
  [`checks.yml:20`](../../../ai-engineering-project-lab/.github/workflows/checks.yml#L20)
