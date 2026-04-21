---
schema_version: 1.2.0
date: 2026-04-21
type: memo
status: draft
skill_origin: list-builder
kay_approved: null
kay_approval_date: null
people: []
companies: []
projects: []
tags: [date/2026-04-21, output, output/memo, status/draft, topic/apollo-enrichment, topic/industry-experience-network-scan, topic/attio-hygiene]
---

# Apollo Prioritized Bulk Enrichment — Step 1 Run Report

## Summary

**500 of 500-credit budget spent. 100% Apollo match rate. 492/500 (98.4%) written to Attio and verified. 8 write failures from Apollo enum mismatches left for retry post-May-2.** Industry-experience network scanning is now live across ~25% of Attio People.

## Population Picture (Attio People)

| Bucket | Count |
|---|---|
| Total People records | 1,825 |
| Already Apollo-enriched pre-run | 5 |
| Unmatchable (no LinkedIn, no email) | 16 |
| Tier 1 — `nurture_cadence` populated | 65 |
| Tier 2 — `relationship_type` populated | 2 |
| Tier 3 — `last_interaction` within 180d | 567 |
| Tier 4 — LinkedIn URL populated (no tier 1-3 signal) | 895 |
| Email-only, no tier qualification | 275 |
| **Total matchable in priority tiers 1-4** | **1,529** |

Nurture sub-breakdown (Tier 1, 65 records): Dormant 19, Occasionally 28, Quarterly 16, Monthly 2, Weekly 0. (Note: this diverges from relationship-manager's 51-record morning count; `nurture_cadence=Dormant` appears to have been counted separately by relationship-manager.)

## Enrichment Run

- **Queue size:** 500 (Tier 1: 65 + Tier 2: 2 + Tier 3: 433).
- **Credits burned:** 500 (2 in pre-test, 498 in main run).
- **Credits remaining until May 2 reset:** 250.
- **Apollo match rate:** 500/500 = **100%**.
- **Rich employment_history (>=1 role):** 394/500 = 78.8%.
- **Empty employment_history (0 roles):** 106/500 = 21.2%. Consistent with the 20% empty rate observed in yesterday's 5-record test.
- **Role-depth distribution across matched:** 0 roles = 106, 1-3 = 205, 4-6 = 68, 7-10 = 73, 11+ = 48. Max observed = 24 roles. Average across all 500 matched = 3.7 roles (average excluding empty: 4.7 roles).
- **Match key breakdown:** LinkedIn URL = 132, Email = 360 (8 failed to write, still counted as matched). Email-matched records slightly over-represented because Tier 3 draws heavily from email-only history.

## Attio Write-Back

- **Write success:** 492/500 = 98.4%.
- **Post-write verify PASS:** 492/492 (every successful write confirms `nddl_apollo_enriched_at` is populated). 0 verify failures.
- **Write failures:** 8 records. All from two Apollo enum values not configured in Attio's select option lists:
  - `"product_mangement"` (sic, Apollo's typo) in `departments` — 4 records: Michael Fox, krutarthbshah, Jacob Rigos, Nonya Collier.
  - `"extrapolated"` in `email_status` — 4 records: Walker Deibel, Max Smith, Amy Murro, Tim Kostolansky.
- **Action item for Step 1b / future runs:** Add `"product_mangement"` to Attio's `nddl_apollo_departments` select options, and `"extrapolated"` to `nddl_apollo_email_status` select options. Then retry these 8 records (8 credits) in the Step 1b run after the May 2 reset. Cost today: 0 extra credits (stayed under the hard cap).

## Safety Log

- **Snapshot path:** `/tmp/apollo-bulk-enrichment-snapshot-20260420-183838.json` — pre-write state of all 500 records' `nddl_apollo_*` fields captured before any PATCH calls. Empty pre-state confirmed (no non-Apollo fields overwritten).
- **Queue path:** `/tmp/apollo-bulk-enrichment-queue-20260420-183323.json` (full population breakdown + ranked queue).
- **Results path:** `/tmp/apollo-bulk-enrichment-results-20260420-184116.json` (main run) + `/tmp/apollo-bulk-enrichment-results-20260420-184030.json` (2-record pre-test).
- **Hard cap enforced:** run halted exactly at 498 of 498-queue (+ 2 pre-test) = 500 credits.
- **No non-Apollo fields touched:** PATCH payloads contained only `nddl_apollo_*` slugs.
- **Apollo API key never echoed:** only referenced via `$APOLLO_API_KEY` env var.
- **Rate limit hits:** 0 (paced at ~0.5s/record, well under Apollo's 1000/min limit).

## Backlog for Step 1b (post-May-2 reset)

- **Unenriched matchable in priority tiers 1-4:** 1,529 total minus 500 enriched = **1,029 records remaining**.
- Tier 3 not fully drained (134 tier-3 records still in backlog, plus all 895 tier-4 records).
- Tier 4 is the big bucket — 895 records with LinkedIn URL but no nurture / relationship_type / recent interaction. Estimated cost at ~2,500/mo plan: full drain over ~1 calendar month of steady enrichment.
- **8 write-failure records** also go into the 1b queue once select options are added to Attio.
- **275 email-only records** with no tier qualification are low-signal but matchable; post-1b candidate pool only if network-scan coverage demands.

## Match Use-Case Confirmation

The prior test's hypothesis holds at scale: `nddl_apollo_employment_history` is a structured JSON array per record with `organization_name`, `title`, `start_date`, `end_date`, `current`. The 78.8% rich-history rate across 500 records means industry-experience network scanning can now tokenize `organization_name` across ~394 People and produce warm-intro-path candidates for any niche where prior employment at named companies is a signal. 106 empty-history records match Apollo's "person exists but LinkedIn work history sparse" pattern — LinkedIn CSV fallback remains the gap-fill option if coverage becomes material.

## Sample — 5 Enriched Records (redacted)

- **Tier 1 | A. Y.** — 4 past roles, example past: Stanford Graduate School of Business, Assistant Director, Center for Entrepreneurship.
- **Tier 1 | B. N.** — 6 past roles, example past: David Zwirner, Senior Director of Registration and Exhibitions.
- **Tier 1 | E. D.** — 5 past roles, example past: Dermatology Arts, Senior Medical Associate.
- **Tier 1 | H. H.** — 5 past roles, example past: Glasswing Ventures, Partner.
- **Tier 1 | J. B.** — 4 past roles, example past: MHS Licensing, Account & Retail Project Manager.

## Operational Surprises

1. **urllib + Cloudflare** — Python's default `urllib` User-Agent got Cloudflare-1010 blocked on Apollo. Fixed by shelling out to `curl` (the standard pattern used elsewhere in the repo). Worth memorializing in `memory-snapshot/reference_apollo.md` or equivalent.
2. **Python 3.14 ISO parser rejects nanoseconds** — Attio timestamps come with `.000000000Z` (9-digit fractional seconds), which `datetime.fromisoformat` silently fails on. Initial tier-3 count was 0 as a result. Truncation to 6 digits fixed it. Recommend codifying a `parse_attio_ts()` helper if more scripts query interaction fields.
3. **Apollo enum typos** — `"product_mangement"` is a persistent misspelling inside Apollo's data model (not a transient fluke); 4 of our 500 records hit it. Attio must carry that typo as a valid select option to round-trip cleanly.
4. **Tier 1 < relationship-manager count** — The Attio `nurture_cadence` field has only 65 populated records, whereas relationship-manager's morning scan reported ~51 actively-cadenced plus many "Dormant". The 65 matches Dormant+Occasionally+Quarterly+Monthly, so the scan is consistent; what differs is that relationship-manager treats Dormant as a separate bucket when summarizing.
5. **Tier 2 tiny (2 records)** — `relationship_type` is almost never populated in isolation; anyone with a relationship_type typically also has a nurture_cadence, which puts them in Tier 1. Consider whether Tier 2 should be merged into Tier 3 criteria in Step 1b.
6. **Unnamed records in queue** — 8 of the 500 queue entries had empty `name` but still had linkedin/email and matched successfully on Apollo. Worth a separate pass to back-fill Attio `name` from Apollo `first_name`/`last_name` (a 0-credit operation, just a field copy).

## Outcome

- **Published:** null
- **Engagement:** null
- **Hypothesis result:** confirmed (prioritized bulk enrichment is feasible within a 500-credit daily budget, match rates hold at scale, write-back is reliable modulo the 8 enum-mismatch edge cases).
