---
schema_version: "1.1.0"
date: 2026-03-23
type: budget-report
status: published
tags:
  - date/2026-03-23
  - output
  - output/budget-report
  - status/published
  - topic/budget
  - topic/runway
  - topic/fund-management
  - source/quickbooks
---

# Budget Report: January-February 2026

First monthly budget report from the budget-manager skill. Data sourced from StartVirtual bookkeeper P&L and Balance Sheet PDFs (QBO accrual basis).

## Fund Position (as of February 28, 2026)

| Metric | Value |
|--------|-------|
| Fund Balance | $255,724 |
| DD Reserve (held back) | $40,000 |
| Available for Operations | $215,724 |
| Monthly Burn (Jan) | $31,304 |
| Monthly Burn (Feb) | $30,096 |
| 2-Month Avg Burn | $30,700 |
| Steady-State Burn (est.) | $19,500 |
| Fund Deadline | February 2027 |

## Monthly P&L Summary

| Category | Jan 2026 | Feb 2026 | YTD |
|----------|----------|----------|-----|
| Principal Draw | $12,692 | $12,692 | $25,384 |
| Payroll Taxes | $1,533 | $1,172 | $2,706 |
| Health Insurance | $8,787 | $8,250 | $17,037 |
| Business Insurance | $0 | $55 | $55 |
| Contractors (JJ + Analyst + BK) | $1,924 | $884 | $2,808 |
| Office/Rent | $1,220 | $992 | $2,212 |
| Travel | $3,506 | $1,946 | $5,452 |
| Software & CRM | $447 | $903 | $1,350 |
| Databases & Research | $1,962 | $282 | $2,244 |
| Marketing | -$116 | $247 | $131 |
| Professional Fees | $0 | $3,200 | $3,200 |
| Bank Fees | $4 | $5 | $8 |
| **Total Expenses** | **$31,958** | **$30,628** | **$62,587** |
| Interest Income | $654 | $532 | $1,186 |
| **Net Burn** | **$31,304** | **$30,096** | **$61,400** |

## Variance Flags (>10% over YTD prorated budget)

1. **Health Insurance: $17,037 actual vs $5,500 budget (210% over)**
   Explanation: Unbudgeted item. $33K annual health plan paid in installments. One installment remaining. After completion, this line goes to $0 monthly.

2. **Payroll Taxes: $2,706 actual vs $1,666 budget (62% over)**
   Likely includes higher withholding rates than Delaware estimate in original budget. Monitor but not actionable.

3. **Travel - Airfare: $2,028 actual vs $500 budget (306% over)**
   California trip airfare (subsequently canceled, $2K credit available). Feb was $0. Should normalize.

4. **Travel - Meals: $2,769 actual vs $834 budget (232% over)**
   Conference and business development meals. Heavy in first 2 months. Monitor trend.

5. **Professional Fees: $3,200 actual vs $534 budget (499% over)**
   CPA annual tax filing. One-time item. Will not recur until 2027.

6. **Office Supplies: $211 actual vs $84 budget (151% over)**
   Small dollar amount. Monitor but not material.

## Runway Analysis

| Scenario | Monthly Burn | Runway | Lasts Through |
|----------|-------------|--------|---------------|
| Current avg ($30,700) | $30,700 | 7.0 months | Oct 2026 |
| Post-health-installments ($22,000) | $22,000 | 9.8 months | Jan 2027 |
| Target steady-state ($19,500) | $19,500 | 11.1 months | Mar 2027 |
| Target with cuts ($17,300) | $17,300 | 12.5 months | Apr 2027 |

## Key Observations

- Jan and Feb burn rates are inflated by health insurance installments ($17K in 2 months) and CPA annual filing ($3.2K). These are front-loaded, not recurring monthly.
- Once last health installment processes (likely March), steady-state monthly burn should drop to $19-22K range.
- To hit $17,300/month target (11 months of runway with $40K DD reserve), need $2-5K/month in savings from tech stack, databases, and bookkeeper transition.
- Year 1 underspent by ~$48K vs budget, primarily from zero DD costs and lower contractor spend.
- Interest income (~$593/mo average) provides small but meaningful offset, earning ~$6.5K over remaining fund life.

## Action Items

1. Process final health insurance installment (March)
2. Run tech stack audit to identify software savings
3. Evaluate JJ cold calling performance over next 2-3 weeks
4. Begin Kick evaluation for bookkeeper transition
5. Review travel budget to maintain discipline after heavy Jan

## Data Sources

- P&L: StartVirtual bookkeeper, QBO accrual basis, reports dated March 19, 2026
- Balance Sheet: StartVirtual bookkeeper, QBO accrual basis
- Budget: G&B 2025-2026 Budget 12.31.24.xlsx, FINAL BUDGET tab
- COA Mapping: Suggested COA.xlsx from BOOKKEEPING/MONTHLY REPORTING
