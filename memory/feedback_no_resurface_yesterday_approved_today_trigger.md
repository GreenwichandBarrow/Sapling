---
name: Don't re-surface yesterday-APPROVE'd items with a today execution trigger
description: If Kay APPROVE'd an action yesterday with a today execution trigger (scheduled send, scheduled draft, defer-until-Monday-AM), don't re-surface it on today's Decision list unless there's positive evidence it failed. Partial visibility is not evidence.
type: feedback
---

If Kay APPROVE'd an action in yesterday's session-decisions with a today execution trigger ("send Mon AM ~9am", "draft for Mon AM"), **do not re-surface it on today's morning briefing Decision list** unless there is positive evidence the action did not happen.

**Why:** Items 2 and 3 on the 2026-05-11 morning briefing (Harrison Wells send, Lauren Young draft verify) were both Sunday-APPROVE'd with explicit Monday-AM triggers. I re-surfaced them as Decisions because (a) I didn't have live keyring auth in this session to probe Gmail outbound, and (b) Lauren's draft probe returned zero — but Lauren conversed with Kay via her personal email (invisible to gog) and Harrison sent on schedule. Both were already done. Pulling them onto the Decision list reverses the chief-of-staff job — Kay should not be answering for things she already arranged.

**How to apply:**

1. When assembling the morning Decisions list, scan yesterday's session-decisions for APPROVE'd items with today as the execution trigger. Default these to **in-flight, suppress** — they do not appear as Decisions.
2. To re-surface, you need **positive evidence the action failed**: a Gmail outbound probe that confirms no send to the recipient in the relevant window, a draft list that explicitly shows the named contact as missing, a Slack-failure alert, etc. Partial visibility (keyring not loaded, MCP not connected, personal-email channel) is **not** evidence — it's a blind spot. Blind spots default to trust-Kay, not pull-onto-her-queue.
3. The exception is when the action is irreversible-if-wrong AND time-bounded AND the visibility gap is closable. E.g., "verify the draft exists before Kay's 9am send window closes" is legitimate if it's 8:45am and the keyring is loadable. Past the window, default to suppress.
4. If you genuinely need to verify silently, do it in System Status footnotes or in a "Quiet checks" line, not in the numbered Decision list. The Decision list is for items that **require Kay's judgment today**.
5. Cross-reference: `feedback_briefing_no_done_items.md` (briefing = open items only), `feedback_silent_approval_assumption.md` (don't read silence as approval — symmetric: don't read silence as failure either), `feedback_scheduled_vs_todo_presentation.md` (scheduled = wired-up, not Kay-queue).

**Litmus test:** "If Kay reads this Decision item and her answer is 'I already did that yesterday' or 'already done via channel you can't see,' it should not have been on the list."
