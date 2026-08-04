# Project roadmap

The sequence covers recurring project cases, not one oversized application. Estimates assume
5–7 focused hours per week and are planning ranges, not completion promises.

| # | Project case | Recurring engineering pattern | Main tools introduced | Range |
|---|---|---|---|---|
| 1 | Grounded Support Assistant | Production RAG with abstention and citations | Pydantic, provider SDK, FAISS, Sentence Transformers, LangChain, Qdrant, promptfoo, LangSmith, FastAPI | 10–12 weeks |
| 2 | Auditable Document Intake | OCR, extraction, validation, and human correction | Docling/PyMuPDF, vision model, Pydantic, object storage, PostgreSQL | 5–6 weeks |
| 3 | Approval-Aware Operations Agent | Stateful tool use, retries, memory, and human approval | LangGraph, MCP, LangSmith, Redis; bounded framework comparisons | 7–8 weeks |
| 4 | Relationship Investigation | Graph construction and GraphRAG versus vector RAG | Neo4j, Microsoft GraphRAG, retrieval evaluation | 6–7 weeks |
| 5 | Domain Adaptation Lab | Dataset curation, training, and honest model comparison | Datasets, Transformers, Accelerate, PEFT/LoRA, TRL, MLflow | 7–8 weeks |
| 6 | Local Inference Service | Quantization, batching, serving, and capacity measurement | Ollama, Docker, OpenTelemetry; vLLM when hardware permits | 5–6 weeks |
| 7 | Production AI Capstone | Secure service operations across earlier patterns | FastAPI, LiteLLM, Postgres, Redis, object storage, Langfuse, CI/CD, red teaming | 9–11 weeks |

## Mastery gate for every project

A project advances only when the learner can:

1. run it from a clean checkout;
2. explain the baseline and its failure modes;
3. reproduce evaluation, latency, and cost results;
4. defend each major dependency against a simpler alternative;
5. handle invalid input, provider failure, secrets, and unsafe output;
6. make a small change without step-by-step instructions.
