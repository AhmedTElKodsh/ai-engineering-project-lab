# Curriculum mapping, state, and adoption

Revised 14 October 2026 to implement the [independent audit](../review/from-scratch-audits/python-to-llm-audit-2026-10-12.md). The audit remains the historical reviewed snapshot; this package and the project route were corrected without learner completion awards.

Prepared 11 October 2026 from the current checkout and route resolver. All lesson links below point to existing local documents. Their existence and selected contents were inspected in the original planning task. The audited corrections now have focused reference demos/tests; this still does not certify the entire curriculum or any learner implementation.

## Current verified state

Updated 15 October 2026, when this plan moved from the curriculum clone into this repository:

- The project route [`from-scratch/route.json`](../../from-scratch/route.json) was adopted on 14 October 2026 at 10 hours/week, CPU first.
- `python -X utf8 from-scratch/scripts/next_learning_route.py --project-root from-scratch --curriculum-root <curriculum checkout>` returns **S0**, "Diagnose through a text task".
- No learner completion has been recorded. The evidence ledger lives in the learner workspace, outside this repository.
- Lesson links below point to the upstream curriculum on GitHub. The learner's edited copies of four phase-10 lessons are in [`from-scratch/lessons/`](../../from-scratch/lessons/).

## Mapping policy

The table supplies **bounded project bridges**. Many lesson frontmatters list much broader prerequisites than the project task needs. Extracts are therefore explicitly focused study, not full completion and not a rewrite of the lessons' prerequisites.

Use four study labels:

- **Full:** satisfy the whole lesson contract, quiz, and artifact requirements.
- **Focused bridge:** cover the named mechanism for the project; record remaining depth.
- **Comparison:** inspect or run a reference only after learner implementation; no authorship credit.
- **Deferred:** keep the topic visible for later, with a reason.

A mapped lesson being useful does not automatically make it required in the authoritative route. Do not silently expand the existing manifest. In particular, the Phase 7 transformer capstone and Phase 10 complete pipeline have broad completion requirements; completing this custom small-model project does not close those lessons in full.

## Setup and Python bridges

| Project use | Lesson | Focus |
|---|---|---|
| S0 local readiness | [00/01 Dev Environment](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/01-dev-environment/docs/en.md) | Check actual interpreter and a self-terminating script. |
| S1/S7 evidence | [00/02 Git & Collaboration](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/02-git-and-collaboration/docs/en.md) | Explain working changes, commit identity, and reproducible evidence. |
| S0/S1 environment | [00/06 Python Environments](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/06-python-environments/docs/en.md) | Isolate the learner environment; avoid installing the whole curriculum stack. |
| S1/S4/S7 data | [00/09 Data Management](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/09-data-management/docs/en.md) | Provenance, splits, and persistence; use text/JSON initially. |
| All stages debugging | [00/12 Debugging & Profiling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/12-debugging-and-profiling/docs/en.md) | Traceback, `pdb`, logging, timing, `cProfile`, `tracemalloc`; skip disallowed extra profilers. |
| S2 live model boundary | [00/04 APIs & Keys](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/04-apis-and-keys/docs/en.md) | Request/response, local secret entry, timeouts and safe errors. |

The repository does not supply a complete intermediate-Python module for this project. The planned S0/S1 tasks fill that gap using original exercises and selected sections of the [official Python 3.12 tutorial](https://docs.python.org/3.12/tutorial/). Do not create new curriculum lesson directories merely to execute the personal learning plan.

## Applied AI bridges

| Stage | Lessons | Focus |
|---|---|---|
| S2 prompts | [11/01 Prompt Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/01-prompt-engineering/docs/en.md), [11/02 Few-Shot](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/02-few-shot-cot/docs/en.md) | Controlled prompt comparison; context and examples; avoid equating explanation with hidden reasoning. |
| S2 contracts | [11/03 Structured Outputs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/03-structured-outputs/docs/en.md) | JSON parsing, schema concepts, invalid-output handling; use the allowed stack. |
| S2 vectors/context | [11/04 Embeddings](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/04-embeddings/docs/en.md), [11/05 Context Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/05-context-engineering/docs/en.md) | Semantic similarity and context budgets; preserve lexical baseline. |
| S2 retrieval | [11/06 RAG](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/docs/en.md), [11/07 Advanced RAG](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/07-advanced-rag/docs/en.md) | Retrieval → context → generation; compare one improvement. |
| S3 tools | [11/09 Function Calling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/09-function-calling/docs/en.md), [11/14 MCP](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/14-model-context-protocol/docs/en.md) | Tool contracts and protocol bridge; declare educational scope. |
| S3 orchestration | [11/16 State Machines](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/16-langgraph-state-machines/docs/en.md) | State, transitions, checkpoints, approval; own Python state machine first. |
| S2/S8 evaluation | [11/10 Evaluation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/10-evaluation/docs/en.md) | Cases, baselines, failure analysis; real and fixture evidence separated. |
| S8 reliability | [11/11 Caching & Cost](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/11-caching-cost/docs/en.md), [11/12 Guardrails](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/12-guardrails/docs/en.md) | Cache identity/invalidation, budgets, trust boundaries, redaction. |

## Mathematics and ML bridges

| Mechanism | Lessons | When |
|---|---|---|
| Vector intuition and operations | [01/01 Linear Algebra](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/01-linear-algebra-intuition/docs/en.md), [01/02 Vectors & Matrices](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/02-vectors-matrices-operations/docs/en.md) | S2 tiny similarity example; deeper S4 raw implementation. |
| Tensors and stability | [01/12 Tensor Operations](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/12-tensor-operations/docs/en.md), [01/13 Numerical Stability](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/13-numerical-stability/docs/en.md) | Before S5/S6 vectorization and softmax. |
| Similarity and norms | [01/14 Norms & Distances](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/14-norms-and-distances/docs/en.md) | S2/S4 cosine, normalization and distance choices. |
| Probability/Bayes | [01/06 Probability](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/06-probability-and-distributions/docs/en.md), [01/07 Bayes](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/07-bayes-theorem/docs/en.md) | S4 counts, smoothing and a transparent classifier. |
| Derivatives and chain rule | [01/04 Calculus](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/04-calculus-for-ml/docs/en.md), [01/05 Chain Rule & Autodiff](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/05-chain-rule-and-autodiff/docs/en.md) | S4 regression, then S5 backpropagation. |
| Optimization and information | [01/08 Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/08-optimization/docs/en.md), [01/09 Information Theory](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/01-math-foundations/09-information-theory/docs/en.md) | Updates, log loss, perplexity, and compression interpretation. |
| Learn from data | [02/01 What Is ML](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/01-what-is-machine-learning/docs/en.md), [02/02 Linear Regression](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/02-linear-regression/docs/en.md) | S4 synthetic task and generalization. |
| Text classification | [02/14 Naive Bayes](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/14-naive-bayes/docs/en.md), [02/03 Logistic Regression](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/03-logistic-regression/docs/en.md) | S4 choose one implementation; contrast the other only if helpful. |
| Evaluation and generalization | [02/09 Model Evaluation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/09-model-evaluation/docs/en.md), [02/10 Bias-Variance](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/10-bias-variance/docs/en.md) | S4/S7 splits, overfitting, and honest metrics. |

## Neural networks, text, and transformer bridges

| Stage | Lessons | Focus |
|---|---|---|
| S5 network mechanics | [03/01 Perceptron](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/01-the-perceptron/docs/en.md), [03/02 Forward Pass](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/02-multi-layer-networks/docs/en.md), [03/03 Backpropagation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/03-backpropagation/docs/en.md) | Scalars, small networks, computation graph and accumulation; first probe shared graph identity/execution order and an unrelated stored callback. |
| S5 training choices | [03/04 Activations](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/04-activation-functions/docs/en.md), [03/05 Losses](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/05-loss-functions/docs/en.md), [03/06 Optimizers](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/06-optimizers/docs/en.md) | Derive a small case and compare an update. |
| S5/S7 stability | [03/07 Regularization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/07-regularization/docs/en.md), [03/08 Initialization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/08-weight-initialization/docs/en.md), [03/09 Schedules](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/09-learning-rate-schedules/docs/en.md) | Apply only needed mechanisms after baseline training works. |
| S5 abstraction/comparison | [03/10 Mini Framework](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/10-mini-framework/docs/en.md), [03/11 PyTorch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/11-intro-to-pytorch/docs/en.md) | Focused small-network interface and library parity; full framework remains optional depth. |
| S1/S4 text | [05/01 Text Processing](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/01-text-processing/docs/en.md), [05/02 BoW & TF-IDF](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf/docs/en.md), [05/14 Information Retrieval](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/docs/en.md) | Normalization, transparent vectors and retrieval. |
| S4 prediction | [05/16 N-gram Models](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/docs/en.md) | Counts → distributions → smoothing → held-out NLL. |
| S6 attention | [07/02 Self-Attention](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch/docs/en.md), [07/03 Multi-Head](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/03-multi-head-attention/docs/en.md), [07/04 Positions](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/04-positional-encoding/docs/en.md) | Q/K/V, mask, shapes, learned position baseline; advanced encodings deferred. |
| S6 architecture | [07/05 Full Transformer](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/05-full-transformer/docs/en.md), [07/07 GPT](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/07-gpt-causal-language-modeling/docs/en.md) | Contrast encoder/decoder; implement the causal decoder subset. |
| S6 tokenization/data | [10/01 Tokenizers](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/01-tokenizers/docs/en.md), [10/02 Building a Tokenizer](../../from-scratch/lessons/10-llms-from-scratch/02-building-a-tokenizer/docs/en.md), [10/03 Data Pipelines](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/03-data-pipelines/docs/en.md) | Byte/BPE and split-safe shifted windows; corrected 10/02 stdlib reference covers Arabic/Unicode and requires explicit control opt-in. It is educational, without persistence/production parity. |
| S7 training | [10/04 Mini-GPT Pretraining](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/04-pre-training-mini-gpt/docs/en.md), [10/10 Evaluation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/10-evaluation/docs/en.md) | CPU configuration and lifecycle concepts only: 10/04 Python backward omits attention/first norm/positions/input-use tied gradients; 10/10 probabilities are simulated. Exclude both from training/quality parity. Verify all intended gradients, actual logits, count-weighted targets, and real next-batch resume on the learner graph. |
| S8 lifecycle/adaptation | [10/13 Complete Pipeline](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/13-building-complete-llm-pipeline/docs/en.md), [10/06 SFT](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/10-llms-from-scratch/06-instruction-tuning-sft/docs/en.md), [11/08 LoRA](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/08-fine-tuning-lora/docs/en.md) | Selected lifecycle concepts; required tiny SFT/LoRA checks on the validated learner graph. 10/06 random weight perturbations are not SFT and are excluded from adaptation parity. Test first response alignment/zero targets and initial LoRA equality plus genuine adapter update. No full-lesson/large-model claim. |

## Important mismatches with the existing route

1. **Pace:** saved 5–7 hours differs from your new 10-hour instruction.
2. **Readiness:** the existing route begins prompting; this proposal adds a project-based Python diagnostic and build before that step.
3. **End goal:** the saved M1 prioritizes an applied stack; this proposal makes learner-written training and model internals required within the main route.
4. **Framework breadth:** saved M1 includes LoRA, MCP and LangGraph. This proposal keeps tool/protocol/state concepts and tiny adaptation comparisons, makes adoption conditional on evidence, and separates prohibited framework implementations from curriculum work.
5. **Compute:** the local pretraining lesson is titled 124M parameters and contains a short training-time claim. Treat it as reference material; the plan does not carry that claim forward to your CPU or assume its code establishes a complete successful run.
6. **Prerequisite breadth:** local frontmatters often require full phases or intervening lessons. Project bridges preserve deferred depth and do not certify those whole prerequisites as done.

The existing route is a legitimate application-first route. The new plan is a proposed evolution based on your updated goal, not evidence that earlier work was wasted.

## Adoption without losing state

Adoption happened on 14 October 2026 (see the [historical runbook](ADOPTION-RUNBOOK.md)). The steps below are kept as the procedure for any later route change.

When you ask to use this plan for actual tutoring:

1. Locate the learner workspace and inspect its current instructions/state.
2. Preserve genuine previous execution/explanation evidence; test current transfer where needed.
3. Update the saved pace and explicitly choose how to represent the project route: initially a recorded detour, or later explicit adoption of the validated inactive project candidate with project-stage IDs and bridge labels. Its validation does not activate it.
4. Keep curriculum completion IDs in the repository's required `phase/lesson-directory` form. Use [the evidence protocol](EVIDENCE-PROTOCOL.md): attempts never satisfy a requirement; eligible focused bridges satisfy only their exact stage; full eligibility needs reviewed content/quiz/artifact and independent readiness. Legacy progress rows alone are untrusted. Store project-stage gates separately; do not pretend S0–S8 are existing curriculum lessons.
5. Validate any revised manifest using the resolver. If the resolver reports a real manifest error, stop and repair it; do not select a different lesson silently.
6. Resume the first unresolved gate, rather than resetting all work to S0.

The original planning run did not activate the proposal. The 14 October corrections update resolver/policy prose, evidence contracts, tutoring instructions, and specified reference qualifications/coverage while preserving active M1, 5–7-hour pace, lesson order, and empty learner progress. At that point the candidate used 10 hours/week and was still inactive; it was adopted on 14 October. No learner implementation or completion was created. The planning helpers did recreate `.venv` through `uv run`; it was resynchronized using `uv sync --frozen` from the existing lockfile and checked separately.

## Dependency and contribution policy

The source repo remains a curriculum. New lesson work must follow its one-lesson-per-commit, code/header/test, tagged-fence, quiz and validation contracts. Personal project exercises do not alter those contracts.

Use stdlib, NumPy and PyTorch for the proposed core. Named dependencies outside the allowlist are skipped here because the route **stays stdlib-first for educational clarity**. A separate learner workspace may have a different policy; inspect it before scheduling a real framework comparison. Existing broad dependency metadata is not itself permission to add banned dependencies to curriculum lessons.

External project repositories are evaluated only in the personal research annex outside the checkout. Core learning exercises and future lesson code must be original; cite official documentation, specifications, and papers for mechanisms.

## Project route and evidence routing

[from-scratch/route.json](../../from-scratch/route.json)
contains nine required S0–S8 project stages and core gates G0–G8. Additional live
generation, semantic retrieval, live tool selection, and held-out quality gates
remain independently pending while core readiness permits local work. Schema validation
rejects unsupported/empty stages, duplicate IDs, invalid booleans/modes, and invalid
evidence. Resolver states derive from reviewed checks, not supplied readiness flags.

Use the [evidence protocol commands](EVIDENCE-PROTOCOL.md#route-and-output-contract)
to probe it. Probing is read-only and never records evidence or changes the route.
Ready-to-advance, pending/failed
retention, retained, and closed remain distinct. If delayed evidence fails, repair
the observed gap rather than restarting the phase or deleting earlier work.
