---
schema_version: 1.0.0
date: 2026-04-12
type: trace
title: "SaaS Filter (Jake + Adam) is a separate qualification gate, not a better scorecard"
tags: ["date/2026-04-12", "trace", "topic/niche-selection", "topic/vertical-saas", "topic/saas-filter"]
target: skill:niche-intelligence
---

### Filter and scorecard serve different purposes and must both run in order
**Reasoning:** After scoring 5 Specialty Healthcare PM/EHR sub-niches at 2.24-2.51 (below Kay's existing actives at 2.60-2.81), instinct was to rework the G&B industry scorecard to avoid under-scoring DealsX broad-industry niches. Wrong frame. Jake Stoller's 7-dimension defensibility rubric + Adam's Datacor business-structure pattern REWARD the same structural features (PE-backed incumbents, consolidated top tier, long sales cycles) that the G&B scorecard PENALIZES (low Porter's score, low Size/Fragmentation score). Kay's insight: they're two different tools — filter is pass/fail qualification; scorecard is ranking among qualified. Fixing the scorecard would erase signal.
**Trigger:** For any SaaS niche, run the SaaS Filter (Jake + Adam) first. Niches that fail the filter do NOT proceed to one-pager or scorecard — don't waste work. Niches that pass go through the G&B scorecard for ranking. A 2.25 scorecard on a filter-pass SaaS niche is more interesting than a 2.57 on a filter-fail niche.

### SaaS Filter applies only to SaaS niches, blank for services/brokerage/distribution
**Reasoning:** Jake's 7 dimensions and Adam's Datacor structure are specifically vertical-SaaS criteria. Applying them to services businesses (Premium Pest Management, Art Advisory, Estate Management) or brokerage (Specialty Insurance) would produce false fails. Those niches run through Kay's existing G&B buy-box + scorecard path only.
**Trigger:** Classify each niche as SaaS or non-SaaS during identification. Only SaaS niches hit the SaaS Filter gate. Tracker column "SaaS Filter" is blank for non-SaaS niches — meaningful blank, not missing data.

## Learnings
- niche-intelligence: Step 2 (Identification) must tag each candidate as SaaS or non-SaaS + run SaaS Filter for SaaS niches before Step 3 (one-pager). Update skill to enforce.
- Industry Research Tracker: "SaaS Filter" column (Col M) + Reference tab documenting criteria. Non-SaaS niches stay blank.
- calibration-workflow: Track filter-pass rates and filter-pass-but-scorecard-low rates. If many SaaS niches pass filter and score low, that's expected — shouldn't trigger scorecard recalibration.
