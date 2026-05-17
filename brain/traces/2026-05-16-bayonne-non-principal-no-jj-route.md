---
schema_version: 1.1.0
date: 2026-05-16
type: trace
today: "[[notes/daily/2026-05-16]]"
task: Decide whether to route Bayonne Exterminating card to JJ-Call-Only
output: "[[context/session-decisions-2026-05-16]]"
had_human_override: true
tags: [date/2026-05-16, trace, topic/jj-routing, topic/heels-to-deals, pattern/non-principal-no-channel-route]
---

# Decision Trace: Blue-Collar Niche Card ≠ Automatic JJ Route

## Context
A pest-control card surfaced while processing Heels to Deals cards: Sandra Fernandez, Bayonne Exterminating — pest control is an active priority niche, blue-collar, normally JJ's lane. The card had no email and Sandra is "Customer Service & Sales." It was actually picked up at the NPMA NJ event, not Heels to Deals.

## Decisions

### Route Bayonne to JJ-Call-Only?
**AI proposed:** YES — pest control is an active niche + blue-collar = JJ's lane; we have the phone number.
**Chosen (Kay):** NO.
**Reasoning:** the contact is non-principal (Customer Service & Sales, not owner/decision-maker), no email, and the card's true provenance was a different event. Niche-fit + blue-collar does not by itself qualify a contact for the JJ call queue when the named contact is not a principal.
**Pattern:** #pattern/non-principal-no-channel-route

## Alternatives Considered
- Route to JJ anyway and let JJ ask for the owner (Kay rejected — wastes a JJ touch on a non-principal cold entry)
- Enrich for the owner's contact, then route (not pursued this session)

## Why This Trace Matters
The default heuristic "blue-collar + active niche → JJ-Call-Only" is strong enough that a future agent will apply it reflexively. Kay's override adds a gate: the named contact must be a principal/decision-maker before a niche card earns a channel route. A junior/admin contact at a niche-fit firm is not a routable target on its own.

## Key Insight
Channel-routing a niche-fit firm requires a principal-level named contact. Non-principal cards (CSR, sales, admin) do not auto-route to JJ even when the firm sits squarely in an active blue-collar niche.
