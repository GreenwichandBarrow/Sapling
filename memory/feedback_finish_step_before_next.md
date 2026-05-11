---
name: Always finish a step thoroughly before moving to the next item
description: Complete each step fully — verify, double-check, confirm — before starting the next item or conversation topic. Do not defer corrections to "after the next thing." Do not jump ahead. Finishing one thing cleanly compounds; partial work across multiple threads creates loss and rework.
type: feedback
originSessionId: 848374e5-1268-4868-935b-ca7f12026b58
---
Always finish a step thoroughly before moving on. Do not:
- Defer corrections with phrases like "I'll fix this after the next step"
- Jump to a new conversation topic while prior work is in a dirty / unverified / pending state
- Write half-complete values into sheets/docs and plan to return later
- Start a calibration / architecture / strategy conversation while there are pending file changes from a prior request
- Assume I'll remember to come back — I often won't, or context will be lost, or a session-restart will drop unfinished threads

Instead:
- Finish the current edit fully, verify it landed, confirm it's correct
- Only THEN acknowledge or pivot to the next topic
- If a pivot is requested mid-stream, surface the incomplete work first: "I have X in a dirty state — finishing it now before we switch context"
- If a session might end mid-stream, prioritize finishing the current step over capturing new work

**Why:** 2026-04-21 — During the Deal Aggregator Sourcing List audit, I said "I'll hold on writing corrections to the sheet until after the calibration conversation." Kay: "Don't do that — fix the skills now. So if we need to start a new session nothing is lost." Kay followed with: "I always prefer you finish a step thoroughly before moving onto the next item — it helps us in the long run." The rule compounds value because (a) session loss is real — partial work gets dropped when context restarts, (b) dirty intermediate states create rework when someone (including future-me) acts on them before they're cleaned up, (c) finishing one thing creates a clean save-point whereas partial work across 3 threads creates 3 incomplete save-points.

**How to apply:** Before pivoting to any new topic / question / conversation thread, ask: "Is there an unfinished write, uncorrected error, or pending verification from the prior step?" If yes → finish it first, confirm verification, THEN pivot. If the user pivots first, surface the incomplete state before responding to the new topic: "I'll finish X first (1 more tool call) so nothing's lost, then engage with Y." The save-state risk during long sessions (per `feedback_midday_degradation_save_state` pattern) makes this especially important mid-afternoon.
