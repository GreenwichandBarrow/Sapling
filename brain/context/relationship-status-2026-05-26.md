---
date: 2026-05-26
type: relationship-status
---

## Overdue Contacts (Top 5)
1. Kristina Marcigliano (WTW) — Quarterly, last contact 2025-12-23, 154 days (56 days overdue)
   Suggested action: check-in email
2. Hunter Hartwell (Ellirock) — Quarterly, last contact 2026-01-14, 132 days (34 days overdue)
   Suggested action: check-in email
3. Dan Tanzilli (Third Eye, Art World) — Monthly, last contact 2026-03-26, 61 days (26 days overdue)
   Suggested action: art-world check-in / luxury-niche intel ping
4. Kyle McGrath (Markel, Industry Expert — Fine Art & Specie) — Quarterly, last contact 2026-02-10, 105 days (7 days overdue)
   Suggested action: quarterly check-in (light touch; commitment line in next_action is informational, no specific owed action)

_Note: Gmail and Google Calendar are the only channels this skill can verify. Text, phone, and in-person interactions are not captured — Attio `next_action` notes were used as a secondary signal where present._

## Auto-Resolved (No Action Needed)
- None — no overdue candidates had outbound from Kay in the last 14 days.

## Suppressed (cadence-window or signal-already-present)
- Britta Nelson — Quarterly, 161 days. `next_action`: "Texted recently (late March 2026). No follow-up needed." Treated as recent interaction per SKILL.md.
- Chase Lacson (Goodman Taft) — Monthly, 210 days. Assistant; principal is Molly Epstein, who is in trigger-based "Awaiting response" state. Suppressed under Assistant-vs-Principal rule.
- Molly Epstein (Goodman Taft) — Occasionally, 56 days. `next_action` trigger ("Awaiting response" to 3/30 reconnection draft).

## Pending Intros
- James Emden (Helmsley Spear, river-guide candidate) — owed: share scheduling windows for intro call with Peter Shakalis joining. Last contact 2026-05-08 (18 days ago, within cadence). Asset-light deal context to be flagged upfront.

## Warm Intro Opportunities (from target-discovery)
- None — no target-discovery handoff active this morning.

## Vault → Attio Syncs
- None — no vault entities pending sync. Six person-entities modified in the last 7 days were already synced 2026-05-22 (carlos-nieto-dca, oswaldo-ponce, sam-lamson, laura-smith-bankunited, sam-transworld, matt-becky-colleague). Emilio Mitidieri (modified 2026-05-19) has no `## Relationship Notes` section — sync detection criterion not met; will retry once notes are added.

## Attio Dedup Needed
- None — no duplicate email addresses across People records (~2,353 total scanned).

## Metadata Drift / Record Hygiene
- **Michelle Perr (UBS)** — Occasionally cadence, no `last_interaction` populated. Either backfill last contact date or move to Dormant.
- **David Wolkoff (Former Colleague)** — Occasionally cadence, no `last_interaction` populated. `next_action`: "Personal relationship, not search-related. Maintain warmth." Consider moving to Dormant or backfilling.
- **`thyme@everystall.com`** — Occasionally cadence, no name populated, last contact 2025-06-03 (357 days). Likely a vendor/system stub; recommend deletion or move to Dormant.
- **`customercare@squarespace.com`** — Occasionally cadence, vendor support address (Squarespace). Recommend deletion or move to Dormant.

## System Status Alerts
- None — Attio API health check returned 200 (`GET /v2/self`). REST reads + writes operational. All vault→Attio sync prerequisites met (no entities pending sync this run).
