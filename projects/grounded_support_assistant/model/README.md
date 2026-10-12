# Internal small-model laboratory

This component is planned learner work inside the same support workbench. No trained model or completed transformer is supplied by consolidation. The governing [build specification](../../../docs/learning-path/05-LLM-BUILD-SPEC.md) defines architecture, compute profiles, validation and deliverables.

Reuse approved/synthetic corpus provenance and document-level split discipline. Build count models and manual gradients first; implement and check backprop for a small network before tensor/autograd training. Then write byte/BPE tokenization, shifted next-token windows, embeddings/positions, scaled multi-head causal attention, normalization/residuals/feed-forward blocks, output logits and loss. Own train/evaluate/checkpoint/reload/generate commands.

Use the smallest CPU profile first and measure steps/second and peak memory before committing to a longer run. Verify causal invariance under changed future input, gradient parity, one-batch overfit, actual parameter changes, compatible held-out baseline metrics and deterministic checkpoint reload. Protect final test data from tuning. Report size/data/runtime honestly; the result is a complete small language model, not frontier-scale capability.

The six retained mechanism exercises are a preparatory shelf. Their forward transformer-style block lacks the full causal-model/training endpoint. Their passes cannot complete S6/S7. Integrate learned primitives into this component and compare its narrow completion behavior with the assistant's existing adapter at S8.
