# CORE-002 — Systematic Debugging

- **Scope:** Global workflow
- **Status:** Candidate
- **Trigger:** A technical process, document, tool, script, build, or generated artifact behaves unexpectedly.
- **Negative trigger:** Do not invoke the full workflow for a known deterministic correction whose cause and regression test already exist.

## Rule

Investigate the cause before proposing a correction. A visible symptom is not sufficient evidence of the root cause.

## Phase 1 — Evidence

1. Read all errors and warnings, including paths and line numbers.
2. Reproduce the problem and record exact steps and environment.
3. Identify recent changes that could affect the behavior.
4. For multi-stage workflows, inspect input and output at every boundary.
5. Trace an invalid value or state backward to its first incorrect origin.
6. When reproduction is inconsistent, gather more evidence instead of guessing.

## Phase 2 — Comparison

1. Find the nearest working example in the same environment.
2. Read the relevant reference far enough to understand its assumptions.
3. List differences between the working and failing cases.
4. Identify required packages, settings, files, versions, and hidden state.

## Phase 3 — Hypothesis

1. State one specific hypothesis: cause, evidence, and predicted observation.
2. Change the smallest possible variable.
3. Run the relevant check.
4. If the prediction fails, revise or discard the hypothesis instead of stacking another correction on top.

## Phase 4 — Correction and verification

1. Preserve or create the smallest failing example.
2. Correct the identified cause with one focused change.
3. Run the original reproduction and relevant regression checks.
4. Verify that unrelated behavior remains intact.
5. Record the confirmed cause and the evidence that distinguishes it from plausible alternatives.

## Escalation

After three unsuccessful correction attempts, stop adding local patches. Reconsider the architecture, template, dependency choice, assumptions, or problem framing.

## Warning signs

- proposing a correction before reproduction;
- changing multiple variables at once;
- hiding a structural symptom with arbitrary offsets or spacing;
- trusting a generated success message without inspecting the output;
- continuing with “one more attempt” after repeated unrelated failures.
