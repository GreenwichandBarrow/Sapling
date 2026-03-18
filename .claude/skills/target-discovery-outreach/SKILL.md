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

Input: An activated niche with ICP defined.
Output: 4-6 qualified targets per day → personalized email drafts for Kay + call list for JJ → targets in Attio Active Deals pipeline.

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
4. **Claude drafts personalized emails** for Tier A targets (top 10 per week)
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
- Company scorecards for Tier A targets
- Financial analysis when financials received
</essential_principles>

<niche_activation>
## Phase 1: Niche Activation (Week 1 of sprint)

When a new niche is activated:

### 1. Write Thesis
Kay writes 2-3 sentence thesis positioning. Claude can draft for review.
```
Example: "Insurance producer license compliance firms manage multi-state
broker license renewals and CE compliance for insurance agencies. Regulatory
complexity by state creates switching costs and recurring revenue.
Consolidation is underway (Altaline/Haven, Kelso, Wolters Kluwer) validating
the economics."
```

### 2. Define ICP
Claude drafts ICP parameters for Kay's approval:
- Company size: revenue range, employee count
- Ownership: independent, owner-operated, not PE-backed
- Geography: within buy box (1hr of home preferred, anywhere US if remote)
- Age: 10+ years operating history
- Model: recurring revenue, B2B services
- Owner profile: retiring, fatigued, or succession-planning

### 3. Create Linkt ICP
```
POST /v1/icp with:
- Name: "{Niche Name} - G&B Acquisition Target"
- Entity targets: company + person (owner/CEO)
- Criteria from ICP definition above
```

### 4. Conference Mapping
Check conference-prep Pipeline sheet for events in this niche. Flag relevant upcoming conferences.

### 5. Intermediary Mapping
Search vault and Attio for existing contacts who could be river guides in this niche:
- Brokers who cover this industry
- CPAs/attorneys who serve these businesses
- Association leaders
- Industry consultants

### 6. Define Tier Framework
- **Tier A (top 10):** Best-fit targets. Kay sends personalized email. Claude does deep research per company.
- **Tier B (next 20-30):** Good fit. Claude drafts personalized email. Kay reviews/sends.
- **Tier C (remaining):** JJ cold calls with script.

### Deliverables (Week 1)
- [ ] Thesis written and approved
- [ ] ICP created in Linkt
- [ ] Tier A/B/C framework defined
- [ ] Conference calendar checked for relevant events
- [ ] Intermediary map drafted
- [ ] JJ's call script written for this niche
- [ ] Niche sprint Google Sheet created (see references/drive-locations.md)
</niche_activation>

<target_discovery>
## Phase 2: Target Discovery (Daily, Weeks 2+)

### Step 1: Free Research (Claude, no credits)
Before spending any Linkt credits, build a raw target list from free sources:

**Web Search:**
```
"{niche} companies {state/region}"
"{niche} firms independent"
"site:linkedin.com {niche} owner founder CEO"
"{industry association} member directory"
"{niche} companies list"
```

**Association Directories:**
- Industry association member lists (often public or behind free registration)
- State licensing board registries (public records of licensed firms)
- Professional certification directories

**Conference Exhibitor Lists:**
- From conference-prep skill outputs
- Past conference attendee lists in the CONFERENCES Drive folder

**Existing Intelligence:**
- Attio pipeline (already tracked companies)
- Vault entities and call notes
- Niche one-pagers from niche-intelligence skill
- Industry Research Tracker

**Output:** Raw list in a Google Sheet with: company name, website, location, estimated size, source, owner name if found.

### Step 2: Kay Reviews Raw List
Present the raw list to Kay. She marks which targets are worth a Linkt credit. This is the gate that protects the 150 credits/month.

### Step 3: Linkt Enrichment (approved targets only)
For each approved target:
```
Run Linkt Search flow with the niche ICP
OR search existing Linkt entities first to avoid re-spending credits
```

**Output per target:**
- Company: name, website, HQ, industry, employees, revenue, ownership status
- Person: owner/CEO name, title, email (validated), phone, LinkedIn

### Step 4: Tier Assignment
Based on enrichment data + Kay's review:
- Tier A → deep research + Kay's personalized email
- Tier B → Claude's personalized email
- Tier C → JJ's call list
</target_discovery>

<outreach>
## Phase 3: Outreach Drafting (Daily, Tue-Thu)

### Email Drafts (Tier A + B)

**Voice:** Kay's calibrated outreach voice (see memory: user_outreach_voice.md)
**Rules:**
- No em dashes. Periods, commas, line breaks.
- Conversational, warm, direct
- Reference something specific about the owner or business (from research)
- Never mention "I want to buy your company" — frame as exploring the industry, learning from experts
- Keep it short (3-5 sentences)
- Propose a specific next step (phone call, coffee if local)

**Tier A Template (Kay sends, deeply personalized):**
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

**Tier B Template (personalized but lighter touch):**
```
Subject: Quick question about {their niche/specialty}

Hi {first name},

{1 sentence about their company and what caught your attention}.
{1 sentence about what you're exploring in the space}.

Would you be open to a brief call?

Kay Schneider
Greenwich & Barrow
```

Draft in Gmail via gog. Kay reviews and sends from Superhuman.

### JJ's Call List (Tier C)

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
