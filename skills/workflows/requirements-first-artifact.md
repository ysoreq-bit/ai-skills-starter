# WORKFLOW-001 — Requirements-First Artifact

- **Scope:** Workflow
- **Status:** Candidate
- **Trigger:** A request produces a substantial document, repository change, study resource, data artifact, or multi-step technical deliverable.
- **Negative trigger:** Skip the full workflow for a small direct edit with explicit boundaries and no meaningful design choices.

## 1. Intent

State the user's goal, intended audience, decision or use case, and why the artifact is needed. Separate the desired outcome from the implementation format.

## 2. Requirements

Extract:

- required content;
- exclusions and protected content;
- output format and scope;
- source hierarchy and provenance rules;
- style and terminology;
- tools, cost, and environment constraints;
- acceptance criteria;
- unresolved assumptions.

Ask only questions whose answers materially change the result. Do not ask the user to repeat information already available.

## 3. Requirements checklist

Review the written requirements as if they were code:

- **Completeness:** Are all required sections, cases, and outputs specified?
- **Clarity:** Are vague terms converted into observable criteria?
- **Consistency:** Do instructions conflict across levels or sources?
- **Measurability:** Can completion be checked?
- **Scenario coverage:** Are normal, alternate, error, and recovery cases addressed when relevant?
- **Dependencies and assumptions:** Are external inputs and missing information explicit?
- **Traceability:** Can each major requirement be mapped to a source or user instruction?

This checklist tests the quality of the requirements, not whether the implementation works.

## 4. Plan

Map files or output sections before editing. Break work into units with a clear deliverable and verification method. Preserve the user's current artifact before structural changes.

For repository work, identify exact paths and checks. For documents, identify sections, source mappings, assets, and expected layout behavior.

## 5. Execution

Implement one coherent unit at a time. Avoid placeholders that conceal missing decisions. Record genuine unknowns explicitly rather than replacing them with plausible content.

## 6. Verification

Apply `CORE-003 — Verification Before Completion`. Map each requirement to evidence, report gaps, and distinguish structural, factual, computational, and visual checks.

## 7. Capture

After delivery, preserve only transferable methods, repeated corrections, tests, and general templates. Do not promote the one-off final artifact merely because it was expensive to produce.
