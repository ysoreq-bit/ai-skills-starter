# Privacy and Public-Repository Safety

A public repository is readable, cloneable, indexable, and permanently copyable. Removing a file later does not guarantee that earlier copies disappear.

## Never commit

- passwords, API tokens, cookies, private keys, or recovery codes;
- personal medical or financial records;
- private conversations or full chat exports;
- confidential client or employer material;
- copyrighted textbooks, lecture notes, exams, or answer collections without permission;
- private email addresses, phone numbers, addresses, or identifiers;
- source files that contain hidden metadata or credentials.

## Prefer

- general methods derived from private work;
- redacted or synthetic examples;
- filenames, hashes, and private source pointers instead of source contents;
- minimal fixtures that reproduce a failure without exposing the original project;
- a separate private repository for personal profiles and source material.

## Before publishing a change

1. Review the full diff, not only the files you intended to change.
2. Search for names, email addresses, tokens, URLs, and copied source passages.
3. Check images, PDFs, ZIP files, and document metadata.
4. Confirm that every third-party excerpt is permitted and attributed.
5. Run automated secret scanning when available.
6. Assume that merged history may be copied permanently.

## If a secret is committed

Deleting the file is not enough. Revoke or rotate the secret immediately, then follow the hosting provider's guidance for history cleanup. Report the incident without reposting the secret.
