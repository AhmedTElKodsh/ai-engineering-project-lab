# Library map for RAG and agents

Prepared 15 October 2026 from job-posting analyses and 2026 framework comparisons (sources below), plus the libraries Mushir actually runs on. The evidence is directional: most sources are job-board aggregations, vendor blogs or single postings, not neutral surveys. Re-check versions and status in official documentation when a stage starts.

## What the market evidence says

- Across 534 agentic-AI job listings, one analysis found LangChain in about 34%, LangGraph about 22%, LlamaIndex about 14%, CrewAI about 11% and AutoGen about 8%. A second tally of 1,135 listings gave the same top three. LangChain + LangGraph was the most common pairing.
- CrewAI and AutoGen rarely appear without LangChain alongside. Microsoft folded AutoGen and Semantic Kernel into its Agent Framework 1.0 (April 2026), and AutoGen is described as being in maintenance.
- Pinecone and Weaviate are the vector stores most often named next to LangChain/LlamaIndex in postings; no reliable store ranking was found.
- Evaluation and observability are repeatedly called the scarce, best-paid skills. Teams usually pair one offline eval library (RAGAS, DeepEval) with one tracing platform (LangSmith, Langfuse, Phoenix).
- Pay differences between frameworks are small; framework-agnostic understanding matters more than loyalty to one stack.

## Tiers

**Core** means hands-on in the named stage, with evidence. **Compare once** means one bounded rebuild or experiment, then keep, defer or drop. **Know about** means you can explain what it is for and when you would pick it; no install is required.

| Area | Core | Compare once | Know about |
|---|---|---|---|
| Provider access | `openai` SDK against OpenAI-compatible endpoints (OpenRouter, Groq) — S2 | LiteLLM for multi-provider routing — S2 | Anthropic and Google SDKs |
| Data validation | Pydantic — S1, S2 | | |
| HTTP and async | `httpx` — S1 | | |
| Orchestration | LangChain (models, prompts, loaders, splitters, retrievers) — S2, S3 | | Haystack |
| RAG framework | LlamaIndex — S3 | | |
| Document parsing | `pypdf` or PyMuPDF, `python-docx`, BeautifulSoup — S3 | Docling — S3 | OCR with Tesseract for scanned PDFs |
| Embeddings | `sentence-transformers` (multilingual models such as BGE-M3) — S3 | A hosted embedding API — S3 | |
| Vector stores | Chroma — S3 | Qdrant or pgvector — S4 | Pinecone, Weaviate, FAISS |
| Hybrid and re-ranking | `rank_bm25`, cross-encoder re-rankers — S4 | | Hosted re-rank APIs |
| RAG evaluation | RAGAS or DeepEval (pick one) — S4 | The other one — S4 | promptfoo |
| Observability | LangSmith — S2 onward | Langfuse — S4 | Arize Phoenix (OpenTelemetry) |
| Agent graphs | LangGraph (state, checkpointer, interrupts) — S5, S6 | | |
| Agent SDKs | | OpenAI Agents SDK or PydanticAI — S5; CrewAI — S6 | Microsoft Agent Framework (AutoGen successor), Google ADK, Claude Agent SDK |
| Protocols | MCP official Python SDK — S5 | | A2A (agent-to-agent) |
| Serving (later branch) | | | FastAPI, Docker, Ollama, vLLM |

## Mushir's own stack

Mushir is built mostly from separate libraries rather than one orchestration framework: `sentence-transformers`, `chromadb`, `rank_bm25`, `langchain-text-splitters`, the `openai` SDK (via OpenRouter), FastAPI, httpx, Qdrant, PostgreSQL and Redis clients. That is why each stage uses a library directly before rebuilding with LangChain or LlamaIndex: you need to read Mushir's code, and you need the frameworks for the job market and other projects.

## Adding a library

A library joins `pyproject.toml` when its stage starts, in a dependency group named after the stage, so the default environment and CI stay small. Record the version from the lock file, the official docs page used, and what the comparison concluded.

## Sources

- [AI Agent Framework Jobs 2026: 1,135 listings ranked](https://agentic-engineering-jobs.com/ai-agent-frameworks-job-market-2026)
- [We analyzed 534 agentic AI engineering jobs: the LangChain market](https://agentic-engineering-jobs.com/langchain-job-market-2026)
- [AI agent frameworks in mid-2026 (The Agent Report)](https://the-agent-report.com/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/)
- [AI agent frameworks compared 2026 (AgentMelt)](https://agentmelt.com/blog/ai-agent-frameworks-compared-2026/)
- [Agentic AI frameworks 2026: production comparison (Uvik)](https://uvik.net/blog/agentic-ai-frameworks/)
- [Best LLM and RAG evaluation tools 2026 (AgentsCamp)](https://agentscamp.com/guides/evaluation/best-llm-eval-tools-2026)
- [Top LLM observability and evaluation platforms 2026 (MarkTechPost)](https://www.marktechpost.com/2026/08/09/top-llm-observability-and-evaluation-platforms-in-2026-langfuse-langsmith-braintrust-arize-and-more-compared/amp/)
- [Hiring AI engineers 2026 (callmissed)](https://www.callmissed.com/en/blog/hiring-ai-engineers-2026)
- [The AI engineer in 2026: what the role actually requires (Tribune India)](https://www.tribuneindia.com/news/business/the-ai-engineer-in-2026-what-the-role-actually-requires/)
