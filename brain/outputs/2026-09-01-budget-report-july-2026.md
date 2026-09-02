---
schema_version: 1.2.0
date: 2026-09-01
type: budget-report
status: final
skill_origin: budget-manager
kay_approved: null
kay_approval_date: null
people: ["[[entities/anthony-bacagan|Anthony Bacagan]]"]
companies: ["[[entities/greenwich-and-barrow|Greenwich & Barrow]]", "[[entities/startvirtual|StartVirtual]]"]
projects: []
hypothesis: null
trace: null
task_ref: null
published_url: null
tags:
  - date/2026-09-01
  - output
  - output/budget-report
  - status/final
  - person/anthony-bacagan
  - company/greenwich-and-barrow
  - company/startvirtual
  - topic/budget
  - topic/runway
  - topic/tech-stack
---

# July 2026 Budget Report

Source files are filed in the [[entities/startvirtual|StartVirtual]] monthly reporting folder for July 2026:

- Monthly P&L: `1a04434972f8b44a_ANGjdJ8I_G&B Monthly Profit and Loss - July 2026.pdf`
- Balance Sheet: `1a04434972f8b44a_ANGjdJ-d_G&B Balance Sheet - July 2026.pdf`
- July checking statement: `JUL 2026.pdf`

## Fund Position

| Metric | Value |
|---|---:|
| Fund balance / cash at July 31 | $119,203.22 |
| Checking | $3,571.82 |
| Savings | $115,631.40 |
| DD reserve held back | $40,000.00 |
| Available for operations | $79,203.22 |
| Percent of fund remaining | 21.60% |

The balance sheet cash total ties to checking plus savings. July actual burn also ties to the fund balance movement from June 30 to July 31.

## P&L Summary

July operating expenses were **$22,752.32**. Anthony's P&L also shows **$569.43** of other expenses below the operating subtotal and **$300.54** of interest income. For runway, use the full July net burn of **$23,021.21**, not the operating-expense-only burn.

Largest July spend areas:

| Category | July actual | Comment |
|---|---:|---|
| Regular wages | $12,692.32 | Normal payroll month, below monthly comp budget after June timing spike. |
| Payroll taxes | $970.97 | Normal. |
| Health insurance | $2,750.00 | At Kay's normalized forward level. |
| Advertising & marketing | $3,009.68 | Main issue; likely includes Payoneer $2,575.50. |
| Travel | $1,341.69 | Lower than June, still above smaller-event base. |
| Office rent | $1,000.00 | Stone Street, still active. |
| Business taxes/licenses | $1,322.00 | Timing item, not monthly base unless it repeats. |
| Professional fees/accounting | $247.00 | Looks like ongoing bookkeeping/classification, not annual CPA. |

## Variance Flags

- **Advertising & marketing is the main July variance.** July was $3,009.68 against an $83 monthly budget. The checking statement shows **Payoneer Inc. $2,575.50** on July 20, which Kay clarified is DealsX and reflected two months behind. Model DealsX as **$1,250/month** unless Sam reduces pricing; do not treat the full July catch-up as monthly base.
- **Linkt still charged $199.99 on July 1.** The dashboard had Linkt marked canceled. This should be verified and recovered or stopped.
- **OpenAI/ChatGPT is now a real run-rate issue.** July had **$217.75** after June also had elevated OpenAI/ChatGPT charges. This should stay in base run-rate until the plan is downgraded or usage is capped.
- **Travel remains high YTD.** July travel was $1,341.69, lower than June but still about $467 above the smaller-event monthly base of roughly $875.
- **Health is over budget YTD but normalized going forward.** The YTD variance is mostly timing/plan design; forward model uses $2,750/month.
- **CPA/accounting is over budget YTD but should not be annualized.** The annual/timing payments are real historical spend, but not evidence of a recurring monthly CPA run-rate.

## Runway Analysis

Recommended planning run-rate is **about $20.95K/month** after Kay clarified Payoneer is DealsX and chose to remove office rent from the forward plan.

That assumes:

- Payoneer/DealsX is recurring at $1,250/month unless the requested price reduction lands.
- Linkt is stopped/refunded and not in the go-forward base.
- Office rent is removed from the forward base once the lease break is effective.
- StartVirtual VA/cold-calling, Dodo/AI consultant, Superhuman, and BizBuySell paid membership remain absent.
- Health stays at $2,750/month.
- Travel returns to smaller, lower-cost events.
- OpenAI/ChatGPT remains at the July level until actively changed.
- Office rent is excluded once the lease break is effective; if Stone Street continues, add $1,000/month back.

| Scenario | Burn | Runway from Aug 1 | Cash-out timing |
|---|---:|---:|---|
| Recommended normalized case | ~$20.95K/mo | ~3.8 months | Late Nov 2026 |
| Risk case if office rent continues | ~$21.95K/mo | ~3.6 months | Mid/Late Nov 2026 |
| Target to reach Feb 2027 | ~$13.2K/mo | Needed | Requires ~$7.75K/mo savings |

The key point: the confirmed vendor cuts helped, but available operating cash is now down to $79.2K after the DD reserve. To preserve deal-cost capacity through February, the operating base has to come down materially or cash has to be supplemented.

## Tech Stack / Cancellation Review

Confirmed absent from July checking:

- StartVirtual VA/cold-calling service.
- Dodo Digital / AI consultant.
- Superhuman.
- BizBuySell paid membership.

Recurring or active July charges found:

| Vendor/tool | July cash charge | CFO read |
|---|---:|---|
| Linkt | $199.99 | Should not be active; verify cancellation/refund. |
| DealsX / Payoneer | $2,575.50 | July was two months behind; model forward at $1,250/month unless price reduction lands. |
| OpenAI/ChatGPT | $217.75 | High; cap or downgrade if not directly producing deal throughput. |
| Apollo | $64.24 | Keep if replacing Linkt and actively feeding target discovery. |
| QuickBooks | $41.37 | Keep until Kick/bookkeeper transition is complete. |
| SVTrueBookkeeping | $247.00 | Ongoing bookkeeping cost. |
| Stone Street rent | $1,000.00 | Remove from forward plan once lease break is effective; add back if timing slips. |
| Granola | $15.24 | Low cost, keep if it supports meeting notes. |
| Hetzner + foreign fee | $15.03 | Low cost core infrastructure. |
| Google One | $2.16 | Low cost. |
| Tailscale | $8.71 | Low cost core infrastructure. |
| Claude | $21.78 | Reasonable after downgrade. |
| DocSend | $15.59 | Downgraded; reasonable for investor sharing. |

## Action Items

1. **Continue DealsX price reduction discussion.** Current forward model assumes $1,250/month; any reduction drops directly into deal-cost capacity.
2. **Break/cancel the office lease and remove Stone Street from forward run-rate once effective.** This saves $1,000/month.
3. **Verify Linkt cancellation and request credit/reversal for $199.99.** It charged despite being marked canceled.
4. **Review OpenAI/ChatGPT plan and usage.** Current run-rate is $217.75/month; dropping to subscription-level use could save about $196/month.
5. **Hold travel to the smaller-event budget.** July was still about $467 above the forward base.
6. **Keep low-cost core tools unless workflow changes.** Apollo, QuickBooks, Google, 1Password/core infrastructure, Granola, Claude, and DocSend are not the main problem at current levels.

No emails were sent. Slack was not sent because external messages require explicit approval outside the automated monthly run context.


## September 1 Correction

Kay clarified that Payoneer is DealsX. The July **$2,575.50** charge represented two months behind, so the forward model should carry DealsX at **$1,250/month**, not treat Payoneer as an unknown one-time item. Kay also indicated she is moving to break/cancel the office lease, so the forward plan removes **$1,000/month** of Stone Street rent once effective.

Net effect versus the prior July-forward model: **+$250/month** to normalized burn, because DealsX adds back $1,250/month while office rent removes $1,000/month. Linkt remains excluded from base but needs cancellation/recovery because it still charged **$199.99** on July 1.

Revised normalized run-rate: **~$20.95K/month**. Available operating cash remains **$79,203.22** as of July 31 after the DD reserve, implying **~3.8 months** of runway from August 1 and a continued need for roughly **$7.75K/month** of additional savings or offset to comfortably reach February 2027.
