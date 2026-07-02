---
schema_version: 1.1.0
date: 2026-07-02
type: relationship-status
tags: [date/2026-07-02, output, output/relationship-status, status/done, person/kyle-mcgrath, company/markel, person/christopher-wise, company/risk-strategies, person/britta-nelson, person/george-yates, company/dayton-ritz-osborne, person/austin-yoder, company/ashford-ventures]
---

Gmail and Calendar are the only verified channels in this scan; text, phone, and in-person contact may not be captured. Attio REST health-check returned 200 and Gmail auth was available via `gog auth list --check`.

## Overdue Contacts (Top 5)
1. [[entities/kyle-mcgrath|Kyle McGrath]] ([[entities/markel|Markel]]) - Quarterly, last contact 2026-02-10, 44 overdue
   Suggested action: check-in
2. [[entities/christopher-wise|Christopher Wise]] ([[entities/risk-strategies|Risk Strategies]]) - Quarterly, last contact 2026-02-18, 36 overdue
   Suggested action: check-in

## Auto-Resolved (No Action Needed)
- [[entities/britta-nelson|Britta Nelson]]: Attio `next_action` says she was texted recently and no follow-up is needed.
- [[entities/austin-yoder|Austin Yoder]] ([[entities/ashford-ventures|Ashford Ventures]]): real record says follow-up already sent and no action is needed; separate cal.com scheduling stub still exists.

## Pending Intros
- [[entities/george-yates|George Yates]] ([[entities/dayton-ritz-osborne|Dayton, Ritz + Osborne]]): intro email still pending. Attio `next_action` remains "Send introductory email. No prior contact - handwritten letter was planned Nov 2025 but never sent."

## Warm Intro Opportunities (from target-discovery)
None - no target-discovery handoff landed for this run.

## Vault → Attio Syncs
None - no vault entities pending sync.

## Attio Dedup Needed (if any)
- [[entities/austin-yoder|Austin Yoder]]: 2 matching person records (`hello@cal.com`, `austin@magratheapartners.com`) - keep the Magrathea record; retire the cal.com scheduling duplicate.

## System Status Alerts (if any)
None - Attio REST and Gmail auth were healthy.
