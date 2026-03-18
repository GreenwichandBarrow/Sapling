---
name: target-discovery
description: "Find acquisition targets via Linkt + web research. Runs daily Tue-Thu during active sprint. Hands approved targets to outreach-manager."
user_invocable: true
context_budget:
  skill_md: 2000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Find targets. That's it.

This skill discovers acquisition targets via Linkt (primary list builder) and supplemental free research. Kay reviews the list. Approved targets go to skill/outreach-manager for all outreach drafting.

**Inputs from other skills:**
- **skill/niche-intelligence** — activated niche with one-pager, scorecard, buy-box target validation, ICP criteria, Linkt ICP already created
- **skill/pipeline-manager** — existing Attio contacts in this niche, intermediary referrals, deals already in pipeline (to avoid duplicates)

**Outputs to other skills:**
- Approved target list → skill/outreach-manager (cold outreach subagent)
- New targets added to Attio Active Deals at "Identified" → skill/pipeline-manager takes over from here

Goal: 4-6 qualified targets per day.
</objective>

<target_discovery>
## Target Discovery (Daily, Tue-Thu)

### Step 1: Run Linkt Search
Linkt is the primary list builder. It has the database. It finds companies matching the ICP, enriches them, and returns validated owner contact info — all in one step.

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
- **Conference exhibitor lists** — from conference-discovery skill outputs
- **Web search** — industry-specific searches for companies Linkt may have missed
- **Existing intelligence** — Attio pipeline, vault entities, niche one-pagers from niche-intelligence
- **Intermediary referrals** — deals forwarded by brokers, CPAs, network contacts

For companies found through free sources, use Linkt to enrich them (get validated contact info) if worth a credit.

### Step 3: Kay Reviews Target List
Present the combined list (Linkt + supplemental) to Kay. She reviews:
- Which targets are real acquisition candidates
- Remove any that don't fit (wrong size, PE-backed, already contacted, etc.)
- Flag any she has existing connections to (warm intro path)

### Step 4: Attio Dedup & Pipeline Entry
Before handing off to outreach-manager:
- Check every approved target against Attio Active Deals. If the person/company already exists in the pipeline, skip them.
- If they're already receiving outreach from conference-discovery (pre-conference email in flight), exclude from cold outreach.
- Add approved new targets to Attio Active Deals at "Identified" stage.

### Step 5: Handoff to Outreach Manager
Pass approved, deduped targets to skill/outreach-manager's cold outreach subagent with:
- Company name, website, headquarters
- Owner name, title, email, phone, LinkedIn
- Research context (what makes them a good target, any personal hooks found)
- Linkt enrichment data
</target_discovery>

<essential_principles>
## Principles

### Linkt Credit Management
- 150 credits/month = ~5-6 companies/day if running daily
- 1 credit = 1 entity (company or person)
- Linkt IS the list builder — discovery is what it's for, just keep searches tight and focused
- Run smaller, focused searches (10-20 entities) rather than large broad ones
- Supplemental free research extends the target pool without burning credits
- Save some credits for signal monitoring and conference attendee enrichment

### Team Roles (for this skill only)
- **Claude:** Run Linkt, supplement with free research, present list to Kay, dedup against Attio, hand off to outreach-manager
- **Kay:** Review target list, flag warm intro paths
- **Outreach Manager:** All outreach drafting (email, call list, follow-ups) — separate skill
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
- [ ] Target list reviewed by Kay
- [ ] Approved targets deduped against Attio
- [ ] Approved targets handed to outreach-manager
- [ ] New targets added to Attio Active Deals at "Identified"

### Weekly
- [ ] 20-30 targets discovered and handed off
- [ ] Sprint progress reviewed (Friday)
</success_criteria>
