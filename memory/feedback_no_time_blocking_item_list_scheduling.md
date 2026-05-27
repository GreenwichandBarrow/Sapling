---
name: feedback-no-time-blocking-item-list-scheduling
description: Kay does NOT block time on the calendar for work items — schedule via To Do + day-tab priority slots instead. Codified 2026-05-26.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37de3c90-d2d0-44f1-9b4b-ddb0727158c9
---

Do not propose "block this morning to draft X" / "block 2 hours for Y" framings. Kay does not block time and the approach does not work for her. Instead: append the item to To Do, then place it as a priority slot on today + tomorrow's day tabs (or whichever days fit). Item-list scheduling, not calendar-time scheduling.

**Why:** Kay said directly on 2026-05-26: *"we dont block time, it doesnt work, just update to do list and put it on today and tomorrow."* Confirmed pattern after morning brief item #2 ("Block this morning to start the quarterly investor update draft") was retired in favor of "update To Do + put on today and tomorrow." Time-blocking framings have failed implicitly across prior briefings — this is the explicit naming of why.

**How to apply:**

1. **Briefing language:** Don't say "block this morning for X" or "carve out time for Y." Say "add X to To Do + place on today and tomorrow's priority slots." Same intent, item-list grammar.

2. **When a priority surfaces (active deal, investor update, urgent follow-up):** the correct mutation is `task_tracker.py append` (Short Term, with Due date if applicable) + `schedule-to-day-slot` for today + tomorrow. Two slot writes, not a calendar block.

3. **Recurring items:** these already use `Horizon = Weekly Recurring {day}` and flow through `build-week` → Week tab → `distribute-week` → day tabs. No calendar holds.

4. **Calendar events** are external meetings (calls, lunches, conferences) and personal logistics — those go on Google Calendar. Internal work items do NOT.

5. **If Kay misses an item's intended day** (e.g., "investor update this morning" but financials work consumed the slot): don't surface the miss as a failure. Reschedule the item — push to tomorrow as top-priority, or split across today PM + tomorrow AM. Same item, different slot.

**Edge case — true deadlines:** if an item has a hard external deadline (e.g., "submit form by Friday 5pm"), the deadline goes in the Due column on To Do. The day-slot placement still drives execution; the Due date drives surface-as-overdue logic, not calendar blocking.

See also: [[user-task-management]], [[feedback-default-to-now-not-later]] (don't defer execution to a hypothetical future block — schedule the item, work it from the day tab when the slot comes up).
