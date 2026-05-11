---
name: Strategic thresholds need grounding (no vibe-numbers)
description: Never propose a strategic threshold (financial floor, scoring cutoff, retention window, etc.) as a vibe-number. Either cite the constraint that derives it, or admit it's a guess and ask the principal to set it.
type: feedback
originSessionId: e8a79c7a-dbe3-484f-a6ad-c576b0b6d195
---
When proposing any number that's load-bearing — meaning future agents will cite it, or it gates important decisions — the number must be derivable from a stated constraint OR explicitly tagged as a guess for the principal to set.

**Why:** 2026-05-03 I proposed an "OPPORTUNISTIC EBITDA floor" of $1M for broker-channel deals in deal-aggregator. There was no math behind it — just "lower than the $2M strict floor." Kay caught it immediately: "Why is the floor dropping?" The actual constraint chain (per `feedback_deal_screen_300k_salary_15pct_margin`) makes $2M source-invariant — Kay's $300K salary + debt service produces the floor regardless of channel. A $1M broker-channel deal still doesn't pencil. The proposed relaxation would have surfaced noise as signal for weeks before being caught. See `brain/traces/2026-05-03-strategic-thresholds-need-grounding.md`.

**How to apply:**

Before proposing a number that gates decisions, do ONE of the following:

1. **Derive it.** Show the constraint chain: "$2M EBITDA = $300K salary / 15% margin floor / debt-service-affordable per `feedback_deal_screen_300k_salary_15pct_margin`." If you can name the constraint, the number is grounded.

2. **Admit and ask.** "I don't have a basis for this number — what should it be?" Single question, one shot. Default to grounding via memory; only ask if no memory derives it.

**Specifically for G&B deal-screen logic:** Financial floors (EBITDA, margin, debt-service) are constraint-driven by Kay's salary + structure. Don't relax them by source, channel, niche, or any other axis. Relax INDUSTRY filters, GEOGRAPHY filters, or NICHE-strict requirements when source format justifies. Never touch the financial gate without a constraint argument.

**Threshold examples that are load-bearing in this system (need grounding):**
- Buy-box financial floors (EBITDA, margin, revenue, asking price)
- Retention thresholds (days silent → propose retire)
- Scoring weights (G&B Industry Scorecard)
- Cadence windows (nurture cycles, conference T-7)
- Validator thresholds (artifact size minimums, runtime ceilings)

**Threshold examples that are NOT load-bearing (vibe is fine):**
- UI display ordering tweaks
- Log retention days (admin choice)
- Slack message length caps
