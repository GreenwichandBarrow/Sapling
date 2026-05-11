---
name: Deal-aggregator scope is prepped deals only
description: Deal-aggregator's single job is to find deals where the owner has already decided to sell (listed, teased, announced for-sale, or actively under sell-side mandate). Target-seeding lists, member directories, warm-intro networks, and market intel belong in other skills.
type: feedback
originSessionId: 848374e5-1268-4868-935b-ca7f12026b58
---
Deal-aggregator aggregates **existing, prepped deals** — businesses whose owner has already decided to sell and whose deal is listed, teased, announced, or actively in a sell-side mandate. That is its only job.

**In scope (deal-aggregator sources):**
- Broker-platform listings (BizBuySell, Empire Flippers, Business Exits, Synergy BB, Flippa, Quiet Light, etc.)
- Industry-specialist advisors' active sell-side mandates (Cetane live listings, DealForce buyer platform)
- Searchfunder member deal digest
- Email-inbound CIMs, broker blasts, NDA follow-ups
- Association *classified / for-sale / transitions* sections — where member owners have posted "I want to sell"
- AI-powered marketplaces (Acquire, BizScout, Kumo, Rejigg — all listing-based)
- Press releases announcing a specific company *actively for sale* (not post-close)

**Out of scope — belongs elsewhere:**
- Target seed lists (IIABA 349-agency Best Practices list, NPMA/IREM/NARPM member directories, conference attendee lists, Apollo pulls) → **DealsX / target-discovery** — but note target-discovery is PAUSED as of 2026-04-21 (see `feedback_target_discovery_paused.md`); DealsX owns this end-to-end right now
- River guides and warm-intro networks → **river-guide-builder**
- Blacklists / consolidator platform company lists (Anticimex platforms, etc.) → **DNC / Blacklist Master** (consumed by outreach-manager + JJ)
- Post-close announcements, completed transactions, consolidator tombstones → **niche-intelligence** (market intel)
- Educational / thesis content (IIABA perpetuation hub, MarshBerry insights reports, Reagan RedZone podcast) → **thesis docs / niche research**
- Cold outreach drafting → **outreach-manager** (for lists that already exist; net-new target outreach is handled by DealsX)

**Why:** 2026-04-21 — during deal-aggregator buildout I repeatedly pushed target-seeding sources (IIABA 349-agency list, association member directories) into deal-aggregator. Kay corrected: "The intention of the deal aggregator is to aggregate deals. This is not a cold outreach or target list building skill. You are only searching and scraping all these sites and references for existing deals. That means these are defined deals where the owner has already engaged to be selling his business."

**How to apply:** Before adding any source to the deal-aggregator Source Catalog (or recommending it as a deal-aggregator improvement), ask: "Is this source a list of deals the owner has already decided to sell?" If yes, add to deal-aggregator. If no, route to the correct skill: target-discovery (seed lists), niche-intelligence (intel), outreach-manager (drafts), river-guide-builder (warm paths), DNC master (blacklists).
