# LangChain document loaders

Two follow-along notebooks on LangChain data ingestion, copied with outputs cleared on 15 October 2026:

| Notebook | Source repository and commit |
|---|---|
| 01-loaders-july.ipynb | AhmedTElKodsh/LangChain `602619a6` — TextLoader, PyPDFLoader, DoclingLoader, WebBaseLoader, ArxivLoader |
| 02-loaders-august.ipynb | AhmedTElKodsh/LangChain_Ultimate `619fa003` — TextLoader, PyPDFLoader, WebBaseLoader |

`dummy.txt` and `dummy.pdf` are the sample inputs. The August notebook's `speech.txt` was a Wikipedia excerpt and is not copied; any short text file works. AhmedTElKodsh/Learn_Rag `efa41f70` held an empty notebook and is recorded here only for completeness.

Packages used: `langchain`, `langchain-community`, `langchain-docling`, `pypdf`, `bs4`, `arxiv`. Route stage S3 covers loaders properly, with the HR corpus.
