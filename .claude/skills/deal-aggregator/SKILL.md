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
Scan searchable broker platforms for new listings matching the buy box.

**General broker platforms (cross-industry):**
- Business Exits (businessexits.com/listings/) — email + searchable, consistently accessible
- DealForce (dealforce.com) — Generational Equity buyer platform, registration required, filter by SIC/EBITDA/revenue
- Rejigg (rejigg.com) — automated deal match emails + searchable
- Flippa (flippa.com) — email alerts + searchable (mostly digital/online businesses)

**General broker platforms (email-only, no searchable platform):**
- Everingham & Kerr (everkerr.com) — most active broker, email listings
- Benchmark International (embracebenchmark.com) — email deal flow, advisory only
- Viking Mergers (vikingmergers.com) — periodic deal blasts
- Quiet Light (quietlight.com) — email + searchable but persistently Cloudflare-blocked

**Relationship-only intermediaries (no public listings):**
- Woodbridge International (woodbridgegrp.com) — homepage accessible, no public listings
- Paine Pacific (painepacific.com) — few public listings, mostly NDA-gated
- IAG M&A Advisors (iagmerger.com) — Kay has account, advisory
- ProNova Partners (pronovapartners.com) — 403 blocked, relationship-only

**Gated platforms (need Kay's registration):**
- FE International (app.feinternational.com) — requires buyer registration
- Website Closers (websiteclosers.com) — no public listings page

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
  -d '{"text":"🔔 Deal match\nSource: {Platform or Broker}\nCompany: {Name or blind profile}\nIndustry: {Industry description}\nRevenue: {Revenue} | EBITDA: {EBITDA} | Margins: {margin%}\nGeography: {Geography or \"Not disclosed\"}\nMatch type: {Thesis match / Buy-box match, new niche}\nTeaser:\n{Link to listing or teaser document}\n\nNote: {1-2 sentence analyst note — why this matches or key risk}\n\n👍 = pursue  |  👎 = pass"}'
```

**CRITICAL: Each deal gets its own Slack message.** Kay and her analyst react individually.

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
- Deals already flagged from platform scanning (dedup by company name/description)

### Channel 3: Industry-Specific Deal Sources

Scan niche-specific platforms and brokers that specialize in the active thesis industries.

**Premium Pest Management:**
- PCO Bookkeepers & M&A Specialists (pcobookkeepers.com) — Advisory only, Dan Gordon (CPA), $1B+ in sell-side transactions. Monitor newsletter/blog.
- Keystone Business Advisors (keystonebusinessadvisors.com/business-listings/) — Registration required. Pest control up to $50M revenue.
- Cetane (cetane.com/industries/pest-control/) — Lower middle market M&A advisory, no public listings.
- DealFlow Agent (dealflowagent.com/home-services/pest-control) — AI-powered M&A marketplace, 200+ active pest control buyers.
- Anticimex (us.anticimex.com/selling-your-business/) — Strategic acquirer, market intelligence only.

**Specialty Insurance Brokerage:**
- Sica Fletcher (sicafletcher.com/announcements) — #1 insurance M&A advisory, JS-rendered, relationship-only.
- MarshBerry (marshberry.com) — Investment banking + consulting for insurance, relationship-gated.
- Reagan Consulting (reaganconsulting.com) — Insurance M&A advisory, no public marketplace.
- Agency Checklists (agencychecklists.com) — Tracks insurance M&A transactions quarterly, public, scrapable.

**Estate Management Companies:**
- Exit Strategies Group (exitstrategiesgroup.com/propertymanagement/) — Property management M&A advisory, sell-side focused.
- Synergy Business Brokers (synergybb.com/businesses-for-sale/real-estate-businesses-for-sale/) — Real estate management listings, publicly browsable.

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
