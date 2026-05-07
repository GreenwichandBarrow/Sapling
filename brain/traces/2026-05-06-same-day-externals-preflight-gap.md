---
schema_version: 1.1.0
date: 2026-05-06
type: trace
today: "[[notes/daily/2026-05-06]]"
task: Surface and crash-fix a process gap where same-day external meetings had no briefs generated
had_human_override: true
importance: high
target: skill:pipeline-manager
tags: ["date/2026-05-06", "trace", "topic/morning-briefing", "topic/meeting-brief", "topic/pipeline-manager", "pattern/preflight-covers-today-and-tomorrow"]
---

# Decision Trace: Same-Day Externals Fell Through Pre-Flight — Andrew Lowis + Guillermo

## Context

Today's calendar had two confirmed external calls:
- **12:00 PM ET** — Andrew Lowis (Axial), repeat contact, call #2
- **1:30 PM ET** — Guillermo Lavergne, biweekly investor

This morning's pipeline-manager pre-flight only flagged ONE external for brief generation: James Emden (Helmsley Spear) — Thursday 5/7 10 AM, the D+1 external. **Neither today's externals were surfaced for brief generation.** Kay had to ask explicitly mid-morning ("did you make a brief for the meeting with Andrew Lowis?") and again early afternoon ("where is my guillermo brief?"). In both cases, no brief existed in vault or Drive. Crash-mode briefs were generated under tight time pressure (10-min budget each).

## Decisions

### Pre-flight scope: today + tomorrow, not just tomorrow

**AI proposed (today's pre-flight, implicit):** Pipeline-manager looks 2 days ahead in calendar. The brief-decisions invariant in CLAUDE.md states "enumerate tomorrow's external meetings." Today's externals are assumed already prepped from yesterday's pre-flight.

**Chosen (Kay's correction via two crash-brief asks):** **Pre-flight must enumerate TODAY's externals AND tomorrow's externals.** Today's externals can fall through if yesterday's pre-flight missed them OR if the meeting was scheduled <24 hours ago OR if the meeting is recurring and didn't trigger a fresh pre-flight scan.

**Reasoning:**
- Today's Andrew Lowis call was scheduled in late April but the brief was never auto-generated; pipeline-manager's D+1 scan never saw it because it was already "today" by the time the scan ran each morning during the prep window.
- Today's Guillermo call is a recurring biweekly. Pipeline-manager's 2-day calendar lookahead doesn't auto-generate briefs for recurring events because the assumption is the owning skill (`investor-update`) handles that. But `investor-update` didn't fire either. The recurring case has TWO failure modes: pipeline-manager skips it (assumes ownership elsewhere) AND owning skill doesn't auto-fire (no scheduled trigger). Both failures stack.

**Pattern:** #pattern/preflight-covers-today-and-tomorrow

## Why This Trace Matters

Today this cost two crash-mode briefs under 10-min time pressure each — both landed but with quality compromises (Andrew's brief had to skip the Drive Doc; Guillermo's brief had stale-cadence text the COO had to fix post-hoc in vault + Drive). A more substantive externals miss (e.g., LP one-pager, owner first-call) at the same gap could be unrecoverable.

The systemic fix has two parts:
1. **Pipeline-manager pre-flight enumerates today's externals AND tomorrow's externals.** For each today external, verify a brief exists at `brain/briefs/{today}-{slug}*.md`. If missing, surface as 🔴 RECOMMEND: Generate brief immediately (not "tomorrow morning").
2. **Recurring investor briefs auto-fire from `investor-update` skill 24h ahead, on a per-cadence cron** (biweekly Guillermo, monthly Jeff Stevens, quarterly all-LP). Don't depend on pipeline-manager's pre-flight to catch recurring cases.

## Key Insight

The brief-decisions pre-flight invariant (added 2026-04-21 after the original Guillermo miss) only covers D+1. **D+0 has a structural gap** — meetings that were on the calendar before yesterday's pre-flight ran, AND recurring meetings that fall outside the 2-day lookahead window. Today's Andrew + Guillermo double-miss is the second time this pattern has bitten in three weeks (Guillermo missed on 2026-04-21, both missed today). It's now a pattern, not an outlier.

Two memory rules proposed (carried to next session):
- `feedback_preflight_covers_today_and_tomorrow.md` — pipeline-manager pre-flight scans D+0 + D+1 for missing briefs, not just D+1.
- `feedback_recurring_investor_briefs_owned_by_skill.md` — recurring investor briefs auto-fire from the `investor-update` skill on per-cadence cron, not from pipeline-manager pre-flight.
