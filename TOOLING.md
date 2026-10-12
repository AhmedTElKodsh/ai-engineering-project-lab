# Tool adoption and comparison

The required path starts with standard Python functions, files, JSON, dataclasses, explicit errors and local tests. The inherited baseline uses locked Pydantic; learner-written parsing/counting/math mechanisms should stay visible before their production equivalents.

NumPy enters after raw vector/matrix operations and shape reasoning. PyTorch tensors/autograd enter after manual gradients, finite differences and a small-network backprop proof. The learner still writes embeddings, causal attention/masks, normalization, blocks, output head and training lifecycle. Ready-made GPT/Transformer model classes do not satisfy that work.

Provider SDKs, semantic embedding libraries, API servers, MCP SDKs and orchestration frameworks are selected at their stage, with official versions verified then. A handwritten read-only MCP slice is educational protocol evidence, not complete protocol/authentication compliance.

A comparison requires a concrete question, fixed inputs, baseline, quality/cost/latency or clarity metric, bounded budget and exit decision. Production adoption requires a measured benefit or operational need. An optional framework comparison does not replace the core mechanism.

Keep vector databases, graph RAG, several agent frameworks, cloud infrastructure, distributed queues, large-model serving and RLHF as extension shelves. Their concepts can be discussed when needed, but installing each is not a prerequisite for the small CPU model. S8's tiny SFT/LoRA mechanism comparisons are bounded breadth exercises on a copy, not substitutes for random-weight training.
