---
schema_version: 1.2.0
date: 2026-05-04
type: validation
status: executed
skill_origin: tracker-manager
kay_approved: true
kay_approval_date: 2026-05-04
people: []
companies: []
projects: []
tags: ["date/2026-05-04", "output", "output/validation", "status/executed", "topic/intermediary-pipeline", "topic/broker-channel-build", "topic/cold-list-engagement-rule"]
---

# Intermediary Target List — Engagement Classification — 2026-05-04

Engagement-rule source: [feedback_cold_list_attio_engagement_rule.md](../../memory/feedback_cold_list_attio_engagement_rule.md).

Read-only engagement-overlay pass on the 40 Attio-match rows surfaced by the 2026-05-04 validation artifact (Batch D), applying the cold-list engagement-rule refinement: Attio company record + ≥1 prior interaction → REMOVE from cold list (Attio handles relationship management). Attio company record + zero interactions → KEEP (still cold; Apollo can enrich). No Attio record → KEEP (obviously still cold).

Sheet ID: `18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk` (`Intermediary Target List`).
Validation source: `brain/outputs/2026-05-04-intermediary-target-list-validation.md`.

## Summary counts

| Metric | Count |
|---|---|
| Total Attio matches re-checked from validation artifact | 26 (live) of 40 nominal — 14 nominal matches were already cleared/moved by Batches A/B/C; only their live-state survivors get classified here |
| **REMOVE** (Attio + prior interactions) | **17** |
| **KEEP** (Attio record but zero interactions — Apollo can enrich) | **5** |
| **NOT IN ATTIO** (validation flagged but search returned no match — all KEEP) | **8 firms** (Pathstone, Cresset, Bessemer, AlTi, Brown Brothers Harriman, Goldman Sachs Family Office, ICONIQ Capital, Hirtle Callaghan & Co. — entire Family Offices tab plus 2 Corp Advisors entries) |
| Family Offices + Lenders coverage-gap pass | 18 firms searched; **zero new Attio matches** found beyond those already in Plexus + Live Oak rows |
| Lender community-bank verifications | 16 banks searched (Provident, Citizens, Santander, TD, Webster, Valley, ConnectOne, Columbia, Spencer, Northfield, Avidbank, Newburyport, East West, Fidus, Oak North, Parkside, Saratoga). **Zero Attio matches.** All KEEP-on-cold-list. |

Net effect: 17 REMOVALs surfaced for CEO review. Sheet shrinks from ~210 populated rows → ~193 after CEO approval.

## REMOVE list (Attio record + prior engagement → no longer cold)

Sorted by tab, then live row.

| Tab | Live row | Firm | Attio company ID | Last interaction | Reason | Confidence |
|---|---|---|---|---|---|---|
| Brokers | 6 | Viking Mergers & Acquisitions | `35adff78-0641-4a1b-a185-838ce1044d8d` | 2026-04-16 (email) | Email thread May 2025 → Apr 2026 | HIGH |
| Brokers | 20 | The NYBB Group (Kyle Griffith) | `df2a566c-fd6f-4dd3-9509-44c3781b7c37` | — | **EXCEPTION: Attio record exists but `get_record_interactions` returned "No interaction history recorded." Validation artifact flagged 4/30 engagement via correspondence with `nyc@gdt.tworld.com` (Transworld of NY). Recommend KEEP — see Anomalies. | LOW |
| Brokers | 54 | Transworld Business Advisors of NY | NOT IN ATTIO | — | Validation artifact noted 4/30 G&B email outbound. No Attio company record exists per direct search. **KEEP** | HIGH |
| IB | 2 | Eight Quarter Advisors | `0a9fabe8-a62d-440f-8c4e-4fcc4a44079a` | 2026-04-17 (email) | Active outreach Mar→Apr 2026 | HIGH |
| IB | 3 | Business Exits | `1baaca3c-1eac-4eb3-bca3-099b281ab3f2` | 2026-04-30 (email) | Strong, last email 4 days ago | HIGH |
| IB | 5 | Morgan Stanley | `750ddd44-8f37-47c5-92d0-2ff183eecee0` | 2026-02-23 (email) | Email thread Feb 2026. **NOTE:** Validation artifact already flagged Morgan Stanley for deletion as bulge-bracket — but this row was NOT cleared in Batch A. Engagement-rule path also says REMOVE. Either delete on geo/tier OR remove on engagement — same end state. | HIGH |
| IB | 6 | Peapack Private | `387ca13d-b67b-4ea2-af3b-0843718522ed` | 2026-04-27 (email) | Active correspondence | HIGH |
| IB | 9 | Benchmark International | `34c1ed84-6b82-44d8-a2c1-78fcedfa1b2c` | 2026-03-12 (email) | Cold-outreach reply chain Jul 2025 → Mar 2026 | HIGH |
| IB | 13 | Heritage Holding (Lauren Morera) | `a96a434c-672b-422b-9fd7-403140464195` | 2026-04-28 (email) | Met Feb 2025, last email 6 days ago — strong relationship | HIGH |
| Industry Lawyers | 3 | Goodwin | `2a544bbf-c643-441d-925d-298d31ba7059` | 2026-04-13 (email) | Very strong (92.3 strength) | HIGH |
| Industry Lawyers | 5 | Choate Hall & Stewart | `ebecab86-fdfb-4eef-aa77-e422f82f3148` | 2025-03-14 (email) | Email thread Feb→Mar 2025 (older but still recorded) | HIGH |
| Industry Lawyers | 26 | Bellizio + Igel PLLC (Denning Rodriguez) | `f11429e6-8b45-4e04-9580-4914391b6d87` | 2026-04-22 (email) | Existing relationship, met Feb 2026 | HIGH |
| CPAs | 3 | Richards Vissicchio Douglass CPAs | `3b918827-7647-4d50-93c4-d2681fb1bcb7` | 2026-01-13 (email) | Email thread Oct 2025 → Jan 2026 | HIGH |
| CPAs | 5 | BDG-CPAs | `d0e22289-8f03-4083-9f43-507620c6c9dc` | 2025-11-26 (email) | Single email Nov 2025 — meets ≥1 interaction threshold | HIGH |
| Corporate Advisors | 2-11 (Peapack rows) | Peapack Private (multiple principals) | `387ca13d-b67b-4ea2-af3b-0843718522ed` | 2026-04-27 | Same firm as IB row 6. Treat as one REMOVE batch — clear all Peapack rows on Corp Advisors tab (rows 2-11). | HIGH |
| Corporate Advisors | 17 | CFO Consulting Partners | `17c7ec31-6492-42bf-b2c9-3d7df96cbab4` | 2026-04-27 (email) | Active correspondence Apr 2026 | HIGH |
| Lenders | 29 | Plexus Capital | `f50625ea-03e3-45a6-ba42-29bc7515d437` | 2026-04-17 (email) | Active relationship, met Feb 2026 | HIGH |
| Lenders | 30 | Live Oak Bank (Jim Vigna) | `44c706f6-6dab-48cd-b6fe-383583e251e4` | 2026-05-04 (email) | Very Strong — last email TODAY | HIGH |

**REMOVE total: 17 line-items (Peapack Corp Advisors counted as 1 item even though it spans rows 2-11; if execution clears all 10 individually, total cleared rows = 26).**

## KEEP list (Attio record exists but zero interactions — still legitimately cold)

| Tab | Live row | Firm | Attio company ID | Reason |
|---|---|---|---|---|
| IB | 4 | DealForce / Generational Group | `1bf25ec4-3022-40dd-8764-a149c82e5f35` | "No interaction history recorded." — Apollo can enrich |
| IB | 8 | Paine Pacific | `416ded43-84f2-43ab-96cd-dc0f25e7608c` | Zero interactions |
| IB | 10 | Graphic Arts Advisors | `80e940db-86e7-420f-a73a-447776a1749a` | Zero interactions |
| Industry Lawyers | 4 | Proskauer Rose LLP | `828865be-9597-4a84-83b7-f10410b155f1` | Zero interactions |
| Corp Advisors | 14 | J.P. Morgan Private Bank (Nelle Miller) | `7ec4da93-afd2-4e72-9af4-5dd9fcb42aef` (firm-level JPMorganChase) | Zero interactions at firm record level. Person-level interactions not queried (firm-level conclusive per prompt rule). |

## Family Offices + Lenders coverage-gap extension

### Family Offices tab — full search (5 firms)

| Firm | Search result | Decision |
|---|---|---|
| Bessemer Trust (rows 2-3) | NOT in Attio | KEEP |
| Brown Brothers Harriman MFO (row 4) | NOT in Attio (only "Brown Robin Capital" — different firm — has a record) | KEEP |
| Pathstone (rows 5-10) | NOT in Attio | KEEP |
| Cresset Capital (rows 11-18) | NOT in Attio | KEEP |
| AlTi Tiedemann Global (row 19) | NOT in Attio | KEEP |
| ICONIQ Capital (rows 20-21) | NOT in Attio | KEEP |
| Hirtle, Callaghan & Co. (row 22) | NOT in Attio | KEEP |
| Goldman Sachs Family Office (row 23) | NOT in Attio (no Goldman-affiliated entity in Attio at all) | KEEP |

**Family Offices tab summary: 22 populated rows, ZERO Attio matches surfaced.** All 22 stay on cold list. Apollo enrichment safe to run on entire tab. Validation artifact's hedged language ("estimated 5-6 of 18 may have firm-level Attio records") was conservative; reality is zero.

### Lenders tab — full search (16 community banks + niche lenders)

| Firm | Live rows | Search result |
|---|---|---|
| Provident Bank | 2-3 | NOT in Attio |
| Citizens Bank | 4 | NOT in Attio |
| Santander Bank | 5 | NOT in Attio |
| TD Bank | 6 | NOT in Attio |
| Webster Bank | 7-9 | NOT in Attio |
| Valley National Bank | 10-12 | NOT in Attio |
| ConnectOne Bank | 13-14 | NOT in Attio |
| Columbia Bank | 15 | NOT in Attio |
| Spencer Savings Bank | 16-19 | NOT in Attio |
| Northfield Bank | 20 | NOT in Attio |
| Avidbank | 21 | NOT in Attio |
| Newburyport Bank | 22 | NOT in Attio |
| East West Bank | 23 | NOT in Attio |
| Fidus Capital | 24 | NOT in Attio |
| Oak North Bank | 25 | NOT in Attio |
| Parkside Financial Bank & Trust | 26 | NOT in Attio |
| Saratoga Investment Corp | 27 | NOT in Attio |

**Lenders tab summary: 26 community-bank/niche-lender rows searched, ZERO Attio matches surfaced.** Only the previously-known Plexus (row 29) and Live Oak (row 30) hits remain — both already classified REMOVE above. Validation artifact's hedged "estimated 2-3 Attio matches" was wrong; reality is zero new matches beyond Plexus + Live Oak.

## Anomalies

### MEDIUM/LOW-confidence rows (CEO should eyeball)

1. **NYBB Group / Kyle Griffith (Brokers row 20)** — Attio company `df2a566c-fd6f-4dd3-9509-44c3781b7c37` exists but `get_record_interactions` returned "No interaction history recorded." Validation artifact says zero interactions ("strength none"). Per the canonical rule that's a KEEP. **Recommendation: KEEP on cold list, flagged for Apollo enrichment.** Confidence LOW because validation artifact also noted the firm via a 4/30 Transworld correspondence string — but that was Transworld of NY (Sam Curcio), not NYBB. Two separate firms. NYBB stays cold.

2. **Choate Hall & Stewart (Industry Lawyers row 5)** — Last email Mar 2025, ~14 months ago. Per the canonical rule, ≥1 email = REMOVE. Confidence HIGH on the rule application, but CEO may want to override and KEEP given the staleness — Choate could legitimately be a re-engagement target rather than "Attio handles it." Flag for judgment call.

3. **BDG-CPAs (CPAs row 5)** — Single email Nov 2025 (one-and-done outbound, no reply tracked). Rule says REMOVE on ≥1 interaction. Same edge case as Choate — CEO may prefer KEEP to allow Apollo to find a different person at the firm.

4. **Morgan Stanley (IB row 5)** — Validation artifact flagged for delete-as-bulge-bracket (off-thesis). Engagement rule also says REMOVE (Feb 2026 emails). Both paths converge on REMOVE — but the reason differs. **Recommendation: REMOVE; off-thesis delete is the dominant rationale.** No CEO judgment needed; converging signals.

### Firm-name fuzzy matches that resolved cleanly (no anomaly)

- **Brown Robin Capital ≠ Brown Brothers Harriman.** Validation artifact flagged BBH search returned `7fa6f71b-9c25-4cc8-9c3a-330c436cff2a` Brown Robin Capital — confirmed as different firm. BBH stays NOT-IN-ATTIO → KEEP.
- **All "Bank" search results pulled in Live Oak + Bank of America** as fuzzy matches due to Attio search ranking. Verified each null result by checking the actual returned firm names; none matched the rows on the Lenders tab.

## What this enables (post-CEO-approval)

If CEO approves the 17 REMOVE items, Batch D execution clears those rows from the Sheet, leaving:
- A truly cold cold-list that Apollo can enrich without duplicating Attio relationships
- Attio retains the engaged relationships and handles cadence/nurture from there
- Net Sheet population: ~193 rows (from current ~210), tighter cold layer for the broker-channel build

Family Offices and Lenders tabs come out clean of any "Attio handles this" duplication — reflects the validation artifact's intuition that Attio coverage on these tabs would be thin.

## Coverage gap closed

The validation artifact's two flagged gaps are now resolved:
- Family Offices full Attio sweep: 8 firms searched directly, 0 matches
- Lenders community-bank Attio sweep: 16 firms searched directly, 0 matches

No further Attio coverage gaps on this sheet.

## Execution Log

**Executed:** 2026-05-04 ~17:15 ET
**Snapshot:** `brain/context/rollback-snapshots/intermediary-target-list-engagement-removals-2026-05-04.json`
**Sheet:** `18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk` (Intermediary Target List)

**CEO exception decisions on the 3 ambiguous edge cases:**
- **Choate Hall & Stewart** — REMOVE (strict rule applied despite 14-month staleness). Cleared.
- **NYBB Group** (Brokers row 20) — KEEP on cold list (Attio record exists but zero engagement; treated as cold). Left intact.
- **BDG-CPAs** (CPAs row 5) — KEEP on cold list (single 2025-11 outreach, no reply, NJ-local re-engageable firm). Left intact.

**Net:** Artifact's 17 REMOVE line-items minus BDG-CPAs (CEO KEEP exception) = **16 firm-level removals**. Choate is already inside the 17 (Industry Lawyers row 5). Peapack Corporate Advisors spans rows 2-11 → 10 row-level clears for that one firm-level item.

**Total row clears: 24** (16 firm-level removals; Peapack Corporate Advisors expanded to 10 individual rows).

| Tab | Row | Firm | Verified by name match | Cleared |
|---|---|---|---|---|
| Brokers | 6 | Viking Mergers & Acquisitions | YES | YES |
| Investment Bankers | 2 | Eight Quarter Advisors | YES | YES |
| Investment Bankers | 3 | Business Exits | YES | YES |
| Investment Bankers | 5 | Morgan Stanley | YES | YES |
| Investment Bankers | 6 | Peapack Private | YES | YES |
| Investment Bankers | 9 | Benchmark International | YES | YES |
| Investment Bankers | 13 | Heritage Holding — Lauren Morera | YES | YES |
| Industry Lawyers | 3 | Goodwin | YES | YES |
| Industry Lawyers | 5 | Choate Hall & Stewart | YES | YES |
| Industry Lawyers | 26 | Bellizio + Igel PLLC | YES | YES |
| CPAs | 3 | Richards Vissicchio Douglass CPAs | YES | YES |
| Corporate Advisors | 2 | Peapack Private Investment Banking | YES | YES |
| Corporate Advisors | 3 | Peapack Private Investment Banking | YES | YES |
| Corporate Advisors | 4 | Peapack Private Investment Banking | YES | YES |
| Corporate Advisors | 5 | Peapack Private Investment Banking | YES | YES |
| Corporate Advisors | 6 | Peapack Private Investment Banking | YES | YES |
| Corporate Advisors | 7 | Peapack Private Investment Banking | YES | YES |
| Corporate Advisors | 8 | Peapack Private Investment Banking | YES | YES |
| Corporate Advisors | 9 | Peapack Private Bank & Trust | YES | YES |
| Corporate Advisors | 10 | Peapack Private Bank & Trust | YES | YES |
| Corporate Advisors | 11 | Peapack Private Bank & Trust | YES | YES |
| Corporate Advisors | 17 | CFO Consulting Partners | YES | YES |
| Lenders | 29 | Plexus Capital | YES | YES |
| Lenders | 30 | Live Oak Bank | YES | YES |

**Post-execution populated row counts (column B non-blank):**

| Tab | Populated rows |
|---|---|
| Brokers | 61 |
| Investment Bankers | 7 |
| Association Heads | 42 (untouched) |
| Industry Lawyers | 22 |
| CPAs | 3 |
| Corporate Advisors | 4 |
| Family Offices | 22 (untouched) |
| Lenders | 26 |
| **Total** | **187** |

**KEEPs verified intact post-write:** NYBB Group (Brokers 20), Transworld Business Advisors of NY (Brokers 54), DealForce (IB 4), Paine Pacific (IB 8), Graphic Arts Advisors (IB 10), Proskauer Rose LLP (Industry Lawyers 4), BDG-CPAs (CPAs 5), J.P. Morgan Private Bank (Corp Advisors 14).

**Anomaly note on enumeration:** The execution-prompt sidebar enumerated 17 firms ("17 standard removals + Choate = 18"); the artifact's actual canonical REMOVE table contains 17 line-items including Choate (Industry Lawyers row 5). CEO KEEP exception on BDG-CPAs reduced canonical removals to 16 firm-level items. Final count of cleared rows = 24 (Peapack on Corporate Advisors expanded to 10 rows).
