---
name: Rev Source only when Revenue exists
description: Never populate Rev Source column if Revenue is blank — looks wrong to show source with no data
type: feedback
---

Rev Source column (Col G) should ONLY be populated when Revenue (Col H) has a value.

**Why:** Writing "Apollo" in Rev Source with blank Revenue looks like bad data. Kay caught this on the Pest Management call logs April 7.

**How to apply:** In list-builder and any sheet write, check if Revenue is populated before writing Rev Source. If Revenue is blank, leave Rev Source blank too.
