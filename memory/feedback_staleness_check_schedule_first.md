---
name: Staleness check requires schedule lookup
description: Before declaring a scheduled skill stale/broken, cross-reference its schedule in CLAUDE.md's Scheduled Skills table against today's day-of-week. Last-log-date ≠ last-scheduled-fire.
type: feedback
originSessionId: b0fe75c7-8d2c-4071-8651-bfb51510d83a
---
Before flagging any scheduled skill as STALE / BROKEN / MISSED in System Status or briefings, run this two-step check:

1. **Read the Scheduled Skills table in CLAUDE.md** — confirm which day(s) of the week + which hour the skill is actually supposed to fire.
2. **Compare today's date to the expected fire schedule** — if today is between two scheduled fires, log absence is *expected*, not stale.

**Why:** On 2026-04-22 (Wed) I flagged `jj-operations` as STALE because the newest log was 4/12. But jj-operations-prep only fires Sunday 11pm ET — so between 4/19 Sunday and 4/26 Sunday there is no scheduled fire at all. The 4/19 Sunday prep was missed (legitimately) but was manually patched; I then double-diagnosed the same non-issue twice in one session, burning Kay's attention on a phantom problem.

**How to apply:**
- Never report "skill X hasn't fired since {date}" without also stating "X's next scheduled fire is {date}" from the table
- If today IS the scheduled day and the fire didn't happen → real stale flag
- If today is NOT a scheduled day → silent (or mention next-fire date only if someone explicitly asks about the skill)
- Applies to: jj-operations (Sun 11pm), niche-intelligence (Tue 11pm + nightly), weekly-tracker (Fri), and any new scheduled skill added to the table
- Heuristic: if the skill's schedule is weekly or less-frequent, a 7-day gap in logs is normal, not suspicious
