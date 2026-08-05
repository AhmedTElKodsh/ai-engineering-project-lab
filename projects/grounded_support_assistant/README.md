# Project 1: Grounded Support Assistant

## Quest briefing

You are the AI engineer joining a support team. Customers ask questions, and the team has an
approved handbook containing the answers it is allowed to give. A confident invented answer
could give wrong account, billing, or single sign-on guidance; drift into unrelated medical or
financial advice; or create avoidable support rework.

An earlier engineer left a small local prototype and a set of checks. Your job is to understand
that inherited system, find where it fails, and improve it step by step until its answers are
supported, traceable, and able to refuse unsupported questions safely. You do not need any
AI-engineering vocabulary before starting; each idea is introduced only when the quest needs it.

The first checkpoint requires no code.

## Problem

Support teams need fast answers from approved documentation, but an assistant must cite its
source and abstain when the documentation does not support an answer.

## Acceptance contract

Given a question and the local handbook, return JSON with:

- the question and answer;
- zero or more source/section citations;
- an explicit `abstained` flag.

The 20-case [evaluation asset](eval/cases.json) contains supported, unsupported, and adversarial
questions. It checks retrieval, abstention, and expected answer facts. One strict expected
failure records a semantic paraphrase that the lexical baseline misses. Changing a model,
prompt, retriever, or database without rerunning this evaluation is not progress.

## Slice 0: inherited transparent baseline

The current implementation ranks handbook sections by exact non-stopword token overlap. It is
intentionally too simple to be the final system; its job is to establish the contract, data,
evaluation, and failure-analysis habit before an LLM hides mistakes behind fluent text.

```powershell
uv run python .\projects\grounded_support_assistant\app.py "Can administrators view my password?"
uv run pytest
```

## Orientation checkpoints

Complete these in separate learner turns before implementation:

1. Explain in ordinary language why the assistant should refuse when the approved handbook does
   not contain an answer.
2. Given a verbatim [handbook excerpt](data/handbook.md) and its heading displayed in the mentor's
   current message, provide only the requested supported fact.
3. Given that verbatim excerpt and heading displayed again, provide only its source section.

Orientation is complete only after the learner independently demonstrates all three. A mentor
explanation, existing code, or passing runtime evidence does not satisfy them.

## Learner-owned implementation slices

1. Inspect one passing question from input to cited answer, introducing only the terms needed to
   explain what the prototype does.
2. Run the 20 cases, trace the expected paraphrase failure, and explain its cause.
3. Add meaning-based retrieval and measure recall before selecting any framework or index.
4. Add provider-backed answer generation while preserving validated output, citations, and
   refusal behavior.
5. Recreate the proven flow with an orchestration framework and record what it adds or obscures.
6. Add persistent vector retrieval, reranking, and a measured storage comparison.
7. Add stronger evaluation and tracing, then compare the evidence each option exposes.
8. Expose the accepted flow through an API, adding gateway behavior only when multiple providers
   or a gateway policy creates the need.
9. Containerize, threat-model prompt injection and data leakage, and publish measured quality,
   latency, and cost.

The learner owns each implementation after Slice 0. The assistant supplies questions, hints,
reviews, and theory at the decision point—not a hidden finished solution.

## Inspiration and originality

This project adapts the document-question-answering pattern from AI Engineering Hub's Simple
RAG Workflow and GitHub RAG projects recorded in [REFERENCES.md](../../REFERENCES.md). Its
implementation, data, evaluation, and learning exercises are original.
