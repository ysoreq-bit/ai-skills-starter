# Setup Guide

## Option A — Use this repository as a template

Choose **Use this template** on GitHub and create a repository in your own account. This produces an independent copy that you can personalize and make private.

Recommended when you want your own long-term system and do not need automatic synchronization with this upstream repository.

## Option B — Fork

Create a fork when you want to keep a visible relationship to this repository and periodically incorporate upstream changes.

Keep personal or confidential profiles in private files or a separate private repository. A public fork is not a safe place for private context.

## Option C — Read-only use

An AI tool with read access may use this repository directly without modifying it. The generic Skills will apply, but personal preferences and project-specific knowledge will not persist here.

## Connect an AI tool

Give the AI tool access to your copy using the tool's supported GitHub or local-workspace integration. Confirm whether the connection is read-only or write-capable.

Repository access alone does not guarantee that the agent will consult these files. Add the bootstrap instruction below to the relevant project, workspace, or agent instructions.

## Bootstrap instruction

```text
For complex, multi-step, technical, or artifact-producing tasks, read AGENTS.md, then INDEX.yaml and ROUTER.yaml. Load only the routed Skills and relevant project profile. Apply my current request and project-specific instructions before generic Skills. Before claiming completion, run the relevant verification. Capture only transferable knowledge, not one-off outputs or private source material.
```

## First customization

1. Copy `templates/PROJECT_PROFILE_TEMPLATE.md` into a project-specific folder.
2. Fill in source hierarchy, terminology, protected behavior, and verification requirements.
3. Add only preferences that materially change future results.
4. Keep secrets and private source documents outside the repository.
5. Test one normal case and one negative case before treating a new rule as verified.

## Confirm the setup

Ask the agent:

```text
Read AGENTS.md, INDEX.yaml, and ROUTER.yaml. Tell me which files you would load for a multi-source comparison task, without performing the task.
```

A correct response should select the research route and avoid loading unrelated LaTeX Skills.

## Updating from upstream

Template copies are independent. To receive future changes, compare manually or add the upstream repository as a Git remote.

Forks can use GitHub's synchronization features. Review upstream changes before merging because generic updates may conflict with your local profiles.
