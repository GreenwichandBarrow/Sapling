---
name: target-discovery-outreach
description: "Niche sprint execution — find acquisition targets via Linkt + web research, draft personalized owner outreach, build JJ's call list. Runs daily Tue-Thu during active sprint."
user_invocable: true
context_budget:
  skill_md: 3000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Turn an activated niche into owner conversations. This skill executes the Field Execution phase of the G&B 8-week research cycle.

This skill builds on three prior skills:
- **skill/niche-intelligence** — provides the one-pager, scorecard, buy-box target validation (Step 4b), and Industry Research Tracker data for the activated niche
- **skill/pipeline-manager** — tracks all targets in Attio, manages stage progression, captures meaningful conversations, handles nurture reminders and follow-ups
- **skill/conference-prep** — provides conference calendar, attendee/exhibitor lists, pre/post conference outreach for events in the activated niche

Input: An activated niche that has already been scored, validated, and promoted via niche-intelligence.
Output: 4-6 qualified targets per day → personalized email drafts for Kay + call list for JJ → targets in Attio Active Deals pipeline (managed by pipeline-manager).

Goal: 1 interesting deal reviewed per week, fed by 2-5 meaningful owner conversations per week.
</objective>

<essential_principles>
## How It Works

### Two Parallel Tracks

**Track 1: Niche Sprint (daily, Tue-Thu)**
Focused on the activated niche of the month. Claude finds targets, drafts personalized emails, builds JJ's call list. Kay reviews/sends. JJ dials.

**Track 2: Conference Outreach (weekly, as needed)**
When a conference is coming up, this skill works with conference-prep to identify targets from the attendee list. May be a different niche than the sprint, but always within top 5 or IDEATION list.

### Daily Rhythm (Tue-Thu)

1. **Claude researches 4-6 new targets** in the activated niche using free sources first (web, associations, directories)
2. **Kay reviews the raw list** — approves which to spend Linkt credits on
3. **Claude enriches approved targets via Linkt** — gets validated email, phone, owner details
4. **Claude drafts personalized emails** for each approved target
5. **Claude adds targets to JJ's call sheet** with phone numbers and script
6. **Kay reviews and sends emails** from Superhuman
7. **JJ cold calls** from the sheet
8. **All targets added to Attio** Active Deals at "Identified"

### Volume Targets (from investor survey data)
- 4-6 owners contacted per day (funds that acquired averaged 4, not 9)
- Quality over quantity — deep research on each target, personalized outreach
- Track meaningful conversations, not emails sent
- In-person seller meeting every 15.6 days (Kay's weekly conference target exceeds this)

### Linkt Credit Management
- 150 credits/month = ~5-6 companies/day if running daily
- 1 credit = 1 entity (company or person)
- **Never burn credits on discovery.** Free research first, Linkt for validated contacts on approved targets only.
- Create tight ICPs so search results are pre-qualified
- Run smaller, focused searches (10-20 entities) rather than large broad ones

## Team Roles

**Claude:**
- Free research to build raw target lists (web search, association directories, industry databases)
- Run Linkt for approved targets (enrichment + contact info)
- Draft personalized emails (Kay's voice, no em dashes)
- Build JJ's call sheet with script
- Add all targets to Attio Active Deals pipeline
- Track response rates and conversion

**Kay:**
- Approve which targets get Linkt credits
- Review and send email drafts
- Conduct Stage 1 calls with responding owners
- Go/no-go on each target

**JJ:**
- Cold call from Claude's sheet (company, owner, phone, script)
- Log outcomes in the sheet (connected, voicemail, callback, not interested)
- Not doing research, list building, or CRM work

**Analyst:**
- Landscape memo at niche activation (Week 1)
- Company scorecards for approved targets
- Financial analysis when financials received
</essential_principles>

<niche_activation>
## Phase 1: Niche Activation (Week 1 of sprint)

When a new niche is activated, pull from existing skill outputs — don't rebuild what's already been created.

### 1. Pull Existing Intelligence

**From skill/niche-intelligence:**
- One-pager (already created in Google Drive, RESEARCH > INDUSTRY ANALYSIS & SCORING)
- Scorecard (already scored on Industry Research Tracker)
- Buy-box target validation (Step 4b) — confirmed acquirable target count
- Thesis positioning — already written in the one-pager

**From skill/pipeline-manager:**
- Existing contacts in Attio who are in this niche (intermediaries, industry experts, network contacts)
- Any deals already in the Active Deals pipeline for this niche

**From skill/conference-prep:**
- Conference Pipeline sheet — events already discovered for this niche
- Any attendee/exhibitor lists already acquired

### 2. Define ICP for Linkt
Using the one-pager and scorecard criteria, Claude drafts ICP parameters for Kay's approval:
- Company size: revenue range, employee count (from scorecard)
- Ownership: independent, owner-operated, not PE-backed
- Geography: within buy box
- Age: 10+ years operating history
- Model: recurring revenue, B2B services
- Owner profile: retiring, fatigued, or succession-planning

```
POST /v1/icp with:
- Name: "{Niche Name} - G&B Acquisition Target"
- Entity targets: company + person (owner/CEO)
- Criteria from ICP definition above
```

### 3. Map Intermediaries and River Guides
Search vault entities and Attio People records for existing contacts in this niche:
- Brokers who cover this industry (Intermediary pipeline)
- CPAs/attorneys who serve these businesses
- Association leaders (from one-pager research)
- Industry consultants and experts (People records with relationship_type = Industry Expert)
- River guides who could accompany Kay to conferences in this niche

### 4. Create Sprint Assets
- [ ] ICP created in Linkt (informed by one-pager + scorecard)
- [ ] Conference calendar reviewed for this niche (from conference-prep)
- [ ] Intermediary/river guide map drafted (from pipeline-manager + vault)
- [ ] JJ's cold call script written for this niche
- [ ] Niche sprint Google Sheet created in LINKT TARGET LISTS folder (see references/drive-locations.md)
</niche_activation>

<target_discovery>
## Phase 2: Target Discovery (Daily, Weeks 2+)

### Step 1: Run Linkt Search
Linkt is the primary list builder. It finds companies matching the ICP, enriches them, and returns validated owner contact info — all in one step.

```
Execute the niche ICP Search flow in Linkt:
POST /v1/task/{task_id}/execute
```

Linkt's AI agents will:
- Find companies matching the ICP criteria (industry, size, geography, ownership)
- Enrich each company with revenue, employee count, ownership status
- Identify the owner/CEO with validated email and phone
- Verify criteria matches against the ICP

**Run smaller, focused searches** (10-20 entities per run) rather than large broad ones. Each entity = 1 credit. 150 credits/month.

**Output:** Linkt returns enriched entities in sheets. Export to Google Sheet in LINKT TARGET LISTS folder with one row per company+owner:
Company | Website | Headquarters | Industry | Employees | Revenue | Ownership | Owner Name | Owner Title | Email | Phone | LinkedIn (Owner) | LinkedIn (Company)

**Phone number formatting:** Linkt returns phones as `+1 973-770-9090`. When writing to Google Sheets:
1. Strip the country code prefix (`+1 `)
2. Reformat to `(XXX) XXX-XXXX` (e.g., `(973) 770-9090`)
3. Write with `--input USER_ENTERED` and apostrophe prefix (`'(973) 770-9090`) to prevent formula interpretation
This must happen on every Linkt pull, not as a cleanup step.

### Step 2: Supplement with Free Sources
Linkt won't find everything. Supplement with free research:

- **Association directories** — member lists, state licensing board registries
- **Conference exhibitor lists** — from conference-prep skill outputs
- **Web search** — industry-specific searches for companies Linkt may have missed
- **Existing intelligence** — Attio pipeline, vault entities, niche one-pagers from niche-intelligence
- **Intermediary referrals** — deals forwarded by brokers, CPAs, network contacts

For companies found through free sources, use Linkt to enrich them (get validated contact info) if worth a credit.

### Step 3: Kay Reviews Target List
Present the combined list (Linkt + supplemental) to Kay. She reviews:
- Which targets are real acquisition candidates
- Remove any that don't fit (wrong size, PE-backed, already contacted, etc.)
- Flag any she has existing connections to (warm intro path)

### Step 4: Outreach Assignment
Every approved target gets quality attention. For each target, Claude:
- Does deep web research on the company and owner (beyond what Linkt provides)
- Drafts a personalized email for Kay to send
- Adds the owner to JJ's call sheet (phone + script)
- Both channels hit the same target — email from Kay, call from JJ
</target_discovery>

<outreach>
## Phase 3: Outreach Drafting (Daily, Tue-Thu)

### Email Drafts

Every target gets a deeply personalized email. At 4-6 targets per day, there's no reason for templates.

**Voice:** Kay's calibrated outreach voice (see memory: user_outreach_voice.md)
**Rules:**
- No em dashes. Periods, commas, line breaks.
- Conversational, warm, direct
- Reference something specific about the owner or business (from Claude's deep research)
- Never mention "I want to buy your company" — frame as exploring the industry, learning from experts
- Keep it short (3-5 sentences)
- Propose a specific next step (phone call, coffee if local)

**Structure:**
```
Subject: {Something specific to their business}

Hi {first name},

{1 sentence showing you researched their specific business}.
{1 sentence connecting your background to their world — why you're credible}.
{1 sentence proposing a conversation — learning about the industry, not pitching}.

Would love to connect for 15 minutes.

Kay Schneider
Greenwich & Barrow
```

Draft in Gmail via gog. Kay reviews and sends from Superhuman.

### JJ's Call List

Populate a Google Sheet in OPERATIONS with:
| Company | Owner Name | Phone | Location | Script | Status | Notes | Date Called |

**Script** is niche-specific, written once at activation and refined based on JJ's feedback.

**Script structure:**
```
Hi, this is JJ calling on behalf of Kay Schneider at Greenwich & Barrow.
We're reaching out to {niche description} companies in the {region} area.
Kay is exploring the {niche} industry and would love to speak with the
owner about their experience in the space. Is {owner name} available
for a brief conversation?
```

JJ logs status: Connected, Voicemail, Callback Requested, Not Interested, Wrong Number.
</outreach>

<pipeline_integration>
## Phase 4: Pipeline Integration

### Every target gets added to Attio
1. **Create/update company record** in Attio
2. **Add to Active Deals pipeline** at "Identified" stage
3. **Create vault entity** at brain/entities/{slug}.md
4. **Tag with source attribution:** email-outreach, cold-call, conference, broker, network

### Stage Progression
| Action | Move To |
|--------|---------|
| Email sent or call made | Contacted |
| Owner responds positively | First Conversation |
| Follow-up call/meeting | Second Conversation |
| NDA signed | NDA Executed |
| Financials received | Financials Received |
| Active analysis | Active Diligence |
| Offer made | LOI / Offer Submitted |
| Offer accepted | LOI Signed |
| Passed or rejected | Closed / Not Proceeding |

### Track Meaningful Conversations
After every owner call, pipeline-manager asks: "Was this a meaningful conversation?"
If yes → check `meaningful_conversation` on the Active Deals entry.

### Response Rate Tracking
Weekly tracker captures: emails sent, responses received, response rate %, conversations by source.
</pipeline_integration>

<cadence>
## Weekly Cadence

**Monday:** Conference (attend, Granola captures). No outreach.
**Tuesday:** Pipeline manager morning review (includes conference follow-ups). Claude presents new targets researched. Kay reviews/approves. Emails drafted.
**Wednesday:** Kay reviews/sends emails. JJ calling. Claude researches next batch.
**Thursday:** Same as Wednesday. Pre-conference outreach if event next Monday. Claude researches next batch.
**Friday:** Weekly tracker. Niche intelligence. Conference discovery. Review sprint progress.

### Sprint Check-In (Every 2 Weeks)
At the 2-week mark, evaluate:
- How many targets found in this niche?
- Response rate from owners?
- Any meaningful conversations?
- Is the target pool deep enough to continue?
- Kill, advance, or table this niche?

If the niche is running dry, escalate to Kay. Don't wait 8 weeks.
</cadence>

<success_criteria>
## Success Criteria

### Daily
- [ ] 4-6 new targets researched
- [ ] Kay reviewed and approved Linkt spend
- [ ] Email drafts ready for Kay's review
- [ ] JJ's call sheet updated
- [ ] New targets added to Attio

### Weekly
- [ ] 20-30 owners contacted (email + phone combined)
- [ ] 2-5 meaningful owner conversations
- [ ] Response rate tracked
- [ ] Conference attended (Monday)
- [ ] Sprint progress reviewed (Friday)

### Per Sprint (5-8 weeks)
- [ ] 50+ owners contacted in this niche
- [ ] 5+ Stage 1 calls
- [ ] 1+ deals progressed to financials
- [ ] Kill/advance/table decision made
</success_criteria>
