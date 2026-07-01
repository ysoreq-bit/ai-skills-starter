# LATEX-002 — Mixed-Direction Text in TikZ

- **Scope:** Domain / workflow
- **Status:** Candidate
- **Trigger:** A TikZ picture contains RTL prose together with LTR text, numbers, or mathematical notation.
- **Negative trigger:** Do not add direction wrappers to a picture containing only mathematics or LTR text.

## Invariant

TikZ geometry remains in its normal coordinate direction. Directionality is applied only to the textual content that requires it.

## Method

1. Keep `tikzpicture`, coordinates, paths, anchors, and transformations outside broad RTL wrappers.
2. Define separate node styles for RTL prose, LTR prose, mathematical labels, and mixed labels.
3. Choose the node anchor from geometry before adding manual offsets.
4. Isolate mathematical notation from surrounding RTL text using the host document's established direction commands.
5. Test multi-line labels separately because line breaking changes the node bounding box.
6. Inspect rendered bounding boxes when labels overlap; visible text width may differ from node width.

## Diagnostic order for a misplaced label

1. Is the anchor appropriate?
2. Is the text direction correct?
3. Is the alignment correct?
4. Is a font or math wrapper changing the bounding box?
5. Only then adjust `xshift` or `yshift`.

## Common failure modes

- the entire diagram is mirrored because an RTL environment wraps the picture;
- punctuation and numbers appear in the wrong order;
- a correct label overlaps a line because the anchor is centered rather than edge-aligned;
- repeated arbitrary shifts make later edits unstable.

## Acceptance checks

- geometry remains unchanged when an RTL label is replaced by an LTR label of similar size;
- prose, numbers, and mathematics render in the intended reading order;
- a label can be moved by changing its anchor without editing the underlying path;
- a pure-math negative fixture compiles without unnecessary direction wrappers.
