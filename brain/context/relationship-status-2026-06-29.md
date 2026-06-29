---
schema_version: 1.1.0
date: 2026-06-29
type: relationship-status
tags: [date/2026-06-29, output, output/relationship-status, status/done, person/britta-nelson, person/kristina-marcigliano, person/kendall-warson, person/stanley-rodos, company/squarespace, company/wtw, company/alumni-ventures]
---

Gmail and Calendar are the only verified channels in this scan; text, phone, and in-person contact may not be captured. Attio REST health-check returned 200 and Gmail auth was available via `gog auth list --check`.

## Overdue Contacts (Top 5)
1. [[entities/britta-nelson|Britta Nelson]] - Quarterly, last contact 2025-12-16, 97 overdue
   Suggested action: email check-in
2. [[entities/kristina-marcigliano|Kristina Marcigliano]] ([[entities/wtw|WTW]]) - Quarterly, last contact 2025-12-23, 90 overdue
   Suggested action: email check-in
3. [[entities/squarespace|Squarespace]] - Occasionally, last contact 2025-09-28, 61 overdue
   Suggested action: check-in
4. [[entities/kendall-warson|Kendall Warson]] ([[entities/alumni-ventures|Alumni Ventures]]) - Quarterly, last contact 2026-03-02, 21 overdue
   Suggested action: check-in
5. [[entities/stanley-rodos|Stanley Rodos]] - Quarterly, last contact 2026-03-17, 6 overdue
   Suggested action: coffee

## Auto-Resolved (No Action Needed)
None — no Kay outbound email was found in the last 14 days for the surfaced contacts.

## Pending Intros
None — no intro-related next_action items were pending in the active cadence set.

## Warm Intro Opportunities (from target-discovery)
None — no target-discovery handoff landed for this run.

## Vault → Attio Syncs
- [[entities/peter-nofo-tick-control|Peter NoFo Tick Control]]: no Attio person match yet, so no engagement-note sync was possible.
- None — no vault entities were eligible for a successful Attio engagement-note backfill this run.

## Attio Dedup Needed (if any)
None.

## System Status Alerts (if any)
- Attio backfill helper hit a transient HTTP 502 from `query-people` while processing `Colin Woolway` after the invalid-slug scan fix; the run partially completed and should be retried.
