# Tool adoption

Library placement and bounded comparison acceptance live in the single
[Problem-first RAG plan](docs/learning-path/02-PROJECT-ROADMAP.md), inside each stage.
Use the direct official library before an orchestration adapter. Keep one pipeline.
A comparison needs a question, fixed inputs, metrics, a two-session cap and a
keep/defer/drop decision. Optional references do not mandate installs.

Add dependencies in the stage's group only when it starts; check installed/locked
versions and current official docs then. S0 needs no new library, model, provider or
tracing credentials. Default tests use deterministic fakes; live calls require an
explicit target and budget. Keep secrets out of logs and records.

Python 3.12 is the canonical CI/runtime target. Run the maintenance commands in
[project-context.md](project-context.md). Preserve incomplete learner acceptance tests;
expected baseline failures are not successful behavior. Handwritten framework/model
internals belong to the dormant optional shelf unless explicitly requested.
