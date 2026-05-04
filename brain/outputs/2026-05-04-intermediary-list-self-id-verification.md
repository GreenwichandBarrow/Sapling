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
tags: ["date/2026-05-04", "output", "output/validation", "status/review", "topic/intermediary-pipeline", "topic/broker-channel-build", "topic/self-id-verification"]
---

# Intermediary Target List — Self-ID Verification Pass

**Sheet:** `Intermediary Target List` (`18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`)
**Method:** Per-firm homepage hero/H1 self-ID quote, NOT analyst-inferred deal-size band (per `feedback_classify_intermediary_by_self_id.md`).
**Mode:** READ-ONLY — CEO reviews and decides.
**Coverage budget:** 25 minutes; partial pass focused on Brokers + Investment Bankers + cross-tab spot-checks. Full coverage requires a follow-up run.

## Summary

| Tab | Total Populated | Verified This Run | Mismatches Found | Ambiguous | FLAG / Likely Delete |
|---|---|---|---|---|---|
| Brokers | 61 | 18 | 4 | 0 | 1 |
| Investment Bankers | 5 | 5 | 0 | 0 | 0 |
| Association Heads | 42 | 1 (spot) | 1 | 0 | 0 |
| Industry Lawyers | 22 | 1 (spot) | 0 | 0 | 0 |
| CPAs | 3 | 2 | 1 | 0 | 0 |
| Corporate Advisors | 4 | 2 | 0 | 0 | 0 |
| Family Offices | 22 | 3 (spot) | 0 | 1 | 0 |
| Lenders | 26 | 0 (spot only) | 0 | 0 | 0 |
| **TOTAL** | **185** | **32** | **6** | **1** | **1** |

NOTE: 153 rows remain unverified (mostly Brokers without websites + Lenders + Lawyers full-tab + Association Heads full-tab + Family Offices full-tab). Estimated 90-120 min of additional web-fetch + Google-fallback to fully resolve.

---

## Mismatches by Tab

### Brokers tab — 4 mismatches

| Row | Firm | Current Tab | Self-ID Quote | Correct Tab | Recommended Action | Reason |
|---|---|---|---|---|---|---|
| 20 | The NYBB Group | Brokers | "The NYBB Group – Your Trusted M&A Experts" | Investment Bankers | **MOVE-to-Investment Bankers** | Self-IDs as M&A experts, not broker. No "broker" language on hero. |
| 29 | WorldCity Group LLC | Brokers | "Investing in Your Future, Today." (services: M&A, project finance, corporate restructuring) | Investment Bankers | **MOVE-to-Investment Bankers** | Self-IDs as investment-banking-style management consultancy, not broker. |
| 33 | Midas Advisors | Brokers | "Business Sales & Acquisitions for Mid-Market Companies" | Investment Bankers | **FLAG-for-CEO** | "Mid-market" framing closer to IB; verify with CEO. Borderline. |
| 35 | MergersCorp M&A International | Brokers | "We are a leading investment banking firm with an exclusive focus on M&A and corporate advisory services for companies worldwide." | Investment Bankers | **MOVE-to-Investment Bankers** | Explicit "investment banking firm" self-ID. Clear mismatch. |

### Association Heads tab — 1 mismatch

| Row | Firm | Current Tab | Self-ID Quote | Correct Tab | Recommended Action | Reason |
|---|---|---|---|---|---|---|
| 36 | MarshBerry | Association Heads | "A GLOBAL LEADER IN INVESTMENT BANKING & CONSULTING" | Investment Bankers | **MOVE-to-Investment Bankers** | Explicit IB self-ID; FINRA/SIPC member through MarshBerry Capital, LLC. NOT a trade association. |

### CPAs tab — 1 mismatch

| Row | Firm | Current Tab | Self-ID Quote | Correct Tab | Recommended Action | Reason |
|---|---|---|---|---|---|---|
| 4 | Baldridge Financial | CPAs | "Baldridge Financial is a full-service financial planning and tax firm that works closely with small and midsize business owners" | Corporate Advisors (or stay) | **FLAG-for-CEO** | Hybrid financial planning + tax shop, not pure CPA. Could stay if "tax firm" anchor counts; could move to Corporate Advisors. CEO call. |

---

## Ambiguous Rows

| Row | Firm | Current Tab | Reason for Ambiguity |
|---|---|---|---|
| FO R20-21 | ICONIQ Capital | Family Offices | Hero self-IDs as "global investment firm" (not "family office"). However, well-known industry positioning IS as family office for tech founders. Recommend KEEP — naming convention is industry shorthand, not self-ID literal. Flag noted. |

---

## Confirmed Correct (no action needed)

**Brokers tab — confirmed correct via self-ID:** IAG Mergers (R5, "M&A advisory" — borderline; current notes match), Gottesman Company (R9, "America's International Network of M&A Business Brokers" — confirms recent revert), ProNova Partners (R10), Lion Business Advisors (R71-73, "trusted business broker and M&A advisory firm"), Transworld Business Advisors of NY (R54, franchise — keep per franchise-on-Brokers rule), Sunbelt Business Brokers of Manhattan (R45, "Sell Your Business. Secure Your Future." franchise — keep), Pi Business Brokers (R17, "We Help Plan, Expand, Buy & Sell"), Hedgestone Business Advisors (R42, "The Gold Standard of Business Brokering"), Hughes Klaiber (R38, "Trusted, Experienced Business Brokers"), First Choice Business Brokers (R51, "The World's Authority in Business Sales"), Calder Associates (R60, "Business Brokers & M&A Services"), Excelsior Business Group (R28, "full service business brokerage firm"), Hempstead & Co. (R55, "Ready for a Change?... Next Stage of life"), Cetane Associates (R68-70, current Brokers placement matches G&B's existing pattern for industry-specialist M&A advisors).

**Investment Bankers tab — confirmed correct:** DealForce (R4 — borderline "Other / Marketplace" but acceptable on IB tab), Paine Pacific (R8, "M&A services for companies under $50M"), Graphic Arts Advisors (R10, "M&A Advisory and Consulting Services"), Baird (R11, explicit "Global Investment Banking"), Woodbridge International (R15, "Trusted M&A advisors since 1993").

**Industry Lawyers tab — spot check:** Proskauer Rose (R4) self-IDs as M&A/transactional law firm — correct.

**CPAs tab — spot check:** BDG-CPAs (R5, "Top Quality Accounting") — correct.

**Corporate Advisors tab — spot check:** BBH Capital Partners (R12-13) — confirmed BBH self-IDs as global financial services firm with Capital Partners advisory arm; placement defensible. JPM Private Bank (R14) — diversified wealth/private bank platform; placement defensible if treating private bank as corporate advisor entry point.

**Family Offices tab — spot check:** Bessemer Trust (R2-3, "Private Wealth Management & Investment Advisory" + "deep family office expertise") — correct.

---

## FLAG-for-CEO (Likely Delete or Investigate)

| Row | Firm | Current Tab | Reason |
|---|---|---|---|
| Brokers R33 | Midas Advisors | Brokers | Borderline IB / broker; "mid-market" framing leans IB but firm is small. CEO decides. |
| Brokers R52 | Opportunify | Brokers | 403 on web-fetch; firm name + URL not resolving cleanly. Possible defunct or aggregator. Verify or delete. |
| Brokers R41 | Biz Brokerage Hub | Brokers | URL pattern suggests possible listing aggregator (like BizBuySell) rather than firm. 403 on fetch. Verify or delete. |

---

## Coverage Gaps (rows where website + LinkedIn weren't accessible)

**Brokers tab — websites missing in sheet (43 rows need URL discovery before self-ID can be verified):**
R13 Touchstone Advisors (verified independently: "Exit Strategy Partner" — M&A Advisor leaning), R14 Basso Associates (basso.com redirects to dennisbasso.com — wrong firm; URL needs correction), R16 Richman Business Brokerage, R18 ThielGroup ("M&A, valuations, advisory" — verified), R19 Rapt Business Brokers, R21 SBBA LLC, R22 VNB Business Brokers, R23 Link Business NYC, R24 Connect the Dents (returned dental industry profile — likely WRONG firm match, FLAG), R25 GillAgency (ECONNREFUSED), R26 ValueCap (no content), R27 Pillai Capital (ECONNREFUSED), R31 Nichol City Business Brokers (ECONNREFUSED), R32 ECA Business Alliance (404), R34 Inbar Group (503), R36 Bold Business Brokers (ECONNREFUSED), R37 Murphy Business Sales (403 — known broker franchise, KEEP per franchise rule), R39 United Galaxy Associates, R40 MBA Brokers Inc., R43 Compass Capital Advisors, R44 IBG Business - Skylight, R46 White Stone Brokers, R47 Valuation Resource Group (ECONNREFUSED), R48 Lisiten Associates, R49 Mango Tree Holdings, R50 East Coast Business Brokers, R53 Synergy Business Brokers (403), R56 Procision Business Brokers (timeout), R57 HartmannRhodes (403), R58 Evergreen Financial Corp., R59 HartmannRhodes Intermediaries LLC, R61 NJ Broker Plus, R62 ASPIRA Business Brokers (ECONNREFUSED), R63 Edison Business Advisors, R64 Legacy Advisors LLC, R65 NorthBridge Business Advisors, R66 Murray & Associates, R67 Atlantic Business Brokers.

**Investment Bankers tab:** Full coverage achieved (5/5).

**Association Heads tab:** 41 rows unverified this run; most appear self-evidently associations from name (NPMA, NJPMA, NYPMA, ACG NY, AM&AA, SSA, etc.). Recommend a future targeted pass on the non-association-named entries (MarshBerry already caught) plus the Booth-Kellogg / ETA conferences which may belong on a separate "Conferences" axis if one is created.

**Industry Lawyers tab:** 21 rows unverified beyond Proskauer spot. Notes column says all are "Art Law" — likely correct as-is given they were vetted at addition; recommend a sweep only if a doubt is raised.

**Lenders tab:** 26 rows unverified. Names + roles read as commercial/community banks + 1 BDC + 1 search-fund-specialist; placement looks defensible from sheet context. Recommend low-priority follow-up.

**Family Offices tab:** 19 rows unverified beyond Bessemer + ICONIQ + BBH spot. Pathstone, Cresset, AlTi, Hirtle Callaghan, Goldman FO are well-known multi-family offices; placement defensible.

**CPAs tab:** R6 JV CPA PC unverified; name strongly suggests CPA — placement likely correct.

**Corporate Advisors tab:** R16 Goldman Sachs Family Office Solutions — note this is on Corporate Advisors but is a family-office solutions group; possible candidate to MOVE-to-Family Offices, but R23 on Family Offices already has "Goldman Sachs Family Office" — risk of duplicate. FLAG-for-CEO.

---

## Top 5 Highest-Confidence Reclassifications

1. **MarshBerry** (Assoc Heads R36 → Investment Bankers) — explicit "INVESTMENT BANKING & CONSULTING" hero + FINRA/SIPC member. Strongest evidence.
2. **MergersCorp M&A International** (Brokers R35 → Investment Bankers) — "leading investment banking firm" hero.
3. **The NYBB Group** (Brokers R20 → Investment Bankers) — "Trusted M&A Experts" hero, no broker language.
4. **WorldCity Group LLC** (Brokers R29 → Investment Bankers) — IB-style consultancy, M&A + project finance + restructuring.
5. **Goldman Sachs Family Office Solutions** (Corp Advisors R16 → Family Offices, OR delete duplicate) — same parent as FO R23; consolidation needed.

---

## Recommendations

1. **CEO decides on the 6 mismatches above** — most are MOVE-to-Investment-Bankers; one CPA hybrid borderline.
2. **Delete or verify 1 likely-deletes** — Opportunify, Biz Brokerage Hub, possibly Connect the Dents (wrong-firm match).
3. **Schedule a follow-up run** — 90-120 min budget — to resolve the 153 unverified rows. Highest-value: Brokers without websites (need URL discovery + self-ID), then Industry Lawyers full sweep, then Lenders, then Family Offices.
4. **Fix `basso.com` URL** for Brokers R14 — currently redirects to a fashion designer site (wrong domain).
5. **Consider a "Conferences" tab** if Booth-Kellogg ETA / ETA@MIT / PestWorld belong on a separate axis from associations.
