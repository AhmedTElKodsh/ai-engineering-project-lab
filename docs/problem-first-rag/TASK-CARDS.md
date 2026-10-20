# Problem-first task cards — consult only at the eligible stage

These are **supplementary prompts** tied to the existing roadmap. They do not create new stage IDs, grades or acceptance gates. Start with **FIRST-SESSION.md** and the currently unresolved capability; do not hand the learner all cards as a task list.

| Stage | First user-visible failure | One bounded learner change or explanation | Verify on |
|---|---|---|---|
| S0 | Inventing a leave deadline can mislead an employee | Explain harm, supported clause and source; later trace manual input -> evidence -> output | pf-leave-carryover and a different subsequent displayed passage |
| S1 | Support cannot reliably find a policy clause across files | Define a small record contract; implement a loader before BM25 ranking; preserve ID, section, source and Unicode | Normal, empty, malformed and tie cases; mutation-sensitive pytest |
| S2 | A model may attach a valid citation to an unsupported sentence | Specify the structured answer/clarify/abstain contract; test fake valid, malformed, unknown-ID and unsupported-claim proposals | A deterministic fake; a separately authorized, budgeted live call and trace later |
| S3 | Worded-differently questions and mixed formats produce missed or incomplete passages | Isolate a missed paraphrase; compare lexical with semantic retrieval, then parsing/chunking/index lifecycle on fixed cases | Hit@k/MRR for answerable questions; role/region/date eligibility BEFORE retrieval/ranking |
| S4 | The returned policy is old, regionally inapplicable or contradicted | Add a negative eligibility/conflict/conversation case before optimizing search | Security hard gates and paired case-level comparison, not average alone |
| S5 | The employee asks for *their* balance or a leave request draft | Design read-only fake lookup, trusted actor, validation and approval-bound simulated draft | 20 original scenarios plus tamper/replay/unknown-write controls |
| S6 | Another engineer cannot reproduce or defend a release | Reproduce, inject a failure, compare workflow and agent only when useful | Local clean run, tests/CI, manifests, cost, traces and independent defense |

## First coding slice (S1 only after S0 requirements)

**Problem:** one of nine supplied policy passages cannot be found reliably from the current source collection.  
**Input:** the official **projects/grounded_support_assistant/data/starter-corpus.json**, which already contains supplied record boundaries.  
**Contract to design before code:** preserve supplied stable IDs, document/section/version and original Unicode text; decide empty/malformed-file behavior; return a clear error rather than inventing source data.  
**Normal and negative checks:** one known ID resolves to its published text, and a missing or invalid record is rejected or reported by a documented policy.  
**Ownership:** the learner implements the reader, tests and explanation. This task card intentionally includes **no function solution** and does not bypass the S1 stage blockers. Follow with **rank_bm25** only after the records contract is understood.

Do not treat the inherited **app.py** Acme lexical implementation as the new learner's HR search code. It can be inspected as prior art, but it is not proof of authorship. Other stages and integration with private Mushir require their named prerequisites and authorization.

## Evidence hygiene

A tutor captures the learner's actual answer/patch, assistance level, command/output when available, revision, a fresh non-rehearsed variation and the next unresolved capability. Use the existing revision-checked evidence writer only after local validation and an authorized, truthful observation. No grading from generated files alone.
