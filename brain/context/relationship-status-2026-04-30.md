---
date: 2026-04-30
type: relationship-status
---

> **Note:** Today is Thursday. Per `feedback_relationship_cadence_friday_only.md`, pipeline-manager suppresses this section Mon-Thu. Artifact is still written for system-of-record continuity and Friday consolidation.

## Overdue Contacts (Top 5)

1. **Kristina Marcigliano (WTW)** — Quarterly, last contact 2025-12-23, **128 days since / 30 days overdue**. Next_action empty. Art-insurance broker (former Risk Strategies, current WTW Associate Director). Suggested action: short check-in email re art-insurance niche pipeline.
2. **Hunter Hartwell (Ellirock)** — Quarterly, last contact 2026-01-14, **106 days since / 8 days overdue**. Next_action empty. Suggested action: light check-in email; no urgent thread.
3. **Dan Tanzilli (Third Eye)** — Monthly, last contact 2026-03-26, **35 days since / at threshold**. Art World relationship via Karaugh Brown intro. Strongest connection: Good. Suggested action: check-in email or coffee invite.

Only 3 surfaced. Chase Lacson (Goodman Taft, ~184 days, Monthly) is an assistant — principal is Molly Epstein, who is Occasionally cadence and within window (last contact 2026-03-31; reconnection draft awaiting response). No principal-level surfacing today.

**Caveat:** Gmail/calendar are the only verified channels for last_interaction. Text and phone interactions are not captured; surfaced contacts may already be live via those channels.

## Auto-Resolved (No Action Needed)

- No outbound from kay.s@greenwichandbarrow.com to overdue candidates (Kristina Marcigliano, Hunter Hartwell, Dan Tanzilli, Molly Epstein, Chase Lacson) within the last 14 days. Nothing auto-resolved.

## Pending Intros

- None outstanding. Kendall Warson → Amanda completed (next_action: "Thank you sent, introduced to Amanda"). Rachel → Zoe completed 2026-04-01 (Rachel replied 2026-04-02). No other intro promises in next_action fields.

## Warm Intro Opportunities (from target-discovery)

- None new. No target-discovery handoff this run.

## Vault → Attio Syncs

- **Kristin Wihera** ([[entities/kristin-wihera]]) — vault entity modified 2026-04-24 (WSN post-mortem call notes from [[calls/2026-04-23-kristin-wihera]]). No `attio_id` set; Attio search for "Wihera" returned 0 matches. Person record does not yet exist in Attio. Sync deferred per SKILL.md — will retry tomorrow once auto-creation fires on next email signal.
- All other person entities modified in last 7 days (ian-stuart, nikki-higgins, peter-shakalis, andrew-lowis, jim-vigna, james-emden) already synced — `attio_synced_at` is newer than file `modified` time for each. No re-sync needed.

## Attio Dedup Needed

- None detected today. Three "Kristina" results in Attio (Marcigliano @ WTW, Marcigliano-CLCS unmapped, Baynes-Reid) are distinct individuals, not duplicates.

## Metadata Drift

- None. `next_action` text matches `nurture_cadence` field on all surfaced contacts. The Lauren Della Monica precedent pattern (text says quarterly, cadence is Occasionally) was checked — no current contacts exhibit it.

## System Status Alerts

- **Attio MCP filter limitation:** Filtering people by `is_set`/`is_not_empty` on the `nurture_cadence` select field returned HTTP 400. Worked around by issuing one filter per cadence value (Weekly/Monthly/Quarterly/Occasionally). Not blocking — full population captured. Flagged for future skill-side simplification: keep the per-value loop pattern instead of `is_set`.
- **Gmail/calendar verified-only channels:** Restated as a permanent caveat. Text/phone interactions are not surfaced; cadence-overdue lists may include people Kay has texted recently. Honor `next_action` evidence of recent contact when present.
- **Friday-only surfacing rule:** Today is Thursday 2026-04-30. Pipeline-manager should NOT include the Overdue Contacts section in this morning's briefing per `feedback_relationship_cadence_friday_only.md`. Artifact remains for Friday's consolidation.
