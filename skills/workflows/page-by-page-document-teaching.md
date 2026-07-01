# WORKFLOW-002 — Page-by-Page Document Teaching

- **Scope:** Workflow / study support
- **Status:** Candidate
- **Trigger:** The user asks to learn or review a document sequentially and controls when to advance.
- **Negative trigger:** Do not use the full workflow for a global summary, one isolated passage, or a one-page document.

## Goal

Teach at the user's pace while keeping explanations conceptually complete. Page numbers are navigation anchors, not rigid stopping points.

## Preflight

Before beginning or continuing:

1. Review the full document, including diagrams, tables, annotations, and dependencies between pages.
2. Build an internal topic map with page ranges.
3. Identify prerequisites, natural topic boundaries, repeated concepts, and later sections that qualify earlier statements.
4. Do not expose the internal map unless the user asks for it.

## Delivery units

When the user asks to continue from page `N`:

1. Explain every not-yet-taught topic that begins or appears on page `N`.
2. If the final topic continues onto later pages, continue until its natural conclusion.
3. Stop before the next distinct topic begins, even when the boundary occurs midway through a later page.
4. Do not cut a proof, derivation, example, or tightly connected explanation at a page break.
5. State the page range actually covered when it extends beyond the requested page.
6. Reuse previously taught ideas without repeating full derivations unless new nuance is added.
7. Distinguish document content, prerequisite background, and brief forward references.
8. End after the current coherent unit and wait for the user's instruction.

## Repetition control

Track concepts as:

- **introduced** — mentioned but not fully explained;
- **taught** — explained sufficiently;
- **extended** — revisited with a new result, proof, condition, or application.

When a user asks early about a later concept, teach what is needed now and update the future walkthrough so the original location receives only a proportionate recap plus new material.

## Adaptation

Repeat or deepen an explanation when the user asks, later material changes assumptions, the user shows a misconception, or a recap is necessary for continuity.

## Acceptance checks

- the full document informed the teaching sequence;
- explanations stop at natural topic boundaries;
- page breaks do not cause artificial cuts;
- later sections are not duplicated unnecessarily;
- the user remains in control of when to continue;
- unreadable or missing material is reported rather than fabricated.

## Regression cases

- A derivation begins on page 5 and ends on page 6: cover the complete derivation, then stop.
- Page 8 contains two complete topics and starts a third that ends on page 9: finish all three, then stop.
- The final topic on page 4 ends on page 4: do not add page 5 merely to look ahead.
- The user asks for a whole-document summary: use a summary workflow instead.
