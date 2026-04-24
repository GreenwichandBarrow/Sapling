---
date: 2026-04-24
type: context
title: "Continuation — G&B Command Center Dashboard Build Session"
tags:
  - date/2026-04-24
  - context
  - topic/dashboard
  - topic/command-center
  - topic/continuation
  - topic/streamlit
---

# Continuation — Dashboard Build Session (2026-04-24)

## Purpose

Start a fresh Claude session focused exclusively on building the G&B Command Center dashboard. This file primes the session with all design decisions already locked from today's main session, plus the open scoping questions Kay was about to answer before plan mode.

## Why urgent

Today's main session edited CLAUDE.md, goodmorning.md, and pipeline-manager/SKILL.md to migrate the morning briefing from 4-bucket + System Status → Decisions-only. Kay flagged the sequencing error ("build new before sunset old") and I rolled back the format changes, but the dashboard is now the gating artifact for the briefing-format flip. Until the dashboard is live, the 4-bucket briefing stays. See `memory/feedback_build_new_before_sunset_old.md`.

**Target:** V1 Live Activity Feed pane running on localhost by Monday morning so the briefing migration can follow.

## Design decisions already locked

### 4-pane layout (from 2026-04-15 Pober reference doc)

See `brain/context/pober-acquisitions-platform-reference-2026-04-15.md` for full detail. Screenshots at `brain/reference/pober-acquisitions-screenshots-2026-04-15/`.

```
┌────────────────────────────────────────────────┐
│ TOP: Live Activity Feed (last 20 events)       │
├────────────────────┬───────────────────────────┤
│ Agent Metrics      │ System Map                │
│ (6 C-suite agents) │ (skills under each agent) │
├────────────────────┴───────────────────────────┤
│ FOOTER: Domain Health Monitor                  │
└────────────────────────────────────────────────┘
```

### Tool decision: Streamlit

- Open-source Python library, free, runs locally
- Installed with `pip install streamlit`, launched with `streamlit run dashboard.py`, opens at `localhost:8501`
- No signup required for local use
- Reads directly from vault files + sheets (no API shim layer needed)
- Dashboard code lives in this repo alongside skills — compounds with everything else

Rejected alternatives:
- **Retool** — SaaS, $10–15/mo, would need HTTP shim for hook-state JSON files
- **Looker Studio** — snapshot tool, doesn't handle live feed well
- **Metabase / Notion** — overkill / wrong shape

### Pane 1 (Live Activity Feed) — event types + sources

| Icon | Event | Data source |
|------|-------|-------------|
| 📧 | CIM received | email-scan-results-*.md |
| ✉️ | Email sent | session-decisions SENT verb-tag |
| ✅ | Draft approved | trace with /cmo APPROVE |
| ❌ | Target killed | trace with /cio KILL |
| ⚖️ | C-suite verdict | traces |
| 📅 | Meeting booked | session-decisions / calendar |
| 📝 | NDA executed | session-decisions CREATED |
| 🧠 | Trace captured | brain/traces/*.md |
| 🤖 | Skill run | logs/scheduled/*.log |
| 🔴 | Blocker flagged | health-monitor output |

Per-row fields: relative timestamp ("2 min ago"), icon, one-line description, clickable source-file link.
Filter controls: event-type multi-select dropdown + free-text search.

### Pane 2 (Agent Metrics) — 6 C-suite agents

Columns: Agent / Status / Invocations (today/week/month) / Verdict split / Kay override rate / Avg latency / Last invoked (link).
Data source: `brain/traces/` filtered by `role/*` tag; calibration-workflow pre-aggregates weekly.
Interaction: click agent row → expand 5 most-recent invocations.

### Pane 3 (System Map) — tree of skills under each C-suite agent

Hierarchy: 6 C-suite agents as top nodes, skills nested. Per-skill row: indicator dot (🟢🟡🔴⚪), last run time, one-line health note.
Data source: `logs/scheduled/*.log`, `launchctl list`, `.claude/skills/` enumeration.

### Pane 4 (Domain Health) — footer

1-line summary by default, expand for detail.
Fields: domain / warmup status / inbox rate / emails sent today / bounces / spam complaints.
Data source: NEW collector needed — domain health doesn't exist yet. **Defer to V2** per today's scoping recommendation; V1 shows "coming soon" placeholder.

## Open scoping questions Kay hasn't answered yet

Six items from today's scope discussion, my recommendations in bold:

1. **Weekly Activity Tracker integration.** → **(a) Keep separate** — dashboard = live ops, Sheet = Friday advisor review (different audiences, different cadences).
2. **Desktop or mobile.** → **Desktop-only V1**, phone view later.
3. **Refresh cadence.** → **Poll every 60s** for V1 (simplest, feels live enough).
4. **Default time window.** → **Feed = "today only" with scroll-back button, Agent panel = "this week"**.
5. **Lead Score / Intent Signal placement.** → **Stays on target sheets, not the Command Center itself** — confirms 4/15 design doc.
6. **Domain Health timing.** → **Defer to V2**, V1 shows three panes with data today + placeholder for Pane 4.

## V1 build scope (smallest viable slice)

**V1 = skeleton + Live Activity Feed pane only.** One Python file reads session-decisions + traces + today's email-scan + relationship-status artifacts, extracts verb-tagged events, renders as chronological feed. No Agent Metrics, no System Map, no Domain Health in V1. Shape the skeleton so V2/V3 can add panes without refactoring.

**Estimated build time:** 30 min once scope is locked.

**Dependencies:**
- Python 3.14 (already installed per this session's test runs)
- `pip install streamlit` (no sign-up required)
- Read access to `brain/context/*.md`, `brain/traces/**/*.md`, `logs/scheduled/*.log`

## What the new session should do, in order

1. **Confirm scope.** Answer the 6 open questions above (Kay's call on each).
2. **Enter plan mode.** Draft a V1 build plan in plan mode. Show Kay for review.
3. **Exit plan mode and execute.** Install streamlit, create `dashboard/command_center.py`, build skeleton + Live Activity Feed pane.
4. **Verify running.** Launch `streamlit run dashboard/command_center.py` on port 8501. Kay opens in browser, confirms it renders live data.
5. **Document.** Add `.claude/commands/dashboard.md` or similar so Kay can launch it with a slash command.
6. **Signal completion.** Once V1 is running, flag to main-session Claude that briefing-format migration can now happen (the trigger to flip pipeline-manager/SKILL.md from 4-bucket to Decisions-only).

## State of the main session when this file was written

- 3 new stop hooks live (column-letters, Sunday-send, revenue-in-outreach, Kay-in-deliverables — plus the 4/24 column-letters one already shipped)
- 4 new memories saved (fix-skills-inline-by-default, build-new-before-sunset-old, jj-call-date-from-field-not-tab, vault-schema-inline-array-tags, onepager-must-cite-sources)
- CLAUDE.md updates: Friday sheet-populate commitment, meta-calibration section, LET'S DISCUSS wording, dashboard-migration-pending note
- Briefing format ROLLED BACK to 4-bucket (dashboard is blocker for format flip)
- Weekly tracker corrected: ~49 JJ dials this week (17 Mon, 23 Tue, 9 Fri-today) vs original "0 all week" miscount
- 4/23 Granola transcripts landed + 5 entity stubs created (Kristin Wihera, Axial, Wiggin and Dana, Saunders Street, Andrew Lowis)
- 4/24 session-decisions bookend anomaly quarantined
- Jim Vigna reply drafted and in Superhuman (`draft00c0d2b60c8e457c`)

## For Kay

**To start the dashboard session:** open a new terminal tab, cd to this project, run `claude`, and paste something like:

> *Let's build the V1 Command Center dashboard. Full context at `brain/context/continuation-2026-04-24-dashboard-build.md` — please read that first, then walk me through the 6 open scoping questions.*

**Parallel email-drafts session:** open a second terminal/tab for the email work — no context collision since the sessions are independent.
