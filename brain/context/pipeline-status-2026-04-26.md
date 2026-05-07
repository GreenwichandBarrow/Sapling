---
schema_version: 1.1.0
date: 2026-04-26
type: context
title: "Pipeline Status — 2026-04-26 (Sunday — calendar + Attio down, snapshot-only briefing)"
tags: [date/2026-04-26, context, topic/pipeline-manager, topic/morning-briefing, topic/sunday-carryover, topic/broken-systems]
---

# Pipeline Status — 2026-04-26 (Sunday)

Sunday morning manual run. Inputs: [[brain/context/email-scan-results-2026-04-26]] + [[brain/context/relationship-status-2026-04-26]] + [[brain/context/session-decisions-2026-04-25]]. Snapshot read from `brain/context/attio-pipeline-snapshot.json` (fetched Sat 16:59 UTC — last refresh before launchd Mon-Fri quiet period).

## Broken Systems (surfaced as 🔴 Decisions)

1. **Attio MCP credentials missing** — `smithery_debug_config` confirms `hasAttioWorkspaceId: false`; `search_records` 401s. **3rd consecutive day**, escalating: Friday notes-only → Sunday read+write. Live queries blocked; pipeline-manager runs from cached snapshot only.
2. **gog calendar events list returning 404** — both `--tomorrow` and absolute date ranges 404 `notFound`. Calendars list works (Holidays + kay.s primary, owner role). Cannot enumerate Monday meetings — pre-flight invariant degraded.

## Pipeline State (from cached snapshot)

- 18 active deals (11 Contacted / 7 Identified). No movement since Sat 16:59.
- 132 closed (130 pre-NDA outreach attrition / 2 post-NDA). No new closures.
- No CIM / NDA / LOI / financials inbound (per email-scan).
- No Active-Deal soft-nudge candidates flagged.

## Monday Pre-Flight (degraded)

Pre-flight invariant requires enumerating Monday's external meetings. **Calendar 404s + Attio 401s = cannot enumerate live.** Fallback signals checked:
- `brain/briefs/` — last brief is 4/22 (Jeff Stevens + WSN). No Monday-dated briefs pre-staged.
- session-decisions-2026-04-25 — no Monday meetings logged.
- email-scan-2026-04-26 — no Monday-dated meeting confirmations bounced back. James Emden + Cara Lovenson are Monday-AM-DRAFT items, not meetings.

**Conclusion:** No verified Monday external meetings. If Kay has one not visible in cache, the broken systems are masking it — surface as a 🔴 verify-meeting decision.

## Decision Items Sourced

- 🔴 Attio MCP broken (3rd day, escalating)
- 🔴 gog calendar 404 (new today)
- 🔴 Verify no hidden Monday meeting (pre-flight degraded)
- 🟡 James Emden Monday-AM availability draft (from email-scan)
- 🟡 Cara Lovenson Monday-AM confirm + $40 Venmo (from email-scan)
- 🟢 Phase 2 first-fire watch (open loop, verification Mon AM not Sun)
- 🟢 Andrew Lowis silent watch (no action until Wed if still silent)
- 🟢 5 overdue cadence contacts (Carlos x2 / Ashlee / Kanayo / Robert) — Monday-AM batch flip-or-touch decision

## Clustering Applied

- **XPX cluster:** James Emden + Andrew Lowis + Ian Stuart all in email-scan + relationship-status. Stuart closed; Lowis silent-watch (🟢); Emden is the only one needing decision (🟡). Collapsed.
- **Broken systems cluster:** Attio + calendar + meeting-verify could be one item, but each has distinct remediation (Smithery config / gog auth / fallback workflow). Kept separate but adjacent.
- **Cadence-debt cluster:** 5 overdue contacts collapsed into one batch decision (Monday metadata sweep). Per `feedback_close_the_loop` + `feedback_remove_kay_from_loop` — most are Dormant flips, not relationship actions.

## Tags

- topic/pipeline-manager
- topic/morning-briefing
- topic/broken-systems
- topic/attio-token-scope-blocker
- topic/calendar-404
- date/2026-04-26
