# Adoption runbook: from the M1 lesson route to S0 task 1

> **Historical.** This runbook was executed on 14 October 2026 in the curriculum clone
> (commit `fca7de30`). Paths below are as they were there; in this repository the route
> lives at `from-scratch/route.json` and the resolver at `from-scratch/scripts/`.

Proposal drafted 14 October 2026 for audit finding B-01. Nothing here has been run
or applied. Every step marked **ASK FIRST** changes learner state and needs the
learner's explicit yes in chat before anyone executes it.

Goal: after step 8, the resolver returns `project_stage_id: S0` at 10 hours/week with
a learner workspace outside this checkout, and the tutor can say why.

Interpreter: use the one that exists on the machine. On this Windows machine
`py` and `python3` are absent; `python -X utf8` works. Check first:

```powershell
python -X utf8 --version
```

Placeholders: `$CURR` is this checkout; `$WS` is the learner workspace
(proposed `D:\AI Projects\Learning\python-to-llm-workspace`, any path outside `$CURR`).

## Current state (verify before starting)

| Fact | Check | Expected today |
|---|---|---|
| Active route is M1 at 5-7 h/week | `python -X utf8 scripts/next_learning_route.py --project-root .` | `lesson_id` `11.01`, `milestone` `M1` |
| Candidate resolves S0 | same command with `--route docs/learning-path/route.project-candidate.json` | `project_stage_id` `S0` |
| No learner workspace | `Test-Path $WS` | `False` |

## Steps

### 1. Baseline the resolver and tests

```powershell
python -X utf8 scripts/next_learning_route.py --project-root .
python -X utf8 -m unittest discover scripts/tests
```

Expected: `"lesson_id": "11.01"`; all tests pass. Read-only.

### 2. ASK FIRST: create the learner workspace outside this checkout

The workspace holds the learner's code, tests, notes, and evidence artifacts. It
must not be inside `$CURR`, so reference solutions under `phases/*/code` are not
beside the learner's files and evidence cannot cite curriculum files (H-01, H-05).

```powershell
New-Item -ItemType Directory -Path $WS
git -C $WS init
```

Verify: `Test-Path $WS` is `True`; `git -C $WS rev-parse --is-inside-work-tree` prints
`true`; `$WS` does not start with the `$CURR` path. If git reports "dubious
ownership", the user decides whether to run the `safe.directory` command it prints;
do not change git config unasked.

### 3. ASK FIRST: copy the empty evidence file into the workspace

```powershell
Copy-Item docs/learning-path/project-evidence.template.json "$WS\evidence.json"
git -C $WS add evidence.json
git -C $WS commit -m "chore: empty evidence ledger"
```

Verify: `"records": []` in `$WS\evidence.json`.

### 4. ASK FIRST: record the pace and mode in `LEARNING.md`

Edit only these lines of `LEARNING.md`, as the user confirms each:

1. `Pace: ~5–7 hours/week` becomes `Pace: ~10 hours/week`.
2. Under "Study directions for AI tutor", replace the M1 route bullets with:

```text
- Mode: project (adopted YYYY-MM-DD)
- Route: docs/learning-path/route.project-candidate.json
- Learner workspace: <absolute path of $WS>
- Evidence ledger: <$WS>\evidence.json
- Superseded: docs/learning-path/route.json (M1) is retained for reference
```

Keep the Placement and Progress log rows; they are historical context.
Verify: `Select-String -Path LEARNING.md -Pattern "Pace|Mode: project"` shows 10 hours
and the project mode. Check against the user's real weekly availability first; 10
hours is the plan's figure, not a measurement (audit H-02).

### 5. ASK FIRST: make the candidate route carry the workspace and ledger

In `docs/learning-path/route.project-candidate.json`, set
`"evidence_file"` to the absolute ledger path from step 4 and add
`"learner_workspace"` with the absolute workspace path. Nothing else changes.
Alternative with no route edit: pass `--workspace` and `--evidence` on every call.

Verify:

```powershell
python -X utf8 scripts/next_learning_route.py --project-root . --route docs/learning-path/route.project-candidate.json --validate
```

Expected: `"status": "valid"`, `"evidence_records": 0`, nine project stages, 13 required gates.

### 6. ASK FIRST: route activation, the tutor entry point

Activation means the tutor and `AGENTS.md` "Learner-mode routing" select the
candidate. Two changes, each confirmed separately:

1. Tutor commands use `--route docs/learning-path/route.project-candidate.json`
   (and `--workspace "$WS"` unless step 5 stored it). Edit the resolver command in
   `.agents/skills/learn/SKILL.md` (and the same text in `AGENTS.md` step 2) to read
   the route named by the `Route:` line of `LEARNING.md`, falling back to `route.json`.
2. Set `"candidate": true` in the candidate route to `false`, and mark M1 as
   superseded in `docs/learning-path/MILESTONES.md`, so the docs no longer say "inactive".

The tutor skills currently do not load in this checkout (audit H-06: broken
junctions to a path that does not exist); repair them or the `learn` edit has no effect.

Verify: step 7.

### 7. Verify the resolver result

```powershell
python -X utf8 scripts/next_learning_route.py --project-root . --route docs/learning-path/route.project-candidate.json
```

Expected JSON fields: `"status": "next"`, `"project_stage_id": "S0"`, `"stage": "S0"`,
`"gate_ids": ["G0"]`, `"overdue_retention": []`, `"pending_obligations": []`.
Then confirm the guard that stops forgery:

```powershell
python -X utf8 -m unittest discover scripts/tests
```

All tests pass, including `test_forged_readme_in_curriculum_root_rejected`.

### 8. Record the adoption

Add one dated line to the `LEARNING.md` progress log, for example
`| YYYY-MM-DD | adoption | n/a | project route adopted; workspace <path>; S0 next |`,
and commit the workspace baseline. This is the only place adoption is recorded; it
awards no completion, quiz credit, or mastery.

Verify: the step 7 command still returns S0. Next action: S0 task 1 in
`_bmad-output/planning-artifacts/python-to-llm-2026-10-11/04-FIRST-FOUR-WEEKS.md`
(predict the counts for `Python helps. Python teaches!`, then write `count_words`).
The learner writes it in `$WS`; the tutor follows the learner-owns-the-solution rule.

## Rollback

Undo in reverse: restore the `Pace:` and "Study directions" lines in `LEARNING.md`,
drop `learner_workspace` and the absolute `evidence_file` from the candidate route,
and run step 1 again. Expected: `11.01` and M1. The workspace is left in place.

## What needs the user's explicit approval

| Step | Action |
|---|---|
| 2 | Create a directory and git repository outside the checkout |
| 3 | Write the evidence ledger in it |
| 4 | Edit `LEARNING.md` (pace, mode, route, workspace) |
| 5 | Edit the candidate route (`learner_workspace`, `evidence_file`) |
| 6 | Change tutor commands, `AGENTS.md`, the route's `candidate` flag, and `MILESTONES.md` |
| 8 | Add the adoption line to `LEARNING.md` |
