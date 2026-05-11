---
name: Skill rules live in the skill build, not in template documents
description: Voice rules, validation rules, workflow rules, etc. belong in SKILL.md and references/. Template documents (Sheets, Docs, Drive files) should contain ONLY template content — no rule commentary, no voice-rule preambles, no "how to use" meta-instructions.
type: feedback
originSessionId: 79db8074-299b-4018-a98a-3aced9a42eb3
---
Templates and skill rules are separate layers. Never mix them.

**Skill layer (SKILL.md + references/):**
- Voice rules (no em dashes, warm opener, sign-off style)
- Audience taxonomy and classification logic
- Variable substitution order
- Validation gates
- Workflow (when/how to trigger, ordering, escalations)

**Template layer (Google Sheets/Docs in Drive):**
- Just the template content (subject + body with variables)
- Optional: one-line operational note per template row (e.g., "Use when intermediary pitched a specific deal")
- That's it.

**Why:** Kay reviews templates to see what the email actually reads like. Stuffing rule enumerations into the template doc (e.g., "Voice rules baked in: no em dashes, warm opener, no fund language...") clutters her review surface with metadata that is Claude's responsibility, not hers. The rules live IN the skill — that's the point of the skill. If a reader opens the template doc, they should see templates, not policy.

**How to apply:**
- When creating a review/preview doc for templates: show subject, body, recipient mapping, summary. Nothing else.
- Never write "voice rules baked in:" or "How to use this doc" meta-sections in a template doc.
- Never list skill validation gates in a template doc.
- Never put "voice rules" or "audience taxonomy" sections in a template-store Sheet.
- The template-store Sheet can have a "notes" column per template row for one-line operational context (e.g., "Use when deal mentioned"). That's inline per-template, not a global rule dump.
- If Kay asks "what are the rules?", point her to SKILL.md and references/, not the template doc.
- When in doubt: if the content would appear in every template doc for any skill, it's a skill-level rule and belongs in SKILL.md.

**Precedent:** 2026-04-23 conference-engagement build. I included a "Voice rules baked in: no em dashes, warm opener, Very best/Kay sign-off, no 'fund' or PE language, no thesis leaks, $2-5M EBITDA" line in the review Google Doc. Kay flagged: "Shouldn't those be in the skill build itself?" She was right. Fixed by stripping the rule preamble and "How to use this doc" section from the doc.
