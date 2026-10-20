# S0 session 1 — a missed leave deadline

**Mode:** supported project practice only. **Stage/capability:** S0 / S0.user_problem. Do not grade independent mastery or close a gate while P1-B is pending.

## The employee problem

You have joined the support/engineering team of **Nilebyte Solutions**, a fictional employer. An employee asks about unused annual leave that might expire. They need the published rule and a checkable source. A wrong or invented date could change how they plan leave.

## Approved source, displayed before the question

**Record:** pf-leave-carryover  
**Policy:** HR-LV-01 — Leave Policy  
**Version:** 2026.1  
**Section:** 2.6 Carryover  
**Source fixture date:** 2026-09-24

> 2.6 Carryover. Up to 5 unused annual leave days may be carried over into the next calendar year. Carried-over days must be used by 31 March of that year, after which they expire. Unused days above the carryover limit are forfeited and are not paid out, except on leaving the company (see 2.8).

This text is the supplied, visible practice excerpt from the current repository's **starter-corpus.json**. It is not a personal leave-balance lookup and does not prove a particular employee's leave balance.

## Exactly one learner action

**In your own words, explain what could go wrong for this employee if the assistant invented a carryover deadline instead of using the cited policy.** Answer in two or three sentences. Do not write code yet.

**Return:** your explanation.  
**Observable evidence:** the response connects an unsupported deadline with the employee's decision and identifies why the published source matters. The tutor should review what the learner actually says rather than supplying a model answer.

## Tutor continuation (only after the attempt)

Review that one answer first. If a misconception appears, teach one needed term or boundary and allow repair. Next choose the active capability/action from the canonical route and only the relevant excerpt. Later S0 asks the learner to separate a general policy rule from unknown personal state and to trace a **manual** answer path; it does not require a Groq key, HTTP client, new vector store or Mushir access.

To inspect the actual state locally, use the documented read-only commands in a **verified repository root**: check Git status, run **uv run python scripts/learning_state.py status**, then **uv run python scripts/check_s0_readiness.py**. These are not evidence of the learner's competence or of an isolated tutor-host pilot. A remote-only assistant must label the commands **not executed**.
