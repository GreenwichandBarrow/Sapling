---
schema_version: 1.1.0
date: 2026-04-21
type: trace
had_human_override: true
importance: high
target: process
tags: ["date/2026-04-21", "trace", "pattern/external-data-over-internal-scoring", "topic/niche-ranking", "topic/searcher-criteria"]
---

# Decision Trace: Niche Ranking Methodology Pivot

## Context

Kay asked for a ranking of 8 active acquisition niches to identify a primary vehicle under an acquisition-timeline stress-test. Claude ran two ranking passes back-to-back.

## Decisions

### First-pass ranking (REJECTED)
**AI proposed:** 4-dimension lens combining warm-network depth, tri-state target density, PE competition, differentiation fit. Scored using river-guide-builder outputs + vault scorecards + session decisions. Ranked Private Art Advisory primary, Art Storage backup.
**Kay's response:** "I think your analysis is full of holes and fluff."
**Reasoning for rejection:** Ranking leaned on internal vault data that was itself thin (river-guide Phase 1 outputs had failed to land on target-list sheets, Apollo enrichment incomplete on Pest, Phase 3 Network Matches thin-yield investigation unresolved). Internal-data weakness propagated into the rank in ways that didn't reflect actual niche attractiveness.

### Second-pass ranking (ACCEPTED)
**AI proposed:** Traditional ETA searcher criteria only — 9 dimensions scored on external data (IBISWorld, MarshBerry, Capstone, Stanford search-fund study, industry M&A reports). Luxury-fit applied as final multiplier, not primary scoring dimension. Zero internal vault data used. Scored Specialty Insurance (HNW) primary, Premium Pest backup.
**Kay's response:** "This list resonates with me much better than the first pass. I agree."
**Pattern:** #pattern/external-data-over-internal-scoring

## Learnings

- When ranking niches, strategic positions, or market opportunities under time-pressure decisions, external market data beats internal scoring outputs — especially when internal data is known to be thin.
- "Warm network depth" is about the person running the search, not about niche attractiveness. Don't mix them as ranking dimensions.
- Luxury credibility is applied correctly as a final weighting factor (0.9/1.0/1.1/1.2), not as a primary dimension. Most niches are neutral on this axis.
- Codified as `feedback_niche_ranking_searcher_criteria_only.md`. Future ranking requests default to external-data methodology.
- Kay's "fluff" callout is a signal to check whether an analysis rests on inferred or incomplete data that's been papered over with confidence language.
