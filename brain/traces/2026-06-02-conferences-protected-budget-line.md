---
schema_version: 1.1.0
date: 2026-06-02
type: trace
task: Set conference budget line in runway plan
had_human_override: true
importance: high
target: skill:budget-manager
tags: [date/2026-06-02, trace, topic/budget-runway, topic/conference-attendance, pattern/protect-highest-roi-channel, status/done]
---

# Decision Trace: Conferences Are a Protected Budget Line, Not Discretionary Fat

## Context
While trimming discretionary spend to extend runway, the model initially folded conference/travel cost into a generic "discretionary" bucket subject to a ~$1,000/mo trim. Kay challenged this ("what are you budgeting for conferences?") — conferences are G&B's #1 ROI channel (direct owner/intermediary contact).

## Decisions

### Treatment of conference spend in the runway model
**AI proposed:** A blanket ~$1,000/mo discretionary trim that implicitly cut into the travel/conference line.
**Chosen:** Carve out **Conferences & Networking as a PROTECTED ~$700/mo line.** Discretionary trim (~$600/mo) comes only from coffee + rideshare, never conferences. Big registrations (>$300) and out-of-region trips are discrete, pre-approved one-offs OUTSIDE the $700 baseline.
**Reasoning:** Local cadence is cheap/free (most events $0–90), so $700/mo comfortably covers 1–3 local events/week. The budget only breaks on big-ticket registrations (InsurTech $1,695) or out-of-region travel (Boston, Charlotte) — which should be deliberate decisions, not baseline. Starving the highest-ROI sourcing channel to save runway is self-defeating.
**Pattern:** #pattern/protect-highest-roi-channel

## Learnings
- When trimming budget for runway, **never trim the conference line** — protect it explicitly. Trim coffee/rides/meals instead.
- Cost driver for conferences is LOCAL vs OUT-OF-REGION, not frequency. Local cadence ≈ $140–300/mo actual; the spikes are travel + premium registrations.
- Validated against the back-filled 28-event attendance record (Feb-2025 → May-2026): actual cadence ~0.6/week, mostly local/cheap, with cost concentrated in a few out-of-region trips.
