---
schema_version: 1.2.0
date: 2026-04-16
type: trace
task: Draft LinkedIn DM to Bryan Cummings mentioning Lacey Wismer
had_human_override: true
importance: high
target: process
tags: ["date/2026-04-16", "trace", "pattern/contact-rule-scope", "domain/outreach"]
---

# Decision Trace: "Mentioning" vs "Re-engaging" — Scope of a No-Contact Rule

## Context

Kay confirmed earlier in the day: "IM NOT REENGAGING WITH LACEY, JUST A NOTE IS FINE." Later, when drafting LinkedIn DMs to ACG NY DealSource attendees, Bryan Cummings's mutual connection was Lacey Wismer. Question: does mentioning Lacey's name in a DM to Bryan violate the no-Lacey rule?

## Decisions

### Rule Scope Interpretation

**AI proposed:** Possibly remove Lacey's name from the Bryan DM to be safe, or park the Bryan DM entirely.

**Chosen (by Kay):** Mentioning Lacey's name in a DM to Bryan is within the rule. The rule prohibits *outreach to Lacey* (contact, re-engagement, asking her for anything). It does not prohibit *using her name as social proof* in a third-party DM where Lacey never sees the message and is never contacted.

**Reasoning:** The no-Lacey rule is about protecting Kay's boundary with Lacey (no re-entering that relationship), not about suppressing Lacey from the world. Bryan can verify the connection on LinkedIn himself. Lacey is never asked to do anything. The downside of over-enforcement (losing the Bryan warm-connection signal, weakening the DM) is real, and the rule's actual purpose isn't served by it.

**Pattern:** #pattern/contact-rule-scope

## Learnings

- **A "no contact" rule has a specific scope** — it bans reaching out, not using the person as a reference/connection signal to third parties. When the rule's purpose is relationship-boundary protection, mentioning is distinct from contacting.
- **Future agents must clarify the scope of no-contact rules** when edge cases arise (mentioning, CC'ing, forwarding about, recommending to someone else). Default to asking Kay rather than over-enforcing or under-enforcing.
- **The underlying principle:** protect Kay's intent, not just the literal rule. The intent here is "I don't want to be in a relationship with Lacey." Mentioning her name to Bryan doesn't violate that intent; contacting her does.

## Targets for Calibration

- **Memory:** Add to `feedback_never_reask_decided` or create a new memory entry about no-contact rule scope interpretation.
- **outreach-manager skill:** When a draft references a person who's on a no-contact list, check whether the reference is "mentioning for social proof" (allowed) vs "contacting" (blocked), and flag for Kay if ambiguous.
