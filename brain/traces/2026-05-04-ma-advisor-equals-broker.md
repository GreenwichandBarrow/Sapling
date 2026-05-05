---
schema_version: 1.1.0
date: 2026-05-04
type: trace
title: "M&A Advisor = Broker (not Investment Banker) — calibration override of strict self-ID rule"
trace_type: doctrine-establishment
tags: ["date/2026-05-04", "trace", "topic/intermediary-classification", "topic/broker-channel-build", "topic/calibration-override"]
---

# M&A Advisor = Broker (not Investment Banker) — calibration override of strict self-ID rule

## Trigger

During the Pass 2 per-firm web verification of the Intermediary Target List, 7 firms on the Brokers tab (Touchstone Advisors, Pillai Capital, GillAgency, IBG Business, Inbar Group, NorthBridge, Evergreen Financial) were flagged as candidates to MOVE to the Investment Bankers tab. Reasoning: their homepage hero text self-identified as "M&A Advisor" / "M&A Advisory" / "M&A advisory firm" — and the prior `feedback_classify_intermediary_by_self_id` rule said "use firm self-ID as primary signal." Hero says M&A Advisor → IB tab.

The same logic also recommended moving Mariner (formerly Woodbridge International) — already on IB tab — would have stayed there, and might have pulled additional Pass 1 candidates (NYBB, WorldCity, MergersCorp, Midas) onto the IB tab.

I surfaced the calibration question to Kay: STRICT SELF-ID (move all 7 to IB) vs. IBBA-CREDENTIAL-WINS (keep on Brokers) vs. HYBRID per firm.

## Decision

Kay collapsed the question with a one-sentence rule: **"M&A Advisors are business brokers, not investment bankers."**

Doctrine: the "M&A Advisor" / "M&A Advisory" label belongs on the Brokers tab. The Investment Bankers tab is reserved for firms that explicitly self-identify with "Investment Bank" / "Investment Banking" label, typically backed by FINRA/SIPC registration.

Concrete reclassification triggered by this rule:
- **Stay on / move to Brokers (per the rule):** Touchstone, Pillai, GillAgency, IBG, Inbar, NorthBridge, Evergreen, NYBB, WorldCity, Midas, Gottesman (revert from incorrect Batch B move)
- **Mariner / Woodbridge** (currently IB tab, "Trusted M&A Advisors" hero) → MOVE to Brokers per the new rule
- **Stay on / move to IB:** MergersCorp ("leading investment banking firm"), MarshBerry (FINRA/SIPC + "INVESTMENT BANKING & CONSULTING")

Captured as a refinement to `feedback_classify_intermediary_by_self_id.md`.

## Alternatives Considered

1. **Strict self-ID rule applied uniformly** — what the prior memory said, what Pass 2 had recommended. Rejected because it put 7+ IBBA-credentialed firms on the wrong tab. Brokers self-marketing as "M&A Advisors" is industry-wide aspirational language, not a meaningful tier indicator.
2. **IBBA membership as overriding signal** — keep all IBBA-credentialed firms on Brokers regardless of self-ID. Cleaner mechanically, but flips when the firm is credentialed and explicitly self-IDs as IB (Pillai Capital had FINRA/SIPC AND IBBA exposure — would be ambiguous).
3. **Hybrid per-firm judgment call** — what I initially defaulted to. Rejected because it doesn't scale; every future verification pass re-litigates the same question.

## Reasoning

Kay's answer flips the strict self-ID rule on a single label. The label "M&A Advisor" is industry vernacular that brokers, IBs, fractional CFOs, exit planners, and even some valuation firms all use. Treating it as the IB-tier signal pulled too many real brokers off the Brokers tab. The IB tab should be narrow and specific: only firms that explicitly say "Investment Bank" / "Investment Banking" — that's a smaller, more defensible bucket.

This isn't a soft preference; it's a doctrine that resolves an entire class of categorization questions. Future Verification passes apply this rule directly — no need to escalate per-firm.

## Why This Trace Matters

A future agent reading the prior `feedback_classify_intermediary_by_self_id` rule literally would conclude "homepage hero says M&A Advisor → IB tab." That conclusion is wrong by Kay's doctrine. Without this trace + the memory refinement, the next intermediary list verification subagent would re-recommend the same 7+ wrong moves, Kay would have to re-correct, and the cycle would repeat. The trace + the memory refinement collapse it to a one-rule application.

## Key Insight

**Industry vernacular labels are unreliable categorization signals when widely adopted across tiers.** "M&A Advisor" is not a meaningful broker/IB distinction — it's just shorthand many sell-side firms use. The right discriminators are explicit IB self-ID + structural signals like FINRA/SIPC registration. Defaulting to the broader bucket (Brokers) when the label is ambiguous is the safer call because it preserves more cold-list inventory for outreach and avoids creating a thin/inflated IB tab that doesn't match reality.

Same dynamic likely applies to other industry-vernacular tier labels (e.g. "advisor" generically, "consultant" generically) — when in doubt, default to the higher-volume tab and require explicit signals to elevate.
