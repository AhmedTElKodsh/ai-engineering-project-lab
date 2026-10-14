# Party discussion: the choices behind the plan

Revised 14 October 2026 to implement the [independent audit](../review/from-scratch-audits/python-to-llm-audit-2026-10-12.md). The audit remains the historical reviewed snapshot; this package and the project route were corrected without learner completion awards.

11 October 2026. A planning snapshot for Ahmed. Voices: Nadia, senior AI engineer; Amelia, Python programmer; Paige, software engineering tutor. Ahmed's later clarification is incorporated: 10 hours/week, CPU first, and cumulative RAG/agent coverage.

## Start with AI or with Python?

🧠 **Nadia:** “Start with an AI-related problem. If the first month has no visible connection to the goal, we have built a prerequisite waiting room. Search your documents, show the passage, then add generation.”

💻 **Amelia:** “Search still has to run. I want to see the word counter, file reader, and ranking rule Ahmed wrote. 'Basic Python' tells me little about mutation, modules, or failure handling.”

📚 **Paige:** “You are both trying to make the first task too large. Three tiny documents. One function. A prediction before execution. We diagnose through work, but we teach an unfamiliar mechanism before testing it.”

🧠 **Nadia:** “Fine, but don't let the diagnostic become a four-week exam.”

💻 **Amelia:** “Two sessions, with targeted repair afterward. No claim that he has mastered intermediate Python because one script printed a result.”

## One project or several?

📚 **Paige:** “One accumulating project keeps the context familiar. Ahmed should not learn a new business domain for every algorithm.”

🧠 **Nadia:** “One application can hide the core goal. A RAG system can become excellent without its author ever implementing a training objective. The model needs its own laboratory.”

💻 **Amelia:** “Two projects, then. Shared contracts and evidence habits. Shared code only when we actually have two consumers. I am not building a plugin framework for two toy scripts.”

📚 **Paige:** “And no independent mini-project collection. A scalar-gradient exercise is a small unit inside the laboratory. It still needs a new task afterward so we can observe transfer.”

## Ahmed asks for RAG and agents as well

🧠 **Nadia:** “Then the route needs an applied release before the long model build. Prompting, structured output, retrieval, grounding, tool calls, state, evaluation. Those skills recur across practical projects.”

💻 **Amelia:** “A workflow first. Three tools, validated arguments, explicit limits. An agent loop earns its place through a comparison. It doesn't get a pass because 'agent' sounds more advanced.”

📚 **Paige:** “The reasoning matters too. Ahmed should distinguish information supplied in context, persistent state, and knowledge learned in weights. That distinction connects the assistant to the model lab.”

🧠 **Nadia:** “That is the connection worth keeping. And the tiny trained model may still fail the assistant's answer requirements. We measure that instead of forcing a ceremonial integration.”

## What counts as from scratch?

💻 **Amelia:** “Random weights and learner-written architecture. Not loading a GPT class and changing the training data.”

📚 **Paige:** “And not spending six months writing a complete tensor engine before seeing language generation. First derive gradients, implement scalar autodiff and a small network, then use the tensor library deliberately.”

🧠 **Nadia:** “I want attention, masking, positions, loss, checkpointing, and generation visible. PyTorch autograd is acceptable after the earlier proof. But call the final result a small language model and report its actual capability.”

💻 **Amelia:** “I will keep a full manual transformer backward pass as additional scope. The default estimate cannot quietly include it.”

## How fast, and on this hardware?

📚 **Paige:** “Ten hours per week is a routine, not a deadline guarantee. The Friday transfer task decides what comes next.”

🧠 **Nadia:** “CPU is enough to build and test the mechanisms at small scale. Longer quality experiments need measured throughput. Start tiny.”

💻 **Amelia:** “No GPU installation detour in week one. Measure a model step before offering a training-time promise. Check the 1050 Ti's current support only when acceleration would help.”

📚 **Paige:** “If the model call is unavailable, do local work and label the evidence. We can continue learning without calling a fixture a real RAG success.”

## Where the recommendation remains conditional

🧠 **Nadia:** “A document assistant is my proposed theme because it brings the requested skills together. Ahmed has not chosen a corpus, provider, or final model task. Those choices should follow the first useful release.”

💻 **Amelia:** “And we inspect the existing learner project. A historical commit is not present mastery, but it is not a reason to start over either.”

📚 **Paige:** “The research gives us useful design principles, not proof that this exact sequence is uniquely best for Ahmed. After four weeks, look at actual retention, independence, and motivation.”

## Decision record

| Choice | Reason | What could change it |
|---|---|---|
| Two connected cumulative projects | Preserve applied breadth and mandatory model internals. | A chosen domain demonstrates an equally clear combined route. |
| Python assessment inside a text task | Find real gaps while keeping a purpose. | Diagnostic shows a need for a short separate foundations bridge. |
| Early RAG and bounded agents | Reflect Ahmed's explicit coverage requirement. | External model access is unavailable; local lab work moves forward while live gates remain pending. |
| Manual small-network proof, then PyTorch tensors/autograd | Make gradients understood and keep full-model training manageable. | Ahmed explicitly chooses full tensor/manual-transformer differentiation as added scope. |
| CPU baseline | Works across the two machines without an acceleration prerequisite. | Benchmarks and compatibility checks justify optional GPU use. |
| Gate-based progression and spaced review | Measure independent skill and retention. | Assessment shows a different support level or pace is needed. |
| Current route preserved during planning | Avoid losing state or claiming completion. | Ahmed asks to adopt the new route; reconcile and validate state then. |

Open implementation choices are corpus/domain, actual learner workspace, model/embedding provider or local runtime, any spending budget, RAM/throughput, and optional framework comparisons. They do not prevent producing or reviewing this planning package.

## Decisions corrected after the independent audit

The earlier dialogue above records the 11 October proposal. These dated operational
decisions incorporate the independent review without turning that review into learner
progress or activating a route:

| Decision | Operational consequence |
|---|---|
| Separate readiness, retention, and closure | Execution/explanation plus a fresh independent implementation/debug task permits advancement. Delayed independent success establishes retained status; all required gates need it for closure. Failed retention gets targeted repair. |
| Scope evidence categories | Attempts do not advance; focused bridges satisfy their exact stage only; full completion needs reviewed eligibility. Quiz recognition and changed-input reruns cannot award construction mastery. |
| Sample S0 | Count/explain plus one file/mutation probe; stop at a real blocker and observe remaining skills later. |
| Preserve source/action identity | Hash exact decoded snapshots with defined character offsets; bind approval to action, canonical target, and content hash; test freshness and crash replay. |
| Probe graph/callback mechanisms | Shared-node identity/order and stored callable behavior precede scalar autodiff; syntax choices remain optional. |
| Use qualified references | Unicode/control coverage is repaired in 10/02. Partial 10/04 backward, random-update 10/06 SFT, and simulated 10/10 metrics are excluded from correctness/quality parity. |
| Make model verification exact | Count-weighted content-target NLL, declared context/boundaries, actual next-batch fresh-process resume, first-response/zero-target SFT and initial-equality/update LoRA checks. |
| Maintain continuity and bound S8 | Small assistant tasks rotate through existing lab review time. Re-estimate separate integration/reliability, adaptation-literacy, and final-demonstration slices after S7; original totals remain provisional. |
| Keep candidate inactive | It validates all nine core gates at 10 hours/week and starts at S0 with empty evidence; default active M1 still selects 11.01 at 5–7 hours/week. |

The [evidence protocol](EVIDENCE-PROTOCOL.md) governs the
corrected state semantics. None of these maintainer corrections authorizes a learner
solution, billable model call, project creation, or publication.
