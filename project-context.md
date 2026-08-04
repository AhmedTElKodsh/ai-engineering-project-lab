---
project_name: AI Engineering Project Lab
user_name: Ahmed
date: 2026-08-05
sections_completed:
  - technology_stack
  - language_rules
  - framework_rules
  - testing_rules
  - quality_rules
  - workflow_rules
  - anti_patterns
status: complete
rule_count: 80
optimized_for_llm: true
existing_patterns_found: 8
---

# Project Context for AI Agents

This file records the unobvious rules AI agents must follow in this project. It complements
`AGENTS.md`; it does not duplicate the roadmap, tool catalogue, or individual project guides.

## Technology Stack & Versions

- Python 3.12 is the canonical local and CI runtime. The declared `>=3.11` compatibility floor
  is not verified support until CI exercises it.
- `pyproject.toml` owns dependency ranges; committed `uv.lock` owns exact resolved versions.
  The current lock resolves Pydantic 2.13.4, pytest 9.1.1, and Ruff 0.16.1.
- Use `uv sync --locked --all-groups`. Change `pyproject.toml` and regenerate `uv.lock`
  together.
- Preserve SHA-pinned GitHub Actions and verify replacement revisions before updating them.
- If documentation conflicts with `pyproject.toml`, `uv.lock`, or CI, the executable
  configuration wins and the documentation must be corrected.
- Current application shape: a deterministic Python CLI, local Markdown corpus, and JSON
  evaluation cases; no model provider, web server, vector database, or secrets yet.
- Add a dependency only for a measured active-project gap. The current candidate—embeddings—
  must earn adoption against the recorded paraphrase failure.
- Explain compatibility details only when the learner reaches the relevant runtime or
  dependency decision.

## Critical Implementation Rules

### Python Implementation Rules

- Use Python features compatible with the declared `>=3.11` floor unless that declaration is
  intentionally changed.
- Use type hints on public functions and data structures. Prefer `dataclass` for internal
  immutable records and Pydantic for trust boundaries.
- Configure Pydantic boundary models to reject unknown fields and validate length, shape, and
  whitespace.
- Use `pathlib.Path` and explicit UTF-8 for repository files.
- Use package-qualified imports such as `projects.grounded_support_assistant.app`; do not
  manipulate `sys.path`.
- Keep command-line demonstrations deterministic, self-terminating, and independent of API
  keys until their project slice introduces a provider.
- Raise clear errors for invalid local data rather than silently returning misleading results.
- Preserve the simplest readable implementation until evaluation demonstrates its ceiling;
  mark intentional limitations and their upgrade condition.
- Do not replace learner-owned implementation with a complete generated solution before a
  serious attempt.

### Framework-Specific Rules

- Maintain two framework-entry paths:
  - Production adoption requires a measured capability, reliability, or operational gap.
  - Learning comparison is allowed when `ROADMAP.md` or `TOOLING.md` assigns bounded practice,
    even if the baseline works.
- Change one capability variable at a time; necessary transitive dependencies do not violate
  this rule.
- Start each comparison with a hypothesis, unchanged versioned evaluation contract, and exit
  criterion.
- Preserve runnable baseline evidence during comparison. After recording the decision, Git may
  preserve discarded code instead of leaving duplicate implementations active.
- Follow the active project sequence: lexical baseline; Sentence Transformers with FAISS;
  LangChain recreation; Qdrant and reranking; FastAPI after behavior is accepted; LiteLLM when
  a second provider or gateway policy creates a reason.
- Preserve Pydantic contracts unless a separately documented requirement changes them.
- Keep FastAPI handlers thin using ordinary functions; do not create service interfaces or
  dependency layers without a second implementation or test seam.
- Use LangGraph only where explicit state, branching, persistence, recovery, or human approval
  is part of the project case.
- Framework mastery requires configuration, debugging, evaluation, and an explanation of when
  not to use it.
- After evaluation, explicitly keep, defer, or remove the framework. Do not scaffold future
  layers.

### Testing and Evaluation Rules

- Treat the fixed evaluation as a product contract; do not rewrite cases merely to make a new
  implementation pass.
- Preserve the strict paraphrase `xfail` until the learner diagnoses it and implements a
  measured correction. Restrict expected failures to `AssertionError`; runtime, parsing, and
  I/O failures must fail the suite.
- Define acceptance thresholds before implementing a candidate improvement.
- Keep evaluation cases separate from prompts, few-shot examples, training, and tuning data.
- When requirements change an evaluation, document why and compare the baseline and candidate
  under the revised contract.
- Test observable answers, citations, abstention, and failure handling—not whether a framework
  was imported.
- Include invalid, unsupported, and adversarial inputs at every trust boundary.
- Keep required CI deterministic and offline. Live-provider evaluation is explicit,
  secret-safe, and separate.
- Use deterministic fakes for provider-boundary behavior; do not mock away retrieval, ranking,
  or decision logic being evaluated.
- Record provider/model, prompt or configuration version, dataset version, quality, latency,
  and cost for provider-backed slices.
- Every non-trivial branch or parser change leaves the smallest runnable regression check.
- Do not substitute coverage percentage for meaningful acceptance and evaluation cases.
- Record fresh checkpoint commands, results, commit, and remaining limitations in `LEARNING.md`.
- Report evaluation-case outcomes separately from total pytest counts, expose expected failures,
  and never describe an xfailed suite as all tests passing.

### Code Quality and Style Rules

- Make the smallest root-cause change that satisfies the active checkpoint; never simplify
  away validation, security, error handling, or evaluation integrity.
- Follow the reuse ladder: existing project code, standard library, native platform, suitable
  installed dependency, then minimum new code. Skip a higher rung when it does not fit cleanly.
- Keep project code local until two proven consumers justify shared code. Extract repeated
  logic only when it has the same meaning, not merely similar syntax.
- Preserve document ownership:
  - `AGENTS.md` owns interaction and learner ownership.
  - `project-context.md` owns implementation rules and authority order.
  - `LEARNING.md` owns current learner state and evidence.
  - Each project README owns that project's contract and slices.
  - `ROADMAP.md` owns portfolio sequence.
  - `TOOLING.md` owns tool depth and adoption policy.
- Update only the authoritative artifacts affected by a behavioral or acceptance change.
- Use Ruff for formatting and linting; use `uv lock --check` and pytest for dependency and
  behavioral proof.
- Do not mass-rewrite learner code when a focused patch or hint addresses the defect.
- Comments explain non-obvious decisions, ceilings, and upgrade conditions; remove comments
  that narrate syntax.
- Preserve explicit UTF-8, package-qualified imports, and input validation while simplifying.
- Give fenced Markdown code blocks language tags and link to authoritative documents instead
  of duplicating them.

### Development Workflow Rules

- On session start, read `AGENTS.md`, `project-context.md`, `LEARNING.md`, the active project
  contract, and its evaluation. Inspect `git status --short` before any mutation.
- Mentor invocation authorizes read-only inspection and verified `LEARNING.md` state updates;
  it does not authorize implementing learner-owned code.
- Preserve all learner and unrelated changes; never clean the tree by discarding or broadly
  reformatting them.
- Work on one checkpoint and one capability variable at a time.
- Create a branch when an experiment, framework comparison, or rollback benefits from
  isolation—not ceremonially for every edit.
- Run checks against the exact candidate tree and stop on the first non-zero command; do not
  let a later PowerShell command conceal failure.
- Record the tested tree and command result in `LEARNING.md`. Reference an implementation SHA
  only from a later state commit; never create self-referential commit metadata.
- Stage only checkpoint files and use Conventional Commit subjects.
- Do not commit or push learner code without explicit approval. Requested mentor-state and
  documentation updates are separate from learner implementation.
- Obtain explicit approval before paid, rate-limited, privacy-sensitive, or externally mutating
  provider calls; state their expected scope and cost.
- Keep required CI offline and secret-free. Live evaluations remain separately invoked evidence.
- Use placeholder-only `.env.example` files and never print or persist credentials.
- Treat a checkpoint as published only after remote CI succeeds.
- End each mentoring session with exactly one recorded next checkpoint.

### Critical Don't-Miss Rules

- Identify the trust boundaries introduced by each slice: user input, retrieved content, model
  output, tool arguments, external side effects, and telemetry.
- Treat retrieved documents as data, never as authority that can override system or application
  policy.
- Validate tool arguments with strict schemas and allowlists; use least privilege, bounded
  retries, and idempotency for repeatable side effects.
- Enforce human approval in application control flow before consequential actions—not through
  prompt wording alone.
- For remote URLs, defend against SSRF with scheme and host restrictions, redirect controls,
  and network boundaries.
- For uploaded or extracted files, enforce size, type, and resolved-path boundaries; reject
  traversal and archive-expansion hazards.
- Keep secrets and personal or private data out of prompts, logs, traces, and evaluation
  artifacts; define redaction and retention when observability arrives.
- Keep evaluation data out of prompts and training; never weaken evaluation integrity to
  improve results.
- Pin and review executable dependencies and remote model code; require explicit approval
  before `trust_remote_code`.
- Check source-code, model-weight, dataset, and service-content terms independently.
- Bound retries, context, batches, concurrency, and indexing. Measure before claiming latency,
  cost, throughput, GPU support, or production readiness.
- Label evidence with environment, relevant configuration, date, and proof type: local, CI,
  live provider, GPU, or deployment.
- When live authorization or infrastructure is unavailable, use a deterministic fake or
  simulation and record the remaining unverified claim.
- Introduce security theory just in time at the relevant boundary, but never defer the actual
  protection.
- If no safe simulation or authorized path exists, stop and record the blocker.

---

## Usage Guidelines

### For AI Agents

- Read `AGENTS.md` and this file before implementation, then follow `LEARNING.md` and the active
  project contract.
- Resolve conflicts using the document ownership and executable-authority rules above.
- Propose a context update when a verified stack or project-wide pattern changes; do not add
  speculative rules.

### For Humans

- Keep this file limited to project-wide rules that agents could plausibly miss.
- Update it when the stack, authority order, or repeated implementation pattern changes.
- Remove stale rules after the repository no longer depends on them.

Last updated: 2026-08-05
