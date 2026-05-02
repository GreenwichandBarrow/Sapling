---
schema_version: 1.1.0
date: 2026-05-01
type: trace
title: "launchd-debugger v1.1: failure-trigger architecture with recursion guard + known-incident registry"
tags: ["date/2026-05-01", "trace", "topic/launchd-debugger", "topic/scheduled-skills", "topic/silent-failure-detection", "domain/technical"]
importance: high
target: skill:launchd-debugger
---

# launchd-debugger failure-trigger architecture

## Context

launchd-debugger v1 was built earlier today as a daily 5am ET scan of overnight launchd job logs to catch silent failures before the morning briefing. Within hours of v1 ship, three architectural gaps surfaced: (a) a 5am daily scan misses failures during the workday, (b) repeated incidents would spam Slack day after day until manually fixed, (c) without a recursion guard, the debugger firing on its own failures would loop.

## Decision

**AI proposed (initial v1):** Single daily 5am scan, surface every detected failure to Slack #operations.

**Chosen (v1.1):** Three architectural additions on top of v1:

1. **On-failure trigger architecture** — auto-fire launchd-debugger on every non-zero exit from any other scheduled-skill wrapper. The wrapper case-statement in `scripts/run-skill.sh` invokes launchd-debugger as a subprocess after the originating skill returns non-zero. The 5am daily scan stays as a backstop for any failures the on-failure trigger missed.

2. **Recursion guard** — launchd-debugger CANNOT fire itself when it fails. Implemented via env var check or skill-name check in the wrapper before the on-failure trigger invokes the debugger. Prevents infinite-loop scenario where launchd-debugger crashes, triggers itself, which crashes, triggers itself, etc.

3. **Known-incident registry + cross-day dedup** — `brain/trackers/health/known-incidents.json` holds entries like `{ "incident_id": "ai-ops-5wx", "skill": "niche-intelligence", "suppress_until": "2026-05-06", "reason": "Agent B fixing in parallel — pre-suppress to avoid Slack spam" }`. Before pushing to Slack, launchd-debugger checks the registry and suppresses any incident whose ID matches. Cross-day dedup also suppresses identical errors that fired the previous day (rolling window).

**Reasoning:** Silent failures during the workday are worse than overnight ones — by the time the 5am daily scan catches them, Kay has already acted on stale dashboard data. On-failure trigger gives near-realtime detection. The recursion guard is a hard requirement (otherwise one bad debugger run = infinite Slack spam). The known-incident registry is the noise-suppression mechanism that lets us ship the failure-trigger without flooding Kay during in-flight bug fixes (ai-ops-5wx was pre-suppressed today during the niche-intelligence fix).

## Why this matters for future agents

The architectural pattern here generalizes: any monitor/observer that triggers on events MUST have:
- A **recursion guard** (the monitor cannot trigger on its own events)
- A **known-incident registry** to suppress noise during in-flight fixes
- A **cross-day dedup** so repeated identical failures don't spam beyond initial detection
- A **fallback periodic scan** so missed events still get caught eventually

Without all four, the monitor either misses events (no event-trigger), spams the user (no dedup/registry), or loops infinitely (no recursion guard).

## Concrete activation outcome

`launchctl load` succeeded today. First fire 5/2 5am ET. Failure-trigger live. ai-ops-5wx pre-suppressed in known-incident registry to avoid Slack spam during Agent B's niche-intelligence Tuesday hardening fix (registry entry expires once Tuesday 5/5 22:30 ET production verification passes).

## How a future agent should apply

When building any monitor / observer / health-check skill:

1. **Default to event-trigger + periodic-scan-as-backstop**, not periodic-scan-only.
2. **Hardcode the recursion guard** at the wrapper layer (env var or skill-name check), not inside the skill (skill might forget).
3. **Initialize a known-incident registry file** as part of the skill ship. Use it for pre-suppression during in-flight fixes.
4. **Implement cross-day dedup** with a clear "if same error hash N days in a row, suppress unless severity escalates" rule.
5. **Document the suppression mechanisms in SKILL.md** so future agents know how to add a pre-suppression entry without reading the code.

## Related

- `feedback_mutating_skill_hardening_pattern` — every scheduled mutating skill needs headless prompt + POST_RUN_CHECK validator
- `feedback_launchd_parallel_fire_collisions` — stagger ≥30 min on parallel scheduled fires to avoid collision-look-alike failures
- ai-ops-5wx (niche-intelligence Tuesday hardening) — first real-world test of the suppression mechanism
- launchd-debugger SKILL.md — full architecture doc
