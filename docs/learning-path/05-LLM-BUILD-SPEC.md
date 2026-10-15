# Specification for the learner-built language model

Prepared 11 October 2026; reclassified 15 October 2026. **This is the contract for the optional from-scratch track, not a route stage.** The core route (S0–S6 in the [roadmap](02-PROJECT-ROADMAP.md)) learns RAG and agents with existing frameworks. Start this track only by choice, after or alongside the core.

The track has five phases, renumbered from the previous route's S4–S8: **T1** count baselines, probability and gradient descent; **T2** manual backpropagation and a small network; **T3** tokenizer and causal transformer; **T4** training from random weights, checkpoint and generation; **T5** comparison with the assistant's model and tiny SFT/LoRA experiments. Their detailed slices are under Phase slices at the end of this document. This is a build contract, not implemented code or a claim of current model performance.

## Outcome and authorship

Build a small, complete, decoder-only autoregressive language model trained from random weights, with a tokenizer, dataset pipeline, training, checkpoints, evaluation, and bounded generation. Report the parameter count and data/compute actually used.

The required scratch boundary is explicit:

| Layer | Learner implements | Library/runtime may supply |
|---|---|---|
| Foundations | Scalar graph/backprop; small-network gradients; SGD; a small Adam comparison | Python stdlib; NumPy arrays after raw examples |
| Tokenizer | Deterministic BPE train/encode/decode; byte fallback; persistence | UTF-8 conversion and file I/O |
| Model | Embeddings, affine projections, attention/mask, head transformations, normalization, residuals, MLP, logits | PyTorch tensors, `nn.Parameter`/module registration, autograd, device execution |
| Objective/update | Shifted targets; loss explained and a stable small reference; training/update orchestration | Validated library cross-entropy and optimizer for longer runs after comparison |
| Lifecycle | Batch construction, split manifests, checkpoint/resume, evaluation, generation | Array/tensor storage and standard filesystem tools |

No pretrained weights, ready-made GPT class, `nn.Transformer`, or `nn.MultiheadAttention` counts as the learner model implementation. Such components may be comparison references after the independent mechanism works. The original attention paper supports the components; this project chooses a simplified decoder architecture. [Primary attention source](https://arxiv.org/abs/1706.03762)

A full tensor-autograd engine and manually derived gradients for every transformer operation are optional additional depth. They are not silently included in the default effort estimate. The required scalar/manual-neural proof comes before relying on PyTorch differentiation.

## Required components

1. **Data provenance:** source terms, raw document IDs/hashes, preprocessing policy, and train/validation/test membership.
2. **Tokenizer:** raw byte baseline, then deterministic BPE; reserved IDs for boundary/control tokens; saved merges/vocabulary and hash.
3. **Examples:** input tokens at positions `0..T-1`, targets at `1..T`; explicit document boundaries; no cross-split windows.
4. **Embeddings:** token lookup plus learned position embeddings up to a configured maximum context.
5. **Decoder blocks:** pre-layer normalization, multi-head masked self-attention, residual addition, feed-forward activation/projection, residual addition.
6. **Output:** final normalization and projection to vocabulary logits. Weight tying is optional and its parameter-count effect must be reported.
7. **Loss:** mean negative log probability of target tokens, with explicit padding/mask policy if variable-length batches are introduced.
8. **Training:** seeded initialization, learning rate, batch/step limits, gradient reset, backward/update, periodic validation, finite-value checks.
9. **Checkpoint:** model, optimizer, configuration, tokenizer identity, split identity, step, and relevant random-generator states.
10. **Inference:** evaluation mode, bounded autoregressive loop, greedy and temperature/top-k sampling, context policy, EOS handling, decode policy.
11. **Report:** architecture, training conditions, compatible baselines, held-out metrics, samples, failure analysis, and limitations.

Adam is a useful optimizer comparison after SGD is understood. Longer-run optimizer choices and hyperparameters are experiments, not a requirement to emulate a particular production model. [Adam source](https://arxiv.org/abs/1412.6980)

## Tensor contract

| Quantity | Shape |
|---|---|
| Input and target IDs | `(B, T)` |
| Token plus position representation | `(B, T, D)` |
| Q/K/V after head split | `(B, H, T, D/H)` |
| Attention scores and weights | `(B, H, T, T)` |
| Combined attention output | `(B, T, D)` |
| Vocabulary logits | `(B, T, V)` |
| Scalar mean loss | `()` |

`D` must be divisible by `H`. The causal mask allows each position to use itself and previous input positions; the shifted target is the next token. Test sequence lengths 1, the configured maximum, and beyond the limit. Reject out-of-range token IDs with useful errors.

## CPU-first configurations

These are starting experiments, subject to RAM and throughput measurements. They are not recommended training-duration guarantees.

| Configuration | Vocabulary | Blocks / width / heads | Context / batch | Purpose |
|---|---:|---|---|---|
| C0 correctness | 256 bytes plus explicit controls | 1 / 32 / 1 | 16–32 / 1–4 | Shape checks, gradients, one-batch overfit |
| C1 CPU training | Same byte vocabulary | 2 / 64 / 2 | 64 / 4–8 | Genuine small-corpus pretraining and sampling |
| C2 optional quality experiment | BPE roughly 512–2,048 entries | 2–4 / 128 / 4 | 128 / tuned from measurement | A bounded larger run if time and memory permit |

Actual parameter counts are measured from the implementation, including embeddings, biases, and normalization. C0/C1 should be well below one million parameters under these choices. C2's count depends on vocabulary and block count; verify rather than attaching a marketing label.

Start with 100–500 measured steps after warm-up. Record tokens/second and peak memory. Calculate projected elapsed time as required processed tokens divided by measured throughput; include validation/checkpoint overhead. Set the training budget before starting a longer run. If it exceeds the budget, reduce configuration, processed tokens, or corpus scope and report the tradeoff.

FP32 training with Adam commonly needs parameter, gradient, and two moment arrays, about 16 bytes per parameter before activations, data, workspaces, and other state. Treat this as a rough accounting model; measured process/device memory governs decisions. Attention activations grow with sequence length squared, so context length is a major budget control.

The GTX 1050 Ti is optional. Verify the actual card, memory, driver, and installed PyTorch support before attempting acceleration. Do not promise current CUDA support or a larger run based solely on the card name. The laptop remains a supported CPU path.

## Data policy

Begin with learner-authored or clearly usable small text for mechanism tests. Preserve original document boundaries, choose deterministic source-level splits, and create windows after splitting. Never place adjacent overlapping windows into different splits.

Fit BPE merges and any learned preprocessing on training data only. Keep validation available for tuning and reserve a separate final test set. Check duplicate documents across splits. Save preprocessing/tokenizer/split hashes in each run.

TinyStories is a possible larger experiment because its paper investigates small models on a restricted story distribution. This does not imply an arbitrary tiny model or short run will reproduce its results. Its current dataset card lists CDLA-Sharing-1.0; inspect the license and release terms before using or redistributing data or derived artifacts. Do not assume the dataset is public domain or automatically fetch the entire collection. [Study](https://arxiv.org/abs/2305.07759), [owner's dataset card](https://huggingface.co/datasets/roneneldan/TinyStories)

BPE byte fallback supports arbitrary UTF-8 input for encoding. Arbitrary sampled byte sequences can still be invalid UTF-8; generation must state its decode/replacement policy. Control tokens must not be accidentally produced by ordinary text encoding. Normalization that changes text changes the exact round-trip requirement and must be declared. [Primary subword source](https://arxiv.org/abs/1508.07909)

## Verification gates

| Gate | Required checks |
|---|---|
| V0 numerical building blocks | Stable softmax on large logits; probabilities sum to one; finite-difference gradients at smooth points; correct shared-node accumulation. |
| V1 token/data integrity | Round trip under declared normalization; deterministic ties in merges; save/load equivalence; byte/Unicode cases; boundaries and splits preserved. |
| V2 architectural correctness | Correct shapes and finite outputs; masked future probabilities zero; changing future tokens leaves earlier logits unchanged in evaluation mode. |
| V3 actual learning | Nonzero finite gradients; parameters change after update; one-batch loss can be reduced substantially on a tiny fixture. |
| V4 lifecycle | Save/load logits agree in evaluation mode; interrupted/resumed run agrees with controlled reference within a declared tolerance; generation terminates. |
| V5 generalization | Held-out loss compared with frozen baselines; final test untouched during tuning; sample failures and limitations reported. |
| V6 learner understanding | Independently trace token IDs → logits → loss → update → next token and repair one new bug. |
| V7 adaptation literacy | Fine-tune a copy of the tiny model on prompt/response examples with prompt loss masked; verify a small LoRA projection's frozen/trainable parameter behavior; compare held-out behavior with the base model. |

Use at least five meaningful tests in each substantial learner module; tests for masks, shared gradients, token boundaries, and checkpoint mismatch are more useful than tests that merely repeat a formula from the implementation.

A tiny model may pass V0–V4 while failing V5. Report structural completion and unresolved quality separately. If the intended quality gate fails, investigate data, objective, capacity, and training duration. Do not make a larger model the automatic first fix.

## Fair comparisons

Use the same byte/character tokenizer and held-out documents for the unigram, bigram, neural fixed-context, and first transformer comparisons. Token-level perplexity across different tokenizers is not directly comparable. For later BPE experiments, use a common normalization such as bits per byte, with boundaries/control tokens handled consistently, and report tokenization separately.

Training loss reduction is not evidence of factual grounding. A strong completion sample is not evidence of general instruction following. Track several fixed prompts and qualitative failures, but use held-out predictive metrics for the model comparison. Separately evaluate any eventual document-QA integration.

## Reproducibility and storage

Record Python/NumPy/PyTorch versions, hardware, seed, dtype, code revision, run configuration, tokenizer hash, and split hash. Aim for comparable results under a controlled environment; exact numerical equality across devices, versions, and algorithms is not assumed.

Use owned checkpoint files only; do not load arbitrary serialized files from strangers. Small configuration and results are JSON/JSONL. Large weights and datasets stay out of the curriculum repository. Do not commit keys, downloaded corpora, generated site files, or model checkpoints.

## Minimum final artifacts

- Learner model, tokenizer, data, training, evaluation, and generation modules.
- Tests and a self-terminating CPU smoke demo.
- A small permitted fixture corpus and a dataset manifest for larger runs.
- Run manifest, checkpoint identity, metrics, and baseline comparison.
- Model card: size, objective, data, training time/hardware, appropriate tasks, and known failures.
- A short independent explanation of one training step and one generated token.

The model card describes a small language model trained by the learner. T5 includes bounded SFT and LoRA mechanism experiments for breadth; adaptation is adopted in the assistant only if the comparison supports it. A later scale-up, larger-model instruction tuning, RLHF experiment, or accelerated implementation is a new scope decision with its own evidence and budget.

## Phase slices

Carried over unchanged in substance from the 11 October roadmap, renumbered T1–T5. Release labels B1–B5 and A2–A4 refer to that earlier plan.

### T1 — Learn from data and connect the math

**Effort:** 50–70 hours. **Model releases:** B1, count-based language prediction and transparent learning baselines. **Dependency:** Python data transformation/test skills; applied model use does not replace these foundations.

#### Slices

- **B1.1 Counts to probabilities:** unigram and bigram next-token prediction; normalization, smoothing, seeded sampling, negative log likelihood, and held-out data.
- **B1.2 Vectors and similarity:** implement dot products and small matrix multiplication in Python; compare with NumPy. Connect this to A2 retrieval and tensor shapes.
- **B1.3 Learn a scalar relationship:** fit a synthetic linear regression with loss, a manually derived gradient, and gradient descent. Compare analytical and finite-difference gradients. Use a synthetic task to make the mechanism observable; an unreliable document feature is a poor first gradient example.
- **B1.4 Text classification:** label a small document/intent corpus; implement a transparent Naive Bayes or logistic baseline after the required Bayes/gradient bridge. Report confusion counts, precision/recall, and imbalance.
- **B1.5 Evaluation discipline:** split by document/source before creating related examples; prevent duplicate leakage; fit vocabulary and statistics on training data; separate tuning from final testing.

**Math:** vectors, matrices, mean/variance, derivatives, chain rule introduction, probability, Bayes when needed, logarithms, cross-entropy, and optimization. Include small hand calculations before vectorized code. Defer SVD and unrelated mathematics unless a project need arises.

**Connection to the assistant:** use intent classification to suggest a search strategy, then measure whether it improves retrieval. Keep it as a lab experiment if it does not help the assistant.

**Exit:** probabilities sum to one; finite loss on defined unseen cases; deterministic split; lower held-out NLL than the frozen unigram baseline or an honest diagnosed failure; correct regression gradient; one independent probability/gradient task. Compare language-model losses only under compatible tokenization and units.

### T2 — Write backpropagation and a neural network

**Effort:** 45–65 hours. **Model release:** B2, a learning engine and neural text predictor. **Dependency:** T1 derivatives, probability, vectors, loss, and update rules.

- Derive gradients for a scalar expression, then a tiny network.
- Implement a scalar computation graph with backward functions, topological ordering, and gradient accumulation. Test shared subexpressions rather than only a chain.
- Implement a small MLP with a forward pass, activation, loss, and hand-coded training/update loop. Learn on XOR or another tiny synthetic task before increasing dimensions.
- Build a small neural next-token predictor over a fixed short context. Compare it against the count-based model.
- Implement SGD and a small Adam experiment; compare one update against PyTorch with identical state, parameters, dtype, and hyperparameters. [Adam paper](https://arxiv.org/abs/1412.6980)
- Port the validated small network to PyTorch; compare forward outputs and gradients before using the library to scale training. PyTorch handles automatic differentiation, while you continue to own the model design. [Official autograd tutorial](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)

**Scope boundary:** a full tensor-autograd framework is optional depth. The required route uses scalar autodiff plus manual gradients on a small network, followed by PyTorch for the transformer. Writing a full differentiable tensor system changes the effort estimate substantially.

**Exit:** finite-difference gradient checks on smooth test points; shared-node accumulation correct; loss reduction on a tiny train set; held-out evaluation; explanation of zeroing versus accumulating gradients; independent diagnosis of a wrong update or missing backward edge.

### T3 — Tokenizer and a causal transformer

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

### T4 — Train, checkpoint, evaluate, and generate

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

### T5 — Integrate, compare, and harden

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
