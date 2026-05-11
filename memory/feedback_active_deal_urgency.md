---
name: Active deals get urgent treatment
description: Any inbound signal for a deal already in Active Deals pipeline (stages 3-9) should be flagged immediately, not wait for next morning's pipeline review
type: feedback
---

Active deals deserve faster response than standard pipeline cadence. When a CIM, financials, NDA response, or broker follow-up arrives for a deal already in Active Deals (First Conversation through LOI Signed), it should be surfaced the same day — not queued for the next morning's pipeline review.

**Why:** Brokers and intermediaries shop deals to multiple buyers. Speed signals seriousness. A CIM that sits in inbox over a weekend while other buyers are reviewing it is a competitive disadvantage. Project Restoration CIM arrived Friday evening — waiting until Monday means 2 lost days.

**How to apply:**
- Pipeline-manager's email ingestion should tag active-deal signals as `urgency: high`
- If an active-deal signal is detected mid-session, surface it immediately (don't wait for next session start)
- If detected during automated runs, send a Slack ping to #active-deals with the specific signal
- Standard pipeline review (morning briefing) still covers everything — this is an additional fast-path for active deals only
