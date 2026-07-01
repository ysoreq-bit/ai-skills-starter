# META-002 — Skill Design and Evaluation

- **Scope:** Meta
- **Status:** Candidate
- **Trigger:** Create, revise, compare, or promote a reusable Skill.
- **Negative trigger:** Do not create a permanent Skill for a one-time task detail.

## Design

1. State the capability in one sentence.
2. Define positive and negative activation contexts.
3. Define required inputs, expected output, dependencies, and failure behavior.
4. Keep the main file focused. Put detailed references, scripts, and templates in separate resources loaded only when needed.
5. Explain the reason behind important rules so the method transfers beyond the original example.
6. Use examples only when they improve activation or output consistency.

## Evaluation set

Prepare realistic prompts for:

- a normal activation case;
- an edge case;
- a negative case where the Skill should remain inactive;
- an older failure when improving an existing Skill.

For objective work, use assertions that can be checked automatically. For subjective work, preserve outputs for human comparison and use a clear review rubric.

## Baseline comparison

Compare the candidate with no Skill or the previous version. Measure:

- correctness;
- requirement coverage;
- unsupported claims;
- regressions;
- time and token use when available;
- number of user corrections;
- unnecessary activation on simple tasks.

## Promotion

- `draft`: extracted but untested;
- `candidate`: one successful implementation or initial tests;
- `verified`: original case, new case, and negative case pass;
- `stable`: repeated successful use across relevant contexts;
- `deprecated`: replaced but retained for history.

The Skill description is part of the implementation. It must describe both the capability and when it should activate.
