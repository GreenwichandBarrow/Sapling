---
name: Morning briefing is Decisions-only (post-dashboard, 2026-04-25)
description: Briefing format = single Decisions list ordered by urgency emoji (🔴/🟡/🟢). Replaces 4-bucket model. Cluster by entity. Obama framing.
type: feedback
originSessionId: 79f2536c-7455-4155-bafd-6653508b83e4
---

Morning briefing structure: **single Decisions list**, ordered by urgency,
≤5 items. Replaces the prior 4-bucket model (Today / Decisions / This Week
/ Dropped Balls + System Status footer).

**Why migrated 2026-04-25:** Command Center dashboard went live this session
(all 6 pages, real data, snapshot refreshes, staleness banner, README). The
4 buckets were doing two jobs — surface judgment calls AND show context
(pipeline state, system status, weekly activity). The dashboard now holds
the context layer (Infrastructure + C-Suite & Skills + Active Deal Pipeline
+ M&A Analytics pages). Briefing collapses to its actual job: surface
judgment calls. Per `feedback_decision_fatigue_minimization`, fewer items
to triage = sharper morning routine.

Per `feedback_build_new_before_sunset_old`, this migration was held until
the dashboard was verified operational. Original lock: Apr 17 webinar
(Harry Liu's Escalate/This Week/Noise/Dropped Balls model). Migration
trigger: Apr 25 dashboard launch.

**Format (Obama framing throughout):**
```
N. {urgency-emoji} [{C-suite}] **RECOMMEND: {action}** — {one-sentence reason}
   → YES / NO / DISCUSS
```

**Urgency tags** (replace prior buckets):
- 🔴 **Today / ASAP** — active-deal fast-path, time-sensitive sends, soft-nudges on next-day externals. Sort to top.
- 🟡 **This week** — bounded but not urgent. Sort middle.
- 🟢 **Dropped balls / nurture** — slipped follow-ups, overdue cadences, warm-intro replies (still surfaced — slipped follow-ups cost deals). Sort bottom.

**Header line above the list:** one sentence pointing at the dashboard,
e.g. *"5 decisions ordered by urgency. System status + pipeline + outreach
metrics live at localhost:8501."* Replaces the multi-line System Status
section.

**How to apply:**
- Cluster by entity — collapse to ONE item per person/deal/niche, never split
- Ascending numbering across the whole list (Kay replies by number)
- C-suite labels (CFO/CIO/CMO/CPO/GC) per `feedback_c_suite_naming`
- ≤5 items per `feedback_decision_fatigue_minimization`
- True noise gets archived silently (never a "noise" bucket)
- Briefing hygiene: only open items; never report back things Kay did

**Brief-decisions pre-flight (mandatory invariant):** Before delivering,
enumerate tomorrow's external meetings. Each unconfirmed/non-skipped meeting
MUST appear as a 🔴 item: **RECOMMEND: Generate brief for {name}** →
YES/NO/DISCUSS. HOLD-prefixed events with 0 non-Kay attendees = unconfirmed;
skip unless soft-nudge needed.

**Broken-system escalation:** If a scheduled skill failed or a snapshot job
is stuck, surface as 🔴 Decision: **RECOMMEND: Investigate {job}** → YES/NO.
Don't bury silent failures — the dashboard's stale-snapshot banner does
that already, but a broken job is decision-worthy.

**Source:** Original lock 2026-04-19 (4-bucket post-Harry-Liu webinar).
Migration to Decisions-only 2026-04-25 (post-dashboard-launch).
