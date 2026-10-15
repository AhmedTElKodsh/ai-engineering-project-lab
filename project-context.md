# Implementation and document authority

The current product is the AI Engineering Workbench. The active assistant directory is projects/grounded_support_assistant; the existing lexical app is inherited reference implementation. Future learner modules remain unimplemented until authored during tutoring. The route's depth is RAG and agents with existing frameworks; its model/ directory is reserved for the optional from-scratch track. Mushir, the private client project, is where each stage is applied; its code and corpus stay in its own repository.

Python 3.12 is the canonical locked/CI runtime. pyproject.toml declares a broader interpreter floor; untested versions are not verified. Use `uv sync --locked --all-groups`; retain pinned GitHub Actions. Pydantic is inherited at the trust boundary; pytest and Ruff are development tools. No provider/network call occurs during default imports or checks. Stage libraries join as named dependency groups when their stage starts (see TOOLING.md); the default environment stays small.

## Owners

- README.md: entry/index and narrow current claims.
- AGENTS.md and the single mentor skill: contributor and interaction responsibilities.
- learning/route.json: IDs, prerequisites, confirmed pace, compute policy and effort ranges.
- Detailed planning documents: acceptance, skill depth, session method and model contracts.
- Project README: current quest, baseline behavior, data and known limitations.
- learning/evidence.jsonl: append-only factual history. Derived state and LEARNING.md: resumable view.
- TOOLING.md: dependency/adoption boundaries. Review report: source selection and verification evidence.
- resources: the HR practice corpus, fixtures and optional from-scratch material, not another active course.
- explorations: side quests with no route, state or credit.
- archive: historical state, never current instruction.

## Check a maintenance candidate

```powershell
uv sync --locked --all-groups
uv run python scripts/check_mentor_contract.py
uv run ruff check .
uv run ruff format --check .
uv run pytest -rxX -q
```

The package check validates paths, state, declared document structure and exercise collection. It is structural proof, not an evaluation of real tutoring or learner retention. Test counts are separate from fixed evaluation case counts. Strict xfails are labelled measured baseline defects, never silently called successful behavior. One lab at a time is collected because inherited exercises use the same module name; incomplete behavior tests stay outside normal CI.

## Engineering rules

Validate inputs and outputs at boundaries; keep deterministic authorization outside model output. Retrieval is data. Filter access, version and eligibility before ranking/top-k. Source offsets are Python Unicode code-point indices when slicing str; byte spans must be declared and converted explicitly. Verify bounds and nonempty evidence, while remembering that an exact quote does not prove entailment.

Use fake providers/tools first. Timeouts, retries, token/tool limits and cancellation must actually terminate; include negative controls showing a meaningful wrong implementation fails. File persistence serializes before atomic replacement. Repeated writes are idempotent; ambiguous external writes require reconciliation, not blind retry. No external financial, clinical or communication actions are part of the baseline.

Never collect or print API keys. Secrets stay outside Git and progress artifacts. Preserve the original dirty local learner checkout and its environment. Current provider model IDs and APIs must be checked against official sources when a real provider stage begins; older source examples are not currency evidence.
