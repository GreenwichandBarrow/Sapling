---
schema_version: 1.1.0
date: 2026-05-06
type: trace
today: "[[notes/daily/2026-05-06]]"
task: Process the intermediary outreach cadence bump from 5/day to 7-per-day-total
had_human_override: true
importance: medium
target: skill:outreach-manager
tags: ["date/2026-05-06", "trace", "topic/intermediary-channel", "topic/broker-outreach", "pattern/total-cap-not-additive-cap"]
---

# Decision Trace: Intermediary Cadence — 7 Per Day Total, Not 7+5 Additive

## Context

Yesterday's session-decisions saved a "5 email + 5 LinkedIn DMs per day" doctrine for intermediary outreach (`feedback_intermediary_outreach_5_email_5_linkedin.md`). This morning Kay flagged "we are behind in kicking off intermediary emails. to still reach the 50 target by the end of next week, lets increase an evenly dispersed amount for each day."

The COO did the math: 50 emails ÷ 8 workdays remaining (5/6 → 5/15) = 6.25/day → rounded to 7/day. Recommendation surfaced as **"Bump intermediary email cadence from 5/day → 7/day, hold LinkedIn DMs at 5/day. New doctrine = 7+5 (12 touches/day)."**

Kay replied "5. yes, raise to 7." COO interpreted that as approval of the 7+5 frame and renamed the memory file `feedback_intermediary_outreach_7_email_5_linkedin.md`.

Kay then corrected: "I thought we were updating to 7 per day not 7+5."

## Decisions

### The daily cap is 7 TOTAL across all channels, not 7 email + 5 LinkedIn additive

**AI proposed:** 7 emails + 5 LinkedIn = 12 touches/day total (additive bump on top of yesterday's two-channel split).

**Chosen (Kay):** **7 touches per day, total across all channels.** Channel mix determined per-person within the 7-cap. Email is the priority channel because the catch-up target is email-specific; LinkedIn fills any remainder for Apollo no-match brokers.

**Reasoning:**
- Yesterday's "5+5" frame was additive (10 touches/day total); the bump conversation conflated the email cadence with the channel-stack.
- Total touch volume matters for sender reputation and bandwidth, not channel-isolated cadence. A 12/day stack is meaningfully different from a 5/day stack — that wasn't the intended bump.
- Math still works under the corrected frame: if every slot goes to email (best case), 7×8 = 56 emails by 5/15, clears the target. If some slots fall to LinkedIn DMs (Apollo no-match brokers), email count is lower but daily volume holds at 7.

**Pattern:** #pattern/total-cap-not-additive-cap

## Why This Trace Matters

Future agents will see "Kay said 'yes raise to 7'" in session-decisions and may re-misread it as additive (carry the 5 LinkedIn forward and add 7 email). The correction came AFTER the initial yes, which makes the trail confusing. This trace captures: **a "raise to N" instruction in a multi-channel cadence context means TOTAL of N, not N + existing-channel-count, unless explicitly stated as additive.**

The same misread pattern could happen on JJ dial counts, DealsX volume, or any other multi-channel cadence. Default interpretation: cap means total, not channel-isolated.

## Key Insight

When recommending a cadence bump, **state the total touches/day explicitly** in the recommendation — "Bump from 5 emails/day → 7 emails/day for 7 total daily touches (LinkedIn DMs absorbed into the 7-cap)" — rather than letting the reader infer whether the bump is additive or replacement. The ambiguity costs a memory rewrite cycle.
