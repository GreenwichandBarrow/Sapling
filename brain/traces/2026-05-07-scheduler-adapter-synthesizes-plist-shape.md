---
schema_version: 1.1.0
date: 2026-05-07
type: trace
title: "Scheduler adapter synthesizes plist-shaped dicts on Linux"
had_human_override: false
importance: medium
target: "skill:dashboard, process"
tags: ["date/2026-05-07", "trace", "topic/dashboard", "topic/systemd", "topic/scheduler-adapter", "topic/architecture", "pattern/shape-match-abstraction"]
---

# Trace: Scheduler Adapter Synthesizes Plist-Shaped Dicts on Linux

## Context

Phase 3 of the Linux migration ported 19 launchd plists to systemd user timers. The dashboard's `dashboard/data_sources.py` had launchd-specific reading throughout (`_registered_jobs()` calling `launchctl list`, `_read_plist()` using `plistlib.load`, several pages walking `StartCalendarInterval` dicts). Question: how to keep the dashboard rendering scheduler data on both platforms without forking display code?

## Decisions

### Adapter shape
**AI proposed:** Three options — (1) fork display code per platform with separate `_systemd_*` functions, (2) introduce a `ScheduledJob` dataclass that both backends produce + refactor display code to consume it, (3) build an adapter that returns plist-shaped dicts on both platforms (synthesizing a fake `StartCalendarInterval` from `OnCalendar` lines on Linux).

**Chosen:** Option 3. Built `dashboard/_scheduler_adapter.py` as a thin abstraction. macOS reads launchd as before. Linux reads systemd `.timer` files from `~/.config/systemd/user/` and synthesizes a plist-shaped dict with a fake `StartCalendarInterval` list back-derived from `OnCalendar` lines. Downstream code in `data_sources.py` consumes the same dict shape on either platform. `_registered_jobs()` and `_read_plist()` in `data_sources.py` were edited to delegate to the adapter; everything else unchanged.

**Reasoning:** The synthesized-dict pattern picks the "shape match" boundary as the abstraction layer. Every line of display code already knew how to walk `StartCalendarInterval` entries from years of launchd reading. On Linux, parsing `OnCalendar=Mon..Fri 06:00:00` back into 5 `{Weekday: N, Hour: 6, Minute: 0}` dicts is a small reversible mapping. Cost: one `_parse_oncalendar()` function (~30 lines). Benefit: zero changes to display code. The "proper dataclass" alternative was philosophically cleaner but blocked the migration — too many call sites to refactor in one session. Forking display code compounds maintenance burden every time the dashboard evolves.

**Pattern:** #pattern/shape-match-abstraction

## Learnings

When porting a system to a new runtime, the cheapest abstraction layer is often "match the shape the existing consumer already expects" rather than "design the proper interface." The proper interface can come later, once you understand the cross-platform requirements from running both. Today, picking shape-match got 19 timers + 5 dashboard pages working in 2 hours; the proper-dataclass refactor would have eaten the whole session.

A future agent looking at `_scheduler_adapter.py` might think it's hacky (fake plist on Linux) and want to "clean it up" by introducing the proper dataclass. The dataclass refactor is fine, but it's a *separate* project with its own risks (touches display code). Don't bundle it into a "while I'm here" cleanup. The synthesized-dict pattern is intentionally minimal and bounded.
