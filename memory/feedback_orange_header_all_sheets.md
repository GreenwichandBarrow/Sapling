---
name: Orange header convention for all agent-trigger columns
description: Any column that triggers agent action must have an orange header. Verify across ALL skills and trackers.
type: feedback
---

Orange column header = agent reads this column and takes action based on its value. This convention must be applied across ALL sheets and trackers, not just WEEKLY REVIEW.

**Why:** Visual signal to Kay and anyone reading the sheet that changing a value in this column will trigger automated behavior. Prevents accidental agent activation.

**How to apply:**
- WEEKLY REVIEW Col D (Current Status) — already orange
- WEEKLY REVIEW Col K (Outreach Channel) — needs orange (can't be set via CLI, must be manual)
- Target sheets Col O (Kay Decision) — already orange
- Any future column that gates agent behavior must get an orange header
- When creating new tracker columns that agents read, always flag for manual orange formatting
- gog CLI cannot format cells — orange headers must be set manually by Kay or noted for manual application
