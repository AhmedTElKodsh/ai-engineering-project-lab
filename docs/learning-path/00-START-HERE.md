# Ahmed's project route: Python to AI engineering to a language model

Revised 14 October 2026 to implement the [independent audit](../review/from-scratch-audits/python-to-llm-audit-2026-10-12.md). The audit remains the historical reviewed snapshot; this package and the project route were corrected without learner completion awards.

Prepared 11 October 2026. Status: the S0 project route was adopted on 14 October 2026 and folded into this workbench on 15 October 2026. No learner completion is awarded by either step.

## The recommendation

Build two connected projects: **a grounded document assistant** and **a language-model laboratory**. Start with a small local text-search feature in the assistant. Use it to diagnose and develop Python skills. Add model interaction, RAG, and bounded agent tools; then build the learning algorithms and transformer internals in the laboratory. Return to the assistant for a measured integration and reliability capstone.

This creates a useful application early and keeps the long-term goal of implementing a model yourself visible. Each project has successive releases. Small experiments live inside those projects rather than becoming a collection of unrelated tutorials.

Your clarification governs this plan:

- Study **two hours a day, five days a week: 10 hours/week**.
- Use **CPU as the baseline** on both desktop and laptop.
- Treat the desktop GTX 1050 Ti as an optional later experiment; its memory and current software compatibility have not been verified.
- Cover cumulative Python, software engineering, ML, deep learning, LLMs, **RAG and agents**, along with evaluation and system reliability.
- You write the learning code. The tutor explains, demonstrates small isolated examples, reviews attempts, and adjusts difficulty.
- The tutor guides you to the solution with progressively stronger hints. If you remain stuck after an attempt and useful hints and ask for more help, it may supply the smallest tricky part; you implement and integrate the rest. A complete solution requires your explicit request for a complete solution. See the [tutor conduct and hint ladder](01-LEARNING-METHOD.md#tutor-conduct).

The application theme is a replaceable teaching vehicle. A document assistant offers frequent opportunities to practice common AI engineering patterns. You have requested cumulative skill coverage, rather than a specific business domain. Begin with a tiny, non-sensitive text corpus; choose the eventual domain after you have used the first release.

## Read the planning package

| Document | Purpose |
|---|---|
| [Learning method](01-LEARNING-METHOD.md) | Research basis, session structure, hints, review, and tutor conduct |
| [Project roadmap](02-PROJECT-ROADMAP.md) | Nine stages, concrete releases, prerequisites, effort, and exit gates |
| [Skills and mastery](03-SKILLS-AND-MASTERY.md) | Python diagnostic and cumulative AI engineering coverage |
| [First four weeks](04-FIRST-FOUR-WEEKS.md) | Twenty two-hour sessions, with adaptation rules |
| [Language-model build specification](05-LLM-BUILD-SPEC.md) | Exactly what you implement, compute limits, and proof of training |
| [Curriculum map and state](06-CURRICULUM-MAP-AND-STATE.md) | Verified local lesson links and interaction with the saved route |
| [Party discussion and decisions](07-ROUND-TABLE-AND-DECISIONS.md) | The disagreements behind the proposal and open choices |

The review of your five supplied project sources is a separate personal research annex inside this repository: [Project-source review](../research/PROJECT-SOURCE-REVIEW.md). This keeps external curriculum-repository references out of curriculum documentation.

## The cumulative route

```mermaid
flowchart TD
    S0["S0: Diagnose through a small text task"] --> S1["S1: Build a reliable document-search CLI"]
    S1 --> S2["S2: Add model interaction and evaluated RAG"]
    S2 --> S3["S3: Add a bounded agent and tool contracts"]
    S3 --> S4["S4: Learn from data: probability and gradient descent"]
    S4 --> S5["S5: Write backprop and a small neural network"]
    S5 --> S6["S6: Write tokenization and a causal transformer"]
    S6 --> S7["S7: Train, checkpoint, evaluate, and generate"]
    S7 --> S8["S8: Compare models and harden the assistant"]
    S1 -. "Shared corpus and data contracts" .-> S4
    S2 -. "Shared evaluation discipline" .-> S7
    S3 -. "Shared tracing and budgets" .-> S8
```

The connections are deliberate. File handling becomes dataset ingestion. Counting words becomes probability estimation. A test suite becomes an evaluation harness. JSON persistence becomes checkpoint metadata. A prediction function becomes a model adapter. A bounded workflow becomes an agent loop. These are conceptual connections; share source code only after two actual consumers demonstrate that it fits.

## What 'a full LLM from scratch' means here

The required outcome is a **complete small decoder-only language-model system trained from random weights**. You implement its tokenizer, input/target construction, embeddings, attention, normalization, feed-forward blocks, next-token objective, training orchestration, checkpoint handling, and generation. You first implement backpropagation and a small network yourself, then use PyTorch's tensor and differentiation engine for practical transformer training while retaining your own model architecture.

A model at this learning scale is a small language model with the core architecture and lifecycle used in LLMs. The plan does not establish frontier-scale capability, reliable factual question answering, or strong instruction following. Those capabilities need separate data, compute, and evaluation. The name of the project must report its actual size and training evidence.

Training a base model, calling a hosted model, RAG, and fine-tuning are different achievements. Record them separately. The laboratory's tiny model does not automatically replace the assistant's more capable generation model. Its first useful integration may be a text-completion tool with a narrow task.

## Effort and calendar

These are planning estimates, not research findings or fixed deadlines. They include reading, coding, debugging, tests, and review; unattended long training time is additional elapsed time.

| Stage | Focused hours | Cumulative focused hours |
|---|---:|---:|
| S0: Diagnostic and project framing | 4–6 | 4–6 |
| S1: Intermediate Python through document search | 26–38 | 30–44 |
| S2: Model interaction and RAG | 36–52 | 66–96 |
| S3: Bounded agents and tools | 20–30 | 86–126 |
| S4: Math, classical learning, and text baselines | 50–70 | 136–196 |
| S5: Backpropagation and neural networks | 45–65 | 181–261 |
| S6: Tokenizer and transformer implementation | 60–85 | 241–346 |
| S7: Training and inference | 45–70 | 286–416 |
| S8: Integration and reliability | 20–30 | **306–446** |

S8 currently contains a provisional 20–30-hour allowance, not an accepted budget for all its work. Re-estimate its integration/reliability, adaptation-literacy, and final-demonstration slices after S7. The totals below retain that placeholder; no replacement estimate is defensible without observed pace.

Add a **20% planning reserve** for repair and retention: approximately **367–535 hours**, or **37–54 study weeks at 10 hours/week**, roughly **9–13 months of consistent study**. Time away adds calendar weeks. These estimates assume the bounded scopes in the roadmap; a full tensor-autograd engine, larger-scale pretraining, or additional framework projects change the estimate.

An initial evaluated RAG release is estimated at approximately **8–12 study weeks including reserve**. The first bounded agent release is approximately **11–16 weeks cumulatively**. A useful local search release comes earlier. Re-estimate after the diagnostic, first project release, first gradient implementation, and first transformer benchmark.

## Advancement, retention, and closure

Readiness and final closure are distinct under [the evidence protocol](EVIDENCE-PROTOCOL.md). Collect these forms of evidence:

1. **Execution:** learner-authored code runs on the documented command and relevant tests pass.
2. **Explanation:** you trace the mechanism and explain a design choice in your own words.
3. **Transfer:** you independently implement a small new contract or repair an unfamiliar bug after the teaching example is closed. A trace or changed-input rerun alone is useful execution evidence, not independent construction.
4. **Retention:** you pass a fresh delayed implementation/debug task independently; assisted delayed work remains practice, not retained construction.

The first three establish **ready to advance**. Keep a dated fresh task as **retention pending** and continue reachable work. A failed delayed check triggers targeted repair and another review; it does not erase earlier evidence or restart a whole phase. **Retained** requires the delayed independent pass. A stage is **closed** only when every required core/live/quality gate is ready and retained. Pending external evidence remains visible while local work proceeds.

Help is recorded, not punished. Reading documentation is allowed for implementation. Independent assessment uses a small fresh task with AI completion disabled; syntax references can remain available where the task tests design rather than memorization.

## Boundaries and next action

These documents record a plan, not learner results. They do not create a completed learner application, start billable calls, train a model, or award completion.

The S0 project route was adopted on 14 October 2026 in the curriculum clone and folded into this repository on 15 October 2026. Its resolver lives in [`from-scratch/`](../../from-scratch/README.md), and the learner's own code and evidence live in the separate learner workspace named in [`from-scratch/route.json`](../../from-scratch/route.json). Running the resolver returns **S0**, the text-counting diagnostic.

This repository also contains the 12 October workbench state engine (`learning/route.json`, `scripts/learning_state.py`). The two engines have not been reconciled yet. Until they are, follow the `from-scratch` project route for the learner's next step, and treat `learning/` as the record of the six-repository consolidation.

The next guided session opens **S0, task 1** from the first-four-weeks plan in the learner workspace. If an earlier project already contains a search baseline, use it for a fresh explanation and change task. Do not require the learner to rebuild demonstrated skills just to match this document's order.

See the [six-repository review and merge decisions](../review/CONSOLIDATION.md) and the [audits behind this revision](../review/from-scratch-audits/).
