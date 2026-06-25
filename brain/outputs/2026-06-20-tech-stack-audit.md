---
schema_version: 1.2.0
date: 2026-06-20
type: tech-stack-audit
status: final
skill_origin: budget-manager
kay_approved: null
kay_approval_date: null
people: []
companies: ["[[entities/greenwich-and-barrow]]"]
projects: []
hypothesis: null
trace: null
task_ref: null
published_url: null
tags:
  - date/2026-06-20
  - output
  - output/tech-stack-audit
  - status/final
  - company/greenwich-and-barrow
  - topic/budget
  - topic/tech-stack
---

# Greenwich & Barrow Tech Stack Audit - June 20, 2026

Company: [[entities/greenwich-and-barrow|Greenwich & Barrow]]

## Executive Readout

The Budget Dashboard Tech Stack Inventory has been reconciled against the current budget plan, Anthony's May 2026 monthly report, and receipt evidence available from Gmail.

Anthony's reports are category-level, not vendor-level, so they cannot prove every subscription by name. They do show that May tech/research/marketing spend is materially higher than the old inventory total:

| Anthony May 2026 P&L category | May actual |
|---|---:|
| Apps & Software - CRM & Storage | $82.92 |
| Apps & Software - Office Use | $636.09 |
| Databases & Research | $1,235.86 |
| Advertising & Marketing | $89.19 |
| **Category total** | **$2,044.06** |

The inventory previously showed $1,062.65/month, but several rows were stale or internally inconsistent. The updated forward tech-stack run-rate is now **$407.50/month**, excluding the July pauses for DealsX and the AI consultant and removing Linkt because Kay confirmed it was canceled. This uses May checking-statement cash amounts where available.

## Confirmed Updates Made

| Tool | Status | Budget Dashboard treatment |
|---|---|---|
| Claude Code | DOWNGRADE | Changed from $217.75/mo to $17/mo effective June 27, 2026. May receipt confirms $217.75 through June 27. |
| DealsX / KeyReach | EXCLUDED FROM JULY / EMAIL WED | Month-to-month; forward run-rate is $0 beginning July. To Do added for June 24 to email pause confirmation. |
| AI Consultant / Dodo Digital | CONFIRMED STOPPED | Kay confirmed Dodo was removed and emailed; no further charges expected. May $1,000 charge remains historical. |
| 1Password | KEEP | Corrected from an implied $52/mo to $4.34/mo run-rate based on $52.13 annual May 21 receipt. |
| Apollo | KEEP | Filled annualized totals: $64.24/mo, $770.88/yr. |
| DocSend | KEEP / EVALUATE LATER | Filled annualized totals: $70/mo, $840/yr. |
| BizBuySell | DOWNGRADED FREE / MARKETPLACE | Kay downgraded BizBuySell to free on June 20. Apr/May $24.95 charges are historical; remove from forward run-rate and dashboard tech stack. |
| Tailscale | EVALUATE | Marked verify: sheet had $8.71/mo but notes said free tier. May receipt exists, so treat as paid until verified. |
| Linkt | CUT | Kay confirmed Linkt was canceled; removed from forward run-rate. |

## May Checking Statement Vendor Match

Source checked: `BOOKKEEPING / CHECKING / MAY 2026.pdf`. The savings statement for May did not show tech-stack or rent/vendor transactions. The Budget Dashboard was updated to use the May checking-statement cash amount where a vendor appeared in checking.

| Vendor on May checking statement | May cash amount | Inventory / budget treatment | Alignment |
|---|---:|---|---|
| GOOGLE*SVCSGREENWICHAN | $28.71 | Google Workspace | Updated to $28.71/mo cash run-rate. |
| APOLLO.IO | $64.24 | Apollo | Aligned exactly. |
| INTUIT *QBooks Online | $41.37 | QuickBooks | Updated to $41.37/mo cash run-rate. |
| DODO DIGITAL | $1,000.00 | AI Consultant / Dodo Digital | Corrected. This is the AI consultant charge, not Stone Street. Paused from July in the runway plan. |
| SUPERHUMAN | $43.55 | Superhuman | May cash charge exists; May 22 cancellation email confirms forward run-rate is $0. |
| GRANOLA INC | $15.24 | Granola | Updated to $15.24/mo cash run-rate. |
| PAYPAL *GOOGLE GOOGLE ONE | $2.16 | Google One / storage | Added as a separate row for now; can be folded into Google Workspace later. |
| 1PASSWORD | $52.13 | 1Password | Aligned as annual cash charge; corrected run-rate to $4.34/mo. |
| TAILSCALE US INC. | $8.71 | Tailscale | Aligned to paid row; prior "free tier" note was stale. |
| CLAUDE.AI SUBSCRIPTION | $217.75 | Claude Code | May charge aligned to old Max plan; forward run-rate corrected to $17/mo effective June 27. |
| OPENAI *CHATGPT SUBSCR | $21.73 | ChatGPT | Updated to $21.73/mo cash run-rate. |
| DROPBOX DOCSEND | $70.77 | DocSend | Updated to $70.77/mo cash run-rate. |
| BIZBUYSELL | $24.95 | BizBuySell | Charge observed on April 30 and May 30; Kay downgraded to free on June 20, so forward run-rate is $0. |

Stone Street Software did not appear in the May checking or savings statement text extraction because the rent cash timing falls outside May. April checking confirms Stone Street Sof Bill.com payments of $1,000 on April 1 and April 29. June email evidence confirms invoice 250186 for $1,000 due June 1 and a BILL payment scheduled for June 4; the confirmation says it will show on the bank statement as "Stone Street Sof BILL". Based on Kay's correction and this evidence, Stone Street should be treated as office rent, not tech stack or AI consulting.

## Remaining Alignment Gaps

1. **Anthony's P&L does not map vendors directly.** The monthly reports validate category totals, but not which vendor caused each charge. Vendor-level reconciliation still depends on receipts or QBO detail.
3. **Howie row is inconsistent.** Prior note says annual $120/yr ($10/mo), but the old inventory modeled $25/mo. I left the row as active/verify rather than silently reducing it.
4. **Attio row is inconsistent.** Prior note referenced $901.49/yr, but the modeled row is $69/mo or $828/yr. I left the modeled run-rate unchanged and marked renewal verification.
5. **Tailscale row is inconsistent.** Receipt evidence indicates a paid charge, while the old note said free tier. I kept the $8.71/mo charge and marked it verify.

## Recommendations

1. **CUT: Linkt** - Kay confirmed cancellation; forward run-rate is now **$488.22/mo**.
2. **KEEP: Apollo** - keep as primary list-building system while Linkt is being removed; it is cheaper and operationally integrated with Attio.
3. **DOWNGRADE: Claude Code** - already handled; keep the $17/mo plan unless coding-agent workload requires a temporary upgrade.
4. **DONE / FOLLOW-UP: DealsX / KeyReach** - excluded from July budget because it is month-to-month; To Do added for June 24 to email pause confirmation.
5. **DONE: AI Consultant / Dodo Digital** - Kay confirmed it was removed and emailed; do not count it in runway starting July.
6. **DONE: BizBuySell** - downgraded to free on June 20 and removed from forward run-rate; treat as marketplace access, not tech stack. **DONE: DocSend** downgraded to Personal at $15/mo, saving $55.77/mo vs the May charge.
7. **EVALUATE: Howie** - verify whether the paid tier is $25/mo or $10/mo annualized. Tailscale is now validated as paid from the May checking statement.

## Savings

Confirmed July changes already reflected in the runway plan:

| Change | Monthly impact |
|---|---:|
| Claude downgrade | $200.75 |
| DealsX summer pause | $1,000.00 |
| AI consultant pause | $1,000.00 |
| **Confirmed tech/service savings** | **$2,200.75/mo** |

Additional likely savings pending verification:

| Candidate | Monthly impact |
|---|---:|
| BizBuySell unexpected charge if stopped | $24.95 |
| DocSend downgrade savings | $55.77 |
| Tailscale / Howie paid-tier cleanup | up to $33.71 |

## Superhuman Cancellation Update

Gmail confirms a May 22, 2026 email from Superhuman with subject "Your Superhuman subscription has been canceled." The Budget Dashboard already models Superhuman at $0 forward run-rate. The May checking statement charge of $43.55 is historical cash timing only and does not affect the July-forward runway plan.

## Linkt Cancellation Update

Kay confirmed Linkt was canceled on June 20, 2026. The Budget Dashboard now removes Linkt from the forward run-rate, reducing tech-stack run-rate from $788.22/mo to $488.22/mo and reducing the runway plan burn from $17,238/mo to $16,938/mo starting July. Projected zero remains January 2027, but the additional monthly savings needed to fully bridge to February improves from $1,825/mo to $1,525/mo.

## BizBuySell Charge Flag

Kay stated BizBuySell should not be paid. Statement review shows a $24.95 BizBuySell debit on April 30 and another $24.95 debit on May 30, with no refund/reversal found in the April or May checking statements. Kay downgraded BizBuySell to the free membership on June 20. The Budget Dashboard now treats BizBuySell as `Downgraded free / marketplace absent OK`, removes it from forward run-rate, and removes it from the operational dashboard tech stack. The April/May $24.95 charges remain documented as historical cash timing until the June statement confirms the charge stopped.

## BizBuySell Free Downgrade Update

Kay downgraded BizBuySell to the free membership on June 20, 2026 and clarified it is marketplace access, not tech stack. The Budget Dashboard now shows BizBuySell as $0 forward run-rate with status `Downgraded free / marketplace absent OK`; the operational dashboard no longer lists BizBuySell. This lowers tech-stack run-rate from $488.22/mo to $463.27/mo and lowers the plan burn from $16,938/mo to $16,913/mo. Projected zero remains January 2027; additional monthly savings needed to fully bridge to February improves to $1,500/mo.

## Dodo and DealsX Confirmation Update

Kay confirmed Dodo Digital has been removed and emailed, with no further charges expected. DealsX / KeyReach remains excluded from the July budget because it is month-to-month; a To Do item was added for June 24, 2026 to email the pause confirmation. Follow-up verification remains statement-based: confirm no Dodo or DealsX charge appears in the June/July checking statements.

## DocSend Downgrade Update

Kay downgraded DocSend to the Personal plan on June 20, 2026 at $15/mo. The May checking statement showed the old Dropbox DocSend charge of $70.77. The Budget Dashboard now models DocSend at $15/mo forward run-rate, lowering tech-stack run-rate from $463.27/mo to $407.50/mo and lowering plan burn from $16,913/mo to $16,857/mo. Projected zero remains January 2027; additional monthly savings needed to fully bridge to February improves to $1,444/mo.

## Dashboard Cross-Validation

Validation rule added from the Linkt miss: any Budget Dashboard tech-stack row that is absent from the operational dashboard tech stack must be classified as either (1) active paid missing from dashboard, which is a correction required, or (2) budget-only absent OK, which must be canceled/paused and explicitly labeled.

Final cross-check result:

| Class | Items | Action |
|---|---|---|
| Active paid missing from dashboard | None | Clean. |
| Active paid added to dashboard | QuickBooks | Added to `dashboard/data/tech_stack.yaml` and marked dashboard-validated in the Budget Dashboard. |
| Budget-only absent OK | Linkt; Superhuman; AI Consultant / Dodo Digital; BizBuySell | Linkt and Superhuman are canceled; Dodo Digital is paused service-vendor spend; BizBuySell is free marketplace access, not tech stack. |
| Dashboard amount cleanup | DocSend; 1Password | Dashboard notes updated to $70.77/mo for DocSend and $52.13/yr ($4.34/mo) for 1Password. |

Post-check: no duplicate Budget Dashboard rows and no active paid budget item is absent from the operational dashboard tech stack.

## CFO View

The stack is now aligned to the May checking statement where vendor transactions appeared and directionally aligned with the budget plan: July forward run-rate excludes DealsX, Linkt, BizBuySell, and the Dodo Digital AI consultant charge, and includes DocSend Personal at $15/mo; Claude is corrected to the downgraded plan; and annualized rows are no longer materially overstating 1Password or understating Apollo/DocSend/BizBuySell.

The remaining problem is vendor-level proof for rows that do not appear in May checking. Anthony's report confirms the spend categories but not every exact vendor. The next best control is to use receipt/QBO detail for Howie, Attio, Squarespace, Slack, Canva, Google Voice, and Hetzner, then lock those rows as verified.
