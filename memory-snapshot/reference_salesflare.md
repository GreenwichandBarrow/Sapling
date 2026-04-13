---
name: SalesFlare Archive
description: SalesFlare CRM data archived after migration to Attio (March 2026)
type: reference
---

SalesFlare API key in `.env` as `SALESFLARE_API_KEY` (deprecated — migrated to Attio).
Full data archived at `brain/library/internal/salesflare/`:
- contacts.json (2,105 total), accounts.json (879), opportunities.json (195), pipelines.json (4), tags.json (20)
- migrate_contacts.json (845 — excluded bulk imports from Mar 7-8 2025, Oct 9 2025, Feb 20 2026)
- excluded_contacts.json (1,260 — bulk import contacts not migrated to Attio)
- contact_crossref.json, company_crossref.json, people_created.json — migration mapping files
