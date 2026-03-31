---
name: target-discovery
description: "Find acquisition targets via Linkt + web research. Runs daily Mon-Fri during active sprint. Hands approved targets to outreach-manager."
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
- Approved target list (Col O = "Approve") → skill/outreach-manager creates Attio entry at "Identified" → skill/pipeline-manager takes over from here

Goal: 4-6 qualified targets per day.
</objective>

<target_discovery>
## Target Discovery (Daily, Mon-Fri)

### Industry Name Aliases (CRITICAL)
Niches often have multiple names. **Every search — Linkt, web, association directories — must use ALL known aliases**, not just the primary name. Missing an alias = missing targets.

The niche one-pager (from niche-intelligence) must include an "Also Known As" section listing all aliases. Pull aliases from:
- Industry association websites (how they describe the service)
- Target company websites (how they brand themselves)
- Carrier/underwriter sites (how they categorize the product)

Example: "Trade Credit Insurance" is also called "Accounts Receivable Insurance", "A/R Insurance", "Credit Insurance", "Receivables Insurance". A broker branding as "accounts receivable insurance specialist" won't show up in a TCI-only search.

**For Linkt:** Run separate searches for each alias if the ICP search field is keyword-based.
**For web research:** Rotate through all aliases in searches. Don't stop at the primary name.

### Step 1: Run Linkt Search (DISCOVERY ONLY)

**NOTE: Linkt is on Starter plan as of March 31, 2026. Upgrade to Pro in sprints when needed. When upgrading, run a full E2E test first via MCP (create ICP → sheets → task → execute → verify results with hide_duplicates) before burning credits on real searches.**

Linkt is the primary list builder for discovering NEW companies. It finds companies matching the ICP and returns enriched data including owner contact info. **All Linkt operations use MCP tools** (not raw API calls).

**Linkt discovers AND enriches** — companies it finds come back with full contact data. That's fine, that's what a credit buys you. **But do NOT use Linkt credits to enrich companies found through OTHER sources** (free research, associations, referrals, conferences). Those get contact-scraped manually (Step 2b). Linkt credits = discovering companies we don't know about yet.

**Use ALL niche aliases in Linkt searches.** Run separate search tasks per alias if needed. Each alias may surface different companies.

#### Linkt Integration via MCP (All Steps Required — STOP HOOK)

**Linkt is connected as an MCP server.** Use MCP tools (not raw API calls) for all Linkt operations. The MCP server handles authentication and request formatting.

**Before running any Linkt search, verify ALL of these or the search will silently fail:**
1. ICP has `entity_targets` array (company + person entries, one marked `root: true`)
2. Sheets exist for the ICP (company sheet + person sheet)
3. ICP description includes the target count as text (e.g., "Find 50 independently owned...")
4. `desired_count` parameter is IGNORED — only the description text matters

**ICP Naming Convention:** Always name ICPs with the date they are created: `"{Niche} {YYYY-MM-DD}"` (e.g., "IPLC 2026-04-01"). Never use version numbers (v1, v2, v3).

**Correct MCP flow:**
```
# Step 1: Create ICP with entity_targets
mcp__linkt__create_icp_v1_icp_post
  name: "{Niche} {YYYY-MM-DD}"
  description: "Find 50 independently owned {criteria}..."
  entity_targets: [
    {"entity_type": "company", "description": "{what makes a good target company}", "root": true},
    {"entity_type": "person", "description": "{decision-maker criteria}", "desired_count": 1}
  ]

# Step 2: Create sheets (REQUIRED before task execution)
mcp__linkt__create_sheet_v1_sheet_post
  name: "{Niche} - Companies {YYYY-MM-DD}", icp_id: "{icp_id}", entity_type: "company"
mcp__linkt__create_sheet_v1_sheet_post
  name: "{Niche} - People {YYYY-MM-DD}", icp_id: "{icp_id}", entity_type: "person"

# Step 3: Create search task
mcp__linkt__create_task_v1_task_post
  name: "{Niche} Search {YYYY-MM-DD}"
  flow_name: "search"
  deployment_name: "search"
  icp_id: "{icp_id}"
  task_config: {"type": "search", "desired_contact_count": 1}

# Step 4: Execute task
mcp__linkt__execute_task_v1_task
  task_id: "{task_id}", icp_id: "{icp_id}"

# Step 5: Monitor run
mcp__linkt__get_run_v1_run  (check status)
mcp__linkt__get_run_queue_v1_run  (see processed entities)

# Step 6: Export results (ALWAYS use hide_duplicates)
mcp__linkt__export_entities_v1_entity_export_get
  icp_id: ["{icp_id}"], format: "combined", hide_duplicates: true
# OR list entities:
mcp__linkt__list_entities_v1_entity_get
  icp_id: ["{icp_id}"], hide_duplicates: true, page_size: 100
```

**Deduplication:** ALWAYS pass `hide_duplicates: true` when listing or exporting entities. Without this flag, Linkt returns multiple entries per company (company entity + person entities + potential duplicates). This was the cause of the Howard & Gay triple-entry issue on 2026-03-30.

**Credit model:** Each entity costs 1 credit. A company + 1 person contact = 2 credits per target. With 15 targets requested, expect ~30 credits per search.

**CRITICAL LESSON:** ICPs created without `entity_targets` will show status "Complete" immediately with 0 results. This is a silent failure — it looks like Linkt ran and found nothing, but it never actually searched. This was the root cause of all failed searches in March 2026.

**Platform bug (2026-03-30):** 4 of 5 ICPs failed because icp_id was null on run documents. If this recurs with MCP, delete the broken ICP + task and recreate from scratch. The MCP server may use a different code path that avoids the bug.

Linkt's AI agents will:
- Find companies matching the ICP criteria (industry, size, geography, ownership)
- Enrich each company with revenue, employee count, ownership status
- Identify the owner/CEO with validated email and phone
- Verify criteria matches against the ICP

**Run smaller, focused searches** (10-20 entities per run) rather than large broad ones. Each entity = 1 credit. Pro plan = 300 credits/month. Put the target count in the ICP description text (the `desired_count` API parameter is ignored). Default to requesting 15 entities per search in the description. If the ICP is narrow (e.g., one niche in one state), request 10. If broad (national search), request 20 max.

**Output:** Linkt returns enriched entities. Only write to the sheet after verifying minimum data bar (see Write Gate below). Append to the niche sprint's master sheet ("{Niche} - Target List") in LINKT TARGET LISTS folder. One master sheet per niche sprint — do NOT create new sheets per run. New results append to the "Active" tab.

If the master sheet doesn't exist yet (first run of a new sprint), **COPY the template sheet** — do NOT create a blank sheet. The template has all headers, dropdowns, column formatting, and orange header on Col O already configured.

```bash
# Copy the template sheet (preserves all formatting, dropdowns, orange headers)
gog drive copy 1wIK4Jv56QIZejcmpq-gGrCWAPe07eJWUbKsWTRwh778 "{Niche} - Target List" -a kay.s@greenwichandbarrow.com --parent 1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc -j
```


**Template must include:** All columns A through AB, with dropdowns on Col AA (1st, 2nd, 3rd) and Col AB (Drafted, Sent, Responded, No Response). If the template doesn't have these columns yet, add them before the first run of a new sprint.

This ensures Kay never has to manually copy dropdowns. The template is the single source of truth for sheet structure.

When Kay marks a row "Pass" in Col O, move it to the "Passed" tab with all data preserved.

**Phone number formatting:** Linkt returns phones as `+1 973-770-9090`. When writing to Google Sheets:
1. Strip the country code prefix (`+1 `)
2. Reformat to `(XXX) XXX-XXXX` (e.g., `(973) 770-9090`)
3. Write with `--input USER_ENTERED` and apostrophe prefix (`'(973) 770-9090`) to prevent formula interpretation
This must happen on every Linkt pull, not as a cleanup step.

### Art Storage Niche: Activity Report Cross-Reference (STOP HOOK)
When discovering targets for the art storage niche, cross-reference every candidate against the Activity Report (Google Sheet) which contains companies already contacted in prior outreach rounds. Do NOT rediscover or re-add companies that are already on the Activity Report. This avoids duplicate outreach and wasted research time on known companies.

### Step 2: Supplement with Free Sources
Linkt won't find everything. Supplement with free research:

- **Association directories** — member lists, state licensing board registries
- **Conference exhibitor lists** — from conference-discovery skill outputs
- **Web search** — search ALL niche aliases (not just the primary name) for companies Linkt may have missed
- **Existing intelligence** — Attio pipeline, vault entities, niche one-pagers from niche-intelligence
- **Intermediary referrals** — deals forwarded by brokers, CPAs, network contacts

### Step 2b: Enrichment for Free-Source Companies (FREE — do not use Linkt credits)
For companies found through free research (Step 2), research and populate ALL missing fields — not just contacts. Every row must have the same data quality as Linkt-sourced rows.

**Website is mandatory.** Every target MUST have a website (col C) before being added to the sheet. Web search "{Company Name} {City}" to find it. No blank website cells.

Enrich in this order:
1. **Company website** (col C) — find via web search first, then use the site for everything else
2. **Company details** — Headquarters, Employees, Revenue, Ownership (cols D-H) from website, LinkedIn, press
3. **Owner/CEO contact** — About Us, Team, Leadership pages for name and title
4. **LinkedIn** — company page → People tab → filter by CEO/President/Owner/Founder
5. **State business registrations** — registered agent/officer filings (Secretary of State websites)
6. **Press releases / news** — owner names often appear in local business news
7. **Industry association member directories** — sometimes list key contacts

Populate cols C-N (Website, Headquarters, Industry, Employees, Revenue, Ownership, Owner Name, Title, Email, Phone, LinkedIn Owner, LinkedIn Company). If company phone is all that's findable, note "(main)" in the cell. JJ validates phone numbers on his calls.

**Do NOT burn Linkt credits on enrichment.** If we already know the company exists, the contact info can be found manually or by JJ.

### Write Gate (HARD RULE)
**No row hits the Active tab until it meets ALL of these:**
- Col C (Website) — populated and verified (loads a real page, not a redirect to a parent company)
- Col I (Owner Name) — real person identified, not "Unknown"
- Col K (Email) OR Col L (Phone) — at least one contact method

This applies to ALL sources — Linkt, free research, associations, referrals. No exceptions. If enrichment can't meet this bar after a reasonable research effort, log the company name in the daily briefing as "could not enrich" with what's missing. Do NOT add it to the sheet with blank fields for Kay to catch.

### LinkedIn Tracking Columns (added by outreach-manager overnight prep)

- **Col AA: LinkedIn Connection Degree** — "1st", "2nd - {mutual name}", "3rd", or blank. Auto-populated during overnight prep by cross-referencing against Kay's 901 imported LinkedIn connections. Kay manually updates "2nd - {mutual name}" when she spots mutual connections.
- **Col AB: Kay: LinkedIn DM Status** — Dropdown: `Drafted` | `Sent` | `Responded` | `No Response`. Set to "Drafted" when outreach-manager creates the Slack DM. Kay updates to "Sent" after sending. Kay updates to "Responded" when reply received. Auto-set to "No Response" after 10 business days.

### Step 3: Kay Reviews Target List
Present the combined list (Linkt + supplemental) to Kay. She reviews:
- Which targets are real acquisition candidates
- Remove any that don't fit (wrong size, PE-backed, already contacted, etc.)
- Warm intro paths pre-identified by pipeline-manager (Kay reviews, does not need to flag manually)

### Step 4: Attio Dedup Check (Read-Only)
Before handing off to outreach-manager:
- Check every approved target against Attio Active Deals. If the person/company already exists in the pipeline, flag them on the target sheet (Col P: "Already in Attio") and skip.
- If they're already receiving outreach from conference-discovery (pre-conference email in flight), exclude from cold outreach.
- **Do NOT create Attio records.** Target-discovery only writes to the Google Sheet. Outreach-manager creates Attio entries at "Identified" stage after Kay approves in Col O. This keeps the CRM clean — only approved targets enter the pipeline.

### Step 5: Handoff to Outreach Manager
Pass approved, deduped targets to skill/outreach-manager's cold outreach subagent with:
- Company name, website, headquarters
- Owner name, title, email, phone, LinkedIn
- LinkedIn Owner URL (Col M) — for LinkedIn DM drafting and connection degree lookup
- Research context (what makes them a good target, any personal hooks found)
- Linkt enrichment data
</target_discovery>

<essential_principles>
## Principles

### Linkt Credit Management
- Starter plan as of March 31, 2026 — upgrade to Pro ($300/mo, 300 credits) in sprints when actively running discovery
- 1 credit = 1 entity (company or person). Each target = ~2 credits (1 company + 1 person contact).
- Linkt IS the list builder — discovery is what it's for, just keep searches tight and focused
- Run smaller, focused searches (10-15 entities) rather than large broad ones
- Supplemental free research extends the target pool without burning credits
- When upgrading: run full E2E test via MCP (create ICP → sheets → task → execute → verify results with hide_duplicates) before burning credits on real searches
- ALWAYS export/list with `hide_duplicates: true` to avoid inflated entity counts

### Team Roles (for this skill only)
- **Claude:** Run Linkt, supplement with free research, present list to Kay, dedup against Attio, hand off to outreach-manager
- **Kay:** Review target list, flag warm intro paths
- **Outreach Manager:** All outreach drafting (email, call list, follow-ups) — separate skill
- **Analyst:** Company scorecards for approved targets (when requested)

### ICP Calibration Loop

The ICP is a living document. Track these signals to know if it needs adjustment:

**After Kay reviews target list:**
- Track accept/reject rate. Rejecting 50%+ = ICP too loose. Accepting all but pool is tiny = ICP too tight.
- Log rejection reasons (wrong size, PE-backed, wrong industry, wrong geography). Patterns in rejections = ICP criteria to tighten.

**After JJ's calls (from outreach-manager):**
- High "Wrong Number" rate = bad contact data from Linkt, not an ICP problem.
- High "Not Interested" rate = wrong type of company. ICP may need adjustment.
- Connected + positive conversations = ICP is working.

**After outreach responses (from outreach-manager):**
- Response rate by batch. No responses from an entire batch = wrong audience.
- Response quality. "Not selling" = ICP identified the right companies but wrong timing. "Wrong person" = contact criteria need tightening.

**Sprint check-in (every 2 weeks):**
Pull all the above metrics and explicitly evaluate:
- Should we tighten, loosen, or shift the ICP criteria?
- Are Linkt search parameters matching what Kay actually approves?
- Credit efficiency: how many credits per approved target?

If the niche is running dry or ICP is consistently off, escalate to Kay. Don't wait 8 weeks.
</essential_principles>

<validation>
## Validation (Stop Hooks)

After target discovery completes, verify all deliverables before notifying Kay:

### Step 1: Sheet Validation
- Confirm Google Sheet in LINKT TARGET LISTS folder has new rows with today's date
- Verify phone numbers are formatted correctly: `(XXX) XXX-XXXX`

### Step 1b: Contact Completeness Check (STOP HOOK)
Read every row on the Active tab. For each row, check cols I-L (Owner Name, Title, Email, Phone):

```bash
gog sheets get {SHEET_ID} "Active!B:L" -a kay.s@greenwichandbarrow.com -p
```

**Flag every row missing ANY of these:**
- Col C (Website) — empty (mandatory for all targets, no exceptions)
- Col I (Owner Name) — empty or "Unknown"
- Col K (Email) — empty
- Col L (Phone) — empty

**If missing contacts found:**
1. Spawn a sub-agent to scrape contact info for those companies (Step 2b process: company website, LinkedIn, state registrations, press releases)
2. Update the sheet with whatever is found
3. Re-check after scraping
4. Any STILL missing after scraping → flag in the daily briefing: "{n} targets missing contact info. JJ to validate."

**A target cannot be handed to outreach-manager without at minimum: Owner Name + (Email OR Phone).** This is a hard gate. No contact info = no outreach.

### Step 2: Attio Dedup Validation
- Confirm Attio was checked (read-only) for existing entries before handoff
- Confirm no Attio records were CREATED by target-discovery (Attio writes happen in outreach-manager only)

### Step 3: Handoff Validation
- Confirm target data was passed to outreach-manager with all required fields
- Confirm no targets are missing email (required for Day 1 email)
- Confirm no targets are missing phone (required for JJ Day 3 call)

### Step 4: Credit Tracking
- Log credits consumed this run
- Calculate remaining monthly credits
- Flag if <20 credits remaining this month

### Step 5: Slack Notification
Only after all validation passes:
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Target list ready for review — {n} new targets in {niche}.\n{n} credits used ({n} remaining this month).\nhttps://docs.google.com/spreadsheets/d/{SHEET_ID}/edit"}'
```

If validation fails, do NOT send Slack. Report the failure and fix before notifying.
</validation>

<success_criteria>
## Success Criteria

### Daily
- [ ] 4-6 new targets discovered and researched
- [ ] Google Sheet populated with new targets
- [ ] Kay notified via Slack with sheet link
- [ ] Target list reviewed by Kay
- [ ] Approved targets deduped against Attio (read-only check)
- [ ] Approved targets handed to outreach-manager (which creates Attio entries)
- [ ] Credits consumed logged

### Weekly
- [ ] 20-30 targets discovered and handed off
- [ ] ICP accept/reject rate tracked
- [ ] Sprint progress reviewed
</success_criteria>
