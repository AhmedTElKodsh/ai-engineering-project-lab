# Learning evidence and route state

Revised 12 October 2026. This protocol records evidence, not invented learner results.
The [project route](../../from-scratch/route.json) (S0–S8, 10 hours/week) was adopted on
14 October 2026. The [M1 lesson route](../../from-scratch/route.m1-superseded.json) is
superseded and kept for reference. Probing a route with a command never modifies
`from-scratch/LEARNING.md`.

## Advancement, retention, and closure

| State | Required evidence | Next action |
|---|---|---|
| Not ready | One or more readiness checks missing/failed/assisted | Teach or repair the smallest gap; preserve prior evidence. |
| Ready to advance | Learner execution, explanation, and a fresh independent implementation or unfamiliar bug repair pass | Continue reachable work; retain outstanding obligations. |
| Retention pending | Readiness established; delayed check not yet passed | Keep a dated fresh task in the review queue. |
| Retention failed | Readiness previously established; delayed check fails | Targeted repair and another delayed task; do not restart a whole phase automatically. |
| Retained | Readiness plus a successful independent delayed check after the original construction date | M4 may be recorded for this capability. |
| Closed | Every required stage gate ready and retained, with required live/quality evidence satisfied | Review remaining milestone exit criteria before changing its status. |

Readiness permits advancement; it does not close a stage or establish retained mastery.
A failed delayed check remains visible even when a new stage is schedulable. If its gap
blocks that new task, teach the gap first. Missing provider access permits local work;
required live generation, semantic retrieval, live tool selection, and model-quality
gates stay pending. Offline fixtures never satisfy those gates.

## Evidence categories

| Category | Meaning | Scheduling effect |
|---|---|---|
| `attempt` | Incomplete/failed/assisted practice or a diagnostic observation | Never satisfies a requirement. |
| `focused_bridge` | Scoped study with deferred depth, tied to exact lesson and focused stage | Eligible independent readiness satisfies that scope, never a later full requirement. |
| `full_completion` | Whole lesson material, staged quiz, and artifact reviewed for eligibility | Only `completion_eligible: true` plus readiness satisfies a full requirement. |
| `project_gate` | Evidence for one named project gate | Readiness derives independently for each gate. |

`LEARNING.md` is the human study record. Existing rows are historical context, not
machine-certified completion. Migrate a row only after reviewing its actual evidence;
record the reviewed category, checks, assistance, and eligibility explicitly. A quiz
score or prose marker alone is insufficient. Do not erase legacy rows.

The active route optionally reads `docs/learning-path/evidence.json`. A missing default
file means no eligible evidence. The candidate explicitly reads the empty
[evidence template](../../from-scratch/project-evidence.template.json); it contains no earned records.
Copy that structure to the actual governed workspace only upon adoption. Off-route
diagnostic detours remain in human evidence notes until represented in a validated
route; unknown evidence subjects are rejected, including attempts.

## JSON contract

The root object has integer `schema_version: 1` and an ordered `records` list.
Each record has a unique non-empty `id`, `category`, and `subject`. Lesson subjects use
`phase/lesson-directory`; project subjects use `S0`–`S8`. A focused bridge also names
`stage`; a project record names `gate_id`; a full record requires boolean
`completion_eligible`. New records for the same eligible scope supersede older checks;
preserve original artifacts and notes. Attempts do not erase an earlier passed check.

Except for attempts, records have `observed_at` (ISO date) and four check objects:
`execution`, `explanation`, `transfer`, `retention`. Their `status` is `not_observed`,
`pending`, `failed`, or `passed`. Passed/failed checks require `evidence`, an object
that binds the check to an artifact in the learner workspace:

```json
{"path": "src/search.py", "sha256": "<64 lowercase hex>", "commit": "<7-40 hex>"}
```

- `path` is relative to the learner workspace (or absolute inside it) and must resolve
  to an existing non-empty file inside that workspace after symlinks and `..` are resolved.
- `sha256` is the digest of the file bytes and is recomputed on every run, so editing
  the artifact after review invalidates the record.
- `commit` is the learner-workspace commit that contains the reviewed artifact. The
  resolver checks its format only; the tutor verifies it with `git cat-file -e <commit>`
  and `git show <commit>:<path>` inside the workspace.

The learner workspace is a directory outside the curriculum checkout, named by the
route's optional `learner_workspace` field or by `--workspace`. It must exist, must not
be the curriculum root, and must not contain or sit inside it. Any passed/failed check
without a workspace is an error, so a file such as `README.md` in the curriculum root
can never certify a gate. One artifact (same path and hash) cannot be cited for two
different subjects, gates, or focused stages. Dates must not be in the future. The tutor
must still inspect the artifacts, execution mode, authorship, and support; a matching
hash proves the file is unchanged, not that it is true. Evidence is a trusted mentoring
record, not a tamper-proof credential or automated grading system, and the resolver
cannot tell the learner from the tutor: assessor separation remains a human practice.

A passed transfer requires boolean `independent` and `kind`: `implementation`,
`debug`, `trace`, or `changed_input`. Only an independent implementation/debug pass
establishes construction readiness. Tracing and new-input runs remain useful evidence.
A pending/failed retention check names ISO `due` and fresh `task`; `due` is at least
7 days after `observed_at`. A passed delayed check names `checked_at`, at least 7 days
after `observed_at` and not after today, boolean `independent`,
`kind`, and a reviewed delayed-task artifact. Retained construction requires
`independent: true` and `kind: implementation` or `debug`; assisted, trace, and
changed-input delayed passes keep readiness but do not establish retained status.
Optional `support` and `deferred_depth` retain assistance/debt. Check fields are
`status`/`evidence`, plus `independent`/`kind` for transfer, and
`due`/`task`/`checked_at`/`independent`/`kind` for retention; unknown fields fail.
Derived readiness/mastery flags and unsupported fields are rejected. No example below
awards a pass:

```json
{
  "schema_version": 1,
  "records": [
    {
      "id": "example-attempt-only",
      "category": "attempt",
      "subject": "S0",
      "support": "Example format; replace with actual learner evidence upon adoption."
    }
  ]
}
```

## Route and output contract

Schema 1 supports existing `lesson_ids` stages with `full`, `focused`, `paired`,
or `repair` modes. Schema 2 also supports `kind: project`, `project_stage_id`,
`mode: project`, `evidence_category: project_gate`, non-empty `gate_ids`, and a non-empty
`advancement_gate_ids` subset. Both schemas require real booleans, unique IDs, valid
references, and non-empty required stages. Conditional stages are never auto-scheduled.

The candidate has nine required core gates G0–G8. Its additional required gates are
S2-live-generation, S2-semantic-retrieval, S3-live-tool-selection, and S7-held-out-quality.
Core readiness schedules the next local stage while those obligations remain visible.
`status: next` identifies the next requirement and `evidence_state` explains it.
`pending_obligations` carries prior retention/live/quality debt. When core readiness
is exhausted, `milestone_ready_retention_or_gates_pending` keeps missing evidence
visible; `milestone_requirements_closed` still requires human exit-criteria review.

Every result also carries `overdue_retention`: delayed checks that are ready but not
retained and whose `due` date is before today, each with `stage`, `subject`, `gate`,
`task`, `due`, and `days_overdue`. Overdue items never block scheduling; the tutor
offers them at the start of the next session. `--today YYYY-MM-DD` overrides the date
for testing only.

```powershell
# Run from the repository root. --curriculum-root is a checkout of
# rohitg00/ai-engineering-from-scratch whose phases/ the lesson stages resolve against.
python -X utf8 from-scratch/scripts/next_learning_route.py --project-root from-scratch --curriculum-root ../ai-engineering-from-scratch-1
python -X utf8 from-scratch/scripts/next_learning_route.py --project-root from-scratch --curriculum-root ../ai-engineering-from-scratch-1 --validate
python -X utf8 from-scratch/scripts/next_learning_route.py --project-root from-scratch --curriculum-root ../ai-engineering-from-scratch-1 --route route.m1-superseded.json --validate
python -X utf8 from-scratch/scripts/next_learning_route.py --project-root from-scratch --curriculum-root ../ai-engineering-from-scratch-1 --evidence path/to/reviewed-evidence.json --workspace path/to/learner-workspace
```

Verify the actual learner interpreter first. If `py` exists, `py -X utf8` is another
valid launcher; use the selected interpreter directly when it does not. Commands
read state only. Malformed/unsupported routes or evidence return JSON `status: error`
and exit 1. Stop and repair that error; do not select a different lesson silently.
