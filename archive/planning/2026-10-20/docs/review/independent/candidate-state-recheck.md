# Candidate state repair recheck

Reviewed 2026-10-12 against the current candidate progress code, state tests, protocol, and stage-scoped route configuration. This addendum preserves `candidate-state-review.md` unchanged. No candidate code, evidence, or views were edited.

Ran the state subset once: `uv run --offline --no-sync python -m pytest tests/test_learning_state.py -q -p no:cacheprovider`, with bytecode and plugin auto-loading disabled. **36 tests passed.** The broader 80-pass/5-xfail result was supplied by the parent task; this recheck independently verifies only the 36 state tests.

## Original repair results

- Original-case transfer is now rejected when it matches the current execution or explanation demonstration, and transfer must follow both observations on the same tested tree (`scripts/learning_state.py:211-228`).
- A failure/repair cannot re-credit the old transfer or retention. Transfer must follow the latest selected execution/explanation and all applicable execution/explanation/transfer failures. Retention must follow the selected transfer by the declared interval and use a different demonstration case and the same tree (`:213-239`).
- Contract content and relevant stage facts now enter a stage-specific hash, the session revision includes those hashes, and historical observations count only against their observed contract hash (`:44-73,178-186`). The current route scopes shared roadmap sections and includes the LLM build spec where required. The new contract-edit regression verifies both changed revision and reopened old credit.
- Generated/worked explanation is excluded with generated/worked execution (`:205-208`), and both have targeted regression coverage.
- Boolean schema version and blank stage identifiers are rejected (`:76-94`), with targeted regressions.

These repairs address the reproduced cases in the original report. The exclusive writer, atomic ledger replacement, stale-view checks, and interruption regressions remain intact.

## Remaining material novelty finding

- **Historical supplied-solution cases can still earn fresh transfer or retention credit.** Novelty comparison uses only the latest selected execution/explanation, and for retention the latest selected transfer (`scripts/learning_state.py:209-232`). It does not consider earlier practice observations, including ones explicitly labelled `worked` or `generated`. Validated synthetic sequence: generated execution on case `supplied-complete-answer`; later independent execution and explanation on different cases; transfer on `supplied-complete-answer` with assistance `none`. The result is `ready=True`. A parallel sequence using the earlier generated case for delayed retention yields `retained=True`. Both were reproduced in memory using the current route hash, matching tree, ordered timestamps, and an existing artifact; no event was appended.

This is an enforceable contradiction already present in the ledger, rather than a request for the helper to judge an assertion's truth: the case was explicitly taught with a supplied solution, so later reuse is practice/reassessment, not a fresh independent variation. It matters particularly to the user's gradual-hint policy, which permits supplying the smallest blocker but requires a fresh variation to assess independent understanding later.

Require transfer and retention case IDs to be novel relative to earlier supplied/hinted/practice cases within the relevant stage ownership history, or define an explicit fresh-variation provenance record that cannot reuse that case identity. Preserve earlier observations for history; do not drop assisted practice merely because it cannot qualify as execution credit. Add regressions for a historical generated/worked/hinted case reused after a newer demonstration, and for that same case reused as delayed retention. The current “latest demonstration differs” checks are necessary but insufficient for fresh ownership.

No other material false-credit defect was established in this scoped recheck. The remaining finding should be resolved before calling the novelty/ownership machinery publication-ready; the helper's disclosed inability to verify fabricated assertions remains a human review boundary.

## Final historical-novelty repair verification

The historical-novelty finding above is now **resolved**. Re-inspected only that repair and its regression on 2026-10-12. `scripts/learning_state.py:189-198` builds case exposure from the complete event history, not just the currently credited proof set. The comparison includes all earlier same-stage execution, explanation, transfer, and retention observations regardless of assistance, invalidation, or historical contract version. Both transfer and retention invoke it (`:229-245`). Therefore discarding a generated practice result from qualifying execution does not discard the fact that its case was already seen.

Ran the state subset once after this repair, with the same offline/no-sync/no-cache configuration: **37 tests passed**. The new `test_transfer_cannot_reuse_older_generated_practice_case` regression rejects historical generated-case reuse. Re-ran the two previously reproduced synthetic sequences in memory with current stage hashes and ordered observations: historical supplied case used as transfer now produces `ready=False`; the same historical case used as delayed retention produces `retained=False`. No candidate or evidence files were changed.

There are **no unresolved material false-credit findings from this scoped review**. This statement covers the reviewed relationships and reproduced cases; factual observation, assistance disclosure, and genuinely novel case identity remain human review responsibilities, as the protocol already states.
