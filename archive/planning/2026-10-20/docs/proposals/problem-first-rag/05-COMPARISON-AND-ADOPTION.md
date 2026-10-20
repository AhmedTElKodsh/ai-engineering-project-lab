# Comparison with the existing plan and adoption map

## What the current plan actually says

The existing plan is **already project-first in its stated method**. The
[learning method](../../learning-path/01-LEARNING-METHOD.md) begins each unit with
a project question, teaches foundations as needed, and targets a recognizable
feature in the first sessions. The
[project README](../../../projects/grounded_support_assistant/README.md) opens with
a support-team quest. It would be inaccurate to describe it as pure concept lectures.

The tension is in the sequence. The
[roadmap](../../learning-path/02-PROJECT-ROADMAP.md) assigns 4–6 hours to S0,
20–30 to the Python floor and 20–30 to LLM calls before S3 RAG. Those ranges total
44–66 planned hours before S3 starts, not an observed wait time. The
[first four weeks](../../learning-path/04-FIRST-FOUR-WEEKS.md) opens model calls in
week four. Practice shifts from a support handbook to HR policies, while every
stage also applies to private Mushir. Several frameworks require rebuilds.

The user's alternative can make the practice more consistently driven by one
customer problem. It changes when and why mechanisms enter, rather than discarding
the current ownership and assessment safeguards.

## Three approaches

| Approach | Benefit | Cost/risk | Judgment |
|---|---|---|---|
| Keep current ordering; improve the stories | Least maintenance; broad foundation gates remain intact | The long foundation block and corpus switch still shape the experience | Useful low-change option, but only partly answers this request |
| **Reorganize one cumulative policy assistant into problem-driven releases** | Earlier useful behavior; new mechanisms answer visible limitations; reuses existing data | Stage contracts and library placement must be reconciled; small early gates can omit important skills if left unchecked | **Recommended design to pilot** |
| Give a complete chatbot template and learn by modifying it | Fast runnable demo | Inherited integration can conceal gaps; easy for the tutor to finish the project; difficult authorship attribution | Keep a reference for observation, not the primary learner path |

This recommendation is a design judgment, not a measured claim that problem-first
teaching works better for this learner. The current route also intends guided
practice; the proposal must prove a better experience through a pilot.

## Side-by-side comparison

| Dimension | Current documented plan | Proposed sequence |
|---|---|---|
| Opening | Quest, refusal, local CLI and full Mushir trace | One employee question and displayed evidence; local trace after teaching boundaries |
| Main domain | Support handbook at S1–S2, HR at S3–S6, private application every stage | Tiny HR fixture from the start, expanding within one domain; private work remains separate |
| Python | Dedicated 20–30-hour floor before S2 | Minimum safe boundary for the current feature; broader skills revisited at their actual use |
| First sourced generative path | LLM at S2; automatic RAG at S3 | R1 lexical retrieval feeds R2 generation; fake first, explicit live proof later |
| Need for embeddings | S3 concepts and build requirements | Observed different-wording failure motivates an R3 comparison |
| Parsing | Multiple formats within S3 | Clean supplied passages, then full text, then one format at a time |
| Access/version handling | Strong general engineering rule, but explicit build slice appears in S4 | Safe allowlist initially; selection enforced before any broader/restricted indexing |
| Frameworks | LangChain/LlamaIndex rebuilds and later SDK comparisons | One main pipeline; bounded same-behavior comparisons with a keep/defer/drop decision |
| Assessment | Execution, explanation, independent transfer and delayed retention | Preserve all four; product release labels never substitute for stage proof |
| Agents | S5–S6 remain part of the full route | Product extension after useful RAG; still required for full route if that route remains selected |
| Theory | Already says “learn as needed, as much as needed” | Apply that rule to the actual sequence; teach before assessment, no theory-free shortcuts |
| State | One route, one ledger, derived views | Preserve; no R0–R9 state machine or second tutor |

## Adoption contract: change the owners, not their authority

Do not activate this pack by pasting a tutor prompt. A separate authorized maintenance
task must prepare a consistent candidate in the existing owners, validate it, and
show the diff. Keep S0–S6 identities so historical observations remain interpretable.
The proposed target grouping is below. It is an allocation design, not a one-to-one
proof migration. Re-estimate hours after pilot evidence instead of preserving old
hour ranges under changed responsibilities.

| Existing stage ID | Proposed release coverage | Necessary owner change |
|---|---|---|
| S0 | R0 | Local fallback and one bounded trace; configuration repair is separate; reconcile private application exception |
| S1 | R1 | Load/validate records, minimum Python/testing/Git and library-based lexical retrieval; defer broader HTTP/async coverage to its provider/batch use |
| S2 | R2 | Retrieve-then-answer, fake/live boundaries, structured validation, bounded failure policy, secret-safe config and tracing |
| S3 | R3–R4 | Dense retrieval, complete-text/mixed-format ingestion, chunking, index lifecycle; remaining Python/HTTP/batch gaps explicitly owned here or S2 |
| S4 | R5–R7 | Eligibility, conflict, security, multilingual evaluation, measured improvements and bounded follow-up handling |
| S5 | R8 | Fake HR tools, deterministic workflow, LangGraph comparison, approval/recovery, bounded MCP |
| S6 | R9 | Integration/reproducibility/defense; state/memory and workflow-versus-agent comparison when R8 is included |

Before any stage can close, every critical capability in its revised contract needs
its own qualifying evidence. Moving a requirement to a later use must give it a
named owner and exit; it cannot disappear between stages. R9 is an integrated
defense, not a substitute for earlier capability checks or delayed retention.

### File changes for a future adoption task

| Owner | Required reconciliation |
|---|---|
| `learning/route.json` | Preserve stage IDs; revise title/next action/effort and scoped contract dependencies consistently; never infer readiness from this pack |
| `docs/learning-path/02-PROJECT-ROADMAP.md` | Replace concept-block ordering with revised stage/release acceptance; retain explicit capability exits, live boundaries and private application decisions |
| `docs/learning-path/08-LIBRARY-MAP.md`, `TOOLING.md` | Move small BM25 use to S1; direct SDK before LangChain; define bounded LlamaIndex/other framework comparisons; select tracing authority consistently |
| `docs/learning-path/04-FIRST-FOUR-WEEKS.md` | Replace a fixed pre-LLM foundation block with problem slices, review and repair; estimate from measured pace |
| `docs/learning-path/03-SKILLS-AND-MASTERY.md`, `learning/PROTOCOL.md` | Preserve authorship/independence; bind critical capability and contract coverage; disclose supplied-case exposure |
| `project-context.md`, project README | One HR domain from the start; inherited lexical app is reference; actual implementation claims remain narrow |
| `.agents/skills/project-mentor/SKILL.md`, `AGENTS.md` | Merge only necessary tutor changes into the single mentor; reconcile the S0/private exception and startup; no copied skill tree |
| `resources/corpora/hr-policy/README.md`, `data/README.md` | Declare early clean-source/JSON teaching use, later corpus-only parser evaluation, and provenance/family grouping |
| Eval selectors, gates, CI and state helper/tests | Implement only the authorized integrity/evaluation changes; verify actual consumers and negative controls |
| `LEARNING.md`, `learning/state.json` | Regenerate through the existing writer/refresh only after valid owner changes; never edit manually |

The optional [from-scratch specification](../../learning-path/05-LLM-BUILD-SPEC.md)
remains a separate track. This proposal adds no hand-built embedding, vector-store,
transformer or model-training requirement to the core route.

### Relation to the existing improvement plan

The [merged improvement plan](../../review/IMPROVEMENT-PLAN-2026-10-20.md) is an
additional proposal, not an implemented prerequisite checklist this task has passed.
Use its U/P identifiers in the authorized adoption work rather than duplicating it:

- Before new mastery decisions: verify exposure/freshness repairs (P0-1), relevant
  contract dependency binding (P0-2), the stage's capability representation (P1-A)
  and isolated mentor pilot (P1-B). P0-3 supplies the S0 fallback proposed here.
- Before claiming clean RAG release evaluation: complete/verify P2-1 split selectors,
  applicable gates and scoring policy; verify P2-2's support negative control.
- Bound comparisons per P2-3; implement early eligibility/index lifecycle per P2-4.
- Preserve S5 authorization/recovery and S6 defense requirements from Phase 3.

Supported practice can proceed without a mastery claim. This planning pack does
not fix local failing tests or authorize broader repairs.

### Private application decision

For the proposed core product, no private checkout is needed to start R0/R1.
For the **current route**, per-stage Mushir application remains required unless its
actual owners are explicitly revised. During adoption, choose whether to keep those
applications within each stage or make them a separate selected transfer branch;
do not silently omit them because public RAG works. Default proposal: retain them
with the bounded S0 fallback. Private text stays in its private checkout.

## Pilot and adoption evidence

First validate the revised tutor on isolated synthetic sessions: unfamiliar term,
correct concept plus syntax error, stuck learner asking for hints, explicit complete
solution request, confident wrong explanation, forgetting, stale state and no provider.
Do not manufacture real learner records from these transcripts.

Then observe the first learner R0–R2 sessions. Record time to a useful result,
coding/setup/repair time, hints/code supplied, ability to explain evidence boundaries,
and an independent fresh modification after instruction. Revisit a taught mechanism
after the retention delay. Compare against the current plan's documented targets;
there is no observed control cohort, so this is not a causal experiment.

Keep or revise the design based on observed independence, clarity and manageable
task size. Faster demos with lower independence do not count as an improvement.
Adoption is complete only when owners agree, checks pass, unchanged history is
verified and the resumed single mentor selects the correct unresolved checkpoint.
