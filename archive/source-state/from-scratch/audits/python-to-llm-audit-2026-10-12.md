# Independent audit: Python to AI engineering and a language model

12 October 2026. Learner: Ahmed. Scope: the 11 October proposal, its operational learning state, and selected reference implementations used by its mappings.

## Assessment

**Keep the two connected projects and the core model-build specification. Resolve progression and assessment semantics before formal adoption, and qualify several incorrect reference implementations before using them.** A guided S0 diagnostic can begin as a recorded project detour after locating the learner workspace. No model-engineering or teaching finding requires completing every later correction before that first interaction.

The proposal is a viable design for intermediate Python, applied AI, RAG, bounded agents, numerical foundations, and a complete small decoder-only model trained from random weights. Its viability is an engineering and instructional-design judgment, not demonstrated learner mastery or measured training performance. The default use of PyTorch tensors/autograd after manual gradient and small-network work is a defensible scope choice. A complete tensor differentiation engine would be additional work.

The final model should retain the proposal's honest label: a small language model with a complete training and inference lifecycle. Strong factual QA, instruction following, and frontier-scale capability require separate evidence.

## Review procedure and limits

Three reviewers worked in separate contexts: Nadia, model engineering; Amelia, Python/software reliability; Paige, teaching and assessment. Each inspected proposal documents 00–06 without seeing the other reviews or document 07's earlier roundtable conclusions. Their first findings were frozen before a shared reaction round. The coordinating reviewer checked current files and adjudicated the findings.

This is an **independent, peer-blinded AI review**, not a fully double-blind study. The source documents reveal the learner and project context; the reviewers share a model family and are not independent human experts. The procedure reduces cross-review anchoring but does not establish statistical independence or eliminate common blind spots.

The review covered prerequisite order, Python progression, project continuity, numerical algorithms, tokenization, model architecture, training, data leakage, evaluation, lifecycle/reproducibility, compute boundaries, RAG/tools, security contracts, tutoring conduct, assessment, retention, pacing, routing, and source mappings. Selected reference routines were inspected and probed; this was not an exhaustive audit of all curriculum lessons.

No proposal, active route, learner progress, lesson implementation, or learner application was changed. This report is the new artifact. No learner proficiency was awarded. Existing working changes were present when the review began.

## What is already sound

- Two accumulating projects connect useful applied work to mandatory model internals. Pure functions and concrete records come before elaborate abstractions.
- Learner authorship, the hint ladder, limited partial assistance, explicit requests for complete solutions, and fresh later checks are already specified.
- Small data, CLI-first releases, stdlib/NumPy/PyTorch, and CPU measurements keep the required scope manageable. Extra frameworks are outside the core estimate and this curriculum's allowlist.
- Scalar backpropagation, shared-node gradient accumulation, numerical checks, and small-network/library comparisons precede transformer training.
- Tokenizer fitting on training data, source-level splitting before windows, duplicate checks, compatible baseline units, future-token invariance, one-batch overfit, and checkpoint identity are already required.
- Hosted inference, offline fixtures, pretraining, RAG, and adaptation have distinct evidence. A tiny trained model is not automatically promoted to the assistant's answer generator.
- Time estimates include a reserve and explicit re-estimation points. The proposal acknowledges missing runtime, provider, budget, workspace, and hardware evidence.

Do not add these again as new recommendations or reopen the route simply because optional advanced topics are absent.

## Findings requiring action

The priorities below identify when a correction matters. They are not a demand to finish the entire list before S0.

### A1 — Required project work can disappear during route validation

**Priority: high, before adopting project stages in the authoritative manifest.**

The adoption proposal allows a later validated manifest revision with project-stage IDs. The current resolver only expands `lesson_ids`; an unsupported required project stage with no such entries produces zero scheduled items and passes its validation function. A successful validation response therefore cannot certify S0–S8 scheduling.

Evidence: [adoption proposal](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/06-CURRICULUM-MAP-AND-STATE.md:104>), [stage expansion](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/scripts/next_learning_route.py:89>), [validation response](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/scripts/next_learning_route.py:124>). Both the independent review and coordinator reproduced the zero-item case using an in-memory fixture.

**Minimum correction:** initially use the proposal's recorded-detour option. Before formal project routing, extend its schema and resolver together, reject unsupported/empty required stages, and verify that every required project gate is returned or explicitly pending. Preserve existing curriculum IDs. The current proposal correctly leaves adoption pending; this finding concerns the future adoption mechanism.

### A2 — Progress records cannot enforce attempt, bridge, and full completion distinctions

**Priority: high, before placing project/focused-study evidence in the resolver's completion table.**

The parser treats a lesson ID in any progress row as completed. It does not inspect assistance, deferred depth, artifact evidence, or the row's status. A fixture with a 0/2 score and an explicit incomplete/focused/deferred note still counts as completed. A quiz score alone is not a universal completion threshold; the demonstrated issue is that record presence cannot enforce the proposal's richer distinctions.

Evidence: [completion parser](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/scripts/next_learning_route.py:55>), [study labels](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/06-CURRICULUM-MAP-AND-STATE.md:22>), [tutor recording procedure](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/.agents/skills/learn/SKILL.md:115>). Coordinator and independent reviewer reproduced the classification in memory.

**Minimum correction:** define distinct attempt, focused-bridge, project-gate, and eligible full-completion records. Route selection must consume only the appropriate category. Until then, keep project detours and bridge evidence separate from the completed-lesson table. A small explicit state record is sufficient; an elaborate progress platform is unnecessary.

### A3 — Advancement, closure, and delayed retention have incompatible definitions

**Priority: high, before the first completion decision.**

[The overview](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/00-START-HERE.md:85>) requires execution, explanation, transfer, and delayed retention for stage completion. [The mastery rubric](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/03-SKILLS-AND-MASTERY.md:78>) normally permits exit at independent transfer with retention only scheduled. Different tutors can accept the same evidence and select different next actions.

**Minimum correction:** name three statuses consistently: ready to advance after execution/explanation/independent transfer; retention pending with a due task; retained after the delayed task succeeds. State whether stage closure includes retention, and what a later failed review reopens. Continue reachable work while retaining visible review obligations.

### A4 — Quiz skill language can override the intended meaning of mastery

**Priority: high, before using phase-quiz outcomes to advance or repair the project route.**

The installed [phase quiz skill](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/.agents/skills/check-understanding/SKILL.md:113>) labels 7–8 multiple-choice answers “Mastered” and 0–2 “Start Over.” Those labels conflict with capability-specific independent construction/retention and targeted repair. Correct recognition does not establish that Ahmed can implement or debug the mechanism; missing full-phase questions after a focused bridge does not justify erasing demonstrated project skills.

**Minimum correction:** explicitly subordinate quiz labels and numeric phase suggestions to the project's evidence rubric and active route. Use quiz results to identify questions for diagnosis; preserve required curriculum quizzes and schemas. Require an independent construction/debugging task for authorship claims.

### A5 — Some early transfer checkpoints establish new-input behaviour, not independent coding

**Priority: medium, before recording M3 for an early Python mechanism.**

[Week 1's new document](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/04-FIRST-FOUR-WEEKS.md:21>) and [week 2's new input without logic edits](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/04-FIRST-FOUR-WEEKS.md:33>) are useful checks, but assisted code can pass them without fresh learner construction.

**Minimum correction:** keep those tasks as execution/generalization or tracing evidence. To award independent construction, request a small new contract implementation or unfamiliar bug repair with the teaching example closed. The plan's stronger week-4 release task is a suitable pattern.

### A6 — The diagnostic needs a stopping rule for sampling

**Priority: medium, before S0's second session.**

[Seven diagnostic tasks](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/03-SKILLS-AND-MASTERY.md:7>) and [session 2's remaining tasks plus repair](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/04-FIRST-FOUR-WEEKS.md:18>) can encourage a broad sweep after one blocking mechanism is already evident. The low-stakes wording and adaptive rules help but do not specify when to stop.

**Minimum correction:** begin with counting/explanation and one file or mutation probe; stop and teach when a specific blocking mechanism appears. Sample remaining areas in the project slices that use them. Unsampled means unobserved. This preserves the diagnostic's purpose without turning it into seven simultaneous lessons.

### A7 — Persistent source positions and indexes need freshness and offset contracts

**Priority: medium, before persisted A1 data feeds S2 RAG.**

The roadmap requires source IDs, paragraph offsets, JSON persistence, and rebuild behaviour, but schedules explicit version invalidation in S8. Editing a document or changing chunking can leave an old excerpt under a known source ID. Windows newline translation and Unicode also make unspecified byte/character offsets ambiguous.

Evidence: [source records and persistence](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/02-PROJECT-ROADMAP.md:35>), [later invalidation](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/02-PROJECT-ROADMAP.md:166>). Python's text-I/O rules explain newline translation. [Official Python open documentation](https://docs.python.org/3.12/library/functions.html#open).

**Minimum correction:** define document hashes, normalization/chunking versions, and stale-index rebuild/rejection. Specify offsets into one exact decoded snapshot, including newline handling. Test document edit/deletion and an Arabic CRLF fixture. Source existence and passage support are separate checks.

### A8 — Approval must identify the exact action, including restart behaviour

**Priority: medium, before S3 enables a writing tool.**

The roadmap already requires approval, action IDs, bounded paths, restart evidence, and repeated-action tests. It does not state whether approval remains valid after content/target changes or after a crash between writing and recording success.

Evidence: [draft and persistence contracts](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/02-PROJECT-ROADMAP.md:82>).

**Minimum correction:** bind approval to action ID, canonical target, and content hash; changes invalidate it. Define idempotent application and test a crash immediately after the write but before success-state persistence. Keep the exercise bounded to one note/output directory. These are refinements to the existing boundary, not additional generic approval rules.

### A9 — Scalar autodiff hides a Python/graph prerequisite

**Priority: medium, before S5.**

[The S5 sequence](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/02-PROJECT-ROADMAP.md:117>) introduces backward functions, topological ordering, and shared-node accumulation without an explicit readiness probe for graph identity, execution order, or stored callable behaviour. Difficulty here can be misdiagnosed as weak calculus and invite excessive solution hints.

**Minimum correction:** trace a tiny shared dependency graph and an unrelated stored-callback example before implementing autodiff. Teach the needed Python mechanism conditionally. Closures and operator overloading are implementation choices; shared graph identity and correct execution order are required concepts.

### A10 — The mapped tokenizer is an unsuitable correctness oracle

**Priority: high, before S6 reference comparison.**

The stdlib fallback [pre-tokenization pattern](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/phases/10-llms-from-scratch/02-building-a-tokenizer/code/main.py:12>) matches ASCII words while excluding Unicode word characters from its punctuation branch. Isolated probes reproduced `مرحبا` and `你好` decoding to empty strings, and `café` decoding to `caf`. [Ordinary encoding](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/phases/10-llms-from-scratch/02-building-a-tokenizer/code/main.py:97>) also automatically emits a registered control ID for its literal spelling. That differs from this proposal's byte-coverage and control-token separation policy. Python's Unicode word-character semantics explain the missing matches. [Official re documentation](https://docs.python.org/3/library/re.html).

**Minimum correction:** label the mapped implementation's limitations and exclude it from correctness parity. Start with full raw-byte coverage, then deterministic BPE; use round-trip and control-policy tests. Do not add `regex`: **stays stdlib-first for educational clarity**. Installing it would not resolve the control-policy mismatch.

### A11 — The mapped pretraining backward path is incomplete

**Priority: high, before S7 training comparison.**

The [reference update loop](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/phases/10-llms-from-scratch/04-pre-training-mini-gpt/code/main.py:229>) updates the MLP, second normalization, final normalization, and the output-use contribution to tied embeddings. It omits attention backpropagation, first normalization, positional embeddings, and the embedding input-use contribution. The independent review's isolated one-step probe observed unchanged attention and positional weights while other parameters changed; the coordinator confirmed the omitted code paths. A falling loss would not prove a complete gradient implementation.

**Minimum correction:** qualify [the mapping](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/06-CURRICULUM-MAP-AND-STATE.md:84>) beyond its existing scale/time warning. Exclude this routine from training parity; verify gradient/update participation for intended trainable modules in the learner's tensor graph. Tiny tests must cover both uses if embeddings are tied. This does not require adding a full manual transformer backward pass to the learner route.

### A12 — SFT reference updates are random perturbations

**Priority: high, before S8 adaptation comparison.**

The [SFT reference](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/phases/10-llms-from-scratch/06-instruction-tuning-sft/code/main.py:145>) calculates `dlogits` but does not use it for the shown weight updates. Instead, it perturbs MLP weights with random arrays. Changed weights and different generated samples therefore do not establish supervised learning driven by response loss.

**Minimum correction:** label the mapped routine as an invalid training comparator. Retain the useful prompt/response mask concept, then implement it on the validated learner graph and verify loss-derived updates. Follow the proposal's explicit byte/control-ID policy. The audit rejected an initial additional claim that clamping to 252 corrupts ordinary valid UTF-8: valid UTF-8 encoded bytes are at most 244. [UTF-8 standard](https://www.rfc-editor.org/rfc/rfc3629). That subclaim is not evidence against this routine; its random-update defect remains independently demonstrated.

### A13 — Model evaluation needs one exact scoring protocol

**Priority: high, before S7 quality claims.**

The proposal already requires compatible tokenization and held-out data. It still needs an explicit definition of which targets are scored, their context, document-start/EOS/tail policy, padding exclusion, and aggregation. Averaging unequal batch means or double-counting overlapping targets can alter comparisons. The mapped [evaluation example](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/phases/10-llms-from-scratch/10-evaluation/code/main.py:112>) simulates token log probabilities from a model-quality argument; it is not measurement from a trained model.

**Minimum correction:** sum measured target NLL and divide by actual scored-target count; freeze context/stride and boundary policies. Define the exact byte denominator for BPB experiments. Verify an unequal-length hand example and label simulated metrics as demonstrations. These concepts are described in [official perplexity guidance](https://huggingface.co/docs/transformers/perplexity) and [PyTorch loss documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html); citing them does not authorize adding Transformers.

### A14 — Existing lifecycle/adaptation gates need two concrete boundary refinements

**Priority: medium, before their S7/S8 verification tasks.**

The checkpoint contract already includes relevant RNG state. With direct random-window sampling that can suffice; shuffled epochs or iterators additionally need permutation/cursor state. A scheduler needs state only when one exists. A resume test with a fixed supplied batch does not check real next-batch continuation. Reproducibility remains limited to a declared controlled environment, as [PyTorch documents](https://docs.pytorch.org/docs/stable/notes/randomness.html).

The adaptation contract already includes prompt masking and frozen/trainable parameter checks. Add first-response-target alignment and a zero-supervised-target policy after truncation. For LoRA, require initial base/adapter output equality followed by an actual adapter update while base weights remain fixed. Both factors initialized to zero would prevent that first learning signal; the current LoRA example already uses the appropriate one-random/one-zero pattern. [Original LoRA paper](https://arxiv.org/abs/2106.09685).

**Minimum correction:** make tests exercise the actual batch path in a fresh process and the stated adaptation boundaries. Keep C0/C1 simple rather than adding workers, schedulers, or optional optimizations solely to satisfy imagined production needs.

### A15 — Keep the assistant active during the lab and re-estimate S8 in slices

**Priority: medium, before S4 scheduling and S8 commitment.**

S4–S7 total 200–290 focused hours, about 24–35 study weeks with the proposed reserve. General spaced reviews exist, but assistant mechanisms are principally revisited in S3/S8. Later integration could require substantial relearning. S8's 20–30 hours also combines reliability, integration, new SFT/LoRA mechanisms, comparisons, packaging, and independent demonstrations in both projects.

Evidence: [effort table](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/00-START-HERE.md:73>), [S8 scope](<D:/AI Projects/Learning/ai-engineering-from-scratch-1/_bmad-output/planning-artifacts/python-to-llm-2026-10-11/02-PROJECT-ROADMAP.md:162>).

**Minimum correction:** rotate occasional assistant traces, bugs, and tiny contract changes into the existing review allocation during the lab. Split S8 into integration/reliability, adaptation literacy, and independent final demonstration; estimate each after S7. No defensible replacement total can be inferred without observed learner pace. Keep the current total as a provisional planning estimate.

## Teaching evidence and its practical limits

The existing research claims are appropriately qualified. [PRIMM's primary paper](https://primmportal.com/wp-content/uploads/2020/10/teaching-computer-programming-with-primm-a-sociocultural-perspective.pdf) supports structured prediction, investigation, modification, and construction in its school setting. It does not demonstrate that this adult roadmap or timetable is optimal.

[Bastani and colleagues](https://hamsabastani.github.io/education_llm.pdf) distinguish assisted mathematics practice from later unaided performance. Their safeguards mitigated harm; they did not establish that this exact tutor policy improves adult Python mastery. The design implication is to measure independent performance separately from assisted success.

Retrieval and distributed practice have support in [Dunlosky and colleagues' review](https://journals.sagepub.com/stoken/rbtfl/Z10jaVH/60XQM/full). [Cepeda and colleagues](https://laplab.ucsd.edu/articles/Cepeda%20et%20al%202008_psychsci.pdf) show that useful spacing depends on the retention horizon. The proposal's one-day/one-week/three-week intervals should remain adjustable heuristics. None of these sources validates the stated project hours.

## The reviewers' shared-room exchange

**Amelia:** “I can approve the first word-counting diagnostic. I cannot approve project-stage routing until a required stage cannot disappear during validation.”

**Paige:** “Amelia, I would keep S0 moving as an explicitly recorded diagnostic detour: save Ahmed's attempt, explanation, assistance, and unresolved gap without closing a lesson or project stage. I disagree with making the full state-system repair a prerequisite for that first small learning interaction.”

**Nadia:** “The recorded detour can proceed once the workspace is located. I distinguish the sound learner build contract from unsafe reference routines. Tokenizer references need qualification before S6, incomplete backward and simulated metrics before S7, and SFT before S8.”

**Amelia:** “A reference that updates weights with random noise or fabricates evaluation probabilities can teach the wrong success criterion. Before each relevant comparison, select a trustworthy small reference or an independently checked fixture.”

**Paige:** “My priority is a reachable next action with honest status: a running script establishes execution; a fresh learner-authored change establishes independent construction; delayed performance establishes retention. We can advance between those checks while keeping the outstanding evidence visible.”

**Nadia:** “I defend scalar autodiff followed by PyTorch. Ahmed needs to understand gradient flow and own the transformer architecture; requiring a complete tensor-autograd engine would substantially expand this route.”

**Amelia:** “Keep SFT and LoRA as separate bounded lab slices and let integration follow measured benefit, so deployment polish cannot conceal unfinished mechanism checks.”

## Verified current state and checks

- The current resolver returns `11.01 / 11/01-prompt-engineering`, M1-S1, full mode. Formal project adoption has not occurred.
- `--validate` returns M1: 26 and M2: 75 expanded lesson references. This checks the current lesson manifest, not project-stage scheduling, learning evidence, or runtime correctness.
- This checkout's progress log has no completed learner rows. That does not establish that work in another learner workspace is absent.
- Relative local links in all eight proposal documents resolve. Selected primary sources were checked; every external link was not exhaustively audited.
- The focused-hour sum is 306–446; the 20% reserve yields 367.2–535.2 hours. At 10 hours/week this is about 37–54 study weeks. Arithmetic is correct; learner pace and training duration remain unmeasured.
- Routing and tokenizer counterexamples were reproduced without altering source/state. Selected model update/evaluation paths were inspected, with a disposable one-step reference probe reported by the independent model reviewer. No learner application was implemented or executed, and no CPU/GPU throughput benchmark was conducted.
- Whole-curriculum validation and test sweeps were not run. No lesson code was changed by this audit.

## Reviewed document fingerprints

SHA-256 identifies the snapshot reviewed; the source package remains unchanged.

| Document | SHA-256 |
|---|---|
| 00-START-HERE.md | f1a543c2f01f103e5070d901e066255550fb286c4ab4b6eefdb4fa085ae77f21 |
| 01-LEARNING-METHOD.md | ca390d71b0fbbaecd61cca46b3eada33a784629e399ef5b91820a16e15b5abdf |
| 02-PROJECT-ROADMAP.md | 05c469eaa798171b8554da5a1a96ec8ffbe1cc1d5a4c422fb78186e7a7b64e75 |
| 03-SKILLS-AND-MASTERY.md | ab58e46f7ad4caea91b03f530f6e7e0c29082667a4cc13781c8961542962c595 |
| 04-FIRST-FOUR-WEEKS.md | 93ceb92482041e8cb1479a97bcfb716b6f7cce5c48615c0f1910d49af5351405 |
| 05-LLM-BUILD-SPEC.md | 3de7d87c43cd730b7a954d60fe62d6d9dcaed8ec60dd53777f295175051f6504 |
| 06-CURRICULUM-MAP-AND-STATE.md | 946b25f647f5a60cbd98de497c6da5b477b9b2080dc59be38af2071699a5074c |
| 07-ROUND-TABLE-AND-DECISIONS.md | 3f33b2fbd71734cad1adf9552d589dced80264fa47712ab34c7871578b405460 |

Document 07 was available only to the coordinator; it was withheld from the independent first passes. This review creates recommendations and evidence, not an adopted route or completed learner milestone.
