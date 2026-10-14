# Specification for the learner-built language model

Revised 14 October 2026 to implement the [independent audit](../review/from-scratch-audits/python-to-llm-audit-2026-10-12.md). The audit remains the historical reviewed snapshot; this package and the project route were corrected without learner completion awards.

Prepared 11 October 2026. Required scope for S5–S8. This is a build contract, not implemented code or a claim of current model performance.

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
9. **Checkpoint:** model, optimizer, configuration, tokenizer identity, split identity, step, and relevant random-generator states. Shuffled/streaming batch paths also preserve the permutation/cursor; save scheduler state only if a scheduler exists. Resume testing must exercise the actual next-batch path in a fresh process.
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
| V4 lifecycle | Save/load logits agree in evaluation mode; fresh-process interrupted/resumed run agrees with controlled reference within a declared tolerance, including next batch IDs/cursor and updates; generation terminates. |
| V5 generalization | Held-out loss compared with frozen baselines; final test untouched during tuning; sample failures and limitations reported. |
| V6 learner understanding | Independently trace token IDs → logits → loss → update → next token and repair one new bug. |
| V7 adaptation literacy | Fine-tune a copy using actual loss-derived updates with the first response target correctly aligned; skip/reject and count zero-supervised-target cases after truncation. Verify initial LoRA/base output equality with one random/one zero factor, then actual adapter updates while base weights stay fixed; compare held-out behavior. |

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

The model card describes a small language model trained by the learner. S8 includes bounded SFT and LoRA mechanism experiments for breadth; adaptation is adopted in the assistant only if the comparison supports it. A later scale-up, larger-model instruction tuning, RLHF experiment, or accelerated implementation is a new scope decision with its own evidence and budget.

## Exact scoring and reference boundaries

For the first byte-baseline comparison, insert document-boundary controls as context
and score original content targets once under a fixed context/stride. Include final
partial tails; exclude padding and inserted BOS/EOS controls from the main score.
EOS prediction may be a separate reported diagnostic. Overlapping windows may supply
context but cannot double-count targets. Sum actual target NLL and divide by the
number of scored targets; perplexity is exp of that mean under the same tokenizer.
Test unequal counts: NLL totals 2/1 target and 12/3 targets combine to 14/4 = 3.5.
For BPB, use content-only NLL/(ln(2) * scored original UTF-8 content bytes), after
the declared normalization and excluding controls/padding. Save target masks/policy.

[The corrected tokenizer reference](../../from-scratch/lessons/10-llms-from-scratch/02-building-a-tokenizer/docs/en.md)
covers Unicode with stdlib and explicit control opt-in; it remains an educational
reference without persistence/production-vocabulary compatibility. The mapped
pretraining backward is partial, SFT updates are random noise, and evaluation
probabilities are simulated. Exclude those routines from numerical training parity
and model-quality claims. For the learner graph, verify gradient/update participation
for every intended trainable module and both tied-embedding uses. Qualification of
a reference is not a claim that its algorithm was repaired into complete training.

Structural readiness can precede successful held-out quality and delayed retention.
Record these independently under [the evidence protocol](EVIDENCE-PROTOCOL.md).
