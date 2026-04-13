---
name: Investor budget reporting format
description: Investors get exactly one inline bullet for budget — dollar amount, percentage, context. No tables, no extra metrics.
type: feedback
---

Investor quarterly updates show budget as ONE bullet, inline format:
`• $433K (79% remaining of $550K raised) slightly under budget`

Three data points in one sentence: dollar amount, percentage of fund, brief context.

**Why:** This is how Kay has reported in every quarterly update (Q1-Q3). Investors don't need burn rate, runway months, or DD reserve breakdowns. Those are internal CFO brief numbers.

**How to apply:** When investor-update skill pulls from budget-manager, it MUST only use budget_remaining and budget_pct, formatted as a single inline bullet. Never expand into a table or add extra budget metrics to the investor deck.
