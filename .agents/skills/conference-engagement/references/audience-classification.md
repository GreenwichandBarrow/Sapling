# Audience Classification — Post-Conference Cards

## Three Buckets (per `feedback_audience_taxonomy_conferences`)

Never create a fourth "advisor" bucket. Advisors are intermediaries.

### Intermediary
Anyone who advises business owners and can refer deal flow.

**Firm/role signals:**
- M&A advisor, corporate advisor, investment banker
- Wealth manager, private wealth, family office advisor (client-facing)
- Exit planner (XPX-style)
- CPA / accounting firm partner serving private businesses
- Business attorney / M&A attorney / tax attorney
- Business broker, Main Street broker
- Lower-middle-market lender / commercial banker
- Insurance broker (for HNW / business insurance)
- Consultant to owner-operated businesses (ops, succession, value creation)

**Outreach pattern:** `postconf_intermediary` template. Buy-box paragraph included. Reciprocal value hook encouraged.

### Owner
Potential sellers — current operators of businesses that could be acquisition targets.

**Firm/role signals:**
- CEO / President / Owner / Founder of a private operating business
- Title explicitly says "Owner" or "Principal"
- Family-business second-generation operator
- Job title + LLC/Inc. + not a service/advisory firm

**Outreach pattern:** `postconf_owner` template. NO buy-box. NO ask. Curiosity only. Long-game relationship building.

**Flag for:** target-discovery pipeline if niche fits; warm-intro-finder for network cross-check.

### Peer / Ecosystem
Anyone who is neither a potential referrer nor a potential seller.

**Firm/role signals:**
- Other searchers (independent sponsors, search fund principals)
- Family office peers (investors, not advisors)
- Service providers to the M&A industry (software, data, diligence tools)
- Fellow LPs / capital partners
- Industry analysts, trade press, academic researchers

**Outreach pattern:** `postconf_peer` template. Simple stay-in-touch. No buy-box.

## Ambiguity Decision Tree

When a card is unclear:

1. **Do they personally meet with business owners as part of their job?**
   - Yes → Intermediary (they have direct owner access and can refer)
   - No → continue

2. **Do they own or run a business that could be an acquisition target?**
   - Yes (firm matches G&B buy-box: founder-owned, operationally critical B2B services, not PE-owned) → Owner
   - No → continue

3. **Default:** Peer / Ecosystem.

If still ambiguous after the tree, escalate to Kay with the card details. Do not draft.

## Edge Cases

**"Advisor" in title but actually a salesperson for a SaaS tool:**
- Peer, not Intermediary. They don't refer deals; they sell software.

**Partner at PE firm:**
- Peer. Potential co-invest or deal-share counterparty, but not a referral source for G&B-style deals.
- Never classify as Owner (PE-owned targets are a hard-stop per `feedback_no_pe_owned_targets`).

**Wealth manager who also happens to own a business:**
- Classify based on their card title / why they were at the conference. Default to Intermediary (their job is advising owners).

**Family member of an owner (e.g., spouse, child):**
- Owner bucket if they are involved in the business. Otherwise skip.

## Conference-Specific Priors

Different conferences have different audience mixes. Use this as a starting prior:

| Conference | Expected mix |
|-----------|--------------|
| XPX (Exit Planning Exchange) | ~85% Intermediary, ~10% Owner, ~5% Peer |
| ACG chapter events | ~70% Intermediary, ~20% Peer (other searchers/PE), ~10% Owner |
| Industry trade shows (e.g., NPMA for pest) | ~70% Owner, ~20% Vendor/Peer, ~10% Intermediary |
| Family office conferences | ~60% Peer, ~30% Intermediary, ~10% Owner |

Use the prior as a sanity check on the classification output. If XPX cards come back 60% Owner, something is miscalibrated — review before drafting.
