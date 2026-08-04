# AI Engineering Project Lab

Build the recurring systems an AI engineer is hired to deliver, then learn each tool at
the moment the project creates a reason for it.

This is not a collection of framework demos. Each case starts with a small baseline and a
fixed evaluation. A library earns its place only when it improves quality, reliability,
cost, latency, safety, or maintainability.

## Current project

[Grounded Support Assistant](projects/grounded_support_assistant/) is active. Its first
slice is deliberately local and deterministic:

- a bounded Markdown knowledge base;
- Pydantic contracts for the question, answer, citations, and abstention;
- a transparent lexical retrieval baseline;
- 20 supported, unsupported, and adversarial cases with answer-fact assertions, including
  one strict expected failure that exposes the baseline's paraphrase weakness;
- pytest, Ruff, and GitHub Actions checks.

The live learner checkpoint is recorded only in [LEARNING.md](LEARNING.md). When project
orientation is incomplete, the mentor begins with a plain-language quest rather than code or
tool names.

## Continue with the mentor

From this repository, invoke `$project-mentor` with “continue,” “review my attempt,” or a named
project question. The mentor reads [the agent context](project-context.md),
[current learning state](LEARNING.md), and the active project before guiding one checkpoint at
a time. It assumes no AI-engineering vocabulary until the learner demonstrates it, introduces
one necessary term at a time, and resets to a concrete example when the learner is confused.
The learner writes the important implementation; the mentor explains, asks, hints, reviews,
verifies, and records evidence.

## Quick start

```powershell
git clone https://github.com/AhmedTElKodsh/ai-engineering-project-lab.git
Set-Location .\ai-engineering-project-lab
uv sync
uv run python .\projects\grounded_support_assistant\app.py "How long is an export link valid?"
uv run pytest
uv run ruff check .
```

No API key is required for the current slice.

## The learning loop

1. Define the user problem and acceptance cases.
2. Build the cheapest transparent baseline.
3. Measure it and diagnose a concrete gap.
4. Learn only the theory needed to choose the next technique.
5. Add one tool, compare it with the baseline, and keep or remove it on evidence.
6. Harden the boundary, evaluation, observability, security, and deployment.
7. Publish the result, trade-offs, and reproducible commands.

At 5–7 hours per week, the [roadmap](ROADMAP.md) favors durable mastery over artificial
weekly deadlines. [TOOLING.md](TOOLING.md) records which tools deserve deep practice,
one bounded comparison, or deliberate deferral. [REFERENCES.md](REFERENCES.md) records
the external idea sources and license boundary.

## What counts as portfolio proof

A screenshot is not completion. A finished case has runnable tests, a versioned evaluation
set, measured before/after results, failure analysis, architecture and tool decisions,
security and cost notes, and a reproducible deployment or local run.
