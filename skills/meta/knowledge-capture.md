# META-003 — Durable Knowledge Capture

- **Scope:** Meta
- **Status:** Candidate
- **Trigger:** A conversation produces a reusable decision, method, lesson, FAQ, correction, project rule, or known issue.
- **Negative trigger:** Do not capture ordinary transient discussion, facts with no expected future value, or any private-repository write that the user did not explicitly authorize in the current conversation.

## Classify the record

Choose one primary type:

- decision;
- how-to or workflow;
- FAQ;
- concept or reference note;
- lesson learned;
- project rule;
- known issue.

## Before creating

1. Search the repository for the same concept and synonyms.
2. Prefer updating or linking an existing record over creating a duplicate.
3. Identify audience, scope, freshness, and source authority.

## Extract

Preserve the parts relevant to the record type:

- concise summary;
- context and problem;
- decision or method;
- rationale and alternatives;
- prerequisites and dependencies;
- steps or rules;
- edge cases and negative triggers;
- source and confidence;
- follow-up tasks;
- last reviewed date.

Do not copy the entire conversation when a shorter durable representation is sufficient.

## Private memory write boundary

Separate three states:

1. **Capture candidate:** an insight, correction, method, or course claim may be worth preserving.
2. **Prepared record:** a concise final or distilled record has been drafted and checked against existing records.
3. **Authorized capture:** the user explicitly requests a repository write in the current conversation.

The first two states do not authorize writing. Phrases such as "that is good", "correct", "done", "useful", or approval of an answer are content feedback only unless the user also asks to save, remember, add, update, commit to memory, or otherwise write to the private memory repository.

Before writing to a private memory repository:

1. confirm the user requested the write in the current conversation;
2. search for an existing canonical record and likely synonyms;
3. write only the final, distilled, approved content;
4. avoid drafts, rejected attempts, full conversations, raw source files, scanned exams, secrets, and private source contents;
5. report created and modified paths precisely.

## Link and maintain

- link related Skills, profiles, issues, templates, and tests;
- record a short changelog when updating an established rule;
- mark replaced guidance as deprecated rather than silently erasing history;
- create a follow-up issue when evidence is incomplete but the question matters.

## Quality check

A future reader should understand what to do, when it applies, why it exists, what not to do, and where the evidence came from without reopening the original conversation.
