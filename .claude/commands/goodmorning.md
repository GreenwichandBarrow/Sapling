---
description: Morning orchestration — email-intel, relationship-manager, pipeline-manager, target-discovery, Decisions-only briefing (migrated from 4-bucket 2026-04-25 once Command Center dashboard went live)
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
- **Filter by Outreach Channel FIRST.** target-discovery only fills target sheets for `Kay Email` and `JJ-Call-Only` channels. **`DealsX Email` niches are SKIPPED unconditionally** — Sam's team at DealsX manages the contact universe externally; the local target sheet for a DealsX niche is *expected* to remain empty and an empty sheet is NOT a refill signal. Never surface a DealsX niche as "needs target-discovery."
- For Kay Email + JJ-Call-Only niches only: check target sheet fill rate
- If new activation with no target sheet OR weekly dashboard flagged refill needed → run target-discovery
- Skip niches with adequate pipeline

### Step 5 — JJ-operations

JJ-operations runs independently via launchd (8am) and posts to Slack at 10am. Do NOT re-run during /goodmorning — it has its own schedule. Verify it fired by checking `logs/scheduled/jj-operations-{date}.log` and flag if missing.

### Step 6 — Day-of-week overlays

- **Sunday:** + `task-tracker-manager report` (full health: overdue, carryover from prior week's incomplete priority slots, empty slot count for new week, stale Long Term items, stale Gantt-project ticks). Surface as a **Weekly Planning Review** section in the briefing — Kay walks through each carryover item: keep / promote to a day this week / move to Long Term / drop. Approved promotions fire `task-tracker-manager promote` inline. This is the canonical Sunday-morning weekly-planning ceremony (no separate systemd timer — `/goodmorning` itself is the trigger).
- **Monday:** + conference-discovery status check
- **Wednesday:** + niche-intelligence sprint status
- **Friday:** + weekly-tracker + health-monitor + calibration-workflow (parallel, results needed by 10am ET)

### Step 7 — Judge + present briefing (Decisions-only)

Migrated 2026-04-25 from the prior 4-bucket format. The Command Center
dashboard now holds the displaced context (Infrastructure + C-Suite & Skills
pages = system status; Active Deal Pipeline + M&A Analytics pages = pipeline
state + activity rollups). Briefing shrinks to a single ordered list of
decisions. See CLAUDE.md "Morning Workflow" Step 9 for the full format spec.

Read all outputs. Apply chief-of-staff judgment. Present a **single Decisions
list** per `feedback_decision_fatigue_minimization`. ≤5 items. Numbering
ascends across the list — never resets.

**Per-item format (Obama framing):**
```
N. {urgency-emoji} [{C-suite}] **RECOMMEND: {action}** — {one-sentence reason}
   → YES / NO / DISCUSS
```

**Urgency tags** (replace prior buckets):
- 🔴 Today / ASAP — active-deal fast-path, time-sensitive sends, soft-nudges
- 🟡 This week — bounded but not urgent
- 🟢 Dropped balls / nurture — recovery items (still surface — they cost deals)

Sort 🔴 → 🟡 → 🟢. Cluster by entity (collapse to one item per person/deal/niche).
C-suite labels per `feedback_c_suite_naming`.

**Header line above the list:** one sentence pointing at the dashboard, e.g.
*"5 decisions ordered by urgency. System status + pipeline + outreach metrics
live at agent-vps-7731c88b.tail868ef9.ts.net."*

**Briefing hygiene (unchanged):**
- Only surface items that need action or decision. Omit anything done/resolved.
- Never report back things Kay did herself.
- Noise gets archived silently — never a "noise" section.

**Brief-decisions pre-flight (mandatory invariant — added 2026-04-21 after
Guillermo miss):** Before delivering, enumerate tomorrow's external meetings.
Each unconfirmed/non-skipped meeting MUST appear as a 🔴 item:
**RECOMMEND: Generate brief for {name} ({time} {date})** → YES/NO/DISCUSS.
HOLD-prefixed events with 0 non-Kay attendees = unconfirmed; surface only
if Kay needs a soft-nudge decision.

**Broken-system escalation:** If a scheduled skill failed or a snapshot job
is stuck, surface as a 🔴 Decision: **RECOMMEND: Investigate {job}** →
YES/NO. Don't bury silent failures.

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
- **If a scheduled skill failed overnight**, surface it in System Status with 1 line. Don't escalate unless blocking. (Post-dashboard-launch: this routes to the dashboard's System Map pane instead.)
- **Active deals (CIM, NDA, LOI, financials) get same-day treatment**, not next-morning briefing delay per `feedback_active_deal_urgency`.
- **Every briefing item has an explicit question or action.** No ambiguous items per `feedback_morning_briefing_format`.

## Variables

- `{date}` = today's date (YYYY-MM-DD)
- `{previous-workday}` = last weekday before today (skip weekends/holidays)
