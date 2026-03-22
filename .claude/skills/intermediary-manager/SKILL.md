---
name: intermediary-manager
description: "Manage the 20% intermediary deal channel — platform scanning, email screening, new intro processing, and niche signal detection. Flags matches for Kay, feeds signals to niche-intelligence."
user_invocable: true
context_budget:
  skill_md: 2500
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Manage the intermediary deal flow channel. Screen broker platforms and inbound listing emails against the buy box, surface matches, and detect niche signals.

This is the 20% channel. It supplements proprietary outreach (target-discovery + outreach-manager), never replaces it. Broker deals go to 3000+ buyers — we rarely win competitive bids. The value here is: early detection of thesis-matching deals, niche signal intelligence, and growing the intermediary network over time.

**This skill does NOT:**
- Create targets on the target list (broker deals go through broker, not direct)
- Draft outreach to owners (broker is the gatekeeper)
- Enter deals into Attio (pipeline-manager handles that when NDA is signed)
- File documents into ACTIVE DEALS folders (pipeline-manager handles that)

**This skill DOES:**
- Scan searchable broker platforms daily for buy-box matches
- Screen inbound deal flow emails (blasts vs. direct)
- Flag matches via Slack (#active-deals) with link to listing
- Archive non-matching blasts silently
- Surface direct broker-to-Kay emails that need a response
- Feed listing patterns to niche-intelligence as market signals and new thesis ideas
- Process new broker introductions (research platform, assess scrapability, add to rotation)

**Inputs from other skills:**
- **skill/niche-intelligence** — active thesis criteria, buy box, industry scorecards
- **skill/pipeline-manager** — Attio Intermediary Pipeline (broker stages, relationship status)

**Outputs to other skills:**
- Buy-box matches → Slack notification → Kay signs NDA → pipeline-manager detects and takes over
- Niche signals → skill/niche-intelligence (new thesis ideas, market patterns)
- New intermediary entities → Attio Intermediary Pipeline via pipeline-manager
</objective>

<channels>
## Three Channels

### Channel 1: Platform Scanning (Daily)
Scan searchable broker platforms for new listings matching the buy box.

**Platform scan + email listings (both channels):**
- Everingham & Kerr (everkerr.com) — most active broker, email listings
- Business Exits (businessexits.com/listings/) — email + searchable
- Benchmark International (embracebenchmark.com/search-deals) — email + searchable
- Rejigg (rejigg.com) — automated deal match emails + searchable
- Quiet Light (quietlight.com) — email + searchable
- Flippa (flippa.com) — email alerts + searchable
- Empire Flippers (empireflippers.com) — email alerts + searchable
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
1. Sub-agent visits each platform's listing page
2. Scrape new listings since last scan (track by listing ID or date)
3. For each listing, extract: company description, industry, revenue, EBITDA, asking price, geography, employee count
4. Screen against buy box criteria (from niche-intelligence active theses)
5. Two types of matches:
   - **Thesis match** — fits an active niche thesis (e.g., TCI brokerage, insurance compliance). High priority.
   - **Buy-box match, new niche** — fits the financial buy box ($1-5M EBITDA, $3-20M revenue, independently owned) but in a niche we haven't evaluated. Route to niche-intelligence as a discovery signal.

**When a match is found:**
```bash
curl -s -X POST "$SLACK_WEBHOOK_ACTIVE_DEALS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Broker listing match\nSource: {Platform}\nCompany: {Name or blind profile}\nIndustry: {Industry}\nRevenue: {Revenue} | EBITDA: {EBITDA}\nMatch type: {Thesis match / Buy-box new niche}\n{Link to listing}\n\nAction: Sign NDA on platform to receive CIM."}'
```

**Platform rotation:** If intermediary channel exceeds 25% of weekly targets (tracked on Weekly Tracker), reduce platform scanning to every other day and only surface exact thesis matches.

### Channel 2: Inbound Email Screening (Overnight)
Screen deal flow emails that arrive in Kay's inbox.

**Email classification (CRITICAL):**
Every email labeled "DEAL FLOW" must be classified as one of:

1. **BLAST** — BCC'd distribution, generic greeting, "New Listing" subject, sent to broker's full network of 3000+. Agent screens against buy box. Match → Slack ping. No match → archive silently. Kay never sees these unless there's a match.

2. **DIRECT** — Addressed to Kay by name, references prior conversation or specific criteria Kay shared, expects a response, may include "Introduction" or "RE:" in subject, sometimes has CIM/teaser attached. These ALWAYS get surfaced to Kay — never auto-archived. Present in morning briefing via pipeline-manager's Inbound Intermediary Deal Detection flow.

3. **NEWSLETTER** — Industry newsletters, deal roundups, educational content (e.g., Helen Guo / SMB Deal Hunter). Not actionable deal flow. Move to a "DEAL FLOW/ARCHIVE" label. Scan for niche signals only — patterns in what industries are being listed, new niche ideas.

**Pattern detection for classification:**
- BCC header present → BLAST
- Kay's name in greeting ("Hi Kay", "Dear Kay") + personalized context → DIRECT
- Unsubscribe link + no personalization → NEWSLETTER or BLAST
- Sender in Attio Intermediary Pipeline at "Warmed" or higher + personalized → DIRECT
- Sender not in Attio + mass-email patterns → BLAST

**Guardrail:** When uncertain, default to DIRECT. It's better to surface an email Kay doesn't need than to archive one that needed a response.

### Channel 3: New Introductions
When Kay receives a broker introduction (someone introduces her to a new intermediary):

1. **Detect** — Agent scans for intro patterns: "I'd like to introduce you to...", "Connecting you with...", "Meet [name] who...", CC'd introductions
2. **Research** — Visit the broker's website. Determine:
   - Do they have a searchable listing platform?
   - What industries/deal sizes do they focus on?
   - Are they relevant to our active theses?
3. **Add to system:**
   - Create entity in `brain/entities/{slug}.md`
   - Add to Attio Intermediary Pipeline at "Identified"
   - If scrapable platform → add to Channel 1 scanning rotation
   - If email-only deal flow → note for Channel 2 monitoring
4. **Draft response** — Warm reply in Superhuman (thank introducer, express interest to broker, mention search criteria). Per feedback: short, offer NDA, don't over-explain.
5. **Update this skill** — Add new platform to the scanning list in Channel 1 if applicable
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
- [ ] Buy-box screen applied: $1-5M EBITDA, $3-20M revenue, independently owned. Anything outside these ranges is NOT a match regardless of industry fit.
- [ ] If zero matches found across all platforms, report "No matches" — don't fabricate or stretch criteria to surface something

**If any check fails:** Fix before sending Slack notification. A bad link or wrong match wastes Kay's time.

### Email Classification Stop Hook
After classifying deal flow emails, verify:
- [ ] Every DIRECT email is surfaced — zero false negatives on this category
- [ ] BLAST classification confirmed by at least 2 signals (BCC header, generic greeting, mass-send pattern)
- [ ] No email from a sender in Attio at "Warmed" or higher stage was classified as BLAST
- [ ] NEWSLETTER classification only for actual newsletters (recurring, editorial content, not deal-specific)
- [ ] Every archived email logged with classification reason

**If uncertain on classification:** Default to DIRECT. Surface it. Let Kay decide.

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
- [ ] All DEAL FLOW emails classified (BLAST/DIRECT/NEWSLETTER)
- [ ] Matches sent to Slack with links
- [ ] Non-matches archived
- [ ] Direct emails surfaced in morning briefing
- [ ] New introductions processed (if any)

### Weekly (on Weekly Tracker)
- [ ] Intermediary vs proprietary ratio calculated
- [ ] If >25%, throttle platform scanning
- [ ] Niche signals compiled and sent to niche-intelligence
- [ ] Intermediary pipeline stages reviewed (any gone cold?)
- [ ] Platform scanning working? (any sites changed structure/blocked?)

### Guardrails
- **Never auto-archive DIRECT emails.** When in doubt, surface it.
- **Never exceed 25% intermediary ratio** without flagging Kay.
- **Never contact an owner directly** on a broker-sourced deal. Always go through the broker.
- **Never burn time on competitive auctions.** If a deal is clearly going to multiple bidders with higher offers, flag it but recommend pass.
</validation>

<success_criteria>
## Success Criteria

### Phase 1 (Testing — first 2 weeks)
- [ ] Platform scanning runs daily for all 16 platforms
- [ ] Email classification accuracy >90% (verify with Kay)
- [ ] Zero DIRECT emails accidentally archived
- [ ] Slack pings include working links
- [ ] Niche signals generated weekly

### Phase 2 (Steady state)
- [ ] Intermediary channel stays at 15-25% of weekly deal flow
- [ ] At least 1 thesis-matching deal surfaced per week
- [ ] New introductions processed within 24 hours
- [ ] Intermediary network grows by 1-2 per month
- [ ] Platform list maintained (broken sites removed, new ones added)
</success_criteria>
