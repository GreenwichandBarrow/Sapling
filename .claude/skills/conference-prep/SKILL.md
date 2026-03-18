---
name: conference-prep
description: "Weekly conference discovery, registration, target identification, pre-conference outreach, and post-conference follow-up. Goal: 1+ conference per week to meet business owners in person."
user_invocable: true
context_budget:
  skill_md: 3000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Get Kay in front of business owners every week. Conferences are the highest-ROI channel for direct owner conversations. This skill handles the full lifecycle so Kay's only job is showing up and talking to people.

Target rhythm: 1 conference every Monday. Tuesday/Wednesday NYC-only as backup. Thursday possible but less preferred.

Reference: Colin Woolway and Will Gallagher attended 1-2 conferences/week and landed their acquisition. Kay is a solo searcher with a lean team (Claude, analyst, VA, bookkeeper). Claude owns conference logistics end-to-end.
</objective>

<essential_principles>
## How It Works

### Weekly Rhythm

**Friday (during weekly review):** Claude surfaces next 2-4 weeks of conference options. Kay picks next week's conference.

**T-minus 2 weeks:** Register. Begin attendee/exhibitor list acquisition.

**T-minus 1 week:** Scrape attendee list for targets. Score and rank. Draft pre-conference emails to top 5-10 targets. Kay reviews and sends.

**Day of conference:** Kay attends. Runs Granola at booths to capture conversations. Talks to as many owners as possible within 2 hours.

**Next morning:** Claude processes Granola transcripts + Kay's notes. Drafts follow-up emails. Adds contacts to Attio (People records + Active Deals pipeline). Kay reviews and sends follow-ups during morning pipeline-manager review.

### Scheduling Constraints

| Day | Available | Constraint |
|-----|-----------|-----------|
| Monday | Full day | Preferred. Can fly early, back by dinner. Most common conference day. |
| Tuesday | NYC only | Must be done by 1:30pm |
| Wednesday | NYC only | Must be done by 1:30pm |
| Thursday | NYC + nearby | Must be done by 4:30pm |
| Friday | No | Weekly review day |

### Geography

**Priority 1:** NYC metro (walk, subway, car)
**Priority 2:** Northeast corridor (Boston, Philly, DC, Hartford — train or short flight)
**Priority 3:** Midwest (Chicago, Charlotte, Atlanta — early morning flight, back by dinner)
**Excluded:** West Coast (California regulatory concerns, travel time prohibitive)

### Niche Targeting

Search for conferences in this priority order:
1. **Top 5 active niches** (from Industry Research Tracker)
2. **Adjacent/runner-up niches** (from IDEATION list) — only if top 5 exhausted for a given week
3. **General small business owner gatherings** — ETA events, SBA conferences, local business expos

Current top 5 niches:
1. Trust Administration (NAEPC, fiduciary associations, estate planning)
2. Estate Management Companies (luxury/UHNW events, property management)
3. Insurance Producer License Compliance (insurance industry, compliance events)
4. Art Insurance Brokerage (art fairs, insurance conferences)
5. Trade Credit Insurance (trade finance, credit insurance, textile/fashion)

### Conference Types (all qualify if 5+ business owners present)
- Trade shows with exhibitor booths (PREFERRED — booth = business owner you can talk to)
- Association meetups and chapter meetings (PREFERRED — smaller, intimate, high-quality conversations)
- Regional industry conferences (30-200 people ideal)
- Professional networking events
- Business expos and showcases

### Conference Selection Preferences
- **Smaller > bigger.** 30-200 person events with booths/expos beat 1,000+ person conferences where you get lost in crowds.
- **Booth/expo format > panel/speaker format.** Kay needs face time with owners at their tables, not keynote audiences.
- **Industry association chapter meetings are ideal.** NAEPC DC was the gold standard — intimate, business owners present, real conversations.
- **Skip consumer-facing fairs.** Art fairs, consumer expos = visitors and collectors, not acquisition targets. Exception: industry-specific events AT art fairs (e.g., insurance roundtable during Art Basel).
- **Large conferences (1,000+) are "Register Only" candidates** — get the attendee list for outreach, but don't attend unless booth format or high-value niche.
- **Association memberships worth joining** if they unlock regular chapter meetings with business owners (e.g., EPCNYC for estate planners, local insurance agent associations).

### Register-Only Events
Some conferences are worth registering for without attending — to access the attendee/exhibitor list for outreach. Flag these separately. Large conferences (1,000+) default to this category unless booth format.

### Association Memberships
Some events require association membership. Kay is open to joining if it unlocks multiple relevant conferences. Flag membership cost and number of accessible events. Ask Kay before purchasing.

## Architecture

Claude handles all phases directly (no sub-agents needed). The workflow is sequential and runs weekly.

## Team Roles
- **Claude:** Discovery, registration logistics, attendee scraping, target scoring, email drafting, pipeline integration, follow-up drafts
- **Kay:** Picks conferences, reviews/sends emails, attends, provides post-conference notes
- **Analyst:** Not involved (focused on financial analysis and deck building)
- **VA (JJ):** Not involved in conference prep (focused on cold calling and validation)
</essential_principles>

<discovery>
## Phase 1: Conference Discovery

Run weekly (Friday or on-demand). Find conferences for the next 2-6 weeks.

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

Present to Kay as a ranked list. She picks which to attend and which to register-only.

### Conference Calendar

Maintain in `brain/trackers/conference-calendar.md`:
```markdown
| Date | Event | Location | Niche | Status | Targets | Notes |
|------|-------|----------|-------|--------|---------|-------|
| 2026-03-24 | NAEPC Regional | NYC | Trust Admin | Registered | 8 | Pre-outreach sent |
```

Statuses: Discovered, Evaluating, Registered, Prep Complete, Attending, Attended, Skipped, Register-Only
</discovery>

<registration>
## Phase 2: Registration & Attendee List Acquisition

After Kay approves a conference:

### Registration
1. Provide direct registration link
2. Create Motion task: "Register for {conference name}" with deadline 2 days before registration closes
3. If association membership required, present cost and ask Kay for approval first
4. Update conference calendar status to "Registered"

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

<outreach>
## Phase 3: Pre-Conference Target Outreach

Run T-minus 1 week before the conference.

### Target Scoring

Rank targets by:
1. **Niche fit** — direct match to top 5 niches (highest weight)
2. **Owner presence** — confirmed business owner/operator at booth
3. **Company size** — within buy box (~$1-10M revenue, 5-50 employees)
4. **Geography** — bonus for northeast businesses
5. **Not already in pipeline** — new contacts get priority

Present top 10 to Kay. She selects 5-10 for outreach.

### Email Drafts

For each approved target, draft a personalized email:

**Voice:** Use Kay's calibrated outreach voice (see memory: user_outreach_voice.md)
**Rules:**
- No em dashes. Use periods, commas, line breaks.
- Conversational, warm, direct
- Reference the specific conference by name
- Mention Kay will be attending and would love to connect briefly
- Keep it short (3-4 sentences max)
- Propose a specific ask: "Would love to stop by your booth" or "Grab a coffee during the break"

**Template structure:**
```
Subject: {Conference Name} — quick hello

Hi {first name},

{1 sentence about finding them on the exhibitor list / their company}.
{1 sentence about why Kay is interested — niche connection, not "I want to buy your company"}.
{1 sentence proposing a brief connection at the conference}.

Looking forward to it.

Kay Schneider
Greenwich & Barrow
```

Draft in Gmail via gog. Kay reviews and sends from Superhuman.

Create Motion task: "Review and send {conference} pre-outreach emails" with due date T-minus 5 days.
</outreach>

<post_conference>
## Phase 4: Post-Conference Follow-Up

### Data Capture (Day of)

Kay captures booth conversations via:
1. **Granola** running on phone at each booth — transcripts auto-ingest into brain/calls/ via pipeline-manager
2. **Manual notes** — Kay texts or types names/companies/notes to Claude after the event
3. **Business cards** — Kay photographs and shares

### Follow-Up Drafts (Next Morning)

The morning after the conference, as part of the pipeline-manager daily briefing:

1. Process Granola transcripts from the conference day
2. Match conversations to companies/people
3. For each person Kay spoke with:
   - Draft personalized follow-up email referencing specific conversation points
   - Use Kay's voice, no em dashes
   - Propose a next step (call, meeting, send info)
   - Short and specific — reference something from the actual conversation
4. Present all drafts during morning review. Kay approves and sends.

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

Create `brain/calls/{date}-{conference-slug}.md` with:
- Conference name, date, location
- List of people met with notes
- Key takeaways and opportunities identified
- Follow-up actions
- Tagged: `call`, `source/conference`, relevant niche tags
</post_conference>

<success_criteria>
## Success Criteria

### Per Conference
- [ ] Conference discovered and evaluated with full details
- [ ] Registration completed (or flagged for register-only)
- [ ] Attendee/exhibitor list acquired and processed
- [ ] Top targets identified and scored
- [ ] Pre-conference emails drafted and sent to 5-10 targets
- [ ] Kay attended and captured conversations (Granola + notes)
- [ ] Follow-up emails drafted next morning
- [ ] All contacts added to Attio (People + Active Deals)
- [ ] Vault entities created for each new contact
- [ ] Conference debrief note saved to brain/calls/
- [ ] Motion tasks created for any outstanding follow-ups

### Weekly Rhythm
- [ ] At least 1 conference attended per week (Monday preferred)
- [ ] Conference calendar maintained with 4-6 weeks of options
- [ ] Pipeline growing from conference contacts
</success_criteria>
