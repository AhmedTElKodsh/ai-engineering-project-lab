# From-scratch curriculum route

This directory holds the learner's work from a clone of
[rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch),
moved here on 15 October 2026 so that the clone could be reset to upstream.

| Path | What it is |
|---|---|
| `route.json` | S0–S8 project route, adopted 14 October 2026 at 10 hours/week |
| `route.m1-superseded.json` | Earlier M1 lesson route, kept for reference |
| `LEARNING.md` | Placement, study directions and tutoring rules for this route |
| `scripts/next_learning_route.py` | Read-only resolver that picks the next stage from reviewed evidence |
| `project-evidence.template.json` | Empty evidence ledger shape |
| `lessons/` | The learner's edited lesson files, new tests and notebooks (see below) |
| `skills/` | Curriculum learning skills, stored inactive (see below) |
| `pyproject.toml`, `uv.lock` | Environment used to run the curriculum lessons |

The plan behind the route is in [docs/learning-path](../docs/learning-path/00-START-HERE.md).
The audits that shaped it are in [docs/review/from-scratch-audits](../docs/review/from-scratch-audits/).

## Run the resolver

Lesson stages resolve against a checkout of the upstream curriculum, so pass its path:

```powershell
python -X utf8 from-scratch/scripts/next_learning_route.py --project-root from-scratch --curriculum-root ../ai-engineering-from-scratch-1
```

Project-only routes (like the adopted S0–S8 route) do not need the curriculum checkout,
but lesson references in the superseded M1 route do. Tests:

```powershell
python -m unittest discover from-scratch/scripts/tests
```

Set `FROM_SCRATCH_CURRICULUM` to a curriculum checkout to also run the M1 route check.

## Lessons

`lessons/<phase>/<lesson>/` mirrors the upstream `phases/` layout. It contains full copies of
the files the learner changed, plus new tests and notebooks. `lessons/upstream-edits.patch`
is the same change set against upstream commit `7157ca74`; apply it inside a curriculum
checkout with `git apply from-scratch/lessons/upstream-edits.patch` (paths start at `phases/`).
It applies cleanly at `7157ca74`. Upstream has since changed lesson 10/10 (evaluation), so on a
newer checkout use `git apply -3` and resolve that lesson by hand.

The IMDB parquet download used in lesson 00/09 is not stored here; re-download it when needed.

## Skills

`skills/` holds the curriculum's `learn`, `start-learning`, `course-guide`,
`find-your-level` and `check-understanding` skills as modified in the clone. They expect to
run from a curriculum checkout (a `phases/` directory and `LEARNING.md` in the working
directory), so they are stored here rather than in `.agents/skills`, which keeps this
repository's single active mentor. To use them, copy them into a curriculum checkout's
`.agents/skills/`.

## License

Files under `lessons/` and `skills/` derive from the upstream curriculum and remain under
its MIT license; see [NOTICE](NOTICE).
