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
- **Buy-box docs** (Google Drive, `Deal Aggregator` folder) — single source of truth for all filter criteria. Read at the start of every run. Never use cached or hardcoded bands.
  - **Services Buy Box** — doc ID `14hf5QaKtcP_Um0u_P0LZyUM_zvv7haWVVkgGmRL9iyc` — applies to Premium Pest, Estate Management, Specialty Coffee Equipment, Art Storage, Private Art Advisory, High-End Commercial Cleaning, and all new-niche non-SaaS non-Insurance listings
  - **Insurance Buy Box** — doc ID `1lkxntRwn3FOPXig86qF36eNyUS0BfbMumfNuIyInD-M` — applies to Specialty Insurance Brokerage only
  - **SaaS Buy Box** — doc ID `1I8r8w0FPJUepfBxM6HM7V_q4ibmitybIBF6w6sMQumU` — applies to Vertical SaaS for Luxury and all new-niche SaaS listings
- **Industry Research Tracker** (Sheet: `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins`, WEEKLY REVIEW tab) — active niche list read at scan start
- **email-scan-results artifact** (`brain/context/email-scan-results-{date}.md`) — inbound deal emails classified by email-intelligence
- **skill/pipeline-manager** — Attio Intermediary Pipeline (broker stages, relationship status)

**Data Availability Rule (applies to every buy-box criterion):** Missing data on a listing is never grounds to auto-reject. Apply each criterion only when the corresponding field is disclosed. If a field is not disclosed, the deal is NOT rejected on that criterion — it is flagged for review. A deal with several "not disclosed" fields but no disclosed-and-failed fields still passes the buy-box gate.

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

**AI-powered marketplaces (confirmed scrapable):**
- DealFlow Agent (dealflowagent.com) — AI-powered M&A marketplace, industry-segmented, already in Channel 3 (Premium Pest Management)

**AI-powered marketplaces (need Kay to register first — scrapability TBD):**
- Acquire.com (acquire.com) — SaaS/digital-heavy. Likely login-gated. Register and re-test.
- BizScout (bizscout.com) — Partial public marketplace via "DealOS." Verified buyer tier promises exclusive access — test both tiers after register.
- Kumo (kumo.so) — Did not resolve on initial fetch; retest before adding.

**Deal-sharing communities:**
- Searchfunder (searchfunder.com) — member deal board + email digest. Kay has annual membership. Path: enable email alerts in notification settings → email-intelligence picks up digest → deal-aggregator classifies matches. Backend scraping not available on member tier.

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

**Step 0a — Load active niches + DealsX references (REQUIRED before scanning):**
Read the Industry Research Tracker WEEKLY REVIEW tab:
```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "'WEEKLY REVIEW'!A3:I20" -a kay.s@greenwichandbarrow.com --json
```
Row 3 is headers: Rank, Niche Hypothesis, Current Status, Outreach Channel, Score, QSBS, Target Pool, Quick notes, DealsX Niche. Filter for rows where Current Status starts with "Active" (Active-Outreach or Active-Long Term). For each active row, capture:
- "Niche Hypothesis" field (G&B's narrow thesis name — authoritative)
- "DealsX Niche" field (foreign-key reference to the DEALSX tab; may be blank)

**Step 0c — Load keywords from DEALSX tab (REQUIRED for listing matching):**
Read the DEALSX tab for the keyword corpus per niche:
```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "'DEALSX'!B5:I20" --json
```
Relevant DEALSX fields: "Niche" (Sam's broad DealsX-submitted names), "Quick notes" (Industries/Types sub-verticals), "Keywords" (pre-tokenized match corpus).

For each active niche from Step 0a, resolve its keyword corpus:
- IF the row's "DealsX Niche" field on WEEKLY REVIEW is populated → match that value against the "Niche" field on DEALSX → pull the "Quick notes" field AND the "Keywords" field from that DEALSX row as the primary corpus (Industries/Types sub-verticals + tokenized match terms). Also pull the WEEKLY REVIEW "Quick notes" field as supplementary signal — DEALSX is more robust and takes precedence, but WR Quick notes can add niche-specific color not captured on DEALSX. Combine all three into a single matching corpus.
- IF the "DealsX Niche" field on WEEKLY REVIEW is blank (e.g., Private art advisory firms — no DealsX equivalent) → build the matching corpus from the WEEKLY REVIEW row itself. Specifically:
  1. "Niche Hypothesis" field — full string + key noun phrases tokenized (e.g., "Private art advisory firms" → "art advisory", "art advisor", "private advisory", "art consulting", etc.)
  2. "Quick notes" field — extract industry-descriptive terms, business-model phrases, customer-profile language, and any named sub-verticals
  3. Any other populated fields on that WR row ("Target Pool", "Outreach Channel") that contain industry language
  Combine these into a match corpus for the niche. Log "DealsX reference blank for {niche}; corpus built from WR row (Niche Hypothesis + Quick notes)" in the scan artifact for visibility and calibration.

**Step 0b — Load buy-box criteria (REQUIRED before scanning):**
Read the three buy-box docs from the Deal Aggregator Drive folder. These are the single source of truth for all filter criteria. Never use cached or hardcoded bands; always re-read on every run so the skill reflects Kay's current criteria.
```bash
gog docs cat 14hf5QaKtcP_Um0u_P0LZyUM_zvv7haWVVkgGmRL9iyc > /tmp/buybox-services.txt
gog docs cat 1lkxntRwn3FOPXig86qF36eNyUS0BfbMumfNuIyInD-M > /tmp/buybox-insurance.txt
gog docs cat 1I8r8w0FPJUepfBxM6HM7V_q4ibmitybIBF6w6sMQumU > /tmp/buybox-saas.txt
```
Parse each doc's financial bands, structural requirements, industry hard-excludes, and geography filters. Each doc begins with the Data Availability Rule — absence of a disclosed field never auto-rejects; it flags for review.

**Category routing — which buy-box applies to which listing:**
- Specialty Insurance Brokerage listings → Insurance Buy Box
- Vertical SaaS listings (any vertical) → SaaS Buy Box
- All other listings (pest, estate mgmt, coffee, art storage, art advisory, cleaning, or new-niche non-SaaS non-Insurance) → Services Buy Box

1. Sub-agent visits each platform's listing page
2. Scrape new listings since last scan (track by listing ID or date)
3. For each listing, extract every field the listing discloses: company description, industry, revenue (or ARR for SaaS / commission revenue for insurance), EBITDA, asking price, geography, operating history, ownership structure, employee count
4. Determine category (Services / Insurance / SaaS) per routing above; apply the matching buy-box
5. Screen: for each buy-box criterion, either confirm pass (disclosed + passes), flag fail (disclosed + fails → auto-reject), or mark "not disclosed" (do not reject; flag for review)
6. Deal passes the gate if: no disclosed criterion fails AND no industry hard-exclude matches AND thesis or new-niche match exists
7. Two types of passing matches:
   - **Thesis match** — fits an active niche thesis from Step 0a. High priority.
   - **Buy-box match, new niche** — passes the buy-box gate but sits in an industry not on the active thesis list. Route to niche-intelligence as a discovery signal.

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
- [ ] Step 0b completed: all three buy-box docs were freshly read from Drive this run (Services, Insurance, SaaS). Cached or hardcoded bands = hard fail.
- [ ] Step 0c completed: keyword corpus resolved for EVERY active niche. For any niche where the WEEKLY REVIEW "DealsX Niche" field is blank, the corpus was built from the WR row itself (Niche Hypothesis + Quick notes + other populated fields). Niche-name-alone matching is NOT acceptable when other WR row data is available. This is a hard requirement.
- [ ] Every match includes: source, listing URL, company description, industry, revenue/EBITDA (or "not disclosed"), geography
- [ ] Listing URL is a working link (not a search results page or homepage)
- [ ] Each listing routed to the correct buy-box category (Services / Insurance / SaaS) per the routing rule
- [ ] Data Availability Rule enforced: no listing auto-rejected on a missing field. Auto-reject only triggers on disclosed-and-below or disclosed-and-failed criteria.
- [ ] Industry hard-excludes applied per the matching buy-box doc (Services / Insurance / SaaS)
- [ ] Match classified as "Thesis match" or "Buy-box match, new niche"
- [ ] No duplicate listings (dedup across platforms AND email inbound)
- [ ] Zero matches = report "No matches" — never fabricate
- [ ] Scan artifact logs, for each niche, which corpus path was used: "DealsX keywords" or "WR row enrichment (Niche Hypothesis + Quick notes)" — so underperforming niches can be calibrated next cycle

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
- **Buy-box filter criteria come from the three Drive docs, not from this SKILL.md.** Never hardcode revenue floors, EBITDA bands, margin floors, or industry excludes in the skill or subagent prompt. If a criterion needs to change, Kay edits the Drive doc — the skill picks it up on the next run.
- **Data Availability Rule is absolute.** A listing that doesn't disclose a field is never auto-rejected on that field. Flag for review, continue scoring against disclosed fields.
- **Hard-excludes apply per the matching buy-box doc's Industry Hard-Excludes section, when disclosed on the listing.** No external lists, no blacklists maintained — scope is pass-through review of existing deals only.
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
