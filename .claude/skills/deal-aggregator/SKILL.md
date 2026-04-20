---
name: deal-aggregator
description: "Daily aggregation of prepped deals — businesses actively selling. Scans broker platforms, email inbound (CIMs, broker blasts), and association deal boards. Target: 1-3 evaluable deals/day surfaced to Kay via Slack."
user_invocable: true
context_budget:
  skill_md: 2500
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Surface prepped deals — businesses that are actively selling — from every non-DealsX channel, every day. These are deals Kay can evaluate immediately: they have financials, a teaser, or a CIM available.

**This is distinct from cold outreach.** DealsX, outreach-manager, and JJ calls target owners who aren't selling yet. This skill finds businesses already on the market.

**Target: 1-3 evaluable deals per day.** If the skill consistently surfaces fewer, expand source coverage. The funnel needs volume.

**Sources:**
1. Broker platforms (searchable listing sites)
2. Email inbound (CIMs, broker blasts, intro forwards — read from email-scan-results artifact)
3. Industry-specific deal sources (niche brokers and M&A advisors)
4. Association deal boards (classified sections, member transition programs)

**This skill does NOT:**
- Handle DealsX deal flow (DealsX has its own dashboard)
- Draft outreach to owners (broker is the gatekeeper for broker-sourced deals)
- Enter deals into Attio (pipeline-manager handles that when NDA is signed)
- File documents into ACTIVE DEALS folders (pipeline-manager handles that)
- Scan Gmail directly (email-intelligence handles scanning, writes artifacts this skill reads)

**This skill DOES:**
- Scan all broker platforms daily for buy-box matches
- Read email-scan-results for inbound deals (CIMs, broker blasts, direct broker emails)
- Scan industry-specific deal sources for niche-relevant listings
- Monitor association deal boards
- Flag every match via Slack (#active-deals) — one message per deal, thumbs up/down workflow
- Feed listing patterns to niche-intelligence as market signals
- Process new broker introductions (research, classify, add to rotation)

**Inputs:**
- **Industry Research Tracker** (Sheet: `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins`, WEEKLY REVIEW tab) — active niche list read at scan start
- **email-scan-results artifact** (`brain/context/email-scan-results-{date}.md`) — inbound deal emails classified by email-intelligence
- **skill/niche-intelligence** — buy box, industry scorecards
- **skill/pipeline-manager** — Attio Intermediary Pipeline (broker stages, relationship status)

**Outputs:**
- Deal matches → individual Slack notifications → Kay reacts thumbs up/down → pipeline-manager takes over on NDA
- Niche signals → niche-intelligence (new thesis ideas, market patterns)
- New intermediary entities → Attio Intermediary Pipeline
</objective>

<channels>
## Channels

### Channel 1: Platform Scanning (Daily)

Scan searchable broker platforms + general marketplaces for new listings matching the buy box. **All sources below were verified parseable via WebFetch on 2026-04-20.**

**Source treatment rules (set 2026-04-20):**
- **No priority tiering.** Every Active niche from the tracker (Step 0) gets equal scanning. A deal is a deal. No Active-Outreach vs Active-Long Term distinction.
- **Fingerprint dedup** (see Cross-Day Deduplication below) prevents the same deal from re-surfacing across multiple sources.

**General marketplaces — Tier 1 (parseable):**
- BusinessBroker.net — `/state/{state}-businesses-for-sale.aspx`, aggregator of 30+ brokers
- Raincatcher — `/business-listings/`
- Synergy Business Brokers — `/listings/` (kept from prior skill)
- Website Closers — `/businesses/{slug}/{id}/` (2,000+ listings — previously underused)
- VR Business Brokers — `/businesses-for-sale/`
- Murphy Business Sales — `/business-brokerage/detail/{id}/{slug}`
- First Choice Business Brokers (FCBB) — `/businesses-for-sale` with filters
- **Axial** — `axial.net/forum/closed-deals/` + `/winning-loi-hub/` + `/trends-dashboard/` (weekly fresh, static HTML)
- **Acquisitions Direct** — `acquisitionsdirect.com/buy-a-business/` (static HTML, monthly-verify freshness)

**Online-business specialty (keep, filter digital niches):**
- Flippa — filter `revenue_per_month > $400K AND industry matches thesis`. Otherwise skip — skews micro-SaaS.
- Empire Flippers — Monday cadence matters (new listings drop Mondays)
- Quiet Light Brokerage — `/listings/` (bot-blocks WebFetch; email alerts recommended instead)

**Tier 2 — bot-blocked marketplaces (Kay subscribes to email alerts; flow through email-intelligence):**

These sites 403 WebFetch but have free "new listings today" email alerts. Kay subscribes; email-intelligence parses the digests; deal-aggregator reads the email-scan-results artifact (Channel 2).

- BizBuySell (bizbuysell.com) — largest US marketplace
- BizQuest (bizquest.com)
- BusinessesForSale.com
- DealStream (dealstream.com) — absorbed MergerNetwork
- Sunbelt Network (sunbeltnetwork.com) — largest broker franchise
- Transworld Business Advisors (tworld.com) — large franchise inventory
- BizBen (bizben.com) — CA-heavy SMB listings, JS-rendered
- FOCUS Bankers (focusbankers.com/deals/) — JS carousel
- IBBA (ibba.org) — newsletter form on homepage; no public deal board

**Tier 3 — registration/paywall (email-alert-only, if Kay registers):**
- **Kumo** (withkumo.com — NOT kumo.so which is dead) — $30/mo Pro tier gives daily alerts on 815K+ listings
- **BizScout / DealOS** (bizscout.com, dealos.bizscout.com/marketplace) — 40K+ listings gated
- **DealForce** (dealforce.com — NOT generationalequity.com which is parked) — registered-buyer Deal Alerts by industry/geo/size
- **DealSuite** (dealsuite.com) — validated-user-only, EU-first

**Deal-sharing communities:**
- Searchfunder (searchfunder.com) — Kay has membership. Email alerts → email-intelligence → this skill.

**Relationship-only intermediaries (no scraping, monitor for warm intros via email-intelligence):**
- Everingham & Kerr (everkerr.com)
- Benchmark International (embracebenchmark.com)
- Viking Mergers (vikingmergers.com)
- Woodbridge International (woodbridgegrp.com)
- IAG M&A Advisors (iagmerger.com)
- ProNova Partners (pronovapartners.com)
- Paine Pacific (painepacific.com)

**Retired / dead (removed 2026-04-20):**
- ~~DealFlow Agent~~ — NOT a listings board; sell-side landing page
- ~~Agency Checklists as deal source~~ — editorial M&A news, not listings. Moved to niche-intelligence newsletter tier.
- ~~Business Exits~~ — demoted to email-subscription tier (right band, wrong channel — broker-curated, not marketplace). 5+ consecutive zero-match days.
- ~~Union Square Advisors~~ — domain parked (firm may have rebranded; rediscover later)
- ~~Potomac PCG~~ — server down (ECONNREFUSED)
- ~~MergerNetwork~~ — 301 redirect to DealStream (deduplicated)
- ~~InsuranceJournal /news/mergers-acquisitions~~ — 404, topic URL also dead
- ~~Blouinartinfo~~ — defunct (timeout)
- ~~ARIS Title Insurance~~ — NXDOMAIN
- ~~Acquire.com / BizScout / Kumo / FE International~~ — login-gated, skip

**Scanning process:**

**Step 0 — Load active theses (REQUIRED before scanning):**
Read the Industry Research Tracker WEEKLY REVIEW tab to get the current active niches:
```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "'WEEKLY REVIEW'!A3:D20" -a kay.s@greenwichandbarrow.com --json
```
Row 3 is headers: Rank, Niche Hypothesis, Current Status, Outreach Channel. Filter for rows where Current Status starts with "Active" (Active-Outreach or Active-Long Term). Build a thesis list from the Niche Hypothesis column.

1. Sub-agent visits each platform's listing page
2. Scrape new listings since last scan (track by listing ID or date)
3. For each listing, extract: company description, industry, revenue, EBITDA, asking price, geography, employee count
4. Screen against buy box criteria AND the active thesis list from Step 0
5. **Revenue floor (auto-reject):** Any listing with stated revenue below $1.5M is auto-rejected. Do not flag, do not Slack, do not surface.
6. Two types of matches (only after passing revenue floor):
   - **Thesis match** — fits an active niche thesis. High priority.
   - **Buy-box match, new niche** — fits the financial buy box ($1-5M EBITDA, $3-20M revenue, independently owned) but in a niche we haven't evaluated. Route to niche-intelligence as a discovery signal.

**Slack notification — ONE per deal:**
```bash
curl -s -X POST "$SLACK_WEBHOOK_ACTIVE_DEALS" \
  -H "Content-Type: application/json" \
  -d '{"text":"🔔 Deal match\nSource: {Platform or Broker}\nCompany: {Name or blind profile}\nIndustry: {Industry description}\nRevenue: {Revenue} | EBITDA: {EBITDA} | Margins: {margin%}\nGeography: {Geography or \"Not disclosed\"}\nMatch type: {Thesis match / Buy-box match, new niche}\nTeaser:\n{Link to listing or teaser document}\n\n👍 = pursue  |  👎 = pass"}'
```

**CRITICAL: Each deal gets its own Slack message.** Kay and her analyst react individually.

**NO COMMENTARY IN SLACK POSTS.** Team channels (#active-deals, #strategy-active-deals) get raw deal facts only — no analyst notes, no filter gating ("would need Jake/Adam SaaS filter"), no motivation reads ("seller is 'curious' not 'exploring'"), no thesis framing. Internal reasoning belongs in terminal dialogue with Kay, not in team-facing Slack. The `👍/👎` workflow IS the commentary channel — Kay and her analyst discuss via reactions, not via pre-written notes in the post.

**Morning briefing:** Report count only: "deal-aggregator — {n} new deals posted to Slack". Kay reviews deals on Slack, not in the briefing.

### Channel 2: Email Inbound
Read `brain/context/email-scan-results-{date}.md` for deal-related emails classified by email-intelligence.

**What to surface:**
- CIMs received (any industry) — immediate Slack notification
- Broker blast emails with specific deals matching buy box or thesis
- Direct broker emails with deal teasers or blind profiles
- NDA requests or follow-ups on previously flagged deals

**What to skip:**
- Newsletter content (market commentary without specific deals)
- Broker marketing (capability presentations, tombstones)
- Deals already flagged from platform scanning (dedup by company name/description — see Cross-Day Deduplication below)

### Cross-Day Deduplication (background, not surfaced to Kay)

Maintain a persistent listing fingerprint store so the same deal re-listed across platforms or reposted over multiple days is only Slacked once.

**Store:** `brain/context/deal-aggregator-fingerprints.jsonl` — append-only log.

**Fingerprint fields per entry:**
```json
{"date_first_seen": "YYYY-MM-DD", "source": "Business Exits", "company_hash": "...", "industry": "...", "revenue_band": "3-5M", "ebitda_band": "1-2M", "geography": "Southeast", "listing_url": "..."}
```

**Fingerprint rule:** `company_hash` = SHA-1 of (normalized industry description + revenue band + geography). Two listings with the same hash = same deal, regardless of source.

**Before sending any Slack notification:**
1. Compute fingerprint for the candidate listing
2. Check the store — if a matching fingerprint exists within last 30 days, suppress the notification
3. If the listing has changed materially (new price, new broker) log as update but still suppress re-Slack
4. If new fingerprint → Slack and append to store

**Exposure:** This runs silently. Never surface dedup activity in the morning briefing or Slack. It's hygiene, not a feature.

### Channel 3: Industry-Specific Deal Sources

Scan niche-specialist M&A advisor transaction pages + trade-press M&A sections. **All Tier 1 sources below verified parseable on 2026-04-20.**

**Specialty Insurance Brokerage (Art & Collectibles):**
- Sica Fletcher — `sicafletcher.com/announcements` (current URL; old /deals page stale since 2021)
- MarshBerry — `marshberry.com/financial-advisory/transactions/recent-transactions/`
- OPTIS Partners — `optisins.com/wp/articles-and-thought-pieces/` (try `/wp/feed/` for RSS)
- Dowling Hales — `dowlinghales.com/transactions`
- Agency Brokerage Consultants — `agencybrokerage.com/about/transactions/` (redirected from old URL)
- AgencyEquity — `agencyequity.com/category/articles`

**Premium Pest Management:**
- PCT Online (Pest Control Technology) — `pctonline.com/rss/` **(RSS feed — strongest pest signal)**
- PMP (Pest Management Professional) — `mypmp.net/feed/` **(RSS feed)**
- NPMA PestWorld — `npmapestworld.org/your-business/latest-news/`
- PCO Bookkeepers — `pcobookkeepers.com/transactions/` (image tombstones; OCR or title-text)
- ~~Potomac PCG~~ — REMOVED (server ECONNREFUSED)
- Cetane (`cetane.com/industries/pest-control/`), Anticimex (`us.anticimex.com/selling-your-business/`) — intel only, no scrape

**Estate Management Companies:**
- Wealth Management / Trusts & Estates — `wealthmanagement.com/trusts-estates/` + site-wide `/rss.xml` (no T&E-specific feed)
- Synergy BB real-estate listings — `synergybb.com/businesses-for-sale/real-estate-businesses-for-sale/`
- Exit Strategies Group — `exitstrategiesgroup.com/propertymanagement/` (advisory only)

**Specialty Coffee Equipment Service:**
- Daily Coffee News — `dailycoffeenews.com/feed/` **(RSS)**
- Barista Magazine — `baristamagazine.com/feed/` **(RSS)**
- Fresh Cup Magazine — `freshcup.com/feed/` **(RSS)**

**Art Storage & Related Services:**
- ARTnews Market — `artnews.com/c/art-news/market/` (+ `/feed/`)
- The Art Newspaper — `theartnewspaper.com/rss.xml` **(RSS)**

**Vertical SaaS (Luxury / HV-Asset Services):**
- Software Equity Group (SEG) — `softwareequity.com/transactions/`
- Shea & Co — `sheaco.com/transactions/`
- Tyton Partners — `tytonpartners.com/transactions/` (EdTech/HealthTech focus)
- GP Bullhound — `gpbullhound.com/deals/`
- Berkery Noyes — `berkerynoyes.com/transactions`
- ~~Union Square Advisors~~ — REMOVED (domain parked; rediscover later)

**High-End Commercial Cleaning:** — no sources yet (niche not yet launched per Kay 2026-04-20)

**Private Art Advisory:**
- Uses the same Art Storage sources above (ARTnews Market, The Art Newspaper) — market coverage overlaps

### Channel 4: Association Deal Boards

Monitor for off-market opportunities through industry associations.

**Pest Management:**
- NPMA (npmapestworld.org) — 5,000 members. Monitor newsletters and PestWorld conference for transition announcements.
- State PMAs — Check state-level pest management associations for classified sections.

**Insurance:**
- IIABA / Big I (independentagent.com) — Agency perpetuation planning resources, member network transitions.
- State insurance agent associations — classifieds and transition programs.

**Estate Management:**
- IREM (irem.org) — Institute of Real Estate Management, member networking.
- NARPM (narpm.org) — National Association of Residential Property Managers, occasional member transitions.

### Channel 5: New Introductions
When Kay receives a broker introduction (detected via email-scan-results).

1. **Detect** — Read email-scan-results for introduction signals
2. **Research** — Visit broker's website. Assess: searchable platform? Industries? Deal sizes? Relevant to active theses?
3. **Add to system:**
   - Create entity in `brain/entities/{slug}.md`
   - Add to Attio Intermediary Pipeline at "Identified"
   - If scrapable → add to scanning rotation
   - If email-only → classify as email-only intermediary
4. **Draft response** — Superhuman draft: short, warm, offer NDA, don't over-explain
5. **Update this skill** — Add new platform to scanning list if applicable

**Classify new intermediaries:**
- **Platform** → "Register as buyer on their site"
- **Boutique** → "Send broker intro email to managing director"
- **Industry specialist** → "Introduce as buyer in their specialty"
- **Association** → "Research membership and deal flow programs"

**Track registration:** After Kay registers or sends broker email, watch for deal flow within 4 weeks. Flag if no flow after 4 weeks.
</channels>

<niche_signals>
## Niche Signal Detection

Every listing scanned generates data. Track patterns:

### Thesis Validation
- Multiple listings in same niche across brokers → market exists and businesses trade
- Listing prices and multiples → market comp data
- Geographic clustering → regional opportunities

### New Thesis Discovery
- Listing fits buy box but in unscreened niche → create `brain/inbox/` item for niche-intelligence
- Recurring industry across platforms → possible consolidation wave
- Format: "Broker signal: {n} {industry} businesses listed in past {period} across {platforms}. Average: ${revenue} revenue, ${EBITDA} EBITDA. Consider for screening?"

### What NOT to signal
- One-off listings in random industries
- Listings obviously outside buy box (PE-backed, $100M+ revenue, franchise)
- Duplicate listings across platforms
</niche_signals>

<folder_management>
## ACTIVE DEALS Folder Management

**Normal flow (email-based):**
1. Deal-aggregator flags match → Slack ping to Kay
2. Kay signs NDA (on platform or via email)
3. Broker emails NDA confirmation and/or CIM
4. Pipeline-manager detects email, creates ACTIVE DEALS folder, files documents, creates Attio entry at "NDA Signed"

**Edge case (platform-only unlock):**
1. Kay signs NDA on platform → no email sent
2. Kay creates folder manually in ACTIVE DEALS
3. Pipeline-manager overnight scan detects new folder, creates Attio entry
</folder_management>

<results_file>
## Results File

**REQUIRED after every run.** Write to `brain/context/deal-aggregator-scan-{YYYY-MM-DD}.md`:

```markdown
---
date: {YYYY-MM-DD}
deals_found: {n}
platforms_scanned: {n}
email_deals: {n}
---
# Deal Aggregator Scan — {date}

## Deals Surfaced (sent to Slack individually)
1. **{Company/Profile}** — {Source} | {Revenue} | {EBITDA} | {Match type} | {Link}

## Email Inbound Deals
1. **{Company/Profile}** — {Broker} | {Type: CIM/Teaser/Blast} | {Details}

## Near Misses (not Slacked)
- {listing} — {reason not flagged}

## Platform Status
- {Platform}: {accessible/blocked/login required}

## Volume Check
- Deals surfaced today: {n}
- 7-day rolling average: {n}
- Target: 1-3/day — {ON TRACK / BELOW TARGET / ABOVE TARGET}
```
</results_file>

<stop_hooks>
## Sub-Agent Stop Hooks

### Scan Stop Hook
- [ ] Every match includes: source, listing URL, company description, industry, revenue/EBITDA (or "not disclosed"), geography
- [ ] Listing URL is a working link (not a search results page or homepage)
- [ ] Match classified as "Thesis match" or "Buy-box match, new niche"
- [ ] No duplicate listings (dedup across platforms AND email inbound)
- [ ] Revenue floor enforced: sub-$1.5M auto-rejected
- [ ] Buy-box screen: $1-5M EBITDA, $3-20M revenue, independently owned
- [ ] Zero matches = report "No matches" — never fabricate

### New Introduction Stop Hook
- [ ] Entity created in vault with proper schema
- [ ] Attio Intermediary Pipeline entry at "Identified"
- [ ] Website researched and scrapability assessed
- [ ] Draft response in Superhuman — short, warm, offers NDA
</stop_hooks>

<validation>
## Validation

### Daily Check
- [ ] All accessible platforms scanned
- [ ] Email inbound deals from email-scan-results processed
- [ ] Matches sent to Slack individually with links
- [ ] Results file written with volume check

### Weekly
- [ ] Niche signals compiled and sent to niche-intelligence
- [ ] Intermediary pipeline stages reviewed (any gone cold?)
- [ ] Platform scanning status (any sites changed/blocked?)
- [ ] Volume trend: are we hitting 1-3/day? If not, identify gaps and expand sources.

### Guardrails
- **Never contact an owner directly** on a broker-sourced deal. Always go through the broker.
- **Auto-reject sub-$1.5M revenue deals.** Silently archived, no exceptions.
- **No PE-owned companies.** Hard stop.
</validation>

<success_criteria>
## Success Criteria

### Phase 1 (Current — get volume flowing)
- [ ] All accessible platforms scanned daily
- [ ] Email inbound deals surfaced same-day
- [ ] Industry-specific sources scanned for each active niche
- [ ] Slack notifications working with thumbs up/down workflow
- [ ] Results file written daily with volume tracking

### Phase 2 (Steady state — 1-3 deals/day)
- [ ] Rolling 7-day average: 1-3 deals/day surfaced
- [ ] New introductions processed within 24 hours
- [ ] Intermediary network growing (1-2 new sources/month)
- [ ] Platform list maintained (broken sites removed, new ones added)
- [ ] If below target: proactively identify and add new sources
</success_criteria>
