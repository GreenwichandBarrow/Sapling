---
schema_version: 1.1.0
date: 2026-04-29
type: trace
today: "[[notes/daily/2026-04-29]]"
task: Resolve simultaneous launchd plist failures (niche-intelligence + nightly-tracker-audit)
had_human_override: false
tags: [date/2026-04-29, trace, pattern/launchd-stagger, domain/technical]
---

# Decision Trace: Stagger Two Colliding Launchd Plists

## Context

On 2026-04-28 23:04:52 ET, both `niche-intelligence` (Tuesday 23:00 plist) and `nightly-tracker-audit` (daily 23:00 plist) fired at the same second. All 6 retry attempts (3 each) failed with `error: An unknown error occurred (Unexpected)`. Both ran ~6 hours, both exit 1 at 05:19, both Slack-alerted.

The wrapper retry loop did not help because every attempt hit the same parallel-fire collision. Each skill in isolation would have succeeded.

## Decisions

### Stagger Schedule
**AI proposed:** 30-min stagger (22:30 + 23:00).
**Chosen:** 60-min stagger — niche-intelligence Tue 22:30, nightly-tracker-audit daily 23:30.
**Reasoning:** niche-intelligence has historically run ~2 hours under retry pressure. 30 min isn't enough buffer if it overruns; both could end up writing to the tracker sheet simultaneously. 60 min absorbs the worst-case overrun without any future code change.
**Pattern:** #pattern/launchd-stagger

### Which Skill Runs Earlier
**AI proposed:** Tied — either order works.
**Chosen:** niche-intelligence earlier (22:30), nightly-tracker-audit later (23:30).
**Reasoning:** (1) Heavier-skill-earlier — niche-intelligence is the heavyweight (newsletter scrape + scoring + multi-sheet writes), gets first crack at resources. (2) Tuesday-only-skill-earlier — niche-intelligence is Tuesday-only; audit fires nightly. Putting the daily skill at 23:30 keeps the daily fire in a single consistent slot Mon-Sun rather than shifting around niche-intelligence's once-a-week earlier slot.
**Pattern:** #pattern/heavier-job-earlier

### Don't Bump Retry Count
**AI proposed:** Increase `MAX_ATTEMPTS` 3 → 5 in `scripts/run-skill.sh` to absorb future "Unexpected" failures.
**Chosen:** Reject. Stagger is the fix; retries don't help with simultaneous-fire collisions.
**Reasoning:** Every retry hits the same collision because both plists are still mid-flight. Bumping retries only stretches failed-run wall-clock from ~6h to ~10h while still failing. The wrapper layer cannot diagnose parallel-fire conflicts — that's a scheduling-layer problem, fixed at the plist layer.
**Pattern:** #pattern/right-layer-fix

## Learnings

- When two scheduled skills fail at the **exact same minute** with `error: An unknown error occurred (Unexpected)`, the first hypothesis is launchd parallel-fire collision. Not API outage, not auth, not network. (Codified in `feedback_launchd_parallel_fire_collisions.md`.)
- Diagnostic shortcut: `grep -A 6 "StartCalendarInterval" ~/Library/LaunchAgents/com.greenwich-barrow.*.plist | grep -E "plist|Hour|Minute"` shows all schedules at a glance.
- The fix is at the plist layer, not the wrapper layer — `<key>Hour</key>` / `<key>Minute</key>` edit + `launchctl unload/load`. No code change.
- 60-min stagger is the right buffer for two heavyweight Opus calls on Kay's Mac. Tighten to 30 min only after both skills consistently run <30 min in production.
- Niche-intelligence will still fail next Tuesday until bead `ai-ops-5wx` (mutating-skill hardening — headless prompt + validator + wrapper case) ships. Stagger fixes the *collision* but not the missing-headless-prompt root cause.
