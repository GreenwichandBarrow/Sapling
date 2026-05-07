---
schema_version: 1.1.0
date: 2026-05-04
type: trace
title: "PE-vibe in owner-facing copy comes from we-centric claims, not from founder visibility"
trace_type: doctrine-establishment
tags: ["date/2026-05-04", "trace", "topic/website-revamp", "topic/voice-and-copy", "topic/anti-pe-positioning"]
---

# PE-vibe in owner-facing copy comes from we-centric claims, not from founder visibility

## Trigger

During /socrates framing, Kay said she wanted G&B to look anti-PE on the website and used Shoreham Partners as her reference: *"I think Shoreham sounds so family and community oriented that it doesn't feel PE. That's why I think without the CEO face works."* She tied the anti-PE feel to the absence of Amanda Neilson on Shoreham's site.

I pressure-tested the reasoning — anti-PE feel actually comes from Shoreham's COPY (warm, owner-anxiety-aware: "we know how hard it is...") and aesthetic, not from hiding the founder. A Kay-led site with the same warm copy would read equally non-PE. Kay heard the pushback and stuck with full Shoreham model anyway, for separate reasons (avoiding the searcher-amateur trigger).

Day 1 mockup shipped. Hero, three teasers, About page with mission + four commitments ("we hold for the long run / we don't run auctions / we respect the transition / we protect what already works"). Kay's reaction: *"It sounds like private equity."* Despite the firm-led / no-founder-on-site choice, the site STILL read PE.

## Decision

**The PE-vibe in owner-facing copy comes from the structure of the claims, not from founder visibility.** Specifically: "we [verb] X" claim patterns — "we hold long-term," "we don't run auctions," "we look for businesses that...," "built for owners not for exits" — read as PE marketing regardless of whether the firm has a founder on the site.

The fix is to flip the voice from CLAIM to OBSERVATION:
- PE register (claims): *"We hold for the long run. We don't run auctions. We respect the transition."*
- Anti-PE register (observations): *"Some businesses run on the kind of trust that takes decades to build and only one bad transition to lose. The technical work is the cost of admission. The relationship is the moat."*

The site describes the kind of business and the kind of owner that fits. The reader recognizes themselves. The implication of "we'd be a good buyer" arises from the reader's recognition, not from the firm asserting it.

## Alternatives Considered

**Option A: Hide the founder, keep the we-centric claims** — what I built first, after Kay's "I want to not be on it" decision. Failed because the claims themselves are the PE-tell. Founder visibility is downstream.

**Option B: Strip the we-centric claims entirely** — write the site as third-person observation about service businesses, owners, and transitions. Use "we" only in the necessary places (firm identification, contact CTA). **(Selected)** This kills the PE register at the source.

**Option C: Keep the claims but soften with adjectives** — "we patiently hold for the long run / we humbly don't run auctions" — would still read PE, just sycophantic-PE. Rejected.

**Option D: Quote the firm's founder talking about the kind of business** — would let the owner-empathy come through a human voice. Mismatched with the no-founder-on-site decision.

## Reasoning

PE marketing copy has a recognizable rhythm: it lists what the firm does, what it doesn't do, who it's for, and what it promises. The structure is "we / we don't / for / not for." The reader picks up the structure subconsciously and codes the writer as PE regardless of how warm the words are.

Anti-PE copy refuses the structure. It describes the world (the kind of business, the kind of owner, the kind of transition) and lets the reader's recognition do the work. The firm gets identified at the bottom of the page, in the contact section, as the entity asking for the conversation.

This is closer to how individual operators talk about their work than how investment firms describe their funds. The Charter end-state Wertheimer archetype (`project_gb_charter`) sits behind this — an allocator who lets the operating businesses speak for themselves.

## Why This Trace Matters

A future Claude writing G&B-facing copy (website, broker outreach, one-pager, investor update) will default to the natural firm-marketing pattern: "we are a long-term holding company, we acquire one business at a time, we don't run auctions." That pattern triggers the PE association even when every individual word is non-PE. The override is to write OBSERVATIONS about the world G&B serves, not PROMISES about the firm.

The same principle applies to broker outreach (already partly captured in `feedback_no_search_fund_language_intermediaries`) and owner outreach (`feedback_outreach_about_them`). This trace generalizes the pattern to all owner-facing artifacts.

## Key Insight

**Observations beat claims.** A G&B-facing artifact that describes the kind of business and owner that fits will always feel less PE than one that describes what G&B does, no matter how warm the language is.
