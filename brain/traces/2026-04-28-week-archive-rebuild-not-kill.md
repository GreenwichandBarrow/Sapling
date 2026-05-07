---
schema_version: 1.1.0
date: 2026-04-28
type: trace
today: "[[notes/daily/2026-04-28]]"
task: Resolve Week Archive page quality complaint
had_human_override: true
importance: medium
target: process
tags: [date/2026-04-28, trace, topic/dashboard, topic/ui-architecture, pattern/check-load-bearing-before-killing]
---

# Decision Trace: Week Archive Rebuild, Not Kill

## Context

Kay flagged the dashboard's Week Archive page as "terrible" via screenshots showing wikilinks (`[[entities/matthew-luczyk]]`), implementation paths (`~/.local/bin/superhuman-draft.sh`), schema labels (`schema 1.0.0 — legacy weekly tracker`), and operator-narrative dumps ("Key Relationships Advanced", "Surprising Findings", "Blocker"). The page was rendering raw markdown from `brain/trackers/weekly/{date}-weekly-tracker.md` — my private notes leaking onto a CEO surface.

My initial diagnosis cleanly identified six failures and produced three resolution options:
- (a) Cosmetic pass — clean labels, kill legacy pill, color deltas (~30 min)
- (b) Visual rebuild — match locked visual language with charts/sparklines (~1-2 hr)
- (c) Sunset — kill the page entirely, rely on M&A Analytics

I leaned (c) — calling something "legacy" on a CEO surface is the bigger sin than the formatting. Then Kay corrected: *"Remember this is replacing... G&B Weekly Activity Tracker."*

That flipped the calculus entirely. Then she added a second clarification: *"Not meaning we are doing away with G&B Weekly Activity Tracker but the info will all be visible on the commend center, and then be captured in that file at the end of the week for archive purposes."*

## Decisions

### Rebuild not kill

**AI proposed:** Sunset the Week Archive page entirely. Numeric metrics fold into M&A Analytics; narrative content stays in `brain/notes/weekly/`.

**Chosen:** Full structural rebuild matching the Google Sheet's Weekly Topline + Weekly Detail tabs. 5-zone visual mirroring M&A Analytics, frozen for selected past weeks. Drop the markdown dump entirely.

**Reasoning:** The page wasn't a vestigial surface to retire — it was the *replacement* for a load-bearing manual artifact (the G&B Weekly Activity Tracker Google Sheet that Kay used to maintain by hand). The architecture Kay clarified: dashboard = live working surface, sheet = end-of-week archive captured FROM the dashboard. Killing the page would leave a gap in that pipeline. A rebuild was required, not optional.

**Pattern:** #pattern/check-load-bearing-before-killing

### Read source-of-truth before designing the rebuild

**AI proposed (initially):** Skip straight to writing the new page from M&A Analytics's visual patterns.

**Chosen:** Read the Google Sheet's actual structure first — Weekly Topline tab (5 KPIs × weekly columns × target column) + Weekly Detail tab (30+ metrics across 9 sections, with per-niche breakdown columns) — to understand what shape the dashboard page must produce.

**Reasoning:** Without the source-of-truth schema, the rebuild would have invented a structure that didn't match what would land in the sheet at end-of-week. The sheet IS the contract; the page must mirror it. ~5 min of `gog sheets get` calls saved hours of misalignment.

**Pattern:** #pattern/read-target-format-before-rendering

## Why This Trace Matters

When a CEO-facing surface is bad, "kill it" is the lowest-risk-looking option but the highest-risk-actually option if the surface is replacing a manual artifact in a workflow Kay relies on. Future agents seeing a similar complaint ("this dashboard page is terrible") should default-check what the page is REPLACING (manual sheet? prior tool? operator habit?) before recommending sunset.

The corollary: when a page IS being rebuilt, read the source artifact's actual schema first. The sheet's column structure is the de facto API contract; the page is the implementation. Don't invent a fresh visual schema and hope it converges later.

## Key Insight

Bad CEO surfaces have three failure modes:
1. **Vestigial** (kill it — no downstream consumer)
2. **Misdesigned but load-bearing** (rebuild it — workflow depends on it)
3. **Right design, wrong content** (fix the data layer — not the surface)

Defaulting to "kill" because the surface looks bad ignores categories 2 and 3. Always check the workflow it serves before choosing the resolution path.
