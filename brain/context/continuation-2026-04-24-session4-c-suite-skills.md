---
schema_version: 1.1.0
date: 2026-04-24
type: context
title: "Continuation — Dashboard Session 4 (C-Suite & Skills page)"
tags: [date/2026-04-24, context, topic/dashboard, topic/command-center, topic/continuation, topic/session-4]
---

# Continuation — Dashboard Session 4 (C-Suite & Skills page)

## What's shipped

- **Session 1** (`536100c`): app shell + Dashboard landing + 6 tiles.
- **Session 2** (`5ae7203`): Deal Aggregator page + `st.navigation` router.
- **Session 3** (`f4d5e48` + auto-commit `4c083e4`): Deal Pipeline page — 6-col Kanban replica of Attio `Active Deals – Owners` list, closed strip below, snapshot-file pattern (agent writes via Attio MCP → Streamlit reads JSON).

Master scope (locked): [[brain/context/continuation-2026-04-24-dashboard-scope-locked]]
Session-3 decisions + bugs caught: [[brain/context/session-decisions-2026-04-24]] (Session 3 section appended at bottom)

## Session 4 target: C-Suite & Skills

**Purpose (locked in scope doc):** Scheduled-skill fire/no-fire canary organized by C-suite agent. Hierarchical: 6 C-suite leads (CFO / CIO / CMO / CPO / GC / COO) as top-level rows, their skills nested beneath. Primary signal per skill = did it fire when it should have today.

**Visual spec (locked):**
- Status dot per skill: green (fired), yellow (fired with warning), red (didn't fire but should have), grey (not scheduled today)
- Click skill → expand last 5 runs + log output
- Pober-style 10.5px uppercase muted labels for C-suite section headers
- Match `mockup-deal-aggregator.html` patterns where possible — this is a list page, not a tile page

## Data sources — no MCP needed this time

All data is local filesystem + shell. Streamlit can read it directly. Much simpler than Session 3.

1. **`launchctl list | grep greenwich`** — returns currently-registered launchd jobs. Parse lines like `-\t0\tcom.greenwich-barrow.{skill}`. Columns: pid (`-` if not currently running) / exit-code (`0` = last run OK) / label. Signals whether the job is even registered with the system.
2. **`logs/scheduled/{skill}-{YYYY-MM-DD}-{HHMM}.log`** — actual run logs, 14-day rotation (per CLAUDE.md). Today's logs = did it fire today.
3. **`~/Library/LaunchAgents/com.greenwich-barrow.{skill}.plist`** — the schedule itself (hours/weekdays). You can parse these plists (XML) to know when each job *should* fire, which unlocks the "should-have-fired but didn't" red-dot logic.
4. **CLAUDE.md Scheduled Skills table** — authoritative human-readable schedule spec. Cross-reference the plists against this when writing the skill→cadence map.

## Still-open scope decision — ask Kay at session start

**C-suite → skill assignment.** The visual is hierarchical by C-suite agent, but the mapping from skill to owner isn't fully codified. `memory/feedback_c_suite_naming.md` says always label which C-suite owns each piece of work, but the skill-level mapping has to be explicit for the page.

Proposed starter mapping (Claude's cut — present to Kay for approval; she may re-route):

| C-suite | Skills |
|---|---|
| **CIO** (Chief Investment Officer) | deal-aggregator, deal-aggregator-afternoon, deal-aggregator-friday, niche-intelligence, target-discovery-sunday, nightly-tracker-audit, conference-discovery |
| **CPO** (Chief People Officer) | relationship-manager, jj-operations-sunday |
| **CMO** (Chief Marketing Officer) | email-intelligence, weekly-tracker |
| **CFO** (Chief Financial Officer) | (none scheduled today — show empty state) |
| **GC** (General Counsel) | (none scheduled today — show empty state) |
| **COO** (Chief of Staff) | calibration-workflow |

**RECOMMEND: use the table above as a starting point.** Kay sign-off or re-route before building — otherwise the page ships with the wrong mental model.

## Patterns to reuse from Sessions 1–3

1. **Data loader as a separate function in `dashboard/data_sources.py`.** Add a `load_skill_health()` returning `list[SkillHealthRow]` (dataclass: skill, c_suite, scheduled_today, last_run, last_status, recent_runs). Keep all shell-outs (`launchctl list`, log-file scan) in the loader — page render stays pure.
2. **Render functions return HTML strings; `st.markdown(..., unsafe_allow_html=True)` dumps them.** Dedent with `textwrap.dedent(...).strip()` so HTML is left-flush (Streamlit markdown parser eats 4-space-indented HTML as code blocks).
3. **Status dot classes already exist in `theme.py`**: `.gb-status-dot.green`, `.yellow`, `.red` with soft glow. Add a `.grey` variant if not present. Reuse don't recreate.
4. **`st.expander`** handles the click-to-expand-last-5-runs pattern natively — no custom JS needed. But style it via `[data-testid="stExpander"]` to match the dark theme (similar to how `st.page_link` got re-skinned in Session 2).
5. **AppTest on both the landing and the new page before claiming done.** Use the `AppTest.from_function` harness pattern from Session 3 (import `streamlit as st` *inside* the function — AppTest's function-based mode strips the module closure).
6. **Flip the Session 4 nav item's `implemented` flag to `True` in `theme.py::NAV_ITEMS`** and register the renderer in `command_center.py::_PAGE_RENDERERS["c-suite-skills"]`.

## Gotchas (still live)

- **Port 8501:** Session 3 left the Streamlit server running (Kay was verifying). Before starting Session 4: `lsof -ti:8501 | xargs kill`.
- **Streamlit markdown parser eats 4-space-indented HTML** as code blocks. Must be left-flush after `dedent`.
- **`st.Page(default=True)` normalizes `.url_path` to `""`** — keep your own url_path → page map (already handled in `command_center.py`).
- **`AppTest.from_function` strips closures.** Import `streamlit as st` *inside* the harness function, not at module level, or you'll get `NameError: name 'st' is not defined`.
- **Hook auto-commits** fire in the background. Session 3 saw `theme.py`, `data_sources.py`, `command_center.py` auto-committed mid-session by a background git hook ("update context, dashboard"). Don't `git amend` if you didn't see the commit yourself — make a new commit for the rest.
- **Don't flip the briefing format (4-bucket → Decisions-only)** until all 6 dashboard pages are live and verified (per `feedback_build_new_before_sunset_old`).
- **Don't retire the Weekly Activity Tracker Google Sheet** — that waits for Session 6 (M&A Analytics).

## Environment

- venv: `dashboard/.venv/` — has `streamlit`, `pandas`, `pyyaml`.
- Launch: `dashboard/.venv/bin/streamlit run dashboard/command_center.py`
- URL: `localhost:8501/c-suite-skills` once registered.
- Branch: `imac-mid-day-save-2026-04-22`. Session 3 committed as `f4d5e48`; 2+ commits ahead of origin at Session 4 start.

## First 10 minutes of Session 4

1. Kill any lingering Streamlit: `lsof -ti:8501 | xargs kill` (Session 3 left it up).
2. Resolve C-suite → skill mapping with Kay (the table above as starting point). Don't start coding until confirmed.
3. Read the plist for ONE skill (e.g. `~/Library/LaunchAgents/com.greenwich-barrow.deal-aggregator.plist`) to confirm the schedule-parsing approach. Plists are XML; `plistlib` is stdlib.
4. Read one real log file to confirm the "success" heuristic — exit code in the launchctl list plus non-empty log content is probably the minimum.
5. Build loader, page, CSS. AppTest. Commit. Session-decisions.

## Do NOT

- Don't marathon into Session 5 (Infrastructure). One page per session — explicit pacing rule.
- Don't silently drop skills that aren't scheduled via launchd (there are many — triage, today, task, etc.). This page is scoped to *scheduled* skills only. If Kay wants on-demand skills too, that's a Session 4.5 scope expansion — ask, don't assume.
- Don't hard-code the "should have fired today" logic off Claude's current-weekday guess. Parse the plist's `StartCalendarInterval` array; it's authoritative.
