---
name: intermediary-manager
description: "Manage the 20% intermediary deal channel — platform scanning, new intro processing, and niche signal detection. Flags matches for Kay, feeds signals to niche-intelligence. Email scanning (broker classification) is handled by pipeline-manager."
user_invocable: true
context_budget:
  skill_md: 2500
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Manage the intermediary deal flow channel. Screen broker platforms against the buy box, process new introductions, surface matches, and detect niche signals.

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

**Platform scan + email listings (both channels):**
- Everingham & Kerr (everkerr.com) — most active broker, email listings
- Business Exits (businessexits.com/listings/) — email + searchable
- Benchmark International (embracebenchmark.com/search-deals) — email + searchable
- Rejigg (rejigg.com) — automated deal match emails + searchable
- Quiet Light (quietlight.com) — email + searchable
- Flippa (flippa.com) — email alerts + searchable
- DealForce (dealforce.com) — email alerts + searchable

**Platform scan only (no email, agent must scrape):**
- BizBuySell (bizbuysell.com) — Kay has account
- FE International (feinternational.com) — Kay has account
- IAG M&A Advisors (iagmerger.com) — Kay has account
- Gottesman (gottesman-company.com)
- ProNova Partners (pronovapartners.com)
- Woodbridge International (woodbridgegrp.com)
- Paine Pacific (painepacific.com)
- Graphic Arts Advisors (graphicartsadvisors.com)
- Website Closers (websiteclosers.com)

**Email only (no searchable platform):**
- Viking Mergers (vikingmergers.com) — periodic deal blasts

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

### Channel 2: New Introductions
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
   - If scrapable platform → add to Channel 1 scanning rotation
   - If email-only deal flow → note as email-only intermediary (pipeline-manager handles email scanning)
4. **Draft response** — Warm reply in Superhuman (thank introducer, express interest to broker, mention search criteria). Per feedback: short, offer NDA, don't over-explain.
5. **Update this skill** — Add new platform to the scanning list in Channel 1 if applicable

### New Intermediary Surfacing

When the morning scan detects intermediaries at "Identified" stage in Attio, classify and surface them with specific next steps:

1. **Classify type:**
   - **Platform** (has a website with deal listings, e.g., Gottesman, ProNova) → "Next step: register as buyer on their site"
   - **Boutique** (small advisory firm, NDA-gated listings, e.g., Paine Pacific) → "Next step: send broker intro email to managing director"
   - **Association** (industry group, trade org) → "Next step: research membership and deal flow programs"

2. **Surface in morning briefing** with the specific next step:
   - "New intermediary: {name} — {type} with {detail}. Next step: {action}."

3. **Track registration status:** After Kay registers on a platform or sends a broker email, note it on the intermediary’s Attio record. Watch for deal flow within 4 weeks of registration.

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
- [ ] All platforms scanned (or on rotation schedule if throttled)
- [ ] Matches sent to Slack with links
- [ ] Non-matches archived
- [ ] New introductions checked in `brain/context/email-scan-results-{date}.md` (if any)

### Weekly (on Weekly Tracker)
- [ ] Intermediary vs proprietary ratio calculated
- [ ] If >25%, throttle platform scanning
- [ ] Niche signals compiled and sent to niche-intelligence
- [ ] Intermediary pipeline stages reviewed (any gone cold?)
- [ ] Platform scanning working? (any sites changed structure/blocked?)

### Guardrails
- **Never exceed 25% intermediary ratio** without flagging Kay.
- **Never contact an owner directly** on a broker-sourced deal. Always go through the broker.
- **Never burn time on competitive auctions.** If a deal is clearly going to multiple bidders with higher offers, flag it but recommend pass.
- **Auto-reject sub-$1.5M revenue deals.** Any broker deal with stated revenue below $1.5M is silently archived. No exceptions for thesis fit, broker relationship, or niche signal. Too small.
</validation>

<success_criteria>
## Success Criteria

### Phase 1 (Testing — first 2 weeks)
- [ ] Platform scanning runs daily for all 17 platforms
- [ ] Slack pings include working links
- [ ] Niche signals generated weekly

### Phase 2 (Steady state)
- [ ] Intermediary channel stays at 15-25% of weekly deal flow
- [ ] At least 1 thesis-matching deal surfaced per week
- [ ] New introductions processed within 24 hours
- [ ] Intermediary network grows by 1-2 per month
- [ ] Platform list maintained (broken sites removed, new ones added)
</success_criteria>
