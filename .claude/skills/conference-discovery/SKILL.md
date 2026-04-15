---
name: conference-discovery
description: "Weekly conference discovery, registration, and attendee list processing. Finds conferences, registers Kay, processes attendee/exhibitor lists into targets. Hands targets to outreach-manager."
user_invocable: true
context_budget:
  skill_md: 3000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Get Kay in front of business owners every week. Conferences are the highest-ROI channel for direct owner conversations. This skill handles discovery, registration, and attendee list processing. All outreach (pre-conference emails, post-conference follow-ups) is handled by skill/outreach-manager.

Target rhythm: 1 conference every Monday. Tuesday/Wednesday NYC-only as backup. Thursday possible but less preferred.

Reference: Colin Woolway and Will Gallagher attended 1-2 conferences/week and landed their acquisition. Kay is a solo searcher with a lean team (Claude, analyst, VA, bookkeeper). Claude owns conference logistics end-to-end.

**Outputs to other skills:**
- Processed attendee/exhibitor target lists → skill/outreach-manager (conference outreach subagent)
- Post-conference conversation data (Granola transcripts + notes) → skill/outreach-manager (conference outreach subagent)
- New contacts → Attio Active Deals at appropriate stage → skill/pipeline-manager takes over
</objective>

<essential_principles>
## How It Works

### Weekly Rhythm

**Sunday night (automated):** Claude surfaces next 2-4 weeks of conference options. Kay reviews Monday morning during travel to conference and picks next week's.

**T-minus 2 weeks:** Register. Begin attendee/exhibitor list acquisition.

**T-minus 1 week:** Process attendee list into scored target list. Hand targets to outreach-manager's conference outreach subagent for pre-conference emails.

**Day of conference:** Kay attends. Runs Granola at booths to capture conversations. Talks to as many owners as possible within 2 hours.

**Next morning:** Claude processes Granola transcripts + Kay's notes. Hands conversation data to outreach-manager's conference outreach subagent for follow-up drafting. Adds contacts to Attio.

### Scheduling Constraints

| Day | Available | End time |
|-----|-----------|-----------|
| Monday | Day + evening (only night Kay can do evenings) | Flex / late |
| Tuesday | Daytime only | 2:00pm |
| Wednesday | Daytime only | 2:00pm |
| Thursday | Daytime only | 5:00pm |
| Friday | Daytime only | 3:00pm |

### Geography

**Priority 1:** NYC (walk, subway, car)
**Priority 2:** Long Island, NJ, CT (car / short train)
**Priority 3:** Pennsylvania (Philly metro, train)
**Excluded:** Boston, DC, all Midwest, West Coast. Only exception: if a uniquely high-signal event occurs outside priority zones, surface with explicit flag for Kay's override decision.

### Event Format Priority (CRITICAL — set 2026-04-15)

Kay's preferred event format is **grass-roots intermediary networking**, NOT big industry conferences. Her unlock came from the Greg Donus / Smart Tours story (Helen Guo podcast): he found his acquisition via a Long Island broker breakfast → insurance contact → BDO connector → accountant → $25M deal. Kay's strategy mirrors this.

**Priority 1 — Intermediary networking (PRIMARY):**
**Format constraint (HARD):**
- **Mon:** full-day flex, including evening events (happy hours OK)
- **Tues:** daytime only, must end by 2:00pm
- **Wed:** daytime only, must end by 2:00pm
- **Thu:** daytime only, must end by 5:00pm
- **Fri:** daytime only, must end by 3:00pm

Breakfast, coffee, morning, and lunch are the default priority. Monday is the ONLY day Kay can do evening events — she is a solo parent, Tues–Fri evenings require advance babysitter planning and will not be surfaced without explicit Kay ask. Full-day conferences are OK within the per-day end time.

- Broker breakfasts (Long Island 7am diner rotation and similar)
- Morning M&A meetings — check if firms have AM versions of their evening happy hours
- ACG chapter breakfasts (NYC, NJ, East, Boston) + ACG M&A Source morning speed networking
- XPX (Exit Planning Exchange) chapter breakfasts
- AM&AA (Alliance of M&A Advisors) breakfasts
- Accounting firm morning events (BDO, Grant Thornton, Marcum, CohnReznick, EisnerAmper — client breakfasts, CPE breakfasts)
- M&A law firm breakfasts (Goodwin, Proskauer, Kirkland, Morgan Lewis — CLE breakfasts, client breakfasts)
- Wealth manager breakfasts/lunches serving HNW/SMB owners (must end by 1:30pm)
- Capital Roundtable breakfasts
- NYIC morning events only

**Priority 2 — Vertical industry conferences:**
- CMAA (Private Club mgmt), boat/yacht shows, Menopause-health SaaS events, ArtTable, family-office events
- Use the DEALSX tab for aperture on which verticals to hunt
- Keep these rare — 1-2/month max — because they're expensive, exhausting, and lower-density for intermediary meetings

**Priority 3 — General SMB owner gatherings:**
- ETA events, SBA conferences, local business expos

**De-prioritized (do NOT surface without explicit Kay ask):**
- Big industry conferences (SaaStr, HIMSS, major ETA flagships) — too expensive, too low-density for relationship building

### Event Criteria Filter

Before surfacing any event to Kay, check:
- **Cost:** under $100 preferred; $100-500 OK for high-signal; flag anything over $500
- **Duration:** 2-3 hours preferred; willing to do 4-6 hour if NYC
- **Format:** breakfast / coffee / lunch / happy hour / speed networking (top priority); conference/panel (secondary)
- **Geography:** NYC + Long Island + NJ + CT + Philly + Boston (per scheduling table above)
- **Attendee profile:** must skew intermediary (brokers, M&A advisors, CPAs, M&A lawyers, wealth managers, bankers) OR SMB owner clusters (for vertical events)

### Cadence

Target **1 event/week minimum**. More if discovery yields more viable events (Kay's physical capacity is high for short local events; discovery rate is the constraint).

### Shared pipeline with river-guide-builder

Conference-discovery and river-guide-builder operate on the same data source: event attendee lists. Every broker-breakfast attendee is simultaneously a potential river guide AND a potential deal source. Run them as one pipeline, not two separate searches. Post-event protocol: within 48 hours, every attendee Kay met gets (a) vault entity, (b) Attio People record, (c) `relationship_type` tagged, (d) `nurture_cadence` assigned, (e) next_action if Kay committed to something.

### Niche Targeting (for Priority 2 vertical conferences only)

When searching for Priority 2 vertical industry conferences, read **BOTH tabs** on the Industry Research Tracker:

1. **WEEKLY REVIEW tab** — Kay's curated sub-niches (active work queue). Priority order:
   - Active-Diligence and Active-Outreach niches first
   - Under Review niches only if active niches exhausted
2. **DEALSX tab** — Sam's 6 high-level buckets + ~45 sub-niches (broader aperture). Use this tab to find vertical-specific conferences that Kay's curated rows don't surface. Examples: CMAA (Private Club mgmt), boat/yacht shows (Marina/Yacht SaaS + Yacht Household Mgmt), Menopause-health conferences (Menopause Clinic SaaS), ArtTable (Fine Art Insurance), family-office events (Family Office Operational Services).

### Storage

All events go into the existing **Conference Pipeline** Google Sheet (ID: 1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY). Do not create a new sheet. Add a column if needed for event format (breakfast / speed-networking / happy hour / conference).

The two tracker tabs serve different purposes: WEEKLY REVIEW = Kay's work decisions; Sam's DealsX Universe = conference-search aperture (broader net so dedicated vertical events aren't missed). Run parallel searches against both, then dedupe results before presenting.

**Do NOT hardcode niches here.** Always read the current active niches from the Industry Research Tracker at runtime:
```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!B3:D20" -a kay.s@greenwichandbarrow.com -j
```
Filter for rows where Current Status (col D) contains "Active". Use the Niche Hypothesis (col B) as the search term.

**Why Active-Diligence triggers conference discovery:** Conferences are a form of customer validation. Attending an industry conference and talking to practitioners is diligence — you learn how the niche works, what matters, who the players are. This makes conferences a natural fit for the Active-Diligence phase, not just Active-Outreach.

### Audience Filter (CRITICAL — apply before anything else)

Only surface conferences where the attendees are one of these two groups:
1. **Owners of businesses G&B wants to buy** — insurance agency/brokerage owners, TCI broker principals, art advisory firm owners, collection management firm owners
2. **Clients of businesses G&B wants to buy** — people who hire those firms (family offices, UHNW individuals, corporate risk managers, art collectors, estate planners who refer to art advisors)

If the audience is primarily vendors, tech providers, carrier executives, curators, academics, industry analysts, or other people who are NOT owners or clients of target businesses — do NOT put it on the sheet. This filter eliminates InsurTech vendor conferences, museum professional events, general business expos, and industry analyst summits.

**Ask yourself:** "Will Kay meet someone who either owns a business she could acquire, or hires the kind of business she wants to acquire?" If no, skip it.

### Owner Verification Gate (CRITICAL — learned from InsurTech Spring 2026)

Before recommending ANY conference, verify that **target business owners are confirmed on the exhibitor/booth list or attendee/meetup list.** A conference in the right industry is not enough. The exhibitor list must contain actual acquisition targets, not just vendors and tech providers serving that industry.

**Process:**
1. Get the exhibitor/booth list and attendee list (if available)
2. Cross-reference against G&B's target profile: independently-owned businesses in active niches
3. Count confirmed owner matches. If zero owners on the list, do NOT recommend the conference.
4. In the recommendation, list the specific owners/companies Kay would target at booths

**InsurTech Spring 2026 lesson:** Conference was insurance-industry-adjacent but exhibitors were all InsurTech vendors (AI, SaaS, data platforms). Zero brokerage owners had booths. Conference was a waste of time. The audience filter alone is not sufficient — must verify the exhibitor list contains actual targets.

### Conference Types (all qualify if they pass the audience filter)
- **Association chapter meetings and dinners** (HIGHEST VALUE — intimate, business owners present, real conversations, recurring monthly. One membership = 10+ events/year)
- **Industry niche meetups and gatherings** (small groups of practitioners in the exact niche — TCI brokers dinner, art advisory roundtable, insurance agent networking)
- Trade shows with exhibitor booths (expo halls where owners have tables)
- Regional industry conferences (30-200 people ideal)
- Client-facing events where target business owners exhibit or network
- **Supplier/vendor events where target owners are buyers** — e.g., chemical supplier hosts pest control operators for product training. The owners attend as customers.
- **Certification and continuing education events** — owners often attend in person for license renewals, CE credits, or new certifications. These are small, regional, and full of practitioners.
- **Award dinners and galas** — "Best of" industry awards, chamber of commerce business awards. Owners show up to be recognized or network with peers.
- **Local business association meetups** — BNI chapters, Rotary, local chamber events. Not niche-specific but owners attend. Lower hit rate, higher frequency.

### Broadening for Conference-Thin Niches

Some niches (blue collar services, fractional/advisory, niche storage) have very few formal conferences. When the standard search returns zero results for a niche, escalate to these alternative gathering types:

1. **Supplier-hosted events** — search "{niche} supplier training event", "{niche} manufacturer demo day". Equipment/chemical/materials suppliers regularly host their customers (the owners) for product demos, training days, and networking dinners.
2. **State/local licensing and CE events** — search "{niche} continuing education {state}", "{niche} license renewal class {region}". In-person CE classes are intimate and full of owner-operators.
3. **Facebook/LinkedIn groups with meetups** — search "Facebook group {niche} owners {region}", "LinkedIn group {niche} professionals". Many niche industries organize informal meetups through social groups. Check for pinned event posts.
4. **Franchise/buying group meetings** — search "{niche} franchise convention", "{niche} buying group meeting". Franchise systems and cooperative buying groups hold annual or quarterly meetings where independent operators gather.
5. **Adjacent-industry conferences** — if pest management has no events, check property management, facilities management, or real estate investor conferences where pest control owners exhibit or attend as vendors/partners.
6. **State association chapter events** — many niche industries have state-level associations with regular chapter dinners that don't appear on conference aggregators. Go directly to the state association website.

**Report gaps explicitly.** If after the expanded search a niche still has zero upcoming gatherings, report it with what was searched and recommend alternative owner-access strategies (direct outreach, warm intros, LinkedIn engagement).

### Niche Association Registry

Each niche's target sheet should have an **"Associations" tab** listing relevant professional associations. This is the primary source for conference discovery — check association event calendars before using aggregators.

**Associations tab columns:**
| Column | Header |
|--------|--------|
| A | Association Name |
| B | Website |
| C | Events Page URL |
| D | Scope (National / State / Local) |
| E | Membership Cost |
| F | Member? (Y/N) |
| G | Notes |

**When to populate:** During the first discovery cycle for a niche, research and populate the Associations tab. Update it whenever new associations are discovered. This tab is also used by deal-aggregator (association leaders as intro sources) and niche-intelligence (understanding industry structure).

**How to find associations:**
```
WebSearch: "{niche} professional association"
WebSearch: "{niche} trade association United States"
WebSearch: "{niche} industry association {state}"
WebSearch: "{niche} owners association"
```

Capture national associations first, then state/regional chapters in the Northeast corridor (NY, NJ, CT, PA, MA).

### Search Strategy — Prioritize Associations, Then Expand

The best source of weekly conferences is **association event calendars**, not conference aggregators. For each active niche, read the Associations tab first and check each association's events page directly.

**Step 0: Read the Associations tab** on the niche's target sheet. If it's empty, populate it first (see above), then proceed to Step 1.

**Search pattern for each niche (standard):**
```
# First: check each association's events page from the Associations tab
# Then supplement with broader searches:
WebSearch: "{niche} professional association"
WebSearch: "{niche} industry association events {region}"
WebSearch: "{niche} chapter meeting {city} {month} {year}"
WebSearch: "{niche} networking event {city}"
```

**Expanded search for conference-thin niches (when standard returns <2 results):**
```
WebSearch: "{niche} owner meetup {region}"
WebSearch: "{niche} supplier training event {year}"
WebSearch: "{niche} continuing education in person {state}"
WebSearch: "{niche} awards dinner {region} {year}"
WebSearch: "{niche} franchise convention {year}"
WebSearch: "{adjacent industry} conference exhibitors {niche}"
WebSearch: "Facebook group {niche} owners {state}"
```

Then visit each association's website → Events/Calendar page → capture all upcoming events.

**Skip "pay to be in the room" events** where non-members pay premium rates ($2,000+) to access a curated audience. These attract vendors, not peers. The pricing model itself is the red flag — if it's free for one group and expensive for everyone else, you're the product.

### Conference Selection Preferences
- **Smaller > bigger.** 50-500 attendees is the sweet spot. NAEPC (~400) is the gold standard.
- **Booth/expo format > panel/speaker format.** Kay needs face time with owners at their tables, not keynote audiences. Kay strongly prefers expo halls — walkable floors where companies have booths/tables. When evaluating, always check whether the event has a dedicated expo hall, exhibition area, or "expo safari" component. Flag this clearly in Agent Notes.
- **Industry association chapter meetings are ideal.** Intimate, business owners present, real conversations.
- **Avoid redundant conferences from the same organizer.** Multiple PIA chapter meetings or different association events in the same niche are fine — different attendees each time. But don't surface the same conference company's events twice (e.g., two InsurTech NY events in one quarter).
- **Large conferences (500+) are "Register Only" candidates** — get the attendee list for outreach, don't attend.
- **Budget: $10K annual T&E ($20K buffer available).** Evaluate each conference on its merits — value of attendees, content quality, agenda, location, niche relevance. A $1,500 event with 200 target-rich owners is a better spend than a $50 event with no one relevant. Show registration cost in the Pipeline sheet so Kay can make informed decisions.
- **Association memberships worth joining** if they unlock regular chapter meetings with business owners (e.g., EPCNYC for estate planners, local insurance agent associations). Most are $200-500/year.

### Register-Only Events
Some conferences are worth registering for without attending — to access the attendee/exhibitor list for outreach. Flag these separately. Large conferences (1,000+) default to this category unless booth format.

### Association Memberships
Some events require association membership. Kay is open to joining if it unlocks multiple relevant conferences. Flag membership cost and number of accessible events. Ask Kay before purchasing.

## Architecture

Claude handles all phases directly (no sub-agents needed). The workflow is sequential and runs weekly.

## Team Roles
- **Claude:** Discovery, registration logistics, attendee scraping, target scoring, pipeline integration
- **Kay:** Picks conferences, attends, provides post-conference notes
- **Outreach Manager:** All email drafting (pre-conference and post-conference follow-ups)
- **Analyst:** Not involved (focused on financial analysis and deck building)
- **VA (JJ):** Not involved in conference discovery (focused on cold calling and validation)
</essential_principles>

<discovery>
## Phase 1: Conference Discovery

Run weekly (Sunday night, ready Monday morning). Find conferences for the next 2-6 weeks.

### Search Strategy

**Step 1: Search top 5 niches**
For each active niche, search for upcoming conferences:
```
WebSearch: "{niche} conference {month} {year} {region}"
WebSearch: "{niche} trade show {month} {year}"
WebSearch: "{industry association} events calendar {year}"
WebSearch: "{niche} expo {city} {year}"
```

Target sources:
- 10times.com (conference aggregator)
- TradeShowNews.com
- EventBrite (filter: Business, Conferences)
- Industry association websites (check "Events" pages)
- Local chamber of commerce event calendars

**Step 2: If top 5 exhausted, expand**
Search adjacent niches from the runner-up list in the Industry Research Tracker.

**Step 3: General business owner events**
Search for ETA networking events, SBA conferences, local business expos in the northeast corridor.

### Output: Conference Options List

For each conference found, capture:
- Event name
- Date(s) and hours
- Location (venue, city, state)
- Travel feasibility (walk/train/flight + estimated travel time)
- Registration cost
- Registration deadline
- Estimated attendance / number of exhibitors
- Attendee list availability (public, post-registration, or unavailable)
- Association membership required? (Y/N, cost)
- Niche relevance (which of the top 5 it maps to)
- Conference website URL
- Register-only candidate? (Y/N)

Prepare rows for the Conference Pipeline Google Sheet (do NOT write yet — the Stop Hook in the Validation section requires Kay's approval first). All columns have dropdown data validation where applicable.

**One conference = one row.** Multi-day conferences get a single row with the date range in column A (e.g., "2026-05-03 - 05-06"). Never create separate rows for different days of the same conference. Kay makes one attend/skip decision per conference, not per day. Which specific day she attends is her choice, not a pipeline decision.

**Column layout:**
A: Date of Conference | B: Event Name | C: Location | D: Travel | E: Niche | F: Registration Cost | G: Reg Deadline | H: Est. Attendees | I: Attendee List | J: Website | K: Status | L: Agent Rec | M: Decision | N: Notes | O: Agent Notes

**Dropdown columns:**
- **Status (col K):** Discovered, Evaluating, Registered, Prep Complete, Attended, Skipped
- **Agent Rec (col L):** Attend, Register Only, Skip, Investigate — Claude's recommendation
- **Decision (col M):** Attend, Register Only, Skip — Kay's final call

**Agent Notes (col O):** Far right column. Claude's rationale for the recommendation. Separate from the rec itself so it doesn't clutter.

**Notes (col N):** Kay's own notes column.

Claude fills in: all columns A-L, O (everything except Decision and Notes).
Kay fills in: Decision (M) and Notes (N).

When Kay marks Decision = Skip, Claude moves the row to the Skipped tab.

### Auto-Archival (runs every discovery cycle)

Before adding new conferences, scan the Pipeline tab and auto-move rows off Pipeline when:
1. **Decision = Skip** → move to **Skipped** tab
2. **Status = Attended** (or Decision = Attend AND date is past) → move to **Attended** tab
3. **Date is past AND no Decision/Status indicating attendance** → move to **Skipped** tab (conference passed without attending)

**Process:**
1. Read all Pipeline rows
2. Identify rows matching any archival criteria above
3. Route each row to the correct tab (Attended or Skipped)
4. Delete matching rows from the Pipeline tab
5. Re-sort all three tabs chronologically after changes
6. Report in Slack notification: "{n} moved to Attended, {n} moved to Skipped"

This keeps the Pipeline tab clean — only future conferences that still need decisions or action.

### Conference Calendar

Maintain in the **Conference Pipeline Google Sheet** (see references/drive-locations.md).

**Three tabs:**
- **Pipeline** — future conferences only: Discovered through Registered/Prep Complete. Active decisions and upcoming events.
- **Attended** — conferences Kay attended. Permanent record of attendance for debrief, follow-up tracking, and ROI assessment.
- **Skipped** — conferences Kay passed on or that passed without attending.

Statuses: Discovered, Evaluating, Registered, Prep Complete, Attended, Skipped

**Sort order:** Always chronological — earliest/closest date at top, farthest away at bottom.

### Slack Notification (end of Phase 1)

After discovery is complete, Kay has approved the proposed changes via the Stop Hook, sheet is updated, and sort validation passes, send a Slack notification to the SVA channel. See Validation section (Step 5) for the notification format and webhook details.
</discovery>

<registration>
## Phase 2: Registration & Attendee List Acquisition

After Kay approves a conference:

### Registration
1. Provide direct registration link
2. Create Motion task: "Register for {conference name}" with deadline 2 days before registration closes
3. Create Drive subfolder in RESEARCH/CONFERENCES: `gog drive mkdir "{CONFERENCE NAME}" --parent "18H0L-5UgHObt_0Reb6YlRshbWakEozk5"` — all conference materials live here (attendee lists, target list, debrief note, slides, reports)
4. If association membership required, present cost and ask Kay for approval first
5. Update conference calendar status to "Registered"

### Attendee/Exhibitor List
1. Check conference website for public exhibitor/sponsor list
2. If list is behind registration wall, flag for Kay to download after registering
3. If list is a PDF, extract to structured data (company, person, title, booth)
4. If list is a web page, scrape exhibitor directory

### List Processing
```
For each exhibitor/attendee:
  1. Company name + person name + title
  2. Web search: "{company name}" for basic info (what they do, size)
  3. Check if owner/operator (not a vendor, not an employee)
  4. Cross-reference Attio: already in pipeline? Already a contact?
  5. If new + owner + niche-relevant → add to target list
```

Store processed list in vault: `brain/outputs/{date}-{conference-slug}-targets.md`
</registration>

<target_scoring>
## Phase 3: Target Scoring & Handoff

### Target Scoring

Score each target using the **G&B Company Scorecard** (10 criteria, 1-10 weighted scale). See `niche-intelligence/references/company-scorecard.md` for full rubric.

For conference attendees, not all criteria will have data available pre-conference. Score what you can from public information (value proposition, market size, revenue concentration, technology) and flag unknowns. A partial score is fine for prioritizing pre-conference outreach — the full scorecard gets completed after the conversation.

Additional conference-specific filters:
- **Owner presence** — confirmed business owner/operator at booth (not a vendor or employee)
- **Not already in pipeline** — new contacts get priority

Present top 10 to Kay with scores. She selects 5-10 for pre-conference outreach.

### Handoff to Outreach Manager

Pass approved targets to skill/outreach-manager's conference outreach subagent with:
- Company name, person name, title, email
- Conference name, date, booth number (if applicable)
- Scoring notes and research context
- Whether pre-conference email or post-conference follow-up

### Conference Prep Doc (Saturday before Monday conferences)

If a Monday conference has scheduled in-person meetings or outreach targets attending, generate a Conference Prep doc Saturday night. Save to the conference's Drive folder (RESEARCH/CONFERENCES/{CONFERENCE NAME}).

**Template:** Conference Prep Template (Drive ID: `1nAm1BWsnomiuwDAd7km4Ur4kLUqfqrBxoRlea8MiUH8`) in G&B MASTER TEMPLATES. Copy to the conference folder and populate.

**Structure — two sections:**

**Scheduled Meetings** — for each confirmed meeting:
- **Name, company, role**
- **How they got on your radar** — outreach response, attendee list match, intro, etc.
- **Key context** — what they do, why they're relevant, any prior touchpoints (emails, calls, Attio history)
- **What you want to get out of the conversation** — specific questions, information to confirm, relationship goal

**Outreach Targets Attending** — for targets who were outreached to pre-conference:
- Same structure as above, plus outreach status (email sent, response received, no response)

**Conference Notes** — general intel: what to expect, layout, key sessions, networking opportunities.

Kay reviews this Sunday afternoon on MacBook/iMac. No Slack notification — she knows to check the conference folder.

### Post-Conference Data Capture

**Day of conference:** Kay captures booth conversations via:
1. **Granola** running on phone at each booth — transcripts auto-ingest into brain/calls/
2. **Manual notes** — Kay texts or types names/companies/notes to Claude after the event
3. **Business cards** — Kay photographs and shares

**Next morning:** Claude processes Granola transcripts + Kay's notes, then passes conversation data to outreach-manager's conference outreach subagent for follow-up drafting.

### Pipeline Integration

For each conference contact:
1. **Create/update Attio People record** with all 5 custom attributes:
   - relationship_type: Operator/Owner (or appropriate type)
   - nurture_cadence: based on conversation quality
   - value_to_search: what they do, why relevant
   - next_action: follow-up from conversation
   - how_introduced: "{Conference Name}, {date}"

2. **Add to Active Deals pipeline** at appropriate stage:
   - Had substantive conversation about their business → "First Conversation"
   - Brief booth chat, expressed interest → "Contacted"
   - Got card but no real conversation → "Identified"

3. **Create vault entity**: `brain/entities/{slug}.md` with proper schema

4. **Tag for attribution**: All contacts tagged with `source/conference` and `conference/{slug}`

### Conference Debrief Note

Create in **three locations:**

1. **Google Doc** in the conference's own Drive folder (RESEARCH/CONFERENCES/{CONFERENCE NAME}) — easy to read on phone, lives with all conference materials
2. **Vault file** at `brain/calls/{date}-{conference-slug}.md` — searchable context for future reference
3. **Slack notification** with Doc link — triggers Kay's review the morning after

Note: A Drive subfolder is created for each conference at registration time (see references/drive-locations.md). All conference materials — attendee lists, debrief note, target list, slides — live in that folder.

**Debrief structure:**
- Conference name, date, location
- Total people met
- **People met** — for each person: name, company, what they do, what you talked about, how promising (hot/warm/cold), follow-up action
- **Key takeaways** — what you learned about the niche from being there, surprises, patterns
- **Opportunities identified** — which conversations could lead somewhere
- **Things you might have missed** — Claude flags anything from Granola transcripts that Kay didn't explicitly note (names mentioned in passing, intros promised, business details shared)
- **Follow-up actions** — consolidated list of next steps
- Tagged: `call`, `source/conference`, relevant niche tags

The debrief is designed to be easily digestible on a phone screen — short bullets, person names bolded, no walls of text. It should trigger thoughts and catch things Kay missed in the moment.
</target_scoring>

<conference_decision_scan>
## Conference Decision Scan (Moved from pipeline-manager)

After Kay reviews the Conference Pipeline sheet Monday morning and marks decisions in Col M ("Attend" or "Register Only"), this scan picks them up and executes.

**When to run:** Monday morning scan, or any time Kay marks a new decision on the sheet.

**Process:**
1. Check Conference Pipeline Google Sheet for any row where Decision (Col M) = "Attend" or "Register Only" AND Status (Col K) is NOT yet "Registered"
2. For each new decision:
   - Create Motion task: "Register for {conference name}" with deadline 2 days before registration closes (Col G)
   - Include registration link from conference website (Col J)
   - If attendee list is publicly available (Col I), begin attendee list acquisition
   - Update Status (Col K) to "Registered" after Motion task created
3. Present changes to Kay before writing (per Stop Hook above)

**Note:** Kay picks conferences Monday morning. This scan runs after her review. Gives Kay a grace period to change her mind before registration is kicked off.
</conference_decision_scan>

<validation>
## Validation & Stop Hooks

Before reporting success, validate all outputs. If any check fails, do NOT send Slack. Report the failure and fix it.

### Sheet Write & Review Flow

**Write directly to the sheet. Kay reviews there, not in the conversation.**

The Conference Pipeline sheet IS the review surface. Don't dump raw search results or proposed rows into the conversation — that's noise. Write the filtered, quality-checked rows to the sheet, send Kay the link, and she marks Decision (col N) on the sheet itself.

**Procedure:**
1. Run discovery searches (parallel subagents for each niche)
2. Apply audience filter and owner verification gate — only conferences that pass go on the sheet
3. Write new rows to the Pipeline tab using `gog sheets update` or `gog sheets append` with `--values-json` flag (NOT `--values`)
4. Re-sort all data rows chronologically by Column A
5. Send Slack notification with link to the sheet
6. Kay reviews on the sheet and marks Decision column

**gog sheets syntax:**
```bash
# Append new rows
gog sheets append {SHEET_ID} "Pipeline!A:O" --values-json '[["col1","col2",...],...]' -a kay.s@greenwichandbarrow.com

# Update specific range
gog sheets update {SHEET_ID} "Pipeline!A{row}:O{row}" --values-json '[["col1","col2",...]]' -a kay.s@greenwichandbarrow.com
```

**Do NOT present conference results in the conversation.** The sheet is the single source of truth. Keep the conversation clean — just confirm what was added and send the link.

### 1. Sheet Validation (after discovery, post-approval)
Verify the Conference Pipeline Google Sheet has new rows with data in all required columns:
- Columns A-L (Date, Event Name, Location, Travel, Niche, Reg Cost, Reg Deadline, Est. Attendees, Attendee List, Website, Status, Agent Rec)
- Column O (Agent Notes)
- No blank cells in required columns for newly added rows

### 1b. Chronological Sort Validation (REQUIRED after every write)
After adding, removing, or modifying any rows in the Pipeline tab, re-sort ALL data rows (A2 onwards) by Column A (Date of Conference) in chronological order. Then verify:
- Read back Pipeline!A2:A{last_row} and confirm dates are in ascending order
- No header row was displaced
- No data was lost during sort (row count before = row count after)
- All columns preserved their association (no misaligned rows)

**This is mandatory.** The sheet must always be sorted chronologically — earliest date at top, farthest at bottom. Never leave the sheet unsorted after a write operation.

### 2. Attendee List Validation (if processing attendees)
Verify `brain/outputs/{date}-{conference-slug}-targets.md` exists with:
- Valid frontmatter per output schema
- Populated target list (not empty/placeholder)
- Each target has company name, person name, title at minimum

### 3. Attio Validation (post-conference processing)
Verify all conference contacts were created in Attio:
- People records exist with all 5 custom attributes populated
- Active Deals entries exist at correct pipeline stage
- No duplicates (cross-reference before creating)

### 4. Vault Validation (post-conference processing)
Verify:
- Entity file exists at `brain/entities/{slug}.md` for each new contact, with proper schema
- Debrief note exists at `brain/calls/{date}-{conference-slug}.md` with proper schema
- All wiki-links resolve (no broken links)

### 5. Slack Notification via AI-Operations Channel (only after validation passes)

All conference discovery notifications go to the AI-Operations Slack channel. Use the `SLACK_WEBHOOK_OPERATIONS` webhook from `scripts/.env.launchd`. (Kay attends conferences, not JJ — SVA is JJ's channel.)

**After discovery run (sheet updates confirmed and written):**
```bash
source scripts/.env.launchd
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Conference Pipeline updated — {n} new conferences added, {n} modified, {n} moved to Skipped.\n\nChanges:\n{bullet summary of what was added/changed}\n\nReview the pipeline:\nhttps://docs.google.com/spreadsheets/d/1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY/edit"}'
```

**After post-conference processing:**
```bash
source scripts/.env.launchd
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Post-conference processing complete for {conference name}.\n{n} contacts added to Attio. Follow-up drafts in Superhuman.\n\nDebrief: {Google Doc link}\n\nReview the debrief for anything you might have missed.\n\nConference Pipeline:\nhttps://docs.google.com/spreadsheets/d/1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY/edit"}'
```

**Slack message content:**
- Summary of what was added/changed (numbered list matching what Kay approved)
- Direct link to the Conference Pipeline sheet
- Keep it scannable, no walls of text

**If validation fails:** Do NOT send Slack. Report which checks failed and fix before retrying.
</validation>

<success_criteria>
## Success Criteria

### Per Conference
- [ ] Conference Prep doc created in conference Drive folder (if Monday conference with meetings/targets)
- [ ] Conference discovered and evaluated with full details
- [ ] Registration completed (or flagged for register-only)
- [ ] Attendee/exhibitor list acquired and processed
- [ ] Top targets identified, scored, and handed to outreach-manager
- [ ] Kay attended and captured conversations (Granola + notes)
- [ ] Conversation data handed to outreach-manager for follow-up drafting
- [ ] All contacts added to Attio (People + Active Deals)
- [ ] Vault entities created for each new contact
- [ ] Conference debrief note saved to brain/calls/
- [ ] Motion tasks created for any outstanding follow-ups

### Weekly Rhythm
- [ ] At least 1 conference attended per week (Monday preferred)
- [ ] Conference calendar maintained with 4-6 weeks of options
- [ ] Pipeline growing from conference contacts
</success_criteria>
