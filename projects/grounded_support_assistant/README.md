# Project 1: Grounded Support Assistant

## Quest briefing

You are the AI engineer joining a support team. Customers ask questions, and the team has an
approved handbook containing the answers it is allowed to give. A confident invented answer
could mislead a customer, expose private information, or create work for the support team.

An earlier engineer left a small local prototype and a set of checks. Your job is to understand
that inherited system, find where it fails, and improve it step by step until its answers are
supported, traceable, and able to refuse unsupported questions safely. You do not need any
AI-engineering vocabulary before starting; each idea is introduced only when the quest needs it.

The first checkpoint requires no code: explain in ordinary language why the assistant should
refuse to answer when the approved handbook does not contain the answer.

## Problem

Support teams need fast answers from approved documentation, but an assistant must cite its
source and abstain when the documentation does not support an answer.

## Acceptance contract

Given a question and the local handbook, return JSON with:

- the question and answer;
- zero or more source/section citations;
- an explicit `abstained` flag.

The 20-case evaluation contains supported, unsupported, and adversarial questions. It checks
retrieval, abstention, and expected answer facts. One strict expected failure records a semantic
paraphrase that the lexical baseline misses. Changing a model, prompt, retriever, or database
without rerunning this evaluation is not progress.

## Slice 0: inherited transparent baseline

The current implementation ranks handbook sections by exact non-stopword token overlap. It is
intentionally too simple to be the final system; its job is to establish the contract, data,
evaluation, and failure-analysis habit before an LLM hides mistakes behind fluent text.

```powershell
uv run python .\projects\grounded_support_assistant\app.py "Can administrators view my password?"
uv run pytest
```

## Guided build slices

1. Understand the quest, its user-visible success conditions, and why guessing is unsafe.
2. Inspect one passing question from input to cited answer, introducing only the terms needed to
   explain what the prototype does.
3. Run the 20 cases, trace the expected paraphrase failure, and explain its cause.
4. Build embedding retrieval with Sentence Transformers and FAISS; measure recall before adding
   a framework.
5. Add one direct provider SDK for answer generation while preserving Pydantic validation,
   citations, and refusal behavior.
6. Recreate the proven flow with LangChain and record what it adds or obscures.
7. Move retrieval to Qdrant, add a cross-encoder reranker, and compare with pgvector.
8. Add Ragas/promptfoo evaluation and compare LangSmith traces with Langfuse.
9. Expose the accepted flow through FastAPI, then add LiteLLM only when a second provider or
   gateway policy is required.
10. Containerize, threat-model prompt injection and data leakage, and publish measured quality,
    latency, and cost.

The learner owns each implementation after Slice 0. The assistant supplies questions, hints,
reviews, and theory at the decision point—not a hidden finished solution.

## Inspiration and originality

This project adapts the document-question-answering pattern from AI Engineering Hub's Simple
RAG Workflow and GitHub RAG projects recorded in [REFERENCES.md](../../REFERENCES.md). Its
implementation, data, evaluation, and learning exercises are original.
