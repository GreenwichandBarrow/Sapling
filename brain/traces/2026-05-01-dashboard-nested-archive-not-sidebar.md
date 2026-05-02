---
schema_version: 1.1.0
date: 2026-05-01
type: trace
today: "[[notes/daily/2026-05-01]]"
task: Resolve M&A Analytics + M&A Activity sidebar duplication
had_human_override: true
importance: medium
target: process
tags: [date/2026-05-01, trace, topic/dashboard, topic/ui-architecture, pattern/same-surface-across-time-nested]
---

# Decision Trace: M&A Archive Nested in Parent, Not Separate Sidebar Entry

## Context

Kay flagged via screenshot at 10:24am that the G&B Command Center sidebar showed both "M&A Analytics" and "M&A Activity" — she read this as a duplicate. Investigation found they were two distinct pages: M&A Analytics (live current-state with Attio snapshot zones) and M&A Activity / week-archive (frozen weekly historical snapshots with a week selector).

Three resolution paths existed:
- **Rename only:** Rename "M&A Activity" → "Weekly Archive" to clarify the distinction. Both stay as separate sidebar entries.
- **Path A (nested at bottom):** Render live zones at top of M&A Analytics, append a divider + the archive section (with inline week selector) below. Drop the second sidebar entry.
- **Path B (full single-page selector merge):** One zone structure, top-of-page week dropdown selecting "This week" (live Attio) vs any past week (frozen snapshot). Requires reconciling differing zone layouts.

## Decisions

### Sidebar layout — pick the right architecture, not just the right name

**AI proposed:** Rename "M&A Activity" → "Weekly Archive" (one-line label change).

**Chosen:** Path A — drop the second sidebar entry; nest the archive section at the bottom of M&A Analytics.

**Reasoning:** The two pages are the *same surface across time*, not different surfaces. They render the same metrics, just with different time-windows of data (live Attio vs frozen weekly snapshot). When two surfaces are time-shifted views of the same data, they belong on one page, not two sidebar entries. A rename only addresses the symptom (label confusion); the architectural fix removes the cause (parallel sidebar entries that are conceptually one surface).

**Pattern:** #pattern/same-surface-across-time-nested

### Tab placement — bottom, not top

**AI proposed:** `st.tabs(["This Week (Live)", "Archive"])` at top of M&A Analytics.

**Chosen:** Live zones render unmodified at top; archive nested *below* via inline section divider + section header + inline column-constrained week dropdown.

**Reasoning:** Kay explicit: "tabs at the bottom, not the top." The live page IS the page; the archive is a footer to it. Putting tabs at the top makes both views feel equal-weight and forces a click to see the live data — wrong defaults. Bottom-nested treats the archive as a drill-down, which matches its purpose.

**Pattern:** #pattern/primary-content-default-secondary-nested

### Path B deferred

**AI proposed:** Full single-page selector merge (Path B) as the long-term clean state.

**Chosen:** Defer Path B until DealsX zones go live May 7 and the live page's 6-zone layout converges with the archive's 5-zone layout.

**Reasoning:** Merging now would either (a) drop the DealsX-deferred placeholders from live (premature given the May 7 plan) or (b) create stale "Pending — live May 7" placeholders in historical snapshots that never had DealsX data. Better to nest now (Path A) and refactor to single-selector once layouts naturally unify.

## Learnings

- When a "duplicate" complaint surfaces in the UI, ask: "are these the same surface across different time/state windows?" If yes → nest, don't rename. If no → rename or merge content.
- Don't add a parallel sidebar entry for a time-shifted view of an existing page. The default should be: one page, one selector for time/state.
- Architectural fixes beat label fixes when the underlying mental model is misaligned. The label is a symptom.
- Kay's directional instincts (here: "nested under parent") often point at the cleaner architecture even when the surface ask is just "rename."
