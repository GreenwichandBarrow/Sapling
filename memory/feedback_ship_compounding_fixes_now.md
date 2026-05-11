---
name: When a fix compounds on a recurring job, ship NOW — don't defer per plan
description: Fixes that improve a daily/weekly recurring skill output should ship the same session they're identified, not deferred to a "Tue per plan" or future workblock. Each missed cycle compounds the cost of deferral.
type: feedback
originSessionId: c0375c4c-6be2-4191-9f4b-0e97e59a3de4
---
**Rule:** When a fix is identified that would improve the output of a recurring scheduled skill (deal-aggregator at 6am+2pm daily, email-intelligence 7am daily, relationship-manager 6:50am daily, etc.), ship the fix in the current session if it can land before the next scheduled fire. Do not defer to "the locked plan said Tuesday" if today's afternoon fire would benefit.

**Why:** 2026-05-04, two diagnosis recommendations from the broker-channel build came up — (1) audit subagent body-parsing fix to email-intelligence, (2) per-listing rejection log to deal-aggregator. The locked 3-week plan put the deal-aggregator filter work on Tue 5/5. I deferred both fixes to Tue. G&B operator pushed back: "we rerun deal aggregator at 2pm everyday." Each day deferred = one daily fire missing the improvement = compounding loss in observability and decision quality. Saturday already shipped wrapper hardening that benefited Mon's first run; same logic applies to incremental improvements.

**How to apply:**
- When a diagnosis or audit surfaces a fix to a SCHEDULED skill, check the next launchd fire time. If the fix can land before the next fire, ship today.
- "Per the locked plan" is not a reason to defer if the fix is small + bounded. Small fixes compound. Big fixes (full feature wires, e.g., dual-filter routing tied to broker-buy-box doc IDs) stay on plan.
- Default mode for shipping a small fix on the same day: spawn a focused subagent with explicit "DO NOT add scope" guardrails, ship before next scheduled fire, validator catches regressions.
- Read-only skills (deal-aggregator scan, email-intelligence scan) have lower ship-now urgency than mutating skills (target-discovery, jj-operations, weekly-tracker), but recurring read-only fires still benefit from compounding fixes.
- Surface a one-line summary of the wrapper change to the operator the same session: "Today's 2pm fire is the cutover. Validator catches regressions."

**Caught:** 2026-05-04 broker-channel build. Audit + per-listing-log fixes deferred to Tue per locked plan. G&B operator: "why arent you doing those fixes now? we rerun deal aggregator at 2pm everyday." Both fixes shipped same session via parallel subagents, validator update was date-gated to today's afternoon as the cutover. Today's afternoon fire benefited; tomorrow's morning fire benefits; every fire benefits compounding from the moment of ship. Deferral cost was 1 missed afternoon fire if I had stayed with my original plan.
