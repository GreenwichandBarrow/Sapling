---
schema_version: 1.2.0
date: 2026-07-12
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
  - date/2026-07-12
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

# June 2026 Budget Follow-Up: July-Forward Run-Rate

This follow-up translates the June 2026 budget work for [[entities/greenwich-and-barrow|Greenwich & Barrow]] into a forward-looking cash burn view. Source context: Anthony / [[entities/startvirtual|StartVirtual]] July 3 Management Report, June checking statement, live Budget Dashboard, and Tech Stack Inventory.

## CFO Summary

The July-forward normalized net burn is approximately **$20.1K/month**.

With **$142,224.43** fund balance at June 30 and a **$40,000 DD reserve**, available operating cash is **$102,224.43**. At the normalized burn rate, runway is **5.1 months from July 1**, which points to cash exhaustion around **December 2026**.

To carry operating cash to **February 2027**, the target burn is about **$14.6K/month**. That leaves an additional savings need of roughly **$5.5K/month**.

The confirmed **$2,040/month** savings from canceling StartVirtual VA and pausing the AI consultant are real and should stay in the July-forward plan, but they do not by themselves get the fund to February.

## Normalized Burn Bridge

| Item | Monthly impact |
|---|---:|
| June reported net burn | $26,034.59 |
| Normalize compensation / payroll timing vs monthly budget | -$2,496 |
| Remove StartVirtual VA from July onward | -$1,040 |
| Remove paused AI consultant from July onward | -$1,000 |
| Normalize travel to smaller-event base (~$875/month) | -$1,047 |
| Normalize software / marketing overlap to current stack | -$351 |
| July-forward normalized net burn | **~$20,100** |

Health insurance is already at the forward normalized level of **$2,750/month** in June, so no additional adjustment is needed there.

## One-Time / Timing Items vs Recurring Base

Treat these as timing or non-base items unless they repeat:

- Elevated conference travel since March. Kay has decided the larger expensive trips are not worth projecting forward; use smaller, lower-cost events as the base case.
- Payroll timing variance. June compensation ran above monthly budget, so the forward model normalizes to budgeted monthly compensation rather than annualizing June.
- CPA / accounting lumpiness. The apparent annual tax/accounting payments should not be annualized into monthly run-rate without new evidence.
- June OpenAI / ChatGPT usage spike. June checking showed **$426.70** in OpenAI / ChatGPT-related charges. The forward model assumes normal subscription-level use, but this needs July monitoring.

Treat these as recurring base items:

- Payroll, payroll taxes, and benefits.
- Health insurance at **$2,750/month**.
- Office rent at **$1,000/month** while Kay is holding that decision.
- Bookkeeping at the remaining StartVirtual bookkeeping charge level; the VA/cold-calling component is removed.
- Core tech stack at about **$416/month**, excluding the June OpenAI spike.
- Smaller-event travel base of roughly **$875/month**.

## Tech Stack Review

Forward recurring software is now approximately **$415.88/month**. The cleanups already made are meaningful: Linkt, Superhuman, DealsX / KeyReach, BizBuySell paid membership, Dodo Digital / AI consultant, and the higher DocSend plan are no longer in the forward base.

### Keep / Active

- Google Workspace, Google One, Google Voice: core operations.
- QuickBooks: accounting system of record unless replaced by Kick transition.
- Attio: CRM; still worth verifying annual renewal and actual payment.
- Apollo: list building; this is the replacement for Linkt.
- Slack, Granola, Canva, Squarespace, Howie: modest recurring tools, with Howie still worth verifying against usage and plan.
- Claude: downgraded; June bank charge was **$21.78**, so use actual cash charge until invoice proves lower.
- ChatGPT / OpenAI: keep subscription, but monitor usage charges tightly.
- Hetzner, Tailscale, 1Password: core infrastructure/security.
- DocSend: downgraded to **$15/month**, appropriate for occasional investor document sharing.

### Ended / Removed From July Base

- StartVirtual VA / cold-calling service: **-$1,040/month**.
- AI consultant / Dodo Digital: **-$1,000/month**.
- DealsX / KeyReach: **-$1,000/month** excluded from July base.
- Linkt: canceled, no longer in dashboard base.
- Superhuman: canceled, no longer in dashboard base.
- BizBuySell paid membership: downgraded to free; not treated as tech stack.
- DocSend higher plan: downgraded from higher-cost plan to **$15/month**.

### Watch Item

The only software item that could materially change the run-rate is OpenAI / ChatGPT usage. If the June **$426.70** repeats, add roughly **$400/month** to burn and treat it as a real operating cost. If it was transition/API experimentation, leave it out of base but set a billing alert or cap.

## Recommendation

Use **$20.1K/month** as the July-forward normalized net burn for CFO planning.

The budget dashboard has been updated to this model. The February bridge is not solved yet: even after the StartVirtual VA and AI consultant savings, the fund still needs about **$5.5K/month** in additional savings or equivalent offset to comfortably reach February 2027.

The next clean decision lever is still office rent at **$1,000/month**, but that only closes part of the gap. The larger planning question is whether to accept a December runway without new funds, reduce owner/operating burn more aggressively, or identify a capital / timing bridge.

No emails were sent.
