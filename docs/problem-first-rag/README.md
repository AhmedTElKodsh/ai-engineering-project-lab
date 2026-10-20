# Problem-first RAG: guided entry point

This is an **additive tutoring and exercise aid**, reviewed on 20 October 2026. It is not a replacement curriculum, release contract, evaluation benchmark, application or learning-state authority.

## The active problem

You are the junior AI engineer supporting fictional Nilebyte Solutions employees. Employees need a **current, source-backed HR policy answer**, not a confident guess. An invented leave deadline could cause real confusion or lost entitlement. Begin by distinguishing a published rule from a person's current situation and by showing where the rule came from.

**Start with [First session](FIRST-SESSION.md).** It displays the approved current S0 excerpt and asks one learner action. Do not start with an implementation, a model download or a lecture on embeddings.

## Source of truth and precedence

1. Root **AGENTS.md**, **project-context.md** and **.agents/skills/project-mentor/SKILL.md** govern agent behavior.
2. **learning/route.json** and **docs/learning-path/02-PROJECT-ROADMAP.md** define the one current S0-S6 route, capabilities, dependencies, release requirements and library placement.
3. **learning/evidence.jsonl** with **scripts/learning_state.py** is the only progress log/writer. **LEARNING.md** and **learning/state.json** are derived; never edit them directly.
4. **projects/grounded_support_assistant/data/starter-corpus.json** contains nine supplied source passages, including **pf-leave-carryover**. The twelve **starter-dev-cases.json** cases are exposed development cases, not unseen assessment.
5. **resources/corpora/hr-policy/** remains the larger fictional corpus for later stages. The inherited Acme handbook and lexical application are labelled reference code, not the new HR solution or learner authorship.

The older external Acme/customer-export planning pack is a **reference only**. Its eleven-document independent micro-corpus and twenty-two development cases must not be silently mixed into either repository fixture or any holdout.

## Problem -> stage -> observable work

| Stage | User problem | Learner outcome |
|---|---|---|
| S0 | A published leave rule must not turn into an invented personal deadline | Explain the employee risk, identify supported evidence, trace a manual answer boundary |
| S1 | Employees need to find the right passage without manual browsing | Learner-built typed loader, BM25 lexical search, citations, tests and reproducible local run |
| S2 | A relevant passage must become a short answer without unsupported claims | Validated structured responses, fake failure tests, budgeted live call and redacted tracing |
| S3 | Different wording and document layouts defeat the simple system | Measured semantic retrieval, parsing, chunking, index lifecycle and pre-ranking eligibility |
| S4 | Applicable rules conflict or evolve, and changes have uncertain impact | Security, time/region rules, conversations and paired retrieval/answer evaluation |
| S5 | Personal HR information needs authenticated tools and controlled drafts | Fake scoped tools, approvals, replay/recovery handling, bounded agent/workflow |
| S6 | Another engineer must reproduce and defend the combined local release | Tests/CI, tracing, reproducible manifests, guarded integration and independent defense |

A multi-agent design is **not mandatory** for S6. A simpler workflow is preferable when evidence supports it. Do not claim an S-stage completed because a tutor produced code or a test passed.

## Current readiness

The remote read-only state showed **S0 not_started** and a pending **P1-B actual isolated mentor-host behavioral pilot** before the first mastery decision. **Supported S0 practice is permitted**; independent mastery/transfer must not be awarded while the blocker remains. Re-check status in a verified writable checkout.

## Files in this additive aid

- [Two-pass review](REVIEW-2026-10-20.md): issues found, precise adaptations and validation limits.
- [First session](FIRST-SESSION.md): one approved source passage and one learner action.
- [Task cards](TASK-CARDS.md): a problem-first teaching map; never activate tasks ahead of the route.
- [Tutor handoff](TUTOR-HANDOFF.md): concise prompt for agents with the single-authority rule.

Do not modify the active student implementation to demonstrate progress. The next product change belongs to the learner after the relevant stage becomes eligible.
