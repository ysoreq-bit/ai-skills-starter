# LATEX-003 — Page-Flow and Container Debugging

- **Scope:** Domain / workflow
- **Status:** Candidate
- **Trigger:** A section begins unusually low on a page, content uses only part of the page width, or a page transition behaves unexpectedly.
- **Negative trigger:** Do not apply structural container fixes when the page break is intentional and environments are balanced.

## Principle

Trace page-flow symptoms to the active environment stack before adding spacing or page-break commands.

## Diagnostic procedure

1. Preserve the failing source and rendered output.
2. Locate the first page where layout diverges.
3. Inspect the source immediately before that point.
4. Check for open or mismatched containers such as `minipage`, `multicols`, `figure`, `table`, `tikzpicture`, boxes, column modes, and local groups.
5. Check whether a page transition command appears inside a container that cannot break across pages.
6. Replace complex content temporarily with a small placeholder. If normal flow returns, reduce the original content until the minimal cause remains.
7. Apply the smallest structural correction: close or move the environment, split the box, or relocate the transition.
8. Recompile from a clean auxiliary state when needed.
9. Add a regression fixture that fails before the correction and passes after it.

## Repairs to avoid

- repeated page-transition commands without checking the environment stack;
- large manual vertical gaps used to move content;
- rewriting unrelated sections;
- treating partial-width content as a font or margin problem before checking columns and boxes.

## Acceptance checks

- all environments close in the intended order;
- page transitions occur outside non-breakable containers;
- the next section begins at the expected position and full text width;
- removing the correction reproduces the minimal failing fixture.
