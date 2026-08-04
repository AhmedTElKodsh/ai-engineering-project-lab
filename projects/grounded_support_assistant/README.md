# Project 1: Grounded Support Assistant

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

## Slice 0: transparent baseline

The current implementation ranks handbook sections by exact non-stopword token overlap. It is
intentionally too simple to be the final system; its job is to establish the contract, data,
evaluation, and failure-analysis habit before an LLM hides mistakes behind fluent text.

```powershell
uv run python .\projects\grounded_support_assistant\app.py "Can administrators view my password?"
uv run pytest
```

## Guided build slices

1. Run the 20 cases, inspect the expected paraphrase failure, and explain its cause.
2. Add one direct provider SDK and preserve Pydantic validation and abstention.
3. Build embedding retrieval with Sentence Transformers and FAISS; measure recall before adding a framework.
4. Recreate the proven flow with LangChain and record what it adds or obscures.
5. Move retrieval to Qdrant, add a cross-encoder reranker, and compare with pgvector.
6. Add Ragas/promptfoo evaluation and compare LangSmith traces with Langfuse.
7. Expose the accepted flow through FastAPI, then add LiteLLM only when a second provider or gateway policy is required.
8. Containerize, threat-model prompt injection and data leakage, and publish measured quality, latency, and cost.

The learner owns each implementation after Slice 0. The assistant supplies questions, hints,
reviews, and theory at the decision point—not a hidden finished solution.
