# Party discussion: the choices behind the plan

Historical planning discussion. The adopted one-workbench decision is recorded in the update at the end; older project/activation choices below are not current authority.
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


## Adoption update — 11 October 2026

The user subsequently authorized a blind review and consolidation of six owned repositories, publication of one coherent project and removal of redundant projects. The governing choices are now one Workbench with an applied assistant and an internal model laboratory, one S0–S8 route, ten hours weekly, CPU-first completion and independent learner evidence. Earlier proposal-only activation language in the discussion is historical. The review report explains retained content, rejected duplication and executable limits.

## Revision — 15 October 2026

A second round table reviewed the learner's remaining GitHub repositories and the job market for RAG and agents. Ahmed decided:

- **Focus:** RAG systems, then AI agents and agentic engineering, are the depth of the current route. Python, evaluation, observability, cost, security and delivery are the floor inside every stage. Deployment/LLMOps is a later branch.
- **Learn as needed:** theory only as far as each mechanism needs; learn practice with existing libraries and frameworks. The from-scratch work (formerly S4–S8) becomes an optional track, T1–T5 in the [build specification](05-LLM-BUILD-SPEC.md).
- **Frameworks:** LangChain, LangGraph, LangSmith and LlamaIndex are core even where Mushir does not use them. The market-researched [library map](08-LIBRARY-MAP.md) tiers the rest.
- **Mushir:** the client approved using Mushir for learning. Each stage applies its mechanism in the private Mushir checkout. AAOIFI's site permits personal and educational download but requires a licence for redistribution, so standards text stays out of this public repository and is linked instead.
- **Python:** stays inside this workbench as the S1 floor; no separate Python repository.
- **Consolidation:** the HR-Agent corpus and eval data became the S3–S6 practice corpus; the unmerged from-scratch branch's lessons joined the optional shelf and its second route was archived; `explorations/` holds side quests such as the LangChain loader notebooks.

The route went from S0–S8 (306–446 hours, about 65% from-scratch model work) to S0–S6 (174–256 hours). No learner evidence existed beyond one context note, so no credit was lost.

