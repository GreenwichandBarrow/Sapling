---
name: Deal-aggregator does not build or maintain lists of any kind
description: Deal-aggregator is pass-through review of already-formed, existing deals. It does not build blacklists, DNC lists, consolidator lists, or any other maintained reference list. If a teaser discloses an auto-reject criterion, reject. If it doesn't, flag per Data Availability Rule. No lists.
type: feedback
originSessionId: 848374e5-1268-4868-935b-ca7f12026b58
---
Deal-aggregator is a **pass-through**: existing, fully-formed deals come in, Kay reviews them, done. It does not build, maintain, or reference any list of its own.

**Do not propose or build:**
- DNC / Blacklist Master sheets (for consolidators, PE-owned platforms, already-acquired companies, or any other category)
- Source Catalogs that track "which sources feed which niche"
- Niche Coverage Maps that track "channels × niches coverage"
- Registration Unblock Queues
- Change Logs
- Any other multi-row maintained reference artifact

**The filter mechanism is simple:**
- Teaser discloses the auto-reject criterion (e.g., "owned by ALKEME") → reject
- Teaser does not disclose → Data Availability Rule: flag for review, continue scoring
- No list to maintain. No cross-reference to look up.

**Why:** 2026-04-21 — After proposing DNC Master / Source Catalog / Unblock Queue as "Deal Aggregator folder" scaffolding, Kay corrected: "You are experiencing scope creep again. We are not building a list. We are passing through deals that exist, that are fully formed, for review. We are not building a list. We do not have a do-not-call list. That is irrelevant." The temptation to build infrastructure for deal-aggregator comes from thinking like target-discovery (where lists are the work). Deal-aggregator is different — there are no lists because the incoming artifact is a deal, not a target.

**How to apply:** Before proposing any sheet / doc / artifact to support deal-aggregator, ask: "Is this a list of candidates, sources, exclusions, or statuses that needs to persist and be referenced on future runs?" If yes → wrong skill. Deal-aggregator's only persistent artifacts are (a) the three buy-box Drive docs, (b) the daily scan artifact, (c) the weekly performance row for Friday calibration, (d) the cross-day dedup fingerprint store (internal hygiene, never surfaced). Nothing else.
