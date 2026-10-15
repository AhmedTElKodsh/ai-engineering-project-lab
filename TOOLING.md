# Tool adoption and comparison

The core route learns each mechanism with an existing library or framework, with the theory needed to use it correctly. The [library map](docs/learning-path/08-LIBRARY-MAP.md) tiers libraries as core, compare once, or know about, and names the stage that teaches each one.

Order within a stage: the official library first (provider SDK, `sentence-transformers`, Chroma, `rank_bm25`), then the orchestration layer (LangChain, LlamaIndex, LangGraph). This keeps Mushir's library-based code readable and the job-market frameworks familiar. A framework never replaces the learner's explanation of what it does.

A library joins `pyproject.toml` when its stage starts, in a dependency group named after the stage, with the version taken from the lock file and its official documentation checked then. The default environment stays small: the inherited Pydantic boundary and pytest/Ruff development tools. Default tests use deterministic fake models and tools; live provider calls need explicit session authorization and a budget.

A compare-once experiment needs a concrete question, fixed inputs, baseline, quality/cost/latency or clarity metric, bounded budget and an exit decision: keep, defer or drop. Production adoption in Mushir needs a measured benefit.

Plain-Python reimplementation of framework mechanisms, NumPy/PyTorch internals and the learner-written language model belong to the optional from-scratch track. That track keeps its own boundary in the [model build specification](docs/learning-path/05-LLM-BUILD-SPEC.md): manual gradients before autograd, and no ready-made transformer class in place of the learner's architecture.
