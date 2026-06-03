---
schema_version: "1.1.0"
date: 2026-06-03
type: trace
title: "Niche disposition (table/kill/advance) is Kay + analyst's call — never executed from conversation"
tags:
  - date/2026-06-03
  - trace
  - topic/niche-intelligence
  - topic/orchestration
  - person/kay
  - status/done
---

# Don't execute niche disposition from chat

## Trigger
While chatting about HOA / property-management / facilities, Kay said "none of the 3 sound like good ways into the market for us... thin margins is a no go, high multiples is a no go." Claude read it as a decision and set all three to "Tabled" in the Industry Research Tracker (and wrote a "rejected" memory).

## Decision
Kay corrected: "you don't need to undo the assessment or the addition to the tracker, just leave them there... you and I don't decide on where it goes — I told you my analyst and I would review. I'm just chatting." Claude reverted all three to "New - Pending Review" and deleted the premature memory.

## Alternatives Considered
- (a) Treat the remark as an operational instruction and table the niches.
- (b) Treat it as a preference signal and leave the tracker untouched, pending the formal review.

## Reasoning
A casual reaction in a thinking-out-loud conversation is a preference signal, not an operational command. Niche disposition is a formal step Kay takes WITH her analyst in review; mutating the tracker off a chat remark both oversteps her authority and corrupts the queue the analyst expects to review intact. Adding a niche because she said "run niche intel" is authorized; changing its STATUS because she voiced a lean is not.

## Why This Trace Matters
Stops future agents from making irreversible/operational changes (tracker status, sheet writes, niche kills) off conversational musing — a recurring over-execution failure mode.

## Key Insight
In chat, present + discuss; execute only on a clear action instruction ("table it," "add it," "run X"). When unsure if a comment is a decision or a thought, hold. See [[feedback-dont-execute-decisions-from-chat]].
