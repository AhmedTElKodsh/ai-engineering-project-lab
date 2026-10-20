# Consolidated candidate: educational acceptance review

Reviewed 12 October 2026, read-only candidate at `D:/AI Projects/Learning/ai-engineering-project-lab-unified`. This report evaluates instructional coherence and declared acceptance, not learner competence, runtime quality, or provider/API currency. No provider was contacted and no candidate implementation was edited.

## Acceptance judgment

The candidate has the requested educational coverage and a credible single-project spine, but its active planning documents still contain contradictory instructions. Repair the findings below before treating the planning package as a consistent governing contract. This is a document acceptance issue, not missing evidence that the learner has completed the planned route.

The required pace is consistently ten hours/week, five two-hour sessions; CPU is required and the old GPU is optional/unverified. S0/S1 specify observable intermediate Python tasks instead of assuming broad mastery. S2/S3 include prompting, structured output, genuine semantic retrieval, grounded RAG, bounded agents, tools, state, evaluation and an educational MCP bridge. S4–S8 require count models, manual gradients/backprop, learner-owned causal architecture, random-weight training, evaluation, checkpoint/resume, generation and bounded adaptation. Model specification §§Outcome, Verification and Fair Comparisons distinguish a complete small language model from a hosted call, pretrained adaptation, toy forward block, or frontier capability.

Current implementation/learning evidence remains narrow: the model directory contains only README.md; state shows every S0–S8 gate unresolved; the single ledger event is maintainer migration context. README and project/model/resource READMEs accurately label the lexical app as inherited reference code and the retained labs as incomplete preparation. Their baseline performance claims were not independently executed in this review. No learner achievement follows from this review or maintenance tests.

## Findings

### 1. High: the governing roadmap still relocates the learner outside the adopted project

- `docs/learning-path/02-PROJECT-ROADMAP.md:7–11` calls the components Project A and Project B, says they may live in a future separate learner repository, and instructs “Do not build the learner app inside this curriculum checkout.”
- `:179` imports the old curriculum dependency ban, including Pydantic, and requires framework comparisons in a separately governed learner workspace.
- This conflicts with root README:3–7, project-context.md:3–5, TOOLING.md:3–9 and project README:20–24. AGENTS.md:9 and README:23 explicitly make this roadmap the acceptance owner, so the stale text can actively redirect tutoring or prohibit the inherited dependency.
- Fix: define A/B as releases of the assistant and internal model components inside `projects/grounded_support_assistant`, replace the future-repository prohibition with the adopted learner workspace, and refer to TOOLING.md for this project's dependency boundaries. The external curriculum's rules should apply only when contributing there.

### 2. High: the indexed learning method does not implement the updated ownership/hint rule

- `docs/learning-path/01-LEARNING-METHOD.md:49–59` permits “pseudocode” without restricting it to incomplete guidance and H4 “a complete small mechanism,” with the broad justification that H4 is appropriate for new learning.
- Root README:42 presents this as an owner of session method and gradual help. Its text lacks the diagnostic-question rung, guard against serial leakage of the active algorithm, the attempt + useful hints + explicit more-help condition for a smallest tricky fragment, and the explicit-full-solution request boundary.
- AGENTS.md:15–19 and mentor SKILL.md:47–61 already state the requested stronger rule correctly, but an active instructional document should not invite an exception by omission/ambiguity. A complete unrelated toy mechanism is compatible; a complete active mechanism by default is not.
- Fix: synchronize the ladder with those owners, say incomplete pseudocode, restrict demonstrations to unrelated examples, explicitly guard serial algorithm leakage, and add the exact conditions for partial/full solution help and later fresh independent evidence.

### 3. Medium: retention help and stage completion terminology conflict across owners

- `docs/learning-path/00-START-HERE.md:84–89` says stage completion includes delayed retention “with limited help.”
- `docs/learning-path/03-SKILLS-AND-MASTERY.md:78` says stage exit normally requires M3 with retention toward M4 still scheduled.
- `learning/PROTOCOL.md:11` and mentor SKILL.md:94–96 distinguish readiness from retained completion and exclude AI solution/hints from retention.
- A tutor following the entry document could award retention after hints, while the writer rejects that claim; a tutor using “exit” could mistake readiness for final retained completion.
- Fix: use the same two terms everywhere: readiness permits advancement after execution/explanation/fresh independent transfer; retained completion additionally requires the separate fresh delayed case without AI hints/solution, with disclosed syntax references allowed. Assisted revisit is practice, not retained closure.

### 4. Medium: S3's offline prerequisite alternative cannot be selected by the authoritative route

- `docs/learning-path/02-PROJECT-ROADMAP.md:78` allows S3 after tested offline A2 orchestration while live behavior is pending.
- `learning/route.json:65–67` unconditionally requires S2. `scripts/learning_state.py:152–164` makes prerequisites ready and selects focus only among eligible stages. PROTOCOL:13 requires the complete declared contract for a stage pass, so a pending S2 live gate cannot honestly make S2 ready.
- Offline S4 is correctly available after S1 and is a valid escape path, but offline S3 is advertised as a second path without executable support.
- Fix: simplest is to remove the S3 prerequisite alternative and make preparatory fake-tool practice part of incomplete S2; route eligible independent work through S4. Alternatively explicitly model partial prerequisites without awarding S2 readiness, then verify routing semantics. Do not fabricate an S2 pass to unlock S3.

### 5. Medium: the introductory route diagram still makes applied completion precede the math branch

- `docs/learning-path/00-START-HERE.md:39–49` draws a solid S3 → S4 dependency and a dotted S1 → S4 connection labelled shared contracts.
- `learning/route.json:81–83` actually requires only S1 for S4, enabling CPU work while provider gates remain pending. The method and mentor explicitly rely on this offline branch.
- Fix: represent actual prerequisites with solid edges S1 → S4, and both S3 and S7 → S8. Keep shared evaluation/corpus connections visually distinct and label them as conceptual rather than prerequisites. Readers should not infer a second linear route from the entry diagram.

## Historical material and portability

`docs/learning-path/07-ROUND-TABLE-AND-DECISIONS.md:23,69,75` preserves old two-project/proposal activation language, but its opening calls it a planning snapshot and :80–82 explicitly declares those earlier activation statements historical and adopts one workbench. That is materially different from finding 1's active acceptance owner. Improve scanning by moving the adoption status immediately below the title or marking the older decision table historical; do not treat the recorded earlier disagreement itself as a current instruction.

The selected active Markdown files' relative links were checked for target existence. Only the deliberately pending `docs/review/CONSOLIDATION.md` links were missing at inspection; those were excluded as instructed because the parent is writing that file. No other broken relative link or machine-specific absolute Markdown link was found in the specified active scope. Upstream curriculum links are pinned HTTPS references; their remote availability/content was not revalidated here. There is one active route file/state view and one installed mentor; historical archive state is labelled superseded rather than a competing progress owner.

## Recommended final check

After the document fixes, rerun the structural validator, route/state validation and relative-link check, then reread all indexed authority documents for the same tutoring, readiness/retention, workspace and offline-prerequisite rules. Structural passing should be described as package validation, not evidence of real tutoring effectiveness, learner retention, live RAG quality, or a trained model.
