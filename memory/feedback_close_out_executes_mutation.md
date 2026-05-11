---
name: Close-Out Means Mutate the Source, Not Just Log It
description: When Kay closes out an item (mark Dormant, remove cadence, sent, archived), the close-out MUST mutate the source-of-truth system in the same session — logging it in session-decisions.md is not enough.
type: feedback
originSessionId: 6e00ef82-87fc-4340-8f77-32940901bc7c
---
When Kay says "remove X", "mark X Dormant", "X is already sent", "drop X" — the close-out MUST execute the corresponding mutation in the source-of-truth system **in the same session**, not just appear as a note in `session-decisions-{date}.md`.

**Why:** Morning briefings are assembled by skills (relationship-manager, pipeline-manager, deal-aggregator) that re-read source-of-truth fresh each morning. If Attio cadence is unchanged, the contact re-surfaces. If a sheet status is unchanged, the row re-surfaces. Session-decisions.md is a log, not an action queue — skills don't read it as the cadence rule, they read Attio. Logging without mutating means the same item lands in tomorrow's brief and Kay sees noise she already closed.

**Past incidents:**
- **2026-04-23 Lauren Della Monica:** Kay changed cadence Quarterly → Occasionally on 3/31. Logged in session-decisions; Attio cadence updated. But the next_action text still read "Maintain quarterly touchpoint." Skill surfaced her as overdue against quarterly threshold for 3 weeks (4/1, 4/2, … 4/22, 4/23) before Kay caught it.
- **2026-04-23 Stanley Rodos:** Quarterly meeting with Kay confirmed in May. Surfaced as "5+ weeks aged commitment" because skill projected drift instead of trusting cadence window.
- **2026-04-23 Guillermo WhatsApp:** Carried forward 3 days as "draft prepared, Kay to copy-send" because no one verified it had been sent.

**How to apply:**
1. When Kay says **"mark X Dormant"** → execute Attio cadence update in same session, then verify with read-back. Don't just write to session-decisions.
2. When Kay says **"remove X from action list"** → identify the source (Attio next_action field, target sheet status column, calendar HOLD tag) and update it. Confirm to Kay what was mutated and where.
3. When Kay says **"already sent"** or **"already done"** → trust her, but verify the audit trail (Gmail outbound, Attio last_interaction). If verified, clear the next_action and remove from any carry-forward queue. If not visible to system (text, WhatsApp, in-person), add a manual `last_interaction` note in next_action so the skill won't re-surface.
4. When Kay says **"drop"** or **"close"** → propagate across ALL surfaces where the item could re-appear: Attio, target sheet, briefing carry-forward in evening session-decisions, vault inbox items.
5. **Briefing carry-forward hygiene:** When writing the evening session-decisions, if an item was closed during the day, mark it `CLOSED:` not `DEFERRED:`. Carry-forward queues should only re-surface items that are genuinely still open. Anything Kay said no/done/sent to → CLOSED.

**Verification rule:** Before ending any session, scan that day's session-decisions for verbs that imply state change (`REMOVED`, `MARKED`, `SENT`, `CLOSED`, `DROPPED`). For each, confirm the corresponding system mutation actually happened. If only the log entry exists without the mutation, the item will re-surface tomorrow — fix it before closing the session.

**This is the enforcement teeth for `feedback_close_the_loop.md`.** The close-the-loop rule says "every session decision must be actioned across ALL downstream systems before session ends." This memory specifies *how* — by mutating source-of-truth in the same turn Kay says it, not by trusting the next morning's skill to honor a log entry it doesn't read.
