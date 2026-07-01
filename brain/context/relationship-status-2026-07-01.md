---
schema_version: 1.1.0
date: 2026-07-01
type: relationship-status
tags: [date/2026-07-01, output, output/relationship-status, status/done, person/austin-yoder, company/cal-com, person/britta-nelson, person/alex-rejigg, company/rejigg, person/sarah-findlay, person/walker-deibel, person/will-gallagher, company/startvirtual]
---

Gmail and Calendar are the only verified channels in this scan; text, phone, and in-person contact may not be captured. Attio REST health-check returned 200 and Gmail auth was available via `gog auth list --check`.

## Overdue Contacts (Top 5)
1. [[entities/austin-yoder|Austin Yoder]] ([[entities/cal-com|Cal.com]]) - Quarterly, last contact 2026-02-19, 34 overdue
   Suggested action: check-in

Other time-based candidates were suppressed because they were already deferred or trigger-gated in prior session decisions, or had recent non-email contact evidence in Attio.

## Auto-Resolved (No Action Needed)
- [[entities/britta-nelson|Britta Nelson]]: Attio `next_action` says she was texted recently and no follow-up is needed.

## Pending Intros
None - no intro-related `next_action` items were pending in the active cadence set.

## Warm Intro Opportunities (from target-discovery)
None - no target-discovery handoff landed for this run.

## Vault → Attio Syncs
- [[entities/alex-rejigg|Alex / Rejigg]]: engagement note attached, `attio_id` captured in vault entity.

## Attio Dedup Needed (if any)
- [[entities/rejigg|Rejigg]]: 2 matching person records (`support@accounts.rejigg.com`, `info@notifications.rejigg.com`)
- [[entities/sarah-findlay|Sarah Findlay]]: 2 matching person records (`sarah@garde-robe.com`, `sarahfindlay2@gmail.com`)
- [[entities/startvirtual|StartVirtual]]: 2 matching person records (`mail@signnow.com`, `invoice+statements@startvirtual.com`)
- [[entities/walker-deibel|Walker Deibel]]: 2 matching person records (`walker@buythenbuild.com`, `walker@buildwealth.com`)
- [[entities/will-gallagher|Will Gallagher]]: 2 matching person records (`will@legatelp.com`, `gallagher.williamp@gmail.com`)

## System Status Alerts (if any)
None - Attio REST and Gmail auth were healthy.
