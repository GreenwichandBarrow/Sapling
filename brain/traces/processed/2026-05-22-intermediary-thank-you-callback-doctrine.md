---
review_status: applied
schema_version: 1.1.0
date: 2026-05-22
type: trace
task: Draft post-call thank-you to Sam Curcio (Transworld of NY) using canonical Intermediary Email Templates Doc THANK YOU variant
had_human_override: true
importance: high
target: claude-md
tags:
  - date/2026-05-22
  - trace
  - topic/intermediary-doctrine
  - topic/voice
  - topic/callback-doctrine
  - person/sam-curcio
  - pattern/no-parrot-counterparty-thesis
  - status/applied
---

# Decision Trace: Intermediary Thank-You {call_callback} — Don't Parrot

## Context

Drafting the post-call thank-you to Sam Curcio (sell-side broker, Transworld of NY) after the first warm-intro Zoom call on 2026-05-22. Pulled canonical THANK YOU template from `G&B Intermediary Email Templates` Doc and slot-filled `{call_callback}` with: *"Your framing on speed as the #1 differentiator, and the bid-process vs. open-process distinction, were both useful to hear."*

Kay rejected the speed mention: *"I don't think I like the speed mention."*

## Decisions

### {call_callback} swap — away from counterparty's central thesis

**AI proposed:** Echo Sam's central thesis (speed = #1 differentiator) back to him as the takeaway-of-the-call. The bid-process vs. open-process distinction was bundled with it.

**Chosen:** Replace with PE-saturation market read — *"Your read on where PE has saturated above $2M and where the real inefficiency still lives below was useful to hear."* (OR — light version with no specific callback if Kay prefers minimal surface.)

**Reasoning:** Three reasons the speed-callback was wrong:

1. **Parrot problem.** Sam hammered "speed is #1" through the call. Echoing it back positions Kay as the student receiving wisdom, not the peer comparing notes.
2. **Standing problem.** Sam himself said *"you're doing more than most people I meet"* — flagging speed as Kay's takeaway subtly undercuts that endorsement by signaling "this was news to me."
3. **Substance problem.** Process-mechanics callbacks (speed, bid dates, inquiry counts) signal Kay is learning the broker game; market-read callbacks (PE saturation lens, where inefficiency lives) signal Kay holds a peer-level view of the segment.

The PE-saturation alternative passes all three checks: substantive lens Kay can hold a view ON, not parroted from Sam's central thesis, and shows informed market awareness without leaning defensive. Sam made the PE-saturation point with conviction in the call but it was a market observation, not his central thesis — different category.

**Pattern:** #pattern/no-parrot-counterparty-thesis

## Learnings

- **Rule:** In intermediary (broker/IB/lawyer/CPA) post-call thank-you `{call_callback}` slot, do NOT echo the counterparty's own most-emphasized point as the takeaway. Pick a substantive market/structural observation where Kay holds a peer-level view, OR drop the callback entirely (lighter touch).
- **Test:** If the counterparty would recognize the callback as restating their own central pitch, it's a parrot. Swap it.
- **Why it matters:** Brokers signal-test buyers in first calls. The thank-you is the first written artifact post-call. Parroting their thesis is a low-confidence move; offering a peer-level lens is a high-confidence move. Same warmth, opposite standing.
- **Adjacent existing rule:** [[feedback-intermediary-buyer-interest-not-sentiment]] addresses sentiment vs. buyer-interest framing. THIS trace addresses *which substantive observation* to pick when the callback is buyer-interest-shaped. Different angle, same template, complementary.

## Why This Trace Matters

Future intermediary thank-yous (Megan Lawlor, James Emden, Krupa Shah, Sarah Rowell, any new broker) will face the same `{call_callback}` slot decision. Without this trace, default agent behavior is to grab whatever the counterparty repeated most — exactly the parrot trap. With this trace, the agent screens proposed callbacks against "is this their central thesis?" before drafting.

Codified as memory [[feedback-intermediary-callback-no-parrot]] and surfaced in the THANK YOU template's slot-fill guidance.
