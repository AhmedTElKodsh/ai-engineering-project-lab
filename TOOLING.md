# Tool practice map

The target is transferable engineering judgment, not a checklist of imports. “Deep” means
using the tool in a real case, debugging it, evaluating it, and explaining when not to use it.

## Deep practice

| Capability | Primary tools | Required evidence |
|---|---|---|
| Engineering workflow | Python, Git, uv, Ruff, pytest, GitHub Actions, Docker | Locked run, tests, CI, container |
| Contracts and APIs | Pydantic, FastAPI, JSON Schema/OpenAPI | Rejected invalid input and typed output |
| Model access | One direct provider SDK, then LiteLLM | Provider comparison, retry/cost/fallback test |
| Retrieval | FAISS, Sentence Transformers, Qdrant, PostgreSQL/pgvector | Recall/ranking, latency, and migration comparison |
| Application workflows | LangChain, LangGraph, official MCP SDK | Explicit flow, state, tools, retries, approval boundary |
| Evaluation | promptfoo, Ragas, LangSmith | Versioned cases, CI gate, regression report |
| Observability | LangSmith, Langfuse, OpenTelemetry/OpenInference | Trace, score, latency, token and cost views |
| Models and adaptation | PyTorch, Transformers, Datasets, Accelerate, PEFT/LoRA, TRL, safetensors, MLflow | Baseline versus tuned model on held-out data |
| Local inference | Ollama; vLLM when suitable GPU access exists | Reproducible quality/throughput/resource benchmark |
| Application data | PostgreSQL, Redis, S3-compatible object storage | Persistence, cache/queue behavior, recovery check |
| Specialized cases | Docling or PyMuPDF, Neo4j with GraphRAG, garak or PyRIT | Extraction, graph, and security-specific evaluations |

## Compare once

These tools broaden judgment without turning the roadmap into duplicate implementations:

- LlamaIndex and Haystack against the primary RAG path;
- pgvector against Qdrant, and Chroma as a local prototype;
- DeepEval against promptfoo, and Phoenix against Langfuse/LangSmith;
- CrewAI and Microsoft Agent Framework against an explicit LangGraph workflow;
- OpenAI Agents SDK and PydanticAI as bounded agent-framework comparisons;
- DSPy after a useful evaluation dataset exists;
- Outlines or Guardrails AI against provider-native structured output;
- Weights & Biases against local-first MLflow, and Unstructured against Docling;
- A2A as one interoperability exercise;
- llama.cpp and SGLang against vLLM only on available target hardware;
- bitsandbytes when compatible hardware makes a QLoRA experiment useful;
- Elasticsearch/OpenSearch only when hybrid search needs outgrow the chosen database.

## Defer until measurements justify them

Milvus, Weaviate, BentoML, Kubernetes, distributed serving, and full multi-agent systems are
not early learning dependencies. Add one only when a project has a measured scale,
deployment, or coordination problem that the existing stack cannot solve.

Hugging Face TGI is archived and is not a new-project target. AutoGen and Semantic Kernel
remain useful for reading existing systems, while Microsoft directs new agent work toward
Agent Framework. Starlette and Uvicorn are learned through FastAPI rather than treated as
separate portfolio goals. Microsoft GraphRAG is a bounded comparison, not the default RAG
architecture: its own documentation describes a demonstration and warns about indexing cost.

## Decisions from the tool-report audit

The report's strongest additions were LiteLLM, Sentence Transformers, FAISS/Qdrant,
promptfoo/Ragas, Langfuse, Ollama, TRL, OpenTelemetry, MCP, and A2A. The audit also added
missing real-project building blocks: document ingestion, hybrid search, graph storage,
security testing, experiment tracking, PostgreSQL/Redis/object storage, and reproducible CI
tooling.

Exact popularity rankings were not adopted: the report did not expose reproducible scoring,
and its embedded citation markers were not usable public references.
