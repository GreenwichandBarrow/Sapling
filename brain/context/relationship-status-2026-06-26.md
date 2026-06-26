---
schema_version: 1.1.0
date: 2026-06-26
type: relationship-status
tags: [date/2026-06-26, output, output/relationship-status, status/done, person/dan-tanzilli, company/third-eye-collective, person/hunter-hartwell, company/ellirock, person/kristina-marcigliano, company/wtw, person/george-yates, company/dayton-ritz-osborne, person/austin-yoder, company/ashford-ventures]
---

Gmail and Calendar are the only verified channels in this scan; text, phone, and in-person contact may not be captured. Attio REST health-check returned 200 and Gmail auth was available via `gog auth list --check`.

## Overdue Contacts (Top 5)
1. [[entities/dan-tanzilli|Dan Tanzilli]] ([[entities/third-eye-collective|Third Eye Collective]]) - Monthly, last contact 2026-03-26, 56 days overdue
   Suggested action: light check-in email. No Kay outbound to `dan@hellothirdeye.com` found in the last 14 days.
2. [[entities/hunter-hartwell|Hunter Hartwell]] ([[entities/ellirock|Ellirock]]) - Quarterly, last contact 2026-01-14, 64 days overdue
   Suggested action: low-pressure check-in or coffee note. No Kay outbound to `hunter@ellirock.com` found in the last 14 days.
3. [[entities/kristina-marcigliano|Kristina Marcigliano]] ([[entities/wtw|WTW]]) - Quarterly, last contact 2025-12-23, 86 days overdue
   Suggested action: brief catch-up email. No Kay outbound to `kristina.marcigliano@wtwco.com` found in the last 14 days.

Slot 4-5 intentionally empty after exclusions. Trigger-based contacts, deferred contacts from the 2026-06-24 session decisions, assistant/principal duplicates, within-cadence records, and records without reliable direct-contact evidence were suppressed rather than force-filled.

## Auto-Resolved (No Action Needed)
None - no surfaced overdue contact had a substantive Kay outbound thread in Gmail within the last 14 days, so no last-interaction cleanup write was needed.

## Pending Intros
- [[entities/george-yates|George Yates]] ([[entities/dayton-ritz-osborne|Dayton, Ritz + Osborne]]): intro email still pending. Attio `next_action` remains "Send introductory email." No Kay outbound to `gyates@droinsurance.com` found in the last 14 days.

## Warm Intro Opportunities (from target-discovery)
None - no target-discovery handoff landed for this run.

## Vault → Attio Syncs
None - recent person notes with unsynced frontmatter already had matching Attio engagement notes attached, and recent person files without Attio IDs had no matching Attio record yet.

## Attio Dedup Needed (if any)
- [[entities/austin-yoder|Austin Yoder]]: two Attio person records remain. Keep `austin@magratheapartners.com` as the principal record; `hello@cal.com` is the scheduling-service duplicate and should not be the surfaced contact.

## System Status Alerts (if any)
None - Attio REST and Gmail auth were healthy. No Attio writes failed; no new Attio writes were required after action-verification and idempotent vault-sync checks.
