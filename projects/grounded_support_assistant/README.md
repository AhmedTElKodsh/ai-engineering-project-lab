# Grounded Support Assistant

## Quest briefing

You join a support team with an approved handbook. Your job is to build software that finds useful passages, answers only what the sources support, and refuses or asks for clarification when necessary. Wrong account/billing guidance creates rework and user harm. Start with a small local corpus; no AI vocabulary or provider account is assumed.

The inherited prototype is a starting observation. The learner has not yet demonstrated its purpose or implementation. First explain the refusal risk, then use a displayed [handbook excerpt](data/handbook.md) to identify a supported fact and its source. Actual clear evidence can satisfy these ideas across as many turns as needed; existing code or a mentor explanation does not satisfy them.

## Current behavior and limitations

The app ranks English sections by exact non-stopword overlap and returns one whole section when at least two terms match. JSON contains question, answer, citations and abstained. The [original evaluation asset](eval/cases.json) has twenty cases: nineteen currently pass and one paraphrase is a strict expected failure. The [new challenge set](eval/challenges.json) captures unsupported overlap, multiple intents and injection-like phrasing found by independent review. Those failures are deliberate visible improvement work, not proof of reliable supported answers.

A source citation indicates the returned passage's origin; it does not establish that it answers every requested fact. This baseline has no semantic model, authority-bearing tool, provider or full RAG generation. Its corpus language is English; nonmatching language input should produce abstention, and multilingual retrieval is later scope. Do not call lexical search a trained LLM.

```powershell
uv run python projects/grounded_support_assistant/app.py "How long is an export link valid?"
uv run pytest projects/grounded_support_assistant -rxX -q
```

## Cumulative learner-owned releases

The single [S0–S6 roadmap](../../docs/learning-path/02-PROJECT-ROADMAP.md) owns the sequence. S1 makes this program typed, tested and configurable; S2 puts a real model behind it with structured output and tracing; S3 turns it into a RAG assistant over the [HR policy corpus](../../resources/corpora/hr-policy/README.md), built with libraries and then with LangChain and LlamaIndex; S4 deepens retrieval and evaluation; S5 adds tools and a LangGraph agent; S6 combines them into an evaluated agentic system. Each stage is also applied to Mushir in its own private checkout.

The `model/` directory is reserved for the optional from-scratch track and is not part of the core route.

## Tool-authority requirements at S5

Agent tools are allowlisted by name with validated arguments; trusted application context supplies actor, corpus and any internal object IDs. An untrusted model proposal cannot authorize a write. Bind approval to exact target/arguments/hash and an independent approver, revalidate before execution, and reject replay, stale versions, traversal, unknown IDs and changed parameters. A resolved task either explicitly rejects follow-up or starts a new bound run; it never silently accepts a message with no legal state transition.

Start with local simulated effects. Test bounded steps/timeouts and restart, duplicate action IDs, failed writes and unknown outcomes. Claims about real deployment or side effects need separate observed evidence.

## Evaluation hygiene

Keep development cases separate from unseen transfer and final held-out data. Split by source/document before generating related examples, fit vocab/statistics on training only, and compare against a frozen baseline. Report supported/unsupported and multilingual limitations, raw errors, latency and cost. Test a meaningful mutation or counterexample; a green suite that also accepts a broken guard does not protect that guard.
