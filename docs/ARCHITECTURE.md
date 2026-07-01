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
