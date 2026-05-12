---
name: inbox-schema-enums
description: Inbox file frontmatter has STRICT enum values for source (call/email/recurring/manual) and urgency (critical/high/normal/low). Custom values like "user-stated" / "conversation" / "medium" fail the validator silently and break downstream skills.
metadata:
  type: feedback
---

`schemas/vault/inbox.yaml` enforces these enums on inbox file frontmatter:

| Field | Allowed values |
|---|---|
| `source` | `call`, `email`, `recurring`, `manual` |
| `urgency` | `critical`, `high`, `normal`, `low` |

**Forbidden values I've used incorrectly:**
- `source: user-stated` → use `source: manual`
- `source: conversation` → use `source: manual`
- `urgency: medium` → use `urgency: normal`

The corresponding tags MUST match: `source/manual` not `source/conversation`; `urgency/normal` not `urgency/medium`.

**Why:** `manual` is the canonical "Kay surfaced this directly in conversation, not via a system trigger" value. `normal` is the canonical "needs doing, not urgent" tier. Inventing labels because they read more naturally in English silently fails the schema validator and means downstream skills (pipeline-manager, task-tracker-manager) may skip the file.

**How to apply:** Before writing ANY inbox file, mentally translate any natural-language descriptor I'd pick (medium / general / chat / verbal / user-mentioned) to one of the 4-value enum sets above. If a real new category seems needed, propose extending the enum to Kay — don't invent it on the fly.

**Precipitating trace:** 2026-05-12 — wrote two inbox files (Yahoo→Gmail migration + bday/baby cards) with `source: user-stated` and `source: conversation` + `urgency: medium`. Capture subagent flagged the validator failures; I had to edit both files post-write. Direct hit because I'd never read the enum list.
