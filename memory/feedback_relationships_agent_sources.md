---
name: Relationships Agent Must Use All Data Sources
description: The relationships agent must pull from every available source to enrich People records, not just Attio data
type: feedback
---

Relationships agent must use ALL available sources to enrich People attributes in Attio:
1. **Attio** — existing record data (live query)
2. **Vault calls** — brain/calls/ (all transcripts: Fireflies + Granola)
3. **Vault inbox** — brain/inbox/ (Gmail items ingested here)

Once vault ingestion is fully wired, the agent reads the vault, not external APIs directly. Gmail via gog is a fallback until inbox ingestion is complete.

**Why:** The overnight migration agent only used Attio data and produced mostly empty fields (only relationship_type and nurture_cadence). Kay's email exchanges, call notes, and meeting transcripts contain the real depth of context needed for value_to_search, next_action, and how_introduced. Without cross-referencing all sources, the enrichment is shallow and requires Kay to manually fill in gaps.

**How to apply:** When the relationships agent runs (daily or during migration), it should search each source for mentions of the person before proposing attribute values. Evidence from emails and calls should be cited (dates, subjects) so Kay can verify accuracy.
