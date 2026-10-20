# Data and evaluation contract

## Data choice

Use the repository's already supplied **synthetic** employee policies. This avoids
making dataset discovery, licensing or a large download the first learning obstacle.
No external dataset was fetched. Synthetic fixture realism is limited; it does not
establish production performance or real employment rules.

The delivered [starter corpus](data/starter-corpus.json) contains nine short records
from three existing policy families: leave, remote work, expenses. Its record text
is retained verbatim from selected clean authoring sections. Source pointers, policy
identity and metadata accompany it. Record boundaries are supplied scaffolding,
not evidence that the learner has implemented chunking or parsing.

The fixture date is `2026-09-24`, matching the original corpus manifest. A later real
calendar date must not silently change fixture expectations. The trusted starter
context is a Cairo employee asking about current general published policy.

The subset omits many rules. An omitted rule is unavailable in this release, not
false. A source pointer is citation/provenance metadata, not permission to silently
load every policy. Only the selected fixture text is evidence in R0–R3.

## Starter record fields

| Field | Meaning |
|---|---|
| `id` | Stable starter passage ID, independent of list position |
| `doc_key`, `doc_family`, `policy_id` | Original document and grouping identity |
| `title`, `section`, `version` | Human citation and version information |
| `effective_from`, `effective_to`, `status` | Applicability at a trusted reference date |
| `allowed_roles`, `regions`, `language` | Trusted ingestion metadata; never inferred from the question |
| `source_path`, `source_section` | Repository-relative original authoring source and section |
| `text` | Actual selected evidence available to this release |

No embeddings, chunking implementation, retrieval scores, solution functions or
learner progress fields are supplied. Whole-record hashes are useful to freeze a
run, but do not establish authority or factual entailment.

## Expansion ladder

| Release | Data | New difficulty | Boundary |
|---|---|---|---|
| R0–R3 | Supplied nine-passage JSON, English, three families | IDs, search, grounded responses, paraphrase | Clean preselected records; no parser/chunker claim |
| R4a | Full Markdown authoring sources for these same dev families | More sections and chunk boundaries | Explicit teaching exception: clean sources may be ingested here |
| R4b | Matching files from original `data/corpus/` | PDF/DOCX extraction and tables | Compare extracted text with authoring source; do not ingest both copies |
| R5a | Version pairs and trusted role/region metadata | Eligibility and historical intent | Pre-ranking selection must be tested before admitting these files |
| R5b | Conflict pair, FAQ HTML, Arabic sources | Conflict, injection and cross-language support | Add one class at a time with explicit failure cases |
| R6–R7 | Larger declared development pool | Comparative eval and conversation | Freeze manifests and selectors; keep unseen pools separate |
| R8 | Fake HR seed and agent scenarios | Personal-state lookup and local draft actions | Synthetic effects; separate authorization and agent gates |

Original corpus location:
[resources/corpora/hr-policy](../../../resources/corpora/hr-policy/README.md).
Its [manifest](../../../resources/corpora/hr-policy/data/corpus_manifest.json) owns
original file metadata. The early source-reading exception above is a **proposed**
adoption change: the existing corpus contract currently says ingest `data/corpus/`
and use `data/policies/` as parsing ground truth. Update that owner if adopted.
Do not treat the starter JSON metadata as a second master catalog for the full corpus.

When the starter allowlist becomes the full corpus, filter trusted eligibility
before retrieving top-k, and before sending text to any model or external trace.
The tiny allowlist is an early scope boundary, not proof of a general access filter.

## Four pools, four different claims

| Pool | Who may inspect it | Claim it can support |
|---|---|---|
| Displayed teaching examples | Learner and tutor | Supported comprehension/practice |
| Exposed development cases | Developer, tutor and learner | Regression/diagnostic behavior on known cases |
| System release holdout | Scoped evaluator at release time | Untuned system behavior on that frozen pool |
| Learner transfer/retention | Assessor supplies one fresh task after teaching | Independent ability on that task |

The twelve [development cases](data/dev-cases.json) and every example in this pack
are **exposed**. They are not hidden tests or fresh learner assessment. Their answers
are provided deliberately for development. The three source families and related
paraphrases belong to development. Renaming a case or changing its wording cannot
make it fresh.

This pack supplies no release holdout and no scored learner assessment. A future
maintainer/evaluator must partition source/document families before generating
questions, reserve unseen families/material, validate selectors, then freeze the
release artifact and keep its answers out of tutor/developer prompts. Use separate
unfamiliar fictional material for independent transfer. Related versions, extracts
and translations stay in the same grouping family.

With only three starter families, do not claim a broadly representative disjoint
release benchmark. Expansion must add the source groups needed for its claimed
coverage. If a capability cannot be covered without same-corpus cases, label that
narrower claim and revise the owner contract explicitly. A small test set cannot
establish broad statistical superiority.

The current HR evaluation asset is **not automatically a clean holdout**. The
[existing improvement plan](../../review/IMPROVEMENT-PLAN-2026-10-20.md) records
overlapping selectors and other issues. Those are reported prior findings, not
repairs verified by this planning task. Repair and test actual selectors before
using them for a new release claim. If a release case informs debugging, expose
its related family and replace the reserved coverage before claiming unseen results.

## Development response contract

An implementation may choose its internal names, but the observable response needs:
question, status (`answer`, `clarify`, `abstain`), answer or clarification text, and
evidence IDs/citations. Diagnostics record eligible and retrieved IDs separately
from cited IDs. Unsupported/clarification output must not contain invented facts.

Each dev case declares expected behavior, support IDs, required facts, forbidden
claims and conditions. These are a human-readable rubric, not an implemented judge.
Equivalent supported wording is acceptable. Do not score correctness by substring
matching a number: distinguish decimals, units, signs, dates, percentages and Arabic
digits. A generated answer can cite a valid ID and still fail factual support.

## Minimum measurement

- Retrieval: hit@k and MRR on answerable cases with explicit denominators and gold
  relevance sets. Report failures; a partial evidence set may retrieve a relevant
  passage while still being insufficient for an answer.
- Answering: required facts/conditions, unsupported claims, evidence correctness,
  completeness and status decision, reviewed separately from retrieval.
- Unsupported questions: refusal accuracy and leakage, not MRR.
- Trust: version/access/conflict/injection checks when those behaviors enter scope.
- Operations: per-case latency and call/token cost, corpus/index/prompt/model/code
  versions and errors. A fake has no observed live-provider latency/quality.

Start with a tiny case table and deterministic fake failure tests. Later choose one
evaluation library; do not substitute its aggregate score for inspecting errors.
Hard gates block unconditionally. Set practical comparison tolerances before the
candidate run; analyze paired outcomes and report uncertainty. A non-significant
test is not proof of equivalence. A human-calibrated judge may assist, with false
acceptance of unsupported claims reviewed separately.

## Tool and assessment separation

Applicable gates follow behavior: basic RAG does not need leave-request or screening
success. A tool-enabled assistant must also pass applicable retrieval/leakage gates
for its policy-search output. Screening remains an unrelated optional branch.

Freeze the tested tree/config and preserve raw errors. Add one meaningful negative
control, such as an invented source ID or an extra unsupported sentence, showing
that the check catches a real fault. Maintenance checks and synthetic tutor pilots
remain maintainer evidence; neither awards learner independence or retention.

## Current technical references

Checked 20 October 2026; these explain mechanisms, not guaranteed model/API versions:

- [Sentence Transformers semantic search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html): meaning-based retrieval and query/document encoding considerations.
- [LangChain semantic search tutorial](https://docs.langchain.com/oss/python/langchain/knowledge-base): loaders, splitting, embeddings and search building blocks.
- [Original RAG paper](https://arxiv.org/abs/2005.11401): background on combining external retrieval with generation. This practice project does not reproduce its training method or benchmark claims.

Before installing a model or library, verify current official documentation,
installed/locked versions, license, hardware needs and downloads. No live call or
dependency installation is authorized merely because a reference appears here.
