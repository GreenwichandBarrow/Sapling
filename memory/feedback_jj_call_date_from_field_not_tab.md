---
name: JJ call counts come from the Call Date field, never the tab name
description: Tab dates on Call Log sheets are ESTIMATED call dates (when a target batch was prepped/staged). Actual dial counts must be derived from the Call Date values JJ populates, grouped by that actual date.
type: feedback
originSessionId: 3d944631-1e1f-43d0-88c1-6fdd795901fd
---
Tab names like `Call Log 4.21.26` indicate when a target BATCH was staged/estimated for calling, not when dials actually happened. JJ populates a Call Date field per row when he makes the dial. Any pace/volume count for a given day MUST be derived from the populated Call Date values, NOT the tab name.

**Why:** JJ re-dials targets across days (2nd-call rule), batches slip between prep days and actual call days, and JJ sometimes logs today's calls onto yesterday's or next-batch's tab when he works through the target list linearly. Grouping by tab name double-counts or miscounts. This was the first pace-analysis failure on 4/23 (Kay rejected Claude's initial recommendation because it grouped by tab name). Rule is now standalone memory so it stops recurring across skill-invocation boundaries.

**How to apply:**
- For weekly/daily counts of JJ dials: pull the Call Date field across ALL tabs in a sheet (including Full Target List if populated) and group by the actual date value JJ wrote.
- For the post-4/21/2026 (NEW) schema, the fields are "JJ: 1st Call Date" and "JJ: 2nd Call Date".
- For the pre-4/21/2026 (OLD) schema, the field named "JJ: Call Date" exists but beware header-vs-data drift — verify by inspecting a few sample rows before counting (4/20 data was written into the positionally-labeled "Call Notes" field despite the "Call Date" header).
- When answering "how many dials this week/day," never say "N dials on the MM.DD tab" — say "N dials with Call Date = YYYY-MM-DD."
- Enforcement companion: `feedback_no_column_references_in_docs` (stop hook); reference fields by NAME, not letter.
