---
name: Never fabricate status or state columns — verify or declare unverified
description: Status / state / registration / access columns on any sheet, doc, or deck must be backed by verification against an authoritative source (Gmail, Attio, web, tracker). Never infer status from narrative descriptions in SKILL.md or other docs. If verification is expensive, structure the column and spawn a subagent to populate; do not fabricate.
type: feedback
originSessionId: 848374e5-1268-4868-935b-ca7f12026b58
---
Never write a value into a status, state, registration, access, or any claim-about-the-world column without verification. Descriptions in SKILL.md, memory files, or prior session notes are NOT verification — they are narrative text that can be outdated, aspirational, or contextual. A sheet populated with inferred values reads as verified fact to the human reader; fabrication in those columns is high-leverage harm.

**Rules for populating status / state columns:**

1. **Identify the authoritative source for the field before writing.** Examples:
   - Registration / account state → Gmail search (thank-you-for-registering, welcome, digest emails, match alerts)
   - Email subscription state → Gmail search for sender domain in past 90 days
   - Relationship state → Attio nurture_cadence + last-interaction data
   - Niche status → Industry Research Tracker WEEKLY REVIEW tab
   - Source accessibility → actual HTTP fetch of the URL
   - Scan history → deal-aggregator scan artifacts

2. **If verification is quick (one tool call per row, or a batched query across rows)**, verify before writing and populate with verified values.

3. **If verification requires more than ~10-20 tool calls**, do not write fabricated or inferred values. Instead:
   - Write column headers and row structure
   - Tell Kay: "I'm spinning up an agent to verify and populate [column name]"
   - Spawn a subagent to do the verification work
   - Write only the values the subagent returned with evidence
   - Leave unverified cells blank or marked "Needs verification" if the subagent couldn't resolve them

4. **Unverified cells stay blank or marked "Needs verification" — never inferred, never fabricated.**

5. **High-risk column types:** status, state, last-scanned date, registration status, access level, active/inactive, any "when" or "who" claim. Treat these as factual claims, not metadata.

**Why:** 2026-04-21 — I built the Deal Aggregator Sourcing List and labeled 6 sources as "Pending G&B registration" based on narrative text in SKILL.md ("need Kay to register first"). Kay pointed out she's actually registered at Rejigg and receiving match emails. Gmail verification of the 8 sources showed 2 were mislabeled (Rejigg + BizBuySell already registered). Kay: "WHY would you label status' without checking — this is the type of thing that is NOT tolerable. How do we prevent this sub-standard level of work going forward? You can title a column and then tell me that you are spinning off an agent to complete the information within..." The failure was treating descriptive text in a skill file as authoritative status about the world.

**How to apply:** Before writing ANY value into a status/state/registration/access column on any sheet, doc, or deck, pause. Ask: "Do I have verification-grade evidence for this cell?" If yes → write. If no → either (a) run the verification now (Gmail, Attio, tracker, HTTP fetch), or (b) leave blank and declare a subagent-backed verification pass. The pattern Kay named — "title a column and then tell me you are spinning off an agent to complete the information" — is the standard operating procedure for any column requiring verification work.
