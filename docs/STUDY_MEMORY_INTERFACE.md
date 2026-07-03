# Study Memory Interface

## Purpose

This document defines a generic interface for an optional private study-memory companion repository. It lets an agent use private, source-linked academic memory without adding private data, fixed account names, local paths, credentials, or hard dependencies to this public repository.

## Layer model

1. **Source layer:** Google Drive, uploaded files, official course sites, and other authorized systems remain authoritative for exact wording, diagrams, pages, official solutions, and original versions.
2. **Memory layer:** a private study-memory repository stores compact, distilled, source-linked course and learner records.
3. **Method layer:** this public repository stores reusable routing, verification, and workflow methods.

The memory layer assists source-aware work. It is not an automatic substitute for the source layer.

## Expected companion structure

A compatible private memory repository is expected to expose:

```text
AGENTS.md
INDEX.yaml
ROUTER.yaml
courses/<course>/COURSE_PROFILE.md
courses/<course>/CURRENT_STATE.md
```

It may also expose routed maps and records such as topic maps, source registries, assessment indexes, concept notes, theorem notes, solution methods, exam patterns, error records, and learner-model records.

## Discovery protocol

When a substantial study task has authorized access to a compatible private memory repository:

1. read `AGENTS.md`, `INDEX.yaml`, and `ROUTER.yaml`;
2. identify the active course or study context;
3. read `courses/<course>/COURSE_PROFILE.md` and `courses/<course>/CURRENT_STATE.md`;
4. load only the routed records and maps needed for the task;
5. do not load the whole repository or whole course by default.

No access is also a valid state. If the private memory repository is unavailable, continue from the authorized source layer or ask for the missing source context instead of guessing.

## Selective loading

Use memory selectively:

- course profile and current state first;
- source registry, topic map, assessment index, or specific records only when routed;
- learner-model records only when the task requires learner-specific context;
- original sources when memory is missing, stale, uncertain, contradictory, or insufficiently precise.

## Read behavior

For read-only use, the agent may use private memory to find source pointers, recall verified course structure, retrieve known methods, and identify known uncertainties. Private memory claims must retain their provenance, confidence, and verification status.

Do not expose private memory contents into public repository files. Public outputs should avoid private identifiers unless the user explicitly requests them in a private context.

## Write behavior

Repository access does not imply permission to write.

Writing to a private memory repository requires all of:

- explicit user authorization to save, remember, add, update, or otherwise write in the current conversation;
- a final or distilled record, not a draft or rejected attempt;
- a search for an existing canonical record or likely duplicate;
- no copied raw source material, scanned exams, secrets, credentials, or unnecessary private content;
- precise reporting of created and modified paths.

Useful output, verification, or approval of answer content may create a capture candidate. It does not authorize a write.

## Prohibited behavior

Do not:

- require an automatic clone, credential, account, or local path;
- treat lack of memory access as an error that justifies guessing;
- copy private memory contents into this public repository;
- copy raw source files or copyrighted collections into memory;
- write to memory without explicit opt-in in the current conversation;
- store full conversations when a concise durable representation is enough;
- create duplicate records before searching for existing ones.

## Failure behavior

If routing is ambiguous, memory is unavailable, a source pointer is stale, a privacy risk appears, or a write request is not explicit, stop the write path and report the uncertainty. Continue read-only work only when the remaining sources support it.

## Acceptance checks

- Read-only tasks load only the minimal relevant memory records.
- Authorized capture searches for an existing record before writing.
- Content approval without a save request does not write to memory.
- Source fallback happens when memory is uncertain or insufficient.
- No private content, paths, Drive identifiers, learner data, or credentials enter this public repository.
