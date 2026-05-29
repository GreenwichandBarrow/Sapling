---
name: feedback-jj-10am-slack-monday-only
description: "JJ-operations 10am Slack delivery is Monday-only — never surface a \"JJ 10am log missing\" alert on Tue-Sun."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9955477e-c1cb-4801-b01e-ad731993a6df
---

JJ-operations daily 10am Slack delivery only fires on Mondays. Non-Mondays do NOT have a daily JJ-ops Slack — its absence is expected, not a broken-system signal.

**Why:** Kay corrected the morning briefing on 2026-05-28 after I flagged a missing `jj-operations-2026-05-27*.log` as a 🔴 System Status item. JJ runs his calls Mon-Thu but the 10am Slack call-list handoff from Kay's system to JJ happens once at the start of the week (Monday) — the rest of the week he works the list himself. Snapshot-refresh logs (`jj-snapshot-refresh-*`) firing daily are a separate concern; they're the data sync for the tabs, not the call-list delivery.

**How to apply:**
- Tue/Wed/Thu/Fri/Sat/Sun morning briefings: do NOT verify or flag the existence of a daily `jj-operations-{date}.log`. Its absence is by design.
- Monday morning briefing: DO verify the Sunday-night prep log + the Monday 10am Slack delivery. Their absence is a real 🔴.
- Sunday-prep `jj-operations-sunday-*.log` exists at the prior path and IS the canonical Sunday artifact.
- If asked to check JJ-ops health on a non-Monday, point at the snapshot-refresh log + recent Slack-thread history with JJ, not a daily-ops log.
- Related: [[feedback-jj-team-member]], [[feedback-jj-call-timing]], [[feedback-jj-communication-style]].

**Mistake to avoid:** Don't generalize the /goodmorning Step 5 verification rule into a daily check. The rule says "verify it fired by checking `logs/scheduled/jj-operations-{date}.log`" but the implicit precondition is "if it was supposed to fire today." On non-Mondays, the precondition is false, so the verification is meaningless and noise-generates.
