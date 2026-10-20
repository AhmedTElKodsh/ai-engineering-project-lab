# The problem: employees cannot reliably find the right policy

**You are the junior AI engineer on the employee help desk for Nilebyte Solutions,
a fictional company.** Employees ask ordinary questions; the answers are spread
across policies. People Operations wants fewer repetitive searches and fewer wrong
answers. You build the assistant, and explain why each part is needed.

An employee might ask how long carried-over leave remains usable, whether a new
joiner can work remotely, or what a travel receipt needs. A helpful response finds
the relevant policy, gives only the supported information, and points to its source.
A wrong answer can make someone miss a deadline, submit an invalid request, or
see information they should not access. These are fictional practice consequences;
this dataset is not employment or legal advice.

## Why a RAG project fits

The needed facts live in documents, change over time, and need a traceable source.
Retrieval means finding relevant material. Generation means composing a response.
RAG combines them: find appropriate evidence, then give that evidence to a model
to help produce an answer. Installing a vector database does not establish that
the answer is supported, and a source citation alone does not establish support.

Begin with the cheapest useful behavior. A search result with a passage and its
source may already help. A generative answer is justified when it makes the retrieved
material easier to use without inventing conditions. For a tiny corpus, supplying
all its passages is a legitimate comparison; search should later earn its complexity
through relevance, eligibility, context size or cost.

This architectural distinction follows the official
[retrieval overview](https://docs.langchain.com/oss/python/deepagents/retrieval):
search and retrieve-then-generate pipelines are useful before agent-directed retrieval.
It does not imply that this specific learning sequence has proven effectiveness.

## Users and boundaries

| Person | Needs | Boundary |
|---|---|---|
| Employee | Understand a published rule and locate the source | Policy text cannot establish personal balances or approve a request |
| People Operations reviewer | Check why an answer was given | The trace must identify source, version and actual retrieved evidence |
| Learner | Build, diagnose and change the system | The tutor does not implement the active solution |

The first product serves a fictional Cairo employee on the fixed fixture date
`2026-09-24`. It answers general published policy questions from an explicit
allowlist. Later versions receive trusted role, region and date context. A question
cannot choose its own permissions. A response must distinguish a general rule from
an eligibility judgment about a particular employee.

## First useful release

Input: one question and the tiny JSON corpus supplied in this pack.

Output: a relevant passage plus source and section, or an explicit no-supported-answer
result. Once generation is introduced, the response adds a concise supported answer
with evidence references. An unresolved question asks for a relevant missing detail
or abstains; a confident guess is a failure.

Start with one normal question and one unsupported question. Do not build a website,
upload service, cloud deployment, chatbot memory, vector database or agent before
the corresponding release creates a need.

## Problems that arrive later

| Observed user problem | New engineering question |
|---|---|
| Same intent expressed with different words gets no result | How can retrieval use meaning as well as exact words? |
| A useful answer is buried in a long document | What should a retrievable unit contain, and how does it retain its source? |
| Two versions give different rules | Which version applies to this date? |
| A retrieved document belongs to another role or region | How are eligible sources selected before ranking? |
| A passage contains instructions aimed at the assistant | How does the application keep source content from becoming authority? |
| A change helps two examples but breaks others | What comparison would justify keeping it? |
| “Does that apply to me?” lacks necessary context | What should be clarified, and what conversational context is safe to use? |
| “How much leave do I have?” asks for personal state | Which authenticated lookup is needed beyond policy retrieval? |

## Scope of success

The core outcome is a locally reproducible, evaluated policy RAG assistant the
learner can explain and modify on a fresh task. Keep quality, retrieval, refusal,
security, latency and cost visible separately. Local fixture performance establishes
only behavior on that fixture. Live-provider quality, learner independence, delayed
retention and deployment each need their own evidence.

Optional tools can later read a fake HR balance and prepare a local draft request.
Real HR systems, external writes, private client content, production operations,
model training and fine-tuning are outside the starter product.
