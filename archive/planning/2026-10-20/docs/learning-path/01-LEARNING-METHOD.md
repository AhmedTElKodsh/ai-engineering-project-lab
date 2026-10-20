# A guided project method for Ahmed

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
6. **Transfer:** solve a fresh variation after the teaching example is closed.
7. **Return:** revisit the mechanism after a delay in a different context.

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

Use this hint ladder:

| Level | Help | Example |
|---|---|---|
| H0 | No hint | Implement a changed ranking rule from its contract. |
| H1 | Point to a relevant concept or observation | Inspect the value before and after normalization. |
| H2 | Suggest a decomposition or incomplete pseudocode | Separate tokenization, counting, and ranking. |
| H3 | Show a tiny example for a different input | Demonstrate sorting two unrelated records. |
| H4 | After an attempt, useful hints and an explicit request for more help, supply the smallest tricky fragment | Leave surrounding code/integration to the learner, then request an explanation or adaptation. |

A new topic may be taught with a tiny unrelated worked example before an attempt. Do not reveal the active exercise's complete algorithm through a sequence of hints. Persistent difficulty comes from actual attempts and feedback, with no arbitrary waiting time or failure count. Give a complete solution only when explicitly asked for the complete solution; more hints is not that request. Record partial/full supplied code as worked/generated assistance and assess independence later on a fresh variation. Tutor-written code does not award mastery.

Do not:

- Write the whole learner project and then require you to narrate it.
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
| Chunks retrieved for a question are off-topic | Embeddings, cosine similarity and chunk size | Predict which chunk wins for a new question, then run it. |
| The agent repeats the same tool call | The agent loop, state and stop conditions | Add a budget and explain the trace of a new scenario. |

**Learn as needed, as much as needed.** In the core route a mechanism gets the theory needed to use it correctly with an existing library: plain-language idea, one concrete trace, limits, engineering consequence. Each mechanism ends with a concept check: explain it in your own words, predict the effect of one changed setting, run it and compare. Reimplementing a framework mechanism in plain Python, and the mathematics behind model training, belong to the optional from-scratch track unless the learner asks for them. When borrowing an extract from a local lesson, label the deferred content. Do not claim full-lesson completion for an extract.

## Review and retention

Try reviews approximately one day, one week, and three weeks after first learning. These intervals are scheduling heuristics, not a proven optimum for you. Move an item closer after a failure and farther apart after success.

Use retrieval activities that require production: predict a trace, draw the data flow, derive a small update, write a function from its contract, or debug a changed example. Avoid making review entirely multiple choice. Interleave mechanisms once each is understood; for example, contrast a retrieved passage, a generated answer, and a model's learned weights.

Keep a small review queue: concept, last result, next review, and next fresh task. Limit weekly review to the allocated time unless a blocking mechanism needs repair.

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
Fresh transfer task and result:
Help level / supplied code:
Remaining limitation:
Next review / next action:
```

Store execution and explanation separately. For a changed contract, preserve baseline results and compare the candidate on the same frozen evaluation cases. Identify whether results came from fixtures, local training, or a live provider.

## Working agreement for the eventual tutor

At each session, read the actual learning state, locate the learner project, and resume the unresolved checkpoint. Introduce one mechanism, request one learner action, and wait for its output. Give specific feedback and select the next smallest task. Update completion only after the required evidence exists. The tutor may prepare exercises and review code; it should not silently take ownership of the learning implementation.
