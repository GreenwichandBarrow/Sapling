---
schema_version: 1.1.0
date: 2026-04-29
type: context
title: "Session Decisions — 2026-04-29 (Wednesday)"
tags: [date/2026-04-29, context, topic/session-decisions, topic/intermediary-target-list, topic/lender-outreach, topic/pest-management, topic/email-templates]
---

# Session Decisions — 2026-04-29 (Wednesday)

Major build day. Built the entire Intermediary Target List from scratch (8 tabs, 178 unique firms post-cleanup), drafted the G&B Intermediary Outreach Templates Doc, created Premium Pest Management Industry Insights deck, and saved 6 durable memories. Apollo enrichment ran (200 credits, 71 verified emails added). Email drafts held per Kay; she'll signal when ready.

## Decisions

### Intermediary Target List — full build

- **APPROVE:** Build 8-tab Intermediary Target List in `OPERATIONS / TARGET LISTS / INTERMEDIARY/`. Tabs: Brokers, Investment Bankers, Association Heads, Industry Lawyers, CPAs, Corporate Advisors, Family Offices, Lenders.
- **APPROVE:** 17-column schema (post-cleanup). Source / Firm / Website / HQ / Focus / Lead Contact / Title / Email / Office Phone / Direct/Mobile / LinkedIn (P) / LinkedIn (F) / Credentials / Signup URL / Deal Email Pattern / 1st Outreach Date / Notes.
- **APPROVE:** Sheet is a reference list, NOT a maintained tracker. Attio owns ongoing status. 1st Outreach Date populated as "To be contacted" for new rows; date for already-corresponding rows.
- **REJECT:** Year Founded column (removed) — not load-bearing for outreach decisions.
- **REJECT:** Channel Type column (removed) — Deal Email Pattern + Signup URL together capture the same info more usefully.
- **REJECT:** Status columns generally — Attio owns status, not the sheet.

### Brokers tab (128 → 119 firms)

- **APPROVE:** Source list = Jeremy Black email Jan 2025 + IBBA NY/NJ/CT scrape + 4 web-research-found industry specialists.
- **APPROVE:** Geography = Northeast (ME, NH, VT, MA, RI, CT, NY incl NYC, NJ, PA). NOT exclude NYC.
- **APPROVE:** Industry filter = "opportunistic" (no hard exclusion).
- **APPROVE:** Mix = regional + national + industry-specialist brokers (per Megan Lawlor's 4/29 call insight).
- **APPROVE:** For franchise networks (Transworld, Sunbelt, First Choice, Murphy), keep ONE brand row per firm-name (NY-preferred). Multiple Transworld franchisees collapsed to single Transworld NY row + named-suffix franchisees as separate firms.
- **APPROVE:** 7 SIGNUP firms identified (DealForce, Benchmark, Rejigg, Business Exits, Viking, Gottesman, Graphic Arts) with registration URLs in Signup URL column.

### Lenders tab — Guillermo's list cross-validated by Melissa @ BK Growth

- **APPROVE:** Tab named "Lenders" (not "Commercial Bankers" / "Bankers" / "Business Bankers") — most inclusive; covers commercial bank RMs + SBA + mezz + BDCs + private credit + senior debt.
- **APPROVE:** Guillermo's 9 lenders added (Avidbank, Newburyport, East West, Fidus, Oak North, Parkside, Saratoga, True West Capital Partners, Plexus). Bain Capital flagged "Not a fit" (real estate focus).
- **APPROVE:** True West = True West Capital Partners (truewestcp.com) — NOT TruWest Holdings (Kennedy-family SaaS-debt firm). Subagent's initial misidentification corrected; row updated.
- **APPROVE:** Plexus + Avidbank + Parkside cross-validated by Melissa Rosenblatt (BK Growth) email — high-conviction priority targets.
- **APPROVE:** Katie Walker @ Plexus (kwalker@plexuscap.com) is the warm-intro priority-1 lender contact; warm-intro line "Will Bressman, GJ King, and Melissa Rosenblatt at BK Growth recommended I introduce myself" works for her.
- **APPROVE:** Zach Duprey @ Parkside Financial (zduprey@pfbt.com) is priority-2; he was the OTHER BK Growth 1/8/2026 Zoom guest alongside Katie Walker. Same warm-intro line works.

### Cross-tab dedup + categorization audit

- **APPROVE:** Strict by-firm-name dedup with NY > NJ > CT > other tiebreaker. Multi-office same-firm rows collapsed; other contacts preserved in Notes column.
- **APPROVE:** Move Eight Quarter Advisors from Investment Bankers tab to Brokers tab (it's a boutique broker, not bulge IB).
- **APPROVE:** Clear 12 misplaced/non-intermediary rows from Investment Bankers tab (Buyouts, PEI = publications; Alumni Ventures = VC; Harbor Street + Estelio = searchers; Live Oak = on Lenders; Business Exits/DealForce/Paine Pacific/Graphic Arts/IAG/E&K = duplicates already on Brokers). Final IBs tab = 6 true investment bankers (Morgan Stanley, Peapack Private, UBS, Karakoram, Baird, CIBC).
- **APPROVE:** Goldman Sachs Family Office cross-tab dupe → keep on Family Offices, clear from Corporate Advisors.
- **APPROVE:** Bridgeford Advisors → move from Brokers to Corporate Advisors (it's a wealth/trust advisor, not a broker).
- **APPROVE:** Olympia → delete entirely from Brokers (it's a searcher, peer not intermediary, per `feedback_searcher_overlap`).
- **APPROVE:** Tax Alchemy → delete entirely from CPAs (tax-education business, not M&A CPA).
- **REJECT:** Add Nicole Falcey to Industry Lawyers tab — she's an employment lawyer, NOT a deal-flow contact. Industry Lawyers tab criterion stays: M&A counsel / transaction attorneys / tax-PE attorneys only. Her content stays as DD reference for any future NJ pest acquisition.

### Email template (G&B Intermediary Outreach Templates Doc)

- **APPROVE:** Saved to G&B MASTER TEMPLATES folder as new Google Doc (ID `1_cNsAPCopDAfReoDXbB4d3hZW8TcYUqJ3XKYY_er7i4`).
- **APPROVE:** 8 audience-specific variations (one per intermediary tab) + shared core blocks + warm-intro language bank.
- **APPROVE:** Drop "search vehicle" / "search fund" language entirely. Use "holding company in formation" per Heritage Holding model. Saved as `feedback_no_search_fund_language_intermediaries.md`.
- **APPROVE:** Remove "$2.8M committed equity" claim — false framing (search-fund equity is committed-on-deal, not held in escrow).
- **APPROVE:** ONE-AND-DONE cadence for intermediary outreach. No follow-up sequences. Different from owner outreach pattern.
- **APPROVE:** Heritage Holding's monthly newsletter (Sam Kramer) = the calibration source for framing. Buy-box scannable, "what we look for / focus / what we don't do" structure.

### Pest Management — NJPMA workshop notes

- **APPROVE:** Saved 2 vault notes at `brain/library/internal/pest-management/`:
  - `2026-04-29-hoffman-exterminating-presentation.md` — industry-insider perspective + community-fit framing
  - `2026-04-29-falcey-nj-employment-law-dd-reference.md` — NJ employment-law DD reference (NOT for outreach; reference only)
- **APPROVE:** New ongoing-insights deck created at `OPERATIONS / .. / PREMIUM PEST MGMT/Premium Pest Management - Industry Insights` (Slides ID `1dOuzxIiMit2IOBf5Ut8PgMAab4_1jGPWE2bXXmfQWYo`). Existing one-pager preserved untouched. New deck = running log for future industry context.
- **APPROVE:** Hoffman's "community-connected business" + "customer service with a little extermination" framing = key positioning lever for G&B's "buy-and-operate, not roll-up" message. Used in updated Hoffman draft.
- **APPROVE:** Hoffman draft #112 reframed to LEAD with his community insight (not consolidation data) — calibration moment after Kay's correction.

### Lifestyle / identity / niche-fit insight

- **APPROVE:** Save Kay's NJPMA "preppy/casual" reflection as `project_kay_lifestyle_dress_filter.md`. After 10+ yrs of formal corporate dress, casual-preppy operator dress codes are a positive niche fit. Used as tiebreaker, NOT primary kill criterion. Art insurance and luxury-services niches still strategically valid; lifestyle is a personal cost factor.

### Apollo enrichment

- **APPROVE:** Apollo cap at 200 credits per subagent run. Apollo billing renews 1st of each month (May 1 next).
- **APPROVE:** First Apollo run silently hit Cloudflare 403 (User-Agent issue). Re-run with patched User-Agent succeeded; 71 verified emails added across workbook.
- **APPROVE:** Updated `reference_apollo.md` memory with billing cycle + monthly-balance API limitation.
- **DEFER:** Remaining 40 deferred Apollo enrichments (IBs/Lawyers/CPAs/Assn Heads tabs that hit credit cap before reaching) → resume after May 1.

### Tooling / workflow corrections

- **APPROVE:** Superhuman sunset (Apr 28). Drafts now via Gmail directly. Saved as `feedback_gmail_only_no_superhuman.md`. Supersedes 6 prior Superhuman memories (marked deprecated for next calibration sweep).
- **APPROVE:** All replies handled by Kay personally (Kay-sent or Sam-DealsX-sent). Saved as `feedback_kay_handles_all_replies.md`. Reply handling is NOT a per-campaign decision — it's settled.
- **APPROVE:** LinkedIn "Verified on LinkedIn" API is NOT useful for G&B's enrichment workflow. Skip.

## Actions Taken

### Sheet operations

- **CREATED:** Google Sheet "Intermediary Target List" (`18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`) in `OPERATIONS / TARGET LISTS / INTERMEDIARY/`.
- **POPULATED:** 246 rows across 8 tabs initially; collapsed to 178 unique firms after dedup + categorization cleanup.
- **ENRICHED:** 71 verified emails added via Apollo. ~100+ total verified contacts after combining manual research + Apollo + pre-existing Attio data.
- **CREATED:** Google Doc "G&B Intermediary Outreach Templates" (`1_cNsAPCopDAfReoDXbB4d3hZW8TcYUqJ3XKYY_er7i4`) in `OPERATIONS / G&B MASTER TEMPLATES/`.
- **CREATED:** Google Slides "Premium Pest Management - Industry Insights" (`1dOuzxIiMit2IOBf5Ut8PgMAab4_1jGPWE2bXXmfQWYo`) in `OPERATIONS / .. / PREMIUM PEST MGMT/`.

### Vault writes

- **CREATED:** `brain/library/internal/pest-management/2026-04-29-hoffman-exterminating-presentation.md`
- **CREATED:** `brain/library/internal/pest-management/2026-04-29-falcey-nj-employment-law-dd-reference.md`

### Memory writes (6 new + 1 updated)

- **CREATED:** `feedback_gmail_only_no_superhuman.md`
- **CREATED:** `feedback_kay_handles_all_replies.md`
- **CREATED:** `project_guillermo_lender_list.md`
- **CREATED:** `feedback_no_search_fund_language_intermediaries.md`
- **CREATED:** `project_kay_lifestyle_dress_filter.md`
- **UPDATED:** `reference_apollo.md` (Apollo billing cycle + API limitations)
- **UPDATED:** `MEMORY.md` (index updated with new entries)

### Subagent runs

- IBBA + Jeremy + specialist scrape → 167 raw broker entries (subagent ID `a8d07f9300ed6f251`)
- Attio cross-check → 11 firms in Attio (subagent ID `abedb1cdefa6e4915`)
- SIGNUP/DIRECT classifier → 7 SIGNUP + 3 DIRECT confirmed; 71 IBBA defaulted to DIRECT (subagent ID `a2330d8915942d385`)
- Attio intermediaries query → 101 cross-tab intermediaries (subagent ID `a2db249a1ccfae66e`)
- 3-tab populator (Corporate Advisors / Family Offices / Lenders) → 56 rows (subagent ID `ae2e1b6b7b9440bd6`)
- Lender enrichment (8 firms) → 7 verified emails (subagent ID `af87a04bba53f1869`)
- Apollo enrichment (200 credits, 71 verified emails) (subagent ID `a18ab0a4a91250e12`)

## Deferred

- **Email drafts** — held per Kay's "no email drafts yet" directive. When Kay says go, top-3 priorities: Plexus (Katie Walker, warm intro Will/GJ/Melissa); Parkside (Zach Duprey, same warm intro); Avidbank (Anthony Rodriguez, cross-validated by Guillermo + BK Growth).
- **Hoffman meeting-request draft** (#112) — staged but held; updated to LEAD with community-fit insight per Kay's correction.
- **Apollo enrichment of remaining 40 rows** (IBs / Lawyers / CPAs / Assn Heads tabs) — resume after May 1 credit refresh.
- **Stale Superhuman memories cleanup** — 6 deprecated memory files (feedback_drafts_superhuman, feedback_drafts_in_superhuman_not_cursor, feedback_superhuman_drafts_only, feedback_superhuman_down_suppress_drafts, feedback_superhuman_token_fallback, reference_superhuman_cli) marked superseded; cleanup in next calibration sweep.

## Open Loops

- **Hoffman outreach (industry advisor, not intermediary)** — staged draft updated with community-fit opener; awaits Kay's go signal.
- **Hoffman Exterminating Co. as potential acquisition target** — unknown without further conversation; check buy-box fit if Kay decides to advance pest as primary niche.
- **Premium Pest Management one-pager v2** — Kay opted to build a separate ongoing-insights deck instead of editing the existing one-pager. The v1 .pptx remains static; new context goes in the Insights deck.
- **Email-template review/adjustment** — Kay can edit the Doc directly or call out changes for me to apply.
- **40 deferred Apollo rows** (IB/Lawyers/CPAs/Assn Heads) — resume May 1.
- **Apollo dashboard tile relabel** — current label "Apollo credits" reads as monthly balance but actually shows per-min rate-limit. Future fix: relabel + add manual monthly-balance entry field.

## System Status

- **Apollo MCP / API:** ✅ live, 200 credits used today, capped (subagent ID `a18ab0a4a91250e12`); resume May 1
- **Attio MCP:** ✅ live throughout; multiple successful person + company searches
- **gog (Google Workspace):** ✅ live; created Sheet, Doc, Slides; moved + renamed across folders
- **Granola MCP:** ✅ live; pulled Megan call + NJPMA workshop transcripts
- **Gmail (Superhuman sunset):** drafts now Gmail-direct; no Superhuman MCP usage today
