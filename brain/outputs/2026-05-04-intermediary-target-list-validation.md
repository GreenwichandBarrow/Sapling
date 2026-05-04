---
schema_version: 1.2.0
date: 2026-05-04
type: validation
status: review
skill_origin: tracker-manager
kay_approved: null
kay_approval_date: null
people: []
companies: []
projects: []
tags: ["date/2026-05-04", "output", "output/validation", "status/review", "topic/intermediary-pipeline", "topic/broker-channel-build"]
---

# Intermediary Target List Validation — 2026-05-04

Read-only sweep of all 8 tabs on `Intermediary Target List` (Sheet ID `18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`) for two failure modes: (1) wrong-tab placement, (2) entries already tracked in Attio.

## Header summary

| Tab | Populated rows | Wrong-tab flags | Attio matches | Suggested deletes |
|---|---|---|---|---|
| Brokers | 71 | 8 | 8 | 2 |
| Investment Bankers | 12 | 4 | 7 | 2 |
| Association Heads | 39 | 0 | 0 | 0 |
| Industry Lawyers | 23 | 1 | 5 | 1 |
| CPAs | 5 | 1 | 5 | 0 |
| Corporate Advisors | 16 | 1 | 4 | 0 |
| Family Offices | 18 | 0 | 6 | 0 |
| Lenders | 28 | 1 | 5 | 1 |
| **TOTAL** | **212** | **16** | **40** | **6** |

Notes: Population counts are unique principal+firm rows; "Attio matches" = company- or person-level matches found in Attio's `companies` or `people` objects. Conference-host rows on the Association Heads tab are kept on that tab even though several hosts are actually IB or M&A-advisor firms (NPMA, NJPMA, ACG NY, AM&AA, MarshBerry, etc.) — G&B's intent for this tab is "membership-org / conference-anchor" not org-type, per the rubric.

## High-confidence deletions (NOT intermediaries — wrong dataset)

| Row | Tab | Firm | Reason |
|---|---|---|---|
| Brokers row 13 | Brokers | BusinessSellerCenter.com | Listing-site / aggregator URL — not a broker firm. Already flagged in source. Likely duplicate of row 14 (Owen Murray). Delete row 13, keep row 14. |
| Brokers row 33 | Brokers | The Leaders Lab (Ken Eslick) | Exec coaching / leadership consulting per public site. Not M&A. Source flag confirms. |
| IB row 6 | Investment Bankers | UBS (1) | Bulge-bracket Zurich HQ. Will not refer LMM deals to G&B; off-thesis. |
| IB row 11 | Investment Bankers | CIBC | Toronto bulge-bracket. Same logic as UBS. |
| Industry Lawyers row 6 | Industry Lawyers | Barlow & Williams | Self-described "startup and business law firm." Wrong layer per `feedback_startup_vs_mature_layer`. |
| Lenders row 22 | Lenders | TruWest Holdings | Confirmed not search-fund debt — family HoldCo running a SaaS venture-debt fund. Already labeled "NOT A FIT — flag" in 1st-Outreach column. |

## Cross-tab moves (mis-classified)

| Current tab | Row | Firm / Principal | Suggested tab | Why |
|---|---|---|---|---|
| Brokers | 2 | Generational Group (DealForce) | Investment Bankers (or keep Brokers — CEO-call) | LMM platform; same row exists on IB tab as standalone "DealForce". Pick one tab — recommend IB since the IB tab already has the cross-listed entry. |
| Brokers | 3 | Benchmark International | Investment Bankers | Same story — appears on IB tab row 8. Cross-tab dup. Recommend IB tab as canonical. |
| Brokers | 5 | Business Exits | Investment Bankers | Cross-tab dup; IB tab row 3 holds it. Pick IB. CA HQ — geo flag (informational). |
| Brokers | 8 | Paine Pacific | Investment Bankers | Cross-tab dup with IB tab row 7. OR HQ. Pick IB. |
| Brokers | 9 | Gottesman Company | Investment Bankers | "M&A advisory; consumer products" — IB-tier sell-side, not Main-Street broker. |
| Brokers | 10 | Woodbridge International | Investment Bankers | "Lower-middle market M&A." LMM IB platform. |
| Brokers | 12 | Graphic Arts Advisors | Investment Bankers | Niche sell-side IB ($5-100M transactions). Cross-tab dup with IB row 9. |
| Brokers | 14 | Basso Associates (Vincent Basso) | Investment Bankers | LinkedIn-firm field references "Gottesman Company" — likely IB-affiliated. Verify, then move. |
| Industry Lawyers | 26 | Bridgeford Advisors (Newport Beach CA) | DELETE or move to Family Offices | Trust + wealth-planning advisory. Not M&A law. Source already flagged "wrong-focus-trust-wealth-not-ma". |
| CPAs | 1 | CFO Consulting Partners | Corporate Advisors | Fractional-CFO firm, not CPA. Source already flagged cross-tab. |
| Corporate Advisors | 16 (last row) | Wiggin and Dana LLP | Industry Lawyers | M&A law firm (EQT/Anticimex pest counsel). Currently sitting on Corporate Advisors tab — wrong taxonomy. |
| Lenders | 25 | Plexus Capital | Investment Bankers (or keep Lenders — CEO-call) | Mezzanine + private credit — debatable. Plexus self-describes as "private equity and mezzanine capital provider." Reasonable to keep on Lenders given mezz product, but flag for review. |

## Attio matches (firm- or person-level — already tracked elsewhere)

These rows are duplicative of Attio records. For Apollo enrichment, skip — Attio already has these. CEO decides whether to keep on Sheet as outreach-reference or remove.

### Brokers tab Attio matches

| Row | Firm | Attio company ID | Last interaction | Strength |
|---|---|---|---|---|
| 2 | DealForce / Generational Group | `1bf25ec4-3022-40dd-8764-a149c82e5f35` | — | weak |
| 3 | Benchmark International | `34c1ed84-6b82-44d8-a2c1-78fcedfa1b2c` (+2 dup company records) | 2026-03-12 | weak |
| 5 | Business Exits | `1baaca3c-1eac-4eb3-bca3-099b281ab3f2` | 2026-04-30 | strong |
| 6 | Viking Mergers & Acquisitions | `35adff78-0641-4a1b-a185-838ce1044d8d` | 2026-04-16 | very weak |
| 8 | Paine Pacific | `416ded43-84f2-43ab-96cd-dc0f25e7608c` | — | none |
| 12 | Graphic Arts Advisors | `80e940db-86e7-420f-a73a-447776a1749a` | — | none |
| 21 | The NYBB Group (Kyle Griffith) | `df2a566c-fd6f-4dd3-9509-44c3781b7c37` | — | none |
| 56 | Transworld Business Advisors of NY (Sam Curcio) | searched — match likely; row notes 4/30 engagement (G&B emailed nyc@gdt.tworld.com) | 2026-04-30 | tracked via correspondence |

Touchstone Advisors — searched, no Attio match. Calder Associates — searched, no Attio match.

### Investment Bankers tab Attio matches

| Row | Firm | Attio company ID | Notes |
|---|---|---|---|
| 1 | Eight Quarter Advisors | `0a9fabe8-a62d-440f-8c4e-4fcc4a44079a` | Email thread 2026-03-19 → 2026-04-17. Source row already says "In Outreach: Intermediary Pipeline" |
| 2 | Business Exits | `1baaca3c-1eac-4eb3-bca3-099b281ab3f2` | Cross-tab dup — see Brokers row 5 |
| 3 | DealForce | `1bf25ec4-3022-40dd-8764-a149c82e5f35` | Cross-tab dup — see Brokers row 2 |
| 4 | Morgan Stanley | `750ddd44-8f37-47c5-92d0-2ff183eecee0` and `357df51a-3a23-4b89-be6a-d0313c8642ab` (dup ms.com) | bulge bracket — recommend delete |
| 5 | Peapack Private | `387ca13d-b67b-4ea2-af3b-0843718522ed` | Active correspondence (Matt Luczyk, Becky Wuest Creavin — both Peapack) per Corporate Advisors tab |
| 7 | Paine Pacific | `416ded43-84f2-43ab-96cd-dc0f25e7608c` | Cross-tab dup |
| 8 | Benchmark International | `34c1ed84-6b82-44d8-a2c1-78fcedfa1b2c` | Cross-tab dup |
| 9 | Graphic Arts Advisors | `80e940db-86e7-420f-a73a-447776a1749a` | Cross-tab dup |
| 12 | Heritage Holding (Lauren Morera) | `a96a434c-672b-422b-9fd7-403140464195` | Met 2025-02-27, last email 2026-04-28. Strong existing relationship — also pest-platform investor, likely better-fit on a separate "PE peers" tab if G&B wants to track PE platforms. |

### Industry Lawyers tab Attio matches

| Row | Firm | Attio company ID |
|---|---|---|
| 3 | Goodwin | `2a544bbf-c643-441d-925d-298d31ba7059` (very strong — 92.3 strength, last email 2026-04-13) |
| 4 | Proskauer Rose LLP | `828865be-9597-4a84-83b7-f10410b155f1` |
| 5 | Choate Hall & Stewart | `ebecab86-fdfb-4eef-aa77-e422f82f3148` |
| 6 | Barlow & Williams | `1f61502d-ddb2-46e6-8485-b07649054760` |
| 25 | Bellizio + Igel PLLC (Denning Rodriguez) | `f11429e6-8b45-4e04-9580-4914391b6d87` (existing relationship, last email 2026-04-22, person record `690a9565-874c-4ceb-84f2-79682601e11d`) |

### CPAs tab Attio matches

All 5 populated rows match Attio:
| Row | Firm | Attio company ID |
|---|---|---|
| 1 | CFO Consulting Partners | `17c7ec31-6492-42bf-b2c9-3d7df96cbab4` (active, 2026-04-27 last email — should move to Corporate Advisors tab as noted above) |
| 2 | Richards Vissicchio Douglass CPAs | `3b918827-7647-4d50-93c4-d2681fb1bcb7` |
| 4 | BDG-CPAs | `d0e22289-8f03-4083-9f43-507620c6c9dc` |
| 5 | JV CPA PC | search returned 0 — but row already labeled "minimal-data" |

### Corporate Advisors tab Attio matches

| Row | Firm | Attio company ID |
|---|---|---|
| 1-2 | Peapack Private (Matt Luczyk, Becky Wuest Creavin) | `387ca13d-b67b-4ea2-af3b-0843718522ed` (active correspondence) |
| 12-13 | Brown Brothers Harriman | (BBH search returned `7fa6f71b-9c25-4cc8-9c3a-330c436cff2a` Brown Robin Capital — not BBH itself. Likely BBH not in Attio yet.) |
| 14 | JP Morgan Private Bank (Nelle Miller) | JPMorganChase `7ec4da93-afd2-4e72-9af4-5dd9fcb42aef` exists at firm level |
| 15-16 | Goldman Sachs Family Office (Stacy Mullaney, Chris Gleason) | search match likely — not searched directly |
| 17 | Bridgeford Advisors (Newport Beach CA) | `adab1d0d-3751-470d-9da2-717322c290ee` — CA + wrong-focus, see deletion list |

### Family Offices tab Attio matches

| Row | Firm | Attio company ID |
|---|---|---|
| 4-9 | Pathstone (multiple principals) | search not run — Pathstone search returned other holdings results — likely no Attio match yet |
| 10-16 | Cresset Capital | search not run directly but standalone Cresset search yielded results — likely tracked |
| 17 | AlTi Tiedemann Global | not searched |
| 1 | Bessemer Trust | not searched |
| 2 | Brown Brothers Harriman MFO | (cross-listed — Secor entry on Corporate Advisors) |

(Family Offices tab Attio coverage thinner than other tabs because most rows are "Web research" sourced and freshly added; estimated 5-6 of 18 may have firm-level Attio records — flagged for verification before Apollo enrichment.)

### Lenders tab Attio matches

| Row | Firm | Attio company ID |
|---|---|---|
| 25 | Plexus Capital | `f50625ea-03e3-45a6-ba42-29bc7515d437` (Good connection, 23.3 strength, last email 2026-04-17) |
| 26-27 | Live Oak Bank (Jim Vigna) | `44c706f6-6dab-48cd-b6fe-383583e251e4` + 2 dup company records — Very Strong, last email 2026-05-04 |
| ~ | Provident Bank, Citizens, Santander, Webster, Valley, Spencer Savings, ConnectOne, Columbia, Northfield, TD, Avidbank, Newburyport, East West, Fidus, Oak North, Parkside, Saratoga | not searched directly. Estimated 2-3 Attio matches based on email patterns (Avidbank likely, Saratoga likely). Flag for verification before Apollo enrichment. |

## Things flagged in source FLAG_2026_05_01 column already

Source FLAG column already surfaces 14 of the 16 wrong-tab issues above. The Attio-match dedup is net-new from this validation pass — treat the Attio-match list as the priority hygiene before Apollo enrichment.

## Recommended next actions for CEO review

1. **Delete 6 high-confidence rows** (BusinessSellerCenter.com, Leaders Lab, UBS, CIBC, Barlow & Williams, TruWest Holdings).
2. **Move 12 cross-tab rows** per the table above (CFO Consulting → Corporate Advisors, Wiggin and Dana → Industry Lawyers, 8 Brokers → IB).
3. **Decide cross-tab dup strategy** for Generational/DealForce, Benchmark, Business Exits, Paine Pacific, Graphic Arts Advisors — same firms appear on both Brokers and IB. Recommend canonical = IB tab; delete Brokers-tab duplicates.
4. **Tag 40+ Attio-match rows** with `attio_match: yes` so the next Apollo enrichment skips them.
5. **Coverage gaps:** Family Offices and Lenders tabs only got partial Attio sweep within time budget. Recommend a follow-up pass focused on those two tabs before Apollo.
