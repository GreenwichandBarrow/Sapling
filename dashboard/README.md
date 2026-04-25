# G&B Command Center — Dashboard

Streamlit app at `localhost:8501`. Replaces Kay's Weekly Activity Tracker
spreadsheet + multiple ad-hoc tools with a single live operational surface.

## Quick start

```bash
# Launch (kill any prior instance first to avoid port-busy)
lsof -ti:8501 | xargs kill 2>/dev/null
dashboard/.venv/bin/streamlit run dashboard/command_center.py

# Open in browser
open http://localhost:8501
```

Theme config lives in `dashboard/.streamlit/config.toml` — sets
`primaryColor` to G&B accent blue so Streamlit's built-in widgets
(active page_link, segmented_control selected pill) inherit it
automatically. Don't move the file out of `dashboard/.streamlit/`;
Streamlit only reads it from the run-directory.

## Architecture

```
dashboard/
  command_center.py      # Streamlit entrypoint — st.navigation router,
                         # sidebar, topbar, staleness banner
  data_sources.py        # All data loaders (Attio, JJ, calls, calibration,
                         # weekly-tracker, system health, tech stack).
                         # Returns plain dataclasses; pages stay decoupled.
  theme.py               # PALETTE (colors), NAV_ITEMS (sidebar order),
                         # GLOBAL_CSS (~1500 lines) injected on every page
  pages/
    dashboard_landing.py # Hero Active Deal Pipeline tile + 4 small tiles
    deal_aggregator.py   # Daily new-leads table from broker scan artifacts
    deal_pipeline.py     # NDA-forward kanban from Attio snapshot
    ma_analytics.py      # 5-zone activity rollup (replaces weekly tracker
                         # spreadsheet); Zone 2 + 2.5 deferred to DealsX
                         # May 7
    c_suite_skills.py    # Scheduled-skill canary by C-suite agent
    infrastructure.py    # 5 zones: System Health, External Connectivity,
                         # Credits & Spend, Calibration, Tech Stack
  data/                  # Operator-maintained YAML catalogs
    tech_stack.yaml
    external_services.yaml
    credits.yaml
    calibration.yaml
  .streamlit/
    config.toml          # Theme + server config
```

### Data flow pattern

Every page follows the same shape:

```
launchd cron → refresh script → JSON snapshot in brain/context/
                                       ↓
                            data_sources.load_X() reader
                                       ↓
                            page render (HTML strings injected
                            via st.markdown(unsafe_allow_html=True))
```

Streamlit pages are pure read; mutations happen in scheduled scripts
that write to brain/. Pages can't call MCP tools (those live in the
Claude Code harness, not the Python process), so the snapshot pattern
is the contract between agent (writer) and dashboard (reader).

## Scheduled refresh jobs

Both registered in launchd; status: `launchctl list | grep snapshot`.

| Job | Schedule | Output | Wrapper |
|-----|----------|--------|---------|
| `attio-snapshot-refresh` | Mon-Fri hourly 8am-8pm ET (65 fires/wk) | `brain/context/attio-pipeline-snapshot.json` | `scripts/refresh-attio-snapshot.sh` |
| `jj-snapshot-refresh` | Mon-Fri 9am, 2:30pm, 6pm ET (15 fires/wk) | `brain/context/jj-activity-snapshot.json` | `scripts/refresh-jj-snapshot.sh` |

Both use `scripts/.env.launchd` for secrets (`ATTIO_API_KEY`).
Logs at `logs/scheduled/{name}-{date-time}.log`, 14-day rotation.

### Manual trigger

```bash
# Force refresh (useful after a data change you want reflected immediately)
launchctl start com.greenwich-barrow.attio-snapshot-refresh
launchctl start com.greenwich-barrow.jj-snapshot-refresh

# Or run wrapper directly
bash scripts/refresh-attio-snapshot.sh
bash scripts/refresh-jj-snapshot.sh
```

### Staleness handling

Dashboard surfaces a yellow banner above every page if a snapshot is
beyond its threshold. Thresholds are weekend-aware (refresh jobs are
weekday-only): 2h business-hours / 60h off-hours for Attio, 30h / 72h
for JJ. Logic in `data_sources.check_dashboard_staleness()`.

Health-monitor's nightly check uses more permissive thresholds (4h/12h
business-hours, 60h/80h overall) so it only flags genuinely-broken jobs,
not the expected gap between runs.

## Adding a new page

1. Create `pages/your_page.py` with a `render()` function that takes no
   args. Inside `render()`, do `import streamlit as st` (works around
   `AppTest.from_function` closure-stripping per the gotchas section).
2. Add a `(label, url_path, True)` tuple to `theme.NAV_ITEMS` in the
   right slot. `True` = implemented; `False` renders as disabled.
3. Register `(render_fn, "Page Title")` in `command_center._PAGE_RENDERERS`
   keyed by url_path.
4. Add CSS for any new visual primitives to `theme.GLOBAL_CSS` (use the
   `gb-` prefix on classes to avoid collisions with Streamlit internals).
5. Run `lsof -ti:8501 | xargs kill && dashboard/.venv/bin/streamlit run
   dashboard/command_center.py` and verify route returns 200.

## Adding a new data source

If the source is a Google Sheet or Attio query: build a refresh script
under `scripts/refresh_X.py` that writes a JSON snapshot to
`brain/context/X-snapshot.json`. Mirror the Attio script pattern.

If the source is a local artifact (vault file, log, settings): add
the loader directly to `data_sources.py` — see `_scan_calls()` for
the pattern.

In either case, return a plain dataclass from the loader so the
render layer doesn't need to know the source format.

## Gotchas (still live)

- **Streamlit markdown parser eats 4-space-indented HTML** as code blocks.
  Always `textwrap.dedent(...).strip()` before injecting.
- **`AppTest.from_function` strips closures.** Import `streamlit as st`
  *inside* the harness function, not in the module scope.
- **Background hook auto-commits** changes during a session. If your
  `git add && git commit` says "nothing to commit", check
  `git log -1 --stat` — the hook likely grabbed it as `update X`.
  Don't `git amend` on these.
- **Streamlit's Emotion CSS-in-JS beats external CSS overrides** for
  built-in widgets. For things like the active page_link color, set
  `[theme]` values in `.streamlit/config.toml`; for things like sidebar
  spacing, use very-specific `[data-testid]` selectors with `!important`.
- **`gog sheets get`** uses positional `<range>` arg, not `--range`. Tab
  names with spaces need single quotes: `'Full Target List'!T2:V`.
- **Attio doesn't expose stage history** in the entry query endpoint.
  To distinguish post-NDA failures from pre-NDA outreach attrition, use
  the `meaningful_conversation` checkbox + notes count as engagement
  signal — see `_entry_engagement_signal()` in the Attio refresh script.
- **Don't push to origin** unless Kay explicitly asks.

## Testing

No formal test suite. AppTest spot-check pattern:

```python
from streamlit.testing.v1 import AppTest

def _h():
    import sys; sys.path.insert(0, 'dashboard')
    import streamlit as st
    from theme import GLOBAL_CSS
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    from pages import your_page
    your_page.render()

at = AppTest.from_function(_h).run(timeout=15)
assert len(at.exception) == 0
```

Plus `curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8501/your-route`
should return 200.

## Session history

| # | Date | Scope |
|---|------|-------|
| 1 | 4/22 | App shell + landing tile grid |
| 2 | 4/22 | Deal Aggregator page + st.navigation router |
| 3 | 4/24 | Active Deal Pipeline page (Attio kanban) |
| 4 | 4/24 PM | Mockup-first design pass — locked all 6 page mockups |
| 4.5 | 4/24 | Active Deal Pipeline polish — NDA-forward scope |
| 5 | 4/24 | Infrastructure page Zones 1 + 5 (deferred 2/3/4) |
| 6 | 4/25 | M&A Analytics page (3 zones live + 2 DealsX-deferred) |
| 6 polish | 4/25 | Mockup-fidelity sweep across all pages |
| 6 backend | 4/25 | Snapshot scheduled refreshes (Attio + JJ), Closed-strip post-NDA split, Weekly-tracker history backfill, CIM regex fix, Filter pill interactivity, Staleness banner |
| Infra Zones 2/3/4 | 4/25 | External Connectivity, Credits & Spend, Calibration & Learning |

Locked mockup HTML lives in `dashboard/mockup-*.html`. Compare against
live render before declaring a page done.
