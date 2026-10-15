# Factual evidence and safe resumption

The route owns requirements; the append-only JSONL log records observations. state.json and root LEARNING.md are derived views. The helper validates relationships and file existence, not the truth of a tutor or learner assertion. It never executes learner code or contacts a provider.

## Evidence and claims

Each event has id, timezone-aware at, actor, kind, stage, result, assistance, case, artifact and note. Learning proof also has a tested tree/config identifier, artifact_sha256 and contract_sha256. Obtain the current stage contract hash from status; hash the immutable observation artifact before appending. Changed stage requirements conservatively reopen its credit while preserving historical observations. Store an actual durable repository-relative artifact containing the learner attempt/output, source, environment/date and narrow claim. Do not put credentials, private records or fabricated output in evidence. A bare path is not a verified observation.

Kinds are context, focus, execution, explanation, transfer, retention and correction. Context preserves support needs without awarding a gate. Focus records a temporary eligible stage, such as S5 agent work while S4 evaluation is pending. Actor is learner or maintainer. Runtime/explanation/transfer/retention proof requires actor learner and pass/fail; maintainer validation does not count.

Assistance is none, docs, hints, worked, generated or not_applicable. Docs permits syntax/official reference while excluding AI completion and worked answers for independent claims. Supplied partial/full code is worked/generated; it is useful practice, not ownership. Readiness needs execution, explanation and fresh independent transfer after both, on a different case and the same tested tree/config; generated/worked execution or explanation does not qualify. A failure and repaired execution cannot reuse transfer/retention from before the failure. Retained completion also needs a different fresh case at least 24 elapsed hours after transfer, with no AI solution/hints. Usually revisit after 2–7 days. This interval is a scheduling guard, not scientific proof of long-term mastery.

Record software evidence class inside the artifact: static, supplied_replay, local_deterministic, mock_contract, live_provider, deployed_black_box or learner_owned, and completed/access_blocked/incomplete/invalid separately. A mocked provider result is never live quality proof. A stage pass means the complete declared stage contract was reviewed; the helper cannot inspect all its behaviors. Partial results stay practice/context, not an entire-stage pass.

Latest applicable failures reopen only the affected stage/kind. A correction targets one earlier event and preserves the original record; it cannot silently erase history. Dependent readiness/retention recomputes while unrelated stage proof survives. Current state has only a maintainer migration event; all learner gates remain unresolved.

Fresh assessment case IDs must differ from all earlier same-stage practice/assessment cases, including worked/generated help and invalidated or older-contract records. A renamed copy of the same supplied task is not genuinely fresh; the tutor must inspect provenance as well as the helper's identity check.

## Commands

```powershell
uv run python scripts/learning_state.py status
uv run python scripts/learning_state.py validate
uv run python scripts/learning_state.py append --event learning/records/new-event.json --expected-revision REVISION_FROM_STATUS
uv run python scripts/learning_state.py refresh
```

The event file is a prepared observation record, not generated competence. Before append, run/check the appropriate code or read the actual learner response, record assistance and the candidate tree, and compare the reported output. The exclusive writer lock prevents concurrent checkpoint writers; revision comparison includes route, log and stage contracts and rejects stale sessions. Stage-scoped contract hashes prevent earlier claims satisfying changed requirements. Ledger replacement preserves its previous byte prefix and atomically adds the new line. Derived files are individually atomic, not one filesystem transaction: if interrupted between writes, validation fails closed. Refresh rebuilds views from the unchanged valid log. A malformed log must be inspected/recovered from backup; refresh must not invent a replacement event. Inspect any abandoned writer lock before removing it.

Keep exactly one next checkpoint. Incomplete live access permits local work on eligible stages, without completing the missing live gate or final route. Final completion requires all declared stage contracts and retained ownership, not the repository's maintenance test count.
