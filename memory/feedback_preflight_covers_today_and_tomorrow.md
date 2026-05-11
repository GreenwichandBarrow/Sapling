---
name: Brief-decisions pre-flight covers TODAY + TOMORROW, not just D+1
description: Pipeline-manager's brief-decisions pre-flight enumerates BOTH today's external meetings AND tomorrow's, verifying briefs exist for each. D+0 has a structural gap that bit twice in three weeks.
type: feedback
originSessionId: 326c69dd-5175-4205-89f6-eb4a9ec64ab8
---
**Rule:** Pipeline-manager's morning brief-decisions pre-flight invariant covers **today's external meetings AND tomorrow's external meetings**. For each, verify a brief exists at `brain/briefs/{date}-{slug}*.md`. If today's external has no brief, surface as 🔴 RECOMMEND: Generate brief NOW (not "tomorrow morning"). If tomorrow's external has no brief, surface as 🔴 RECOMMEND: Generate brief overnight per existing invariant.

**Forbidden pattern:** Treating "today's externals are assumed already prepped from yesterday's pre-flight" as durable. Today's calendar can include: (a) externals that were on the calendar before yesterday's pre-flight ran, (b) recurring biweekly/monthly meetings outside the 2-day lookahead window, (c) meetings scheduled <24h ago.

**Why:** The original brief-decisions pre-flight (added 2026-04-21 after Guillermo miss) only covered D+1. D+0 has a structural gap. On 2026-05-06 morning, pipeline-manager's pre-flight only flagged James Emden (Thu 5/7) for brief generation. **Two same-day externals (Andrew Lowis 12:00 PM, Guillermo Lavergne 1:30 PM) had NO brief in vault or Drive**, surfaced only when Kay asked explicitly mid-morning ("did you make a brief for Andrew Lowis?") and early afternoon ("where is my guillermo brief?"). Both required crash-mode 10-minute briefs under tight time pressure, with quality compromises (Andrew's skipped Drive Doc, Guillermo's had stale cadence text needing post-hoc fix).

**How to apply:**
- During the morning pre-flight phase of pipeline-manager:
  1. Enumerate `gog calendar list --start <today>T00:00 --end <tomorrow>T23:59 --json`.
  2. For each external (non-Kay attendees > 0, not HOLD-prefixed):
     - Skip Coffee w/ Robe per `feedback_robe_no_briefs`.
     - For TODAY's externals: `ls brain/briefs/{today}-{slug}*.md` → if missing, 🔴 RECOMMEND: Generate brief NOW.
     - For TOMORROW's externals: `ls brain/briefs/{tomorrow}-{slug}*.md` → if missing, 🔴 RECOMMEND: Generate brief.
- Recurring meetings: even if `feedback_recurring_investor_briefs_owned_by_skill` says the owning skill should pre-fire, pipeline-manager STILL verifies the brief exists. Trust-but-verify.

**Source:** 2026-05-06 same-day-externals miss (Andrew + Guillermo double miss). Trace at `brain/traces/2026-05-06-same-day-externals-preflight-gap.md`. This is the second occurrence in three weeks — pattern, not outlier.
