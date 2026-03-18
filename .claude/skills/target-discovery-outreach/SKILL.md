---
name: target-discovery-outreach
description: "Find acquisition targets via Linkt + web research, draft personalized owner outreach, build JJ's call list. Runs daily Tue-Thu during active sprint."
user_invocable: true
context_budget:
  skill_md: 3000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Find targets. Draft outreach. That's it.

This skill does two things: discover acquisition targets and draft personalized outreach (emails for Kay, call list for JJ). Everything before this (niche selection, ICP, scorecard, one-pager) is handled by skill/niche-intelligence. Everything after this (pipeline tracking, stage progression, nurture, follow-ups) is handled by skill/pipeline-manager. Conference-related outreach is handled by skill/conference-prep.

**Inputs from other skills:**
- **skill/niche-intelligence** — activated niche with one-pager, scorecard, buy-box target validation, ICP criteria, Linkt ICP already created
- **skill/pipeline-manager** — existing Attio contacts in this niche, intermediary referrals, deals already in pipeline (to avoid duplicates)
- **skill/conference-prep** — conference attendee/exhibitor lists (supplemental target source)

**Outputs to other skills:**
- New targets added to Attio Active Deals at "Identified" → skill/pipeline-manager takes over from here
- JJ's call outcomes feed back into pipeline-manager for stage progression

Goal: 4-6 qualified targets per day → personalized email drafts for Kay + call list for JJ.
</objective>

<target_discovery>
## Phase 1: Target Discovery (Daily, Tue-Thu)

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

### Step 3b: Attio Dedup Check
Before moving to outreach, check every approved target against Attio Active Deals. If the person/company already exists in the pipeline, skip them. If they're already receiving a pre-conference email from conference-prep, exclude from cold outreach — the conference framing is stronger and you don't want to dilute it.

### Step 4: Outreach Assignment
Every approved target gets quality attention. For each target, Claude:
- Does deep web research on the company and owner (beyond what Linkt provides)
- Drafts a personalized email for Kay to send (Day 1 of cadence)
- Adds the owner to JJ's call sheet with confirmation call date (Day 3)
- Adds target to Attio Active Deals at "Identified" (pipeline-manager takes over from here)
</target_discovery>

<outreach>
## Phase 2: Outreach Cadence (Per Target)

Each target goes through a sequenced multi-channel cadence. Email first, then JJ confirms, then follow-up if needed.

### Outreach Sequence

| Day | Channel | Who | Action |
|-----|---------|-----|--------|
| Day 1 | Email | Kay (via Superhuman draft) | Personalized cold email |
| Day 3 | Phone | JJ | Confirmation call — "wanted to make sure you received Kay's note" |
| Day 5-6 | Email | Kay (via Superhuman draft) | Follow-up email if no response — short, one line |
| Day 8-10 | LinkedIn DM | Kay (manually) | High-value targets only, if email + call didn't land |

After Day 10 with no response, move to nurture cadence (pipeline-manager handles from here).

**Why this sequence:** The email establishes who Kay is and gives the owner time to check LinkedIn (where Kay's Chanel/luxury background closes the credibility gap). JJ's call 2 days later references the email, making it a warm confirmation rather than a cold call. The follow-up email is a lightweight bump. LinkedIn DM is the escalation reserved for high-fit targets.

### Day 1: Kay's Email

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

Draft in Superhuman via the `superhuman` MCP server using the `superhuman_draft` tool with `--account kay.s@greenwichandbarrow.com`. This creates native Superhuman drafts that appear in Kay's drafts folder. Do NOT use `gog gmail drafts create` — Gmail API drafts do not sync to Superhuman. Kay reviews and sends from Superhuman.

### Day 3: JJ's Confirmation Call

JJ calls to confirm receipt of Kay's email. This is NOT a cold call — it's a warm follow-up.

**Script:**
```
Hi, this is JJ calling on behalf of Kay Schneider at Greenwich & Barrow.
Kay sent {owner name} a note a couple days ago and I just wanted to make
sure it came through. She's been researching the {niche} space and would
love to connect briefly with {owner name} about their experience.
Would {owner name} have 15 minutes for a quick call?
```

**Call sheet** — Google Sheet in LINKT TARGET LISTS folder:
| Company | Owner Name | Phone | Location | Email Sent Date | Call Date (Day 3) | Script | Status | Notes |

JJ logs status: Connected, Voicemail, Callback Requested, Not Interested, Wrong Number.

### Day 5-6: Follow-Up Email

If no response to email or call, Kay sends a short follow-up. One or two sentences max.

```
Hi {first name},

Just circling back on my note from earlier this week. Would love to find a time to connect.

Kay
```

Draft in Superhuman. Kay reviews and sends.

### Day 8-10: LinkedIn DM (High-Value Only)

Reserved for targets that are a strong fit but haven't responded to email or phone. Kay sends personally from her LinkedIn. Claude drafts the message, Kay copies and sends.

Not every target gets this. Only use for owners where the company is a clear buy-box match and worth the extra touch.

### Conference Exclusion Rule

If a target is already receiving pre-conference outreach from conference-prep, do NOT run the cold outreach cadence. The conference framing ("I'll be at your booth Thursday") is stronger than cold email. Let conference-prep own that relationship until post-conference follow-up is complete.
</outreach>

<essential_principles>
## Principles

### Volume & Cadence
- 4-6 owners contacted per day (funds that acquired averaged 4, not 9)
- Quality over quantity — deep research on each target, personalized outreach
- Sequenced multi-channel: email Day 1 → JJ confirmation call Day 3 → follow-up email Day 5-6 → LinkedIn DM Day 8-10 (high-value only)
- Conference targets excluded from cold cadence (conference-prep owns that relationship)

### Linkt Credit Management
- 150 credits/month = ~5-6 companies/day if running daily
- 1 credit = 1 entity (company or person)
- Create tight ICPs so search results are pre-qualified
- Run smaller, focused searches (10-20 entities) rather than large broad ones
- Supplemental free research extends the target pool without burning credits

### Team Roles (for this skill only)
- **Claude:** Run Linkt, supplement with free research, deep research per target, draft emails, build call list
- **Kay:** Review target list, review/send emails, take Stage 1 calls
- **JJ:** Cold call from sheet, log outcomes
- **Analyst:** Company scorecards for approved targets (when requested)

### Sprint Check-In (Every 2 Weeks)
At the 2-week mark, evaluate:
- How many targets found in this niche?
- Response rate from owners?
- Any meaningful conversations?
- Is the target pool deep enough to continue?
- Kill, advance, or table this niche?

If the niche is running dry, escalate to Kay. Don't wait 8 weeks.
</essential_principles>

<success_criteria>
## Success Criteria

### Daily
- [ ] 4-6 new targets discovered and researched
- [ ] Email drafts ready for Kay's review
- [ ] JJ's call sheet updated
- [ ] New targets added to Attio Active Deals at "Identified"

### Weekly
- [ ] 20-30 owners contacted (email + phone combined)
- [ ] Sprint progress reviewed (Friday)
</success_criteria>
