# AI Skills Starter

A public, reusable, and testable system for giving ChatGPT, Codex, and other AI agents durable working methods.

This repository is a **starter template**, not a finished personality or a collection of project outputs. It helps an agent reuse proven workflows for planning, research, debugging, verification, document work, knowledge capture, and LaTeX tasks.

## What changes for the user?

Usually, nothing about how you write requests. You continue speaking naturally. For complex tasks, the agent reads `INDEX.yaml` and `ROUTER.yaml`, loads only the relevant Skills, performs the task, verifies its claims, and captures reusable lessons when appropriate.

## Start in three steps

**Hebrew setup guide:** [`docs/ONBOARDING_HE.md`](docs/ONBOARDING_HE.md)

### 1. Create your own copy

Choose one:

- **Use this template** — create an independent repository for your own system.
- **Fork** — keep a link to this repository and pull future updates.
- **Clone** — work locally with Git.

### 2. Connect your copy to your AI tool

Give ChatGPT, Codex, or another compatible agent access to the repository. The exact connection method depends on the tool.

### 3. Give the bootstrap instruction

Use this instruction in the project or agent that should use the repository:

> For complex, multi-step, technical, or artifact-producing tasks, read `AGENTS.md`, then `INDEX.yaml` and `ROUTER.yaml`. Load only the routed Skills. Follow project-specific instructions over generic Skills. Before claiming completion, run the relevant verification. Capture only transferable knowledge, not one-off outputs or private source material.

## Repository structure

```text
AGENTS.md              Operating protocol and instruction priority
INDEX.yaml             Main entry points and capability inventory
ROUTER.yaml            Task classification and selective loading
skills/                Reusable methods and workflows
templates/             Starting points for new Skills and project profiles
registry/              Capability and known-issue indexes
scripts/               Free local validation tools
tests/                 Regression and structural tests
docs/                  Setup, customization, architecture, and privacy guidance
research/               Reviewed external sources and adoption decisions
tools/                  Optional free tools and selection guidance
```

## Included capabilities

- source integrity and non-fabrication;
- requirements-first artifact creation;
- systematic debugging;
- verification before completion claims;
- page-by-page document teaching;
- evidence-mapped course summaries with assessment-informed emphasis;
- course solution playbooks, SOPs, decision trees, and detailed flowcharts;
- single-question error diagnosis, conceptual repair, and transfer testing;
- full-exam diagnostic review, pattern detection, and prioritized remediation planning;
- multi-source research synthesis;
- durable knowledge capture;
- external Skill and tool intake;
- Skill design and baseline evaluation;
- LaTeX layout, TikZ, and mixed-direction text methods.

All capabilities begin as `candidate` unless their own file states otherwise. A method should become `verified` only after it passes an original case, a genuinely new case, and a negative case where it should not activate.

## Personalize safely

Start with the templates in `templates/`. Add personal preferences and project profiles only to your own copy. Do not commit passwords, tokens, private keys, private medical information, copyrighted course material, or confidential source documents.

## Public source policy

External Skills and tools are reviewed individually. Popularity is not proof of usefulness. Each adopted method should have a clear source, license treatment, activation boundary, and comparison against the current baseline. See `THIRD_PARTY_NOTICES.md` and `research/`.

## License

The original material in this repository is licensed under the Apache License 2.0. Third-party projects retain their own licenses; see `THIRD_PARTY_NOTICES.md`.

## Status

Version `0.1.2` adds single-question error remediation and full-exam diagnostic review workflows. The system remains intentionally small enough to understand, customize, and test.
