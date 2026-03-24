---
name: feedback_carryover_logic
description: Daily note carry-over should always be from the previous workday, not from the last daily note that exists
type: feedback
---

Daily note task carry-over should be from YESTERDAY (previous workday), not from the last daily note file that exists.

**Why:** Kay noticed that Tuesday's daily note carried over from Friday because Monday had no daily note. That's wrong — Tuesday should carry from Monday, regardless of whether a daily note was written Monday. If no note exists, just carry new items.

**How to apply:** In the /start Previous Day Agent, always look at yesterday (or Friday if Monday). If that daily note doesn't exist, don't fall back to an older note — just report "no previous daily note" and let the inbox/email agents handle surfacing pending items.
