---
title: AI Engineering Workbench Technical and Learning Audit
audit_date: 2026-10-19
timezone: Africa/Cairo
repository: https://github.com/AhmedTElKodsh/ai-engineering-project-lab
audited_branch: main
audited_commit: 835d97ec9137962807852859494e68bf90a4bd43
learning_revision: d47a29c5f6abb00dbf4ba2e802a69736f8fe9440c7b76aa571c90177c450b31c
review_mode: read_only
report_status: review_findings_and_recommendations
implementation_authorized: false
learner_credit_awarded: false
---

# AI Engineering Workbench Technical and Learning Audit

This is the saved review delivered in chat on 19 October 2026, with repository source links converted to commit-pinned GitHub links for portability. The later request to save the review authorizes this report file; it does not authorize implementing its recommendations or changing learning progress. This report is an audit artifact, not a replacement route, acceptance contract, tutor, or progress system.

For AI analysis: distinguish documented intention, existing implementation, verified behavior, and demonstrated learner competence. Findings apply to the audited commit above. Revalidate them against a newer candidate before implementing changes. Synthetic histories and mutations described below were read-only audit probes, not actual learner observations. Proposed completion criteria and backlog items remain recommendations.

The repository is a strong foundation for learning applied AI engineering, but I would **repair its assessment integrity before the next assessed tutoring session**. I reproduced a case where an answer supplied during practice can later count as fresh independent transfer—and even delayed retention—because the practice was recorded as `context`.

The real learning record remains accurate: all S0–S6 gates are unresolved. No learner achievement was invented or changed during this audit.

🔧 **Principal AI Engineer:** “The technical direction is sound. The danger is spending the available hours rebuilding frameworks instead of learning to diagnose systems.”

🎓 **Technical Educator:** “And a technically sound route still needs reliable assessment. The learner must be able to do something unfamiliar after the scaffolding disappears.”

🔍 **Adversarial Auditor:** “That is where the first repair belongs. The ledger must remember that an answer has already been taught, however the practice was recorded.”

# Part I — Executive assessment

## Verdict and four independent judgments

| System being judged | Assessment | Confidence |
|---|---|---|
| **Technical curriculum coverage** | **4/5 — Strong design.** Good depth in RAG, tool authorization, evaluation and observability. Scope and workload need tighter control. | High for documented coverage; medium for feasibility |
| **Software/repository implementation quality** | **3/5 — A credible maintenance foundation with important gaps.** Reproducibility and state safeguards are substantial, but the novelty defect and incomplete contract hashing weaken progress integrity. | High |
| **Pedagogical and assessment design** | **3/5 — Thoughtful instruction, insufficiently operationalized assessment.** Learner ownership, gradual help and delayed checks are well designed. Capability coverage, review scheduling and tutor behavior still depend heavily on judgment. | High for instructions; medium for likely outcomes |
| **Observed instructional effectiveness** | **N/A — Not established.** There is no current learner evidence demonstrating acquisition, independent transfer or retention under this route. | High confidence in this limitation |

These are separate judgments. They are not averaged into an overall score.

**Outcome A—engineering competence:** The route could develop a capable junior engineer specializing in LLM applications, RAG and agents. The repository does not yet demonstrate that outcome.

**Outcome B—learning effectiveness:** The instructional design is promising and unusually explicit about assistance and ownership. Its effectiveness for this learner remains unmeasured.

## What the repository does particularly well

The strongest feature is its distinction between an artifact and a capability. The route requires execution, explanation, independent transfer and delayed retention. It also distinguishes maintainer work, inherited code, fake-provider tests and live behavior. Those distinctions appear consistently across the [mastery policy][mastery], [evidence protocol][protocol] and [mentor skill][mentor].

Other strengths are:

- One cumulative application gives the work a coherent purpose.
- Python is taught inside useful application work.
- Direct libraries precede orchestration frameworks.
- RAG includes access control, versions, conflicts and abstention.
- Agent actions are governed by deterministic application controls.
- The optional training track has a clear authorship boundary and realistic small-model configurations.
- Known baseline failures remain visible as strict expected failures.
- Research is presented with limits rather than as proof that this exact curriculum is optimal.

## The most consequential weaknesses

1. **Previously supplied practice can escape novelty tracking.**
2. **The HR evaluation split contradicts its own held-out policy.**
3. **Requirements in linked documents and evaluation gates do not participate in stage contract hashes.**
4. **Broad stage-level proof can hide uneven capability within a stage.**
5. **Framework comparisons and private-project integration make the schedule optimistic.**
6. **The route prepares application builders more directly than engineers who can deliver and operate a service.**
7. **Tutor behavior has not been validated through controlled runs or learner outcomes.**

## Actual repository state and verification

Audit date: **19 October 2026**, Africa/Cairo.

| Item | Verified state |
|---|---|
| Repository | `AhmedTElKodsh/ai-engineering-project-lab` |
| Branch | `main` |
| Commit | `835d97ec9137962807852859494e68bf90a4bd43` |
| Remote comparison | Connected GitHub inspection confirmed the same `main` SHA |
| Local tree | Clean before and after the audit |
| Runtime | Python **3.12.14** |
| Locked tools | Pydantic **2.13.4**, pytest **9.1.1**, Ruff **0.16.1** |
| Learning revision | `d47a29c5f6abb00dbf4ba2e802a69736f8fe9440c7b76aa571c90177c450b31c` |
| Learner evidence | One maintainer migration/context event; no completed learner records |
| Active stage | S0 |

I executed the existing local clone, whose commit matched GitHub. No additional clone was necessary.

| Check | Actual result |
|---|---|
| `uv sync --locked --all-groups` | Passed |
| Learning-state status and final validation | Passed |
| Mentor/package contract checker | Passed; explicitly structural |
| Ruff lint | Passed |
| Ruff format check | Passed; 107 files already formatted |
| Default pytest suite | **81 passed, 5 xfailed**; no skips reported |
| HR corpus validator | Passed: **21 documents, 125 golden questions** |
| Answered and abstained baseline CLI examples | Both executed successfully |
| Optional vector-search starter tests | **10 failed, 1 passed**, consistent with unimplemented TODOs |
| Hosted CI for the inspected SHA | [Successful run](https://github.com/AhmedTElKodsh/ai-engineering-project-lab/actions/runs/38743083290) |

The five expected failures concern paraphrase retrieval, unsupported overlap, an unsupported medical question, multi-intent coverage and instruction-like phrasing. They are measured limitations, not successful assistant behavior.

The inspection covered the root contracts; learning-path documents 00–08; mentor instructions and launcher; route, protocol and evidence writer; both maintenance test files; baseline application and tests; dependency and CI configuration; HR metadata, evaluation schemas, splits, validator, generation scripts, tool contract and all 20 agent scenarios; representative optional scaffolds; and relevant historical review/recheck records. The 125 reference answers were checked structurally through the validator, not individually adjudicated for every fact.

The private Mushir implementation, client authorization, actual transfer work, live-provider quality and deployed behavior were outside this inspection. Statements about them remain repository claims.

The five party voices are review perspectives used in this audit, not a blinded experiment involving five independent reviewers.

# Part II — Technical audit scorecard

“Implementation” below describes what exists now. A zero for a future application component means it is unimplemented; that alone is not a defect in a learner-owned starter.

| Dimension | Design / current implementation | Evidence and rationale | Confidence | Highest-impact improvement |
|---|---:|---|---|---|
| Python and software foundations | **4 / 2** | S1 covers records, Unicode, validation, errors, tests, HTTP and async. The current app demonstrates only part of this floor. [S1 contract][s1] | High | Make diagnostic findings and capability-specific exits explicit. |
| LLM application engineering | **4 / 0** | SDK boundary, structured output, retries, tracing, budgets and fakes are specified. No provider implementation exists. [S2 contract][s2] | High | Expand the live-call exit beyond one successful response. |
| RAG engineering | **4 / 0** | The planned lifecycle is broad and useful. Current token-overlap retrieval is not the planned embedding RAG system. [S3][s3], [S4][s4] | High | Repair evaluation partitions and define separate retrieval/support/citation scores. |
| Agents and tool authority | **4 / 0** | Identity, confirmation, idempotency and deterministic authorization are strong contracts. No agent runtime exists. [S5][s5], [tool contract][tools] | High | Align approval semantics and add operational failure scenarios before implementation. |
| Evaluation and experimentation | **3 / 2** | Rich fixtures and visible baseline failures; compromised holdout separation, weak answer assertions and ambiguous statistical acceptance. [gates][gates], [baseline tests][apptests] | High | Establish disjoint development/release sets and appropriate decision rules. |
| Security and reliability | **4 / 1** | Good trust-boundary principles, secret policy and simulated-action scope. Most application protections remain future work. [project contract][appcontract] | High for design | Introduce minimum access/version filtering with the first HR RAG release. |
| Delivery and operations | **2 / 1** | Repository CI is real; API delivery, containers, runtime health, rollback and operational diagnosis are deferred. [CI][ci], [later branches][later] | High | Add a small delivery exercise before claiming broad job readiness. |
| Optional model-training track | **4 / 0** | Coherent numerical, architectural and lifecycle contracts. No learner model is supplied. [T1–T5 specification][scratch] | High for design; low for measured compute | Pilot C0/C1 before estimating training duration. |

## Technical findings by area

**Python.** The proposed floor is appropriate for basic Python knowledge. Dataclasses followed by Pydantic can teach the difference between internal representation and validation at an external boundary. Errors, logging, tests and HTTP appear early enough. Deferring metaclasses and elaborate packaging is sensible.

Git is present mainly as revision identification and reference material. It needs an observable task involving a small branch, a reviewed diff and a regression fix. Database fundamentals are much less explicit. A small persistence exercise belongs near agent checkpointing and idempotency rather than in an unrelated preliminary course.

Property-based testing is not required everywhere. It would be useful selectively for date boundaries, numeric matching, serialization and idempotency invariants.

**LLM applications.** S2 goes beyond an API demonstration: it asks about untrusted output, schema guarantees, model identity, retries and cost. However, one successful live call does not establish reliable provider integration. The stage should also require a recorded decision about transient versus permanent failures, a total time/token budget and a small fixed-case comparison.

Model selection and fallback policy are underdefined. The learner should compare a small number of candidates against declared quality/cost criteria and explain when failing closed is preferable to falling back.

**RAG.** Coverage is strong. The corpus makes parsing, access control, versions, conflicts, multilingual retrieval and tool routing concrete. Section-based relevance labels help chunking comparisons remain meaningful.

Three distinctions need stronger acceptance rules:

- Finding a relevant passage does not establish support for every answer claim.
- A citation can identify a real source while the answer adds unsupported content.
- Hit@k can succeed while a multi-source question remains incompletely supported.

The first HR RAG release should preserve access and version eligibility before ranking. S4 can deepen those mechanisms; it should not introduce their basic boundary after restricted documents are already used.

**Agents.** The fixed-workflow comparison is valuable. It creates a reason to reject unnecessary agent complexity.

The tool contract correctly separates preparing a draft, user confirmation and manager approval. The project README’s broader “independent approver” language should distinguish those three authorities. A user confirming submission does not mean the leave itself has been approved.

LangGraph persistence also needs replay-aware implementation. Its official documentation states that resuming an interrupt restarts the interrupted node, so code before the interrupt can run again. An interrupt therefore supplies a pause mechanism, not an authorization system or exactly-once guarantee. [Official LangGraph interrupt documentation](https://docs.langchain.com/oss/python/langgraph/interrupts)

**Evaluation.** The route appropriately includes negative controls, judge calibration and paired comparisons. The decision language needs correction. McNemar’s test applies to paired categorical outcomes; failure to detect a difference does not prove equivalence. Continuous scores such as MRR need a suitable paired analysis and practical-effect interpretation. [Official statsmodels documentation](https://www.statsmodels.org/stable/generated/statsmodels.stats.contingency_tables.mcnemar.html)

**Operations.** Full Kubernetes, distributed serving and a large cloud stack can remain deferred. A minimal service boundary, persisted state, health check, failure drill and reproducible deployment are much closer to foundational delivery skills.

# Part III — Pedagogical audit scorecard

| Dimension | Score | Rationale and evidence | Confidence | Highest-impact improvement |
|---|---:|---|---|---|
| Purpose and sequencing | **4** | A clear grounded-assistant mission and cumulative progression. [Roadmap][roadmap] | High | Bound the early private-code trace to a manageable path. |
| Active learning and scaffolding | **4** | Predict/run/investigate/build/transfer is explicit; hints escalate and full solutions require a clear request. [Method][method] | High for design | Verify actual help escalation through tutor pilots. |
| Assessment validity | **2** | Strong ownership principles, but a reproduced novelty bypass and broad stage-level assertions undermine enforcement. [Novelty check][novelty] | High | Repair context exposure and require capability coverage in proof artifacts. |
| Retention | **3** | Delayed fresh checks are required, but the proposed review queue is not operationalized in derived state. [Review policy][retention] | High | Derive a small due-review view from the existing evidence system. |
| Transfer | **3** | Fresh tasks and Mushir application are required. One familiar domain and one broad task may still overstate generality. [Mastery][mastery] | Medium | Include an unfamiliar dataset or failure context at selected exits. |
| Mentor instruction quality | **4** | Good handling of vocabulary, confusion, ownership, assistance and resumption. [Mentor][mentor] | High for instructions | Pilot ambiguous and frustrating interactions. |
| Feedback and sustainability | **3** | Adaptive pacing is specified, but later stages have substantial switching and integration costs. [First four weeks][weeks] | Medium | Measure active work, setup, hint use and independent success. |
| Learning-science alignment | **4** | Relevant principles are used with explicit limits on generalization. [Method][method] | High | Evaluate this learner’s outcomes rather than treating the research as certification. |
| Observed teaching effectiveness | **N/A** | No current learner acquisition/transfer/retention series exists. | High | Collect the first four weeks of actual evidence. |

## Research support and its limits

The research rationale is broadly defensible.

- Retrieval practice has experimental support for delayed retention. The original Roediger–Karpicke work supports requiring learners to produce an answer rather than merely reread one. It does not establish that a short programming check measures engineering competence. [Original study](https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01693.x/)
- Spacing research supports revisiting material over time, while showing that useful spacing depends on the intended retention interval. A 24-hour minimum is a scheduling safeguard, not a universal mastery threshold. [Cepeda and colleagues](https://www.yorku.ca/ncepeda/publications/CVRWP2008.html)
- PRIMM was evaluated with 493 students aged 11–14 across 13 schools. Its findings support the chosen programming progression, with substantial uncertainty when applied to an adult studying AI engineering with an AI tutor. [Author’s institutional record](https://eprints.gla.ac.uk/229013/)
- Bastani and colleagues found that assistance could improve practice performance while harming later unaided performance, and that instructional safeguards mitigated that harm in their high-school mathematics setting. This supports separating assisted performance from independent assessment; it does not supply an expected effect size for Ahmed. [Published study](https://www.pnas.org/doi/10.1073/pnas.2422633122)

The exact two-hour schedule, framework sequence and five-to-seven-month forecast are instructional design judgments. They remain unverified assumptions for this learner.

## Six controlled policy walkthroughs

These are **hypothetical transcript-based inspections**, not observed mentor executions. The repository supplies instructions and a launcher, not a controlled behavioral evaluation runner. I did not make provider calls to manufacture tutoring results.

| Case | Appropriate mentor response and question | Feedback/help behavior | Advancement decision |
|---|---|---|---|
| Beginner meets an unfamiliar mechanism | “A timeout limits how long we wait for a response. In this unrelated example, what should the caller do if no reply arrives?” | Teach the term, show one concrete trace, then request one prediction. | No mastery from first exposure. |
| Concept understood, Python mistake | “Your description of the data flow is correct. The traceback points to using the record as though it were a dictionary. What type reaches this line?” | Preserve conceptual evidence; diagnose the language error separately. | Repair and fresh execution evidence are needed; do not erase valid explanation. |
| Still stuck after useful hints | “You have isolated the conversion step. Here is the smallest fragment for converting this unrelated value. Adapt that step and explain the change.” | Supply only the blocker after the learner’s attempt and explicit request. Record assistance. | Supported practice; later fresh independent assessment. |
| Requests the complete solution | “I can show the complete worked solution. We will record it as supplied assistance, then assess a different problem later.” | Give the requested solution and explain it. | No ownership/mastery credit from the supplied solution. |
| Confident but technically wrong | “A citation proves where text came from. It does not prove that your added claim follows from it. Which words in the passage support that claim?” | Use a concrete counterexample and correct the mechanism. | Keep the affected capability unresolved. |
| Returning learner has forgotten | “This was previously demonstrated. Let’s reconstruct one small trace, then revisit a different case after the repair.” | Treat forgetting as diagnostic information; restore scaffolding. | Preserve history, record the current support need and reassess the affected capability. |

The instructions support these responses well. Whether the tutor actually selects them, grades them accurately and resists serial answer leakage still requires behavioral verification.

# Part IV — Stage-by-stage review

The clearer criteria below are recommendations. They are not changes to the current route.

## S0 — Frame the quest and trace one answer

**Objective and skills:** Understand the user, the cost of unsupported answers, basic request flow, configuration boundaries and function inputs/outputs. **Current allocation: 4–6 hours.**

The purpose is strong. The prerequisite—basic syntax—may be insufficient for tracing a large private application from HTTP entry through generation and citation validation without carefully selected excerpts. [S0 contract][s0]

The initial assessment is useful if it asks the learner to trace values, predict behavior and identify a gap. Naming components alone is weak evidence.

**Recommended adjustment:** Keep one bounded answer path, teach each unfamiliar boundary before assessing it, and isolate configuration repair from architecture orientation.

**Measurable completion:** The learner can identify a supported claim and source, explain an abstention, trace one selected request with concrete inputs/outputs, explain a short function’s side effects and correctly distinguish `.env`, process environment, SDK and model ID. A separate fresh trace establishes transfer.

## S1 — Python floor for AI applications

**Objective and skills:** Build typed records, reliable file handling, validation, configuration, useful errors, tests, logging and basic HTTP/async literacy. **Allocation: 20–30 hours.**

The sequence is appropriate. The diagnostic tasks are well chosen and avoid assigning an unsupported “level.” The amount fits only if gaps are localized; a learner needing substantial repair in functions, mutation and data structures will need more time. [S1][s1], [diagnostic][diagnostic]

The “at least five tests” rule is a floor, not sufficient coverage. A learner could write five weak tests.

**Recommended adjustment:** Require a small contract coverage checklist rather than relying on the count. Include one branch/diff/review task.

**Measurable completion:** Normal, empty, missing-file, Unicode and malformed-boundary behavior is tested; a meaningful mutation fails; a secret does not appear in logs; an HTTP failure terminates within its budget; the learner independently repairs a new bug and explains its cause.

## S2 — LLM calls, structured output and tracing

**Objective and skills:** Integrate a provider safely, validate outputs and understand tokens, budgets and traces. **Allocation: 20–30 hours.**

Direct SDK use before LangChain is a good choice. Carrying forward the S1 configuration and HTTP mechanisms reinforces prior learning. The principal weakness is an exit gate centered on one live success. [S2][s2]

**Recommended adjustment:** Use a small fixed development set and one bounded provider/model comparison. Make retryable failures, permanent errors and total request budget explicit. The LangChain comparison should reuse the same application contract.

**Measurable completion:** Reject malformed output and unknown citations; explain a trace and measured cost; demonstrate terminating failure paths through fakes; record a budgeted live run; independently repair a different validation or provider-boundary fault.

## S3 — RAG core with frameworks

**Objective and skills:** Parse, chunk, embed, store, retrieve, cite and evaluate across mixed formats and languages. **Allocation: 30–45 hours.**

This is the first major workload bottleneck. Mixed parsing, multilingual embeddings, Chroma, generation, metrics, two framework rebuilds and Mushir application are substantial for three to four-and-a-half weeks. [S3][s3]

The corpus is useful. Binary inspection confirmed real parsing challenges: a digital PDF with text, a two-column layout and an image-only insurance document with no extractable text. The Arabic DOCX contains Arabic text. These are fixtures to learn from; no full ingestion pipeline was verified.

**Recommended adjustment:** Build one thin end-to-end path first. Preserve access/version eligibility from the start. Compare LangChain and LlamaIndex through bounded implementations of the same narrow path, rather than duplicating every ingestion feature.

**Measurable completion:** Identify corpus/index/embedding versions; trace source sections into chunks; report retrieval metrics on development cases by slice/language; distinguish partial retrieval from complete support; abstain appropriately; diagnose a fresh failure to parsing, chunking, embedding, filtering or ranking.

## S4 — RAG depth and evaluation

**Objective and skills:** Improve hard-case retrieval and answer quality through measured changes. **Allocation: 35–50 hours.**

The technical content is excellent. The acceptance contract is not yet coherent enough: held-out overlap, optional screening gates and ambiguous “beats or ties” statistical language affect closure. [S4][s4], [gates][gates]

Sixty human labels are a meaningful calibration exercise, but kappa alone cannot establish judge validity. False acceptance of unsupported claims deserves separate inspection.

**Recommended adjustment:** Teach one hypothesis at a time: baseline, predicted effect, fixed development comparison, failures and keep/drop decision. Scope hard gates to implemented capabilities and reserve untouched cases for release evaluation.

**Measurable completion:** Evaluate retrieval relevance, claim support, citation correctness, refusal/routing and latency/cost separately; pass applicable hard gates; report paired gains/losses and uncertainty; explain an unsuccessful experiment; independently improve or correctly reject a proposed change.

## S5 — Tool-using agents with LangGraph

**Objective and skills:** Implement validated tool use, graph state, persistence, approval and a protocol boundary. **Allocation: 35–50 hours.**

The deterministic-workflow comparison and session-derived identity are strong. Twenty scenarios provide useful business cases, but do not cover the entire operational contract. [S5][s5], [agent scenarios][scenarios]

Missing scenario types include a crash after a write but before acknowledgement, replay after restart, altered approval arguments, cross-session confirmation and a stalled tool.

**Recommended adjustment:** Clarify draft creation, confirmation and manager approval; add a handful of operational cases; time-box the alternative SDK comparison. Keep MCP read-only for the first protocol exercise.

**Measurable completion:** Scenario outcomes and tool trajectories are correct; step/time budgets terminate; cancellation and restart behave as declared; approval is bound to identity and exact action; duplicates and uncertain writes reconcile safely; the learner independently fixes a fresh failed scenario.

## S6 — Agentic engineering

**Objective and skills:** Combine retrieval and tools, evaluate trajectories, manage memory and compare orchestration designs. **Allocation: 30–45 hours.**

This is a useful integration stage. Its scope is crowded: supervisor/router/handoff patterns, memory, guardrails, evaluation, traces, CrewAI comparison and a private-project change. [S6][s6]

A multi-agent result should not be required to outperform a simpler workflow. Discovering that the simpler design is preferable is valid engineering evidence.

**Recommended adjustment:** Select one measured multi-step problem, compare alternatives and permit a keep/drop decision. Define memory ownership, expiry, deletion and contamination tests.

**Measurable completion:** Deliver reproducible task and trajectory results; prove a guardrail using a failing counterexample; report orchestration overhead; justify the selected architecture; complete an independent integration change with attributable evidence.

## Optional T1–T5 track

| Phase | Assessment | Workload and clearer completion |
|---|---|---|
| **T1: Counts, probability and gradients** | Coherent foundation. Source-level splits and compatible loss units are particularly good. Classification is useful breadth but should remain bounded. | **50–70 hours.** Independent probability/gradient task, finite differences, frozen baseline and honest held-out comparison. |
| **T2: Backpropagation and small networks** | Good progression from scalar/manual proof to PyTorch. Shared-node accumulation is correctly emphasized. | **45–65 hours.** Verify shared gradients, updates, tiny-set learning and diagnosis of a new backward/update fault. |
| **T3: Tokenizer and causal transformer** | Strong architecture and authorship boundary. BPE, shapes and masking create substantial cognitive load; teach them in separate slices. | **60–85 hours.** Tokenizer integrity, future-token invariance, shape/gradient checks, parameter counts and a fresh mask/transpose repair. |
| **T4: Training and lifecycle** | Sensible CPU-first correctness profiles and throughput measurement. No claim of useful language quality is guaranteed. | **45–70 hours plus compute.** Genuine updates, overfit check, controlled resume, bounded generation and held-out evaluation. |
| **T5: Integration and adaptation** | Appropriate comparison with capable generators; tiny SFT/LoRA has explicit boundaries. Its dependency on an existing applied assistant should be clarified if the track runs alongside the core. | **20–30 hours.** Reproducible comparisons, correct frozen/trainable behavior, separate pretraining/adaptation claims and independent explanation. |

The optional track totals **220–320 focused hours**, before reserve and unattended compute. It is a substantial additional program, not a small addition to the core’s five-to-seven-month estimate.

Its CPU configurations are plausible correctness experiments. Their throughput and achievable quality remain unbenchmarked. The detailed specification is stronger than the current supporting implementation maturity. [Optional specification][scratch]

# Part V — Contradictions and failure modes

## F0 — P0: Context-recorded assistance can become “fresh” mastery

**Reproduced behavior:** A schema-valid synthetic sequence containing a generated-answer `context` event, later execution/explanation and transfer on that same taught case produced `ready=True`. A delayed-retention variant also produced `retained=True`.

**Control:** Recording the earlier exposure as generated `execution` instead correctly blocked transfer.

The novelty function inspects only execution, explanation, transfer and retention events. It excludes context. Yet the protocol directs partial results to practice/context and requires novelty against earlier practice. [Novelty implementation, lines 191–198][novelty]; [protocol, lines 13–17][protocol]

**Minimal correction:** Count case-specific practice/answer exposure recorded in context. Keep ordinary migration and general support notes neutral. Add regressions for both transfer and retention, including historical and invalidated exposure.

This is a reproduced enforcement defect, not an observed instance of learner misconduct. No synthetic event was appended.

## F1 — P1: The held-out set is also used for development

Eight of the 25 held-out IDs also appear in the 40-question smoke set:

`q10`, `q30`, `q45`, `q65`, `q80`, `q85`, `q95`, `q120`.

The smoke set is prescribed for every pull request; the holdout rule says never inspect those questions while tuning. In addition, the S3-required slices contain 12 held-out questions unless explicitly excluded. [Gate definitions][gates]; [S3 evaluation instruction][s3]

The validator checks ID existence but not split disjointness. It reported success. [Validator, lines 148–152][hrvalidator]

**Minimal correction:** Define development IDs explicitly, preserve recurring security regressions in development, and create a disjoint release set. Record exposure and renew release cases after they become debugging material.

## F2 — P1: Contract hashes omit linked acceptance requirements

Hashes include the stage’s roadmap section, selected route facts and any declared `additional_contracts`. The active route declares no additional contracts.

Consequently, changes to the library map, mastery rules or imported release gates can change required acceptance without changing the affected stage hash. A mocked library-map change left all stage hashes unchanged. [Hash construction][hashing]; [route][route]

**Minimal correction:** Declare the relevant acceptance dependencies per stage. Prefer scoped content over hashing every documentation file.

## F3 — P1: Optional screening becomes a mandatory S4 gate

S4 requires every hard gate in `gates.json`. That file includes résumé-screening and counterfactual gates. S6 describes screening as optional. [S4 exit][s4]; [screening hard gates][gates]; [S6 optional slice][s6]

**Minimal correction:** Give gates an applicable capability/stage and optionality. An unimplemented optional screener must not block RAG completion.

## F4 — P1: Statistical acceptance can teach a false “tie”

The roadmap asks each change to beat or tie the baseline with a stated test. The imported rule allows changes unless a statistically significant loss is detected. Neither establishes equivalence.

**Minimal correction:** Predeclare practical tolerances, report paired gains/losses and distinguish “no detected difference,” “inconclusive” and “evidence of improvement.” Use McNemar for binary outcomes rather than as a universal metric comparison.

## F5 — P2: “Whole-number” matching accepts a decimal prefix

I executed:

```text
matches("2.5 days", "2") → True
matches("12 days", "2")  → False
```

The documented rule says numeric items match as whole numbers, but the trailing boundary permits a decimal point. [Matching implementation, lines 62–70][matching]

**Minimal correction:** Define numeric token boundaries and units explicitly, then test decimals, percentages, signs and localized formatting. This matters for both false passes and false rejections. The helper remains only a pre-check.

## F6 — P2: Optional-resource labels point to the retired route

The vector-search scaffold says S2/S4; transformer, attention and tokenizer scaffolds say S6; context/decoding mentions S7. The active resource policy places plain-Python mechanisms on the optional track, and S7 no longer exists. Several source comments point to absent `hints.md` files. [Resource policy][resources]; [example stale mapping][labmap]

**Minimal correction:** Replace stale mappings with current optional-phase references or explicit focused-use descriptions. Remove nonexistent hint pointers.

The historical consolidation report itself is dated and includes a later revision notice. Its preserved S0–S8 discussion is not, by itself, a competing active route. [Consolidation revision notice][history]

## Adversarial scenario results

| Scenario | Existing protection | Audit result and remaining failure mode |
|---|---|---|
| Copied generated code grants completion | Generated/worked execution and explanation are excluded; independent transfer required | Protection exists, but F0 bypasses exposure tracking when practice is context. |
| Green tests accept significant answer defect | Challenge xfails and mutation policy | All **19 ordinary fixed-evaluation assertions** passed when an unsupported sentence was appended in memory. This probe covered that subset, not a full mutated-suite run. |
| Remembered answer counts as fresh transfer | Historical case-ID checks | Recognized for proof events; bypassed by context exposure. Renaming a copied case remains a disclosed human-review boundary. |
| Hints reveal the assessment algorithm | Explicit prohibition on serial solution leakage | Good policy; actual tutor compliance unverified. |
| Bare assertions grant stage credit | Artifact hashes, actor, assistance, tree and ordering checks | Synthetic proofs backed only by the README can satisfy the structural helper. The protocol explicitly discloses that it cannot judge truth; this is a review boundary, not a newly discovered authentication defect. |
| Changed requirements leave stale credit | Scoped contract hashes | Roadmap-section changes are covered; linked acceptance changes are not. |
| Tutor teaches an incorrect API | Current official documentation required | Good instruction; no behavioral evidence that it is followed reliably. |
| Retrieved source gives malicious instructions | Treat retrieval as data; injection fixtures | No implemented RAG/agent runtime to test. Future protection is specified, not verified. |
| Agent acts without valid authorization | Session identity, UI confirmation, deterministic checks | Strong contract; no implementation proof. |
| Real citation accompanies unsupported claim | Citation schema and origin tracking | The fixed-case mutation demonstrates that current answer assertions do not reject this class. |
| Framework demo hides weak concepts | Explain, predict, transfer and compare requirements | Sound design; stage-wide proof artifacts need explicit capability coverage. |

# Part VI — Missing competencies and career readiness

Two primary employer postings inspected during the audit support the route’s emphasis on Python, APIs, evaluation and agents. They also expose delivery gaps:

- Menhir’s junior role includes data quality, evaluation, deployment support, observability, Git and REST APIs; LangChain/LangGraph are desirable familiarity. [Employer posting](https://join.com/companies/menhir/16832129-junior-ai-engineer)
- OTP Bank’s junior role, dated 13 October 2026, includes Python, practical SQL, maintainable APIs, Git/Linux, experimentation and supported use of Docker/CI/monitoring. It asks for at least one RAG or agent framework, not mastery of every framework. [Employer posting](https://karrier.otpbank.hu/otp/job/Budapest-Junior-AI-Engineer-1131/1446477233/)

These are illustrative roles in different markets, not a representative hiring survey or a prediction of eligibility.

| Capability gap or weak point | Classification | Appropriate placement and opportunity cost |
|---|---|---|
| Reliable evaluation partitioning and claim-level support checks | **Core-required** | Repair before S3; teach inside the existing harness work. |
| Provider failure classification and total budgets | **Core-required** | S2; a small extension of existing HTTP work. |
| Basic access/version filtering | **Core-required** | First HR RAG path in S3; deepen in S4. |
| Durable persistence and transaction/idempotency reasoning | **Core-required** | S5 checkpoint/write workflow; avoid a separate database course. |
| Git branch, diff and review practice | **Core-required** | S1 onward; use actual small changes. |
| API delivery, health checks, container and failure drill | **Recommended later; necessary before a broad job-ready claim** | Small post-core delivery branch. Full cloud operations can remain deferred. |
| SQL and relational data literacy | **Recommended later**, or earlier for target roles requiring it | Use persisted requests/evaluation results; approximately 4–6 focused introductory hours. |
| Architecture explanation and code-review communication | **Core-required** | Short defenses within each stage’s review allocation. |
| Small classical-ML comparison literacy | **Recommended later** | Add if target roles mix ML and LLM work; no need to mandate the full scratch track. |
| OCR/table extraction depth | **Optional specialization** beyond detecting and handling the declared failure | Deepen when a selected use case needs it. |
| Fine-tuning/model adaptation | **Optional specialization** | Keep the later branch and compare against prompting/RAG. |
| Vision, speech and broad multimodal systems | **Optional specialization** | No justification for mandatory expansion now. |
| Kubernetes, distributed training, large-scale serving | **Unnecessary for the current declared core goal** | Revisit only for a specific role or measured system need. |

The library map’s exact job-market percentages remain secondary-source claims, not independently reproduced statistics. Its warning about source limitations is appropriate. One product-status claim checked against Microsoft’s primary announcement was supported: Agent Framework 1.0 was announced in April 2026 as the convergence of Semantic Kernel and AutoGen foundations. [Microsoft announcement](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/)

Framework familiarity helps employability. Independent implementation, debugging, evaluation and delivery provide stronger evidence of competence.

# Part VII — Prioritized improvement backlog

All effort figures below are planning estimates. **Platform work belongs to maintainers; application implementations and independent challenges belong to the learner.**

| ID | Priority | Improvement | Owner | Engineering effort | Learner time | Dependency / acceptance |
|---|---|---|---|---:|---:|---|
| B0 | **P0** | Preserve context-recorded case exposure | Maintainer | 2–4 h | None | Before assessed tutoring; taught cases cannot earn fresh transfer/retention. |
| B1 | **P1** | Repair corpus split and gate applicability | Maintainer | 4–7 h | 0.5–1 h orientation | Before S3; disjoint development/release IDs and optional gates scoped correctly. |
| B2 | **P1** | Hash linked acceptance dependencies | Maintainer | 2–4 h | None | Before new mastery credit; relevant contract changes reopen affected credit. |
| B3 | **P1** | Operationalize capability coverage and resumption | Maintainer + mentor | 4–8 h | Within existing recording/review time | Before closing S1; proof artifacts map requirements to evidence and expose the next checkpoint. |
| B4 | **P1** | Bound framework comparisons and recalibrate pace | Curriculum maintainer | 2–3 h | Intended to save time | Before S3; fixed comparison question, inputs, budget and keep/drop decision. |
| B5 | **P1** | Correct evaluation decision rules | Maintainer; learner implements harness | 2–4 h design | 2–4 h within S4 | Before S4; correct metric-specific analysis and fabricated-claim negative control. |
| B6 | **P2** | Pilot tutor behavior and learning outcomes | Maintainer + learner | 3–5 h preparation | Embedded in four weeks | Actual traces demonstrate ownership, useful help and calibrated advancement. |
| B7 | **P2** | Add operational agent cases | Maintainer authors cases; learner implements | 2–3 h | 3–5 h within S5 | Before S5 closure; restart/replay/uncertain-write controls verified. |
| B8 | **P2** | Fix numeric helper and stale resource pointers | Maintainer | 1–2 h | None | Before dependent exercises; meaningful boundary regressions and current mappings. |
| B9 | **P2** | Add a compact delivery/readiness branch | Learner, with mentor preparation | 2–4 h preparation | 16–26 h after core | Before broad job-ready claim; reproducible service, persistence, logs and recovery demonstration. |

## B0 — Assessment exposure

**Problem/importance:** F0 allows a previously supplied answer to count as fresh mastery.

**Change/components:** Update exposure handling in `learning_state.py`, protocol examples and state regressions.

**Verification:** Context-based taught-case transfer and retention fail; truly fresh cases pass; invalidated and older-contract exposure remains remembered.

**Preserve:** Append-only history, neutral migration context, scoped corrections and unaffected evidence.

## B1 — Corpus integration

**Problem/importance:** F1 contaminates evaluation; F3 adds an unintended mandatory screening project.

**Change/components:** Update HR gates, evaluation README, validator and S3/S4 instructions.

**Verification:** Reject overlap and unknown IDs; assert gate applicability; exclude release IDs from routine development runners.

**Preserve:** Existing failures as development regressions, bilingual slices, security checks and optional screening material.

## B2 — Contract dependencies

**Problem/importance:** F2 permits stale credit after linked acceptance changes.

**Change/components:** Declare scoped `additional_contracts` or equivalent acceptance inputs in the existing route/hash mechanism.

**Verification:** A relevant gate or mastery-contract change reopens the affected stage; unrelated editorial changes do not invalidate everything.

**Preserve:** Stage scoping and historical observations.

## B3 — Capability evidence and continuity

**Problem/importance:** One broad stage pass does not demonstrate M3 across every introduced mechanism. The next action is largely generic, while the review queue exists as prose.

**Change/components:** Use a compact requirement-to-evidence checklist inside the existing durable artifact format; derive the current checkpoint and due reviews through the existing writer.

**Verification:** Missing capability evidence is visible before stage closure; resumption identifies the actual unfinished task; earlier valid evidence survives remediation.

**Preserve:** One route and one mutable evidence system. Avoid a second tracker or heavy paperwork.

## B4 — Comparison budgets

**Problem/importance:** S3–S6 combine multiple rebuilds, application work and independent assessment within tight allocations.

**Change/components:** Add a maximum scope and time budget for each compare-once experiment. Compare the same narrow behavior through interchangeable adapters.

**Verification:** Every comparison ends with measured findings and a keep/defer/drop decision within its budget.

**Preserve:** The named core frameworks and the “official library first” progression.

## B5 — Evaluation decisions

**Problem/importance:** Weak support assertions and ambiguous statistical language can reward misleading improvements.

**Change/components:** Clarify S4 scoring, practical tolerances, judge calibration and negative controls.

**Verification:** An answer with a real citation plus an unsupported claim fails the relevant support check; binary and continuous metrics use suitable analyses; inconclusive results are labeled honestly.

**Preserve:** Frozen baselines, per-slice reporting and learner ownership of the harness.

## B6 — Tutor pilot

**Problem/importance:** Instructions have not established behavior or learning effectiveness.

**Change/components:** Use the six walkthrough categories as a pilot rubric, then inspect actual interactions and fresh learner outcomes.

**Verification:** Record explanation accuracy, question relevance, assistance, ownership breaches, independence and delayed performance.

**Preserve:** One meaningful learner action at a time, direct help when requested and no fabricated scores.

## B7–B9 — Targeted later work

B7 extends the existing scenario set with operational failures while preserving simulated effects and learner-written implementation. B8 repairs support material without changing learner acceptance to make TODOs green. B9 uses the declared later branch to demonstrate service delivery; it should not become a large infrastructure prerequisite for S0–S6.

# Part VIII — Proposed optimized learning experience

Keep the current stage identities, cumulative assistant, learner authorship and ten-hour routine. The most useful revision is to make each stage a series of small releases with visible evidence.

A typical week should still contain approximately six hours of implementation/debugging, two hours of guided concepts and two hours of testing, explanation and review. Environment repair should be recorded separately so it does not masquerade as conceptual difficulty.

Each small release should answer:

1. What user problem are we solving?
2. What behavior would count as success?
3. What is the simplest implementation worth testing?
4. What evidence identifies the failing layer?
5. What can the learner now do independently?

Use framework comparisons after the first working path. Preserve LangChain, LlamaIndex and LangGraph exposure, but make the comparison question narrow enough that learning remains visible.

Use private Mushir work for application transfer, with minimal public records. At selected exits, also use an unfamiliar fictional corpus or failure context. Otherwise “transfer” may become familiarity with two related codebases.

## Worked instructional-design example: retrieval success versus complete support

This example is unrelated to the active S0 assessment and supplies no solution to it.

**Purpose.** A museum assistant must answer visitor questions. A wrong answer can cause a wasted journey. The learner’s task is to understand why finding one relevant passage may still be insufficient.

**Introduce vocabulary.**

- A *relevant source* contains information needed for the question.
- A *ranked result* is the ordered list returned by search.
- *Hit@k* asks whether at least one required source appears in the first `k` results.
- *Recall@k* asks what fraction of required sources appears there.
- *Reciprocal rank* uses the position of the first relevant result.

**Worked example.**

A question requires source sections **A and B**. Search returns:

```text
Rank:     1   2   3   4
Section:  C   A   D   B
```

At `k = 3`:

| Measure | Result | Interpretation |
|---|---:|---|
| Hit@3 | 1 | At least one required section was found. |
| Recall@3 | 1/2 | Only one of the two required sections was found. |
| Reciprocal rank | 1/2 | The first relevant section was at rank two. |

The retriever has a hit, but the context may still lack half the evidence.

Now suppose A states opening hours, while the answer adds that admission is free. A valid citation to A establishes the origin of the hours; it does not support the admission claim.

**Guided practice.** Show a different ranked list and ask for one prediction before running the evaluator. The learner then uses the stage’s actual retrieval library to inspect document/section metadata. Compare section labels rather than unstable chunk IDs.

**Debugging exercise.** Supply an evaluator trace showing `hit=1` and an incomplete answer. Ask the learner to identify the layer responsible. If the missing source never reached the candidate set, changing the answer prompt is unlikely to repair that retrieval failure.

**Implementation.** The learner adds metric calculation and result reporting to their own harness, following the declared contract. The mentor reviews attempts without supplying the full implementation.

**Independent transfer.** Close the worked example. Give a fresh fictional corpus, different required sources and a changed ranking failure. Ask the learner to diagnose, implement and explain the result without AI completion. Do not reveal expected metrics beforehand.

**Delayed return.** Revisit after several days with a version-conflict or multilingual case. Require the learner to distinguish relevance, eligibility and claim support again. A failure prompts targeted repair while preserving separately valid evidence.

**Evidence.** Record the prediction, implementation revision, actual output, explanation, assistance and fresh-case provenance. A successful library call alone earns no mastery.

# Part IX — Implementation roadmap

## Immediate corrections before further assessed tutoring

Implement **B0**, verify its negative and positive controls, and preserve the real ledger unchanged. Then prepare **B2** so new competence evidence binds to its actual acceptance contract.

Estimated maintainer effort: **4–8 hours**. Learner study overhead: negligible.

S0 orientation and conceptual repair do not require completing every later platform improvement first.

## During the next four weeks

- Pilot the existing first-twenty-session plan against actual learner evidence.
- Introduce the lightweight capability checklist and next-checkpoint record.
- Measure coding, setup and repair time.
- Inspect whether hints become more useful without supplying the active algorithm.
- Schedule fresh delayed checks inside the existing review allocation.
- Prepare B1 before the learner reaches S3.

Estimated maintainer preparation: **7–13 hours**, depending on how much tooling is added. The learner remains on the **10-hour weekly schedule**; this is not an additional course.

## Before later stages

Before S3, repair split isolation, gate applicability and comparison budgets.

Before S4, define claim-support scoring, judge-calibration evidence and statistical decisions.

Before S5, align approval semantics and add the operational cases.

Before S6, agree on one integration problem, memory boundaries and a comparison that can legitimately conclude that a simpler design is preferable.

Estimated additional maintainer work: approximately **7–12 hours**. Learner work should replace overbroad rebuilds within the stages rather than simply accumulate.

## Optional long-term enhancements

Use the existing later branches for a small deployed service, SQL/persistence depth, operational recovery and role-specific ML or adaptation work. Undertake T1–T5 only by choice and with its separate time budget.

Do not add more frameworks merely to increase coverage.

## Is the calendar credible?

The arithmetic is correct: **174–256 focused hours**, with 20% reserve, gives approximately **209–307 hours**, or **21–31 weeks at ten hours/week**.

The feasibility is conditional. It assumes localized Python gaps, reliable provider access, bounded comparisons, manageable private-project changes and review tasks that fit their allocation.

Five to seven months is plausible for the core’s intended depth after scope control. It is not yet an evidence-backed completion forecast, and it excludes the full optional model track and a substantial delivery branch. Re-estimate after S0/S1, the first provider integration and the first RAG release.

# Part X — Final verdict

**1. Is this an effective way to become a capable AI Engineer through hands-on practice?**  
Yes, as a guided route toward applied LLM/RAG/agent competence. Confidence is conditional on repairing assessment integrity and observing independent learner performance.

**2. What does it already do exceptionally well?**  
It protects learner ownership, separates evidence classes, exposes baseline failures, uses one cumulative problem and treats authorization as application logic. The optional training specification is also unusually precise.

**3. What might let the learner finish without genuine competence?**  
The reproduced exposure loophole; broad stage passes with incomplete capability coverage; repeated or renamed tasks; fluent explanations of supplied code; framework rebuilds that hide weak mechanisms; and lenient interpretation of evaluation statistics.

**4. What important capabilities are missing?**  
Operationalized review scheduling, behaviorally verified tutoring, fully isolated evaluation, practical persistence/database experience, and a small delivery/recovery demonstration before a broad job-ready claim.

**5. What is unnecessarily complicated?**  
The number of rebuilds across RAG, agent SDKs and multi-agent frameworks; applying every stage to multiple surfaces without a tight boundary; and imported gates that introduce optional screening work into mandatory RAG acceptance.

**6. Is the AI mentor likely to teach effectively?**  
Its instructions are strong enough to justify a pilot. Actual explanation accuracy, help escalation, frustration handling, grading and advancement remain unverified. Six hypothetical walkthroughs cannot establish those outcomes.

**7. How should progress be measured more reliably?**  
Measure capabilities through actual execution, learner explanation, fresh independent work and delayed return. Preserve assistance and exposure history, map stage requirements to evidence, and distinguish readiness, retention and production behavior.

**8. What are the five highest-impact changes?**

1. Repair context-based exposure tracking.
2. Make development and release evaluation disjoint and scope optional gates.
3. Bind stage credit to linked acceptance requirements.
4. Make capability coverage and resumption visible through the existing evidence system.
5. Bound comparisons and recalibrate the schedule using actual independent performance.

**9. Is ten hours per week realistic?**  
For the core, plausibly—after scope control and with adaptive pacing. The current estimate is a planning range, not a measured promise. The optional training track requires a separate commitment.

**10. What distinguishes successful completion from being job-ready?**  
Completion means satisfying the declared route with retained learner evidence. Job readiness additionally requires handling unfamiliar code and failures, communicating design decisions, delivering a reproducible service, reasoning about persistent state and recovery, and defending quality/cost/security trade-offs. Emerging mid-level readiness also requires sustained ownership and collaboration under real operating constraints.

The first required correction is **B0**. The real learner state remains at S0, with no competence awarded by this audit.

## Binary-fixture verification sources

I visually inspected the [two-column privacy document][privacy-pdf] and [image-only insurance table][insurance-pdf]; text extraction confirmed that the latter has no text layer.

## Finding index for downstream analysis

| Finding | Severity | Evidence classification | Related backlog |
|---|---|---|---|
| F0: Context-recorded answer exposure bypasses novelty | P0 | Reproduced in memory with schema-valid synthetic histories and a control | B0 |
| F1: Development/smoke and held-out overlap | P1 | Executed set comparison; passing validator lacks disjointness check | B1 |
| F2: Linked acceptance requirements omitted from stage hashes | P1 | Static dependency inspection and mocked read-only hash comparison | B2 |
| F3: Optional screening required by S4 imported hard gates | P1 | Cross-document contract contradiction | B1 |
| F4: Statistical acceptance can imply an unsupported tie | P1 | Contract interpretation, checked against statistical API semantics | B5 |
| F5: Whole-number pre-check accepts a decimal prefix | P2 | Executed helper behavior | B8 |
| F6: Optional scaffold mappings/hint pointers are stale | P2 | Static path and text inspection | B8 |

Other backlog items are improvements or verification needs. Their presence does not mean an exploit, learner failure, or production incident was observed.

[roadmap]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L5
[s0]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L19
[s1]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L33
[s2]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L53
[s3]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L75
[s4]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L98
[s5]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L118
[s6]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L141
[later]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/02-PROJECT-ROADMAP.md#L159
[mastery]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/03-SKILLS-AND-MASTERY.md#L65
[diagnostic]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/03-SKILLS-AND-MASTERY.md#L5
[protocol]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/learning/PROTOCOL.md#L5
[mentor]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/.agents/skills/project-mentor/SKILL.md#L27
[method]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/01-LEARNING-METHOD.md#L17
[retention]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/01-LEARNING-METHOD.md#L84
[weeks]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/04-FIRST-FOUR-WEEKS.md#L11
[scratch]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/learning-path/05-LLM-BUILD-SPEC.md#L11
[tools]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/corpora/hr-policy/docs/agent_tools.md#L5
[scenarios]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/corpora/hr-policy/eval/agent_scenarios.jsonl#L1
[gates]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/corpora/hr-policy/eval/gates.json#L6
[apptests]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/projects/grounded_support_assistant/test_app.py#L29
[appcontract]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/projects/grounded_support_assistant/README.md#L26
[ci]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/.github/workflows/checks.yml#L10
[novelty]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/scripts/learning_state.py#L191
[hashing]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/scripts/learning_state.py#L54
[route]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/learning/route.json#L11
[hrvalidator]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/corpora/hr-policy/scripts/validate_data.py#L148
[matching]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/corpora/hr-policy/scripts/validate_data.py#L62
[resources]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/README.md#L5
[labmap]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/labs/vector-search/README.md#L3
[history]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/docs/review/CONSOLIDATION.md#L68
[privacy-pdf]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/corpora/hr-policy/data/corpus/employee_privacy_notice.pdf
[insurance-pdf]: https://github.com/AhmedTElKodsh/ai-engineering-project-lab/blob/835d97ec9137962807852859494e68bf90a4bd43/resources/corpora/hr-policy/data/corpus/health_insurance_schedule_2026.pdf
