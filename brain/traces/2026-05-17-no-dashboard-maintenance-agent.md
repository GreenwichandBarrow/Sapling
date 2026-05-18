---
schema_version: 1.1.0
date: 2026-05-17
type: trace
today: "[[brain/context/continuation-2026-05-17-2]]"
task: Dashboard 7-page diagnostic — root-cause unreliable data feeds
had_human_override: false
review_status: pending
importance: high
target: process
tags: [date/2026-05-17, trace, topic/dashboard, pattern/fix-plumbing-not-add-agent, status/done]
---

# Decision Trace: No Dedicated Dashboard-Maintenance Agent

## Context
Full 7-page dashboard diagnostic surfaced multiple stale/empty panels (JJ calls, DealsX channel, Owner-conversation count). The intuitive fix for "dashboard keeps going stale" is a watchdog agent that monitors freshness and re-runs feeds.

## Decisions

### Reject a dashboard-maintenance agent; fix feeds + add loud validators
**AI proposed (intuitive default):** A scheduled maintenance agent that polls dashboard panels, detects staleness, and triggers re-runs.
**Chosen:** No new agent. Wire the genuinely-missing feeds (DealsX manual weekly snapshot), and harden the existing validators to FAIL LOUD on unexpected zeros instead of silently passing.
**Reasoning:** Every gap traced to one root-cause class — macOS-on-Linux path assumptions, unwired proprietary feeds, operator-YAML mistaken for live data. None of those are "the feed ran but produced stale output" (which a watchdog catches). They are "the feed never ran / was never built / isn't actually a feed." A maintenance agent sitting on top of broken plumbing would report green or paper over the silence without removing the defect, and add a new failure surface that itself needs monitoring.
**Pattern:** #pattern/fix-plumbing-not-add-agent

## Why This Trace Matters
A future agent hitting "dashboard data is unreliable" will reach for a monitor/watchdog/maintenance-agent by default — it feels like the responsible move. This trace records that for THIS system the correct response is to classify the root cause first: if failures are "never ran / never wired / not a live source," adding an agent masks the defect. Agents don't fix unreliable plumbing — loud validators + wired feeds do.

## Key Insight
When the failure mode is silent absence (zero rows, no feed, fake-live YAML), the fix is a validator that screams on the anomaly, not an agent that watches for it. Reserve agents for judgment, not for compensating for missing infrastructure.
