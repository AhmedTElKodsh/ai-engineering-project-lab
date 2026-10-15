# HR policy corpus (Nilebyte Solutions, fictional)

The realistic practice corpus for route stages S3–S6. Every company, person, ID, email and salary here is invented. Imported on 15 October 2026 from AhmedTElKodsh/HR-Agent at commit `e5ab6c4a275d1ca0fe053ed56c0d19053069d7ff`; the learner owns that repository, and its milestone plan and task catalog are kept under archive/source-state/hr-agent for history only.

| Path | Used in | What it is |
|---|---|---|
| [data/](data/README.md) | S3–S6 | 21 corpus documents in PDF, DOCX, HTML and Markdown (two in Arabic), their clean authoring sources, a corpus manifest with versions/roles/regions, a fake HR system, leave rules, a job rubric and eight résumés |
| [eval/](eval/README.md) | S3–S6 | 125 golden RAG questions in 11 slices, 20 agent scenarios, screening expectations, 32 counterfactual résumés and release gates |
| [docs/agent_tools.md](docs/agent_tools.md) | S5 | Tool contract for the HR agent: identity, the confirm flow and failures |
| scripts/ | maintainer | `validate_data.py` checks the data; `build_corpus.py` and `make_counterfactuals.py` regenerate generated files and need `reportlab`, `python-docx` and `pillow` |

The data is built to fail naive systems on purpose: superseded policy versions, role- and region-restricted documents, two active documents that disagree, a hidden prompt injection in the FAQ page, tables and a scanned PDF. Treat `gates.json` held-out IDs as release checks only; never put eval questions into prompts or examples.

This is fixture material, not learner work. Stage progress comes only from the learner's code and records under the route.
