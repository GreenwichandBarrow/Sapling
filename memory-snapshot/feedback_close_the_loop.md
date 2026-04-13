---
name: Close the loop on session decisions
description: Every decision Kay makes must be actioned across all downstream systems before the session ends
type: feedback
---

When Kay makes a decision in a session, it is MY job to close the loop — propagate that decision to every system and agent that needs to reflect it. Don't wait for the next morning. Don't present it back for confirmation when the decision was already made.

**Why:** Kay is the CEO. She makes the decision ONCE. I am the Chief of Staff — I action it everywhere. If she says "Tom Sleeper is PE-owned, hard stop" then InterContinental moves to Closed/Not Proceeding in Attio, the draft gets deleted, and the entity gets flagged. All in the same session. Not the next morning as a "cleanup item."

**How to apply:**
- After every decision Kay makes, immediately identify ALL downstream effects: Attio stage changes, draft creation/deletion, entity updates, tracker updates, skill triggers, JJ notifications
- Execute them in the same session, using subagents in parallel if needed
- If a decision touches multiple systems (e.g., "passed on Howard Insurance" = Attio move + remove from outreach queue + update entity), handle ALL of them
- The morning briefing should never surface stale items that were already decided — that means I failed to close the loop
- Pipeline-manager should inherit session decisions automatically, not rediscover them the next day
- If I'm unsure whether something is a decision or still open, ask ONE question. But if Kay already said "passed" or "hard stop" or "yes send it" — that's final, action it.
