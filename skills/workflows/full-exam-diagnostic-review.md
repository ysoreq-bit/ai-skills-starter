# WORKFLOW-006 — Full-Exam Diagnostic Review

- **Scope:** Study workflow
- **Status:** Candidate
- **Trigger:** The user completes an entire exam or substantial timed practice set and sends their work together with official answers, solutions, rubric, or grading information for a comprehensive analysis of errors, weak topics, and next-study priorities.
- **Negative trigger:** Do not activate for one isolated question, for grading without a learning objective, or when the user only wants a score and no diagnostic analysis.
- **Last reviewed:** 2026-07-02

## Capability

Analyze a completed exam as a connected body of evidence, distinguish primary misconceptions from propagated and incidental mistakes, detect recurring weaknesses and fragile strengths, and produce a prioritized learning plan with targeted deep dives and verification tasks.

## Problem

Reviewing an exam question by question can produce a misleading list of mistakes. One early misconception may create several downstream losses, while several correct answers may conceal guessing, unsupported reasoning, or inefficient methods. A useful post-exam analysis must account for opportunity, severity, recurrence, timing, confidence, and prerequisite structure before claiming that a topic is weak.

## Inputs

### Required

- the complete exam, including all instructions, diagrams, point values, and permitted materials when available;
- the learner's complete submitted work or faithful reconstruction;
- authoritative final answers, official solutions, rubric, or grader feedback when available.

### Strongly preferred

- time spent per section or approximate timing notes;
- questions left blank, guessed, revisited, or changed;
- learner confidence for each question or section;
- score breakdown and grader annotations;
- current syllabus, formula sheet, and relevant course sources.

### Optional

- prior exam or practice analyses;
- target grade, exam date, and remaining study time;
- known accommodations or environmental interruptions;
- project-specific preferences for hint depth, notation, and output format.

## Diagnostic principles

1. Treat the exam as evidence about performance, not a complete measurement of ability.
2. Separate **topic**, **solution stage**, and **root cause**; they are not interchangeable.
3. Count a propagated error once at its root and record its consequences separately.
4. Analyze correct work as well as incorrect work.
5. Adjust conclusions for how many genuine opportunities the exam provided to demonstrate each skill.
6. Distinguish knowledge gaps from execution, strategy, time, and answer-presentation issues.
7. Report confidence and alternative explanations for every broad learning claim.
8. Prioritize repair by likely score impact, recurrence, prerequisite centrality, and transfer value.

## Analysis dimensions

### Topic dimension

Map each question to one or more course topics and prerequisites using current official sources when available.

### Solution-stage dimension

Identify where performance succeeded or failed:

- interpreting the task;
- recalling required knowledge;
- recognizing the problem family;
- selecting a method;
- setting up the representation or equations;
- checking validity conditions;
- executing calculations or proof steps;
- verifying the result;
- communicating the final answer.

### Root-cause dimension

Use the taxonomy from `WORKFLOW-005 — Single-Question Error Diagnosis and Remediation`, including conceptual, recognition, method-selection, setup, validity, execution, proof, communication, timing, and metacognitive causes.

### Evidence-strength dimension

For each inferred weakness, record:

- number of independent opportunities;
- number and severity of failures;
- whether the same cause recurs across different surface forms;
- whether correct responses show robust reasoning or only a correct final answer;
- whether time pressure or propagation provides a competing explanation;
- diagnostic confidence: high, medium, or low.

## Method

### 1. Establish the exam structure

Create a map containing:

- question and sub-question IDs;
- points or estimated weight;
- topic and prerequisite tags;
- expected method or acceptable alternatives;
- answer type: conceptual, computational, proof, interpretation, design, or mixed;
- dependency on earlier sub-parts;
- time expectation when known.

Do not infer topic frequency from raw sub-question count without considering weight and dependency.

### 2. Reconstruct the learner's performance

For every item, record:

- attempted, blank, guessed, or incomplete;
- final answer status;
- reasoning quality;
- first consequential divergence when incorrect;
- primary and secondary error categories;
- propagated consequences;
- awarded or estimated points;
- confidence and timing when known;
- whether the work is readable enough for diagnosis.

Preserve correct intermediate reasoning even when the final answer is wrong.

### 3. Compare against authoritative solutions carefully

Use official solutions and rubrics as the primary grading reference when available. Distinguish:

- equivalent valid methods;
- correct reasoning with a presentation mismatch;
- correct final answer reached by invalid or unsupported reasoning;
- official convention differences;
- ambiguity or possible error in the key.

Do not force the learner's work to match one official path when another valid method exists.

### 4. Identify primary errors and propagation chains

For each wrong or incomplete item:

1. locate the earliest consequential divergence;
2. identify downstream losses caused by it;
3. identify independent secondary mistakes;
4. estimate what portion of the lost score each cause plausibly explains;
5. label uncertainty when the rubric or work is incomplete.

A single sign error that contaminates three later calculations is one primary execution error plus a propagation chain, not four independent conceptual failures.

### 5. Analyze correct answers for fragility

Flag correct answers that show:

- unexplained jumps;
- formula use without checked assumptions;
- guessed multiple-choice selections;
- inconsistent intermediate work;
- excessive time or an unnecessarily costly method;
- correct result only because two errors canceled;
- low confidence despite sound reasoning.

Treat these as **fragile successes**, not failures. They may still deserve reinforcement.

### 6. Build a diagnostic matrix

Aggregate evidence by:

- topic;
- prerequisite;
- problem family;
- solution stage;
- primary error cause;
- severity and points affected;
- recurrence across independent questions;
- confidence;
- time and strategy effects.

Use opportunity-aware statements such as:

- “failed in two of three independent method-selection opportunities”;
- “one high-impact but isolated algebra error”;
- “topic appears weak, but the exam tested it only once”;
- “concept appears understood; speed and verification are the main constraints.”

Avoid absolute labels such as “does not understand the topic” unless evidence is unusually strong.

### 7. Detect cross-question patterns

Look for patterns such as:

- repeated failure to test theorem conditions;
- correct calculations after incorrect model setup;
- strong routine execution but weak recognition of which tool applies;
- repeated sign, unit, domain, or boundary mistakes;
- proof answers missing the same logical bridge;
- late-exam decline suggesting time allocation or fatigue;
- excessive time on low-value questions;
- high confidence concentrated in wrong classifications;
- dependence on familiar surface wording;
- repeated omission of final interpretation or units.

Distinguish a true recurring pattern from several consequences of one shared earlier error.

### 8. Identify strengths as well as weaknesses

Record robust strengths when the learner repeatedly:

- recognizes the correct structure;
- explains conditions and reasoning;
- uses efficient methods;
- verifies results;
- transfers knowledge across representations;
- recovers from an earlier mistake;
- communicates complete answers.

Strengths should inform the remediation plan. Build new understanding from methods the learner already handles reliably.

### 9. Prioritize learning targets

Rank targets using these factors:

- **Impact:** points lost or likely future score effect;
- **Recurrence:** repeated independent evidence;
- **Prerequisite centrality:** whether the weakness affects many later topics;
- **Transfer breadth:** number of question families influenced;
- **Diagnostic confidence:** strength of the evidence;
- **Repair cost:** amount of study likely required;
- **Urgency:** proximity of the next assessment when relevant.

Use a priority label such as:

- **Immediate foundation repair** — high-impact prerequisite gap;
- **High-return procedural repair** — recurring decision or validity mistake;
- **Execution control** — arithmetic, algebra, signs, units, or verification;
- **Speed and strategy** — understood material limited by timing or route choice;
- **Monitor only** — isolated low-confidence event.

Do not prioritize solely by the largest topic heading or raw number of mistakes.

### 10. Design the remediation plan

For each priority target, specify:

1. evidence from the exam;
2. most likely root cause and confidence;
3. the exact concept or decision to repair;
4. source sections to review;
5. a deep explanation or mini-lesson;
6. discrimination practice between similar cases;
7. targeted micro-exercises;
8. return to selected exam questions;
9. near- and farther-transfer questions;
10. a mastery criterion;
11. a later retrieval or timed verification recommendation.

Route question-specific repair through `WORKFLOW-005 — Single-Question Error Diagnosis and Remediation`. Route recurring problem-family gaps through `WORKFLOW-004 — Course Solution Playbook and Flowcharts`.

### 11. Produce a realistic study sequence

Order the plan by dependency rather than exam order:

1. prerequisite concepts;
2. recognition and method selection;
3. setup and validity checks;
4. execution accuracy;
5. mixed transfer;
6. timed strategy and full-section rehearsal.

Separate:

- what must be relearned;
- what needs deliberate practice;
- what only needs a checklist or habit;
- what should be monitored but not overreacted to.

When the available study time is known, fit the plan to it without pretending that all gaps can be fully repaired.

### 12. Verify the diagnosis

Before finalizing:

- check every broad claim against at least one explicit exam example;
- ensure repeated errors are independent rather than propagated duplicates;
- compare wrong and correct evidence for the same skill;
- account for missing attempts, timing, and unreadable work;
- state where the official key is absent or ambiguous;
- verify any score calculations against the rubric;
- apply `CORE-003 — Verification Before Completion`.

## Recommended output structure

### 1. Executive diagnosis

A concise account of the main strengths, main score losses, and highest-priority repairs.

### 2. Question-by-question table

For each item:

- result and points;
- what was done correctly;
- earliest divergence;
- primary cause;
- propagated effects;
- confidence;
- recommended action.

### 3. Cross-exam patterns

Group evidence by topic, solution stage, and root cause.

### 4. Priority learning targets

Ranked by impact, recurrence, centrality, transfer, and confidence.

### 5. Deep dives

Focused explanations of the most important weak concepts or procedures.

### 6. Remediation plan

Ordered tasks, exercises, source references, and mastery criteria.

### 7. Exam-strategy findings

Time allocation, question order, verification habits, and answer-presentation improvements.

### 8. Compact lessons to retain

Short rules, warning signs, and checks suitable for an error log or course playbook.

## Failure behavior

- If the official solution or rubric is missing, distinguish factual diagnosis from independent grading estimates.
- If only final answers are visible, limit claims about the learner's reasoning and request or infer less.
- If timing information is missing, do not diagnose time management confidently from blank answers alone.
- If handwriting is unreadable, mark affected items as unassessable rather than inventing a reasoning path.
- If the exam samples a topic only once, label any topic-wide conclusion as provisional.
- If the answer key appears inconsistent, verify against course sources and report the conflict.
- If the exam is too short for reliable pattern detection, use question-level remediation instead of manufacturing trends.

## Do not

- return only a list of wrong answers;
- treat every lost point as an independent conceptual gap;
- ignore correct but fragile reasoning;
- infer broad weakness from one opportunity without qualification;
- use raw error counts without considering point weight, dependency, and opportunity;
- recommend rereading entire chapters when a narrower repair is supported;
- create a study plan that contains no mastery checks;
- blame time pressure for errors whose work shows a clear conceptual cause;
- publish the learner's exam or personal performance data in a public repository.

## Acceptance checks

- Every exam item is accounted for or marked unassessable.
- Primary, propagated, and independent secondary errors are distinguished.
- Correct answers are checked for robustness, not merely counted as successes.
- Broad weakness claims include evidence strength and diagnostic confidence.
- Patterns are opportunity-aware and not inflated by dependent sub-parts.
- Strengths, conceptual gaps, procedural gaps, execution issues, and strategy issues are separated.
- Priorities reflect impact, recurrence, prerequisite centrality, transfer, and confidence.
- Each high-priority target has a concrete remediation sequence and mastery criterion.
- The plan links back to exact exam evidence and authoritative course sources.

## Evaluation cases

### Original case

A learner sends a full engineering exam, their handwritten work, official solutions, and a score breakdown. The workflow discovers that several apparent topic errors originate from one recurring failure to check validity conditions, while most algebra is reliable.

### Independent new case

A learner sends a mixed conceptual and numerical biology exam with answer key but no rubric. The workflow produces a confidence-qualified pattern analysis, identifies fragile correct answers, and avoids unsupported point estimates.

### Negative case

The learner sends one failed sub-question and asks why their method was wrong. Use `WORKFLOW-005 — Single-Question Error Diagnosis and Remediation` instead of constructing a full-exam pattern analysis.

## Evidence and provenance

- **Source:** Repeated post-exam review needs in which question-by-question correction obscured shared root causes, propagation chains, and prioritization.
- **Confidence:** Candidate; requires validation on exams with different formats, rubrics, and levels of available reasoning evidence.
- **Related files:** `skills/workflows/single-question-error-remediation.md`, `skills/workflows/course-solution-playbook.md`, `skills/workflows/evidence-mapped-course-summary.md`, `skills/core/source-integrity.md`, `skills/core/verification-before-completion.md`.

## Changelog

- 2026-07-02 — Initial candidate draft.
