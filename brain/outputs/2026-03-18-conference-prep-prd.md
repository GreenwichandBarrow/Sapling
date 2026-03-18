---
date: 2026-03-18
type: prd
status: draft
schema_version: 1.0.0
output_type: prd
title: "Conference Prep Workflow Skill"
tags:
  - date/2026-03-18
  - output/prd
  - status/draft
  - topic/conference-prep
  - topic/acquisition-search
---

# Conference Prep Workflow Skill — PRD

## Overview

**What we're building:** A Claude Code skill that finds, evaluates, and prepares Kay for weekly conference attendance. Full lifecycle: discover conferences by niche, register, scrape attendee/exhibitor lists for acquisition targets, draft pre-conference outreach to top targets, and draft same-day post-conference follow-up emails. All approved targets flow into the Active Deals pipeline in Attio.

**Why:** Kay's acquisition search needs more direct owner conversations. Email outreach has diminishing returns. Colin Woolway and Will Gallagher (partnered searchers in Kay's office) attended 1-2 conferences/week and landed their acquisition — Kay's investors respect this approach. Conferences put Kay in front of business owners in person, which is her strength. With a solo search and lean team (Claude, analyst, VA, bookkeeper), Claude must handle the logistics so Kay can focus on the conversations.

**Scope:** New skill build — `.claude/skills/conference-prep/SKILL.md`

**Deadline context:** Fund deadline is Feb 2027. Every week without a conference is a missed opportunity. Goal is 1 conference every Monday starting ASAP.

---

## User Stories

**As Kay,** I want to see a curated list of upcoming conferences relevant to my active niches, so that I can pick which ones to attend each week.

**As Kay,** I want Claude to handle registration, attendee list acquisition, and target identification, so that I only spend time on the in-person conversations.

**As Kay,** I want pre-conference emails drafted to the top 5-10 booth owners/targets, so that I can schedule meetings before I arrive.

**As Kay,** I want same-day post-conference follow-up emails drafted for everyone I spoke with, so that I can close the loop while the conversation is fresh.

**As Kay,** I want every conference contact automatically added to the Active Deals pipeline in Attio, so that nothing falls through the cracks.

**As Kay,** I want conferences that don't require attendance flagged for attendee list scraping only, so that I can still get value from events I can't physically attend.

---

## Features

### 1. Conference Discovery

#### 1.1: Niche-Driven Conference Search
**Description:** Weekly search for conferences, trade shows, association meetups, and industry gatherings with 5+ business owners. Search prioritizes the top 5 active niches, then expands to adjacent/runner-up niches if the calendar week is exhausted.

**Active niches (priority order):**
1. Trust Administration (NAEPC, fiduciary associations, estate planning events)
2. Estate Management Companies (luxury/UHNW events, property management conferences)
3. Insurance Producer License Compliance (insurance industry conferences, compliance events)
4. Art Insurance Brokerage (art fairs, insurance conferences, art industry events)
5. Trade Credit Insurance (trade finance events, credit insurance conferences, textile/fashion industry)

**Acceptance Criteria:**
- [ ] Searches web for conferences in top 5 niches within rolling 6-week window
- [ ] If no Monday conferences available in top 5, expands to adjacent niches from the IDEATION list
- [ ] Returns: event name, date, location, estimated attendance, registration cost, registration deadline, attendee list availability
- [ ] Flags events that are "register only" (for attendee list, no attendance needed)
- [ ] Flags events requiring association membership to attend (with membership cost)
- [ ] Prioritizes Monday events. Tuesday/Wednesday NYC-only (must be done by 1:30pm). Thursday (must be done by 4:30pm).

#### 1.2: Geography Filter
**Description:** Filter conferences by travel feasibility from NYC.

**Acceptance Criteria:**
- [ ] Priority 1: NYC metro (walk, subway, car)
- [ ] Priority 2: Northeast corridor (Boston, Philly, DC, Hartford — train or short flight)
- [ ] Priority 3: Midwest (Chicago, Charlotte, Atlanta — early morning flight, back by dinner)
- [ ] Excluded: West Coast (California regulatory concerns, travel time)
- [ ] Monday: full-day travel OK (early flight out, back by late evening)
- [ ] Tuesday/Wednesday: NYC only, done by 1:30pm
- [ ] Thursday: NYC + nearby, done by 4:30pm

#### 1.3: Conference Calendar
**Description:** Maintain a rolling calendar of discovered conferences with status tracking.

**Acceptance Criteria:**
- [ ] Stored in vault: `brain/trackers/conference-calendar.md` or Google Sheet
- [ ] Statuses: Discovered, Evaluating, Registered, Attending, Attended, Skipped, Register-Only
- [ ] Shows: next 6 weeks of events, sorted by date
- [ ] Updated weekly during the conference prep workflow

### 2. Registration & Attendee List Acquisition

#### 2.1: Registration Management
**Description:** For approved conferences, handle registration logistics.

**Acceptance Criteria:**
- [ ] Provides registration link and deadline
- [ ] Creates Motion task for Kay: "Register for {conference}" with deadline
- [ ] Tracks registration status in conference calendar
- [ ] Flags association membership requirements with cost/benefit analysis

#### 2.2: Attendee/Exhibitor List Scraping
**Description:** Once registered (or for register-only events), acquire and parse the attendee or exhibitor list for acquisition targets.

**Acceptance Criteria:**
- [ ] Scrapes exhibitor list from conference website when publicly available
- [ ] If attendee list requires login/registration, flags for Kay to download manually
- [ ] Parses list into structured data: company name, person name, title, booth number
- [ ] Cross-references against Attio to identify existing contacts vs. new targets
- [ ] Enriches with web research: company revenue estimate, employee count, owner name, niche fit

### 3. Pre-Conference Target Identification & Outreach

#### 3.1: Target Scoring
**Description:** From the attendee/exhibitor list, identify the top targets worth pre-conference outreach.

**Acceptance Criteria:**
- [ ] Filters for business owners/operators (not employees, not vendors)
- [ ] Scores by: niche relevance, company size (buy box fit), owner presence at booth
- [ ] Returns ranked list of top 10 targets with rationale
- [ ] Kay reviews and selects which to email (approx 5-10)

#### 3.2: Pre-Conference Email Drafts
**Description:** Draft personalized outreach emails to approved targets.

**Acceptance Criteria:**
- [ ] Uses Kay's outreach voice (per memory: user_outreach_voice.md)
- [ ] No em dashes (per feedback)
- [ ] References the specific conference and Kay's reason for attending
- [ ] Proposes a brief meeting at the conference (coffee, booth visit, 15 min chat)
- [ ] Drafts ready for Kay to review and send from Superhuman
- [ ] Sent 1-2 weeks before the conference

### 4. Post-Conference Follow-Up

#### 4.1: Conference Debrief
**Description:** Kay captures booth conversations via Granola (running on phone at each booth) and/or provides names/companies afterward. Claude processes transcripts + notes into follow-up drafts for the next morning.

**Acceptance Criteria:**
- [ ] Granola transcripts from booth conversations auto-ingested into brain/calls/ (via pipeline-manager ingestion)
- [ ] Kay can also manually input names/companies/notes (text or business card photos)
- [ ] Claude drafts personalized follow-up emails for each person
- [ ] Follow-ups reference specific conversation points from Granola transcripts or Kay's notes
- [ ] Emails drafted and ready for Kay to review and send **next morning** (not same day)
- [ ] Next-morning review integrated into pipeline-manager daily briefing (Part 4: conference follow-ups)

#### 4.2: Pipeline Integration
**Description:** Every conference contact flows into Attio.

**Acceptance Criteria:**
- [ ] New contacts added to Attio People records with appropriate attributes
- [ ] Business owners added to Active Deals pipeline at "Contacted" or "First Conversation" stage
- [ ] Industry contacts added with appropriate relationship_type
- [ ] Vault entities created for each new person (brain/entities/{slug}.md)
- [ ] Conference tagged in Attio and vault for attribution tracking

### 5. Weekly Conference Rhythm

#### 5.1: Weekly Conference Prep Trigger
**Description:** Integrated into the weekly workflow. Every week, Claude surfaces the conference plan.

**Acceptance Criteria:**
- [ ] Runs as part of weekly review or on-demand via `/conference-prep`
- [ ] Presents: "This week's conference: {name} on {day}. {n} targets identified. {n} pre-outreach emails drafted."
- [ ] If no conference scheduled: "No conference this week. Here are 3 options for next Monday: ..."
- [ ] Tracks conference attendance rate (goal: 1/week minimum)

---

## Technical Approach

**Architecture:**
- Claude Code skill at `.claude/skills/conference-prep/SKILL.md`
- Web search for conference discovery (WebSearch tool)
- Linkt API for company enrichment of attendee lists
- Attio API for pipeline integration and contact management
- Gmail (gog) for email draft creation
- Motion API for registration and follow-up task creation
- Vault for conference calendar and entity creation

**Integrations:**
- **WebSearch/WebFetch:** Conference discovery, exhibitor list scraping
- **Linkt API:** Company enrichment (revenue, employee count, owner info)
- **Attio API:** People records, Active Deals pipeline entries
- **Gmail (gog):** Email draft creation for pre- and post-conference outreach
- **Motion API:** Task creation (register, follow up, etc.)
- **Vault (brain/):** Entity creation, conference calendar tracking

**Key Technical Decisions:**
- Conference discovery uses web search rather than a database — conference listings are fragmented across association sites, event platforms (10times, Eventbrite, TradeShowNews), and industry publications
- Attendee list parsing needs to handle multiple formats (PDF, Excel, web tables)
- Pre-conference emails use the same voice calibration as the outreach skill

**Constraints:**
- Some attendee lists only available after registration (can't preview before committing)
- Some conferences require association membership ($200-2000/year) — need Kay's approval
- Conference websites vary wildly in structure — scraping won't always work, may need manual fallback

---

## Test Strategy

**E2E Scenarios:**
1. **Full cycle test:** Pick a real upcoming conference in a top-5 niche. Discover → evaluate → register → scrape exhibitors → identify targets → draft emails → simulate post-conference follow-up
2. **Niche expansion test:** Simulate a week with no top-5 conferences available. Verify the skill expands to adjacent niches.
3. **Geography filter test:** Verify Monday/Tuesday/Thursday scheduling constraints work correctly

**Edge Cases to Test:**
- Conference with no public exhibitor list (registration-wall)
- Conference requiring association membership
- Multiple conferences on the same Monday (prioritization)
- Conference cancellation after registration
- Attendee list in unusual format (PDF image, non-standard Excel)

---

## Out of Scope

- Booking travel/hotels (Kay handles or uses a travel agent)
- Conference speaking opportunities (not the goal — Kay is there to meet owners)
- Virtual/online conferences (the whole point is in-person owner conversations)
- International conferences
- Conferences longer than 1 day (Kay needs to be back same day)

---

## Open Questions

- [ ] Where to store the conference calendar — vault markdown file vs. Google Sheet vs. Motion project? (Recommend: Google Sheet for visibility + vault for searchability)
- [ ] Should conference discovery run weekly on a specific day (e.g., Friday during weekly review) or rolling?
- [ ] For association memberships that unlock multiple conferences, what's the approval threshold? Auto-approve under $500? Always ask?
- [ ] How to handle conferences that overlap with existing calendar commitments?

---

## Notes

- Colin Woolway and Will Gallagher (Legate Partners) are in Kay's office and can share their conference playbook
- Kay attended NAEPC conference fall 2025 and loved the people — trust administration conferences are a proven fit
- Art Basel Miami (Dec 2025) generated multiple valuable contacts — art world events work
- The skill should complement the Target Discovery + Outreach Drafting skill (being built in parallel)
- Kay's outreach voice is calibrated in memory (user_outreach_voice.md) — no em dashes, conversational tone
