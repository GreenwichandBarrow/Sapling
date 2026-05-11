---
name: Never batch-update records without Kay's review
description: Don't mass-update CRM records, pipeline entries, or contacts overnight. Always present changes for approval first.
type: feedback
---

Never run batch updates to CRM records (Attio People, pipeline entries) without Kay reviewing each change first.

**Why:** Kay caught this during the network migration. The agent was updating 111 People records with relationship_type, nurture_cadence, etc. based on best guesses. But we only validated one record together (Dan Tanzilli). The other 110 could have errors that are hard to undo.

**How to apply:** For migrations and bulk updates, always use the recommend-then-approve pattern:
1. Agent collects data and proposes changes
2. Present a summary to Kay for review (can be batched in groups)
3. Only execute after approval
4. Never run destructive/bulk CRM changes as overnight background jobs
