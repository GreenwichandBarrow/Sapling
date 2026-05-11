---
name: Dashboard Weekly Flow indicators persist through the week
description: C-Suite & Skills page — fired/missed health rings on past-day tiles must remain visible all week, not just on the day-of
type: feedback
originSessionId: 9630552b-8df3-4a81-bdb0-4d83150dadf8
---
C-Suite & Skills "Weekly Flow" grid: when a scheduled skill fires (or misses) on Sunday, the green ring (or red dashed border) must remain visible on Sunday's column through Saturday. The week resets on Sunday-of-the-next-week.

**Why:** Kay reads the grid as a running record of "what fired vs what didn't this week," not just "what's happening today." If indicators reset overnight, Sunday's outcome disappears Monday morning — Kay loses visibility into yesterday's misses. (Source: 2026-05-04 — Kay screenshot of C-Suite & Skills + "for example today, Monday, I should still be able to see what failed yesterday - sunday".)

**How to apply:**
- Past-day tiles in `pages/c_suite_skills.py::_render_weekly_flow` apply the same `fired-ok / fired-warn / fired-err / missed` CSS classes as today's tile, sourced from `SkillHealth.week_status_by_day` (per-iso-weekday status map computed in `data_sources._build_week_status`).
- `theme.py` `.gb-flow-day.past` opacity must NOT dim tiles that carry a status class — only the day-header and unstatused tiles. If a future calibration / refactor reapplies blanket opacity to `.gb-flow-day.past`, it regresses this rule.
- Subtitle legend says "Green = fired this week" (NOT "fired today") for the Weekly Flow. The summary pill row above ("3 fired today") is still today-only — those are different surfaces.
- If you change the week-start day (currently Sunday-first to match the grid), update both `_week_sunday()` in data_sources AND `_SUN_TO_SAT` ordering in c_suite_skills.
