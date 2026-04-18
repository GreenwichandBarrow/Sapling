---
description: Morning orchestration — email-intel, relationship-manager, pipeline-manager, target-discovery, 6-section briefing
---

# /goodmorning

Morning bookend to `/goodnight`. Kay says "good morning claude" or invokes `/goodmorning` → full morning workflow per CLAUDE.md executes in one call.

## Execute Now

### Step 1 — Run signal-gathering skills in parallel

Spawn in a single message:

- **email-intelligence** → writes `brain/context/email-scan-results-{date}.md` (Gmail, Superhuman, Granola scanning)
- **relationship-manager** → writes `brain/context/relationship-status-{date}.md` (nurture cadences, overdue contacts)

### Step 2 — Cross-reference previous session-decisions

Read `brain/context/session-decisions-{previous-workday}.md`:
- Suppress any items already decided yesterday (don't re-surface)
- Honor deferrals until their trigger date
- Surface verification requests for decisions that lacked confirmed actions

### Step 3 — Run pipeline-manager

Invoke pipeline-manager skill. It reads:
- `email-scan-results-{date}.md`
- `relationship-status-{date}.md`
- `session-decisions-{previous-workday}.md`
- Calendar, vault, Attio

Pipeline-manager assembles the raw briefing payload.

### Step 4 — Active-Outreach niche check

For each niche with status `Active-Outreach` on the Industry Research Tracker:
- Check target sheet fill rate
- If new activation with no target sheet OR weekly dashboard flagged refill needed → run target-discovery
- Skip niches with adequate pipeline

### Step 5 — JJ-operations

JJ-operations runs independently via launchd (8am) and posts to Slack at 10am. Do NOT re-run during /goodmorning — it has its own schedule. Verify it fired by checking `logs/scheduled/jj-operations-{date}.log` and flag if missing.

### Step 6 — Day-of-week overlays

- **Monday:** + conference-discovery status check
- **Wednesday:** + niche-intelligence sprint status
- **Friday:** + weekly-tracker + health-monitor + calibration-workflow (parallel, results needed by 10am ET)

### Step 7 — Judge + present briefing

Read all outputs. Apply chief-of-staff judgment. Present the 6-section briefing with **ascending numbering across all sections** (never reset to 1):

1. **Pipeline shifts to review/approve** — stage changes, new deals, Active-Outreach transitions
2. **Pipeline summary** (numbered, open items only, never reports Kay's own completed work)
3. **Action items to review/approve** — Motion task candidates, email drafts
4. **Carried items** — needs Kay's direction
5. **System Status** — 1 bullet per scheduled skill, no detail unless broken/blocked
6. **Other items / today's agenda** — calendar, meeting prep

### Step 8 — Downstream skill invocations based on signals

- Niche flipped to Active-Outreach → target-discovery + list-builder + outreach-manager
- CIM received → deal-evaluation (email-intelligence auto-triggers)
- Target approved on sheet (Col O = "Approve") → outreach-manager + JJ call log
- Monday → conference pipeline review
- If no signals warrant action → skip

## Behaviors

- **Numbering is additive across the conversation**, never reset. Kay replies by number.
- **Suppress completed items.** Only surface open/pending. Never report back Kay's own work.
- **Don't announce that pipeline-manager or email-intelligence "hasn't run yet"** — just run them silently per `feedback_pipeline_manager_no_alarm`.
- **If a scheduled skill failed overnight**, surface it in System Status with 1 line. Don't escalate unless blocking.
- **Active deals (CIM, NDA, LOI, financials) get same-day treatment**, not next-morning briefing delay per `feedback_active_deal_urgency`.
- **Every briefing item has an explicit question or action.** No ambiguous items per `feedback_morning_briefing_format`.

## Variables

- `{date}` = today's date (YYYY-MM-DD)
- `{previous-workday}` = last weekday before today (skip weekends/holidays)
