# A guided project method for Ahmed

Revised 14 October 2026 to implement the [independent audit](../review/from-scratch-audits/python-to-llm-audit-2026-10-12.md). The audit remains the historical reviewed snapshot; this package and the project route were corrected without learner completion awards.

Prepared 11 October 2026. Design target: basic Python knowledge, 10 hours/week, CPU first, cumulative AI engineering and model construction.

## Why this method

Use a real project to supply the purpose, small guided examples to introduce unfamiliar mechanisms, and independent change tasks to demonstrate learning. The recommendation is an instructional design inference for your case. No cited study proves that this exact roadmap is the best method for an adult learning AI engineering.

| Evidence | Finding relevant to this design | Limit and design consequence |
|---|---|---|
| Dunlosky and colleagues' review | Practice testing and distributed practice received high utility ratings across many learning conditions. | General learning research, not a timetable for AI engineering. Use retrieval and repeated sessions; the exact review intervals below are adjustable. [Publisher's account of the review](https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html) |
| Sentance, Waite, and Kallia, PRIMM | A structured Predict, Run, Investigate, Modify, Make approach was evaluated in secondary-school programming; the study reported better post-test performance for the intervention group. | School learners and classroom support differ from your circumstances. Adapt the progression, then measure your transfer. [Author-hosted paper](https://primmportal.com/wp-content/uploads/2020/10/teaching-computer-programming-with-primm-a-sociocultural-perspective.pdf) |
| Bastani and colleagues | In a high-school mathematics experiment, unrestricted AI assistance improved practice performance but reduced later unaided performance; a tutor with learning safeguards largely mitigated that harm. | This does not establish the same effect size in Python. It motivates separate assisted practice and independent checks. [Author-hosted paper](https://hamsabastani.github.io/education_llm.pdf) |

These findings support a combination of purpose, guidance, practice, and testing. They do not justify treating project completion, tutorial viewing, or a tutor's explanation as proof of mastery.

## The learning unit

Each unit answers one project question. Examples: how to count repeated words, how to rank passages, why a gradient changes a weight, or why a token cannot attend to the future. Units should usually fit one or two two-hour sessions; difficult mathematical mechanisms may need more.

1. **Frame:** state the user-visible problem and one success criterion.
2. **Predict:** inspect a small input or example and predict a result before running it.
3. **Run and investigate:** compare the result with the prediction; trace values, shapes, or state.
4. **Build:** implement or change one bounded component yourself.
5. **Check:** test a normal case and a failure case; explain the result.
6. **Transfer:** independently implement a fresh small contract or repair an unfamiliar bug after the teaching example is closed. A changed-input rerun or tracing task does not establish authorship.
7. **Return:** revisit it after a delay with an independent implementation/debug task in a different context; record assistance separately.

Execution, explanation, and independent transfer establish readiness to advance. Schedule retention visibly; close the stage only after all required gates are ready and retained. Follow [the state protocol](EVIDENCE-PROTOCOL.md), not quiz labels or progress-row presence.

The project supplies the destination, but the tutor supplies enough structure to make the next step reachable. Reduce support after successful independent work. Restore support when a specific gap appears.

## A two-hour session

| Minutes | Activity | Expected evidence |
|---|---|---|
| 0–10 | Retrieve a previous concept or predict a result | A learner answer before feedback |
| 10–30 | Understand today's mechanism through one small example | A traced value, diagram, or shape calculation |
| 30–95 | Learner implementation with bounded hints | A function, refactor, bug fix, or experiment |
| 95–110 | Run tests and explain one failure or tradeoff | Command/result and a short explanation |
| 110–120 | Save state and choose the next small action | Evidence note, help level, and next checkpoint |

This is a default allocation. A day spent diagnosing a difficult bug can still be successful if the evidence identifies the cause and a smaller next action. Avoid compensating for a hard session by adding several new topics.

Monday introduces or repairs a mechanism. Tuesday implements it. Wednesday extends it to unfamiliar data. Thursday integrates or tests it. Friday contains review, an independent transfer task, and planning. On a 10-hour week, approximately 6 hours are learner coding/debugging, 2 hours guided concepts, and 2 hours testing/review/documentation; adjust as the evidence demands.

## Tutor conduct

The tutor starts with the current project problem and your latest attempt. It asks one concrete question at a time during active tutoring. It uses plain words before terminology and introduces formulas alongside a numerical example. It distinguishes a conceptual misunderstanding, an implementation bug, and an environment problem.

**Learner clarification, 11 October 2026:** guide the learner to the solution; do not write the active exercise's solution by default. Explain the problem and one mechanism, ask for a prediction or a small attempt, then wait for the actual answer, code, or error. Reference solutions may inform the tutor's preparation, but their availability does not authorize revealing them during the exercise.

Use this hint ladder:

| Level | Help | Example |
|---|---|---|
| H0 | No hint | Implement a changed ranking rule from its contract. |
| H1 | Point to a relevant concept or observation | Inspect the value before and after normalization. |
| H2 | Suggest a decomposition or incomplete pseudocode | Identify tokenization, counting, and ranking responsibilities; leave the active logic for the learner. |
| H3 | Show a tiny example of a different problem | Demonstrate a sorting concept with unrelated records without solving the active ranking task. |
| H4 | Give the smallest tricky part after persistent difficulty and a request for more help | Explain or supply a single blocked update or shape transformation; the learner writes and integrates the surrounding logic. |

Use H4 when a learner attempt and useful hints have not resolved the specific blocker and the learner explicitly asks for more hints or help. Inspect what they tried and what remains confusing. Do not impose an arbitrary waiting time or failure count. A new concept may be taught with an unrelated small example before an attempt, without revealing the active solution.

After H4, ask the learner to explain or adapt the supplied part, implement the remaining work, and show their next result. Do not turn several partial hints into a complete supplied solution. A request for more hints is not permission to finish the exercise. Provide a complete solution only when the learner explicitly requests the complete solution.

Record H4 or a requested complete solution as assisted work. Neither is independent evidence. Assess ownership later with a fresh variation rather than immediate reproduction of the supplied answer.

Do not:

- Write the whole learner project and then require you to narrate it.
- Reveal the active solution, finish its function, or edit learner implementation files merely because the learner is stuck or asks for another hint.
- Turn confusion into a wrong-answer grade before clarifying the question.
- Ask you to explain a function, trace, or term you have not seen or been taught.
- Treat successful hosted inference as evidence that you understand training.
- Mark a stage complete because the tutor generated a passing solution.
- Demand full completion of every prerequisite phase when a bounded project bridge is sufficient.
- Skip a blocking gap because an API or framework makes the demonstration look successful.

## Just-in-time foundations

When a gap blocks the next task, identify its smallest teachable mechanism. Introduce a short bridge, apply it, then return to the project. Examples:

| Observed difficulty | Bridge | Return task |
|---|---|---|
| A word count resets on every occurrence | Dictionary lookup/update and loop state | Count words in a new sentence. |
| Retrieval scores depend on document length | Normalization and vector similarity | Compare two passages with repeated words. |
| A probability table does not sum to one | Counts, normalization, and smoothing | Build an unseen-context fallback. |
| Loss goes up after an update | Derivative sign and gradient descent | Calculate one weight update by hand. |
| Attention tensors have the wrong dimensions | Matrix multiplication, transpose, broadcasting | Annotate every intermediate shape. |

Math remains required. Sequence it according to mechanisms: vectors for similarity; probability and logs for prediction; derivatives and the chain rule for learning; numerical stability for softmax; matrix calculus intuition for attention. When borrowing an extract from a local lesson, label the deferred content. Do not claim full-lesson completion for an extract.

## Review and retention

Try reviews approximately one day, one week, and three weeks after first learning. These intervals are scheduling heuristics, not a proven optimum for you. Move an item closer after a failure and farther apart after success.

Use retrieval activities that require production: predict a trace, draw the data flow, derive a small update, write a function from its contract, or debug a changed example. Avoid making review entirely multiple choice. Interleave mechanisms once each is understood; for example, contrast a retrieved passage, a generated answer, and a model's learned weights.

Keep a small review queue: concept, last result, next review, and next fresh implementation/debug task. Failed retention triggers targeted repair and rescheduling, preserving earlier evidence. Limit review to the allocated time unless a blocking mechanism needs repair. During S4–S7, rotate one short assistant trace, bug, or contract change into the existing Friday review allocation every one or two weeks. Tracing retains familiarity; independent changes are assessed separately. This uses existing review time, not added hours.

## Motivation without overload

The first feature should solve a recognizable problem within the first few sessions. Increase only one main source of difficulty at a time: larger data, a new Python mechanism, a new learning algorithm, or a new system boundary.

When an applied-AI block needs credentials or network access that are not available, work on parsing, contracts, retrieval, fixtures, and evaluation. Label these as offline evidence. Move to the next local learning block if necessary, retain the live evidence gate, and return later. A mocked response does not establish real model quality.

If progress stalls across two sessions, shrink the task and diagnose the cause. If it stalls across a week, re-estimate the stage and remove optional features. Do not solve a planning problem by adding another course or framework.

## Evidence note template

```markdown
Date:
Stage / slice:
Learner project path:
Question or contract:
Prediction:
What I implemented:
Command and observed result:
Code revision or file hash:
Explanation in my own words:
Fresh implementation/debug task and independent result:
Evidence category / readiness / completion eligibility:
Retention state / due task / delayed independent result:
Help level / supplied code:
Remaining limitation:
Next review / next action:
```

Store execution and explanation separately. For a changed contract, preserve baseline results and compare the candidate on the same frozen evaluation cases. Identify whether results came from fixtures, local training, or a live provider.

## Working agreement for the eventual tutor

At each session, read the actual learning state, locate the learner project, and resume the unresolved checkpoint. Introduce one mechanism, request one learner action, and wait for its output. Give specific feedback and select the next smallest task using the hint ladder. When persistent difficulty and a request for more help justify a partial reveal, supply only the blocker and return implementation to the learner. Update completion only after the required evidence exists. The tutor may prepare exercises and review code; a full active solution requires an explicit request for that full solution.
