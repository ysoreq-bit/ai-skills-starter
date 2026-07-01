# LATEX-004 — Vertical Spacing Diagnosis

- **Scope:** Domain / workflow
- **Status:** Candidate
- **Trigger:** Large or inconsistent vertical gaps appear without an obvious semantic reason.
- **Negative trigger:** Do not normalize spacing explicitly required by a source document or deliberate design.

## Principle

Classify the source of the space before changing it. Not every gap is caused by a local spacing command.

## Cause categories

### Explicit spacing

Search near the gap for manual spacing commands, forced line-break spacing, fill commands, or custom macros that expand to spacing. Document every justified exception.

### Page-height stretching

Check whether flexible vertical space is being stretched to align page bottoms. Compare a minimal copy using ragged-bottom page construction. Treat this as a template-level decision, not a local patch.

### Float placement

Check whether a figure or table cannot fit at the requested position. Review placement options, float size, barriers, and forced-placement usage.

### Non-breakable content

Large minipages, boxes, displays, and diagrams can force the next block to another page and leave unused space.

### Heading, list, or display glue

Inspect class and package settings for heading spacing, list parameters, and display-math skips before adding local corrections.

## Diagnostic procedure

1. Mark the exact top and bottom boundaries of the unexpected gap.
2. Identify the semantic blocks immediately around it.
3. Search for explicit spacing and macro expansion.
4. Determine whether a float or non-breakable block moved.
5. Compare page-height construction in a minimal copy.
6. Inspect heading, list, and display settings.
7. Change one cause at a time and record the effect.
8. Promote a correction to a shared template only after success in more than one relevant document.

## Acceptance checks

- the cause category is recorded rather than guessed;
- the correction removes the target gap without changing unrelated pages;
- a negative fixture with deliberate spacing remains unchanged;
- no arbitrary spacing becomes a hidden structural dependency.
