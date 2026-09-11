---
schema_version: 1.1.0
date: 2026-09-11
type: budget-report
status: review
skill_origin: budget-manager
kay_approved: null
people: ["[[entities/anthony-bacagan]]"]
companies: ["[[entities/greenwich-and-barrow]]", "[[entities/startvirtual]]", "[[entities/sidney-garber]]"]
projects: []
tags: [date/2026-09-11, output, output/budget-report, status/review, person/anthony-bacagan, company/greenwich-and-barrow, company/startvirtual, company/sidney-garber, topic/budget]
---

# August 2026 budget report

Automatic email-intelligence upstream trigger; reporting period **2026-08**. This is the CFO operating report for [[entities/greenwich-and-barrow|Greenwich & Barrow]]. Source reports are from [[entities/anthony-bacagan|Anthony Bacagan]] at [[entities/startvirtual|StartVirtual]]. No email was sent.

## Fund position

| Measure | Value |
|---|---:|
| August 31 bank cash | $97,777.71 |
| Fund remaining | 17.7183% |
| Current LOI reserve | $80,000.00 |
| Cash available for operations | $17,777.71 |
| August net burn | $21,425.51 |
| January–August net burn | $219,227.19 |
| Cumulative P&L spend since inception | $452,606.45 |

**Evidence:** August 31 balance sheet cash is the historical anchor. The September 11 pipeline snapshot records [[entities/sidney-garber|Sidney Garber]] at Submitted LOI since September 1, so the current reserve is $80,000 under [[context/budget|budget policy]]. The August cash figure has not been reduced by assumed September spending. Current-policy runway below is measured from September 1, not from today's date, and represents depletion of operating cash above the protected reserve, not total bank cash reaching zero.

The source balance sheet reports invested capital of $551,845.01 versus the established $551,825 reference, a $20.01 discrepancy. The dashboard's 17.7183% uses the source denominator; this does not revise the approved capital reference. Cash is anchored to the balance sheet: cumulative P&L burn omits $139.10 owner distribution and $1,321.75 fixed assets.

## Monthly P&L summary

| August item | Amount |
|---|---:|
| Regular wages | $12,692.32 |
| Payroll taxes | $970.96 |
| Health insurance | $2,750.00 |
| Rent | $2,000.00 |
| Bookkeeping | $247.00 |
| Operating expenses subtotal | $21,325.31 |
| Other expenses | $344.02 |
| Total expenses including other expenses | $21,669.33 |
| Interest income | $243.82 |
| Net burn | $21,425.51 |

Latest January–August source data restate historical dashboard classifications and stale YTD totals. June and July totals now include below-the-line expenses. Prior balance-sheet cash anchors are preserved. Approved-budget mapping puts CPA costs in Office Supplies & Bookkeeping and consulting provisionally in Reserve / Diligence; this classification does not establish that consulting was deal-specific. The dashboard upper-table operating estimates remain separate from the approved annual-category reconciliation at rows 42–54.

## Variance flags

Four categories exceed approved January–August prorated budgets by more than 10%. Positive variance dollars mean under budget; percentages below measure actual over budget.

| Category | YTD actual | YTD budget | Over budget | Explanation |
|---|---:|---:|---:|---|
| Payroll Taxes & Benefits | $51,099.85 | $6,666.67 | 666.50% | Structural unbudgeted health insurance plus front-loaded installments. Health YTD $41,786.91; normalize ongoing health to $2,750/month, never zero. Taxes/insurance alone $9,312.94 exceed $6,666.67 prorated budget. |
| Travel & Business Development | $18,488.04 | $6,666.67 | 177.32% | Structural YTD overspend with lumpy conference/trip timing; travel $18,488.04 already exceeds full-year $10,000 allocation. |
| Office Supplies & Bookkeeping | $15,573.90 | $9,333.33 | 66.86% | Mixed timing and structural: $3,200 CPA annual filing, $9,000 rent YTD, bookkeeping continues $247/month. Approved September lease cancellation is forward savings only. |
| Marketing, Software, Research | $17,328.53 | $10,666.67 | 62.45% | Mixed structural and timing: marketing includes prior DealsX catch-up; approved cancellations and pause are forward assumptions, not historical refunds. |

## Runway analysis

Historical normalized burn is **$24,523.38/month**: trailing January–August net burn averages $27,403.40; normalization removes $19,786.91 health front-loading above $2,750/month, $3,200 annual CPA filing, and $53.23 equipment, divided over eight months. Ongoing health remains $2,750/month. No unsupported contractor-onboarding deduction is taken.

**Model / inference:** scenarios assume the indicated burn continues and use September 1 as the anchor. February 1, 2027 is the inherited dashboard deadline convention; the policy names February without a day. These are reserve-protected operating-cash forecasts, not observed September balances.

| Scenario | Monthly burn | Operating cash | Months from September 1 | Projected reserve threshold |
|---|---:|---:|---:|---|
| Current trailing average | $27,403.40 | $17,777.71 | 0.6487 | 2026-09-20 |
| Steady-state historical normalized | $24,523.38 | $17,777.71 | 0.7249 | 2026-09-23 |
| Approved cuts forward model | $19,635.76 | $17,777.71 | 0.9054 | 2026-09-28 |
| Target to February 1 | $3,555.54 | $17,777.71 | 5.0000 | 2027-02-01 |
| August month-end reserve sensitivity | $24,523.38 | $57,777.71 | 2.3560 | 2026-11-12 |
| Approved cuts plus known commitments | $19,635.76 | $13,357.71 | 0.6803 | 2026-09-21 |

The approved-cuts forward model preserves the September 4 planning rate of **$19,635.76/month**, including approved rent/vendor cancellations and the pause after September. August actuals do not independently validate every saving. The historical normalized base is a separate scenario. The commitment sensitivity deducts $3,120 prior-dashboard payables and the $1,300 October conference; their outstanding status remains unverified. The requested $2,000 deposit is excluded until received. The $40,000 reserve sensitivity represents August month-end policy only.

At current reserve and historical normalized burn, the five-month funding shortfall to February 1 is **$104,839.19** and the required monthly savings are **$20,967.84**. The $3,555.54/month target is arithmetic, not an implemented plan. Prior September planning notes are retained below the new dashboard block and explicitly labeled historical/superseded.

## Action items

- **CFO judgment:** Review reserve-protected liquidity immediately: the historical-normalized model reaches the reserve threshold September 23, and the approved-cuts model September 28, both measured from August 31 cash. This report does not authorize reserve release or salary changes.
- Verify September cash movements, remaining payables, deposit receipt, and implementation of approved cuts before treating either forward scenario as a current bank forecast.
- Resolve the $20.01 capital-source discrepancy and confirm provisional consulting classification with the underlying ledger. No external email has been drafted or sent by this run.
- Use only dollar balance and percentage in investor updates. Internal investor fields remain synchronized with the dashboard; burn and runway stay internal.

Source evidence: [August monthly P&L](https://drive.google.com/file/d/18Nu16iBzgO01eDqeLKeE8N5ps2eUM22R/view), [January–August P&L](https://drive.google.com/file/d/1dCZBI4nFvzGEUOAxQT19KWM95c9bpsZl/view), [August balance sheet](https://drive.google.com/file/d/1H13RNVROBNNIOwNBJZ-3PHHdqB77CYKQ/view), and [live Budget Dashboard](https://docs.google.com/spreadsheets/d/1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0/edit). Durable source PDFs, extraction, reconciled metrics, live verification, and stop-hook manifest are stored in `brain/context/budget-manager/2026-08/`; reserve evidence comes from `brain/context/attio-pipeline-snapshot.json` fetched September 11. See [[context/budget|approved budget and COA crosswalk]].
