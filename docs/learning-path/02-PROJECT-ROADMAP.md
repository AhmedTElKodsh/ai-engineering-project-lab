# The cumulative project roadmap

Prepared 11 October 2026. Read the [mastery rules](03-SKILLS-AND-MASTERY.md) alongside these stages. Effort ranges are estimates for learner work; a stage can take longer without changing its exit criteria.

## Project architecture

**Component A: Grounded Document Assistant.** A local document-search tool evolves into an evaluated RAG application with controlled tools, persistence, and a bounded agent loop. Start with text/Markdown and a command line. Add other formats only after a demonstrated need.

**Component B: Language-Model Laboratory.** Count-based text prediction evolves through gradients, neural networks, tokenization, causal attention, and an end-to-end model trained from random weights. Reuse data and evaluation habits from A; keep architecture experiments separate from the application's stable implementation.

Both components belong to this one AI Engineering Workbench under projects/grounded_support_assistant; model/ is its internal laboratory. The current lexical baseline is inherited reference implementation. Future core solutions are learner-authored during tutoring, not supplied by consolidation. Releases A1–A4/B1–B5 label components, not competing projects or routes.

## S0 — Frame the problem and diagnose through work

**Effort:** 4–6 hours. **Project:** A. **Dependency:** none beyond a working Python interpreter and basic syntax.

Mission: find a relevant piece of information in three short local documents and report where it came from.

- State what a useful answer looks like and what should happen when nothing matches.
- Predict and write a short word-counting function.
- Explain list versus dictionary behavior and identify a mutation bug.
- Read one UTF-8 text file and handle a missing path.
- Write one meaningful assertion and explain what failure it catches.

Use the diagnostic in the mastery document. Complete unsupported concepts through short bridges. Prior scripts and commits are candidate material to inspect, not automatic proof of present mastery.

**Exit:** identify the next Python gaps; run one learner-authored function; explain it; change it for a new input. Save a starting evidence note and project location. No exam-style placement label is needed.

## S1 — Build intermediate Python through a document-search CLI

**Effort:** 26–38 hours. **Assistant release:** A1, deterministic document explorer. **Dependency:** S0 gaps repaired sufficiently to implement small functions.

### Slices

1. **A1.1 Text to records:** read approved `.txt`/`.md` files; assign document IDs; preserve source paths and paragraph offsets. Learn `pathlib`, `with`, UTF-8, list/dict transformations, and pure functions.
2. **A1.2 Records to passages:** split by paragraphs first; handle empty documents and long paragraphs with an explicit bounded policy. Introduce simple dataclasses/type hints only once records become hard to manage.
3. **A1.3 Passages to search results:** implement an overlap score, deterministic tie breaking, and top-k ranking. Progress to a small inverted index; TF-IDF is a later bridge rather than a requirement on day one.
4. **A1.4 Search to CLI:** accept a query and corpus path with `argparse`; print source IDs, excerpts, and scores; return a clear no-match result. Add JSON persistence and rebuild behavior.
5. **A1.5 Reliability:** separate modules by real responsibility; add tests, error messages, logging, and a self-terminating demo.

**Python growth:** comprehensions, sets, tuples, sorting with a key, exceptions, modules/imports, type hints, generators for file iteration, and JSON. Introduce classes through a concrete state-management need. Defer decorators, metaclasses, concurrency, and clever abstractions.

**Evaluation:** create 20 development queries with expected relevant source IDs; include exact-word queries, no-answer queries, paraphrases, ambiguity, empty text, and Unicode. Keep a separate unseen transfer set. Preserve the lexical baseline, including its paraphrase failures.

**Exit:** reproducible CLI; at least five meaningful core tests; source identity retained; deterministic ranking; documented no-match behavior; learner fixes a fresh ranking or file-handling bug. The metric threshold is agreed before implementation for the chosen fixture corpus, not invented after seeing the result.

## S2 — Model interaction and evaluated RAG

**Effort:** 36–52 hours. **Assistant release:** A2, grounded answer generation. **Dependency:** A1 and basic JSON/HTTP literacy.

### S2a: Introduce the model boundary

- Trace local program → request → hosted inference or a local model → response → extracted answer.
- Implement a small adapter with timeout, bounded retries for appropriate transient failures, clear errors, and secret-safe configuration.
- Compare zero-shot instructions and a few examples on fixed cases. Request brief task explanations where helpful; do not require hidden reasoning traces.
- Specify output fields and validate parsed JSON: answer, source IDs, and status. Check types, allowed values, unknown citations, and malformed responses.
- Persist provider/model/configuration metadata separately from secrets.

Use a deterministic fixture adapter for offline contract work. Real model interaction remains an explicit evidence gate. Choose a provider or local runtime at implementation time, using current official documentation and a measured hardware/cost budget. No billable calls are implied by this planning request.

### S2b: Add retrieval and grounding

- Insert retrieved source passages into the prompt with clear boundaries and a context budget.
- Keep the A1 lexical baseline and introduce TF-IDF/cosine similarity as a transparent vector bridge.
- Compare semantic embeddings against the lexical method on the same development cases. Use NumPy similarity calculations over a small stored matrix; a vector database is unnecessary at this scale.
- Compare one retrieval improvement: a hybrid rank fusion or a simple reranking step. Do not adopt it unless the metric and error analysis justify the added work.
- Require answerable, ambiguous, and unsupported cases. Check that cited IDs exist and that the cited passage supports each material answer claim.
- Distinguish retrieval recall from answer correctness and groundedness.

The original RAG research combines learned generation with retrieved information. This educational application uses a simpler retrieval-then-generation pipeline and should describe that difference. [RAG paper](https://arxiv.org/abs/2005.11401)

**CPU-first paths:** retrieval, evaluation, and vector operations remain local. Generation/embedding APIs are optional external adapters requiring an explicit execution budget when used. If the budget is unavailable, preserve fixture tests and retrieval results, move to local S4 work, and retain S2's live-generation and semantic-retrieval gates as pending.

**Exit:** 20 fixed development cases plus at least five retrieval-injection/failure cases; comparison with A1; evidence of real generation; semantic retrieval evidence or a clearly pending branch; schema and citation validation; latency/failure/cost report. A human support rubric is sufficient initially; a model judge alone is not a reliable ground-truth label.

## S3 — Tools and a bounded agent

**Effort:** 20–30 hours. **Assistant release:** A3, a controlled document-work agent. **Dependency:** S2 readiness, including the real model/semantic-retrieval gates. Preparatory fake-tool work may continue as practice while S2 is incomplete; it does not grant S3 readiness. If access is blocked, route eligible CPU work through S4 after S1.

Mission: answer a question that requires searching, reading a selected passage, and optionally drafting a note.

1. Implement three narrow tools: `search_documents`, `read_passage`, and `draft_note`. Treat the draft as an output artifact first; writing requires an explicit approval transition in the eventual application.
2. Validate tool names and arguments. Restrict paths to the project corpus/output directories, cap output sizes, and reject traversal and unknown IDs.
3. Start with a deterministic workflow. Add an agent loop that selects a tool or a final response, observes the result, updates state, and terminates.
4. Set limits such as six tool steps, one retry for a transient tool failure, a bounded context size, and an elapsed-time budget. Tune them using recorded tasks; do not treat these starting numbers as standards.
5. Persist explicit state and task/action IDs with JSON or SQLite. Test restart and repeated action behavior.
6. Compare the fixed workflow and agent on the same tasks. Record where the agent adds value and where the workflow is simpler or more reliable.

Use observable actions, arguments, results, and short decision summaries in traces. A request for private model reasoning is not required to build or evaluate the control loop. The ReAct paper is background for interaction between model decisions and external actions, not a requirement to reproduce its prompt format. [ReAct paper](https://arxiv.org/abs/2210.03629)

**Protocol bridge:** expose one read-only tool through an educational MCP stdio slice with initialization, capability negotiation, tool listing/calling, and error handling. Use the official specification at implementation time. A small protocol exercise is not evidence of production compliance or authentication support. [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)

**Exit:** bounded termination; invalid-tool rejection; two injected-content attacks rejected at the control boundary; approval enforcement independent of model text; restart evidence; workflow-versus-agent comparison. Run fixtures first and report live tool-selection evidence separately.

## S4 — Learn from data and connect the math

**Effort:** 50–70 hours. **Model releases:** B1, count-based language prediction and transparent learning baselines. **Dependency:** Python data transformation/test skills; applied model use does not replace these foundations.

### Slices

- **B1.1 Counts to probabilities:** unigram and bigram next-token prediction; normalization, smoothing, seeded sampling, negative log likelihood, and held-out data.
- **B1.2 Vectors and similarity:** implement dot products and small matrix multiplication in Python; compare with NumPy. Connect this to A2 retrieval and tensor shapes.
- **B1.3 Learn a scalar relationship:** fit a synthetic linear regression with loss, a manually derived gradient, and gradient descent. Compare analytical and finite-difference gradients. Use a synthetic task to make the mechanism observable; an unreliable document feature is a poor first gradient example.
- **B1.4 Text classification:** label a small document/intent corpus; implement a transparent Naive Bayes or logistic baseline after the required Bayes/gradient bridge. Report confusion counts, precision/recall, and imbalance.
- **B1.5 Evaluation discipline:** split by document/source before creating related examples; prevent duplicate leakage; fit vocabulary and statistics on training data; separate tuning from final testing.

**Math:** vectors, matrices, mean/variance, derivatives, chain rule introduction, probability, Bayes when needed, logarithms, cross-entropy, and optimization. Include small hand calculations before vectorized code. Defer SVD and unrelated mathematics unless a project need arises.

**Connection to A:** use intent classification to suggest a search strategy, then measure whether it improves retrieval. Keep it as a lab experiment if it does not help the assistant.

**Exit:** probabilities sum to one; finite loss on defined unseen cases; deterministic split; lower held-out NLL than the frozen unigram baseline or an honest diagnosed failure; correct regression gradient; one independent probability/gradient task. Compare language-model losses only under compatible tokenization and units.

## S5 — Write backpropagation and a neural network

**Effort:** 45–65 hours. **Model release:** B2, a learning engine and neural text predictor. **Dependency:** S4 derivatives, probability, vectors, loss, and update rules.

- Derive gradients for a scalar expression, then a tiny network.
- Implement a scalar computation graph with backward functions, topological ordering, and gradient accumulation. Test shared subexpressions rather than only a chain.
- Implement a small MLP with a forward pass, activation, loss, and hand-coded training/update loop. Learn on XOR or another tiny synthetic task before increasing dimensions.
- Build a small neural next-token predictor over a fixed short context. Compare it against the count-based model.
- Implement SGD and a small Adam experiment; compare one update against PyTorch with identical state, parameters, dtype, and hyperparameters. [Adam paper](https://arxiv.org/abs/1412.6980)
- Port the validated small network to PyTorch; compare forward outputs and gradients before using the library to scale training. PyTorch handles automatic differentiation, while you continue to own the model design. [Official autograd tutorial](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)

**Scope boundary:** a full tensor-autograd framework is optional depth. The required route uses scalar autodiff plus manual gradients on a small network, followed by PyTorch for the transformer. Writing a full differentiable tensor system changes the effort estimate substantially.

**Exit:** finite-difference gradient checks on smooth test points; shared-node accumulation correct; loss reduction on a tiny train set; held-out evaluation; explanation of zeroing versus accumulating gradients; independent diagnosis of a wrong update or missing backward edge.

## S6 — Tokenizer and a causal transformer

**Effort:** 60–85 hours. **Model release:** B3, independently implemented model architecture. **Dependency:** B2 and a shape/matrix refresher.

1. Begin with a byte or character baseline so model debugging has a transparent vocabulary.
2. Implement deterministic BPE training and encoding, byte fallback, save/load, and explicitly reserved control tokens. BPE is introduced as an algorithm; do not attempt compatibility with a particular production tokenizer. [Subword-tokenization paper](https://arxiv.org/abs/1508.07909)
3. Build shifted inputs/targets and document-boundary handling. Explain exactly what the model predicts at each position.
4. Implement stable softmax and scaled dot-product attention in NumPy on a very small sequence.
5. Add causal masking and multi-head shape transformations. Test future-token invariance.
6. Implement token and learned position embeddings, pre-normalization, residual paths, MLP blocks, final normalization, and output logits with PyTorch tensor primitives and learner-written modules.
7. Assemble a small decoder-only model. Compare individual mechanisms to appropriate library operations after the independent implementation.

The original transformer paper is the primary source for attention and transformer components. A causal decoder-only language model is a chosen adaptation, rather than a reproduction of its full encoder-decoder translation system. [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

**Exit:** shape annotations from IDs to logits; tokenizer round-trip/save-load tests; normalized attention weights; future information blocked in evaluation mode; finite outputs/gradients; parameter-count calculation agrees with actual parameters; one independent mask or transpose bug repair.

## S7 — Train, checkpoint, evaluate, and generate

**Effort:** 45–70 hours plus unattended compute. **Model release:** B4, a complete trained small language model. **Dependency:** B3 correctness before larger runs.

- Run the one-batch overfit test first. It proves learning machinery can fit that batch, not generalization.
- Start with a sub-million-parameter CPU model, a short context, and a small corpus. Measure throughput and memory before selecting the next run.
- Train from random weights; record configuration, seed, data split, tokenizer hash, code revision, optimizer state, metrics, and checkpoints.
- Save and resume. Compare interrupted versus uninterrupted training under a controlled local setup and stated tolerance.
- Implement greedy and temperature/top-k sampling; cap context and generated length; handle EOS and invalid arguments.
- Freeze a final held-out set. Evaluate loss, perplexity under the same tokenizer, short completions, repetition, and narrow task behavior.
- Compare the count-based model, neural context model, and transformer. Use a common byte/character tokenizer for the main comparison; handle later BPE comparisons using explicitly comparable normalization such as bits per byte.

The TinyStories study demonstrates that restricted-data language modeling can work at small scales; it does not guarantee comparable results on a small CPU training budget. Begin with learner-authored or clearly usable text. TinyStories is a later candidate after checking its current data terms and choosing a bounded subset. [TinyStories paper](https://arxiv.org/abs/2305.07759)

**Exit:** all essential mechanisms implemented; genuine parameter updates; demonstrated overfit test; reproducible held-out evaluation; checkpoint resume; bounded generation; honest limitations. The research-success target is better held-out prediction than the frozen baseline. If it fails, B4 implementation may be structurally complete but the performance gate remains open; diagnose rather than inflate the claim.

## S8 — Integrate, compare, and harden

**Effort:** 20–30 hours. **Components:** A4 and B5. **Dependency:** prior gates, with unresolved external/model quality gates visible.

- Run your model behind the same generation interface as the assistant's other model. Compare it on narrow completion tasks and separately on document QA. Poor QA is a legitimate finding.
- Preserve the capable generator for RAG if the tiny model fails the grounded-answer requirements. Consider using the tiny model for completion or another bounded task where evidence supports it.
- Add cache/version invalidation, latency measurement, retry tests, trace redaction, and reproducible evaluation commands.
- Complete a bounded supervised fine-tuning exercise on a copy of your own tiny model: format prompt/response pairs, mask prompt tokens from the loss, retain a held-out set, and compare before/after behavior on a narrow task.
- Implement a small LoRA projection experiment in PyTorch: freeze a base weight, add two trainable low-rank matrices, count trainable parameters, and compare one update and a tiny adaptation run. This teaches the mechanism without requiring a large pretrained model or an extra package. [LoRA paper](https://arxiv.org/abs/2106.09685)
- Compare adaptation with a prompting/retrieval baseline for the selected task. Educational comparison is required for breadth; adoption in the assistant depends on measured benefit. Adaptation evidence remains distinct from pretraining evidence. Large-model QLoRA is later depth, subject to a separate compute plan.
- Package a self-terminating offline demo, optional live demo instructions, test commands, dataset provenance, model card, architecture diagram, and results with code/data identifiers.
- Conduct a final walkthrough: explain one retrieved answer, one agent execution, and one training/update/generation trace; make a fresh small change in each component.

**Exit:** reproducible artifacts; baseline/candidate and small adaptation comparisons; honest CPU/cost/runtime reports; traceable learner evidence; independent transfer on Python, RAG/tools, and model internals.

## Breadth after the core

The required core covers recurring capabilities, not every named framework or AI specialization. Record one bounded future comparison for orchestration frameworks and one for an industrial retrieval store if the learner project permits those dependencies. Keep larger-model adaptation, advanced multi-agent systems, multimodal pipelines, distributed training, RLHF, and deployment platforms as separate later branches.

This workbench follows [TOOLING.md](../../TOOLING.md): standard-library mechanisms first, locked inherited boundary/development dependencies, and scoped comparisons only after a measured need or explicit learning question. The external curriculum keeps its own contribution allowlist when editing its lessons; that policy does not relocate this project or ban its inherited runtime. Broad optional comparisons remain outside the core effort estimate.
