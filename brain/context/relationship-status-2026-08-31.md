---
date: 2026-08-31
type: relationship-status
tags: [date/2026-08-31, output/relationship-status, source/attio, source/gmail, source/vault, status/complete]
---

Gmail is the only channel re-verified directly in this run; Attio supplied the interaction timestamps. No 2026-08-28 session-decisions file was present, so live Gmail and Attio evidence handled the action-already-taken check. Text, phone, and in-person contact may still be missing.

Trigger-language `next_action` entries were excluded from time-based surfacing, so the list below only includes cadence-based contacts with no Kay outbound in the last 14 days.

## Overdue Contacts (Top 5)
1. [[entities/kyle-mcgrath|Kyle McGrath]] ([[entities/markel|Markel]]) - Quarterly, last contact 2026-02-10, 104 days overdue
   Suggested action: check-in email.
2. [[entities/christopher-wise|Christopher Wise]] ([[entities/risk-strategies|Risk Strategies]]) - Quarterly, last contact 2026-02-18, 96 days overdue
   Suggested action: email check-in.
3. [[entities/chris-goyette|Chris Goyette]] ([[entities/private-risk-management-association|Private Risk Management Association]]) - Occasionally, last contact 2025-10-27, 95 days overdue
   Suggested action: check-in email.
4. [[entities/donald-moore|Donald Moore]] ([[entities/marsh|Marsh]]) - Occasionally, last contact 2025-10-28, 94 days overdue
   Suggested action: email check-in.
5. [[entities/kendall-warson|Kendall Warson]] ([[entities/cohart|Cohart]]) - Quarterly, last contact 2026-03-02, 84 days overdue
   Suggested action: coffee or email check-in.

## Auto-Resolved (No Action Needed)
- None - no Kay outbound email was found in the last 14 days for the surfaced contacts, so nothing auto-resolved from Gmail.

## Pending Intros
- None - no intro-related `next_action` items were outstanding in the active cadence set.

## Warm Intro Opportunities (from target-discovery)
- None - no target-discovery handoff surfaced in this run.

## Vault → Attio Syncs
- None - no vault entities pending sync.

## Attio Dedup Needed (if any)
- None - no duplicate Attio person records were detected for surfaced contacts.

## System Status Alerts (if any)
- None - Attio REST health returned 200 and `gog auth list --check` was healthy.
