---
schema_version: 1.1.0
date: 2026-06-25
type: relationship-status
tags: [date/2026-06-25, output, output/relationship-status, status/done, person/dan-tanzilli, company/third-eye-collective, person/hunter-hartwell, company/ellirock, person/george-yates, company/dayton-ritz-osborne, person/austin-yoder, person/sarah-de-blasio, person/kristina-marcigliano]
---

Gmail and Calendar are the only verified channels in this scan; text, phone, and in-person contact may not be captured. Attio REST health-check returned 200 and Gmail auth was available via `gog auth list --check`.

## Overdue Contacts (Top 5)
1. [[entities/dan-tanzilli|Dan Tanzilli]] ([[entities/third-eye-collective|Third Eye Collective]]) - Monthly, last contact 2026-03-26, 56 days overdue
   Suggested action: light check-in only if Kay wants to keep the art-world / art-storage path warm. No Kay outbound to `dan@hellothirdeye.com` found in the last 14 days.
2. [[entities/hunter-hartwell|Hunter Hartwell]] ([[entities/ellirock|Ellirock]]) - Quarterly, last contact 2026-01-14, 63 days overdue
   Suggested action: low-pressure fellow-searcher check-in tied to insurance/pest pattern sharing. No Kay outbound to `hunter@ellirock.com` found in the last 14 days.

Slot 3-5 intentionally empty after exclusions. Prior deferrals, trigger-gated contacts, Kay-managed direct relationships, duplicates, role addresses, and records without reliable person identity were suppressed rather than force-filled.

## Auto-Resolved (No Action Needed)
None - no surfaced contact had a substantive Kay outbound thread in Gmail within the last 14 days, so no `last_interaction` / `next_action` cleanup write was needed.

## Pending Intros
- [[entities/george-yates|George Yates]] ([[entities/dayton-ritz-osborne|Dayton, Ritz + Osborne]]): intro email still pending. Attio `next_action` remains "Send introductory email. No prior contact - handwritten letter was planned Nov 2025 but never sent." No Kay outbound to `gyates@droinsurance.com` found in the last 14 days.

## Warm Intro Opportunities (from target-discovery)
None - no target-discovery handoff landed for this run.

## Vault → Attio Syncs
None - no eligible vault entity could be synced today. Recent unsynced person files with relationship notes were [[entities/max-loomis|Max Loomis]] and [[entities/will-smith|Will Smith]]; Attio name searches returned 0 matches, and neither vault entity has a direct verified email suitable for matching. Will Smith has newsletter/subscription Gmail traffic only, not a 1:1 relationship record.

## Attio Dedup Needed
- [[entities/austin-yoder|Austin Yoder]]: two Attio person records remain. The `hello@cal.com` record is the one overdue by date but appears to be a scheduling-service duplicate; the real Magrathea record (`austin@magratheapartners.com`) is within Quarterly cadence and says follow-up already sent.
- [[entities/sarah-de-blasio|Sarah de Blasio]]: Attio still shows Quarterly, but vault/memory says Kay-managed direct / Dormant and 2026-06-03 session decisions say she was texted that day. Suppressed from overdue surfacing; Attio cadence should be reconciled to Dormant in a supervised cleanup.
- [[entities/kristina-marcigliano|Kristina Marcigliano]]: Attio still shows Quarterly, but 2026-06-03 session decisions marked her trigger-gated: surface only when a deal surfaces. Suppressed from overdue surfacing; Attio `next_action` should be updated to encode the trigger explicitly.

## System Status Alerts
None - Attio REST and Gmail auth were healthy. No Attio writes failed; no Attio writes were required after action-verification and idempotent vault-sync checks.
