---
schema_version: 1.1.0
date: 2026-04-20
type: trace
title: "Deal-aggregator source overhaul — the sources were wrong, not the niches"
had_human_override: true
importance: high
target: "skill:deal-aggregator"
tags: ["date/2026-04-20", "trace", "topic/deal-aggregator", "topic/sources", "pattern/fix-the-channel-not-the-thesis"]
---

# Deal-Aggregator Source Overhaul

## Context

Deal-aggregator was producing 5+ consecutive zero-match weekdays (4/14, 4/15, 4/16, 4/17, 4/20). The scan's own daily reports concluded "niches flow through private networks + specialist advisors, not public broker platforms" — framing the zero-match pattern as structural. I echoed that framing. Kay pushed back.

## Decisions

### Interpretation of zero-match pattern
**AI proposed:** Structural mismatch — Kay's niches (insurance, art, pest, estate, specialty SaaS) don't surface on public broker platforms. The channel is inherently wrong for these niches.

**Chosen:** It's not structural — it's source selection. Kay: "I think saying you can't find it on broker platforms is an excuse. If it's not working then we have to make it better. It's not the niches — it's where we are looking."

**Reasoning:** The old skill had 8 sources: Flippa, Empire Flippers, Website Closers, Business Exits, Synergy BB, Agency Checklists, Sica Fletcher (stale 2021), DealFlow Agent (not a listings board). Of those, 4 served the wrong segment (micro-SaaS / eCom / Amazon FBA), 1 was stale, 1 wasn't actually a listings site. The claim that "specialty niches don't flow publicly" was a rationalization for a bad source list.

**Pattern:** #pattern/fix-the-channel-not-the-thesis — if scans aren't producing, first audit source quality, don't conclude the thesis is unreachable.

### Scope of the overhaul
**Chosen:** Dispatch 3 parallel verification subagents to test ~50 proposed sources across industry-specific (6 niches) + general marketplaces + franchise networks. Tier each as Parseable / Needs-Workaround / Dead.

**Result:** 30 Tier 1 parseable sources, up from 8. Killed 10+ dead/mismatched sources. Added per-niche sector-specialist advisor transaction pages (Sica Fletcher rediscovered, MarshBerry, OPTIS, Dowling Hales, SEG, Shea, Tyton, GP Bullhound, Berkery Noyes, etc.) + RSS feeds (pctonline, mypmp, dailycoffeenews, baristamagazine, freshcup, theartnewspaper) + general marketplaces (BusinessBroker.net, Raincatcher, VR, Murphy, FCBB, Axial, Acquisitions Direct).

### Tier 2 handling for bot-blocked marketplaces
**Chosen:** BizBuySell / BizQuest / BusinessesForSale / Sunbelt / Transworld and similar 403 on WebFetch. Kay subscribes to their free email alerts; email-intelligence parses the digests; deal-aggregator reads the email-scan-results artifact. No scraper workaround needed for now.

**Reasoning:** Kay explicitly offered: "If you need email newsletters... let me know which offer them and I will register." Leveraging user-triggered subscriptions beats building JS-rendering infrastructure for sites that already offer the data via email.

### No priority tiering by niche status
**AI proposed:** Weight Active-Outreach niches higher than Active-Long Term for deal surfacing.

**Chosen:** **No priority tiering.** All Active-status niches scanned equally.

**Reasoning:** Kay: "For a lead/deal aggregator anything should NOT have lower priority. Either they come across a deal in that niche or not. period."

### Tracker-live-read requirement
**Chosen:** Skill must re-read Industry Research Tracker WEEKLY REVIEW each run. No cached niche list. If the tracker has stale entries, fix the tracker — not compensate in the scan.

**Reasoning:** Today's scan showed 15 niches. Kay was only actively running 6-8. The mismatch was tracker hygiene, not a scan design flaw. Fix the upstream source of truth.

### Weekly calibration cycle
**Chosen:** Every Friday, health-monitor / calibration-workflow reviews source-by-source yield. Drop non-producers after 2 consecutive zero-weeks, dispatch verification subagent to find replacements.

**Reasoning:** Sources drift. URLs move. Coverage needs continuous re-evaluation. Codified in `reference_deal_aggregator_calibration.md`.

## Learnings

- When a channel produces zero signal for N consecutive days, FIRST audit the channel's inventory quality (does it even serve the user's target segment?). Don't conclude the thesis is unreachable.
- "Structural mismatch" is an easy narrative to adopt when the real problem is source selection. Kay caught this immediately.
- Industry-specific sector advisors (MarshBerry for insurance, SEG for SaaS, PCT Online for pest) are a categorically different source class than general marketplaces — and usually better signal for specialty theses.
- RSS is underused — 6 of 30 Tier 1 sources have clean RSS. Prefer RSS over HTML scrape when available.
- When Kay offers to do user-triggered work (subscribe to newsletters), lean into it. It unlocks sources the scraper can't reach.
