# Customization Guide

## Keep three layers separate

### Global Skills

Reusable methods that should work for many users and projects. Examples: source integrity, systematic debugging, and verification before completion.

### Project profiles

Local rules for one course, repository, client, document family, or workflow. Project profiles may override generic preferences when the override is explicit.

### One-off instructions

Temporary requirements for the current request or artifact. Do not promote them automatically into persistent rules.

## What belongs in a project profile?

Include information that materially changes future work:

- governing sources and their priority;
- required terminology;
- output format and structure;
- non-fabrication rules;
- protected user edits;
- tools, versions, and cost constraints;
- verification requirements;
- project-specific exceptions.

Avoid biography, unrelated preferences, complete conversation transcripts, and private source documents.

## Add a new Skill

1. Copy `templates/SKILL_TEMPLATE.md`.
2. Give the Skill a stable ID and narrow name.
3. Define a positive trigger and a negative trigger.
4. Explain the reusable method and known bad approaches.
5. Add observable acceptance checks.
6. Test an original case, a new case, and a non-activation case.
7. Add the Skill to `INDEX.yaml`, `ROUTER.yaml`, and `registry/capabilities.md`.
8. Keep the status `draft` or `candidate` until evidence supports promotion.

## Avoid instruction inflation

More instructions do not automatically improve an agent. Broad or overlapping Skills can make results worse.

Prefer:

- one clear capability per Skill;
- selective loading;
- concise main files with optional references;
- explicit conflict priority;
- measurable evaluations;
- deletion or deprecation of rules that do not help.

## Suggested private structure

```text
profiles/
  user-profile.md
  projects/
    project-a.md
    project-b.md
private-sources/
  README.md
```

A public starter should not contain the contents of these files. Keep the private layer in a private repository or local workspace.

## Compatible private study memory

For recurring academic work, a private memory companion can hold distilled course maps, current state, verified notes, solution methods, exam patterns, and learner records. Keep the companion generic at the interface level:

- expose an agent protocol, index, router, course profile, and current state;
- route agents to the smallest relevant course records;
- keep raw sources in the authorized source system;
- require explicit opt-in before any write;
- report exactly which paths changed after an authorized save.

Do not add private repository paths, course contents, account names, Drive identifiers, or learner details to this public starter.

## Review schedule

Review active Skills when:

- the user corrects the same behavior repeatedly;
- a tool or dependency changes version;
- a Skill activates on irrelevant tasks;
- a previously successful method causes a regression;
- a new public method appears to overlap with an existing one.
