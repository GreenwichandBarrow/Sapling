---
name: Post-call-analyzer fires per-call (not EOD digest); same-day OK, lag tolerated
description: Post-call-analyzer fires once per call as soon as content is available. Spec is "ideally right after the call, but lag is OK as long as it lands same day." NOT EOD digest. Granola's JSON cache flushes lazily; the skill catches up on the next poll once content lands.
type: feedback
originSessionId: aaa7fafb-587f-4eef-b828-ac937c5c9b99
---
Post-call-analyzer fires **once per call** when Granola content becomes detectable. NOT EOD digest. Same-day delivery is the goal; immediate is preferred but lag is acceptable.

**Why:** 2026-05-07 build session locked two decisions:
1. **No EOD digest** — Kay corrected the initial EOD recommendation. Trigger-driven cadence is the right fit because the trigger only fires when there's actual call content (volume naturally bounded by Kay's meeting load). Decision-fatigue rule applies to *unsolicited surfacing*, not *event-triggered notifications*.
2. **Lag is OK** — Granola encrypts its real-time cache (`cache-v6.json.enc`); the unencrypted JSON cache we can read flushes lazily, sometimes hours later. Kay's clarified spec (2026-05-07): "at some point that day. Ideally right after, but I'm ok with lag." Architecture: calendar-event-triggered polling + wait for Granola to flush + process when content available. Worst case: same-day, not real-time.

**How to apply:**
- Post-call-analyzer skill: launchd polls every 10 min; calendar-event gate exits silently unless an event with Kay just ended; once gated through, checks Granola cache; fires Claude only when populated content appears.
- One Slack message per call (action items, decisions, follow-up email drafts if applicable). Never aggregate across calls.
- Don't engineer for sub-minute latency. Don't decrypt the .enc file or reverse-engineer Granola's API just to shave the lag (rejected 2026-05-07 as not worth the brittleness).
- General rule: trigger-driven notifications (event arrives → fire) bypass the decision-fatigue digest framing.

**Future enhancement (not blocking):** if Granola releases a public API or stable webhook, switch the source-of-truth and tighten the lag. Until then, accept "same-day, not real-time."
