---
name: feedback_verify_live_state_before_redo_when_user_reports_missing
description: "When Kay says a just-made sheet/structural change is \"still missing\"/\"not done\", verify live server-side state BEFORE redoing — stale browser view is the usual cause"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 16ad8905-aab9-4af1-8d4e-c55dfd8fabfd
---

When Kay reports that a change you just made is missing or "still needs to be done" (e.g. "you still need to add the exercise row across the tabs"), **re-query the live server-side state of every affected surface FIRST**. Do NOT re-run the mutation on the assumption it failed.

**Why:** Kay sends requests while you're mid-edit and Google Sheets does not live-refresh open tabs (especially across multiple tabs she has open). The change is usually already persisted; her view is stale. Re-running a structural mutation (e.g. another `insertDimension`) creates a DUPLICATE row and re-shifts hardcoded slot ranges — actively corrupting the board. 2026-05-18: the "Exercises" habit row was already on all 8 tabs (verified incl. native-checkbox data-validation); re-inserting would have duplicated it. Correctly verified + refused, told Kay to hard-refresh.

**How to apply:** On a "still missing / not done" report about recent work: (1) read the live state of all affected tabs/cells via the API (not memory, not snapshot); (2) if present and correct → show concrete proof (values + e.g. data-validation type), state it's a stale-view refresh issue, ask her to hard-refresh, and explicitly say you will NOT re-run the mutation (would duplicate); (3) only if genuinely absent on a specific surface → fix that surface. Pairs with [[feedback_check_before_claiming_artifact]] and [[feedback_verify_dont_ask]].
