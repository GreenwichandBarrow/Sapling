---
name: Vault Is Single Source of Truth
description: All data from external tools must be stored in brain/ — the vault is the canonical record, tools are inputs
type: feedback
---

All data from external tools must flow into the vault (brain/). The vault is the single source of truth. External tools are inputs, not sources to query repeatedly.

**Data flow map:**
- **Granola** transcripts → brain/calls/ (source: granola)
- **Fireflies** transcripts → brain/calls/ (source: fireflies, historical, already done)
- **Gmail** → brain/inbox/ (actionable items, not every email)
- **Attio** → queried live for CRM state, but relationship context lives in vault entities
- **Motion** → tasks queried live, but outcomes/decisions captured in vault traces

**Why:** Kay wants the vault to be the complete picture. Agents should be able to enrich records by searching the vault without needing to re-query every external API. Data stored once, referenced many times. Also reduces API calls and ensures nothing is lost if a tool subscription changes.

**How to apply:** Every workflow that ingests from an external tool must write to the appropriate brain/ path before processing. The relationships agent reads vault calls + inbox, not Granola/Gmail directly.
