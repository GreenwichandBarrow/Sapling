---
schema_version: 1.1.0
date: 2026-04-20
type: trace
title: "Conference-discovery: broker associations + LinkedIn; Twitter dropped"
had_human_override: true
importance: medium
target: "skill:conference-discovery"
tags: ["date/2026-04-20", "trace", "topic/conference-discovery", "topic/channels", "pattern/match-real-discovery-channel"]
---

# Conference-Discovery Channel Expansion

## Context

Kay reviewed today's Conference Pipeline after Sunday night's conference-discovery launchd run and noted: broker breakfasts / grass-roots intermediary events aren't surfacing. The skill HAS Priority 1 = intermediary networking (set 2026-04-15 via the Greg Donus / broker-breakfast unlock trace), but execution wasn't delivering.

## Decisions

### Priority 1 list expansion
**AI audit:** Current Priority 1 list had ACG, XPX, AM&AA, accounting/law firm events, wealth manager events, Capital Roundtable, NYIC. Missing: business broker associations specifically.

**Chosen:** Add to Priority 1:
- IBBA (International Business Brokers Association)
- M&A Source (as standalone, not subordinate to ACG)
- TMA (Turnaround Management Association) — intermediary-heavy
- State business broker associations (NYABB, NJBBA, NEBBA, Business Brokers of Pennsylvania, Long Island Business Brokers)

**Reasoning:** These are the associations Kay's target intermediaries actually attend. Missing from prior list because the 4/15 unlock trace focused on ACG/XPX-adjacent events, not IBBA/state-broker-orgs.

### Social-discovery channel
**AI proposed:** Add Twitter/X scraping alongside LinkedIn.

**Chosen:** LinkedIn only. Twitter explicitly excluded.

**Reasoning:**
- Twitter API is paid-only with free tier nearly useless for search
- Post-2023 Google/Bing indexing of Twitter is heavily throttled — web search against twitter.com URLs misses most recent posts
- Even if accessible: event announcements on Twitter are needle-in-haystack for SMB brokers (1/week among hundreds of unrelated posts)
- LinkedIn by contrast is high-signal: brokers + M&A advisors announce events regularly, public posts are Google-indexable via `site:linkedin.com/posts` queries, LinkedIn Events has its own indexable format

Kay confirmed: "ok lets do linkedin scraping. I can join newsletters."

**Pattern:** #pattern/match-real-discovery-channel — don't add channels because they sound useful; match the channel to where the actual signal lives.

### Informal broker breakfast caveat
**Chosen:** Truly grass-roots events (like the Long Island 7am diner rotation Greg Donus referenced) still won't surface even from LinkedIn when organizers don't post publicly. Three channels for these:
1. Newsletter subscriptions — Kay manages directly
2. Private LinkedIn Groups — Kay joins + forwards
3. Warm intros via river guides

Skill should flag these explicitly rather than pretending scrape coverage is complete.

### Cadence note
**Chosen:** Morning brief System Status line for conference-discovery is always terse: "ran, N added." No event-specific callouts (separate decision, saved as `feedback_briefing_conference_discovery_terse.md`).

**Reasoning:** The Conference Pipeline sheet is source of truth. Echoing its content in the brief is repetition Kay doesn't want. She's disciplined about using the sheet for review.

## Learnings

- Kay's preferred intermediary-networking channels were already documented (4/15 trace), but the SPECIFIC associations she wants weren't complete. Always revisit "what's on the explicit list?" when execution doesn't match intent.
- Social-discovery channels aren't interchangeable. LinkedIn and Twitter look similar but serve different signal densities for this user's domain. Evaluate each against the actual signal location.
- When a skill can't fully automate discovery (informal events via word-of-mouth), be explicit about the gap so the user doesn't assume coverage.
