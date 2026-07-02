# WORKFLOW-005 — Single-Question Error Diagnosis and Remediation

- **Scope:** Study workflow
- **Status:** Candidate
- **Trigger:** The user sends one exam, homework, quiz, or practice question they could not solve or solved incorrectly, optionally with their attempt, and wants to understand the difficulty and prevent the same mistake from recurring.
- **Negative trigger:** Do not activate when the user only wants the final answer, when no learning or diagnosis is requested, or when the item belongs inside a full-exam review that should preserve cross-question patterns.
- **Last reviewed:** 2026-07-02

## Capability

Diagnose the earliest meaningful breakdown in one attempted question, identify the most plausible root cause without overclaiming, teach the missing idea at the required depth, and guide the learner through a targeted remediation sequence that ends with transfer and verification.

## Problem

A wrong final answer does not reveal why the learner struggled. The cause may be conceptual, strategic, algebraic, representational, linguistic, time-related, or a propagated consequence of one earlier mistake. Explaining the official solution alone may repair the question but leave the underlying weakness unchanged.

## Inputs

### Required

- the complete question, including diagrams, definitions, given data, and requested output;
- the authoritative answer or solution when one exists, or permission to solve independently when it does not.

### Strongly preferred

- the learner's written attempt, including crossed-out work when readable;
- the point at which the learner felt uncertain, became stuck, guessed, or changed direction;
- relevant course sources, formula sheet, permitted methods, and notation;
- whether the work was timed and any known time pressure.

### Optional

- the learner's confidence before and after answering;
- prior mistakes on related questions;
- the grader's comments or awarded points;
- project-specific preferences for hints, depth, notation, and interaction style.

## Diagnostic principles

1. Diagnose from evidence, not merely from the wrong final answer.
2. Find the **earliest consequential divergence**, not every downstream symptom.
3. Distinguish an observed error from a hypothesis about its cause.
4. Do not infer a stable knowledge gap from one slip without supporting evidence.
5. Preserve valid parts of the learner's reasoning and build from them.
6. Use the authoritative course method when one is required; label alternatives clearly.
7. Prefer active reconstruction and transfer over passive rereading.

## Error taxonomy

Use one or more categories, but identify a primary cause when evidence permits:

- **Reading and interpretation:** missed condition, misread quantity, misunderstood wording, diagram, notation, or requested result.
- **Recall:** missing definition, theorem, identity, formula, or prerequisite fact.
- **Conceptual model:** incorrect mental model or relationship between quantities.
- **Recognition and classification:** failed to identify the problem family, singularity type, system property, regime, or applicable representation.
- **Method selection:** recognized the topic but chose an invalid, inefficient, or incomplete approach.
- **Setup and representation:** incorrect equation, coordinate system, diagram, domain, sign convention, boundary condition, or decomposition.
- **Validity conditions:** applied a theorem or formula without checking its assumptions.
- **Execution:** algebra, arithmetic, calculus, symbolic manipulation, units, signs, or transcription.
- **Proof and justification:** correct intuition but missing logical bridge, theorem citation, quantifier, case split, or conclusion.
- **Answer communication:** incomplete final form, missing units, missing interpretation, or answer not matched to the question.
- **Strategy and time management:** spent too long, failed to move on, did not perform a sanity check, or selected a high-cost route under time pressure.
- **Metacognitive calibration:** high confidence in a wrong step, low confidence in a correct method, or failure to notice contradiction.

## Method

### 1. Reconstruct the intended task

State precisely:

- what is given;
- what must be found or proved;
- which conditions restrict the solution;
- which course topics and prerequisites are likely involved;
- which answer forms would count as complete.

Do not begin by exposing the full correct solution when the learner's own reasoning can still be diagnosed.

### 2. Reconstruct the learner's path

Read the attempt chronologically. Separate it into decision points and operations. Mark each part as:

- correct and useful;
- correct but unnecessary;
- incomplete or ambiguous;
- incorrect;
- unsupported;
- unreadable or missing.

When the attempt is absent, infer less. Use the learner's description of where they became stuck and, when appropriate, ask or test one narrow diagnostic question before committing to a root-cause claim.

### 3. Locate the earliest consequential divergence

Find the first point where the work becomes incompatible with a valid solution path or where a required decision is omitted. Distinguish:

- **primary error:** the earliest cause that materially changes the path;
- **propagated errors:** later consequences of the primary error;
- **independent secondary errors:** later mistakes that would still matter if the first error were corrected.

Do not count every incorrect line after the primary error as a separate weakness.

### 4. Generate and test root-cause hypotheses

For the earliest divergence, consider several explanations. Test them using evidence such as:

- whether the relevant rule was stated correctly elsewhere;
- whether the learner selected the correct method before executing it incorrectly;
- whether a minimal cue restores progress;
- whether the same confusion appears in another representation;
- whether the learner can explain why the correct condition matters;
- whether time pressure plausibly caused an otherwise isolated slip.

Report:

- observed evidence;
- most likely cause;
- plausible alternatives;
- diagnostic confidence: high, medium, or low.

### 5. State the distilled lesson

Write one memorable, general lesson that would have prevented the error. It should contain:

- the recognition cue;
- the decision or rule;
- the condition under which it is valid;
- the most relevant self-check.

Avoid a lesson tied only to the numbers or wording of the original question.

### 6. Repair the conceptual foundation

Teach the identified weak point from the minimum required prerequisite level upward. Use this order when suitable:

1. precise definition or theorem;
2. intuitive interpretation;
3. why the learner's step was tempting;
4. why it fails;
5. a contrasting example different from the original question;
6. boundary or counterexample showing the rule's limits;
7. connection back to the course's notation and official method.

Adapt depth to the diagnosed cause. Do not reteach the entire chapter when the problem is local.

### 7. Build a targeted remediation ladder

Use the smallest sequence that can demonstrate real repair:

1. **Discrimination task:** distinguish when the method applies and when it does not.
2. **Single-skill micro-example:** practice only the missing decision or operation.
3. **Guided return:** revisit the original question using small prompts rather than immediately replacing the learner's work.
4. **Near-transfer question:** same underlying idea with changed surface features.
5. **Farther-transfer or mixed question:** require selection of the method among alternatives when appropriate.
6. **Self-explanation:** learner states the rule, conditions, and check in their own words.
7. **Delayed retrieval recommendation:** suggest a later re-test when retention, not only immediate performance, matters.

The learner should perform the decisive step. Do not turn remediation into a sequence of assistant-completed solutions.

### 8. Verify that the problem is repaired

Consider the issue repaired only when the learner can:

- identify the relevant cue without being told the topic;
- choose or reject the method correctly;
- explain the validity condition;
- execute the critical step;
- detect a representative wrong approach;
- solve a transfer item with materially reduced help.

Immediate agreement with an explanation is not sufficient evidence.

### 9. Capture reusable knowledge

When useful, produce a compact error record containing:

- question family;
- primary error category;
- earliest divergence;
- root-cause hypothesis and confidence;
- distilled lesson;
- prevention check;
- remediation completed;
- evidence of transfer;
- remaining uncertainty.

Link the lesson to the relevant course summary or solution playbook rather than storing the original copyrighted question in a public repository.

## Recommended output structure

1. **What you did correctly**
2. **Where the solution first went off track**
3. **What the evidence suggests you were missing**
4. **The general lesson to remember**
5. **Deep explanation of the weak point**
6. **Targeted practice sequence**
7. **Return to the original question**
8. **Transfer check**
9. **Compact lesson for future review**

## Failure behavior

- If the attempt is unreadable, identify what can be established and request a clearer image only when guessing would undermine the diagnosis.
- If no authoritative solution exists, solve independently and label that status.
- If multiple root causes remain plausible, run a short diagnostic comparison rather than choosing one confidently.
- If the learner's answer is correct but reasoning is fragile, diagnose the unsupported or accidental step instead of declaring mastery.
- If the problem is caused mainly by time pressure, still check whether method selection or verification can be made cheaper.
- If the issue is broader than one question, route recurring patterns to `WORKFLOW-006 — Full-Exam Diagnostic Review` or `WORKFLOW-004 — Course Solution Playbook and Flowcharts`.

## Do not

- begin with a complete replacement solution before examining the attempt;
- equate a wrong result with conceptual misunderstanding;
- criticize every downstream line after one primary error;
- label the learner as weak in a topic based on one low-evidence event;
- give practice that merely changes numbers;
- ask leading questions whose wording reveals the answer;
- teach an unofficial shortcut as the required course method;
- consider the issue fixed because the learner says the explanation makes sense.

## Acceptance checks

- The earliest consequential divergence is identified or explicitly remains uncertain.
- Observations, root-cause hypotheses, and confidence are separated.
- Valid reasoning in the original attempt is preserved.
- The distilled lesson transfers beyond the original wording.
- The remediation sequence targets the diagnosed cause rather than the entire topic indiscriminately.
- The learner performs at least one decisive reasoning step.
- A transfer check tests recognition, validity conditions, and execution.
- Official, reconstructed, and independent material are distinguished.

## Evaluation cases

### Original case

A learner sends an exam question, their incorrect written solution, and an official solution. The workflow identifies the first wrong classification, explains the missing condition, and uses contrasting and transfer questions to repair it.

### Independent new case

A learner leaves a proof question mostly blank and reports not knowing how to start. The workflow distinguishes missing theorem recall from difficulty translating the requested statement into a proof plan.

### Negative case

The user asks only for the numerical answer to a routine exercise. Provide the requested direct answer according to project instructions rather than initiating a full diagnostic workflow.

## Evidence and provenance

- **Source:** Repeated study interactions in which explaining the correct solution was insufficient until the earliest error, root cause, and transfer skill were isolated.
- **Confidence:** Candidate; requires validation across conceptual, computational, and proof-based questions.
- **Related files:** `skills/workflows/full-exam-diagnostic-review.md`, `skills/workflows/course-solution-playbook.md`, `skills/workflows/evidence-mapped-course-summary.md`, `skills/core/source-integrity.md`, `skills/core/verification-before-completion.md`.

## Changelog

- 2026-07-02 — Initial candidate draft.
