# Independent blind adversarial review: projects D, E, F

Reviewed 2026-10-12 against the requested learner: basic Python, ten hours per week in five two-hour sessions, CPU-first with GTX 1050 Ti optional; one coherent cumulative project covering common AI engineering, RAG and agents, intermediate Python, manual gradients/backpropagation, and an owned complete small causal language model trained from random weights.

Only the named blind snapshots were inspected. Source mappings, original clones, other reviews, and consolidation candidates were not inspected. Active native routes govern the judgments below. Historical bulk and vendor tooling do not count as implemented curriculum. The adversarial-general skill was read and applied; findings are descriptive, without severity scores or ranking. Scope gaps are distinguished from defects within a project's declared scope.

Paths below are relative to `blind/project_D`, `blind/project_E`, or `blind/project_F` respectively. Line references name the inspected snapshot, not a live upstream repository. No dependencies were installed, provider calls made, secrets opened, or lesson implementation files changed.

## Project D

### Native route and useful strengths

`README.md:13-16` explicitly selects `Layer1-Final`. Its native route is a 28-week accelerator, 20 hours/week, aimed at an entrant with a year of AI experience (`Layer1-Final/README.md:4-15`). It develops application engineering, hybrid search, evaluated RAG, hand-built tool agents, frameworks, operations, and portfolio work. This is a recognizably broad application-engineering syllabus, rather than just prompt tips.

The weekly failure log, cost log, recurring architecture exercises, and evolving RAG versions are useful habits (`Layer1-Final/README.md:40-48,96-108`). The tutor guide protects independent implementation and progressively increases assistance (`Layer1-Final/guides/GUIDE-FOR-AI-ASSISTANTS.md:22-54`). The code surface contains concrete ingestion, chunking, parent-document retrieval, provider, structured-output, and persistence modules; for example, `src/ingest/retriever.py:1-120` makes child-to-parent relationships inspectable. These are candidates for small implementation exercises after validation, rather than proof that the active 28-week route is complete.

### Findings

- The starting assumption is wrong for the requested learner. Twenty hours/week and a year of prior AI experience are explicit prerequisites (`Layer1-Final/README.md:6,15`), while the learner has basic Python and half that weekly time. Week 1 immediately asks for async CRUD, PostgreSQL, and migrations (`:78-85`). Reusing this route requires a genuine Python/engineering bridge and a re-budgeted schedule; merely renaming its weeks would preserve the prerequisite failure.

- The recommended quick-start is stale and points outside the active tree. `README.md:15,42` directs the learner to `QUICKSTART.md`, but that file describes `curriculum/chapters`, templates, and reference paths (`QUICKSTART.md:31-44,61,82-86`) absent at the snapshot root. It also starts with chapter-development choices (`:52-71`), rather than an active learner exercise. This breaks the first navigation boundary.

- The active route is largely a syllabus and governance package, not a sequence of executable weekly lesson packages. `Layer1-Final` contains README, guides, and four documentation files, with no active week directories or scaffold/test chain. “Start Week 1” routes to a summary table (`Layer1-Final/README.md:24,78-85`). Root code and historical chapters do not establish which file a beginner should edit, which focused command proves the week's result, or how it joins the next week.

- One repository is confused with one coherent project. The rule says all work lives in one portfolio repository (`Layer1-Final/README.md:42`), but the route explicitly adds two flagships and two mini-projects (`:87,105-108,125,169-179`). The requested single project needs shared contracts, data, state, and cumulative checkpoints; collecting several deliverables in one Git repository does not provide that continuity.

- The schedule silently exceeds five sessions and has inconsistent buffer accounting. Mini-projects occur on the weekend after Weeks 4 and 10 (`Layer1-Final/README.md:87,108`), beyond the stated five-day schedule. The overview calls out flex or flex-specialization weeks at 9, 16, 20, and 27 (`:102,123,146,161`) while the differentiator claims two (`:212`). Those labels cannot serve as a dependable ten-hour/week plan without distinguishing required work, recovery, and optional specialization.

- The root installation has conflicting application and dependency identities. README names a Civil Engineering document system (`README.md:74-85`), while package metadata identifies an AI time-estimation agent for web projects (`pyproject.toml:7-8`). `requirements.txt:7-21` pins an expansive provider/framework stack; `pyproject.toml:32-38` offers a different optional version policy, including a different minimum LangChain OpenAI version. No single documented environment contract connects these code surfaces to the active weekly route.

- Training depth does not meet the requested model-building outcome. The route frames AI engineering as building with models (`Layer1-Final/README.md:15`) and offers an optional fine-tuning specialization (`:131`). The specialization loads a pretrained Mistral model and pretrained tokenizer with quantization (`Layer1-Final/docs/WEEK-16-SPECIALIZATION.md:935-959`). That is adaptation, not an original causal LM trained from random weights, and it contains no required manual-gradient/backprop chain. There is also no bounded CPU training contract or measured GTX 1050 Ti fallback in that route.

- A green test summary could hide missing implementations. Several chapter-error-handling tests turn import or implementation errors into skips (`tests/test_chapter_06B.py:24-25,41-42,57-58,73-74,92-93`). Skips may support unfinished scaffolding, but acceptance must explicitly reject missing required behavior. Otherwise missing modules look like harmless optional omissions instead of unmet capabilities.

- The production-ready exit wording is unsupported by the active teaching evidence. The route promises both flagships production-ready by Week 22 (`Layer1-Final/README.md:221`) without an active executable route or per-learner operational proof. Retain deployment, security, and observability tasks as gated learning goals; remove readiness claims until concrete evidence exists.

### Offline checks and reuse decision

Attempted `python -m pytest tests/test_chapter_06B.py -q -p no:cacheprovider` with bytecode disabled and plugin auto-loading disabled. Collection stopped at `tests/conftest.py:4` because the shared interpreter lacks `hypothesis`. This is a limitation of the available review environment, not proof that D fails in its declared environment. No dependency installation was attempted.

Reuse the failure/cost logs, ownership-oriented tutor ladder, RAG/agent topic inventory, and selected small ingestion tests. Omit stale quick-start instructions, market/readiness slogans, required framework comparisons, Kubernetes/Terraform as beginner core, multi-project architecture, and pretrained adaptation as a substitute for model construction. D needs substantial route engineering before it can carry this learner.

## Project E

### Native route and useful strengths

`START_HERE.md` and `curriculum/main-track/milestone-1-45-hour-map.md` define a concrete cumulative AI Application Implementer route. Its strongest property is narrow executable continuity: the same learner scaffold is used from deterministic baseline through provider boundary, evaluation, grounded retrieval, controlled tool, real HTTP, traces, and defense (`curriculum/main-track/06-capstone-projects/week-03-integration-build/README.md:1-44`). The two-hour schedule has 20 planned sessions and explicit recovery (`START_HERE_2_HOURS_PER_DAY.md:3-6,23-34`), naturally usable across four five-session weeks before repair time.

Support labs have focused selectors, return conditions, and caps rather than forcing completion of the whole library (`week-03-integration-build/README.md:50-76`). Provenance precedes retrieval, citation/abstention precedes authority, and explicit bounded workflow precedes autonomy. The evidence matrix correctly separates structural health, fixture reference behavior, live access, and learner ownership (`LEARNER_READY_MATRIX.md:9-15,49-69`). This is the most directly reusable application-teaching spine among D/E/F.

### Findings

- The advertised placement procedure does not yet establish readiness. `START_HERE.md:29-39` tells the learner to run a five-test sample and infer Python gaps. In the untouched scaffold, swap and flatten are already implemented (`curriculum/main-track/00-python-foundations/week-00-diagnostic/diagnostic_workbench.py:53,106`), while multiplier, Counter, and division remain TODOs. Running the command gives two passes and three failures regardless of whether the learner knows Python. The diagnostic README acknowledges that exact starter result but still calls its failures placement signals and makes implementing TODOs optional (`week-00-diagnostic/README.md:21-25,50-52,74-81`). Reflection can reveal comprehension, but the procedure needs an explicit independent implement/explain task and scoring rule; supplied passes and TODO failures alone are not diagnostic evidence.

- Beginner repair exists but does not have a validated basic-to-intermediate route budget. Module 0 describes eight to twenty remediation hours outside the milestone clock and calls itself a readiness/support track rather than a beginner syntax course (`curriculum/main-track/00-python-foundations/README.md:9-18`). Production Python is optional (`:40-42`). The requested intermediate Python outcome needs explicit application-linked gates for exceptions, classes, iterators, context managers, testing, packaging, and state, with an actual ten-hour/week calendar; it cannot be inferred from incidental Python use.

- The native long-term journey breaks the requested single-project constraint. Milestone 2 explicitly asks for an independently built second application (`curriculum/LEARNER_JOURNEY_MAP.md:46-53`). Independent transfer is a sound mastery test, but the planned learning product is no longer one coherent cumulative project. Adapt this to a fresh vertical slice, unseen requirement, or second data source within the same project while retaining independent transfer evidence.

- The model-internals shelf is intentionally insufficient for a complete causal LM. Tiny-transformer authoring explicitly excludes full GPT training, backpropagation, and token sampling (`curriculum/extended-concepts/01-model-internals/week-01-tiny-transformer/AUTHORING_PLAN.md:95`). Its scaffold has inspectable projections, attention, normalization, and an affine feed-forward step (`workbench.py:45-100`), but no causal mask parameter, positional mechanism, LM head, next-token cross entropy, or training loop. This is useful preparatory forward-pass work; it must not be counted as the user's language-model deliverable.

- Training versus inference only bridges to a scalar linear model. `curriculum/extended-concepts/01-model-internals/week-02-training-vs-inference/workbench.py:9-39` supplies one weight, one bias, MSE, and a gradient step; the lesson explicitly avoids training a real LLM (`README.md:32`). The missing chain is finite-difference gradient checks, chain-rule/backprop over composed operations, tensor/matrix gradients, trainable embeddings and attention, causal next-token objective, checkpoint/reload, and generation from the learner's trained weights. These are new required work, not a minor extension of the scalar exercise.

- Milestone 1 intentionally substitutes fixture output and keyword retrieval for live model behavior. The cumulative checkpoint table calls keyword overlap a local stand-in (`week-03-integration-build/README.md:38`) and fixture/live proof is separated (`:90-108`). This is honest and pedagogically useful, but a later explicit gate must demonstrate a real model boundary and semantic retrieval before claiming common AI engineering competence. Passing the fixture reference alone cannot establish robustness against probabilistic failures or a real provider adapter.

- The later route has capability aspirations rather than an executable progression matching this learner. Milestone 2 is an 80–120-hour planning range, and Milestone 3 branches into specializations (`curriculum/LEARNER_JOURNEY_MAP.md:46-76`). No native required path binds the intermediate Python and causal-LM work to those milestone gates, nor supplies CPU model size, corpus split, training-time budget, and resumed two-hour-session behavior. Keep M1's bounded budget separate from a newly estimated full learning journey.

### Offline checks and reuse decision

Used available Python 3.13.9, with bytecode disabled and pytest plugin auto-loading disabled. `python scripts/validate_curriculum_references.py --strict --executable` passed the cumulative reference's 11 checks; the script reported 42 scaffolds with reviewer notes and no missing notes. `python scripts/validate_curriculum_quality.py --strict` imported 42/42 scaffolds and reported zero curriculum-contract issues. This verifies a fixture-backed reference plus structural quality, not learner mastery, timing, live providers, or production.

The documented setup test passed both tests. The untouched five-test placement sample produced two passes and three TODO failures. Those failures are expected starter behavior and specifically demonstrate why its current run-first readiness interpretation needs refinement.

Reuse the cumulative checkpoint scaffold, local HTTP proof, fixture-first access, source evidence/citation gates, denied tool and bounded workflow tests, evidence distinctions, capped support labs, and session-close format. Reuse tiny-transformer and scalar-gradient exercises as preparatory labs with their limitations preserved. Omit a mandatory second project, any inference that fixture reference success proves learner competence, and treatment of the model-internals shelf as finished LM training.

## Project F

### Native route and useful strengths

F is a rebuild/pilot workspace, transparently not a student release (`README.md:3-11`). Its active manifest specifies a prepared-entrant 33-hour Evaluated AI Service. Three starter lessons form a five-hour pilot; later units are contracts only (`curriculum/1st_Milestone/manifest.json:5-7,61,125-237`). The project is one Evidence-backed Work Intake Service, a modular monolith rather than a framework catalogue (`manifest.json:62-79`).

Its first lesson is concrete, readable, and bounded: predict schema/timeout behavior, inspect a fake, implement one boundary, verify normal and rejected paths, then explain evidence (`lessons/01-first-bounded-model-proposal.md:16-97,158-226`). Typed results require exactly one proposal or failure (`work_intake.py:25-37`). Lesson 2 distinguishes schema validity from source support and deterministic review authority. Lesson 3 has real loopback tests and a supplied transport with request size limits, timeouts, safe errors, and unsupported-method handling (`http_api.py:19-35,75-144`). These are useful reusable teaching patterns.

### Findings

- A basic-Python learner cannot currently enter through an implemented repair route. The admission contract requires functions, collections, exceptions, type hints, JSON, HTTP, terminal work, and Git (`curriculum/1st_Milestone/README.md:26-45`), while the repair shelf is explicitly unimplemented (`manifest.json:52-57`). Classification can identify the blocker but cannot teach the learner out of it. Build and validate targeted bridge lessons before assigning this route to the requested entrant.

- The active route stops after three lessons. Evaluation, PostgreSQL persistence, failure/authority hardening, deployment/operations, and ownership units are `contract_only` (`manifest.json:172,187,203,220,237`). This is not a deceptive completeness claim—the root acknowledges it—but it means F cannot be selected as an immediately usable full curriculum. Its best value is the first pilot and standards, with the later route treated as authoring backlog.

- The active scope excludes major requested capabilities. Default RAG/vector databases, autonomous/multi-agent systems, MCP implementation, and training are deferred (`manifest.json:285-296`; `README.md:213-225` under the milestone). Deferring complexity is correct for the first service, but the repository does not supply an authoritative next route incorporating RAG, agent loops, manual backprop, and a complete random-weight causal LM. Historical chapters cannot fill that authority gap automatically.

- The current route lacks a two-hour-session schedule and CPU model-training envelope. Manifest unit budgets span 90 to 420 minutes (`manifest.json:123-234`) and the pilot's lesson budgets are 90, 105, and 105 minutes (`:241-270`), but the native route does not map unit resumption, retrieval practice, and evidence handoff onto five two-hour sessions/week. No CPU corpus, model-size, checkpoint, or training-time contract exists because model training is outside the active route. These constraints need an explicit extension rather than assumed compatibility.

- The setup command introduces unnecessary dependency breadth at the first offline boundary. Lesson 1 runs `setup.ps1` before its three supplied support checks (`lessons/01-first-bounded-model-proposal.md:51-67`). That script installs the whole editable package with dev extras (`setup.ps1:19-20`), whose dependencies include the live OpenAI client (`pyproject.toml:12-15`). The live probe is separate and optional, but the offline-first learner setup still resolves its SDK. A separate offline lesson environment would preserve access when provider SDK installation is blocked, and optional live extras can be added at the live gate.

- Full-route acceptance still depends on live provider and deployed black-box evidence (`manifest.json:114-120,213-237,275-281`) without an implemented path for those later units. This is an appropriately honest exit gate, but it creates unresolved budget/access requirements for a learner whose first priority is local CPU progress. Keep blocked evidence explicit and provide a clearly labelled local milestone exit and a later hosted evidence gate instead of allowing unknown provider/deployment time to absorb the fixed instructional budget.

- The published validation wrapper conflates starter-red and completion checks. `check.ps1:11-14` runs the entire unfinished suite. Lesson 1 correctly warns against using it for lesson acceptance (`lessons/01-first-bounded-model-proposal.md:81-83`), but setup calls it a whole-milestone integration check (`setup.ps1:28`). Until later lessons exist, novice users need separately named support-health, lesson acceptance, and eventual route-completion commands so expected TODO red output cannot be misread as broken installation or missing production behavior.

### Offline checks and reuse decision

Ran `python -m pytest tests -q -p no:cacheprovider` in the active milestone with bytecode and plugin auto-loading disabled. Result: 16 passed, 28 failed. The failures were unfinished learner boundaries, including `work_intake.py:73,80,85,90` and `http_api.py:44`; the loopback learner acceptance test receives the expected starter 500 from that unfinished adapter. This is expected starter-red evidence, not 28 claimed curriculum defects. No test collection/import failure appeared in this available environment. The run is not a clean install or validation of the pinned dependency versions.

Reuse the first three scoped starters, plain-language terminology, predict/trace/implement loop, schema-versus-semantic distinction, model-proposes/software-authorizes architecture, real loopback transport tests, unrelated entry transfer task, and manifest evidence labels. Omit historic route authority, any implied 33-hour completion claim, absent repair shelves as if already usable, and infrastructure/deployment depth before beginner gates. F's technical standards and pilot may improve another route, but F itself remains an incomplete application route and supplies no causal-LM completion path.

## Consolidation implications without selecting a source identity

None of D/E/F independently satisfies the full requested goal. E provides the strongest executable cumulative application spine and the closest session rhythm. F provides unusually clear scoped teaching and evidence contracts, with honest release limitations. D supplies broad topic coverage and useful engineering habits, but its native pacing, project count, navigation, and executable lesson continuity need the most adaptation.

A coherent combined route still needs newly authored and validated work: basic-to-intermediate Python gates integrated into one product; manual gradient and chain-rule exercises with numerical checks; an inspectable original causal decoder with positional information and next-token objective; training from random weights on a small documented corpus with leakage-safe splits; CPU runtime/memory measurements; resumable checkpoints suitable for two-hour sessions; held-out loss and generation evidence; and the trained model connected back to the same application's provider boundary with an honest comparison to fixture and external models. GTX 1050 Ti use should remain optional until compatibility and benefit are measured. These are acceptance requirements for the user's intended route, not features demonstrated by the reviewed snapshots.
