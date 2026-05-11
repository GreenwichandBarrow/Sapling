---
name: Apollo enrichment state (Attio People)
description: Current state of Apollo enrichment coverage on Attio People — 2026-04-20 snapshot after 500-credit prioritized bulk run
type: project
originSessionId: 4d4166cd-0bb3-4a20-887c-1f29801ff285
---
**As of 2026-04-20:**

- **Total Attio People records:** 1,825
- **Apollo-enriched (nddl_apollo_person_id populated):** 497
- **With non-empty employment_history (scannable for network matches):** 388
- **Empty employment_history (Apollo person exists but work history sparse):** 106 of 500 recently matched = ~21%
- **Write failures from today's run:** 8 records (4 × `product_mangement` department, 4 × `extrapolated` email_status) — **UNBLOCKED 2026-04-20 evening** via Attio schema patch, ready for retry after 2026-05-02 credit reset.
- **Apollo credits remaining this month:** 250 (of 2,520 base + today's 500 spent).
- **Credit reset:** 2026-05-02.

**Backlog for Step 1b (2026-05-03 onward):**
- 1,029 matchable records remaining in priority tiers 1-4 (mostly 895 Tier-4 LinkedIn-only).
- 8 retry records from today's write failures.
- 275 email-only records (lowest priority, only if needed).

**Why:** G&B needs industry-experience matching across Kay's network to find warm-intro paths to acquisition targets. Apollo `nddl_apollo_employment_history` field is the primary data source for river-guide-builder Phase 3. Coverage at 21% means 79% of Kay's Attio network is not yet scannable via Apollo employment history.

**How to apply:**
- **Phase 3 skill runs:** do not rely solely on Attio employment_history. Spec lists 4 data sources (Attio employment history → LinkedIn CSV → Attio standard fields → vault → Gmail). All must be hit, especially while enrichment coverage is 21%.
- **When Kay asks about enrichment cost/plan:** 2,520 credits/month plan, full-population drain (~1,029 remaining) takes ~1 calendar month at steady pace — budget accordingly.
- **Report location:** [[outputs/2026-04-21-apollo-prioritized-enrichment-report]] has full breakdown of today's run including operational surprises (urllib Cloudflare trap, Python 3.14 ISO parser nanoseconds bug, Apollo enum typos).
