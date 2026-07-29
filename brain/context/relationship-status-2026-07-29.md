---
date: 2026-07-29
type: relationship-status
tags: [date/2026-07-29, output, output/relationship-status, status/done, person/kyle-mcgrath, company/markel, person/christopher-wise, company/risk-strategies, person/chris-goyette, company/private-risk-management-association, person/donald-moore, company/marsh, person/rick-hiebert, company/wondeur-ai, person/britta-nelson, person/kendall-warson, person/stanley-rodos, person/austin-yoder, person/samuel-curcio, person/quietlight]
---

Gmail and Calendar are the only verified channels in this scan; text, phone, and in-person contact may not be captured. Attio REST `/v2/self` returned 200 and `gog auth list --check` was healthy. 52 active cadence contacts were reviewed; trigger-based `next_action` records were excluded from the overdue list. Previous-workday session-decisions file was not present, so live Gmail/Attio evidence handled the action-already-taken check.

## Overdue Contacts (Top 5)
1. [[entities/kyle-mcgrath|Kyle McGrath]] ([[entities/markel|Markel International]]) - Quarterly, last contact 2026-02-10, 71 days overdue
   Suggested action: email check-in
2. [[entities/christopher-wise|Christopher Wise]] ([[entities/risk-strategies|Risk Strategies]]) - Quarterly, last contact 2026-02-18, 63 days overdue
   Suggested action: check-in email
3. [[entities/chris-goyette|Chris Goyette]] ([[entities/private-risk-management-association|Private Risk Management Association]]) - Occasionally, last contact 2025-10-27, 62 days overdue
   Suggested action: event invite or check-in
4. [[entities/donald-moore|Donald Moore]] ([[entities/marsh|Marsh]]) - Occasionally, last contact 2025-10-28, 61 days overdue
   Suggested action: email
5. [[entities/rick-hiebert|Rick Hiebert]] ([[entities/wondeur-ai|Wondeur Ai]]) - Occasionally, last contact 2025-12-11, 17 days overdue
   Suggested action: check-in

## Auto-Resolved (No Action Needed)
- [[entities/britta-nelson|Britta Nelson]]: suppressed by Attio next_action ("Texted recently (late March 2026). No follow-up needed. Maintain quarterly nurture.")
- [[entities/kendall-warson|Kendall Warson]]: suppressed by Attio next_action ("Thank you sent, introduced to Amanda. No pending action.")
- [[entities/stanley-rodos|Stanley Rodos]]: suppressed by Attio/calendar state ("Quarterly coffee already on calendar.")
- [[entities/austin-yoder|Austin Yoder]]: suppressed by Attio next_action ("Follow-up already sent. No action needed at this time.")

## Pending Intros
- None — no pending intros found.

## Warm Intro Opportunities (from target-discovery)
- None — no target-discovery handoff landed for this run.

## Vault → Attio Syncs
- [[entities/samuel-curcio|Samuel Curcio]]: vault entity linked to existing Attio person record (`attio_id` captured); no engagement note attached because the Relationship Notes were backfill metadata only.
- [[entities/quietlight|Quietlight]]: no exact Attio match; vault stub remains `attio_sync_status: not_found`.

## Attio Dedup Needed (if any)
- None — no duplicate Attio matches found.

## System Status Alerts (if any)
- None — no system status alerts.
