---
schema_version: 1.1.0
date: 2026-05-04
type: trace
title: "Private examples Kay shares as context for Claude are NOT public website copy"
trace_type: doctrine-establishment
tags: ["date/2026-05-04", "trace", "topic/website-revamp", "topic/voice-and-copy", "topic/private-vs-public-context"]
---

# Private examples Kay shares as context for Claude are NOT public website copy

## Trigger

During `/socrates` framing for the greenwichandbarrow.com rebuild, Kay surfaced two specific examples to illustrate the kind of business G&B values: (1) her local bagel shop that puts a little extra in the bag for her kids and leaves dog treats at the door, (2) a pest-control owner she met at NJPMA who donates to the local high school for prom. She also referenced William Hoffman's NJPMA speech ("Pest control is really a customer service business with a little exterminating thrown in").

I treated these as content fuel and put them directly into the website mockup: bagel-shop story embedded in the customer-service pillar, pest-mgmt-prom story in the community pillar, Hoffman quote as a pull-quote on the home page.

Kay's response: *"the content is so weird. I gave you those examples for your own context, not to be quotes on the website."*

## Decision

**Private examples Kay shares with Claude as conviction-builders are NOT public website copy.** They inform the voice and the underlying thesis, but they do not appear on the public site as quoted stories or attributed quotes.

The same principle applies to other content sources Claude treats as fuel:
- Granola transcripts of meetings Kay attended
- Phone calls / coaching sessions with industry figures
- Conversations Kay had with brokers, owners, advisors
- Personal anecdotes or family references

These are LENS, not CONTENT. They calibrate Claude's understanding so the voice rings true, but the public artifact (website, deliverable, broker email, one-pager) describes the world in general observational terms. The reader does not get to see Kay's private examples or learn her local NJ context.

## Alternatives Considered

**Option A: Use the private examples as content** — what I initially did. Felt grounded and concrete. Failed because (a) it leaked Kay's personal context to public readers (a broker or owner doesn't need to know about her bagel shop), (b) it tied the site to specific NJ examples that couldn't survive a niche pivot, (c) it read as too literal — like Claude was quoting Kay back at her.

**Option B: Paraphrase the examples without specifics** — strip the bagel shop down to "small businesses that notice what their customers care about" without the dog treats / kids-extras detail. **(Selected)** This preserves the texture of Kay's lens without surfacing her private context. The reader feels the observation but the example itself stays internal.

**Option C: Quote Hoffman with attribution** — initially I included this on the home page as a pull quote ("William Hoffman, NJPMA Workshop, April 2026"). Stripped after the same correction. Hoffman's framing is internal content fuel; the website does not credit him publicly.

## Reasoning

The framing question Claude asks at the start of every conversation is: "what is shared, what is withheld, what is for me, what is for the world?" Kay's lived examples sit in the for-me bucket. They tell Claude what kind of business to look for and what voice to write in. They do not sit in the for-the-world bucket.

The mistake was a category error: I treated a calibration signal as a deliverable input. Future agents working on G&B-facing artifacts (website copy, broker outreach, one-pagers, investor decks) need to keep these buckets separate.

## Why This Trace Matters

A future Claude inheriting only the framing brief at `brain/outputs/2026-05-04-discussion-website-revamp.md` would see the bagel-shop and pest-mgmt-prom examples in the "Concrete examples for site copy" section and almost certainly try to use them on the site. The brief itself was written under the same mistaken assumption. This trace overrides that and locks the new doctrine: examples in framing briefs are LENS, not CONTENT.

The same principle protects Kay across other workflows where Claude pulls from her conversational context (Granola transcripts, call notes, vault entities) and might surface that material publicly without realizing it crosses the private/public boundary.

## Key Insight

**LENS vs CONTENT.** Kay shares her texture so Claude understands the world. The public artifact describes the world. The texture stays inside.
