---
date: 2026-06-30
type: relationship-status
tags: [date/2026-06-30, output, output/relationship-status, status/done, person/britta-nelson, person/austin-yoder, person/kristina-marcigliano, company/wtw, company/squarespace, person/kyle-mcgrath, company/markel, person/kendall-warson, person/stanley-rodos]
---

Gmail and Calendar are the only verified channels in this scan; text, phone, and in-person contact may not be captured. Attio REST health-check returned 200 and Gmail auth was available via `gog auth list --check`.

## Overdue Contacts (Top 5)
1. [[entities/kristina-marcigliano|Kristina Marcigliano]] ([[entities/wtw|WTW]]) - Quarterly, last contact 2025-12-23, 91 overdue
   Suggested action: email check-in
2. [[entities/squarespace|Squarespace]] - Occasionally, last contact 2025-09-28, 62 overdue
   Suggested action: check-in
3. [[entities/kyle-mcgrath|Kyle McGrath]] ([[entities/markel|Markel]]) - Quarterly, last contact 2026-02-10, 42 overdue
   Suggested action: email check-in
4. [[entities/kendall-warson|Kendall Warson]] - Quarterly, last contact 2026-03-02, 22 overdue
   Suggested action: check-in
5. [[entities/stanley-rodos|Stanley Rodos]] - Quarterly, last contact 2026-03-17, 7 overdue
   Suggested action: coffee

## Auto-Resolved (No Action Needed)
- [[entities/britta-nelson|Britta Nelson]]: Attio `next_action` says she was texted recently in late March and no follow-up is needed.
- [[entities/austin-yoder|Austin Yoder]]: follow-up already sent, no action needed at this time.

## Pending Intros
None - no intro-related `next_action` items were pending in the active cadence set.

## Warm Intro Opportunities (from target-discovery)
None - no target-discovery handoff landed for this run.

## Vault → Attio Syncs
None - no vault entities were successfully synced this run.

## Attio Dedup Needed
None.

## System Status Alerts
- `scripts/backfill_vault_entities_from_attio.py` hit an Attio API HTTP 429 `rate_limit_exceeded` error on `query-people` while scanning vault entities, so no additional backfill syncs completed this run.
