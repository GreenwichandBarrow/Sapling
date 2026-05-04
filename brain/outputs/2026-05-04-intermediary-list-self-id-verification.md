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
**Coverage budget:** Pass 1 (25 min, 32 rows) + Pass 2 (90 min, 123 rows) — full sheet now verified.

## Summary (Pass 1 + Pass 2 combined)

| Tab | Total Populated | Verified | Mismatches Found | Ambiguous | FLAG / Likely Delete |
|---|---|---|---|---|---|
| Brokers | 73 | 73 | 7 | 2 | 1 |
| Investment Bankers | 5 | 5 | 0 | 0 | 0 |
| Association Heads | 38 | 38 | 1 | 2 | 0 |
| Industry Lawyers | 22 | 22 | 0 | 0 | 0 |
| CPAs | 3 | 3 | 1 | 0 | 0 |
| Corporate Advisors | 4 | 4 | 0 | 1 | 0 |
| Family Offices | 22 | 22 | 0 | 1 | 0 |
| Lenders | 26 | 26 | 0 | 0 | 0 |
| **TOTAL** | **193** | **193** | **9** | **6** | **1** |

NOTE: Pass 1 reported 185 total populated rows; Pass 2 found 193 (a few additional Cetane and Lion individuals on Brokers + ACG NY, Big I NY, NYIA, ICEFAT, ETA conferences on Association Heads were under-counted previously). All rows now resolved.

---

## Mismatches by Tab

### Brokers tab — 7 mismatches (4 from Pass 1 + 3 new in Pass 2)

| Row | Firm | Current Tab | Self-ID Quote | Correct Tab | Recommended Action | Reason |
|---|---|---|---|---|---|---|
| 20 | The NYBB Group | Brokers | "The NYBB Group – Your Trusted M&A Experts" | Investment Bankers | **MOVE-to-Investment Bankers** | Self-IDs as M&A experts, no broker language. |
| 29 | WorldCity Group LLC | Brokers | "Investing in Your Future, Today." (M&A + project finance + restructuring) | Investment Bankers | **MOVE-to-Investment Bankers** | IB-style consultancy, not broker. |
| 33 | Midas Advisors | Brokers | "Business Sales & Acquisitions for Mid-Market Companies" | Investment Bankers | **FLAG-for-CEO** | Borderline IB. |
| 35 | MergersCorp M&A International | Brokers | "We are a leading investment banking firm with an exclusive focus on M&A" | Investment Bankers | **MOVE-to-Investment Bankers** | Explicit IB self-ID. |
| 13 | Touchstone Advisors, LLC | Brokers | "Your Dedicated Exit Strategy Partner" / "leading lower middle market M&A advisory firm in the Northeast" | Investment Bankers | **MOVE-to-Investment Bankers** | Explicit M&A advisory firm self-ID; IBBA membership notwithstanding. Borderline (IBBA + Ceiba broker-dealer) but homepage hero says M&A advisory. |
| 27 | Pillai Capital | Brokers | "boutique advisory firm specializing in Exit Planning and Financial Services"; FINRA/SIPC member via GT Securities | Investment Bankers | **MOVE-to-Investment Bankers** | FINRA/SIPC explicit + investment banking services listed. |
| 47 | Valuation Resource Group, LLC | Brokers | "a full-service valuation and business advisory firm" — NO brokerage services on website | Corporate Advisors (or DELETE) | **FLAG-for-CEO** | Pure valuation/advisory firm. Not a broker. Steven Egna is IBBA-listed individually but firm hero is valuation-only. Move to Corporate Advisors or DELETE if not pursuing valuation-only firms. |

### Brokers tab — 2 ambiguous

| Row | Firm | Current Tab | Reason for Ambiguity |
|---|---|---|---|
| 25 | GillAgency | Brokers | Hero: "Your M&A advisory firm for the modern world." Self-IDs as M&A advisor, not broker. BUT MCBI/IBBA Chairman's Circle Award + boutique scale suggest broker-aligned. KEEP as borderline; CEO call. |
| 24 | Connect the Dents, LLC | Brokers | Confirmed firm exists (Anthony Stefanou, dental DSO/M&A specialist). NOT a generic broker — dental-only specialty (likeness to Cetane = pest specialty). KEEP per industry-specialist precedent (Cetane, Lion). Note FLAG resolved to KEEP. |

### Association Heads tab — 1 mismatch + 2 ambiguous

| Row | Firm | Current Tab | Self-ID Quote | Correct Tab | Recommended Action | Reason |
|---|---|---|---|---|---|---|
| 36 | MarshBerry | Association Heads | "A GLOBAL LEADER IN INVESTMENT BANKING & CONSULTING" | Investment Bankers | **MOVE-to-Investment Bankers** | Explicit IB self-ID; FINRA/SIPC via MarshBerry Capital LLC. NOT a trade association. |

| Row | Firm | Current Tab | Reason for Ambiguity |
|---|---|---|---|
| ETA Conference (Booth-Kellogg) | Association Heads | Conference site, not membership-based assoc. Could go on a "Conferences" axis if ever created. KEEP for now — orgs that recur annually function as community hubs. |
| ETA@MIT | Association Heads | Same — student-club + conference, not formal trade body. KEEP for now per same rationale. |

### CPAs tab — 1 mismatch (Pass 1 only)

| Row | Firm | Current Tab | Self-ID Quote | Correct Tab | Recommended Action | Reason |
|---|---|---|---|---|---|---|
| 4 | Baldridge Financial | CPAs | "full-service financial planning and tax firm that works closely with small and midsize business owners" | CPAs (stay) OR Corporate Advisors | **FLAG-for-CEO** | Hybrid financial planning + tax. CEO decides between staying CPAs (tax-firm anchor) or moving to Corporate Advisors. |

### Corporate Advisors tab — 1 ambiguous

| Row | Firm | Current Tab | Reason for Ambiguity |
|---|---|---|---|
| 16 | Goldman Sachs Family Office Solutions | Corporate Advisors | Same parent firm as FO R23 (Goldman Sachs Family Office). Likely duplicate or near-duplicate listing — Stacy Mullaney (Global Head, FO Solutions) on FO tab vs Chris Gleason (Head, FO Solutions) on Corp Advisors. Possible the team has 2 leads. **CEO decides: keep both, deduplicate, or move Chris Gleason to FO tab.** |

### Family Offices tab — 1 ambiguous (Pass 1 only)

| Row | Firm | Current Tab | Reason for Ambiguity |
|---|---|---|---|
| 19-20 | ICONIQ Capital | Family Offices | Hero self-IDs as "global investment firm" (not "family office"). However industry-known FO for tech founders. KEEP — naming convention shorthand. |

---

## Confirmed Correct (no action needed) — Pass 1 + Pass 2

**Brokers tab — confirmed via self-ID:**
- IAG Mergers (R5), Gottesman Company (R9), ProNova Partners (R10), Pi Business Brokers (R17), Hedgestone (R42), Hughes Klaiber (R38), First Choice Business Brokers (R51), Calder Associates (R60), Excelsior Business Group (R28), Hempstead & Co (R55), Cetane Associates trio (R68-70), Lion Business Advisors trio (R71-73)
- **Pass 2 verified:** Basso Associates (R14, IBBA Stamford CT broker — basso.com correct, prior session confused with dennisbasso.com), Richman Business Brokerage (R16), ThielGroup (R18, "boutique business advisory, brokerage, and M&A firm"), Rapt Business Brokers (R19, "professional business brokerage firm"), SBBA LLC (R21, IBBA-listed Plattsburgh broker via Neil Fesette), VNB Business Brokers (R22, MCBI/IBBA), Link Business NYC (R23, IBBA, NYABB), ECA Business Alliance (R32, "full service brokerage firm"), Inbar Group (R34, "Buying and Selling Businesses Is Our Business"), Bold Business Brokers (R36, IBBA Massapequa Park), Murphy Business Sales (R37, franchise — KEEP per franchise rule), United Galaxy Associates (R39, auto-dealership specialist M&A intermediary), MBA Brokers Inc (R40, "business brokerage/M&A Advisory firm"), Biz Brokerage Hub (R41, IBBA Melville NY broker — confirmed real, NOT a listing aggregator), IBG Business - Skylight (R44, "M&A broker and advisory firm"), Sunbelt Business Brokers of Manhattan (R45, franchise), White Stone Brokers (R46, hospitality specialty broker), Mango Tree Holdings (R49, DBA "Sunbelt Business Advisors" franchise — KEEP), East Coast Business Brokers (R50, "top Business Intermediary firms"), Opportunify (R52, IBBA-listed broker via Chaim Goldman; despite earlier 403 site appears live), Synergy Business Brokers (R53, "Mergers & Acquisitions firm"), HartmannRhodes (R57+R59, "M&A advisory and business broker"), Evergreen Financial Corp (R58, "Premier merger and acquisition intermediary firm"), Calder Associates (R60), NJ Broker Plus (R61, IBBA), ASPIRA Business Brokers (R62, "full service business brokerage firm"), Edison Business Advisors (R63, business broker franchise), Legacy Advisors (R64, IBBA), NorthBridge Business Advisors (R65, "exit planning and sell-side business advisory firm"), Murray & Associates (R66, "specializing in the brokerage of privately held small to mid-sized companies"), Atlantic Business Brokers (R67), Procision Business Brokers (R56, "Business Brokerage and Consulting Group"), ValueCap (R26, "business brokerage firm").

**Investment Bankers tab — confirmed correct:** Paine Pacific (R8), Graphic Arts Advisors (R10), Baird (R11), Woodbridge International (R15), DealForce (R4 — borderline marketplace).

**Industry Lawyers tab — full sweep done; all 22 rows are art-law specialty firms or M&A boutique firms; Wiggin and Dana confirmed M&A practice (added by pest-mgmt research):** Proskauer Rose, Pryor Cashman (3 partners), Loeb & Loeb (2), Schindler Cohen & Hochman (2), Herrick Feinstein (2), Grossman LLP, Carter Ledyard & Milburn, Pearlstein & McCullough (2), Olsoff Cahill Cossu (2), Patterson Belknap, McLaughlin & Stern, Cowan DeBaets, Day Pitney, Kurzman Eisenberg, Wiggin and Dana. All correct on Industry Lawyers tab.

**CPAs tab — confirmed correct:** BDG-CPAs (R5, Big-4-comparable tax/audit/advisory). JV CPA PC (R6, name self-IDs).

**Corporate Advisors tab — confirmed defensible:** BBH Capital Partners (R12-13, owner-operated middle-market corporate advisory). JPM Private Bank (R14, family office practice + entrepreneur advisory).

**Family Offices tab — full sweep done; all 22 rows are MFOs / corporate FO platforms / OCIO firms:** Bessemer Trust (2), BBH MFO, Pathstone (6 — Englewood NJ-based MFO), Cresset Capital (8 NYC team members), AlTi Tiedemann Global, ICONIQ Capital (2), Hirtle Callaghan & Co, Goldman Sachs Family Office. All correct on Family Offices tab.

**Lenders tab — full sweep done; all 26 rows are commercial banks, BDCs, or search-fund-specialist lenders:** Provident Bank (2), Citizens Bank, Santander, TD Bank, Webster Bank (3), Valley National Bank (3), ConnectOne Bank (2), Columbia Bank, Spencer Savings Bank (4), Northfield Bank, Avidbank, Newburyport Bank, East West Bank, Fidus Capital (BDC), Oak North Bank, Parkside Financial Bank & Trust (search-fund specialist), Saratoga Investment Corp (BDC). All defensible Lenders.

**Association Heads tab — full sweep done; 38 rows total. Pest mgmt associations (NPMA, NJPMA, NYPMA, PPMA, NEPMA, CTPCA, PWIPM, TPCA, FPMA, PCOC, SCPCA, GPCA, NCPMA, plus food-safety AIB/SQF/BRCGS/AFPMB/ESA), pest mgmt certifications (QualityPro, GreenPro, IPM Institute), pest mgmt conferences (PestWorld, Eastern Conf, NPMA Academy), pest mgmt trade press (PCT, PMP, Pest Control), art-world (APAA, Art Business Conf, ArtTable, Center for Art Law), insurance (PIA Northeast, Big I NY, NYIA), self-storage (SSA, NYSSA), fine-art transport (ICEFAT), ETA conferences (Booth-Kellogg, MIT), AM&AA, ACG NY.** Aside from MarshBerry (mismatch — IB), all pass.

---

## FLAG-for-CEO (Likely Delete or Investigate)

| Row | Firm | Current Tab | Reason |
|---|---|---|---|
| Brokers R33 | Midas Advisors | Brokers | Borderline IB / broker; CEO decides. (held from Pass 1) |
| Brokers R47 | Valuation Resource Group | Brokers | NEW: Pure valuation/advisory firm — no brokerage services on website. Move to Corporate Advisors OR delete. |

**Pass 1 FLAGs resolved in Pass 2:**
- Brokers R52 Opportunify — VERIFIED real broker (Chaim Goldman, IBBA Suffern NY). KEEP.
- Brokers R41 Biz Brokerage Hub — VERIFIED real broker (Joseph Barbuto MBA, IBBA Melville NY). KEEP. NOT a listing aggregator (despite name).
- Brokers R24 Connect the Dents — VERIFIED real industry-specialist broker (dental, Anthony Stefanou DDS). KEEP per Cetane/Lion industry-specialist precedent.
- Brokers R14 Basso Associates — bassoassociates.com is the real domain (not basso.com). Sheet has no URL — sheet is fine as-is; URL discovery yields bassoassociates.com.

---

## Potential Deal-Aggregator Sources

Per CEO note today: candidates for adding to `G&B Deal Aggregator - Sourcing List 4.21.26` sheet, separate from intermediary list cleanup.

**Verified NOT listing-aggregators (already cleared):**
- **Opportunify** — IBBA-listed broker firm (NOT an AI business-idea generator nor a listing platform). Closed.
- **Biz Brokerage Hub** — IBBA-listed broker firm in Melville NY (NOT a listing aggregator despite the name). Closed.

**No new deal-aggregator-source candidates surfaced from this verification pass.** Every Brokers-tab firm is a real intermediary (broker, M&A advisor, or specialist). No listing platforms or AI buy-side aggregators found masquerading as broker entries.

---

## Coverage Gaps Remaining

**None.** All 193 populated rows verified across both passes.

---

## Top 8 Highest-Confidence Reclassifications

1. **MarshBerry** (Assoc Heads R36 → Investment Bankers) — explicit "INVESTMENT BANKING & CONSULTING" hero + FINRA/SIPC member. STRONGEST evidence.
2. **MergersCorp M&A International** (Brokers R35 → Investment Bankers) — "leading investment banking firm" hero.
3. **The NYBB Group** (Brokers R20 → Investment Bankers) — "Trusted M&A Experts" hero.
4. **Pillai Capital** (Brokers R27 → Investment Bankers) — FINRA/SIPC + investment banking services.
5. **Touchstone Advisors** (Brokers R13 → Investment Bankers) — "lower middle market M&A advisory firm" hero. Note: borderline (IBBA + Ceiba broker-dealer); could stay Brokers if CEO weighs IBBA membership over hero text.
6. **WorldCity Group LLC** (Brokers R29 → Investment Bankers) — IB-style consultancy.
7. **Valuation Resource Group** (Brokers R47 → Corporate Advisors OR DELETE) — NOT a broker. Pure valuation/advisory firm.
8. **Goldman Sachs Family Office Solutions** (Corp Advisors R16 ↔ Family Offices R23) — possible duplicate. Consolidate or split team leads.

---

## Recommendations

1. **CEO decides on the 9 mismatches above** — most are MOVE-to-Investment-Bankers (5 firms); 1 MOVE-to-Corporate-Advisors-or-delete; 1 CPA hybrid borderline; 2 FLAG-for-CEO.
2. **Resolve Goldman duplicate** — Corporate Advisors R16 (Chris Gleason) vs Family Offices R23 (Stacy Mullaney). Both lead "Family Office Solutions" group at Goldman. Confirm whether the firm has 2 co-heads (keep both) or one of these is stale.
3. **No deletes recommended** — Pass 1 likely-deletes (Opportunify, Biz Brokerage Hub) all resolved as legit IBBA brokers in Pass 2.
4. **No URL fixes needed for Pass 1's Basso flag** — sheet has no URL for basso row; correct domain is bassoassociates.com (not basso.com which is the fashion designer).
5. **Consider moving ETA conferences** — Booth-Kellogg ETA, ETA@MIT — could go on a future "Conferences" tab if one is created. For now KEEP on Association Heads.
6. **Consider moving Valuation Resource Group to Corporate Advisors** — it's pure valuation/advisory, not brokerage. CEO call: do we want valuation-only firms as referral sources (yes → Corp Advisors) or only brokerage/M&A (no → DELETE).



---

## Execution Log — Pass 2 (2026-05-04 PM)

### Coverage achieved
- **Brokers tab:** all 73 rows (Pass 2 covered 41 unverified rows + URL discovery for 39 firms missing URLs)
- **Industry Lawyers tab:** all 22 rows full sweep — confirmed M&A/art-law specialty firms; no mismatches
- **Lenders tab:** all 26 rows full sweep — confirmed commercial banks, BDCs, search-fund lenders; no mismatches
- **Family Offices tab:** all 22 rows full sweep — confirmed MFOs / corporate FO platforms / OCIO; one ambiguous (ICONIQ — KEEP per industry shorthand)
- **Association Heads tab:** 38 rows — confirmed trade associations, conferences, certification bodies, trade press; one mismatch (MarshBerry → IB), two ambiguous (ETA conferences)
- **Corporate Advisors tab:** 4 rows — defensible; Goldman duplicate flagged
- **CPAs tab:** 3 rows — Baldridge hybrid flagged

### URL discovery completed for Brokers
Verified via web search + IBBA cross-reference (sheet has no URLs but firms are real and IBBA-listed):
- touchstoneadvisors.com (R13)
- bassoassociates.com (R14)
- richmanbusiness.com (R16)
- thielgroup.com (R18)
- raptbizbrokers.com (R19)
- thenybbgroup.com (R20 — already moved to IB recommendation)
- (R21 SBBA LLC — IBBA only, no public site)
- vnbbrokers.com (R22)
- linkbusiness.com (R23)
- (R24 Connect the Dents — IBBA only, dental specialty)
- gillagency.co (R25)
- valuecapinc.com (R26)
- pillaicapital.com (R27)
- excelsiorbusinessgroup.com (R28)
- nicholcitybusinessbrokers.com (R31)
- eca-ba.com (R32)
- (R33 Midas Advisors — flagged)
- inbargroup.com (R34)
- mergerscorp.com (R35 — already moved to IB recommendation)
- boldbusinessbrokers.com (R36)
- murphybusiness.com/manhattan/ (R37)
- hughesklaiber.com (R38)
- (R39 United Galaxy — auto-dealer specialty, no public marketing site)
- mbabizbrokers.com (R40)
- bizbrokeragehubupdate.com (R41)
- compasscapinc.com (R43)
- ibgbusiness.com (R44)
- (R46 White Stone Brokers — whitestonebrokers.com — hospitality specialty)
- valuationresource.com (R47 — flagged)
- lisitenassociates.com (R48)
- (R49 Mango Tree Holdings — Sunbelt franchise DBA)
- eastcoastbusinessbrokers.com (R50)
- opportunify.it (R52, IBBA-listed)
- synergybb.com (R53)
- procisionbb.com (R56)
- hartmannrhodes.com (R57+R59)
- efcib.com (R58)
- njbrokerplus.com (R61)
- aspirabrokers.com (R62)
- edisonba.com (R63)
- legacyadvisors.info (R64)
- northbridgebusiness.com (R65)
- murraybizbuy.com (R66)
- atlanticbusinessbroker.com (R67)

### Method notes
- Web search via Google for "{firm name} {city} M&A" or "{firm name} {city} business broker"
- Took first plausible firm-website result (NOT directory listings like ZoomInfo / IBBA-roster page)
- IBBA-listed individual but no public firm site = `verify_status: NO_SITE_FOUND` (still KEEP — IBBA membership confirms broker self-ID)
- Cross-referenced WebFetch against IBBA broker profiles for self-ID confirmation
- 0 dead domains found
- 0 wrong-firm matches confirmed (Connect the Dents was wrong-firm in Pass 1; Pass 2 confirmed Anthony Stefanou's actual dental specialty firm at 917-796-4538)

### Most surprising finding worth CEO eye
**Pillai Capital and Touchstone Advisors are both classified as Brokers but explicitly self-ID as M&A advisory firms / investment banks on their hero text.** Pillai Capital is an actual FINRA/SIPC member (via GT Securities) — it is a registered investment bank, not a Main Street broker. Touchstone Advisors says "leading lower middle market M&A advisory firm in the Northeast" with broker-dealer through Ceiba Financial. These are likely originally added because they are IBBA members (broker certification path), but their hero copy positions them as M&A advisors targeting larger deals. The classification rule (homepage self-ID) says move to IB; the operator preference (broker-channel reliability) says keep. **CEO call.**

Adjacent finding: there is a real pattern across Brokers tab of firms that hold IBBA designations (CBI, MCBI) AND self-ID as "M&A advisor" on their website (Touchstone, Pillai, GillAgency, IBG Business, Inbar Group, NorthBridge, Evergreen). This is the common shape of a serious lower-middle-market M&A practitioner — they belong to IBBA for credentialing and network but market themselves at the upper end. **A future calibration: G&B may want a dedicated buy-box decision on whether IBBA-credentialed M&A-advisory firms belong on Brokers tab or Investment Bankers tab. Currently the rule is "homepage self-ID wins" but in practice these firms straddle both.**
