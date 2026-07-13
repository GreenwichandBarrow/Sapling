---
schema_version: 1.2.0
date: 2026-07-13
type: budget-report
status: published
skill_origin: budget-manager
kay_approved: null
kay_approval_date: null
people:
  - "[[entities/anthony-bacagan]]"
companies:
  - "[[entities/greenwich-and-barrow]]"
tags:
  - date/2026-07-13
  - output
  - output/budget-report
  - status/published
  - topic/budget
  - topic/runway
  - topic/fund-management
  - source/startvirtual
  - source/quickbooks
  - person/anthony-bacagan
  - company/greenwich-and-barrow
---

# Budget Report: June 2026

Validated June close for [[entities/greenwich-and-barrow|Greenwich & Barrow]] using the Management Report email from [[entities/anthony-bacagan|Anthony Bacagan]] in Gmail thread `19f293490cb2bcde`, delivered 2026-07-03. The June 2026 Profit & Loss and Balance Sheet PDFs were read from Drive under BOOKKEEPING / MONTHLY REPORTING / JUNE 2026, and the Budget Dashboard is updated through June 30.

## Fund Position

| Metric | Value |
|--------|-------|
| Total invested | $551,845.01 |
| Cash on hand | $142,224.43 |
| DD reserve | $40,000.00 |
| Available for operations | $102,224.43 |
| Budget remaining | $142,224.43 |
| Budget % remaining | 25.77% |
| Steady-state gross burn | $22,100 |
| Interest income monthly average | $492 |
| Net steady-state burn | $20,100 |
| Months remaining | 5.09 |
| Projected zero date | Dec 2026 |
| Fund deadline | Feb 2027 |
| Shortfall vs deadline | 1.91 months |
| Monthly savings needed | $5,497 |

## Monthly P&L Summary

June actuals from the June 2026 report:

| Line Item | Amount |
|----------|--------|
| Total expenses | $26,374.54 |
| Interest income | $339.95 |
| Net burn | $26,034.59 |
| Regular wages | $15,865.40 |
| Payroll taxes | $1,213.70 |
| Health and accident plans | $2,750.00 |
| Business insurance | $39.76 |
| Contractors - outsourcing | $1,287.00 |
| Contractors - contract labor | $436.50 |
| Office rent | $1,000.00 |
| Office supplies | $0.00 |
| Postage | $9.92 |
| Apps and software - CRM | $13.01 |
| Apps and software - office use | $650.90 |
| Databases and research | $52.04 |
| Advertising and marketing | $133.54 |
| Travel - airfare/fare | $27.50 |
| Travel - car/shared rides | $383.99 |
| Travel - meals and entertainment | $1,510.87 |
| Travel - vehicle gas | $0.00 |
| Professional fees / consulting | $1,000.00 |
| Bank fees | $0.41 |

## Variance Flags

1. Health insurance remains the largest YTD timing spike.
   - YTD actual: $36,286.91
   - YTD prorated budget: $16,500.00
   - Variance: +$19,786.91, or +119.92%
   - Assessment: timing and structure issue. The June amount is normalized at $2,750 and the big overage is from earlier installments.

2. Travel is still materially above the annual pace.
   - YTD actual: $16,140.82 across airfare, car/shared rides, meals, and gas
   - YTD prorated budget: $3,500.00
   - Variance: +$12,640.82, or +361.17%
   - Assessment: real overspend unless tightly tied to acquisition work. Meals and entertainment and car/shared rides are the loudest sub-lines.

3. Software and office-use spend is still elevated.
   - YTD actual: $5,839.48 in apps and software
   - YTD prorated budget: $3,600.00
   - Variance: +$2,239.48, or +62.21%
   - Assessment: structural cleanup candidate. Office-use software is the primary issue, not CRM.

4. Advertising and marketing is above the approved run-rate.
   - YTD actual: $3,020.63
   - YTD prorated budget: $500.00
   - Variance: +$2,520.63, or +504.13%
   - Assessment: not huge in absolute dollars, but still well above the approved pace.

5. Accounting / CPA remains an expected one-time annual hit.
   - YTD actual: $5,111.25
   - YTD prorated budget: $1,600.00
   - Variance: +$3,511.25, or +219.45%
   - Assessment: timing issue from February filing and May consulting. Do not annualize this into the forward run-rate.

6. Aggregate monthly expenses remain above prorated budget.
   - YTD actual: $177,721.34
   - YTD prorated budget: $134,500.00
   - Variance: +$43,221.34, or +32.13%
   - Assessment: the combined effect of health installments, travel, software, marketing, and professional fees keeps the budget under pressure.

## Runway Analysis

Using the June 30 cash balance and the $40K DD reserve:

| Scenario | Result |
|----------|--------|
| Trailing average net burn | $29,129.09 |
| Trailing average runway | 3.51 months |
| Steady-state net burn | $20,100 |
| Steady-state runway | 5.09 months |
| Projected zero date | Dec 2, 2026 |
| Target cash date | Feb 1, 2027 |
| Gap to target | 1.91 months |
| Monthly savings needed to hit target | $5,496.51 |

Interpretation:
- June confirms the health-installment spike has ended, but the fund still misses the February 2027 deadline at the current normalized burn after holding back the DD reserve.
- The cleanest gap-closers remain software cleanup, travel discipline, and the remaining bookkeeper transition savings.
- June is still not enough to get to the deadline cleanly; the normalized run-rate needs roughly $5.5K/month of additional savings or burn reduction.

## Action Items

1. Keep the steady-state burn assumption anchored to the current normalized run-rate and do not carry forward the health-installment spike.
2. Push harder on software cleanup and office-use consolidation; this is the clearest recurring savings lever.
3. Keep travel on an acquisition-only standard until the budget trend bends back down.
4. Treat the June close as the current baseline and watch whether July preserves the lower normalized run-rate.
5. Preserve the extraction note that June 2026 reporting included multiple P&L PDFs in the folder and a small owner-investments discrepancy in the balance sheet.

## Extraction Notes

- June 2026 folder contained monthly, quarterly, and generic Profit and Loss PDFs; the monthly file was selected for extraction.
- The selected P&L title is January 1-June 30, 2026 with monthly columns; values above use the JUN 2026 column only.
- The P&L uses the row label Travel Fare; it was mapped to the budget key travel_airfare.
- Balance sheet owner investments were $551,845.01, which is $20 above the budget context reference value. The extracted PDF value was preserved.
