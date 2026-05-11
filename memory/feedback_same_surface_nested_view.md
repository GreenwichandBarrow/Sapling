---
name: Same surface across time = nested view, not separate sidebar entry
description: Dashboard UI principle — historical/archive views of the same surface nest within the live page; never spawn a parallel sidebar entry per time-window.
type: feedback
originSessionId: a5d2f444-4767-400d-829d-ddf5db780f69
---
# Same-surface = nested view

Codified 2026-05-01 from G&B Command Center M&A Analytics + M&A Activity merge. See `brain/traces/2026-05-01-same-surface-nested-view-principle.md`.

When a new dashboard page would render the SAME information surface at a different time-window (current week vs archived weeks, today vs yesterday, this quarter vs prior quarters), do NOT add a parallel sidebar entry. Nest the historical view at the bottom of the live page, separated by a divider + section header.

**Why:** Sidebar nav is a taxonomy of surfaces (M&A vs DealsX vs Operations vs Infrastructure), not a taxonomy of moments. Every "X Archive" sidebar entry is a sign the surface itself isn't being treated as the unit. Time-windows nest within surfaces; surfaces don't fork along time. Kay flagged this when M&A Analytics + M&A Activity duplicated the same metrics surface at different time slices.

**How to apply:**

Decision tree for any new dashboard page:
1. Renders a NEW information surface? → New sidebar entry OK.
2. Renders an EXISTING surface at a different time-window? → Nest as bottom-of-page section in the live page. Use `gb-archive-divider` + `gb-archive-section-head` CSS hooks.
3. Renders an EXISTING surface for a different ENTITY (e.g., per-niche)? → Nest as a tabbed view inside the live page.

Catch this when reviewing any PR that adds an entry to `dashboard/theme.py:NAV_ITEMS`. If the new entry name contains "Archive," "History," "Past," or matches the prefix of an existing entry, default to nest, not add.

Implementation pattern (from M&A Activity merge):
- Remove the page module from `NAV_ITEMS`.
- Keep the page module file so its `render()` can be imported.
- In the parent live page, append `st.markdown('<div class="gb-archive-divider">')` + section header + `child_module.render()` after the live content.
