---
schema_version: 1.2.0
date: 2026-05-04
type: discussion-brief
status: draft
skill_origin: socrates
kay_approved: null
kay_approval_date: null
people: []
companies: []
projects: []
tags: ["date/2026-05-04", "output", "output/discussion-brief", "status/draft", "topic/website-revamp", "topic/greenwich-and-barrow"]
---

# Discussion — Website Revamp

**Direction chosen:** Rebuild greenwichandbarrow.com as a Shoreham-style firm-led credibility site for intermediaries and owner-sellers. The principal does not appear on the site. Thesis: critical service businesses that engage their community, deliver exceptional customer service, and earn their customers' trust (Hoffman-register, niche-agnostic). Build path: HTML/CSS mockup off-platform, iterate to visual approval, translate to Squarespace at end of week. Live by Friday May 8 2026.

## Problem framing

Greenwich & Barrow hired a contractor 5 months ago to revamp greenwichandbarrow.com. Contractor never delivered anything visible. The engagement was terminated and the rebuild is being done with Claude instead. The current live site is 60-70% on-thesis but reflects an older luxury-only framing, names the principal as founder with LinkedIn linked (against current preference), and is missing the community pillar plus the customer-service-via-lived-example dimension that the principal wants to lead with.

## Goal hierarchy

- **Surface ask:** Revamp the website
- **Underlying goal:** Credibility-after-outreach signal for intermediaries and owner-sellers who Google G&B after receiving a G&B email. Site needs to be live by end of week to support a broker outreach push that begins today (5 emails/day, low volume).

## Audience (resolved)

Two co-equal audiences, both counterparty-not-LP:

1. **Intermediaries** (brokers, lawyers, IBs) who screen the firm before responding to outreach
2. **Owner-sellers** who Google G&B after a principal-or-JJ outreach email

Site is NOT for LPs, NOT a sourcing engine, NOT for talent recruiting.

Bar for both audiences: 30-second visit, decide whether to reply favorably. Threading the needle: brokers want legibility (real firm, real thesis), owners want warmth ("I could sell to these people"). Same copy serves both if it stays in the language already used in outreach (drop "fund / search fund / holding company / vehicle" per `feedback_no_search_fund_language_intermediaries`, no revenue or employee references per `feedback_no_revenue_in_outreach`).

## Structural decisions (resolved)

| Decision | Choice |
|----------|--------|
| Vehicle structure | CCV (Committed Capital Vehicle). Permanent capital language defensible. |
| Site anchor | Full Shoreham model. Principal not on the site at all. No name, no photo, no LinkedIn link, no About section. |
| Platform | Squarespace, no migration |
| Build path | Path 3: HTML/CSS mockup off-platform, iterate, translate to Squarespace at end of week |
| Mockup loop | Coded prototype + iterate (screenshot-analyze-improve cycles, principal reviews 1-2 hr/day) |
| Timeline | Live by Friday May 8 2026 |
| Decision rights | Principal alone |
| Maintenance | Principal (Squarespace UI for copy edits) + Claude (structural changes) |
| Logo | Existing wordmark is "basically a font" the principal made in-house. Open to discussion in execution. Likely path: refined typography treatment, no logo mark required. |
| Photography | Current site uses free stock that is rated as not great. `/plan` to budget for upgrade. |
| Contact | contact@greenwichandbarrow.com (existing, keep). Email-only contact, no form. |
| Insights cadence | 2-3 essays at launch, add more over time |

## Thesis (resolved, Hoffman-register, principal's voice)

**Critical service businesses that engage their community, deliver exceptional customer service, and earn their customers' trust.**

Three pillars:
1. **Engage their community** (Hoffman's NJPMA frame, plus the principal's lived experience)
2. **Exceptional customer service** (the bagel shop with the dog treats and the extras for the kids)
3. **Trust** (the through-line that holds it together)

Foundation pillar: **all critical**. The customer can't NOT have the service. They can only choose WHO provides it. And the choice is made on trust, not on price.

Threaded across the current niche set without forcing:
- Pest management = customer service business with a little bit of exterminating (Hoffman)
- Fine art storage = trust business with climate control
- Fine art and specialty insurance = trust business with paperwork
- Specialty coffee servicing = relationship business with wrenches
- Estate management = trust business with logistics

Site copy stays niche-agnostic so the thesis survives a niche pivot.

## Concrete examples for site copy

Two grounded examples surfaced during framing:

1. **Bagel shop** (consumer illustration of exceptional customer service): puts extras in the bag for the principal's kids, leaves dog treats at the door
2. **Pest management owner** (target-niche illustration of community engagement): donates to local high school for prom

Both belong in site copy. They do NOT belong in outreach. Outreach stays curiosity-first per `feedback_outreach_about_them`.

## Content engine (resolved)

**Insights section** repurposes / replaces the existing PERSPECTIVE section.

Niche-agnostic transition essays in Hoffman-register (not consulting voice). Topics drawn from Hoffman's NJPMA speech on success and succession plus the principal's own thinking. Initial 2-3 essays at launch, more added over time.

Topic candidates (final selection in execution):
- *What it feels like to sell the business you built*
- *The buyer matters more than the price*
- *Why we hold instead of flipping*
- *The 12-month transition: what actually makes it work*
- *Customer service is the real moat in service businesses*

**Primary content fuel:** Hoffman's NJPMA speech transcript (recorded on Granola during pest management meeting last week). Pull and extract topics as part of `/plan` or execution.

## Salvage from existing site

**Keep:**
- Hero line: *"A business built with trust / Deserves a thoughtful transition"* (Hoffman-register, exact alignment with new thesis)
- Phrases: "thoughtful stewardship," "steward it with care," "trust, discretion and long-term client relationships," "long-term acquisition"
- PERSPECTIVE section concept (becomes Insights container)
- Aesthetic direction: minimalist, muted palette
- Brand mark direction (typography-based)

**Discard:**
- Principal-as-founder visibility (currently named, LinkedIn linked)
- Luxury-only-tilt copy (*"excellence, discretion, enduring high-touch service"* needs widening to hold pest management and specialty coffee servicing alongside luxury-adjacent niches)
- Contractor's WIP (zero existed, nothing to evaluate)

## Aesthetic reference (resolved)

**Shoreham Partners** (shorehampartners.com): single-page modular scroll, anti-PE warmth, email-only contact, no portfolio shown, withhold institutional signals (no fund size, no team page, no portfolio companies). Adapted for G&B: industry-agnostic through-line replaces Shoreham's niche anchor (care).

## Alternatives considered

1. **Refresh existing site** (keep structure, edit copy). Tradeoff: faster, but anchored to existing structure and feels iterative not transformed. Rejected (visible reset preferred).
2. **Pure firm-led, full Shoreham model (SELECTED)**. Tradeoff: discards lived-experience differentiator, but sidesteps searcher-amateur trigger and matches stated preference for "background."
3. **Light-touch hybrid** (principal in section 2, not anchor). Initially proposed; later clarified to *"I want to not be on it"* and pushed to full Shoreham.
4. **Founder-led** (principal as anchor). Mismatched with stated aspiration to be in the background and with the Charter end-state (Wertheimer archetype, allocator hidden).
5. **Pause site copy until thesis settles**. Rejected: broker outreach this week makes the site a credibility dependency now.

## Assumptions surfaced

- **Anti-PE feel comes from copy and aesthetic, not from hiding the founder.** A founder-led site with the same warm copy would also avoid PE-vibe. The actual reason pure firm-led fits: avoids the searcher-amateur trigger (*"has she run my industry, what's her track record at scale"*). **LOAD-BEARING.** Informs why pure firm-led can work even though it sacrifices the lived-experience lever.
- **Squarespace constrains design quality somewhat.** Iterating coded mockups outside Squarespace and translating at end avoids the constraint during design but reintroduces it at translation time. May require template swap or heavy CSS injection. **NON-LOAD-BEARING for framing**, surfaces in `/plan`.
- **Brokers visiting the site mid-week see the OLD live site.** Outreach today at 5/day means low volume; risk that any broker visits twice (once now, once after Friday swap) is small. Worth accepting for parallel-tracks benefit. **NON-LOAD-BEARING.**
- **CCV structure permits permanent-capital language.** Confirmed during framing; supersedes the earlier (now-stale) `feedback_kay_ceo_deal_1_not_allocator` framing of Deal 1 as "search-fund traditional." **MEMORY UPDATE PENDING at goodnight.**

## Open questions / deferred to /plan

- **Layout exact** (single-page modular scroll confirmed; section count and order TBD)
- **Tech stack for mockup phase** (Vite + plain HTML, Astro, React, etc.)
- **Squarespace template selection or CSS-injection plan** for translation step
- **Photography sourcing path** (paid stock budget vs upgrade to better free sources)
- **Logo treatment specifics** (font choice, wordmark refinement)
- **Insights essay topics finalization + Hoffman transcript extraction**
- **Mockup-to-Squarespace translation process** (manual reconstruction, code injection, or theme override)
- **Iteration cadence** (daily standup-style, async screenshot review)

## Handoff

Ready for `/plan` with this brief as input. Plan should produce a 5-day execution sequence (Mon May 4 → Fri May 8) with daily milestones, mockup review checkpoints, and the Friday swap-to-live cutover.
