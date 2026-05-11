---
name: Attio CRM Access
description: Attio API key, workspace ID, and pipeline list structure for CRM operations
type: reference
---

Attio API key stored in `.env` as `ATTIO_API_KEY`.
Base URL: https://api.attio.com/v2
Auth header: Authorization: Bearer {key}
Workspace ID: 243821c3-e0c9-46f9-8ee8-50e0094e12fb
Workspace slug: greenwich-barrow

## Objects
- People (83972a5b) — 401 from Google Workspace + 592 from SalesFlare migration = ~993
- Companies (78617670) — 252 from Google Workspace + 101 from SalesFlare migration = ~353
- Deals (320308d6) — default object, not actively used (pipelines use Lists instead)

## Pipeline Lists (migrated from SalesFlare 2026-03-14)

**CRITICAL: All pipelines are Attio Lists, NOT the default Deals object. Always query the Lists API.**

1. **Outreach: Network Pipeline** — slug: `outreach_network_pipeline`, list_id: `94ccb017-2b86-4e12-b674-e27de8e146c9`
2. **Outreach: Intermediary Pipeline** — slug: `outreach_intermediary_pipeline`, list_id: `7faac55b-a183-4afe-b7ea-fc8a4ccace10`
3. **Investor Engagement** — slug: `investor_engagement`, list_id: `f9d58294-5fb2-4794-b796-5c9ffa066025`
4. **Active Deals – Owners** — slug: `active_deals_owners`, list_id: `0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b`

All lists use `companies` as parent_object with a `stage` status attribute.

### Active Deals Stage Configuration (confirmed 2026-03-17)
Identified → Contacted → First Conversation → Second Conversation → NDA Executed → Financials Received → Active Diligence → LOI / Offer Submitted → LOI Signed → Closed / Not Proceeding

**Stage-to-tracker mapping:**
- NDA Executed → NDAs Signed
- Financials Received → Financials Received
- LOI / Offer Submitted → LOIs Submitted
- LOI Signed → LOIs Signed
- First Conversation → Stage 1 Calls
- Second Conversation → Stage 2 Calls
- Active Diligence → Deals in Active Review

**API to get all stages:** `GET /v2/lists/{list_id}/attributes/stage/statuses`
**API to get entries:** `POST /v2/lists/{list_id}/entries/query` with `{}`

### Network Relationship Tracking (People-based, new approach)
Network contacts tracked via **People records** with custom attributes, NOT the Network List.
The Network List will be retired after migration.

**Custom attributes on People (created 2026-03-17):**
- `relationship_type` (select): Fellow Searcher, Industry Expert, Advisor, Former Colleague, Friend/Personal, Operator/Owner, Investor Contact, Art World, Lender
- `nurture_cadence` (select): Weekly, Monthly, Quarterly, Occasionally, Dormant
- `value_to_search` (text)
- `next_action` (text)
- `how_introduced` (text)

**API to query people:** `POST /v2/objects/people/records/query`
**API to update person:** `PATCH /v2/objects/people/records/{record_id}`
**API to create select options:** `POST /v2/objects/people/attributes/{slug}/options`

**Custom attribute on Active Deals list (created 2026-03-18):**
- `meaningful_conversation` (checkbox): Has a meaningful owner conversation happened. Checked by pipeline-manager after Kay confirms. Counted by weekly-tracker.

API key now has `object_configuration:read-write` and `list_configuration:read-write` scopes.

## Migration Archive
Full SalesFlare data archived at `brain/library/internal/salesflare/` (contacts, accounts, opportunities, pipelines, tags, crossref files).
SalesFlare API key in `.env` as `SALESFLARE_API_KEY` (deprecated, kept for reference).
