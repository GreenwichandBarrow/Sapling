---
schema_version: 1.1.0
date: 2026-04-24
type: context
title: "Continuation — Dashboard Session 3 (Deal Pipeline page)"
tags: [date/2026-04-24, context, topic/dashboard, topic/command-center, topic/continuation, topic/session-3]
---

# Continuation — Dashboard Session 3 (Deal Pipeline Page)

## What's shipped

- **Session 1** — commit `536210c`: app shell, custom sidebar + topbar, Dashboard landing with 6 placeholder tiles.
- **Session 2** — commit `5ae7203`: Deal Aggregator page live; `st.navigation(position="hidden")` router; sidebar uses `st.page_link` for implemented pages, disabled HTML for the rest; artifact parser reads `brain/context/deal-aggregator-scan-*.md`; 8 real deal rows render.

Master scope (locked, don't re-scope): [[brain/context/continuation-2026-04-24-dashboard-scope-locked]]
Session-2 decisions + bugs caught: [[brain/context/session-decisions-2026-04-24]]

## Session 3 target: Deal Pipeline

**Purpose:** Live Attio pipeline replica — deals by stage, click through to the Attio record. Primary daily-glance view.

**Data source:** Attio MCP — the `mcp__attio__*` tool family is already available. Key calls you'll likely want:
- `mcp__attio__get-lists` — discover the Deal Pipeline list by name
- `mcp__attio__get-list-details` — stage definitions
- `mcp__attio__get-list-entries` / `advanced-filter-list-entries` — pull records grouped by stage
- `mcp__attio__get_record_details` — per-deal detail for row rendering
- Attio record URL pattern: `https://app.attio.com/greenwich-barrow/deals/record/{record_id}` (verify against a known deal before shipping).

**Still-open scope decision** (do NOT decide alone — ask Kay at session start):
> Kanban columns (one per stage, deals as cards) **OR** tabular with a stage-filter dropdown?
>
> Kanban is the common "pipeline" visual but eats horizontal space and fights the 3-col data-table grid the other pages use. Table-with-stage-filter keeps the pattern consistent with Deal Aggregator and scales better if the pipeline grows beyond ~5 active stages.
>
> **RECOMMEND: tabular with stage-filter tabs at the top** (matches Deal Aggregator's filter-tab pattern, reuses the existing .gb-table CSS, scans left-to-right like the rest of the app). → YES / NO / LET'S DISCUSS

Get this answered before building.

## Patterns to reuse from Session 2

1. **Artifact/data loader as a separate module.** `dashboard/data_sources.py` is the right home for Attio fetches too — add an `attio_deals.py` or extend `data_sources.py` with `load_pipeline()` returning a list of `DealPipelineEntry` dataclasses. Keep the MCP-calling code out of the page render function.
2. **Render functions return HTML strings, `st.markdown(..., unsafe_allow_html=True)` dumps them.** Use `textwrap.dedent(...).strip()` so the HTML is left-flush (4-space indent triggers Streamlit's code-block parser — Session 1 gotcha, still live).
3. **`st.page_link` in sidebar + CSS overrides via `[data-testid="stPageLink"]`** already wired. To enable the Deal Pipeline nav item, flip its third tuple element from `False` → `True` in `dashboard/theme.py::NAV_ITEMS` and register the renderer in `command_center.py::_PAGE_RENDERERS`.
4. **AppTest before claiming done.** `streamlit.testing.v1.AppTest.from_file(...)` caught the `KeyError: 'dashboard'` bug in Session 2 before the UI would have. Run it on both the landing and the new page after any routing change.
5. **Empty-state fallback.** Attio may have 0 active deals at times — render a "No active deals in pipeline" cell rather than a bare empty table.

## Gotchas (still live)

- **Port 8501:** Session 2 freed it at end. If reopening a Streamlit instance from a prior session, `lsof -ti:8501 | xargs kill` first.
- **Streamlit markdown parser eats 4-space-indented HTML** as code blocks. All injected HTML must be left-flush after `dedent`.
- **`st.Page(default=True)` normalizes `.url_path` to `""`** — keep your own url_path → page map rather than round-tripping via `page.url_path`. (Bug already fixed; don't re-introduce.)
- **Deal Aggregator's data window is 14 days** (labeled "this week" — widened because `volume_7d_avg=0.14` makes a true 7-day window usually empty). If you touch the Deal Aggregator page, don't revert — re-read `session-decisions-2026-04-24.md` first.

## Environment

- venv: `dashboard/.venv/` — has `streamlit`, `pandas`, `pyyaml`. Attio MCP tools don't require any Python deps, they're in-harness.
- Launch: `dashboard/.venv/bin/streamlit run dashboard/command_center.py`
- URL: `localhost:8501/deal-pipeline` once registered.
- Branch: `imac-mid-day-save-2026-04-22`. After commit `5ae7203`, 1 commit ahead of origin (not pushed; Kay's call whether to push before Session 3).

## First 10 minutes of Session 3

1. Resolve Kanban-vs-tabular with Kay. Don't start coding until it's decided.
2. `mcp__attio__get-lists` → find the Deal Pipeline list ID + record the stage sequence.
3. Peek at one real deal entry so you know what fields you actually have (stage, deal name, company, last_stage_change, NDA status, LOI date, etc.).
4. Then decide column layout (or Kanban card layout) from real fields, not the mockup's fake ones.
5. Build. AppTest. Commit. Session-decisions. Done.

## Do NOT

- Don't marathon into Session 4 (C-Suite & Skills). One page per session — Kay has explicit pacing rules.
- Don't flip the briefing format (4-bucket → Decisions-only); still blocked per `feedback_build_new_before_sunset_old` until all 6 dashboard pages are live and verified.
- Don't retire the Weekly Activity Tracker Google Sheet — that waits for Session 6 (M&A Analytics).
