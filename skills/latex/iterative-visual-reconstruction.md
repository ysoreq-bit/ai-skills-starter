# LATEX-001 — Iterative Visual Reconstruction

- **Scope:** Workflow
- **Status:** Candidate
- **Trigger:** A diagram, chart, flowchart, circuit, or technical illustration must be recreated from a visual reference in LaTeX/TikZ.
- **Negative trigger:** Do not use the full workflow for a rough conceptual sketch or when an editable source already exists and needs only a local correction.

## General problem

Writing a complete TikZ picture in one pass mixes geometry, text direction, styling, and fine alignment. Errors become difficult to localize and arbitrary coordinate changes accumulate.

## Method

### 1. Define the comparison target

Record what must match: semantic content, relative positions, visual hierarchy, connectors, labels, reading direction, and page footprint. Do not assume pixel-perfect similarity unless explicitly required.

### 2. Decompose before coding

Split the reference into layers:

- global frame and coordinate system;
- primary shapes or axes;
- connectors and arrows;
- labels;
- secondary details.

For each object, identify its anchor, relation to neighboring objects, and whether its position is structural or cosmetic.

### 3. Build a geometry-only skeleton

Create shapes and connectors before final text. Use temporary short labels or bounding boxes. Confirm proportions and relationships before typography.

### 4. Choose positioning deliberately

Use relative positioning for repeated or logically connected objects, named coordinates and anchors for intersections and connectors, and absolute coordinates only for genuinely free-form geometry or final small corrections.

### 5. Add text as a separate layer

Treat text direction, math mode, font size, and alignment independently from geometry. Mixed RTL, LTR, and mathematics should use dedicated node styles rather than changing the direction of the whole picture.

### 6. Compare in a fixed order

Review each render for:

1. missing or extra objects;
2. global proportions;
3. structural alignment;
4. connector paths;
5. label anchors and collisions;
6. typography and small spacing.

### 7. Change one defect class per iteration

Group edits by cause: anchors, scale, connector routing, text direction, or typography. This preserves causal information and makes regressions easier to identify.

### 8. Extract the reusable part

Retain the checklist, reusable styles, minimal templates, failure modes, and tests. The subject-specific final drawing is not automatically a permanent asset.

## Failed approaches to avoid

- writing the entire drawing in one pass;
- unrelated hard-coded offsets as the primary structure;
- changing font size to solve an anchor problem;
- applying RTL to the complete `tikzpicture`;
- rewriting the whole picture after a local failure;
- judging quality only by compilation success.

## Acceptance checks

- a new diagram can be decomposed before code is written;
- changing one label does not require re-positioning unrelated geometry;
- mixed-direction labels do not mirror or reorder geometry;
- the review record identifies which change solved each visible defect.
