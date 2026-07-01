# CORE-003 — Verification Before Completion

- **Scope:** Global
- **Status:** Candidate
- **Trigger:** Before claiming that work is complete, correct, fixed, compiled, validated, or ready to use.
- **Negative trigger:** None for completion claims; the amount of verification may scale with risk.

## Gate

Before making a positive status claim:

1. Identify what evidence would prove the exact claim.
2. Run or inspect the complete relevant check freshly.
3. Read the full result, including exit status, warnings, omissions, and changed files.
4. Compare the evidence with the claim.
5. Report the actual state and any remaining limitations.

## Evidence by claim

| Claim | Minimum evidence |
|---|---|
| File created | Confirm exact path and readable file |
| Code or script works | Relevant test or reproducible execution succeeds |
| LaTeX compiles | Correct engine returns success; inspect warnings and output pages |
| Visual artifact matches | Rendered output reviewed against requirements or reference |
| Bug fixed | Original reproduction no longer fails; regression check when practical |
| Source-based answer is complete | Source coverage and attribution reviewed |
| Requirements satisfied | Each requirement mapped to output or an explicit gap |
| Repository change ready | Diff reviewed and automated checks completed |

## Insufficient evidence

- an earlier run rather than a fresh check;
- a linter when compilation is the claim;
- compilation when visual fidelity is the claim;
- an agent success report without inspecting the changed artifact;
- partial tests generalized to the whole project;
- confidence, plausibility, or absence of an obvious error.

## Regression verification

For a new regression test, demonstrate both the failure condition and the corrected condition when feasible. A test that only passes after a correction does not prove that it detects the original problem.

## Reporting

State what was checked, the result, what was not checked, and whether the current status is complete, partial, or blocked.
