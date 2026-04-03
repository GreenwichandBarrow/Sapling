---
name: target-discovery
description: "Find acquisition targets via list-builder (Apollo) + web research. Runs daily Mon-Fri for Active-Outreach niches. Hands approved targets to outreach-manager."
user_invocable: true
context_budget:
  skill_md: 2000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Find targets. That's it.

This skill discovers acquisition targets via skill/list-builder (Apollo, primary) and supplemental free research. Kay reviews the list. Approved targets go to skill/outreach-manager for all outreach drafting.

**Trigger:** Niche status changes to Active-Outreach on the Industry Research Tracker. All Active-Outreach niches run at full 4-6 targets/day.

**Pipeline stages:** Under Review → Active-Outreach → Wind Down → Tabled/Killed

**Inputs from other skills:**
- **skill/niche-intelligence** — activated niche with one-pager, scorecard, buy-box target validation, ICP criteria
- **skill/pipeline-manager** — existing Attio contacts in this niche, intermediary referrals, deals already in pipeline (to avoid duplicates)

**Outputs to other skills:**
- Approved target list → skill/list-builder (Apollo search) + skill/outreach-manager (email drafts)
- Approved target list (Col O = "Approve") → skill/outreach-manager creates Attio entry at "Identified" → skill/pipeline-manager takes over from here

Goal: 4-6 qualified targets per day.
</objective>

<target_discovery>
## Target Discovery (Daily, Mon-Fri)

### Industry Name Aliases (CRITICAL)
Niches often have multiple names. **Every search — Apollo, web, association directories — must use ALL known aliases**, not just the primary name. Missing an alias = missing targets.

The niche one-pager (from niche-intelligence) must include an "Also Known As" section listing all aliases. Pull aliases from:
- Industry association websites (how they describe the service)
- Target company websites (how they brand themselves)
- Carrier/underwriter sites (how they categorize the product)

Example: "Trade Credit Insurance" is also called "Accounts Receivable Insurance", "A/R Insurance", "Credit Insurance", "Receivables Insurance". A broker branding as "accounts receivable insurance specialist" won't show up in a TCI-only search.

**For Apollo:** Run separate keyword searches for each alias.
**For web research:** Rotate through all aliases in searches. Don't stop at the primary name.

### INLINE ENRICHMENT MANDATE (CRITICAL)

**No row is written to the sheet until ALL enrichment steps complete for that target.** Discovery and enrichment are one atomic operation, not two phases. By the time Kay sees the target list, every row must have real, sourced data — not estimates or gaps to backfill later.

For EVERY target, regardless of source (Apollo, web research, associations, referrals), run all 5 enrichment phases before writing to the sheet:

1. **Company data** (Apollo org search or web) → LinkedIn page, employee count, HQ
2. **Owner identification** (company website, LinkedIn People tab, web search)
3. **Owner LinkedIn** (web search)
4. **Email verification** (Apollo people match, 1 credit)
5. **Write complete row** → only after all phases pass

### Step 1: Discover Companies

**Primary: Apollo Organization Search (free, via skill/list-builder)**
Invoke skill/list-builder with ICP parameters. Apollo finds companies matching industry keywords, employee range, location. Returns company name, website, LinkedIn page, employee count, HQ, revenue.

**Supplemental: Free Sources**
Apollo won't find everything. Also search:
- **Association directories** — member lists, state licensing board registries
- **Conference exhibitor lists** — from conference-discovery skill outputs
- **Web search** — search ALL niche aliases for companies Apollo missed
- **Existing intelligence** — Attio pipeline, vault entities, niche one-pagers
- **Intermediary referrals** — deals forwarded by brokers, CPAs, network contacts

**MINIMUM SEARCH BREADTH (CRITICAL):**
- Run 10-15+ keyword variations per niche, not just the primary name
- Pull keyword aliases from the niche one-pager’s "Also Known As" section
- If the one-pager doesn’t have enough aliases, generate them: synonyms, industry jargon, service descriptions, regional terms
- Apollo org search is FREE — there is zero cost to running more keyword variations. Run liberally.

**SUPPLEMENTAL SOURCES ARE MANDATORY, NOT OPTIONAL:**
- If Apollo returns < 10 candidates across all keyword variations, the agent MUST run supplemental sources before stopping
- Supplemental sources: association directories, web search for "{niche} companies", LinkedIn company search, conference exhibitor lists, state licensing board registries
- Target: 15-20 candidates discovered, filtered to 4-6 that pass the write gate
- Log in the briefing: "Apollo returned {n} candidates across {n} keyword searches. Supplemental sources added {n} more."
- If total candidates (Apollo + supplemental) is still < 10 after exhausting all sources, log it as a niche intelligence signal — the niche may be smaller than estimated

### Step 2: Enrich Each Target (Inline — Before Writing to Sheet)

For EVERY discovered company, run these enrichment phases in order. This applies to ALL sources — Apollo, web research, associations, referrals. No exceptions.

#### Phase A: Company Data (free)
```
Apollo /organizations/search → {
  linkedin_url, estimated_num_employees, headquarters, revenue
}
```
If Apollo misses: web search `site:linkedin.com/company/ "{company name}"` for company LinkedIn page. Get employee count from LinkedIn company page (range like "11-50" is fine — it's sourced data).

**Employee count rules:**
- Apollo actual number (e.g., "40") → use it
- LinkedIn range (e.g., "11-50") → use it as-is, it's data-sourced
- NEVER write unsourced estimates (e.g., "10-25" from guesswork)

#### Phase B: Owner Identification (free)
Find the owner/founder/CEO in this priority order:
1. **Company website** → About/Team/Leadership page (highest quality)
2. **LinkedIn company page** → People tab, filter by Founder/CEO/Owner/President
3. **Web search** → `"{company name}" founder OR owner OR CEO`
4. **State business registrations** → registered agent/officer filings

#### Phase C: Owner LinkedIn (free)
```
Web search: site:linkedin.com/in/ "{Owner Name}" "{Company Name}"
```
If no result: try without company name, verify by title/location match.

**Not a gate** — some people genuinely don't have LinkedIn (common in fine art world). Mark Col M as "No LinkedIn presence" and move on.

#### Phase D: Email Verification (1 credit per target)
```
Apollo /people/match → {
  first_name, last_name, organization_name, domain
} → verified business email
```

#### Phase E: Assemble Complete Row
Only after Phases A-D complete, assemble the row with all columns populated. Then check the Write Gate.

**CRITICAL: Apollo People Search (`/mixed_people/search`) returns `None` for names and LinkedIn URLs without credit spend.** The "free" endpoint only confirms people exist at a company. Do NOT rely on it for owner names or LinkedIn profiles. Use web search (Phase B and C) instead.

### Art Storage Niche: Activity Report Cross-Reference (STOP HOOK)
When discovering targets for the art storage niche, cross-reference every candidate against the Activity Report (Google Sheet) which contains companies already contacted in prior outreach rounds. Do NOT rediscover or re-add companies that are already on the Activity Report.

### Write Gate (HARD RULE)
**No row hits the Active tab until it meets ALL of these:**
- Col C (Website) — populated and verified (loads a real page, not a redirect to a parent company)
- Col I (Owner Name) — real person identified, not "Unknown"
- Col K (Email) OR Col L (Phone) OR Col M (LinkedIn Owner) — at least one contact method. LinkedIn DM is a valid outreach channel.
- Col M (LinkedIn Owner) — populated with URL, or explicitly "No LinkedIn presence"
- Col N (LinkedIn Company) — populated with URL, or explicitly "No company page"
- Col F (Employees) — sourced number or LinkedIn range, never unsourced estimate

This applies to ALL sources. No exceptions. If enrichment can't meet this bar after reasonable effort, log the company name in the daily briefing as "could not enrich" with what's missing. Do NOT add it to the sheet with blank fields for Kay to catch.

### Sheet Structure

Append to the niche sprint's master sheet ("{Niche} - Target List") in LINKT TARGET LISTS folder. One master sheet per niche sprint — do NOT create new sheets per run. New results append to the "Active" tab.

If the master sheet doesn't exist yet (first run of a new sprint), **COPY the template sheet**:

```bash
gog drive copy 1wIK4Jv56QIZejcmpq-gGrCWAPe07eJWUbKsWTRwh778 "{Niche} - Target List" -a kay.s@greenwichandbarrow.com --parent 1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc -j
```

**Template columns A-X:**
- A-N: Source through LinkedIn (Company) — list building data
- O: Kay: Decision (Approve/Pass)
- P: Kay: Pass Reason
- Q: Agent Notes (MUST start with "RECOMMEND: Approve" or "RECOMMEND: Pass" + reasoning)
- R-U: JJ columns (Call Status, Call Date, Call Notes, Owner Sentiment)
- V: ICP Match
- W: ICP Miss Reason
- X: Outreach Stage (Approved → Email Drafted → Email Sent → JJ Queued → JJ Called)

When Kay marks a row "Pass" in Col O, move it to the "Passed" tab with all data preserved.

**Phone number formatting:** Always:
1. Strip country code prefix (`+1` or `+1 `)
2. Reformat to `(XXX) XXX-XXXX`
3. Write with apostrophe prefix and `--input USER_ENTERED`

### Outreach Stage Flow (Col X — trigger column)
`Approved` → `Email Drafted` → `Email Sent` → `JJ Queued` → `JJ Called`

Each stage transition triggers the next skill in the pipeline:
- Kay sets Col O = "Approve" → outreach-manager drafts email, sets Col X = "Email Drafted"
- Email confirmed sent → Col X = "Email Sent"
- jj-operations picks up targets where Col X = "Email Sent" → sets Col X = "JJ Queued"
- JJ completes call → Col X = "JJ Called", JJ columns R-U populated

### Step 3: Kay Reviews Target List
Present the combined list (Apollo + supplemental) to Kay. She reviews:
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
- Apollo enrichment data
</target_discovery>

<essential_principles>
## Principles

### Apollo Credit Management
- Plan: Basic ($64/mo), 2,500 credits/month
- Organization search: FREE — run liberally
- People search: FREE — but returns None for names/LinkedIn (useless for contact data)
- Email reveal: 1 credit each — reveal for all targets
- Phone reveal: 8 credits each — skip by default
- Hard cap: never exceed 100 credits in a single run without Kay's approval
- At ~1 credit per target (email only), supports ~2,500 targets/month

### Team Roles (for this skill only)
- **Claude:** Run Apollo via list-builder, supplement with free research, enrich inline, present complete list to Kay, dedup against Attio, hand off to outreach-manager
- **Kay:** Review target list, flag warm intro paths
- **Outreach Manager:** All outreach drafting (email, call list, follow-ups) — separate skill

### ICP Calibration Loop

The ICP is a living document. Track these signals to know if it needs adjustment:

**After Kay reviews target list:**
- Track accept/reject rate. Rejecting 50%+ = ICP too loose. Accepting all but pool is tiny = ICP too tight.
- Log rejection reasons (wrong size, PE-backed, wrong industry, wrong geography). Patterns in rejections = ICP criteria to tighten.

**After JJ's calls (from outreach-manager):**
- High "Wrong Number" rate = bad contact data, not an ICP problem.
- High "Not Interested" rate = wrong type of company. ICP may need adjustment.
- Connected + positive conversations = ICP is working.

**After outreach responses (from outreach-manager):**
- Response rate by batch. No responses from an entire batch = wrong audience.
- Response quality. "Not selling" = right companies, wrong timing. "Wrong person" = contact criteria need tightening.

**Sprint check-in (every 2 weeks):**
Pull all the above metrics and explicitly evaluate:
- Should we tighten, loosen, or shift the ICP criteria?
- Are Apollo search parameters matching what Kay actually approves?
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
Read every row on the Active tab. For each row, check cols I-N (Owner Name, Title, Email, Phone, LinkedIn Owner, LinkedIn Company):

```bash
gog sheets get {SHEET_ID} "Active!B:N" -a kay.s@greenwichandbarrow.com -p
```

**Flag every row missing ANY of these:**
- Col C (Website) — empty (mandatory for all targets, no exceptions)
- Col I (Owner Name) — empty or "Unknown"
- Col F (Employees) — empty or unsourced estimate
- ALL of Col K (Email), Col L (Phone), AND Col M (LinkedIn Owner) empty — must have at least one contact method

**If missing contacts found:**
1. Spawn a sub-agent to enrich (company website, LinkedIn People tab, web search, state registrations)
2. Update the sheet with whatever is found
3. Re-check after enrichment
4. Any STILL missing after enrichment → flag in the daily briefing: "{n} targets missing contact info."

**A target cannot be handed to outreach-manager without at minimum: Owner Name + (Email OR Phone OR LinkedIn Owner).** LinkedIn DM is a valid outreach channel.

### Step 2: Attio Dedup Validation
- Confirm Attio was checked (read-only) for existing entries before handoff
- Confirm no Attio records were CREATED by target-discovery (Attio writes happen in outreach-manager only)

### Step 3: Handoff Validation
- Confirm target data was passed to outreach-manager with all required fields
- Confirm every target has at least one contact method (Email OR Phone OR LinkedIn Owner)
- Flag targets with LinkedIn-only contact (no email/phone) — outreach-manager routes these to LinkedIn DM instead of email sequence

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
