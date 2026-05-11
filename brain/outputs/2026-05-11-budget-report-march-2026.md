---
schema_version: "1.2.0"
date: 2026-05-11
type: budget-report
status: published
skill_origin: budget-manager
kay_approved: null
kay_approval_date: null
people:
  - "[[entities/anthony-bacagan]]"
tags:
  - date/2026-05-11
  - output
  - output/budget-report
  - status/published
  - topic/budget
  - topic/runway
  - topic/fund-management
  - source/quickbooks
  - person/anthony-bacagan
---

# Budget Report: March 2026

Monthly budget report for March 2026. Data sourced from [[entities/anthony-bacagan|Anthony Bacagan]] (StartVirtual) P&L and Balance Sheet PDFs delivered 2026-04-28 (QBO accrual basis). Trigger-chain auto-invoke was broken when the report arrived; this run closes the gap manually. Trigger chain has since been repaired.

## Fund Position (as of March 31, 2026)

| Metric | Value |
|--------|-------|
| Fund Balance (cash) | $223,820 |
| Checking 4538 | $6,956 |
| Savings 8125 | $216,864 |
| Remaining Health Installment | $7,713 |
| Available After Installment | $216,107 |
| DD Reserve (held back) | $40,000 |
| Available for Operations | $176,107 |
| Steady-State Burn (gross) | $23,403 |
| Net Steady-State Burn (after interest) | $22,853 |
| Runway from Apr 1 (steady-state) | 7.5 months |
| Projected Zero Date | Nov 2026 |
| Fund Deadline | Feb 2027 |
| **Shortfall vs Deadline** | **-3.5 months** |
| Monthly Savings Needed | $7,393 |

## Monthly P&L Summary

| Category | Jan 2026 | Feb 2026 | Mar 2026 | YTD |
|----------|----------|----------|----------|-----|
| Regular Wages | $12,692 | $12,692 | $15,865 | $41,250 |
| Payroll Taxes | $1,533 | $1,172 | $1,214 | $3,919 |
| Health & Accident Plans | $8,787 | $8,250 | $8,250 | $25,287 |
| Business Insurance | $0 | $55 | $48 | $103 |
| Contractors - VA (JJ) | $1,537 | $394 | $1,040 | $2,971 |
| Contractors - Analyst | $387 | $490 | $317 | $1,193 |
| Office Rent | $1,000 | $1,000 | $1,000 | $3,000 |
| Office Supplies | $220 | -$9 | $46 | $256 |
| Postage & Shipping | $0 | $1 | $26 | $27 |
| Apps & Software - CRM | $220 | $318 | $1,345 | $1,883 |
| Apps & Software - Office Use | $227 | $585 | $1,224 | $2,035 |
| Databases & Research | $1,962 | $282 | -$1,238 | $1,006 |
| Advertising & Marketing | -$116 | $247 | $244 | $376 |
| Professional Fees (Accounting + Consulting) | $0 | $3,200 | $911 | $4,111 |
| Travel - Car/Shared Rides | $429 | $178 | $819 | $1,426 |
| Travel - Meals & Entertainment | $1,049 | $1,720 | $1,330 | $4,099 |
| Travel - Airfare | $2,028 | $0 | $0 | $2,028 |
| Travel - Vehicle Gas | $0 | $48 | $0 | $48 |
| Bank Fees | $4 | $5 | $6 | $15 |
| **Total Expenses** | **$31,958** | **$30,628** | **$32,447** | **$95,034** |
| Interest Income | $654 | $532 | $544 | $1,730 |
| **Net Burn** | **$31,304** | **$30,096** | **$31,904** | **$93,304** |

## Variance Flags (>10% over YTD prorated budget at Q1)

YTD prorated budget = Annual budget / 12 × 3 months elapsed.

1. **Health & Accident: $25,287 YTD vs $8,250 prorated (+207%)**
   Timing-driven, not overspend. The $33K annual plan was front-loaded into Q1 installments. One installment ($7,713) remains. Once paid, line drops to $0 — this is a known unbudgeted item from `brain/context/budget.md`. Watch for in Q2 forecast.

2. **Professional Fees (Accounting + Consulting): $4,111 YTD vs $801 prorated (+413%)**
   $3,200 CPA annual filing hit Feb; $911 March consulting fees added. Consulting fees are a new line item — investigate what these are (March only). Annual CPA filing was budgeted as one-time; the consulting line needs context before Q2 forecast.

3. **Travel - Meals & Entertainment: $4,099 YTD vs $1,251 prorated (+228%)**
   Significantly over. Watch trend in April. If pattern continues, $5K annual budget is undersized.

4. **Travel - Car/Shared Rides: $1,426 YTD vs $501 prorated (+185%)**
   March spike ($819) drove the YTD overshoot. Conference travel likely.

5. **Apps & Software - CRM: $1,883 YTD vs $900 prorated (+109%)**
   March spike ($1,345 vs $220 Jan, $318 Feb). Likely annual subscription renewal hit March. Verify with Tab 3 tech audit next cycle.

6. **Apps & Software - Office Use: $2,035 YTD vs $900 prorated (+126%)**
   Same pattern — March spike ($1,224). Probable annual renewal cluster in March. Tech-audit cycle should review.

7. **Travel - Airfare: $2,028 YTD vs $750 prorated (+170%)**
   Jan front-load only. Feb-Mar both $0. Likely a conference flight booked far in advance; not a recurring overshoot.

8. **Advertising & Marketing: $376 YTD vs $249 prorated (+51%)**
   Small dollar amount. Not material.

**Under-budget items:**
- Databases & Research: -$1,238 in March (credit/refund), pulling YTD to $1,006 vs $3,750 prorated. Net $2,744 favorable.
- Bookkeeper line: $0 booked YTD vs $741 prorated. Anthony has billed but invoices not yet posted to QBO. Surface to Anthony if not resolved by April close.

## Runway Analysis

**Prior estimate (per `brain/context/budget.md` line 99):** 9.6 months from April 1, projected zero Jan 2027, ~1 month shortfall.

**Current estimate:** 7.5 months from April 1, projected zero Nov 2026, **3.5 month shortfall**.

**Delta: -2.1 months.** This crosses the material-change threshold (>2 months).

Drivers of the change:
1. Steady-state burn revised upward to $22,853 net (was $21,550 in prior report).
2. Health insurance and software annual renewals concentrated more spending in Q1 than the original prorated model assumed.
3. Three months of actual data now anchors the steady-state estimate vs. two months prior.

**Scenarios:**
- **Status quo:** zero Nov 2026, miss deadline by 3.5 months.
- **Cut $7,393/mo** (target): hit Feb 2027 deadline exactly. Requires aggressive tech audit + bookkeeper transition complete + travel discipline.
- **Cut $4,000/mo:** zero Jan 2027, ~1 month shortfall (matches prior estimate baseline).

## Action Items

1. **Run `/budget tech-audit`** — the March software spike ($2,569 combined CRM + Office Use) suggests annual renewals just landed. Tech audit can identify cuts to hit the $7,393/mo savings target.
2. **Investigate March consulting fees ($911)** — new line item, not in original budget. Confirm what it covers.
3. **Follow up with Anthony on bookkeeper line posting** — his invoices haven't hit QBO; verify billing is current.
4. **Track Travel - Meals** — if April continues the $1.3-1.7K pace, the $5K annual budget needs a revision.
5. **Plan for last health installment** ($7,713) — after it clears, monthly burn drops by ~$2,750/mo and runway extends materially.

## Outcome

- **Published:** 2026-05-11
- **Engagement:** Sheets already updated (Tab 1 March column + bottom block; Tab 2 burn rate / runway / investor reporting blocks). Vault artifact created. Material variance + 2.1-month runway delta surfaced for review.
- **Trigger-chain note:** Auto-invoke on bookkeeper P&L was broken when Anthony delivered Mar 28. Trigger chain has been repaired in a parallel session; March was processed manually to close the gap.
