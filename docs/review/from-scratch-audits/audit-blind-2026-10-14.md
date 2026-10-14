# Blind audit: Python-to-LLM learning project

Date: 2026-10-14. Method: read-only except this file. Phases 1-4 were written before any prior audit was opened. Phase 5 is appended at the end.
Labels: CONFIRMED = I reproduced it. PLAUSIBLE = inferred, not reproduced.

## 1. Verdict

| Side | Verdict |
|---|---|
| Technical | **Ship after fixes** |
| Pedagogical | **Rework** (targeted; the method is sound, its operationalization is missing) |
| Overall | **Rework (targeted, not a restart)** |

Justification:

1. Compute and mechanism specs are sound. Measured C1 = 137k params at 48k tokens/s on CPU; CPU is not the constraint.
2. The plan does not drive the actual route. The resolver still returns `11/01-prompt-engineering` at 5-7 h/week (CONFIRMED), so Day 1 of the plan is unreachable.
3. The evidence gate can be forged: one `README.md` closed all 13 gates and the whole milestone (CONFIRMED).
4. Learner-owns-solution is stated everywhere but not enforced. Hint ladders are generic, leak on small tasks, solutions are co-located with the learner, and the tutor skills do not load in this checkout (CONFIRMED).
5. Hours are understated. My recomputation is 58-87 weeks versus the plan's 37-54, and the first 40 hours contain no AI.

Dissent recorded: one reviewer (architecture lens) would rate the overall "Ship after fixes".

## 2. Scorecard

| # | Dimension | Side | Score | Reason |
|---|---|---|---|---|
| 1 | Learner fit | Ped | 3 | Diagnostic is embedded in the project (good); Week-2 checkpoints exceed "basic Python" |
| 2 | Time realism | Ped | 2 | S8 is an admitted placeholder; 20% reserve; retention unbudgeted |
| 3 | CPU feasibility | Tech | 5 | Measured; 4 GB irrelevant at these sizes |
| 4 | Cumulative design | Tech | 3 | Two threads share concepts, not code; LLM arrives at week 51+ |
| 5 | Coverage vs demand | Tech | 3 | Strong on eval/RAG/agents; deployment, observability, frameworks deferred |
| 6 | Pedagogy | Ped | 3 | Evidence cited with honest limits; weak operationalization |
| 7 | Assessment/evidence | Ped | 2 | Heavy, forgeable, no waiver, retention not time-aware |
| 8 | Internal consistency | Tech | 2 | 435 vs 503, 5-7 vs 10 h, M1 vs plan, py/python3 |
| 9 | Honesty of claims | Tech | 4 | Simulated metrics disclosed; most claims reproduce |
| 10 | Maintainability | Tech | 3 | MCP spec superseded, Pascal cliff, annex outside repo, dangling skill links |
| 11 | Tutor-contract enforcement | Ped | 3 | Contract text good; no per-task ladders, no separation |
| 12 | Motivation/ergonomics | Ped | 3 | Week-1 win exists; no AI for 40 h; no rest or stall plan |

Technical subtotal: 20/30. Pedagogical subtotal: 16/30.

## 3. Phase 1: cold read

Day 1 as I would do it before reading further: open `00-START-HERE.md`, follow its last paragraph ("locate the actual learner project, open S0 task 1"), create a folder, open `04-FIRST-FOUR-WEEKS.md`, answer Task 1 (`04:65-69`): predict counts for `Python helps. Python teaches!`, write `count_words`. This works with only basic Python and the PATH `python` (3.13.9).

Ambiguities recorded:

1. No learner project exists; nobody is told to create one (`00:104`, `02-PROJECT-ROADMAP.md:13`, `04:20`).
2. Which route governs: plan "inactive", resolver still picks 11.01 (`00:106`).
3. Pace: 10 h/week (`00:15`) vs `LEARNING.md:12` 5-7 h.
4. A tutor is assumed every session; docs are "reference material for the tutor" (`04:71`), so a learner has no handbook for a tutor-less day.
5. `py` launcher is cited (`06:16`, AGENTS.md); it does not exist on this machine.
6. Annex is an absolute personal path outside the repo (`00:36`).

## 4. Requirement traceability (Phase 2)

| Requirement | Where | Verdict |
|---|---|---|
| Junior with basic Python, gradual | `03:7-21`, `04` | Partial: design Met, Week-2 steps too heavy |
| End goal: full LLM by hand | `02` S5-S7, `05` | Met on paper; reached week 51-76 in my estimate |
| Cumulative project-based guided | `00:9-11`, `02:7-13` | Partial: "share code only after two consumers" (`00:55`) |
| 2 h/day, 5 d/week | `00:15`, `01:35-47` | Met (budget Partial) |
| CPU-first, 1050 Ti 4 GB | `05:55-71` | Met (CONFIRMED by benchmark) |
| Skill list: Python, NumPy/math, ML, NN, tokenization, transformers, pretrain/SFT, LoRA, embeddings, RAG, eval, tools/MCP, agents | `03:44-66`, `02` | Met |
| Guardrails, cost/latency | `02:76,95` | Partial (tests and reports, no depth) |
| Deployment | deferred `02:179` | **Missing** |
| Start with an AI project, Python checked inside | `00:9`, `03:7` | Partial: embedded, but first 40 h is keyword search, fixture only |
| Evidence-justified method | `01:9-17` | Partial: cited and hedged; operational detail thin |
| Five supplied reference lists | annex (outside repo) | Partial: classified, name-dropped, no task derived |
| Learner owns solution | `01:49-69`, `04:65-69` | Partial: see H-04, H-05, H-06 |
| LEARNING.md / docs/learning-path consistent | `LEARNING.md:12`, `route.json:5-8` | **Contradicted** |
| 2026 currency | `02:93` | Partial: MCP spec superseded |

## 5. Findings (ordered by severity)

### Blocker

**B-01 The plan is not operational (CONFIRMED).** Evidence: `00:106`; `route.json:5-8`; `LEARNING.md:8-12`; resolver output `11/01-prompt-engineering`, M1-S1. A tutor following AGENTS.md "Learner-mode routing" teaches Phase 11 prompt engineering at 5-7 h/week to a learner placed 0/10. The project route is inactive and no adoption runbook creates the workspace. Impact: the learner's Day 1 is either a detour or the wrong course. Fix: write an adoption runbook (create separate workspace, set pace 10, switch the route or add a project mode to the `learn` skill, record adoption). Re-verify: resolver returns S0 and `LEARNING.md` pace agrees.

### High

**H-01 Evidence gate is forgeable (CONFIRMED).** Evidence: `scripts/next_learning_route.py:180-184` (existence-only), `:239-252` (retention only needs `checked_at` > `observed_at`, no minimum delay, no future-date check); `EVIDENCE-PROTOCOL.md:57-62`. Probe: 13 forged records citing `README.md` returned `milestone_requirements_closed`. Impact: the tutor or learner can self-certify mastery. Fix: bind evidence to an artifact hash plus commit inside the learner workspace, reject paths in the curriculum root, require a minimum delay (7 days) and no future dates, and separate assessor from learner. Re-verify: the probe returns `status: error`.

**H-02 Time budget understated.** Evidence: `00:69-83` (S8 "provisional 20-30 h" holds SFT, LoRA, integration, packaging, final demo; 20% reserve); `MILESTONES.md:32` (35-45 h for M1). My recomputation is in section 8: 58-87 weeks versus 37-54. Retention tasks (13 gates, about 20-26 h) are not budgeted (`01:102` says they fit existing Friday time). Fix: S8 at least 50 h, a 15% overhead line, a rest/stall week per 8, re-baseline after S1 with measured pace. Re-verify: stage hours sum to the calendar.

**H-03 Week-2 checkpoints exceed a junior's capacity; first 40 h have no AI.** Evidence: `04:32` (session 7: half-open offsets into a hashed LF-normalized snapshot, Arabic CRLF), `04:34` (session 9: raw and snapshot hashes, version invalidation, corrupt-index rejection). Reproduced: on Windows `write_text` writes CRLF (3 CRLF, 0 LF), so the raw hash differs from Linux/CI (`ceb961de…` vs `d36b3fe0…`); `read_text` hides the CRLF so a naive test passes trivially; slicing `"مَرْحَبًا"[0:1]` splits a base letter from its fatha, so "character offsets" are undefined (code points vs graphemes). This is my pick for the step most likely to make a junior quit (PLAUSIBLE on quitting, CONFIRMED on the mechanics). Fix: defer hashing and manifests to after first eval; use text-mode snapshot; define offsets as code points; add a model-touch win (bigram sampler) by week 3. Re-verify: a fixture written on Windows passes the same test on Linux.

**H-04 Hint ladder leaks by construction on small tasks.** Evidence: `01:62` (H3 "sorting concept with unrelated records" is the solution for top-k), `01:63` (H4 "single blocked update" equals the whole count update); the ladder is generic, not per task (`01:57-63`).
Simulations:
- Early Python (word count). Learner: "my counts are always 1". Tutor H1 asks to inspect after the second "Python". Learner asks for more. H3 "different problem" = `votes[n] = votes.get(n, 0) + 1`, isomorphic to the answer.
- Mid NN (shared-node backward, G5). Learner gets `x*x` grad `x`. H2 pseudocode "accumulate" is the whole fix; H4 is one token (`+=`).
- LLM build (causal mask, G6). H1 "mask relative to softmax" is the fix; H3 "padding mask" example is the same `masked_fill`; H4 is that line.
Fix: tutor-facing per-task ladder cards with "never reveal" sets, plus a rule: if the tricky part is at least half the solution, H4 becomes a different-domain analog and the learner writes the transfer. Re-verify: a scripted tutor-simulation eval on 3 tasks shows no ladder step contains the target line.

**H-05 No tutor/learner separation; solutions co-located.** Evidence: 501 of 503 lessons ship `code/` with full reference solutions; `check-understanding/SKILL.md:58-62` reads all phase docs; spec spoilers in learner-readable files (`02:170` and `05:94` give LoRA init and "zero factor receives first signal"). `01:53` is an honor system. Fix: tutor-only index of "do not show" files, and learner workspace outside the checkout (already planned, make it mandatory). Re-verify: tutor-simulation never quotes reference code.

**H-06 Tutor skills do not load here, and the ladder is not wired into any skill (CONFIRMED).** Evidence: `.claude/skills/{learn,start-learning,course-guide,check-understanding,find-your-level}` are junctions to `D:\AI Projects\ai-engineering-from-scratch-1\...`, which does not exist; `.agent/skills` lacks them; only `.agents/skills` has files. These skills are absent from this session's skill list. `learn/SKILL.md:86-92` cites AGENTS.md only; H0-H4 live in a planning document that no skill loads. Fix: recreate junctions to the real path or copy, and reference the ladder from `learn`. Re-verify: `learn` appears in the skill list.

**H-07 Evidence system too heavy and has no exit for unavailable live gates.** Evidence: 13 gates times 4 checks with artifact paths (`EVIDENCE-PROTOCOL.md:55-74`); a 15-field note in the last 10 minutes of every session (`01:43`, `01:112-130`); `STATES` has no waiver (`next_learning_route.py:18`). Live gates need paid API or network. Probe: all gates but `S2-live-generation` returned `milestone_ready_retention_or_gates_pending`, a permanent state. Fix: one-line session log, tutor-generated gate JSON, add `waived`/`deferred` with reason. Re-verify: a no-budget learner can reach a closable state.

### Medium

- **M-01 Retention is not time-aware.** `next_learning_route.py:265-275` never compares `due` to today; overdue items never surface; debt accumulates to S8. Fix: report `overdue` in `pending_obligations`.
- **M-02 No stall or solo-day protocol.** H4 needs an explicit ask (`01:65`) with no stuck budget, so a shy junior can sit at H3 for a whole session; the only timer is for environment problems (`04:86`). Fix: tutor must offer the escalation after N unproductive rounds (offering is not violating); add a one-page learner handbook.
- **M-03 Active M1 route conflicts with the requirement.** `LEARNING.md:6` mission is a portfolio, M1 is applied LLM (RAG, LoRA, MCP, LangGraph), placement 0/10 enters Phase 1 yet the route starts at 11.01. M1's 35-45 h is built on doc-stated lesson times (sum 25.5 h for 20 lessons) that assume reading, not learner-authored code.
- **M-04 MCP spec superseded.** `02:93` pins 2025-11-25 and requires "initialization, capability negotiation". The official page now shows 2026-07-28 with stateless requests and per-request negotiation (CONFIRMED). Fix: link `/latest`, reword the task.
- **M-05 Coverage gaps.** Deployment (requirement), observability, framework and vector-store literacy, judge calibration, prompt regression (see section 7).
- **M-06 Dependency and environment contradictions.** `pyproject.toml`/`requirements.txt` list anthropic, openai, scikit-learn, transformers, tiktoken and more against the AGENTS.md allowlist; lesson 11.16 imports langgraph; mapped lessons import sklearn, tiktoken, datasets. Base Anaconda 3.13.9 has no torch (the repo `.venv` 3.12.14 has torch 2.13.0+cpu). AGENTS.md commands `py` and `python3` do not exist here (CONFIRMED; mitigated in `learn/SKILL.md:41-43`).
- **M-07 Reference lists only name-dropped.** Annex has a classification table (`PROJECT-SOURCE-REVIEW.md:11-17`), no derived tasks, and lives at `C:/Users/Asd/.codex/...`.
- **M-08 Audit overstates health.** `audit_lessons.py:129-132` skips missing quizzes, so 165 of 503 lessons without `quiz.json` pass with "0 issues"; five mapped lessons lack quizzes (07/03, 07/04, 07/05, 07/07, 10/13). AGENTS.md says 435 lessons (`:5,:11`), README says 503.
- **M-09 `learn` warm-up uses MCQ recall** (`learn/SKILL.md:66-72`) while the plan requires production retrieval (`01:100`); generated checks are recorded as scores (`:114-117`).
- **M-10 Skip-ahead is soft.** `route.json:14` honors named overrides with no prerequisite-gate warning; the resolver ignores S5 evidence without S0-S4 (CONFIRMED) but a detour bypasses it.

### Low

- **L-01** `link_check.py` reports 12 "broken" links here: arXiv fails on SSL verification, PRIMM returns 403, yet curl returns 200. It exits 0 without `--strict`.
- **L-02** `completed_lessons()` is dead code returning an empty set (`next_learning_route.py:82-86`).

## 6. Reproduction log

| Command | Result |
|---|---|
| `python -X utf8 scripts/next_learning_route.py --project-root .` | next = 11.01 (PASS, consistent with docs) |
| same with `--validate` | valid; M1 26 lessons (20 required + 6 conditional), M2 75 |
| candidate `--validate` | valid; 9 stages, 13 required gates |
| candidate next | S0 |
| `python -m unittest discover scripts/tests` | 30 tests OK |
| `py -X utf8 ...`, `python3 ...` | command not found (FAIL on this machine) |
| `scripts/audit_lessons.py` | 503 lessons, 0 issues (see M-08) |
| `scripts/check_readme_counts.py` | counts match |
| `scripts/link_check.py` on planning set | 12 broken, all false positives (L-01) |
| lesson count | 503 dirs; 338 quizzes; 501 `code/`; 439 `outputs/` |
| 64 mapped lessons | all `docs/en.md` present |
| 10/02, 10/04, 10/06, 10/10 tests | 16, 7, 7, 8 OK; 10/02 demo exit 0 |
| forged evidence probes | closed milestone from `README.md` (H-01) |
| CPU benchmark (`.venv`, 8 threads) | C0 30,432 params 27k tok/s; C1 137,472 params 48k tok/s; C2 1,334,016 params 18k tok/s |
| `git` in checkout | "dubious ownership" error (environment-specific) |

Weeks 1-4 code: none exists. I executed the task specs' mechanics in scratch only (CRLF, hashing, Arabic slice). Running Python may have created `__pycache__` directories in the checkout.

## 7. Claims ledger and gaps

| Claim | Status |
|---|---|
| All lesson links exist (`06:5`) | Reproduced |
| Resolver returns 11.01 (`06:13`) | Reproduced |
| `py` unavailable (`06:16`) | Reproduced |
| Candidate resolves S0 and nine core gates (`00:106`) | Reproduced |
| Progress table empty (`06:8`) | Reproduced |
| Focused reference demos/tests now exist (`06:5`) | Reproduced (38 tests pass) |
| SFT is random noise; eval simulated (`05:135-142`) | Reproduced (`10/06 main.py:170-173`; `10/10 main.py:13-14`) |
| Partial backward in 10/04 | Reproduced as marker only (`main.py:9-10`) |
| TinyStories license CDLA-Sharing-1.0 (`05:79`) | Reproduced |
| `.venv` recreated and synced (`06:111`) | Partly: exists, imports; sync not verified |
| README counts match | Reproduced; AGENTS.md 435 contradicted |
| "Audit 0 issues" | Reproduced but overstated (M-08) |

Gaps (skill, slot, cost):

| Skill | Slot | Cost |
|---|---|---|
| Serving, Docker, CI | after S2 (week 18-20) | 12-18 h |
| Observability and cost accounting | S3 | 6-8 h |
| Judge calibration, RAG metrics | S2b | 4-6 h |
| Prompt versioning and regression | S2 | 4-6 h |
| Framework and vector-store literacy | after S3, separate workspace | 10-16 h |
| Real-model LoRA/QLoRA | after S8 branch | 20-30 h |
| Async concurrency for LLM calls | after S3 | 6-8 h |
| Chunking, PDF, dedup | S2 | 6-10 h |

Low-value for this learner: exact BPB scoring policy and Adam parity details before first transformer.

## 8. Time-budget recomputation

Assumptions: my stage hours (S0 5-8, S1 40-60, S2 45-65, S3 28-42, S4 65-95, S5 60-90, S6 80-120, S7 55-85, S8 50-80), times 1.15 overhead, divided by 8.5 productive h/week.

| Stage end | Plan weeks | My weeks |
|---|---|---|
| S1 (a) first working project: search CLI with eval, fixture model boundary | 4-5 | 6-9 |
| S2 (b) RAG app, if an API budget exists | 8-12 | 12-18 |
| S3 (c) bounded agent plus MCP slice | 10-15 | 16-24 |
| S7 (d) trained from-scratch LLM with held-out eval | 34-50 | 51-76 |
| S8 everything | 37-54 | 58-87 |

First real LLM call: week 10-14. Recommendation: add a thin slice (bigram sampler, then tiny char transformer) near week 10-14 so generated text arrives before week 25.

## 9. Top 10 fixes, and what to keep

1. Adoption runbook and route switch (B-01).
2. Bind evidence to hashes and commits; min delay; no future dates (H-01).
3. Re-baseline hours; S8 at least 50 h; add rest weeks (H-02).
4. Simplify Week 2; fix Windows newline handling; add an early model win (H-03).
5. Per-task hint-ladder cards with never-reveal sets (H-04).
6. Tutor-only index, mandatory separate learner workspace, remove spoilers (H-05).
7. Repair skill junctions; wire the ladder into `learn` (H-06).
8. Slim evidence to one-line logs; add `waived` state (H-07, M-01).
9. Stall protocol and a one-page learner handbook (M-02).
10. Update MCP task text; fix AGENTS.md counts and `py`/`python3`; make the audit require quizzes (M-04, M-06, M-08).

Keep unchanged: the two-project framing, the evidence-hedged method (`01:9-17`), PRIMM-style session loop, "quiz never counts" rules and the 30 resolver tests, honest qualification of simulated and partial references, CPU configs C0-C2, the Pascal caution, offline-fixture versus live-evidence separation.

## 10. Confidence and limits

- I could not observe a real learner; "quit step" is PLAUSIBLE.
- The laptop was not measured; the benchmark ran on a 16-thread desktop CPU.
- The 1050 Ti was not exercised (the installed torch is CPU-only). Web sources say Pascal's last prebuilt wheel is PyTorch 2.14; the job-market sources are mostly vendor blogs.
- MCP: official page confirms the 2026-07-28 spec; breaking-change details come from secondary sources.
- I did not run the full-repo link check or every lesson's code; only the planning set and the four corrected references.

## 11. Phase 5: prior audits (opened only after sections 1-10 were written)

Opened: `python-to-llm-audit-2026-10-12.md` (A1-A15) and the two implementation specs. I did not open `07-ROUND-TABLE-AND-DECISIONS.md` or the party-mode memories; they add no checkable evidence.

### Prior findings: fixed or not (my reproduction)

| Prior | Status | Evidence |
|---|---|---|
| A1 project stage can vanish in validation | **Fixed** (CONFIRMED) | Candidate `--validate` returns 9 stages and 13 gates; tests reject empty stages |
| A2 progress rows count as completion | **Fixed** (CONFIRMED) | `completed_lessons()` returns empty; categories separate; tests pass. Dead code remains (L-02) |
| A3 advance/retain/close semantics | **Fixed in docs and resolver**; retention still not time-aware (M-01) | `record_state`, protocol table |
| A4 quiz labels "Mastered/Start Over" | **Fixed** | `check-understanding/SKILL.md` Step 6 now subordinates scores |
| A5 new-input is not construction | **Fixed** | `transfer.kind` must be implementation or debug |
| A6 diagnostic stopping rule | **Fixed** | `03:9`, `00` S0 text |
| A7 offsets, freshness, newline | **Fixed on paper, but it created H-03** | The spec now demands hashes, CRLF and Arabic in week 2; I show it is too heavy and Windows-trapped |
| A8 exact-action approval | Fixed in `02:84` | Not exercised (no code exists) |
| A9 graph bridge | Fixed in `02:119` | Not exercised |
| A10-A13 unsafe references | **Fixed by qualification** (CONFIRMED) | Warnings in code and docs; 38 tests pass; algorithms not repaired, as the spec says |
| A14, A15 | Fixed in text; S8 still a placeholder | H-02 |

### Confirmed independently

A1, A2, A3, A10-A13, A15 (S8 optimism), A7 (Windows newline).

### Contradicted or qualified

- Prior "reviewers worked blind" is peer-blinded only (the prior report says so); my pass found problems the fixes introduced.
- Prior "Fixed" implies readiness; the router is now more robust but still forgeable (H-01), which the prior audit did not test.

### Missed by the prior audit

B-01 (plan not operational, route still 11.01), H-01 (forged evidence), H-03 (Windows CRLF trap, no AI for 40 h), H-04 (ladder leakage on small tasks), H-05/H-06 (co-located solutions, dangling skill junctions), H-07 (no waiver), M-04 (MCP spec superseded), M-06 (py/python3, torch missing in base interpreter), M-08 (audit ignores missing quizzes). The prior audit ran no benchmark; mine did (CPU feasibility is fine).

### Status honesty

`spec-implement-python-to-llm-audit.md` still says `status: in-progress` with every task unchecked, while documents 00-06 say "revised to implement the audit". The other spec (`spec-fix-project-mentor-review-findings.md`, status done) concerns a different repository, `D:/AI Projects/ai-engineering-project-lab`, which does not exist on this machine; so the "learner workspace" the plan tells you to locate cannot be found here (supports B-01).
