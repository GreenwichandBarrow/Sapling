---
name: Outbound vendor pointers (TitanX, Handwrytten, Apollo job-postings)
description: Vendor reference for outbound stack evaluation. TitanX = phone propensity scoring, Handwrytten = robot-arm direct mail, Apollo job-postings = signal detection we pay for but don't use.
type: reference
originSessionId: 02a8f99b-e981-420b-a53a-8eb7191dc71e
---
Captured 2026-04-27 from AI Friday session review. None adopted yet — all under evaluation.

## TitanX (titanx.io)
- **What:** Phone Intent platform. Scores contact lists into P1/P2/P3/Bad Data tiers using a 1B+ observed-dial dataset.
- **Claimed lift:** Industry-baseline 3-7% connect rate → 20-30% with their scoring.
- **Architecture:** Sits *on top of* existing dialer (additive, not replacement). Submit list → get tiered list back → dial through current workflow.
- **Pricing:** Not public. Probably enterprise-tier ($1K-3K/mo minimums based on $27M Series A).
- **G&B fit caveat:** Their training data is heavy on tech/SaaS prospect lists. Heritage business owners (60-70 yo, may use landlines) are a distribution shift. Lift could be smaller than claimed. Worth a demo call before pilot, not a blind buy.
- **JJ math:** Current ~5% connect rate × 30-50 dials/day = ~2 connects/day. If TitanX delivers 25%, that's ~12 connects/day — 6x lift. But only if model holds for our list type.

## Handwrytten (handwrytten.com)
- **What:** Robot-arm handwritten direct mail. Phoenix AZ facility. JSON API, integrates with Make/Zapier/Salesforce.
- **Pricing:** $3.25/card start, bulk discounts. Custom handwriting font setup: $1,000 (block), $1,500 (cursive), $250 (signature). USPS first-class.
- **Pilot cost (10 targets, stock cursive):** ~$32.50 + $0 setup. With Kay's handwriting digitized: ~$1,532.50 one-time.
- **G&B fit:** Strong — luxury heritage businesses, owner-craft fit, pattern interrupt for owners who've ignored email + LinkedIn. Use as a "I emailed twice, wanted to try this instead" recovery pattern.

## Apollo job-postings endpoint
- **What:** Apollo (already paid for) exposes `latest_job_postings` and intent signals.
- **Status:** We pay for Apollo. We use it for company/contact discovery. **We do not use the job-postings endpoint.** This is the cheapest path to AI-Friday-style hiring-signal detection — already in stack.
- **Application:** Target hiring a CFO, COO, or "head of finance" = often pre-sale signal (owner cleaning up org chart pre-transition). Wire into target-discovery as a dynamic signal layer on top of the static G&B scorecard.
- **Alternative:** Clay ($800/mo) does this with prettier UI. Apollo is free for us.

## How to apply

- When evaluating phone/dialer tools for JJ → check against TitanX as benchmark.
- When designing pattern-interrupt sequences → consider Handwrytten as the "after email + LinkedIn fail" step.
- When extending target-discovery → use Apollo's job-postings before paying for Clay.
