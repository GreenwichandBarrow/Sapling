---
name: dashboard same surface across time = nested view
description: When two dashboard surfaces are time-shifted views of the same data (live now vs frozen historical), nest one inside the other — never give them parallel sidebar entries.
type: feedback
originSessionId: 7b33e94d-2f80-4c58-94f4-cf166c53744f
---
When designing or modifying the G&B Command Center dashboard, **two surfaces that are time-shifted views of the same data belong as one nested page, not two parallel sidebar entries**. If the only difference between Page A and Page B is "Page A is live current state, Page B is frozen past state of the same metrics," the right architecture is one page with the past-state nested below (or behind a selector), not two sidebar items.

**Why:** May 1 2026 — Kay flagged the M&A Analytics + M&A Activity sidebar as a "duplicated tab." Investigation showed they were technically distinct pages (live Attio snapshot vs frozen weekly snapshot via `snapshot_weekly()`), but they rendered the same conceptual surface (M&A activity metrics) at different time-windows. Kay's instinct: "if it isn't a true duplicate the M&A archive should be nestled within the M&A Analytics tab." Architectural fix beat the surface-level rename fix because the underlying mental model (one surface, two time-windows) was misaligned with the UX (two parallel pages).

**How to apply:**
- Before creating a new sidebar entry, ask: "Is this a different surface, or the same surface at a different time/state?" If same-surface-different-time → nest under existing parent, don't spawn a sibling.
- When refactoring an existing duplicated-feeling sidebar, prefer Path A (nest at bottom of parent + drop sibling sidebar entry) over rename-only fixes. Rename-only addresses the symptom; nesting addresses the cause.
- Bottom-of-page is the correct nest position when the live view is the primary use case and the historical/archive is the drill-down. Use top-of-page tabs only when live and archive are equal-weight surfaces (rare).
- Don't merge to a single-selector page (Path B) until layouts naturally converge — premature merging creates stale placeholders that confuse historical data.

**Where this lives:** `dashboard/theme.py` `NAV_ITEMS`, `dashboard/command_center.py` `_PAGE_RENDERERS`, individual page modules in `dashboard/pages/`. Trace: `[[traces/2026-05-01-dashboard-nested-archive-not-sidebar]]`.
