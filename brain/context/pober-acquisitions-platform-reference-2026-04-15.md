---
date: 2026-04-15
type: context
title: "Pober / Acquisitions.com platform reference — 4 ideas to lift for G&B Command Center"
tags:
  - date/2026-04-15
  - context
  - topic/pober
  - topic/command-center
  - topic/dashboard
  - topic/agent-architecture
---

# Pober / Acquisitions.com Platform Reference

## Context
Kay reviewed 12 screenshots of Moran Pober's Acquisitions.com platform on 2026-04-15. Goal: mine architecture ideas (not volume cold-email model) for the G&B Command Center build (pin #2 from 2026-04-14 evening).

**Screenshots archived at:** `brain/reference/pober-acquisitions-screenshots-2026-04-15/` (12 PNGs, Apr 15 2026 1:41-1:42pm)

**Kay's verdict:** Pober's dashboard is impressive but overkill. Build a simple version lifting the 4 ideas below.

## Not adopting
- Volume cold-email model (16,912 emails, 0.87% reply rate, 31 meetings) — opposite of Kay's 5/day thoughtful approach
- Sell-side / buyer-outreach workflow (PE + Strategics outreach for flips) — G&B is buy-side only
- 6 execution agents (Email Copywriter, Appointment Setter, Lead Researcher, Buyer Matcher, Quality Checker, Copy Optimizer) — G&B's existing skills already cover these functions; G&B's 6 C-suite agents are a **judgment** layer, not execution

## The 4 ideas to lift

### 1. Live Activity Feed (center of Command Center)
Real-time, scrollable, one-line event stream. Pober's feed shows: "Meeting Booked — Robert Chen / Reply — Maria Gonzalez / NDA Signed — James Whitfield / Submitted LOI — Desert Valley Landscaping — $2.2M."

**G&B version:**
- `CIM received from [Intermediary] — [Company]`
- `Draft approved by /cmo — [Target]`
- `/cio killed target — [Company] (buy-box violation)`
- `Meeting booked — [Owner / Company]`
- `NDA executed — [Company]`
- `Frame learning trace captured — /cfo — [Topic]`

**Implementation target:** top pane of Command Center dashboard, auto-refreshing, last 20 events.

### 2. Lead Score + Intent Signal per target
Per-row display on Seller Leads table: numeric 0-100 bar (color-coded) + one-line narrative text describing what drove the score. Pober examples: "Owner mentioned retirement in podcast" / "Web traffic spike — hiring sales lead."

**G&B version:**
- Column on target-discovery output: `Intent Score` (0-100) + `Intent Signal` (one-line narrative)
- Score drivers: web signals (hiring, traffic, job postings), podcast/press mentions, LinkedIn activity (role changes, anniversary), broker listings, trade-publication mentions
- Narrative: quote or paraphrase the specific signal ("Owner interviewed on SMB podcast Mar 2026 discussing succession" / "Posted CFO opening Feb — possible prep for sale")
- Attaches to the **pin #3** build from 2026-04-14 (intent-to-sell score + pre-draft replies). This is literally the visible output of that pin.

**Implementation target:** new column on all niche target sheets; surfaced in Command Center per-target view.

### 3. Agent metrics panel
Pober displays 6 AI agents with: status (Running/Idle), tasks completed today, success rate %, avg response time. Example row: "Email Copywriter / Running / 2,498 tasks / 98.4% / 6s."

**G&B version:** same UI, different semantics — this is the calibration view for the 6 C-suite judgment agents.

| Agent | Status | Invocations Today | Verdict Rate (APPROVE/PASS/KILL split) | Reversal Rate (Kay overrides) | Avg Latency |
|---|---|---|---|---|---|
| /cfo | Running | 3 | 2 PENCILS, 1 MARGINAL | 0/3 | 8s |
| /cio | Running | 12 | 5 APPROVE, 4 TABLE, 3 KILL | 1/12 | 6s |
| /cmo | Running | 8 | 7 APPROVE, 1 REWRITE | 0/8 | 4s |
| /cpo | Running | 2 | 2 NUDGE | 0/2 | 3s |
| /gc | Running | 1 | 1 APPROVE | 0/1 | 11s |

**Feeds:** calibration-workflow scans `brain/traces/` weekly, aggregates by `role/*` tag, writes to the dashboard. Friday review reads this panel.

**Implementation target:** bottom-left pane of Command Center.

### 4. Domain Health Monitor
Per-domain warmup status, inbox rate, spam rate, emails sent today. Pober has 22 domains across 312 accounts at 97.2% inbox rate. Row-by-row breakdown: domain name / accounts / warmup status / inbox rate / spam rate / emails today / spam complaints.

**G&B version:** applies to G&B sending domains (kay.s@greenwichandbarrow.com + any DealsX-managed domains). Critical given the Salesforge incident (2026-04-05) and the hard rule against third-party SMTP.

- Domain warmup status
- Inbox placement rate (vs. spam)
- Emails sent today
- Bounces today (damages sender reputation)
- Spam complaints

**Implementation target:** `health-monitor` skill gets a new sub-agent. Results surfaced in System Status section of morning briefing (1 line: `Sender health — 98.1% inbox rate across 2 domains, 0 bounces today`) and expanded on Command Center dashboard.

## G&B Command Center — simple version (scope for pin #2 build)

Kay: "simple version would be good." Initial scope = 4 panes:

```
┌─────────────────────────────────────────────────────────┐
│ TOP PANE: Live Activity Feed (last 20 events)           │
├──────────────────────────────────┬──────────────────────┤
│ BOTTOM-LEFT:                     │ BOTTOM-RIGHT:        │
│ Agent metrics panel (C-suite)    │ System Map           │
│ — /cfo, /cio, /cmo, /cpo, /gc    │ (tree of skills      │
│ — invocations, reversals, latency│  under each agent)   │
├──────────────────────────────────┴──────────────────────┤
│ FOOTER: Domain Health Monitor (1 line summary + expand) │
└─────────────────────────────────────────────────────────┘
```

Intent Score + Intent Signal columns live on **target sheets**, not the Command Center itself (the dashboard would cite them when surfacing targets).

## Next step
Command Center build is a separate session. This reference note pre-loads the design decisions so the build starts with direction locked.
