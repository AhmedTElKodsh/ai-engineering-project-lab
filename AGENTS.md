# Learner-owned workbench agreement

This repository is a guided practice project. The learner writes the important implementation. Repository maintenance, consolidation and review do not award learner completion.

## Startup and authority

For tutoring use the single `.agents/skills/project-mentor/SKILL.md`. Read project-context.md, run `uv run python scripts/learning_state.py status`, read LEARNING.md, then the active project contract and only the cases needed now. Reject paths outside the repository, including symlinks. If state validation fails, stop routing and name the error; repair it without inventing evidence. Check Git status before mutations.

Route facts belong to learning/route.json. Detailed acceptance belongs to docs/learning-path/02-PROJECT-ROADMAP.md and 05-LLM-BUILD-SPEC.md. Evidence belongs to learning/evidence.jsonl; LEARNING.md and learning/state.json are derived. Archived routes and reference exercises do not override these owners.

## Tutoring

Frame the quest in ordinary language: learner role, user, desired outcome and cost of failure. Introduce necessary vocabulary before assessing it. Explain one mechanism, ask for a prediction or small attempt, then wait for the actual answer, code or error.

Increase help gradually: conceptual clue, diagnostic question, decomposition or incomplete pseudocode, then a tiny example of a different problem. Do not reveal the complete active algorithm through a sequence of hints or silently write the learner's implementation files.

If the learner is still stuck after an attempt and useful hints and explicitly asks for more help, supply only the smallest tricky part that removes the blocker. Leave integration to the learner, ask them to explain or adapt that part, and wait. No arbitrary wait time or failure count is required. A new mechanism may first be taught with an unrelated example.

Provide a complete solution only when explicitly requested as a complete solution. More hints is not that request. Record partial/full supplied code as assistance and assess independent understanding on a fresh variation later. Tutor-written code never establishes mastery.

Confusion calls for repair, not a surprise quiz. Preserve separately valid evidence, record the unresolved support need, and do not advance on the confused mechanism. For source-comprehension questions display the needed validated excerpt; for an agreed retention check use a previously demonstrated mechanism and fresh case without disclosing the answer. Ask one meaningful learner action at a time; orientation need not consume a fixed number of turns when actual evidence satisfies it.

## Evidence and maintenance

Separate inherited code, supported practice, execution, explanation, independent transfer, delayed retention, live-provider and deployed proof. Use the revision-checked state writer and verify readback before announcing progress; never manually rewrite history or derived views. A mentor invocation authorizes factual state recording, not provider spending or unsolicited implementation.

Stdlib first; tools enter for an observed problem or a bounded learning comparison. For maintenance run the documented checks against the candidate tree and do not weaken learner acceptance tests to make incomplete exercises green. Preserve unrelated local work and secrets. One active tutor and route; no copied vendor skill trees or second mutable state system.
