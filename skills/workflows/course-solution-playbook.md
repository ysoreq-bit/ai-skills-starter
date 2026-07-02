# WORKFLOW-004 — Course Solution Playbook and Flowcharts

- **Scope:** Study workflow
- **Status:** Candidate
- **Trigger:** The user requests a reusable collection of course-specific solution procedures, SOPs, decision trees, or detailed flowcharts synthesized from lectures, tutorials, homework, and past assessments.
- **Negative trigger:** Do not activate for one isolated exercise, a theory-only course summary, or a course whose tasks do not contain repeatable decision procedures.
- **Last reviewed:** 2026-07-02

## Capability

Extract the central problem-solving methods of a course and convert them into a validated playbook of recognition cues, decision procedures, detailed flowcharts, checks, variants, and source-linked examples.

## Problem

Students often learn from solved examples without acquiring a transferable procedure. A collection of answers can hide how to recognize the problem type, choose between methods, handle branches, verify the result, and recover when an approach fails. Past exams can also create false confidence when surface-similar questions require different methods.

## Inputs

### Required when available

- tutorial, recitation, and worked-example material;
- homework and official solutions;
- lecture material containing definitions, theorems, and method conditions;
- a representative set of past assessments.

### Optional but valuable

- grading rubrics and examiner comments;
- formula sheets;
- common-error reports or instructor review sessions;
- current syllabus and topic exclusions;
- project-specific requirements for diagram language, notation, detail, and output format.

## Method

### 1. Inventory and normalize the problem corpus

For each problem or worked example, record:

- source, date, course version, and exact location;
- topic labels used by the source;
- givens, requested output, and mathematical structure;
- the method used in an official solution, when available;
- alternative valid methods;
- unusual assumptions, notation, or edge cases;
- whether the item duplicates another source.

Normalize superficial wording differences so that structurally equivalent problems can be compared.

### 2. Identify problem families by structure

Cluster questions according to the decisions and operations needed to solve them, not merely shared keywords. A useful family has:

- recognizable entry conditions;
- a repeatable core procedure;
- meaningful branches or variants;
- a clear completion condition;
- at least one way to verify or reject the result.

Split a family when two questions require different first decisions or validity conditions even if they look similar. Merge families only when one procedure genuinely transfers across them.

### 3. Build an evidence matrix

For every proposed problem family, record:

- representative source instances;
- recurrence across independent homework sets or exams;
- current versus historical relevance;
- official solution availability;
- common variants and integrated-topic appearances;
- confidence that the family is real and reusable.

Do not treat repeated copies, minor number changes, or one instructor's single example as broad evidence by themselves.

### 4. Extract the reusable method

For each family, determine:

1. **Goal:** What output is the solver trying to produce?
2. **Recognition cues:** What features indicate that this procedure may apply?
3. **Negative cues:** What features indicate that it does not apply?
4. **Prerequisites:** Which definitions, theorems, formulas, or representations are required?
5. **Inputs:** What data must be identified or computed first?
6. **Decision points:** Which choices change the path?
7. **Core sequence:** What operations must occur, and in what order?
8. **Branch conditions:** What changes for alternate cases, domains, signs, regions, boundary conditions, or representations?
9. **Completion condition:** How does the solver know the requested result has been reached?
10. **Verification:** Which dimensional, limiting, algebraic, geometric, physical, probabilistic, or source-based checks apply?
11. **Recovery:** What should be reconsidered when a check fails?
12. **Common traps:** Which tempting shortcuts or classifications repeatedly fail?

State any theorem or rule before the step that applies it when the project requires explicit theorem citation.

### 5. Assign provenance to each procedure

Label every method as one of:

- **Official:** stated or demonstrated directly in an authoritative course source;
- **Reconstructed:** inferred from several official examples or solutions;
- **Independent:** derived by the agent without a direct course-source match.

Attach exact source pointers and a confidence level. Never imply that a reconstructed or independent procedure is the instructor's official method.

### 6. Write the SOP before drawing the flowchart

Each procedure should contain:

- title and problem-family definition;
- when to use and when not to use it;
- required inputs and expected output;
- numbered step-by-step method;
- decision table for major branches;
- verification and recovery steps;
- variants and edge cases;
- common errors;
- source examples and provenance;
- confidence and known limitations.

The prose SOP is the semantic source of truth. The flowchart is a visual representation of the same logic and must not silently add or omit decisions.

### 7. Build detailed, readable flowcharts

Use these diagram rules unless the project defines stricter ones:

- one action per process node;
- one explicit question per decision node;
- label every outgoing decision branch;
- use verb-led action text;
- show required preprocessing before the main branch;
- expose algebraic or conceptual steps that students commonly skip;
- include verification nodes and return paths after failed checks;
- show terminal outputs explicitly;
- reference a separate sub-procedure when one chart would otherwise become unreadable;
- keep notation consistent with the theory summary and course sources.

Prefer a two-level structure when the course is large:

1. an overview map that selects the problem family;
2. a detailed flowchart for each family.

### 8. Rank and organize the playbook

Organize procedures by conceptual dependency and exam usefulness. Include:

- a quick recognition table;
- the overview method-selection map;
- detailed SOPs and flowcharts;
- integrative procedures that combine several topics;
- a common-traps index;
- a final-answer and sanity-check checklist.

Use assessment recurrence to prioritize navigation and depth, not to erase foundational or currently required methods.

### 9. Validate on held-out questions

Reserve representative questions that were not used to design each procedure. Test whether the playbook enables the solver to:

- select the correct family;
- reject a misleading near-match;
- follow every necessary branch;
- obtain the correct form of result;
- detect an intentionally introduced error;
- handle at least one variant or edge case.

Revise the procedure when the held-out case reveals an implicit assumption or missing branch. Apply the original-case, independent-new-case, and negative-case logic from `META-002 — Skill Design and Evaluation`.

### 10. Verify the final document

Before completion:

- trace each procedure to its evidence matrix;
- compare every flowchart with its prose SOP;
- check that all branches terminate or loop intentionally;
- confirm that decision labels are mutually understandable and not ambiguous;
- verify representative calculations and source references;
- distinguish official, reconstructed, and independent content;
- apply `CORE-003 — Verification Before Completion`.

## Failure behavior

- If official solutions are unavailable, extract only what the sources support and label the procedure as reconstructed or independent.
- If the assessment set is too small, avoid frequency-based priority claims and present a provisional family map.
- If two sources use incompatible conventions, create explicit branches or separate procedures rather than silently merging them.
- If a problem family cannot be expressed without many hidden exceptions, narrow or split the family.
- If diagram generation is unavailable, deliver the complete SOP and an unambiguous text decision tree rather than an ornamental but incomplete chart.

## Do not

- produce an answer bank that merely swaps numbers into solved examples;
- cluster questions by keywords alone;
- force every question into a flowchart when expert judgment or open-ended proof design is essential;
- hide validity conditions inside footnotes;
- omit failed-check recovery paths;
- overfit one exam or one lecturer's wording;
- present an alternative method as official without evidence;
- create a visually polished chart whose logic is less complete than the written procedure.

## Acceptance checks

- The playbook covers the central recurring problem families supported by the corpus.
- Every family has recognition cues, negative cues, ordered steps, branches, checks, and source provenance.
- Flowcharts and prose SOPs encode the same logic.
- A held-out question can be classified and solved using the documented procedure.
- A misleading near-match is rejected by an explicit negative condition.
- Official, reconstructed, and independent methods are visibly distinguished.
- Rare but foundational or currently required methods are not silently omitted.

## Evaluation cases

### Original case

A quantitative engineering course contains lectures, tutorials, homework, and several years of exams. Build a method-selection map and detailed procedures for the recurring calculation and proof families.

### Independent new case

A physical-chemistry course combines conceptual interpretation, derivations, and numerical questions. Produce separate but linked SOPs for model selection, equation setup, computation, and result validation.

### Negative case

The user asks for help with one unfamiliar proof and does not request a reusable course-wide method. Provide guided problem-solving support instead of constructing a full playbook.

## Evidence and provenance

- **Source:** Repeated requests to generalize lessons from specific exercises into memorable procedures, decision trees, and course-wide flowcharts.
- **Confidence:** Candidate; requires validation on an independent course and held-out problem set.
- **Related files:** `skills/workflows/evidence-mapped-course-summary.md`, `skills/core/source-integrity.md`, `skills/research/multi-source-synthesis.md`, `skills/meta/skill-evaluation.md`, `skills/core/verification-before-completion.md`.

## Changelog

- 2026-07-02 — Initial candidate draft.
