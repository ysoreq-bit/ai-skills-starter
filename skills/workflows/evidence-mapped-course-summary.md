# WORKFLOW-003 — Evidence-Mapped Course Summary

- **Scope:** Study workflow
- **Status:** Candidate
- **Trigger:** The user requests a whole-course or major-unit theory summary built from lectures, tutorials, homework, formula sheets, or past assessments, especially when the result should serve as a dependable reference for later review.
- **Negative trigger:** Do not activate for an isolated concept explanation, page-by-page teaching, or a summary based on one short document with no need for course-wide coverage analysis.
- **Last reviewed:** 2026-07-02

## Capability

Produce a structured course summary whose scope comes from the current course materials, whose emphasis is informed by assessment evidence, and whose claims remain traceable to reliable sources.

## Problem

Course summaries often inherit the order and omissions of one source, overfit a small set of past exams, mix official material with reconstruction, and provide no reliable path back to the underlying theory. This makes them difficult to trust and inefficient to use as a long-term reference.

## Inputs

### Required when available

- lecture notes, slides, or an official course reader;
- tutorial, recitation, or exercise-session material;
- the current syllabus, topic list, or instructor guidance.

### Optional but valuable

- homework and official solutions;
- allowed formula sheets;
- past exams with or without solutions;
- grading rubrics, review sessions, or instructor announcements;
- project-specific terminology, notation, language, and output constraints.

## Source hierarchy

Apply the user's or project profile's explicit hierarchy first. Otherwise use this default:

1. current official syllabus and instructor instructions;
2. current official lecture material;
3. current official tutorial material and official solutions;
4. current homework and formula sheets;
5. past exams and official exam solutions;
6. older course material;
7. student notes or unofficial solutions.

Past exams indicate likely emphasis and integration patterns. They do not override the theory, notation, or scope established by current official course sources.

## Method

### 1. Inventory and qualify the corpus

Create an internal source inventory containing, when known:

- source type, date, semester, and author;
- current or historical status;
- page or section range;
- whether an official solution exists;
- readability, completeness, and suspected omissions;
- duplicate or near-duplicate sources.

Do not treat repeated copies or lightly modified versions of one exam as independent evidence.

### 2. Establish course scope

Build a provisional topic tree from the union of the current official sources. Resolve naming differences and split broad labels into teachable units. Mark:

- required topics;
- prerequisite material used but not taught in depth;
- topics present only in older material;
- topics whose current status is uncertain.

Assessment frequency may change the depth and order of presentation, but it must not silently remove a topic that belongs to the current course scope.

### 3. Build an evidence and coverage map

For every topic, record:

- lecture source and exact location;
- tutorial or worked-example source and exact location;
- related homework;
- past-exam appearances;
- available official solutions;
- confidence in the mapping;
- unresolved contradictions or notation changes.

This map is the control layer for the summary. It may appear as an appendix or a separate companion table when useful.

### 4. Analyze assessment emphasis carefully

Use past assessments to estimate:

- recurrence across independent exams;
- typical depth and point weight when available;
- whether the topic appears directly or inside integrative questions;
- common combinations with other topics;
- recent versus historical emphasis;
- conceptual versus computational expectations.

State the evidence behind any label such as high, medium, or low emphasis. Do not infer probability from one exam or from raw sub-question counts alone.

### 5. Design a logical summary architecture

Organize the summary by conceptual dependency and problem-solving usefulness rather than by source order. For each chapter or unit, include only the elements that materially help the learner:

1. purpose and place in the course;
2. definitions and notation;
3. assumptions and validity conditions;
4. theorems, laws, or principles stated precisely;
5. derivations or mathematical tools needed for understanding and use;
6. physical, geometric, probabilistic, or operational interpretation as relevant;
7. formulas with variable meanings, units, and restrictions;
8. representative examples that illustrate the idea without replacing the theory;
9. common confusions, boundary cases, and failure conditions;
10. assessment relevance and source pointers.

When a theorem is used in a proof or derivation, state the theorem before applying it unless the project instructions explicitly choose another style.

### 6. Preserve provenance in the prose

Distinguish clearly between:

- material stated directly in an official source;
- a reconstruction that combines several sources;
- an independent explanation or example added for clarity;
- an unresolved or low-confidence interpretation.

Use exact page, section, lecture, tutorial, or question references whenever the source format permits. Never invent a citation or present an unofficial solution as official.

### 7. Make the document usable as a reference

Provide:

- a navigable table of contents;
- consistent terminology and notation;
- cross-references between dependent topics;
- a formula or theorem index when the course warrants it;
- explicit links from summary sections back to the evidence map;
- clear separation between core theory, enrichment, and exam strategy.

The main summary should remain useful even when the reader is not currently solving an exam question.

### 8. Verify coverage and fidelity

Before completion:

- map every current official topic to a summary section or an explicit exclusion reason;
- trace every nontrivial formula, theorem, and course-specific convention to a source or clearly marked derivation;
- compare notation across lectures, tutorials, homework, and exams;
- check that assessment emphasis did not distort theoretical scope;
- inspect for contradictory statements, unexplained prerequisites, and duplicated explanations;
- apply `CORE-003 — Verification Before Completion`.

## Failure behavior

- If the official course scope is missing, produce a provisional scope and label it as such.
- If past exams are unavailable or unrepresentative, omit quantitative emphasis claims and explain the limitation.
- If sources conflict, preserve both versions, identify their provenance, and avoid silently choosing one without evidence.
- If a source is unreadable or incomplete, record the gap rather than filling it with plausible material.
- If the requested length cannot support full coverage, preserve the source map and explicitly identify what was compressed or omitted.

## Do not

- organize the entire summary merely by file order;
- use exam frequency as the factual authority for theory;
- omit rare but currently required topics without disclosure;
- copy large portions of copyrighted course material into a public repository;
- hide uncertainty behind smooth prose;
- treat one-off student wording as a course definition;
- turn the summary into an answer bank with little theoretical explanation.

## Acceptance checks

- Every current official topic is covered or explicitly accounted for.
- Major claims and course-specific conventions are traceable to sources.
- Exam emphasis labels are evidence-based and separated from source authority.
- Official, reconstructed, and independently added material are distinguishable.
- The document has a logical dependency order and can be used as a standalone theory reference.
- Known source gaps, outdated material, and conflicts are visible.

## Evaluation cases

### Original case

A technical university course provides lecture notes, tutorials, homework, a formula sheet, and several past exams. Produce a course-wide theory reference with source mappings and assessment-informed emphasis.

### Independent new case

A life-science course provides slides, reading assignments, problem sessions, and mixed-format exams. Build a summary that explains required mathematics, preserves biological interpretation, and distinguishes conceptual from computational emphasis.

### Negative case

The user asks for a short explanation of one theorem from one page. Use a focused explanation or the page-by-page teaching workflow instead of building a course-wide evidence map.

## Evidence and provenance

- **Source:** Repeated course-summary workflows and recurring failures in source coverage, exam overfitting, and provenance tracking.
- **Confidence:** Candidate; requires validation on an independent course and a negative case.
- **Related files:** `skills/core/source-integrity.md`, `skills/research/multi-source-synthesis.md`, `skills/core/verification-before-completion.md`, `skills/workflows/requirements-first-artifact.md`.

## Changelog

- 2026-07-02 — Initial candidate draft.
