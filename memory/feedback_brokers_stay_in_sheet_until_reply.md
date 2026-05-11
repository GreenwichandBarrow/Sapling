---
name: Brokers stay in target Google Sheet until reply
description: Broker / intermediary contacts live in the target Google Sheet — never bulk-add to Attio at "Identified" stage. Attio entry happens only after reply.
type: feedback
originSessionId: eadbe8c6-1597-404d-a31b-5cedebba7005
---
Broker (and broader intermediary) contacts stay in the target Google Sheet through the cold-outreach phase. **No Attio rows before they reply.** When a broker replies → that's the moment they become an Attio Person record (and a Company if needed).

**Why:** Kay deleted the "Outreach: Intermediary Pipeline" list intentionally. Cold-outreach pipelines belong in sheets, not the CRM. Attio is for relationship state — people we have a two-way thread with. Putting 50 cold contacts in Attio at "Identified" pollutes the CRM with noise that has zero engagement signal, makes nurture-cadence detection lie, and inflates "pipeline" metrics that aren't pipeline. The sheet already tracks 5/day send cadence, replies, and follow-up status; Attio adds nothing until there's a reply.

**How to apply:**
- Broker outreach pace = 5/day from the target Google Sheet. Drafting + send happen against the sheet, not Attio.
- Reply received → THEN create Attio Person (and Company) records, attach the email thread, set appropriate Pipeline stage.
- Same rule applies to lawyers, CPAs, IBs, family offices, association heads — any cold intermediary outreach. Sheet first, Attio after reply.
- Never propose "bulk-add to Attio Intermediary Pipeline" or any equivalent for cold lists. If I catch myself recommending it, stop.
- If the "Outreach: Intermediary Pipeline" list re-appears in Attio, it should be deleted (May 4 2026 cleanup).

Source: 2026-05-04 broker-channel build Day 1, Block 6 verification → Kay corrected my recommendation to bulk-add 50 PASS contacts. "We are emailing 5 per day, there is no reason to put in attio before anyone has replied. it stays in the target google sheet."
