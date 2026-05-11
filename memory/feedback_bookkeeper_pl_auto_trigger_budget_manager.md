---
name: Bookkeeper monthly P&L should auto-trigger budget-manager
description: When email-intelligence detects Anthony/StartVirtual P&L delivery, auto-fire budget-manager monthly mode — do not surface as a Decision item
type: feedback
originSessionId: bab08f3e-b893-4381-a68a-1043ae6a1a0b
---
When email-intelligence detects an inbound email from `anthony.b@startvirtual.com` (or any `*@startvirtual.com` sender) with subject/body containing "Management Report" / "Profit and Loss" / "Balance Sheet" or PDF attachments matching those patterns, **auto-fire budget-manager monthly mode**. Do NOT surface "RECOMMEND: Run budget-manager?" as a Decision item.

Surface the **output** of budget-manager (variance flags, runway change, action items) in the next briefing — those are decision-worthy. The trigger event itself is deterministic and burns Kay's decision budget for nothing.

**Why:** Per `feedback_decision_fatigue_minimization` and `feedback_remove_kay_from_loop`. Bookkeeper P&L delivery is a recurring scheduled input — not a judgment call. The decision Kay needs is what to do with the runway and variance numbers, not whether to recompute when fresh data arrives. Today (2026-04-29 Wed): I surfaced "RECOMMEND: Run budget-manager on March P&L" as item #3 of the morning briefing; Kay said "you saw the email so this should be the trigger" — meaning the email scan IS the trigger, the approval step was wasted.

**How to apply:**
- email-intelligence skill detects the bookkeeper P&L → tags inbox item with `urgency: trigger-budget-manager` (or similar)
- Morning workflow Step 4-equivalent: if any inbox item has that trigger, kick budget-manager monthly mode in parallel with pipeline-manager assembly
- Briefing surfaces budget-manager OUTPUT (e.g., "🟡 March runway dropped 0.4 mo vs Feb — review variance flags") instead of the trigger
- Same pattern applies to any future deterministic recurring trigger: niche-intelligence Tuesday newsletters, weekly-tracker Friday data pull, etc. — the trigger fires the skill, the briefing surfaces the output

**Pattern:** Trigger ≠ Decision. Output of trigger may or may not be a Decision. Only the latter belongs on Kay's list.
