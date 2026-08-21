---
schema_version: 1.1.0
date: 2026-08-21
type: relationship-status
tags: [date/2026-08-21, output/relationship-status, source/attio, source/gmail, source/vault, status/complete]
---

Gmail and Calendar are the only verified channels in this scan; text, phone, and in-person contact may not be captured. No previous-workday session-decisions file was present, so live Gmail/Attio evidence handled the action-already-taken check.

## Overdue Contacts (Top 5)
1. [[entities/kyle-mcgrath|Kyle McGrath]] ([[entities/markel|Markel]]) - Quarterly, last contact 2026-02-10, 93 days overdue
   Suggested action: check-in email. No outbound email found in the last 14 days.
2. [[entities/christopher-wise|Christopher Wise]] ([[entities/risk-strategies|Risk Strategies]]) - Quarterly, last contact 2026-02-18, 85 days overdue
   Suggested action: email check-in. No outbound email found in the last 14 days.
3. [[entities/chris-goyette|Chris Goyette]] ([[entities/private-risk-management-association|Private Risk Management Association]]) - Occasionally, last contact 2025-10-27, 84 days overdue
   Suggested action: email check-in. No outbound email found in the last 14 days.
4. [[entities/donald-moore|Donald Moore]] ([[entities/marsh|Marsh]]) - Occasionally, last contact 2025-10-28, 83 days overdue
   Suggested action: light email check-in. No outbound email found in the last 14 days.
5. [[entities/kendall-warson|Kendall Warson]] ([[entities/alumni-ventures|Alumni Ventures]]) - Quarterly, last contact 2026-03-02, 73 days overdue
   Suggested action: check-in email or coffee. No outbound email found in the last 14 days.

## Auto-Resolved (No Action Needed)
- None - no outbound emails were found in the 14-day verification window.

## Metadata Drift
- [[entities/britta-nelson|Britta Nelson]] ([[entities/cohart|Cohart]]) - `next_action` says "Texted recently (late March 2026). No follow-up needed. Maintain quarterly nurture." but `last_interaction` still shows 2025-12-16.
- [[entities/austin-yoder|Austin Yoder]] ([[entities/magrathea-partners|Magrathea Partners]]) - `next_action` says "Follow-up already sent. No action needed at this time." even though the latest recorded interaction is 2026-03-23.

## Pending Intros
- None - no intro-related `next_action` items were outstanding in the active cadence set.

## Warm Intro Opportunities (from target-discovery)
- None - no target-discovery handoff surfaced in this run.

## Vault → Attio Syncs
- None - no vault entities pending sync.

## Attio Dedup Needed
- None - no duplicate Attio person matches were encountered.

## System Status Alerts
- None - Attio REST health check returned 200; `gog auth list --check` was healthy; Attio-to-vault backfill was a no-op.
