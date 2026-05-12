---
name: off-system-resolution-closes-loop
description: When Kay declares she handled a contact off-system (personal email, text, phone, in-person), the loop is CLOSED — stop surfacing in relationship-manager/pipeline-manager regardless of Gmail silence
metadata:
  type: feedback
---

When Kay says "I already wrote back to X" or "I handled X via personal email / text / call" — that's the resolution. Stop surfacing the contact in subsequent briefings, relationship-status artifacts, or pipeline-manager open-loops, even if Gmail/calendar shows no in-system trace.

**Why:** 2026-05-12 morning — relationship-status artifact re-surfaced Lauren Young for the third consecutive day as "draft visibility unverified" because the 5/10 APPROVE was for a Monday-AM check-in draft and Gmail probes returned zero. Kay had actually written back from her personal email the same morning. The relationship-manager skill (correctly per its own rules) couldn't verify off-system action, but I (Chief of Staff) should have heard "I already shared that I wrote back to her on my personal email. you keep raising this" the first time and stopped surfacing. Persisting after Kay's verbal close is decision-fatigue noise.

**How to apply:**
- When Kay says "I already wrote / replied / called / texted X" in conversation, immediately:
  1. Record the off-system resolution in `brain/context/session-decisions-{date}.md` under Actions Taken as `SENT (off-system, {channel}): {contact} — {what was sent/said} per Kay verbal close at {time}`.
  2. Update the contact's `next_action` field in Attio to clear the pending action (mark complete with note "Resolved off-system per Kay 2026-MM-DD").
  3. Add a `do_not_resurface_until: {trigger}` or `last_interaction_override: {date}` annotation to the vault entity or relationship-manager exclusion list so future scans don't re-flag.
  4. Confirm to Kay: "Marked closed — {channel} resolution recorded." Don't ask for a forwarded trace unless Kay explicitly offers and you actually need it for downstream automation.
- If Kay offers to forward the off-system correspondence (e.g., from personal → work email for trace), ACCEPT the offer and treat the forwarded message as the canonical record once it lands. But don't condition the close on the forward — the verbal declaration is sufficient.
- This rule fires regardless of channel: personal email, text/SMS, phone, in-person, LinkedIn message, Signal, anywhere outside the scanned Gmail/calendar/Granola/Attio surfaces.
- Companion rule: `feedback_action_already_taken_verification` (in-system verification) and `feedback_no_resurface_yesterday_approved_today_trigger` (don't re-raise approved actions absent positive failure evidence). This rule extends both to cover the off-system case explicitly.

**Lauren Young precedent (2026-05-12):** Surfaced day 1 (5/10) as overdue → APPROVE'd Monday-AM draft. Surfaced day 2 (5/11) as draft visibility gap. Surfaced day 3 (5/12) again as carry-forward awareness. Kay's annoyed close: "I already shared that I wrote back to her on my personal email. you keep raising this." She is closed. Mark and move on. If she forwards the personal → work email, file the trace; if not, the verbal close still stands.
