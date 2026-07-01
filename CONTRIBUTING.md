# Contributing

Contributions are welcome when they improve a reusable capability without introducing private data, unclear licensing, or unnecessary instruction weight.

## Before proposing a change

1. Search the capability registry and open issues for overlap.
2. Identify the problem, trigger, and negative trigger.
3. Explain why the current baseline is insufficient.
4. Review source and license obligations for any public material used.
5. Prepare a realistic normal case, independent case, and non-activation case.

## Pull request expectations

A pull request should include:

- a concise problem statement;
- exact files changed;
- lifecycle status of new or modified Skills;
- evidence or evaluation method;
- privacy review;
- license and attribution updates when applicable;
- test results and known limitations.

## Skill changes

Use `templates/SKILL_TEMPLATE.md`. Avoid combining unrelated capabilities in one Skill. Keep detailed references and scripts separate from the main instruction file when they are not always needed.

Do not mark a Skill `verified` or `stable` based only on persuasive wording or one successful output.

## Public safety

Do not submit secrets, private source documents, personal records, copyrighted collections, or identifiable chat exports. Use synthetic fixtures and redacted examples.

## Commit style

Prefer small, descriptive commits such as:

```text
feat: add requirements traceability Skill
test: add negative activation case
docs: clarify privacy boundary
fix: prevent page transition inside minipage
```

## Third-party material

Do not copy material with unclear reuse terms. Preserve required copyright and attribution notices, and update `THIRD_PARTY_NOTICES.md`.
