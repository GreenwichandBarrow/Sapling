---
name: intermediary-manager
description: "Manage the 20% intermediary deal channel — lead aggregation across broker platforms, industry-specific deal sources, and association deal boards. Flags matches for Kay, feeds signals to niche-intelligence. Email scanning (broker classification) is handled by pipeline-manager."
user_invocable: true
context_budget:
  skill_md: 2500
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Manage the intermediary deal flow channel. Aggregate leads from broker platforms, industry-specific deal sources, and association deal boards. Screen against the buy box, process new introductions, surface matches, and detect niche signals.

This is the 20% channel. It supplements proprietary outreach (target-discovery + outreach-manager), never replaces it. Broker deals go to 3000+ buyers — we rarely win competitive bids. The value here is: early detection of thesis-matching deals, niche signal intelligence, and growing the intermediary network over time.

**Email scanning note:** Pipeline-manager now handles all inbound email scanning, including broker email classification (BLAST/DIRECT/NEWSLETTER). This skill reads introduction signals from `brain/context/email-scan-results-{date}.md` rather than scanning Gmail directly.

**This skill does NOT:**
- Create targets on the target list (broker deals go through broker, not direct)
- Draft outreach to owners (broker is the gatekeeper)
- Enter deals into Attio (pipeline-manager handles that when NDA is signed)
- File documents into ACTIVE DEALS folders (pipeline-manager handles that)
- Scan Gmail for broker emails (pipeline-manager handles email scanning)

**This skill DOES:**
- Scan searchable broker platforms daily for buy-box matches
- Scan industry-specific deal sources for niche-relevant listings
- Monitor association deal boards and classified sections
- Flag matches via Slack (#active-deals) with link to listing
- Feed listing patterns to niche-intelligence as market signals and new thesis ideas
- Process new broker introductions (research platform, assess scrapability, add to rotation)

**Inputs from other skills:**
- **Industry Research Tracker** (Sheet: `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins`, WEEKLY REVIEW tab) — active niche list read at scan start. This is the live source of truth for which niches are active.
- **skill/niche-intelligence** — buy box, industry scorecards
- **skill/pipeline-manager** — Attio Intermediary Pipeline (broker stages, relationship status)

**Outputs to other skills:**
- Buy-box matches → Slack notification → Kay signs NDA → pipeline-manager detects and takes over
- Niche signals → skill/niche-intelligence (new thesis ideas, market patterns)
- New intermediary entities → Attio Intermediary Pipeline via pipeline-manager
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
Row 3 is headers: Rank, Niche Hypothesis, Current Status, Outreach Channel. Filter for rows where Current Status starts with "Active" (Active-Outreach or Active-Long Term). Build a thesis list from the Niche Hypothesis column. This is what "thesis match" means — a listing in an industry that matches one of these active niches.

Example output: `["Premium Pest Management", "Private art advisory", "Fractional CFO / Advisory Accounting", "Specialty Insurance Brokerage", "Art Storage"]`

This ensures that when a new niche enters Active-Outreach (e.g., Pest Management), the very next scan automatically knows to flag matching listings as thesis matches. No manual update needed.

1. Sub-agent visits each platform's listing page
2. Scrape new listings since last scan (track by listing ID or date)
3. For each listing, extract: company description, industry, revenue, EBITDA, asking price, geography, employee count
4. Screen against buy box criteria AND the active thesis list from Step 0
5. **Revenue floor (auto-reject):** Any listing with stated revenue below $1.5M is auto-rejected regardless of industry fit or broker relationship. Do not flag, do not Slack, do not surface. These are too small.
6. Two types of matches (only after passing revenue floor):
   - **Thesis match** — fits an active niche thesis (e.g., TCI brokerage, insurance compliance). High priority.
   - **Buy-box match, new niche** — fits the financial buy box ($1-5M EBITDA, $3-20M revenue, independently owned) but in a niche we haven't evaluated. Route to niche-intelligence as a discovery signal.

**When a match is found — send ONE Slack notification PER DEAL to #strategy-active-deals (never batch multiple deals into one message).** Kay and her analyst use Slack thumbs up/down reactions on each notification to quickly decide go/no-go. Batching breaks this workflow.

```bash
# Send this ONCE per matching deal — never combine deals
curl -s -X POST "$SLACK_WEBHOOK_ACTIVE_DEALS" \
  -H "Content-Type: application/json" \
  -d '{"text":"🔔 Broker listing match\nSource: {Platform}\nCompany: {Name or blind profile}\nIndustry: {Industry description}\nRevenue: {Revenue} | EBITDA: {EBITDA} | Margins: {margin%}\nGeography: {Geography or \"Not disclosed\"}\nMatch type: {Thesis match / Buy-box match, new niche}\nTeaser:\n{Link to listing or teaser document}\n\nNote: {1-2 sentence analyst note — why this matches or key risk}\n\n👍 = pursue  |  👎 = pass"}'
```

**CRITICAL: If 5 matches are found, send 5 separate Slack messages.** Each deal must be independently reactable.

**Morning briefing behavior:** Do NOT include individual match details in the morning briefing. The briefing System Status line should only report: "intermediary-manager — {n} new lead matches posted to Slack". Kay and her analyst review matches on Slack, not in the briefing.

**Results file (REQUIRED after every run):** Write a structured results file to `brain/context/intermediary-scan-{YYYY-MM-DD}.md` with all matches, passes, and platform status. This is the recall source — Slack messages can be deleted, but this file persists for 48 hours minimum. Format:

```markdown
---
date: {YYYY-MM-DD}
matches_found: {n}
platforms_scanned: {n}
---
# Intermediary Scan — {date}

## Matches (sent to Slack individually)
1. **{Company/Profile}** — {Platform} | {Revenue} | {EBITDA} | {Match type} | {Link}
2. ...

## Near Misses (not Slacked)
- {listing} — {reason not flagged}

## Platform Status
- {Platform}: {accessible/blocked/login required}
```

**Platform rotation:** If intermediary channel exceeds 25% of weekly targets (tracked on Weekly Tracker), reduce platform scanning to every other day and only surface exact thesis matches.

### Channel 2: Industry-Specific Deal Sources

Scan niche-specific platforms and brokers that specialize in the active thesis industries. These sources surface deals that general platforms miss.

**Premium Pest Management:**
- PCO Bookkeepers & M&A Specialists (pcobookkeepers.com) — Advisory only, no public listings. Dan Gordon (CPA) leads. $1B+ in sell-side transactions. Monitor their newsletter/blog for market signals. Contact for buy-side representation.
- Keystone Business Advisors (keystonebusinessadvisors.com/business-listings/) — Registration required. Pest control up to $50M revenue. Southern California base, national reach.
- Cetane (cetane.com/industries/pest-control/) — Lower middle market M&A advisory. No public listings, advisory relationship.
- DealFlow Agent (dealflowagent.com/home-services/pest-control) — AI-powered M&A marketplace. 200+ active pest control buyers. Buyer registration available. Monitor for sell-side mandates.
- Anticimex (us.anticimex.com/selling-your-business/) — Strategic acquirer (not broker). Tracks which companies they approach — useful for market intelligence, not deal sourcing.

**Specialty Insurance Brokerage:**
- Sica Fletcher (sicafletcher.com/announcements) — #1 insurance M&A advisory. $19B+ in transactions since 2014. JS-rendered (not scrapable). Track their quarterly index for market trends. Relationship-only deal flow.
- MarshBerry (marshberry.com) — Investment banking + consulting for insurance. Proprietary deal flow, relationship-gated. Publishes market reports.
- Reagan Consulting (reaganconsulting.com) — Insurance M&A advisory, valuations, perpetuation planning. No public marketplace. IIABA partner for Best Practices Study.
- Agency Checklists (agencychecklists.com) — Tracks insurance M&A transactions quarterly. Public, scrapable. Good for market intelligence and identifying active sellers.

**Fractional CFO / Advisory Accounting:**
- Poe Group Advisors (poegroupadvisors.com/buying/listings/) — Premier accounting practice marketplace. Publicly searchable, filter by location/price. CPA firms, virtual CFO practices, cloud accounting firms.
- Accounting Practice Sales (accountingpracticesales.com) — Global leader, 301 practices sold in 2025. Registration may be needed for full listings. $2B+ in closed deals.
- Accounting Practice Exchange (accountingpracticeexchange.com) — Classified advertising platform ($199/listing). Publicly browsable. Not a broker.
- Accounting Firm Sold (accountingfirmsold.com/listings/) — 35+ years experience. Publicly browsable, 27+ states. Revenue, cash flow, staff details per listing.
- ABA Advisors (acctsales.com/practices-for-sale/) — 40+ active listings. Publicly searchable with filters (region, revenue, practice type). Midwest/Northeast heavy.
- Private Practice Transitions (privatepracticetransitions.com/business-industry/accounting-tax/) — Pacific Northwest focus (OR, WA). 6 active listings. Revenue, SDE, EBITDA shown.

**Estate Management Companies:**
- Exit Strategies Group (exitstrategiesgroup.com/propertymanagement/) — Property management M&A advisory. Sell-side focused, no public listings.
- Synergy Business Brokers (synergybb.com/businesses-for-sale/real-estate-businesses-for-sale/) — Real estate management listings. Publicly browsable.

### Channel 3: Association Deal Boards

Industry associations sometimes have classified sections, member transition programs, or business-for-sale boards. Monitor these for off-market opportunities.

**Pest Management:**
- NPMA (npmapestworld.org) — No dedicated marketplace found. 5,000 members. Monitor member newsletters and PestWorld conference for transition announcements.
- State PMAs — Check state-level pest management associations (e.g., FPMA, TPCA) for classified sections.

**Insurance:**
- IIABA / Big I (independentagent.com) — Member resources include agency perpetuation planning. No public marketplace, but member networks surface transitions.
- State insurance agent associations — Many state-level associations have classifieds or transition programs for retiring agents.

**Accounting:**
- AICPA PCPS (aicpa.org/PCPS) — Succession Planning Resource Center. Not a marketplace, but connects firms seeking buyers/sellers.
- State CPA societies — Several (e.g., FICPA) have classified sections where Poe Group and other brokers list practices.

**Estate Management:**
- IREM (irem.org) — Institute of Real Estate Management. Member networking, no deal board.
- NARPM (narpm.org) — National Association of Residential Property Managers. Member transitions occasionally posted.

### Channel 4: New Introductions
When Kay receives a broker introduction (someone introduces her to a new intermediary).

**Note:** Pipeline-manager now handles all email scanning, including deal flow classification (BLAST/DIRECT/NEWSLETTER). Any broker introductions detected via email are written to `brain/context/email-scan-results-{date}.md`. This channel reads from that file for introduction signals rather than scanning Gmail directly.

1. **Detect** — Read `brain/context/email-scan-results-{date}.md` for introduction signals. Also scan for intro patterns in other channels: "I'd like to introduce you to...", "Connecting you with...", "Meet [name] who...", CC'd introductions
2. **Research** — Visit the broker's website. Determine:
   - Do they have a searchable listing platform?
   - What industries/deal sizes do they focus on?
   - Are they relevant to our active theses?
3. **Add to system:**
   - Create entity in `brain/entities/{slug}.md`
   - Add to Attio Intermediary Pipeline at "Identified"
   - If scrapable platform → add to Channel 1 or Channel 2 scanning rotation
   - If email-only deal flow → note as email-only intermediary (pipeline-manager handles email scanning)
4. **Draft response** — Warm reply in Superhuman (thank introducer, express interest to broker, mention search criteria). Per feedback: short, offer NDA, don't over-explain.
5. **Update this skill** — Add new platform to the scanning list in the appropriate channel if applicable

### New Intermediary Surfacing

When the morning scan detects intermediaries at "Identified" stage in Attio, classify and surface them with specific next steps:

1. **Classify type:**
   - **Platform** (has a website with deal listings, e.g., Poe Group, Business Exits) → "Next step: register as buyer on their site"
   - **Boutique** (small advisory firm, NDA-gated listings, e.g., Paine Pacific) → "Next step: send broker intro email to managing director"
   - **Industry specialist** (niche-specific M&A advisor, e.g., PCO Bookkeepers, Sica Fletcher) → "Next step: introduce as buyer in their specialty"
   - **Association** (industry group, trade org) → "Next step: research membership and deal flow programs"

2. **Surface in morning briefing** with the specific next step:
   - "New intermediary: {name} — {type} with {detail}. Next step: {action}."

3. **Track registration status:** After Kay registers on a platform or sends a broker email, note it on the intermediary's Attio record. Watch for deal flow within 4 weeks of registration.

4. **Cold alert:** If registered/contacted but no deal flow after 4 weeks, flag: "{intermediary} — registered {date}, no deal flow in 4 weeks. Still active?"

5. **Removal recommendation:** If the intermediary is in the wrong sector (flagged 2+ consecutive scans), recommend removal from pipeline with reason.
</channels>

<niche_signals>
## Niche Signal Detection

Every listing scanned (match or not) generates data. Track patterns across all platforms:

### Thesis Validation Signals
- Multiple listings in same niche across different brokers → validates market exists and businesses trade
- Listing prices and multiples → market comp data for active theses
- Geographic clustering → regional opportunities

### New Thesis Discovery
- Listing fits buy box but in unscreened niche → create `brain/inbox/` item for niche-intelligence
- Recurring industry appearing across platforms → may indicate sector consolidation wave
- Format: "Broker signal: {n} {industry} businesses listed in past {period} across {platforms}. Average: ${revenue} revenue, ${EBITDA} EBITDA. Consider for niche screening?"

### What NOT to signal
- One-off listings in random industries — noise, not signal
- Listings obviously outside buy box (PE-backed, $100M+ revenue, franchise)
- Duplicate listings across platforms (same company, different broker)
</niche_signals>

<folder_management>
## ACTIVE DEALS Folder Management

**Agent creates and manages all folders. Kay only creates folders in the edge case where signing an NDA on a platform does not trigger an email (platform just unlocks the CIM directly).**

### Normal flow (email-based):
1. Intermediary skill flags match → Slack ping to Kay
2. Kay signs NDA (on platform or via email)
3. Broker emails NDA confirmation and/or CIM
4. Pipeline-manager detects the email with NDA/CIM
5. Pipeline-manager creates ACTIVE DEALS folder, files documents
6. Pipeline-manager creates Attio entry at "NDA Signed"

### Edge case (platform-only unlock):
1. Kay signs NDA on platform → no email sent
2. Kay creates the folder manually in ACTIVE DEALS and saves the NDA
3. Pipeline-manager overnight scan detects new folder without matching Attio entry
4. Pipeline-manager creates Attio entry at "NDA Signed"

**Pipeline-manager must check for new ACTIVE DEALS subfolders that don't have Attio entries.** This is the catch-all for edge cases.
</folder_management>

<stop_hooks>
## Sub-Agent Stop Hooks

### Platform Scan Stop Hook
After each platform scan completes, verify before reporting results:
- [ ] Every match includes: platform name, listing URL, company description, industry, revenue/EBITDA (or "not disclosed"), geography
- [ ] Listing URL is a working link (not a search results page or homepage)
- [ ] Match is classified as "Thesis match" or "Buy-box match, new niche" — never both, never neither
- [ ] No duplicate listings (same company appearing from multiple platforms counted once, note all sources)
- [ ] Revenue floor enforced: any listing with stated revenue below $1.5M is auto-rejected, not flagged, regardless of thesis fit or broker relationship
- [ ] Buy-box screen applied: $1-5M EBITDA, $3-20M revenue, independently owned. Anything outside these ranges is NOT a match regardless of industry fit.
- [ ] If zero matches found across all platforms, report "No matches" — don't fabricate or stretch criteria to surface something

**If any check fails:** Fix before sending Slack notification. A bad link or wrong match wastes Kay's time.

### New Introduction Stop Hook
After processing a broker introduction:
- [ ] Entity created in vault with proper schema
- [ ] Attio Intermediary Pipeline entry created at "Identified"
- [ ] Website researched and platform scrapability assessed
- [ ] If scrapable: URL documented, added to platform scanning list
- [ ] Draft response created in Superhuman (not sent) — short, warm, offers NDA
- [ ] Introducer thanked (separate draft if Kay didn't already reply)

**If the broker's website is down or has no listings page:** Note "No searchable platform" and classify as email-only or relationship-only intermediary. Don't invent a URL.

### Niche Signal Stop Hook
Before sending niche signals to niche-intelligence:
- [ ] Signal based on 2+ listings across different platforms or 3+ from same platform in 30 days — not a single one-off listing
- [ ] Industry/niche clearly named and described
- [ ] Financial data summarized (average revenue, EBITDA, asking price across listings)
- [ ] Checked against existing niche-intelligence tracker — don't signal a niche that's already active, tabled, or killed
- [ ] Signal framed as a question, not a recommendation: "Consider for screening?" not "This is a good niche"
</stop_hooks>

<validation>
## Validation

### Daily Check
- [ ] All accessible platforms scanned (general + industry-specific for active niches)
- [ ] Matches sent to Slack with links
- [ ] Non-matches archived
- [ ] New introductions checked in `brain/context/email-scan-results-{date}.md` (if any)

### Weekly (on Weekly Tracker)
- [ ] Intermediary vs proprietary ratio calculated
- [ ] If >25%, throttle platform scanning
- [ ] Niche signals compiled and sent to niche-intelligence
- [ ] Intermediary pipeline stages reviewed (any gone cold?)
- [ ] Platform scanning working? (any sites changed structure/blocked?)
- [ ] Industry-specific sources checked for new listings

### Guardrails
- **Never exceed 25% intermediary ratio** without flagging Kay.
- **Never contact an owner directly** on a broker-sourced deal. Always go through the broker.
- **Never burn time on competitive auctions.** If a deal is clearly going to multiple bidders with higher offers, flag it but recommend pass.
- **Auto-reject sub-$1.5M revenue deals.** Any broker deal with stated revenue below $1.5M is silently archived. No exceptions for thesis fit, broker relationship, or niche signal. Too small.
</validation>

<success_criteria>
## Success Criteria

### Phase 1 (Testing — first 2 weeks)
- [ ] General platform scanning runs daily for all accessible platforms
- [ ] Industry-specific sources scanned for each active niche
- [ ] Slack pings include working links
- [ ] Niche signals generated weekly

### Phase 2 (Steady state)
- [ ] Intermediary channel stays at 15-25% of weekly deal flow
- [ ] At least 1 thesis-matching deal surfaced per week
- [ ] New introductions processed within 24 hours
- [ ] Intermediary network grows by 1-2 per month
- [ ] Platform list maintained (broken sites removed, new ones added)
- [ ] Industry-specific sources reviewed monthly for new platforms
</success_criteria>
