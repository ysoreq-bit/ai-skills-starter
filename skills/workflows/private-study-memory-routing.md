# WORKFLOW-007 — Private Study-Memory Routing

- **Scope:** Study workflow
- **Status:** Candidate
- **Trigger:** A substantial study task has authorized access to a compatible private study-memory companion, especially for a mapped course, prior verified knowledge, source lookup, question analysis, exam review, error remediation, course summary, or solution playbook.
- **Negative trigger:** Do not activate for non-study tasks, simple answers that do not need memory, tasks where private memory access is unavailable or unauthorized, requests to rely only on current conversation material, or cases where memory loading would add irrelevant context.
- **Last reviewed:** 2026-07-03

## Capability

Use an optional private study-memory repository as a selective, source-linked companion while keeping private data out of this public method repository.

## Prerequisites

- The user or environment has authorized read access to a compatible private memory repository.
- The repository exposes an agent protocol, index, router, course profile, and current state.
- The task is substantial enough that prior course memory may materially improve source selection, accuracy, continuity, or learner-specific remediation.

## Permission boundary

Read access is not write authorization. A memory update requires an explicit current-conversation request to save, remember, add, update, commit to memory, or otherwise write to the private repository.

Approval of an answer, verification of a claim, or a generally positive response creates no write permission by itself.

## Discovery protocol

1. Read the companion repository's `AGENTS.md`, `INDEX.yaml`, and `ROUTER.yaml`.
2. Identify the active course or study context.
3. Read `courses/<course>/COURSE_PROFILE.md` and `courses/<course>/CURRENT_STATE.md`.
4. Select only the maps and records required by the routed task.
5. Record uncertainty when the active course or route cannot be identified.

## Selective loading

Load the minimum useful context:

- course profile and current state before detailed records;
- topic map or source registry only when needed for scope, provenance, or source fallback;
- assessment index only when exam emphasis, patterns, or remediation are relevant;
- learner-model records only when the user task depends on learner-specific evidence;
- individual concept, theorem, method, exam-pattern, or error records only when targeted by the task.

Do not load the whole private repository or all records for a course by default.

## Source fallback

Return to the authorized source layer when memory is:

- missing;
- stale;
- uncertain;
- contradicted by another memory record or source;
- too imprecise for the task;
- insufficient for exact wording, diagrams, page references, official solutions, or version-sensitive claims.

## Read behavior

Use memory to identify relevant sources, known topic structure, verified claims, recurring solution methods, exam patterns, learner evidence, and open uncertainties. Preserve claim type, confidence, verification status, and source pointers in reasoning and outputs when relevant.

## Write behavior

Treat a possible memory update as two separate decisions:

- `capture_candidate`: content appears reusable or learning-relevant.
- `authorized_capture`: the user explicitly authorizes a repository write in the current conversation.

Before an authorized capture:

1. search for an existing canonical record and likely synonyms;
2. prefer updating or linking existing records over creating duplicates;
3. save only the final, distilled, approved version;
4. avoid raw sources, full conversations, drafts, rejected attempts, and unnecessary private details;
5. report every created or modified path.

## Prohibited behavior

Do not:

- hard-code a private repository name, local path, user account, or credential;
- infer memory contents when access is unavailable;
- copy private memory or source material into the public method repository;
- write because the task was completed, the answer was approved, or a claim was verified;
- write intermediate drafts or superseded answers;
- create a new record before checking for existing canonical records;
- treat `update_when_verified` or similar labels as automatic write authorization.

## Failure behavior

If access, routing, source authority, privacy, or write authorization is unclear, stop before writing and report the exact uncertainty. Continue read-only work only when the remaining authorized context supports the task.

## Acceptance checks

- Read-only use loads only routed, minimal memory records.
- A missing private memory companion causes source fallback or a clear limitation, not guessing.
- Capture candidates remain separate from authorized captures.
- Authorized capture requires explicit current-conversation write permission.
- Existing records are searched before creating new ones.
- No private course content, learner data, Drive identifiers, credentials, or source material are added to the public repository.

## Evaluation cases

### Original case

A user asks for help analyzing a mapped course exam question. The agent reads the companion index, router, active course profile, current state, topic map, and one relevant method record, then returns to the source layer for exact official wording. No memory write occurs.

### Independent new case

A user asks to save a final distilled lesson from a verified recurring mistake. The agent confirms explicit write authorization, searches for an existing error record or learner pattern, updates the best existing record or creates one only if needed, and reports changed paths.

### Negative case

The user says an answer is "good" after a study session but does not ask to save it. The agent may mention that the lesson could be saved on request, but it does not write to the private memory repository.

## Evidence and provenance

- **Source:** Repeated need to separate public reusable methods from private academic memory and to prevent implicit writes.
- **Confidence:** Candidate; requires validation on a read-only study task, an authorized capture task, and a negative no-save case.
- **Related files:** `docs/STUDY_MEMORY_INTERFACE.md`, `skills/meta/knowledge-capture.md`, `skills/core/source-integrity.md`, `skills/core/verification-before-completion.md`.

## Changelog

- 2026-07-03 — Initial candidate draft.
