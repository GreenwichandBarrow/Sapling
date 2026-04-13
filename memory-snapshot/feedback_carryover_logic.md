---
name: feedback_carryover_logic
description: Daily note carry-over should surface all OPEN items across the system, not just yesterday's daily note
type: feedback
---

Carry-over should surface all OPEN items, not just tasks from the previous day's note.

**Why:** Carrying over only from yesterday's daily note means items from earlier days get lost if a day is skipped (e.g., no Monday note means Tuesday misses Friday's open items). The system should track open items regardless of which day they were created.

**How to apply:** The Previous Day Agent should scan for all unchecked tasks across recent daily notes and open inbox items — not just yesterday. An item stays in carry-over until it's checked off or its inbox item is marked done. The inbox scanner already covers inbox items, so the carry-over agent should focus on open tasks from ANY prior daily note that haven't been completed.
