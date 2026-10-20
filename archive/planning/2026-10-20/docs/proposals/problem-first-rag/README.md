# Problem-first RAG learning project: planning pack

Prepared 20 October 2026. **Status: proposed design; not the active learning route.**

The learner wants to build a progressively more useful RAG system, starting with the
problem it solves and learning concepts when they become necessary. The AI tutors;
the learner writes the important implementation. This pack supplies the brief,
release contracts, data, evaluation rules and agent handoffs for that approach.

## Start here

| File | Purpose | Who reads it |
|---|---|---|
| [01-PROBLEM-BRIEF.md](01-PROBLEM-BRIEF.md) | Users, pains, limits and what success looks like | Learner and tutor |
| [02-PROGRESSIVE-RELEASES.md](02-PROGRESSIVE-RELEASES.md) | Small releases driven by observable problems | Tutor, learner and curriculum maintainer |
| [03-TUTOR-OPERATING-CONTRACT.md](03-TUTOR-OPERATING-CONTRACT.md) | How to guide without completing the learner's work | Tutor |
| [04-DATA-AND-EVALUATION.md](04-DATA-AND-EVALUATION.md) | Starter fixture, staged data expansion and honest assessment | Tutor and evaluator |
| [05-COMPARISON-AND-ADOPTION.md](05-COMPARISON-AND-ADOPTION.md) | Comparison with the current plan and exact adoption boundaries | Learner and maintainer |
| [06-AGENT-HANDOFFS.md](06-AGENT-HANDOFFS.md) | Copyable prompts for review, adoption and tutoring | Agent operator |
| [07-VERIFICATION.md](07-VERIFICATION.md) | Observed checks, existing failures and limits of this delivery | Reviewer |
| [data/starter-corpus.json](data/starter-corpus.json) | Nine short passages from three existing fictional policy families | R0–R3 development |
| [data/dev-cases.json](data/dev-cases.json) | Twelve exposed development cases with expectations | Development only |

Read the brief and comparison first. Use the handoff appropriate to the current task;
do not feed every repository file and evaluation answer into the tutor context.

## Design decision

Use **one employee policy help desk** throughout the project. Start with a tiny
subset of the repository's existing Nilebyte Solutions synthetic corpus. Grow into
its mixed-format, multilingual and access-controlled problems later. The starter
fixture is supplied data, not learner-authored implementation or assessment proof.

The default progression is: find a passage → produce a supported answer → handle
different wording → ingest harder sources → respect eligibility and versions →
measure improvements → handle conversation. Tools and agents are an extension when
the user needs a lookup or action that document search cannot provide.

## Authority and activation

This directory is a dormant planning proposal, not a second tutor, route or tracker.
R0–R9 below are **product release labels**, not new stage IDs or ledger values.
Current [route facts](../../../learning/route.json),
[acceptance](../../learning-path/02-PROJECT-ROADMAP.md),
[library assignments](../../learning-path/08-LIBRARY-MAP.md),
[evidence protocol](../../../learning/PROTOCOL.md), and
[single mentor skill](../../../.agents/skills/project-mentor/SKILL.md) remain authoritative.

The user authorized preparation of this pack. It does not activate a curriculum
change, implement learner modules, run a provider, or award progress. A future
adoption task must reconcile the proposal into those existing owners; the pack
then becomes a dated design record. Never resolve conflicts by treating this pack
as higher authority than the repository agreement.

## Verified starting point and assumptions

- Inspected HEAD: `835d97ec9137962807852859494e68bf90a4bd43`, with local changes.
- `learning_state.py status` validated on 20 October: S0 active; every stage
  `not_started`; evidence revision
  `d47a29c5f6abb00dbf4ba2e802a69736f8fe9440c7b76aa571c90177c450b31c`.
- The existing project already has a problem briefing and a lexical reference
  implementation. This proposal changes the sequence and consistency of practice.
- Working assumptions: English first, CPU first, local CLI first, five two-hour
  sessions per week, private Mushir application remains a separate boundary.
- No external dataset download is needed. No claim that this teaching design is
  empirically better has been established; pilot it using the comparison criteria.

Existing local state-writer/test edits and both review documents were present before
this pack. They are not changes or completed repairs delivered by this proposal.
