---
name: list-builder
description: "Apollo API-based company discovery, contact enrichment, and target sheet population. Called by target-discovery when a niche needs new targets. Replaces Linkt as primary list builder."
user_invocable: false
context_budget:
  skill_md: 2500
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Build target lists. Find companies, find owners, get contact info, populate the sheet.

This skill is the list-building engine called by target-discovery. It takes ICP parameters (industry keywords, employee range, location, exclusions), searches Apollo for matching companies, cross-references the niche's existing target sheet, enriches missing contacts, adds new discoveries, and flags sub-threshold rows.

**Called by:** skill/target-discovery (when a niche needs new targets)
**Feeds into:** target sheet → Kay reviews (Col O) → skill/outreach-manager drafts outreach
**Replaces:** Linkt list building (legacy, cancelled March 31, 2026)

**What this skill does NOT do:**
- Does not decide which niches to search (that's target-discovery)
- Does not create outreach drafts (that's outreach-manager)
- Does not write to Attio (that's outreach-manager after Kay approves)
- Does not manage Linkt searches (legacy)
</objective>

<apollo_api>
## Apollo API Reference

API key stored at `/tmp/apollo-key.txt`. Read silently via Bash. Never echo.

```bash
APOLLO_KEY=$(cat /tmp/apollo-key.txt)
```

### Endpoints

| Endpoint | Method | Cost | Purpose |
|----------|--------|------|---------|
| `/api/v1/organizations/search` | POST | Free (0 credits) | Organization search — returns company LinkedIn, employee count, HQ, revenue |
| `/api/v1/mixed_people/search` | POST | Free but USELESS for contact data | Returns None for names and LinkedIn URLs without credit spend. Only confirms people exist. **Do NOT rely on this for owner names or LinkedIn profiles.** |
| `/api/v1/people/match` | POST | 1 credit (email) / 8 credits (phone) | Email and phone reveal — use AFTER identifying owner via web research |

### Credit Budget
- Plan: Basic ($64/mo), 2,500 credits/month
- Email reveal: 1 credit each — reveal for all targets
- Phone reveal: 8 credits each — skip by default, only reveal if Kay requests or target is approved and missing phone
- Hard cap: never exceed 100 credits in a single run without Kay's approval
- Alert threshold: flag if <500 credits remaining in the month
- Log credits consumed per run
</apollo_api>

<process>
## Step 1: Organization Search

Takes ICP parameters from target-discovery: industry keywords, employee range, location, exclusions.

**Default employee filters:**
- Art advisory niches: 10+ employees
- Insurance niches: 5+ employees
- Other: per target-discovery's ICP spec

**Run multiple keyword searches to maximize coverage.** Niches have aliases (e.g., "Trade Credit Insurance" = "Accounts Receivable Insurance" = "Credit Insurance"). Every alias gets its own search. Missing an alias = missing targets.

```bash
APOLLO_KEY=$(cat /tmp/apollo-key.txt)

curl -s -X POST "https://api.apollo.io/api/v1/organizations/search" \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: $APOLLO_KEY" \
  -d '{
    "q_organization_name": "{keyword}",
    "organization_num_employees_ranges": ["{min}-{max}"],
    "organization_locations": ["{location}"],
    "page": 1,
    "per_page": 25
  }'
```

**Returns (free):** company name, website, `linkedin_url` (company page), `estimated_num_employees`, headquarters, revenue. This is the primary source for company LinkedIn pages and real employee counts.

**Deduplication:** After all keyword searches complete, deduplicate results by domain. Same domain = same company regardless of which keyword surfaced it. Keep the richest record (most populated fields) when merging duplicates.

## Step 2: Cross-Reference Target Sheet

Read the niche's existing target sheet (Google Sheet) and match Apollo results against existing rows.

```bash
gog sheets get {SHEET_ID} "Active!B:C" -a kay.s@greenwichandbarrow.com -p
```

Match by:
1. Company name (Col B) — fuzzy match (e.g., "ABC Corp" = "ABC Corporation")
2. Website domain (Col C) — exact domain match after stripping protocol and www

Separate results into three buckets:
- **Existing (enrich):** Apollo found a company already on the sheet that has missing contact fields
- **New (add):** Apollo found a company NOT on the sheet
- **Already complete (skip):** Company is on the sheet with all contact fields populated

## Step 3: Enrich Existing Rows

For matched companies on the sheet that are missing contacts (owner name, email, LinkedIn):

**Owner identification (free — web search, NOT Apollo People Search):**
Apollo People Search returns `None` for names and LinkedIn URLs without credit spend. Use these sources instead:

1. **Company website** → About/Team/Leadership page (highest quality)
2. **LinkedIn company page** → People tab, filter by Founder/CEO/Owner/President
3. **Web search** → `"{company name}" founder OR owner OR CEO`
4. **State business registrations** → registered agent/officer

**Owner LinkedIn (free — web search):**
```
Web search: site:linkedin.com/in/ "{Owner Name}" "{Company Name}"
```
If no result: try without company name, verify by title/location match. If genuinely no LinkedIn presence, write "No LinkedIn presence" in Col M.

**Company LinkedIn + Employee Count (free — Apollo org search):**
```bash
curl -s -X POST "https://api.apollo.io/api/v1/organizations/search" \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: $APOLLO_KEY" \
  -d '{"q_organization_name": "{company name}", "per_page": 1}'
```
Returns: `linkedin_url` (company page), `estimated_num_employees`. If Apollo misses, web search `site:linkedin.com/company/ "{company name}"` and use LinkedIn's employee range.

**Employee count rules:** Apollo actual number (e.g., "40") or LinkedIn range (e.g., "11-50") — both are data-sourced and acceptable. Never write unsourced estimates.

**Email reveal (1 credit per contact):**
```bash
curl -s -X POST "https://api.apollo.io/api/v1/people/match" \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: $APOLLO_KEY" \
  -d '{
    "first_name": "{first}",
    "last_name": "{last}",
    "organization_name": "{company}",
    "domain": "{domain}",
    "reveal_personal_emails": false,
    "reveal_phone_number": false
  }'
```

**Phone reveal (8 credits — skip by default):**
Only reveal phone if explicitly requested by Kay or if the target is approved (Col O = "Approve") and missing phone. Set `"reveal_phone_number": true` in the match call.

**Write enriched data to sheet:**
```bash
gog sheets update {SHEET_ID} "Active!K{row}:M{row}" \
  -v "[[\"email@domain.com\",\"'(XXX) XXX-XXXX\",\"https://linkedin.com/in/slug\"]]" \
  -a kay.s@greenwichandbarrow.com --input USER_ENTERED
```

## Step 4: Add New Discoveries

For Apollo results NOT already on the target sheet.

**Filter out non-targets before adding:**
- Galleries, auctioneers, framers, museums (for art advisory niches)
- Non-advisory firms, parent company subsidiaries
- PE-owned companies (hard stop — never add)
- Companies below the employee minimum for this niche

**For each new company passing filters:**
1. People search for owner (free)
2. Email reveal (1 credit)
3. Phone reveal — skip unless explicitly requested

**Write gate (hard rule from target-discovery):** No row hits the Active tab without:
- Col C (Website) — populated
- Col I (Owner Name) — real person identified
- Col K (Email) OR Col L (Phone) OR Col M (LinkedIn Owner) — at least one contact method. LinkedIn DM is a valid outreach channel.

If a company can't meet this bar, log it as "could not enrich" in the run summary. Do NOT add it to the sheet.

**Append to sheet with standardized columns A-X:**

| Col | Field | Source |
|-----|-------|--------|
| A | Source | "Apollo" |
| B | Company | Apollo org name |
| C | Website | Apollo domain |
| D | Headquarters | Apollo city, state |
| E | Industry | Apollo industry or niche keyword |
| F | Employees | Apollo employee count |
| G | Revenue | Apollo estimated revenue (if available) |
| H | Ownership | "Independent" or flag if unclear |
| I | Owner Name | People search result |
| J | Owner Title | People search result |
| K | Email | Match/reveal result |
| L | Phone | Match/reveal result (if revealed) |
| M | LinkedIn (Owner) | People search result |
| N | LinkedIn (Company) | Apollo org LinkedIn URL |
| O | Kay: Decision | (blank — Kay fills) |
| P | Kay: Pass Reason | (blank — Kay fills) |
| Q | Agent Notes | "RECOMMEND: Approve" or "RECOMMEND: Pass" + reasoning |
| R-U | JJ Columns | (blank — JJ fills) |
| V | ICP Match | Assessment from Apollo data vs ICP criteria |
| W | ICP Miss Reason | If V is not a full match, explain why |
| X | Outreach Stage | (blank — outreach-manager fills) |

**Phone number formatting:** Apollo returns phones as `+1XXXXXXXXXX` or `+1 XXX-XXX-XXXX`. Always:
1. Strip country code prefix (`+1` or `+1 `)
2. Reformat to `(XXX) XXX-XXXX`
3. Write with apostrophe prefix: `'(XXX) XXX-XXXX` to prevent Google Sheets formula interpretation
4. Use `--input USER_ENTERED` flag on gog sheets update

**Agent Notes (Col Q):** Every row MUST start with a recommendation prefix:
- `RECOMMEND: Approve — {reasoning}` (e.g., "strong niche fit, 15 employees, verified email, independent ownership")
- `RECOMMEND: Pass — {reasoning}` (e.g., "PE-owned since 2022, skip" or "only 3 employees, below minimum")

## Step 5: Flag Sub-Threshold Rows

After enrichment and new additions, scan the full Active tab for rows below the employee minimum for this niche.

```bash
gog sheets get {SHEET_ID} "Active!B:F" -a kay.s@greenwichandbarrow.com -p
```

Report any rows where Col F (Employees) is below the niche's minimum threshold. Do NOT remove them. Flag for Kay's review in the run summary:
- "{Company} — {N} employees (minimum is {min} for this niche)"
</process>

<credit_management>
## Credit Management Rules

| Action | Cost | Policy |
|--------|------|--------|
| Organization search | Free | Run liberally, multiple keywords per niche |
| People search | Free | Run for every target, existing and new |
| Email reveal | 1 credit | Reveal for all targets on sheet |
| Phone reveal | 8 credits | Skip by default. Only if Kay requests or target is approved + missing phone |

**Per-run rules:**
- Log total credits consumed at end of every run
- Never exceed 100 credits in a single run without Kay's approval
- If a run would exceed 100 credits, pause and present: "{N} targets need email reveal ({N} credits). Approve?"

**Monthly tracking:**
- Track cumulative credits consumed this month
- Alert if <500 credits remaining
- At month boundary, reset counter

**Credit logging format:**
```
List Builder Run — {date}
Niche: {niche name}
Email reveals: {N} (x1 credit = {N} credits)
Phone reveals: {N} (x8 credits = {N} credits)
Total credits this run: {N}
Estimated remaining this month: {N}
```
</credit_management>

<validation>
## Validation (Stop Hooks)

Before reporting completion to target-discovery, verify all of the following. If any check fails, fix before returning results.

### 1. Deduplication Check
- [ ] All Apollo search results deduplicated by domain across keyword searches
- [ ] Cross-reference complete — no duplicate rows added to the sheet
- [ ] Company names and domains checked against existing Active tab AND Passed tab

### 2. Enrichment Completeness
- [ ] Every existing row with missing contacts had people search + email reveal attempted
- [ ] Enrichment data written to sheet for all available contacts
- [ ] Any rows that could not be enriched are logged in run summary

### 3. New Row Data Quality
- [ ] Every new row meets the write gate: Company name + Website + Owner Name + (Email OR LinkedIn)
- [ ] No rows added with blank Website (Col C)
- [ ] No rows added with "Unknown" in Owner Name (Col I)
- [ ] Agent Notes (Col Q) starts with "RECOMMEND: Approve" or "RECOMMEND: Pass" for every row

### 4. Formatting
- [ ] All phone numbers formatted as (XXX) XXX-XXXX with apostrophe prefix
- [ ] No raw Apollo phone formats on the sheet (+1, dashes, etc.)

### 5. Credit Budget
- [ ] Credits consumed this run logged
- [ ] Run did not exceed 100 credits without approval
- [ ] Monthly remaining credits calculated and reported
- [ ] Alert raised if <500 remaining

### 6. Sub-Threshold Flagging
- [ ] Active tab scanned for rows below employee minimum
- [ ] Sub-threshold rows listed in run summary (not removed)
</validation>

<essential_principles>
## Principles

### Apollo is the List Builder Now
Linkt was cancelled March 31, 2026. Apollo replaces it as the primary company discovery and contact enrichment tool. Organization search and people search are free. Only email/phone reveals cost credits. This makes Apollo dramatically more cost-effective for discovery at scale.

### Free First, Credits Second
Always exhaust free sources before spending credits:
1. Organization search (free) — find companies, get company LinkedIn + employee count
2. Web search (free) — find owners via company website, LinkedIn People tab, web search
3. Web search (free) — find owner LinkedIn profiles via `site:linkedin.com/in/`
4. Email reveal (1 credit) — only after confirming the person is the right contact
5. Phone reveal (8 credits) — only when explicitly needed

**Apollo People Search is NOT useful for contact discovery.** It returns `None` for names and LinkedIn URLs without credit spend. Use web research for owner identification and LinkedIn lookups.

### Sheet is the Staging Area
The target sheet is where targets live until Kay approves them. This skill writes to the sheet. It never writes to Attio. The flow is: list-builder populates sheet → Kay reviews → outreach-manager reads approvals → outreach-manager creates Attio entries.

### Accuracy Over Volume
Better to add 10 well-researched rows with verified contacts than 30 rows with missing data. The write gate exists because incomplete rows waste Kay's review time and create downstream failures (outreach-manager can't draft without email, JJ can't call without phone).

### One Master Sheet Per Niche
Append to the existing niche master sheet ("{Niche} - Target List" in LINKT TARGET LISTS folder). Never create new sheets per run. If the master sheet doesn't exist, target-discovery creates it from the template before invoking list-builder.
</essential_principles>

<success_criteria>
## Success Criteria

### Per Run
- [ ] Organization search completed across all niche keyword aliases
- [ ] Cross-reference against existing sheet completed (no duplicates)
- [ ] New targets added with minimum data quality (write gate passed)
- [ ] Existing targets enriched where contacts were missing
- [ ] Phone numbers properly formatted
- [ ] Agent Notes populated with RECOMMEND prefix on every row
- [ ] Credit usage logged and within budget
- [ ] Sub-threshold rows flagged
- [ ] Run summary returned to target-discovery with: new rows added, rows enriched, credits consumed, sub-threshold flags
</success_criteria>
