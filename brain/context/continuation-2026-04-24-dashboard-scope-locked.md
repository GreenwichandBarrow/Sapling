---
date: 2026-04-24
type: context
title: "Continuation — G&B Command Center Dashboard Scope Locked"
tags:
  - date/2026-04-24
  - context
  - topic/dashboard
  - topic/command-center
  - topic/continuation
  - topic/streamlit
---

# Continuation — Dashboard Scope Locked (2026-04-24, PM)

## Purpose

This file **supersedes** `continuation-2026-04-24-dashboard-build.md` (the AM session's starting point). Today's PM scoping session rewrote the information architecture from the 4-pane Pober-mimic to a 7-section sidebar-nav app. All scope decisions, visual language, and memories are captured here so the next session can start building without re-scoping.

## State at end of this session

**Locked:**
- 7-section information architecture (see below)
- Dashboard landing page — fully scoped + visual mockup approved
- Deal Aggregator page — fully scoped + visual mockup approved
- Visual language (dark theme, Avenir, tile-grid + data-table patterns)
- Global behaviors (desktop-only, 60s polling, briefing stays terminal)
- Build pacing (one page per session across ~6 sessions)

**Not yet built:** nothing. This was a pure scope + mockup session. No Streamlit code written, no skills modified. Two HTML mockup files exist (throwaways) as visual reference.

**Memories saved today** (in `memory/`):
- `feedback_kay_only_audience_for_internal_tools.md` — Dashboard replaces Weekly Activity Tracker; both have Kay as sole audience.
- `feedback_dashboard_scope_not_reminders.md` — Dashboard excludes email-draft reminders and daily nurture prompts; per-skill activity goes to health-monitor as digest lines.
- `feedback_skill_fire_status_is_canary.md` — C-Suite & Skills page primary signal is fire/no-fire per skill per day.
- `feedback_tech_stack_page_is_connectivity_canary.md` — Tech Stack page = OAuth/API/MCP + credit + subscription-creep canary.
- `feedback_silent_failures_are_the_core_concern.md` — META: silent failures are Kay's top operational worry. Always scope "what fails silently?" first.
- `feedback_dashboard_visual_language_locked.md` — Dark theme + Avenir + tile-grid + data-table patterns validated by Kay ("blown away").

## Information Architecture (LOCKED, REVISED 2026-04-24 PM)

**Six sections** (revised from 7), left-sidebar nav, Dashboard as landing page. Tech Stack collapsed into Infrastructure on 2026-04-24 during Session 4 design review — boundary between "external connectivity canary" and "system health" was thin and creating split mental model. Now one place to ask "is the plumbing OK?"

| # | Page | Primary purpose | Cadence |
|---|------|-----------------|---------|
| 1 | **Dashboard** (landing) | Top-line metrics — one tile per sub-page, 1:1 mapping (5 tiles after Tech Stack merge) | Daily glance |
| 2 | **Deal Aggregator** | Businesses actively selling — aggregated from broker platforms, email, association boards. Replaces #deal-aggregator Slack posts. | Daily glance |
| 3 | **Deal Pipeline** | Live Attio pipeline replica — deals by stage, clickable through to Attio records. | Daily glance |
| 4 | **C-Suite & Skills** | Scheduled-skill fire/no-fire canary organized by C-suite agent (COO/CIO/CPO/CMO/CFO/GC, in that visual order). Primary signal: did each scheduled skill fire when it should have? | Daily check |
| 5 | **Infrastructure** | System health + external connectivity & tooling + credits & spend + calibration & learning + full tech stack inventory. Five zones, one page. | Daily glance, deep review Fridays |
| 6 | **M&A Analytics** | Activity rollups — daily / weekly / quarterly / LTD. **Replaces Weekly Activity Tracker Google Sheet** once weekly-view ships. | Weekly for core metrics |

**Dropped** (Kay's explicit calls during scoping):
- Inbox & Replies page — don't need
- Buyer Match page — N/A for G&B
- Buyer Outreach page — N/A for G&B
- AI Agents as vanity metrics page — demoted into C-Suite & Skills with fire-status as primary signal
- Briefing renderer on dashboard — terminal briefing stays primary
- Email draft reminders — Kay checks Superhuman directly
- Daily nurture-cadence reminders — demoted to Friday-only elsewhere
- Dedicated Conference/Niche/Investor-prep pages — collapsed into Infrastructure digest lines

## Visual Language (LOCKED)

**Reference mockups** — match these exactly in the Streamlit build:
- `dashboard/mockup-landing.html` — tile grid pattern for Dashboard landing + any tile-based page
- `dashboard/mockup-deal-aggregator.html` — data table pattern for Deal Aggregator, Deal Pipeline, C-Suite & Skills, Tech Stack, any page showing rows of entities

**Full spec** lives in `memory/feedback_dashboard_visual_language_locked.md`. Short form:

Shared across all pages:
- Near-black bg (`#0B0D12`), panels (`#141821`), borders (`#242A36`)
- Avenir Next / Avenir stack
- Label treatment: 10.5px uppercase letter-spaced muted (Pober-style)
- Status dots: 8px colored dots with soft glow (not emoji)
- Sidebar: 240px, left, active item = accent-blue wash

Tile grid (landing):
- Primary metric 36px weight 300
- 3 cols × 2 rows, 16px gap, 10px border-radius
- Trend arrows (↑ ↓ →), green/red/neutral
- Time-horizon labels (TODAY / NOW / THIS WEEK) in footer

Data table (list pages):
- Summary strip: 4 inline stats with bold numbers + muted labels
- Filter bar: time-tabs + source/industry/status dropdowns + search
- Rows hover highlight, full row clickable
- Source tags (colored dot + text), industry chips (purple-on-purple), status badges (pill, semantic colors)
- Tabular-nums + right-aligned for numeric columns
- External-link arrow (↗) in final column, accent-blue on hover

## Page-level scope

### 1. Dashboard (landing) — FULLY SCOPED

**6 tiles, 1:1 mapped to sub-pages, trend arrows, time-horizon labels. M&A tile stacked with 4 metrics inside.**

| Tile | Primary metric | Horizon | Notes |
|------|----------------|---------|-------|
| Deal Aggregator | # new leads today | TODAY | with trend vs yesterday |
| Deal Pipeline | # active deals | NOW | point-in-time |
| C-Suite & Skills | x/x fired on schedule | TODAY | + green/yellow/red status dot |
| Infrastructure | x/x systems healthy | NOW | + status dot |
| M&A Activity | Owner convos / NDAs signed / Financials received / LOIs submitted | THIS WEEK | stacked 4-metric layout |
| Tech Stack | x/x in range | NOW | + status dot ("connected, credits healthy") |

Click any tile → navigate to that section.

### 2. Deal Aggregator — FULLY SCOPED

Data table. Columns:
1. Source (colored dot + name — Axial green / BizBuySell blue / Email yellow / Association purple / DealsX red)
2. Company (bold) + Industry chip (small purple chip below)
3. Owner (person name)
4. Location (city, state)
5. Revenue (right-aligned, tabular)
6. EBITDA (right-aligned, tabular, `—` if undisclosed)
7. Asking (right-aligned, tabular, `—` if undisclosed)
8. Status badge (New / Reviewed / Pursuing / Passed)
9. External-link arrow to CIM or listing

Summary strip: "X new today / X this week / X pursuing / X awaiting CIM"

Filters: Today / This week / All time-tabs + Source / Industry / Status dropdowns + search.

Data source: deal-aggregator skill daily output + broker platform scrapes + email inbound classification.

### 3. Deal Pipeline — PURPOSE LOCKED + RESCOPED 2026-04-24

**Active conversations only — NDA forward.** Reference mockup: `dashboard/mockup-deal-pipeline.html`.

**Scope shift (2026-04-24 PM):** Page was originally specced as full Attio pipeline replica (6 stages: Identified → Signed LOI). Rescoped during Session 4 design review because DealsX-driven cold outreach will push the Identified + Contacted counts into the thousands, making a Kanban view of those columns visually useless and turning the page into an outbound funnel report instead of an active-conversations tracker.

**4-column Kanban** (NDA → Financials Received → Submitted LOI → Signed LOI) + closed strip below filtered to **post-NDA failures only**. Identified + Contacted counts no longer live on this page; they aggregate to M&A Analytics as outbound funnel stats (DealsX contacted / Kay contacted / JJ called / reply rate / advanced-to-NDA conversion). Closed-lifetime number on this page also drops from 131 (all Attio closures, includes cold-outreach attrition) to ~12 (post-NDA failures only) — far more meaningful read of "deals we lost after real engagement."

**Card visual** (validated in mockup):
- Company name (bold), color-coded category chip (insurance=blue, fine-art=purple, shipping=yellow, consulting=green)
- Meta line: location · employees · ARR
- Footer: stage-age dot (green <14d / yellow 14-30d / red >30d) + last-touch days
- External-link arrow top-right; whole card clickable to Attio record

**Column header visual:**
- Pober-style 10.5px uppercase muted label
- Status dot (green if has deals + healthy ages, grey if empty)
- Count pill
- Thin proportion bar showing % of pipeline at that stage

**Data implications:**
- Attio data unchanged — still has all 6 stages. UI filter handles NDA-forward scope. Reversible.
- The existing `pages/deal_pipeline.py` ships in Session 3 needs an update to filter stages and add the visual upgrades (category chips, age dots, proportion bars). Tracked as a small Session 4 / Session 5 follow-on.

Data source: Attio MCP via `brain/context/attio-pipeline-snapshot.json`, filtered to NDA-forward stages at render time.

### 4. C-Suite & Skills — PURPOSE LOCKED, detail at build time

Hierarchical: 6 C-suite agents (CFO / CIO / CMO / CPO / GC / COO) as top-level rows, skills nested beneath each. Primary signal per skill: fire/no-fire today. Visual: status dot (green fired / yellow fired-with-warning / red didn't-fire-but-should've / grey not-scheduled-today). Click skill → expand last 5 runs + log output.

Data source: `logs/scheduled/*.log` + `launchctl list` + cross-reference against CLAUDE.md Scheduled Skills table per `feedback_staleness_check_schedule_first.md`.

### 5. Infrastructure — PURPOSE LOCKED + DETAILED 2026-04-24

**Five zones** (Tech Stack merged in 2026-04-24 PM during Session 4 design review). Reference mockup: `dashboard/mockup-infrastructure.html`.

1. **System Health** — local environment integrity. Tile grid (4×2): launchd jobs registered (count vs spec), spec-vs-registered diff, logs writing, hooks firing, disk space, vault schema validation, background commits, briefing pipeline timing. Each tile has status dot + headline value + detail line.

2. **External Connectivity & Tooling** — auth, API keys, MCP servers, local tools — one unified row list. Status is the headline ("API key expires in 7 days", "Index 3 days stale", "Healthy · 87 credits remaining"); action chip is one click ("Regenerate", "Refresh", "Logs"). Each row has kind tag (`service` vs `local`). Covers: claude-api, superhuman, attio-mcp, apollo, gog, granola, slack-webhooks, github, motion, linkt + local tools obsidian-vault-ops, agent-chatroom, cass. Replaces the old Infrastructure-Zone-2-tools-only AND old Tech-Stack-Section-1-services-only — they were the same kind of canary with different scope.

3. **Credits & Subscription Spend** — 6-tile grid for operational runway. Apollo credits + days-at-burn, Linkt credits + sunset date, Claude API monthly spend vs budget, total subscription cost + variance vs prior, individual high-stakes line items (Motion renewal, Superhuman). Frame is operational-runway ("when will this break ops"), NOT P&L (per `feedback_budget_not_kays_job.md` — Anthony handles P&L).

4. **Calibration & Learning · This Week** — what calibration-workflow codified/retired/refreshed since last Friday. Entry format: icon + headline + detail-with-code-references + timestamp. Examples: "Rule graduated to stop hook", "Memory files consolidated 3→1", "Skill SKILL.md files refreshed", "Stale memory deleted".

5. **Tech Stack · Full Inventory** — canonical reference list of every service in active use, organized by function (AI & Compute / CRM & Pipeline / Email / Calendar / Storage & Docs / Notes & Knowledge / Task Management / Discovery & Outreach / Communication / Development / Utilities). Chips with status dot + service name + note ("via gog", "sunset 2026-05-30", "retired"). This is the answer to "what tools do we actually use?" — distinct from Zone 2 which is "is each one healthy *now*?"

Data source: health-monitor + calibration-workflow + per-service auth/billing probes + a manually-curated stack inventory file (likely `dashboard/data/tech_stack.yaml`).

**Redundancy note (2026-04-24):** the original "Digest feed — one-line entries per per-skill activity" zone was dropped during Session 4 design review. Per-skill output already lives on (a) C-Suite & Skills page (click skill → expand last 5 runs + log snippets), (b) the destination page for the actual data (Deal Aggregator for surfaced deals, Pipeline for stage moves), and (c) Dashboard landing tiles for top-line counts. A "Today's runs" filter tab on the C-Suite page is the replacement if Kay wants chronological view across skills.

### 6. M&A Analytics — PURPOSE LOCKED, detail at build time

View toggle: Daily / Weekly / Quarterly / LTD. Core metrics per view:
- Owner conversations
- NDAs signed
- Financials received
- LOIs submitted
- Emails sent (Kay + JJ + DealsX split)
- JJ dials / meetings booked
- Conferences attended
- Active-outreach niches count

Trend lines on longer horizons. This page is the Weekly Activity Tracker replacement — ensure it covers what the Sheet does before retiring the Sheet (per `feedback_build_new_before_sunset_old`).

Data source: same as weekly-tracker skill (Gmail, Calendar, Attio, vault).

### 7. ~~Tech Stack~~ — RETIRED 2026-04-24

Merged into Infrastructure (Section 5) on 2026-04-24 PM during Session 4 design review. All three former Tech Stack sections now live as Zones 2 / 3 / 5 of Infrastructure. Sidebar entry removed; landing tile removed (was 6 tiles, now 5).

## Global behaviors (LOCKED)

- **Desktop-only V1** (phone view if/when needed, not now)
- **60s polling refresh** — set as a constant in code so it can flip to 120s or 300s in one line if it ever feels heavy
- **Briefing stays in terminal** — the dashboard is supplementary, not a briefing replacement
- **Tool:** Streamlit (open-source Python, `pip install streamlit`, `streamlit run dashboard/command_center.py`, serves at `localhost:8501`)
- **Code lives in this repo** at `dashboard/` alongside skills

## Operating principles (reference memories)

When building any page, remember:
- **`feedback_silent_failures_are_the_core_concern.md`** — always ask "what fails silently here?" first; that's the load-bearing signal.
- **`feedback_dashboard_scope_not_reminders.md`** — don't add reminder/nag features; Kay has existing surfaces for drafts, nurtures, etc.
- **`feedback_dashboard_visual_language_locked.md`** — match the mockup palette and type scale exactly.
- **`feedback_build_new_before_sunset_old.md`** — don't retire any existing surface (Weekly Activity Tracker especially) until the dashboard's replacement is verified live.
- **`feedback_budget_not_kays_job.md`** — runway isn't on the landing; Anthony handles P&L. But subscription-creep and connectivity alerts ARE Kay's concern (blocks her ops).
- **`feedback_people_not_companies.md`** — always show owner names, not just company names, in table rows.

## Build plan — 6 sessions

| # | Session | Est. time | Output |
|---|---------|-----------|--------|
| 1 | App shell + nav + Dashboard landing | ~1.5 hr | Running Streamlit app with nav + landing page live, reading fake or partial live data |
| 2 | Deal Aggregator page | ~1.5 hr | Page reads live deal-aggregator output |
| 3 | Deal Pipeline page | ~2 hr | Attio MCP integration, stage replica |
| 4 | C-Suite & Skills page | ~1.5 hr | Fire/no-fire canary wired to launchd logs |
| 5 | Infrastructure page | ~1.5 hr | Health-monitor + calibration + digest feed |
| 6 | M&A Analytics + Tech Stack | ~2 hr | Final two pages (Tech Stack canary + M&A views) |

**Total: ~10 hours across 6 sessions over 1-2 weeks.** Pace one page per session to stay inside Claude Code session windows comfortably.

**Hard rule:** one page per session. Don't marathon all 6 — burns token budget and leaves no headroom for other work.

## Session 1 kickoff — what to do first

When starting Session 1:
1. Verify `git status` clean (or any uncommitted work is intentional).
2. Read `memory/feedback_dashboard_visual_language_locked.md` and both mockup files to prime visual memory.
3. `pip install streamlit` if not already installed. Also: `pandas` (for table data), `pyyaml` (for reading vault frontmatter).
4. Create `dashboard/command_center.py` as the entrypoint. Create `dashboard/pages/` for future sub-pages (Streamlit multipage pattern).
5. Build the app shell:
   - Custom CSS injected via `st.markdown(..., unsafe_allow_html=True)` to match the locked palette (copy values directly from `mockup-landing.html`'s `:root` vars)
   - Sidebar nav with 7 items (Dashboard active)
   - Topbar with date + last-updated timestamp
6. Build the Dashboard landing page's 6 tiles. **For Session 1, wire with partial live data or placeholders**; the point is shell + layout + visual fidelity, not 100% live integration. Priority: match mockup visually.
7. Add `.claude/commands/dashboard.md` so Kay can launch with `/dashboard` — command runs `streamlit run dashboard/command_center.py`.
8. Verify: launch, confirm it renders in browser on `localhost:8501`, check against mockup side-by-side.
9. Commit. Write session-decisions entry. End session.

## Open decisions — scoped at build time per page

None at the IA or visual-language level. Remaining scope decisions are page-internal details that are cheaper to resolve with a real rendering in front of Kay than to pre-scope abstractly:
- Deal Pipeline: Kanban columns vs. table-with-stage-filter?
- M&A Analytics: chart library choice (Streamlit native vs. Plotly)?
- Tech Stack: trend chart granularity (daily, weekly, both)?
- Infrastructure: digest-feed density (how many items per day shown)?

These surface naturally during the respective page's build session. Do not pre-answer.

## Parallel / non-build work this weekend

- The main session's **briefing format flip** (4-bucket → Decisions-only) remains **blocked** on dashboard being live per `feedback_build_new_before_sunset_old`. Do NOT flip format until at least Session 1 ships.
- Weekly Activity Tracker Google Sheet continues to populate every Friday per existing weekly-tracker skill until M&A Analytics page (Session 6) is verified live.
- No other scheduled skills affected by dashboard build.

## For the next session

Start with the Session 1 kickoff checklist above. You have everything needed. Don't re-scope — the scope is locked. If something feels ambiguous, check the mockup files first; if still ambiguous, add to an "open question" list and keep building — don't stall.
