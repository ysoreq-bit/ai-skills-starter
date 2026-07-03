# Operating Protocol for AI Agents

This file defines how an AI agent should use this repository.

## 1. Permission boundary

Repository access does not imply permission to change it.

- Read-only agents may inspect and apply the Skills.
- Write-capable agents may modify files only when the user or repository owner has authorized repository changes.
- Prefer reversible work: branches, commits, pull requests, and clearly scoped edits.
- Never force-push, rewrite published history, expose secrets, or delete approved knowledge without explicit authorization.
- Do not modify other repositories unless separately authorized.

## 2. Repository purpose

This repository is a source of reusable capabilities: methods, decision procedures, templates, tests, diagnostics, and workflows that can improve future tasks.

It is not primarily an archive of completed outputs. A difficult report, diagram, analysis, or debugging session is evidence from which a transferable method may be extracted. The one-off final artifact is not automatically a permanent asset.

Prefer:

- general rules over subject-specific answers;
- minimal synthetic examples over private documents;
- tested procedures over persuasive prose;
- clear activation and non-activation conditions;
- evidence-backed updates over silent behavioral changes.

## 3. Before a complex task

Treat a task as complex when it is multi-step, technical, expensive, artifact-producing, easy to regress, source-dependent, or part of a continuing project.

For a complex task:

1. Read `INDEX.yaml` and `ROUTER.yaml`.
2. Classify the task.
3. Load only the routed Skills, templates, project profile, and known issues.
4. Apply the user's current request and project-specific instructions before generic Skills.
5. Preserve the user's current artifact and edits.
6. Make missing information and uncertainty explicit.

Do not load the entire repository for a simple, unrelated request.

## 4. Optional private study memory

A user may authorize access to a separate private study-memory repository. Treat that repository as an optional companion memory layer, not as part of this public method repository.

When a substantial study task has authorized access to a compatible private memory repository:

1. read that repository's agent protocol, index, and router;
2. identify the active course or study context;
3. read only the active course profile, current state, and the smallest routed records needed for the task;
4. return to the original authorized source layer when memory is missing, stale, uncertain, contradictory, or not precise enough;
5. keep private memory contents, private paths, learner information, and source material out of this public repository.

Repository access is not write authorization. Writing to a private memory repository requires an explicit user request to save, remember, add, update, or otherwise change that repository in the current conversation.

## 5. Private capability incubation

A user may maintain a private AI-capabilities repository for draft workflows, personal routing, prompt variants, evaluations, and project-specific behavior. Treat that repository as the preferred incubation layer for private method development.

Promote into this public repository only through `docs/CAPABILITY_PROMOTION.md`. The promoted form must be sanitized, reusable, evaluated, and independent of private repository access.

## 6. Instruction priority

When instructions conflict, use this order:

1. safety, privacy, law, and explicit permission boundaries;
2. the user's current explicit request;
3. artifact-specific requirements;
4. project profile and approved project decisions;
5. workflow or domain Skill;
6. general preferences;
7. model defaults.

Within one level:

- an explicit prohibition overrides a preference;
- a newer approved rule overrides an older one;
- a matching specific trigger overrides a generic rule;
- an authoritative source overrides an example;
- uncertainty must be reported rather than hidden.

## 7. Verification before completion

Before claiming that work is complete, correct, fixed, compiled, verified, or ready:

1. identify what evidence proves the exact claim;
2. run or inspect the relevant check freshly;
3. read the full result, including warnings and omissions;
4. compare the evidence with the claim;
5. report remaining limitations.

Compilation does not prove visual fidelity. A linter does not prove a build. A generated success message does not replace inspection of the artifact or diff.

## 8. Capturing reusable knowledge

Capture new knowledge only when the task produces a reusable method, repeated correction, expensive insight, known failure mode, verified improvement, template, or test.

Before promoting knowledge, record:

- the general problem;
- evidence and provenance;
- failed and successful approaches;
- trigger and negative trigger;
- overlap with existing rules;
- acceptance or regression tests;
- lifecycle status.

Do not promote a one-off preference or final project output merely because it required effort.

## 9. Skill lifecycle

- `draft` — extracted idea, not validated;
- `candidate` — initial implementation or one successful case;
- `verified` — original case, new case, and negative case pass;
- `stable` — repeated successful use across relevant contexts;
- `deprecated` — replaced but retained for history.

## 10. Privacy and source material

Do not commit secrets, credentials, private keys, private medical information, confidential documents, or copyrighted source collections.

Prefer derived methods, original reusable code, small authorized or synthetic fixtures, redacted examples, hashes, and source pointers.

## 11. External methods and tools

Before adopting a public Skill, prompt, script, plugin, or tool, use `skills/meta/research-intake.md`.

Do not import collections wholesale. Review source, license, dependencies, assumptions, activation boundaries, security behavior, and baseline performance.

## 12. Repository changes

When authorized to write:

- use descriptive branches for meaningful changes;
- keep commits logically scoped;
- run available tests before opening or merging a pull request;
- preserve third-party notices;
- do not silently change global behavior.
