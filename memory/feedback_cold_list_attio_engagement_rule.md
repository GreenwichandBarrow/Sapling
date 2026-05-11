---
name: Cold target list — Attio match alone is fine, prior email/call disqualifies
description: A company can stay on a "cold" target list (Intermediary Target List, owner target sheets, etc.) even if it has an Attio Company record — what disqualifies is PRIOR ENGAGEMENT (email or call). Cold list = no two-way history. Attio record without engagement is just data, not a relationship.
type: feedback
originSessionId: eadbe8c6-1597-404d-a31b-5cedebba7005
---
A target list is a COLD outreach list. The disqualifying signal is prior two-way engagement, not the existence of an Attio record.

**Rule (refined 2026-05-04 PM after Transworld + BDG-CPAs decisions):**

Engagement = **two-way correspondence**. Outbound email with no reply does NOT count as engagement; the contact is still cold and the row stays on the list.

- Attio Company record exists, ZERO prior email/call → KEEP (still cold)
- Attio Company record exists, **outbound-only with no reply** → KEEP (still cold; the ping went into the void, no relationship formed)
- Attio Company record exists, **inbound reply received OR call logged OR meeting held** → REMOVE (engaged; lives in Attio for relationship management)
- No Attio record → KEEP (obviously still cold)

**Concrete examples from the 5/4 broker-channel-build session:**
- Choate Hall & Stewart — strong two-way email thread that went stale 14 months ago → REMOVE (engagement existed, just dormant)
- BDG-CPAs — single Nov 2025 outbound, no reply → KEEP (one-way ping, no engagement)
- Transworld of NY (Sam Curcio) — single 4/30 outbound, no reply → KEEP (one-way ping, no engagement)
- Live Oak / Goodwin / Plexus / Heritage / Bellizio — active two-way threads with logged meetings → REMOVE

**Why:** Kay clarified on 2026-05-04 during the broker-channel build. An Attio Company record can come from many non-engagement sources — deal-aggregator broker detection, the (now-deleted) Outreach: Intermediary Pipeline list auto-creates, conference attendee imports, etc. The mere existence of the Attio record doesn't mean we've had a conversation. The point of a cold list is to track who we haven't engaged yet; engagement (sent email, taken a call) is the right boundary, not "is this name in our CRM."

**How to apply:**
- When validating any cold target list against Attio, classify each row by **two-way engagement**, not just record existence:
  - Pull the Attio Person/Company record
  - Check `interactions` / email-thread history (use `mcp__attio__get_record_interactions`)
  - Look for **inbound replies, calls logged, meetings held** — those count as engagement
  - **Outbound-only emails (no reply) do NOT count** — the contact is still cold
  - Has Attio record but only outbound-no-reply or zero interactions → KEEP on cold list
- For Apollo enrichment: cold-list rows that match the "Attio record but no engagement" bucket DO need enrichment (we lack contact data for them); rows with engagement don't (we already have email/phone from prior touchpoints).
- Validation artifacts that classify by "Attio match Y/N" without engagement detail are incomplete — they need the engagement-status overlay before driving any Sheet removals.

Source: 2026-05-04 broker-channel build, Kay corrected my Batch D framing. "Im ok to have companies on the intermediary target list that are in attio, but not ones that we have actually emailed with or had a call with prior. Thats the designation. this is supposed to be a 'cold' list outreach."
