---
schema_version: 1.1.0
date: 2026-04-25
type: context
title: "Continuation — Session 6 (M&A Analytics page, non-DealsX zones)"
tags: [date/2026-04-25, context, topic/dashboard, topic/command-center, topic/ma-analytics, topic/session-6, topic/continuation]
---

# Continuation — Session 6: M&A Analytics page (non-DealsX zones)

## Read these first (in this order, ~5 min)

1. **`dashboard/mockup-ma-analytics.html`** — locked visual spec. Open in browser at the same time as building so you can compare side-by-side.
2. **`brain/context/continuation-2026-04-24-dashboard-scope-locked.md`** Section 4 — IA + scope notes for the page. Section "Post-May-7 follow-ups" lists the DealsX-blocked zones we're deferring.
3. **`dashboard/pages/c_suite_skills.py`** — closest-pattern reference. Same density (multi-zone page with KPI strips + tables), same render patterns, same theme primitives. Mostly copy structure from here.
4. **`memory/feedback_dashboard_visual_language_locked.md`** — palette + typography, do not diverge.
5. **`memory/project_dashboard_externalizes_mental_load.md`** — the load-bearing test for any zone you're tempted to add. If a zone doesn't externalize something Kay's tracking mentally, drop it.

## Locked decisions you can rely on (no re-scoping)

- 5 zones in mockup. **Build 3 full + 1 partial + 2 deferred placeholders** today.
- DealsX integration goes live **May 7** → unlocks Outbound Funnel (Zone 2) + AI Response Categorization (Zone 2.5) + DealsX rows in Channel Performance.
- Sidebar nav already shows M&A Analytics; flip `theme.py::NAV_ITEMS` to `True` once page renders.
- Page goes between Active Deal Pipeline and C-Suite & Skills (already in correct slot in NAV_ITEMS).

## Zone-by-zone build plan

### Zone 1 — Deal Flow Headline · 5 KPI tiles · SHIP TODAY

5 colored tiles (DealsX visual style, dark-theme adapted — see mockup).

| Tile | Color | Data source |
|---|---|---|
| Owner conversations | blue | weekly-tracker output (calls/Granola count this week) — OR Attio call logs in last 7 days |
| NDAs signed | purple | Attio MCP snapshot — count of records that moved into NDA stage in last 7 days. **Use `load_pipeline(scope="full")` and filter by `stage_since` field within 7 days of today** since stage_since updates each move |
| Financials received | yellow | Same Attio approach, filter to "Financials Received" stage |
| LOIs submitted | green | Same Attio approach, filter to "Submitted LOI" stage |
| Closed / Not proceeding | red | Attio closed_count or post-NDA-only filter from snapshot |

Pattern: re-use the `kpi-tile` CSS that the mockup uses (or rename to `gb-kpi-tile`); follow the dashed-circle / colored-border pattern.

### Zone 2 — Outbound Funnel · 5 KPI tiles · DEFERRED placeholder today

Render the zone header + a placeholder body with "Live May 7 · DealsX integration unlocks email + LinkedIn DM volume, opens, replies, positive replies, bounces." Match the placeholder pattern Infrastructure already uses (`gb-zone-pending` class).

### Zone 2.5 — Response Categorization · AI-Classified · DEFERRED placeholder today

Same pattern as Zone 2. Note: "Live May 7 · DealsX AI categorizes replies as Interested / Meeting Request / Information Request / Wrong Person / Not Interested / Uncategorizable + sentiment breakdown."

### Zone 3 — Channel Performance Table · PARTIAL today

6 channels in mockup: Kay email, Intermediary intro, JJ calls, DealsX email, DealsX LinkedIn DM, Conference. **Render 4 of 6 today**:

| Channel | Status | Data source |
|---|---|---|
| Kay email | full row | weekly-tracker email count + Attio reply rate |
| Intermediary intro | full row | weekly-tracker intermediary tag count |
| JJ calls | full row | JJ master sheet (the Activity Sheet — column conventions per `feedback_jj_call_date_from_field_not_tab.md`) |
| Conference | full row | weekly-tracker conference count |
| DealsX email | placeholder row showing "live May 7" | deferred |
| DealsX LinkedIn DM | placeholder row showing "live May 7" | deferred |

Use a yellow status pill on the deferred rows so it's visually obvious they'll populate later.

### Zone 4 — Trends · Last 12 Weeks · SHIP TODAY (best-effort)

4 sparkline panels (NDAs / Reply rate / Owner conversations / JJ dials). Each shows current value, week-over-week delta, and a 12-bar mini histogram.

**Data source:** Weekly-tracker writes a Google Sheet with weekly snapshots — query the last 12 rows of the appropriate columns. If the sheet structure doesn't have all four metrics historically, render the panels you have data for and stub the rest with "pending data history."

If weekly-tracker historical data is hard to query in Streamlit, write a small adapter in `data_sources.py::load_trend_data()` that reads a cached JSON snapshot (the agent can refresh the snapshot via gog Sheets API at build time, like Pipeline's snapshot pattern).

### Zone 5 — Activity Detail · This Week · SHIP TODAY

5 rows in mockup: Active niches, Conferences attended, Intermediary meetings, CIMs received, Business cards added.

| Row | Data source |
|---|---|
| Active niches | Industry Research Tracker sheet → count Active-Outreach niches |
| Conferences attended | weekly-tracker conferences-this-week field |
| Intermediary meetings | weekly-tracker intermediary-meetings tag |
| CIMs received | email-intelligence output (count of CIM-classified emails this week) |
| Business cards added | conference-engagement output (cards processed this week) |

Each row is a chip-list of the entities + a count number on the right. Same pattern as Infrastructure Zone 5 (Tech Stack inventory).

## Pattern reuse from earlier sessions (copy don't redesign)

1. **Page renderer skeleton** — copy `dashboard/pages/c_suite_skills.py`. Same structure: subtitle → summary → filter bar → zones rendered as `<section class="gb-zone">`.
2. **Data loader** — extend `dashboard/data_sources.py` with `load_ma_analytics()` returning a single dataclass with sub-fields per zone. Loader handles missing-data gracefully (returns None for zones with broken data sources rather than crashing the page).
3. **AppTest harness** — same `AppTest.from_function` pattern with `import streamlit as st` *inside* the harness. Verify 0 exceptions + spot-check zone labels render.
4. **Filter bar** — Daily / This Week / This Quarter / LTD pill toggle (visual-only first, interactive in a later session, like Deal Aggregator's filter bar). Channel + niche dropdowns same way.
5. **CSS** — extend `theme.py::GLOBAL_CSS` with the new `.gb-kpi-tile`, `.gb-trend-cell`, `.gb-act-row` classes. Match Infrastructure's `.gb-zone` patterns where applicable.

## Gotchas (still live)

- **Streamlit markdown parser eats 4-space-indented HTML** as code blocks. Always `textwrap.dedent(...).strip()`.
- **`AppTest.from_function` strips closures.** Import `streamlit as st` inside the harness.
- **Background hook auto-commits** — don't `git amend` if you didn't see the commit yourself.
- **Attio snapshot scope** — `load_pipeline(scope="full")` returns all stages; `scope="active"` only returns NDA-forward. Pick deliberately based on which deal-flow metric the zone needs.
- **Don't push to origin** unless Kay explicitly asks.

## First 10 minutes checklist

1. `lsof -ti:8501 | xargs kill 2>/dev/null` — clear stale Streamlit (it's been running since overnight).
2. Open `dashboard/mockup-ma-analytics.html` in browser as visual reference.
3. Read `dashboard/pages/c_suite_skills.py` end-to-end (~150 lines) — that's your structural template.
4. Decide adapter strategy for weekly-tracker sheet data (live read vs cached JSON). Cached JSON is simpler — start there.
5. Sketch the `MAAnalytics` dataclass at the top of a new `data_sources.py` section.
6. Build Zone 1 first (deal-flow KPIs, mostly Attio data) — single zone end-to-end, AppTest, then expand.
7. Flip `theme.py::NAV_ITEMS` `ma-analytics` to `True` once Zone 1 alone renders cleanly. Page becomes clickable mid-build.
8. Add zones 5 → 3 → 4 in that order (5 is small, 3 has the most zones-data variety, 4 is hardest).
9. Render placeholders for Zones 2 + 2.5 (DealsX-deferred).
10. Final AppTest + commit + verify all 6 routes return 200.

## Post-May-7 follow-up (don't do today)

When DealsX goes live:
- Wire Zones 2, 2.5, and DealsX rows in Zone 3 to live data
- Audit DealsX AI taxonomy vs JJ call log outcome categories (per scope-doc post-May-7 list)
- Confirm DealsX LinkedIn DM metric semantics (read receipts? connection-accepts?)

## Branch + state

- Branch: `imac-mid-day-save-2026-04-22`
- Latest commit: `e4cda57` (CLAUDE.md + health-monitor SKILL.md schedule docs)
- Streamlit running on `localhost:8501`, serving 5 of 6 nav items
- Working tree clean as of this file

## Estimate

~90 min focused. Zone 1 = 30 min. Zone 5 = 15 min. Zone 3 partial = 20 min. Zone 4 best-effort = 20 min. Placeholders + commit + AppTest = 10 min.
