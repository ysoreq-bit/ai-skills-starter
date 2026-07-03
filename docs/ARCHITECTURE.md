# Architecture

## Design goals

The system should be:

- easy to use through natural language;
- selective rather than loading every instruction;
- testable and versioned;
- safe for private project extensions;
- portable across compatible AI agents;
- explicit about uncertainty and provenance.

## Control flow

```text
User request
    ↓
AGENTS.md — permission and instruction priority
    ↓
INDEX.yaml — entry points and capability inventory
    ↓
ROUTER.yaml — task classification
    ↓
Relevant Skills + project profile + known issues
    ↓
Execution
    ↓
Verification
    ↓
Optional reusable-knowledge capture
```

## Why selective loading?

A large instruction collection can waste context and cause irrelevant rules to activate. The Router points the agent to the smallest useful set of files for the current task.

## Skill anatomy

A durable Skill should include:

- scope and lifecycle status;
- trigger and negative trigger;
- capability and problem;
- method;
- failure behavior;
- prohibited approaches;
- acceptance checks;
- evaluation cases;
- evidence and provenance.

## Lifecycle

```text
draft → candidate → verified → stable → deprecated
```

Promotion is evidence-based. A persuasive description or one successful output is insufficient.

## Public and private layers

The public repository contains generic methods, synthetic fixtures, templates, and public source notices.

A private user copy may add project profiles, personal preferences, source pointers, and private issue history. Private source documents should remain outside the public repository and should be included only when necessary and authorized.

## Private capability incubator

Users may also maintain a separate private AI-capabilities repository for workflows, prompts, routing experiments, evaluations, and personal operating rules. Treat that repository as the default place to improve private behavior quickly.

This public repository is the sanitized publication layer. Promote from a private capability incubator only after applying `docs/CAPABILITY_PROMOTION.md`: remove private details, replace real examples with safe examples, validate activation and non-activation cases, and keep the public diff reviewable.

The public layer must not depend on access to the private incubator. If the incubator is unavailable, public Skills should still work from their checked-in instructions and public fixtures.

## Private study-memory companion

Some users may keep course memory in a separate private repository. In that arrangement:

- the source layer remains the authority for exact wording, diagrams, pages, official solutions, and source versions;
- the private memory layer stores compact, source-linked, searchable course and learner records;
- a private capability incubator may refine user-specific workflows;
- this public method layer stores only sanitized reusable routing and verification methods.

The public layer must not require a fixed private repository name, local path, account, clone, or credential. It may describe the interface expected from a compatible memory companion, but it must not contain private course names, learner records, source contents, Drive identifiers, or private links.

Read access to a private memory companion is optional and selective. Write access is separately gated: a useful insight, verified claim, or approved answer may become a capture candidate, but it is not written unless the user explicitly authorizes repository writing in the current conversation.

## Agent portability

Different tools discover instructions differently. This repository therefore uses ordinary Markdown and YAML rather than depending on one proprietary runtime.

The user or workspace must still instruct the agent to read `AGENTS.md`, `INDEX.yaml`, and `ROUTER.yaml`. Tool-specific adapters may be added later without changing the underlying Skills.

## Verification layers

- **Structural:** files exist, schemas parse, environments balance.
- **Functional:** scripts, tests, or commands succeed.
- **Factual:** sources support the claims.
- **Computational:** independent checks reproduce the result.
- **Visual:** rendered artifacts match requirements or references.
- **Behavioral:** the Skill activates when appropriate and stays inactive otherwise.
