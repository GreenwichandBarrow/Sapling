---
schema_version: 1.1.0
date: 2026-04-26
type: trace
today: "[[notes/daily/2026-04-26]]"
task: Hardened SaaS purchase rule from "monthly first, annual after 30-60 days" to "never annual unless monthly isn't offered"
had_human_override: true
importance: high
target: memory feedback_saas_monthly_first.md, budget-manager skill
tags: [date/2026-04-26, trace, topic/saas-purchasing, topic/budget-discipline, topic/lock-in-risk, pattern/soft-rule-graduates-to-hard, domain/operational]
---

# Decision Trace: SaaS purchase rule — never annual

## Context

Earlier in the session I saved a soft version of this rule: "Default to monthly billing on new SaaS. Switch to annual only after 30-60 days of confirmed daily use." That version allowed graduating to annual once a tool's value was proven.

Hours later, after the cancellation flow for [[entities/superhuman|Superhuman]] (acquired by Grammarly, billed annually) hit a brick wall — Grammarly chatbot policy stated *"previous charges are not refunded, no human escalation for discretionary refund through this channel"* — Kay said: *"this is why we have a hard rule = no annual subscriptions unless its the only option."*

Then Kay surfaced suspicion that [[entities/motion|Motion]] is also annually-billed. Three vendors with annual lock-in within one session.

## Decision

Replaced the soft rule with a hard rule. The full memory was rewritten 2026-04-26 to state: *"Never sign up for an annual SaaS plan. Always choose monthly. The only exception: when the vendor literally does not offer a monthly tier."*

## Alternatives Considered

1. **Keep the soft rule (45-day evaluation, then annual OK)** — rejected. Even after a year of proven use, switching to annual exposes the same lock-in risk for the next 12 months. Status quo of monthly is strictly safer.
2. **Soften further to "annual OK if discount >25%"** — rejected. The discount math doesn't pencil if the trapped term ever happens.
3. **Just accept the Superhuman/Motion losses as one-offs** — rejected by Kay. She wants the rule codified durably so this never happens again.

## Reasoning

The 15-20% annual discount is mathematically smaller than the cost of being trapped in the wrong tool for 12 months. The savings only materialize if the tool stays in active use for the full term — and that's not predictable on day 1, day 30, day 90, or even after a year of proven use. Status quo of monthly billing has negligible cost (the 15-20% premium) and absolute downside protection (cancel any month).

## Why This Trace Matters

A future agent encountering "annual saves 20% — switch?" will see the soft rule via memory but might reason that 6 months of proven use justifies the discount. This trace documents that the rule was deliberately tightened AFTER such reasoning failed in the wild — the receipt is Superhuman's no-refund stonewall + Grammarly's no-escalation policy + Motion's likely-same.

The hard rule is meant to be slightly costly (foregoing 15-20%) in exchange for absolute optionality. Future agents should not relitigate the math; they should just enforce monthly.

## Key Insight

Behavioral SaaS rules trained from one bad experience are softer than rules trained from three. The Superhuman/Grammarly/Motion compounding made Kay shift from "evaluate carefully" to "just don't." When stating purchase recommendations going forward, never offer the annual price; quote monthly only.
