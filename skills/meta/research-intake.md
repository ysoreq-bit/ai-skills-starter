# META-001 — External Method and Tool Intake

- **Scope:** Meta
- **Status:** Candidate
- **Trigger:** A public prompt, Skill, template, script, workflow, plugin, or tool is considered for use.
- **Negative trigger:** Skip the full process when a source is mentioned only as background and no part will be used or recorded.

## Review sequence

1. Record repository, path, author, version or review date, and license scope.
2. Summarize intended behavior, activation context, dependencies, outputs, and side effects.
3. Inspect supporting scripts, hooks, assets, network access, and file-system behavior that materially affect safety or results.
4. Select a use mode:
   - licensed adaptation;
   - independently written method informed by the source;
   - external tool dependency;
   - reference only;
   - rejected or deferred.
5. Compare assumptions with the actual user environment, privacy needs, languages, budget, and tool versions.
6. Define positive and negative activation examples.
7. Create at least one realistic evaluation prompt and one non-activation prompt.
8. Compare the candidate with the current workflow or no-Skill baseline.
9. Record attribution and license obligations when retained material requires them.
10. Promote only when the candidate improves a relevant outcome without unacceptable regressions.

## Defer when

- source or reuse terms are unclear;
- instructions conflict with the user's current request;
- executable dependencies have not been reviewed;
- the core workflow requires an unavailable or paid service;
- guidance targets an incompatible version;
- activation boundaries are too broad;
- equivalent behavior already exists with no demonstrated advantage.

## Required record

Each retained candidate identifies source, use mode, scope, trigger, negative trigger, dependencies, limitations, evaluation method, status, and last review date.
