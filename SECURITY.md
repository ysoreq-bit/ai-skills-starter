# Security Policy

## Report privately when possible

Do not open a public issue containing credentials, exploitable private data, or a working secret. Contact the repository owner through a private channel available on their GitHub profile.

## In scope

- committed secrets or credentials;
- unsafe executable hooks or scripts;
- instructions that cause unauthorized repository or file-system changes;
- supply-chain or dependency risks in recommended tools;
- privacy leaks in public templates or fixtures;
- prompt or Skill behavior that bypasses explicit permission boundaries.

## Out of scope

Ordinary disagreements about writing style, unsupported third-party tools not included in the repository, and model behavior outside the documented workflows are not security vulnerabilities.

## Response principles

- rotate exposed secrets immediately;
- remove sensitive content from active branches;
- assess whether history cleanup is necessary;
- preserve evidence without republishing the secret;
- add a regression check or preventive rule when practical.
