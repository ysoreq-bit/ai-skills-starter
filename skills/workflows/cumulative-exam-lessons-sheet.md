# WORKFLOW-007 — Cumulative Exam Lessons and Recall Sheet

- **Scope:** Study workflow
- **Status:** Candidate
- **Trigger:** The user wants to create or update a durable, cumulative study sheet from a reviewed exam, their written attempt, official solutions or grading evidence, and the follow-up discussion that exposed important misunderstandings, recognition cues, sanity checks, or robust strengths.
- **Negative trigger:** Do not activate for score calculation only, one isolated question with no persistent artifact request, a general course summary, or an unreviewed exam whose errors have not yet been diagnosed.
- **Last reviewed:** 2026-07-04

## Capability

Transform verified post-exam evidence into a concise but deep cumulative learning artifact that preserves the learner's existing document, integrates new lessons into the right local and global sections, captures follow-up misunderstandings as missing logical bridges, and returns a source file plus a visually verified preview when the format supports rendering.

## Problem

A good exam review and a good lessons sheet are not the same deliverable. A review explains what happened on one assessment. A cumulative lessons sheet must decide what is worth retaining, generalize it beyond the original numbers, place it where it will be found before the next exam, preserve prior edits and design, and avoid turning into either a full course summary or an append-only dump of solved questions.

The most common regressions are:

- copying complete solutions instead of extracting transferable lessons;
- appending a new exam without updating the recognition map, sanity checks, strengths, or recall questions;
- ignoring important confusion revealed only in the follow-up conversation;
- promoting one arithmetic slip into a permanent weakness;
- treating every correct answer as robust mastery;
- replacing or restyling an existing artifact instead of extending it;
- compiling without visually checking page flow, RTL/LTR behavior, tables, or clipped boxes.

## Relationship to other workflows

Use this workflow after or alongside:

- `WORKFLOW-006 — Full-Exam Diagnostic Review` for the question-by-question evidence and cross-question diagnosis;
- `WORKFLOW-005 — Single-Question Error Diagnosis and Remediation` for deep repair of individual errors;
- `WORKFLOW-001 — Requirements-First Artifact` for format, preservation, and acceptance criteria;
- `CORE-001 — Source Integrity` for provenance and authority;
- `CORE-003 — Verification Before Completion` for factual, structural, compile, and visual checks.

This workflow creates or updates the persistent artifact. It does not replace the diagnostic review that supplies the evidence.

## Inputs

### Required

- the current cumulative lessons sheet when one already exists, including the exact source file rather than only a PDF when possible;
- a completed diagnostic review, or enough material to reconstruct it: exam, learner attempt, and authoritative solution or grading evidence;
- the learner's post-review questions and the explanations that resolved or clarified them;
- artifact requirements: format, language, notation, protected edits, and output expectations.

### Strongly preferred

- current course profile, formula sheet, lectures, tutorials, and official notation;
- the previous source file and last compiled preview;
- exact exam name, date, version, and source authority;
- known learner preferences for depth, hinting, terminology, and document design;
- a list of items the learner explicitly marked as needing explanation or retention.

### Optional

- prior exam reviews and error records;
- target exam date and remaining study time;
- source pointers for every official claim;
- previous visual baseline renders for regression comparison.

## Core principles

1. **The artifact is a future-use tool, not a transcript.** Keep what will help recognition, selection, execution, verification, or recall on a later assessment.
2. **Preserve before extending.** Treat the current document, user edits, macros, typography, terminology, and section logic as protected unless the user asks for redesign.
3. **Separate evidence layers.** Distinguish official course facts, reconstructed explanations, independent derivations, and learner-derived conclusions.
4. **Separate local from cumulative lessons.** A lesson may belong in the new exam section without yet qualifying as a global recurring rule.
5. **Count root causes, not symptoms.** Do not create several permanent lessons from one propagated error chain.
6. **Analyze correct work.** Preserve robust strengths and label correct but unsupported, guessed, inefficient, or accidental work as fragile success.
7. **Capture the follow-up conversation.** Repeated “I do not understand this jump” questions are evidence that a missing bridge belongs in the artifact even if the final answer was already known.
8. **Generalize without erasing context.** Keep enough exam-specific evidence to make the lesson concrete, then state the transferable cue, rule, conditions, and check.
9. **Integrate, do not merely append.** Update recognition maps, cumulative warnings, strengths, recall questions, version metadata, and source notes when new evidence changes them.
10. **Verify the artifact at four levels.** Check factual correctness, diagnostic faithfulness, document structure, and rendered appearance.

## Retention model

For every candidate lesson, create a temporary evidence row with:

- exam and question reference;
- topic and problem family;
- learner result: wrong, partial, blank, fragile success, or robust success;
- earliest consequential divergence;
- primary error category;
- official or reconstructed correction;
- follow-up questions that revealed missing understanding;
- transferable recognition cue;
- rule or method;
- validity conditions;
- prevention or sanity check;
- severity and likely future impact;
- recurrence across independent opportunities;
- confidence;
- proposed placement in the artifact.

### Keep in the exam-specific section when

- the lesson is high impact, surprising, explicitly requested, or pedagogically useful;
- the learner needed a deep explanation after the review;
- the item is a fragile success worth stabilizing;
- the method is important even if it appeared only once;
- the evidence is useful but not yet strong enough for a global learner pattern.

### Promote to cumulative sections when

At least one of these is true:

- the same root cause appeared in independent questions or assessments;
- the lesson is a central prerequisite with broad transfer value;
- one concise sanity check could prevent many future losses;
- the learner explicitly reports that the confusion is recurrent;
- a correct answer exposed a dangerous but repeatable unsupported shortcut;
- the lesson is a broadly reusable recognition rule rather than an exam-specific calculation.

Promotion does not require recurrence when a single event reveals a high-impact foundational misconception. In that case, label the conclusion as based on one strong observation rather than pretending it is a repeated pattern.

### Usually omit or compress when

- the issue was a one-off transcription or arithmetic slip with no transfer value;
- the correct reasoning is already covered clearly elsewhere in the sheet;
- the full solution adds length but no reusable cue, condition, or check;
- the evidence is too weak to diagnose the cause;
- the lesson duplicates a stronger existing unit.

## Lesson unit contract

A substantial retained lesson should contain the smallest useful subset of:

1. **Evidence or gap:** what happened, without shaming or overgeneralizing.
2. **Recognition cue:** what wording, structure, or representation should trigger the method.
3. **Precise rule or theorem:** including conditions before use.
4. **Why the tempting wrong step fails:** especially when the learner used it.
5. **Complete bridge:** no hidden logical jump at the point that caused confusion.
6. **Reusable procedure:** a short ordered sequence when the task is procedural.
7. **Sanity check:** range, sign, support, units, limiting case, normalization, or alternative representation.
8. **Compact key rule:** one memorable sentence suitable for rapid review.
9. **Provenance status:** official, reconstructed, independent, or learner-derived when ambiguity matters.

Do not force every unit to contain all nine parts. Use the minimum that makes the lesson independently useful later.

## Method

### 1. Establish the artifact contract

Before editing, record:

- whether this is a new document or an update;
- source format and required deliverables;
- language, font, notation, page size, and compilation engine;
- protected content and user edits;
- existing environments, macros, colors, section order, and naming conventions;
- whether a compiled preview and visual inspection are required;
- versioning and date convention.

When updating, inspect the entire source structure and a representative render before changing content. Do not infer the design only from the first page.

### 2. Verify the diagnostic evidence

Use the official solution or rubric as the grading reference when available, while allowing mathematically or scientifically equivalent valid methods. Confirm:

- the learner's actual selected answer or written path;
- the earliest consequential divergence;
- what was genuinely correct;
- whether later mistakes were propagated;
- whether a correct answer was robust or fragile;
- which follow-up questions exposed the missing conceptual bridge.

If the diagnostic review is not yet reliable, complete `WORKFLOW-006` or `WORKFLOW-005` before extracting lessons.

### 3. Build the evidence-to-placement ledger

For each candidate lesson, choose one or more destinations:

- recognition map;
- exam-specific concept unit;
- warning or sanity-check box;
- robust-strength section;
- fragile-success note;
- quick-recall question;
- future-practice or mastery-check note;
- no insertion, with a reason such as duplicate or low transfer value.

Map all insertions before editing. This prevents an append-only document and reveals duplication early.

### 4. Preserve and deduplicate the existing sheet

Search the current artifact for the concept and its synonyms. Then choose one action:

- extend an existing unit with the new distinction or example;
- add a new local unit under the new exam;
- promote a distilled rule to a cumulative section;
- revise a prior strength from robust to fragile, or the reverse, when new evidence warrants it;
- leave the existing unit unchanged and add only a cross-reference;
- deprecate or correct earlier guidance explicitly rather than silently contradicting it.

Do not rewrite unrelated sections for stylistic consistency unless the user requested a redesign.

### 5. Write the exam-specific section

Create a clearly identified section for the new assessment with:

- exam name and date;
- source-status note;
- lessons organized by concept or problem family, not merely by question number when grouping improves retrieval;
- deep explanations for high-priority misunderstandings;
- warnings for sanity checks that would have caught an impossible result;
- strengths and fragile successes evidenced by that exam.

Keep question numbers as provenance, but make the headings concept-based so the section remains useful after the original exam is forgotten.

### 6. Update cumulative retrieval structures

Review and update all affected global sections:

- **Recognition map:** add cue → first tool → non-negotiable check.
- **Cumulative lessons or warnings:** promote only general, high-value rules.
- **Strengths:** require positive evidence and distinguish robust from fragile.
- **Quick recall:** add short questions for every new high-priority rule or distinction.
- **How to use the sheet:** update only if the workflow or review sequence changed.
- **Future-update template:** keep it aligned with the current artifact structure.

A new exam section without these checks is incomplete when its lessons change the cumulative retrieval system.

### 7. Convert follow-up confusion into explicit bridges

Review the post-exam conversation chronologically. When the learner asks about a jump, identify the exact missing implication and insert it where a future reader would need it.

Examples of bridge types include:

- why a random count is binomial before applying a binomial formula;
- why a monotone function permits an inverse-event transformation;
- why a width appearing in the question is not automatically a standard deviation;
- why a maximum is easier through its CDF than through a direct density argument;
- why a series starts at one rather than zero and how that changes the closed form.

Do not insert the dialogue itself. Insert the durable bridge that resolves it.

### 8. Maintain artifact metadata and source integrity

Update:

- version number;
- last-updated date;
- list or count of included assessments when shown;
- table of contents and internal references;
- source-status notes for the new exam;
- changelog when the artifact uses one.

Do not embed full copyrighted exams, official solution scans, private grades, or personal identifiers in a public template or public repository. Keep source pointers or concise derived lessons.

### 9. Compile and inspect

For LaTeX artifacts:

1. compile with the declared engine, normally twice when a table of contents or references are present;
2. read the full log and distinguish harmless warnings from layout or font failures;
3. render the PDF to images;
4. inspect the cover, table of contents, every newly changed page, dense tables, page transitions around unbreakable boxes, equations with mixed directionality, and the final pages;
5. check for clipped text, overfull boxes, unexpected blank space, broken glyphs, bad RTL/LTR order, orphaned headings, and inconsistent page breaks;
6. compare with the previous render when one exists.

Compilation alone is not visual verification.

For DOCX, slides, or other formats, apply the equivalent structural and visual checks with the appropriate artifact workflow.

### 10. Perform a preservation and coverage diff

Before delivery, verify:

- no prior user-authored lesson disappeared unintentionally;
- all selected candidate lessons were inserted in their mapped destinations;
- no lesson was duplicated with conflicting wording;
- cumulative sections reflect new general lessons;
- low-evidence events were not promoted as stable learner patterns;
- source claims and diagnostic claims retain their confidence level;
- the document remains a review sheet rather than expanding into a full course textbook.

### 11. Deliver both artifact and change report

Return:

- the editable source file;
- a compiled or rendered preview when requested or useful;
- a concise in-chat report of what was added, revised, promoted, or deliberately not promoted;
- verification status and any remaining limitation.

The change report should describe meaningful content and structural updates, not merely list filenames.

## Recommended artifact structure

Preserve the existing structure when updating. For a new artifact, use this minimum model:

1. Cover with course, version, update date, and included assessments.
2. Purpose and instructions for using the sheet.
3. Fast recognition map.
4. One source-aware section per reviewed assessment.
5. Cumulative high-value rules and warnings.
6. Robust strengths and fragile successes.
7. Quick recall questions with concise answers.
8. Template or protocol for the next update.

The reusable LaTeX starting point is `templates/latex/cumulative-exam-lessons-sheet.tex`.

## Failure behavior

- **No existing source file:** create a clean new artifact using the user's preferred format and the minimum structure above; do not attempt to reconstruct editable source from a PDF unless necessary.
- **No official solution:** label grading and corrections as reconstructed or independent, lower confidence, and avoid presenting them as official.
- **Only final answers are visible:** retain answer-level lessons but do not invent root causes from unseen reasoning.
- **Unreadable handwriting:** mark the item unassessable or ask for a clearer crop when the missing detail materially affects the lesson.
- **Conflicting sources:** apply the course authority hierarchy and record the conflict.
- **No compilation or rendering environment:** return the source with compile and visual status explicitly marked unverified.
- **Artifact is already bloated:** consolidate duplicates and prioritize high-impact lessons before adding length; report what was compressed.
- **Too many candidate lessons:** rank by impact, transfer, recurrence, confidence, and retrieval value rather than adding everything.

## Do not

- replace the learner's existing artifact with a new generic document;
- copy every corrected solution into the sheet;
- append a new exam section without checking global recognition and recall sections;
- infer a recurring weakness from one low-evidence mistake;
- classify a correct option as robust mastery without examining the reasoning;
- hide the exact logical bridge that caused repeated follow-up questions;
- duplicate the same lesson under several headings with only superficial wording changes;
- silently alter fonts, macros, terminology, numbering, colors, or page architecture;
- use manual spacing hacks to conceal structural layout problems;
- claim compilation, correctness, or visual quality without fresh evidence;
- commit the learner's private exam, full official solutions, personal performance data, or course archive to a public repository.

## Acceptance checks

- The current artifact and user edits were preserved unless an explicit redesign was requested.
- Every added lesson is traceable to exam evidence, an official or labelled alternative solution, or a documented follow-up misunderstanding.
- Root errors, propagated consequences, fragile successes, and robust strengths remain distinct.
- High-priority follow-up questions were converted into explicit reusable bridges.
- Every substantial lesson contains a cue, rule or method, validity condition when relevant, and prevention check.
- The recognition map and quick-recall section were reviewed and updated where warranted.
- Global learner-pattern claims are proportional to the number and independence of observations.
- Duplicate and contradictory guidance was checked.
- Version, date, included assessments, and source-status notes are current.
- Editable source and preview were delivered when required.
- The declared compilation or rendering check was run freshly and the changed pages were visually inspected.
- The in-chat change report explains what was added and what changed in the cumulative understanding.

## Evaluation cases

### Original case

A learner has a Hebrew XeLaTeX probability lessons sheet built after one exam. They submit a second handwritten exam, the official solution, red annotations requesting explanations, and several follow-up questions about hidden steps. The workflow preserves the Arimo-based design and custom environments, adds a concept-organized second-exam section, updates the recognition map, corrects the strength classification for CLT and convolution, adds quick-recall questions, increments the version, compiles twice, renders and inspects the changed pages, and reports the additions in chat.

### Independent new case

A learner in organic chemistry maintains a cumulative post-exam study document. A new exam reveals confusion between kinetic and thermodynamic control, one unsupported but correct stereochemistry answer, and a repeated failure to state reaction conditions. The workflow integrates the lessons by reaction family, updates a decision table and recall section, preserves the existing document style, and avoids copying full mechanisms when a cue-condition-check unit is sufficient.

### Edge case

A learner scores highly and makes only one arithmetic slip, but two correct answers use invalid assumptions. The workflow does not create a global arithmetic weakness. It records the two fragile successes, adds the missing validity checks, and leaves the robust-strength section unchanged until stronger evidence appears.

### Negative case

The user asks only for the score and a question-by-question grading table for one exam. Use `WORKFLOW-006 — Full-Exam Diagnostic Review`; do not create or update a cumulative lessons artifact unless the user requests it.

### Regression case

A previous approach appended full solutions to the end of an existing document, failed to update the recognition map and recall questions, labelled all correct answers as strengths, and returned a PDF that compiled but contained clipped RTL boxes. The candidate passes only if it prevents all four regressions.

## Evidence and provenance

- **Source:** A successful cumulative probability lessons-sheet update performed on 2026-07-04 from two exams, the learner's handwritten work, official solutions, explicit red annotations, and follow-up conceptual questions.
- **Confidence:** Candidate. The original case passed; independent cross-course and negative-case validation remain required before promotion to verified.
- **Related files:** `skills/workflows/full-exam-diagnostic-review.md`, `skills/workflows/single-question-error-remediation.md`, `skills/workflows/requirements-first-artifact.md`, `skills/core/source-integrity.md`, `skills/core/verification-before-completion.md`, `templates/latex/cumulative-exam-lessons-sheet.tex`.

## Changelog

- 2026-07-04 — Initial candidate extracted from the validated probability cumulative lessons-sheet process.
