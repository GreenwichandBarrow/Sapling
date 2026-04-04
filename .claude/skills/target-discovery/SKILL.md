---
name: target-discovery
description: "Find acquisition targets via list-builder (Apollo) + web research. Runs on initial niche activation and when weekly review signals pipeline needs refilling. Auto-advances qualifying targets to outreach-manager."
user_invocable: true
context_budget:
  skill_md: 2000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Find targets. That's it.

This skill discovers acquisition targets via skill/list-builder (Apollo, primary) and supplemental free research. Targets that pass all buy box + ICP criteria auto-advance to outreach. Edge cases and warm intro paths surface in the morning briefing for Kay. Approved targets go to skill/outreach-manager for all outreach drafting.

**Trigger:** Niche status changes to Active-Outreach on the Industry Research Tracker. Target-discovery does a one-time initial load when a niche first enters Active-Outreach (fill the sheet with a solid batch). After that, the weekly tracker dashboard determines if more targets are needed based on pipeline throughput data. Do not run daily — run on initial activation and when the weekly review signals the pipeline needs refilling.

**Pipeline stages:** Under Review → Active-Outreach → Long Term → Tabled/Killed

**Inputs from other skills:**
- **skill/niche-intelligence** — activated niche with one-pager, scorecard, buy-box target validation, ICP criteria
- **skill/pipeline-manager** — existing Attio contacts in this niche, intermediary referrals, deals already in pipeline (to avoid duplicates)

**Outputs to other skills (routed by Outreach Channel — Col D on WEEKLY REVIEW):**
- `Salesforge Email` → Approved targets go to skill/outreach-manager for email sequences + Attio entry at "Identified"
- `JJ-Call-Only` → Approved targets go to skill/jj-operations call queue. No Salesforge. No email sequences. JJ cold calls only.
- `Other` → STOP. Ask Kay how to route.

**CRITICAL:** Always read Col D (Outreach Channel) from WEEKLY REVIEW before routing approved targets. If Col D is empty or unrecognized, STOP and ask Kay. Never assume a default.

Goal: Fill the pipeline with qualified targets on activation, then refill as needed based on weekly throughput data.
</objective>

<target_discovery>
## Target Discovery (On Activation + Weekly Refill)

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
- Target: discover enough candidates to fill the sheet with a solid initial batch (or refill batch when weekly review triggers a run)
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

**Apollo is the ONLY source for emails.** Web research provides owner names, titles, and LinkedIn URLs. It does NOT provide emails. Never scrape emails from company websites, directories, or web search results — those are unverified and frequently wrong (generic inboxes, old addresses, wrong people).

```
Apollo /people/match → {
  first_name, last_name, organization_name, domain
} → verified business email
```

**Domain-match validation (runs on ALL emails, including pre-existing):**
If a row already has an email from a prior data source (Linkt, manual entry, etc.), do NOT trust it. Validate that the email domain matches the company website domain. If email domain ≠ company domain → discard the email and run Apollo `/people/match` to get the correct one. If Apollo returns unavailable, mark email as empty (target becomes LinkedIn DM candidate).

Examples of domain mismatches to catch:
- Owner works at Company A, but email is `name@companyB.com` (previous employer)
- Email is a university address (`name@university.edu`) for a business owner
- Email belongs to a different person at a different company

#### Phase E: Warm Intro Check (STOP HOOK — runs BEFORE any sheet write)

**No target is written to the sheet until this check completes.** This is a HARD STOP.

Run warm-intro-finder for each target: search Attio People records for the owner name AND anyone at their company. Check vault entities, Gmail history, and network contacts.

| Result | Action |
|--------|--------|
| Warm intro path found | **DO NOT write to sheet.** Route to morning briefing: "{Name}, {Company} — warm intro via {connection}. Draft or Salesforge?" Kay decides. |
| No warm intro path | Proceed to Phase F (assemble row). |

**Why this exists:** Warm intros are higher-conversion than cold email. If Kay has a path to the owner through her network, burning that with a Salesforge sequence is worse than no outreach at all. The warm intro check MUST run before the target enters any automated pipeline.

#### Phase F: Assemble Complete Row
Only after Phases A-E complete, assemble the row with all columns populated. Then check the Write Gate.

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

**Template columns A-Q:**
- A-N: Source through LinkedIn (Company) — list building data
- O: Kay: Decision (Approve/Pass)
- P: Kay: Pass Reason
- Q: Agent Notes (MUST start with "RECOMMEND: Approve" or "RECOMMEND: Pass" + reasoning)

When Kay marks a row "Pass" in Col O, move it to the "Passed" tab with all data preserved.

**Phone number formatting:** Always:
1. Strip country code prefix (`+1` or `+1 `)
2. Reformat to `(XXX) XXX-XXXX`
3. Write with apostrophe prefix and `--input USER_ENTERED`

### Step 3: Auto-Advance & Triage

#### Auto-Advance Stop Hook (CRITICAL)

This checklist runs sequentially for EVERY target BEFORE Col O is set to "Approve". If any hard stop triggers, skip remaining checks and set Pass immediately.

**Hard Stops (block auto-advance, set Col O = "Pass"):**

1. **PE ownership check.** Search for PE/VC ownership signals: Apollo org data, web search `"{company name}" "portfolio company" OR "acquired by" OR "backed by"`. If PE ownership detected → Col O = "Pass", Col P = "PE-owned ({evidence})". STOP — skip remaining checks.
2. **Email verification check.** Read Apollo email status from Phase D enrichment. If status is guessed, unavailable, or bounced AND no LinkedIn Owner URL exists → Col O = "Pass", Col P = "Email not verified ({status})". STOP — skip remaining checks. (If email is unavailable but LinkedIn Owner exists, target is still valid as a LinkedIn DM target — do not pass.)
3. **Generic email check.** If the only email is a generic address (info@, office@, contact@, hello@, admin@, general@, gallery@, art@) → Col O = "Pass", Col P = "Email not verified (generic)". STOP — skip remaining checks. Generic emails are never used for outreach.
4. **Wrong domain email check.** If Apollo returned an email on a different domain than the company (e.g., university email, previous employer) → Col O = "Pass", Col P = "Email not verified (wrong domain)". STOP — skip remaining checks.
5. **Owner identification check.** Read Col I (Owner Name). If name is "Unknown", blank, or generic (e.g., "Info", "Admin", "Contact", "Office") → Col O = "Pass", Col P = "Owner not identified". STOP — skip remaining checks.

**Soft Filters (flag but do NOT block auto-advance):**

6. **California check.** If HQ state is California → add note in Col Q: "CAUTION: California-based". Do not block.
7. **Very small company check.** If employee count < 5 → add note in Col Q: "CAUTION: Very small ({count} employees)". Do not block.

**Warm Intro Check (routes differently, not a block — already ran in Phase E):**

8. **Warm intro check.** This was already executed in Phase E before the target reached the sheet. If Phase E flagged a warm intro path, the target was routed to the morning briefing and never reached this point. This check is a safety net: if a target somehow reached the sheet without Phase E running, re-run warm-intro-finder now. If warm intro found → do NOT auto-advance. Route to morning briefing: "{Name}, {Company} — warm intro via {connection}. Draft or Salesforge?"

**Edge Case Routing:**

9. **Multi-flag edge case.** If a target passes all hard stops but has 2+ soft filter flags from checks 6-7 → do NOT auto-advance. Route to morning briefing as edge case. Format: "{Name}, {Company} — multiple flags: {list flags}. Approve or Pass?"

Only targets that clear all hard stops, have 0-1 soft flags, and have no warm intro path proceed to auto-advance below.

---

After the stop hook, the agent scores each target against buy box criteria AND niche ICP criteria. Targets are triaged into three buckets:

**Auto-Approve (no Kay review needed):**
Targets that PASS all buy box + ICP criteria AND clear the stop hook above. Agent sets Col O = "Approve" and flows them straight to outreach-manager or jj-operations based on Outreach Channel (Col D). Col Q notes: "AUTO-APPROVED: meets all criteria." (plus any soft filter cautions appended).

**Warm Intro Path (surface in morning briefing):**
Targets where warm-intro-finder (checking Attio, vault, Gmail, network) finds a connection. Surface for Kay to decide: personal draft or Salesforge sequence.
Briefing format: "{Name}, {Company} — warm intro via {path}. Draft or Salesforge?"

**Edge Cases (surface in morning briefing):**
Targets with borderline size, geography (California soft filter), unclear ownership, possible PE backing, or 2+ soft filter flags. Surface for Kay to decide: approve to Salesforge/JJ or pass.
Briefing format: "{Name}, {Company} — {reason for review}. Draft or Salesforge?"

Kay no longer reviews every target. She spot-checks outputs. If she sees bad targets flowing through, she tightens the criteria (see ICP Calibration Loop).

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
- **Claude:** Run Apollo via list-builder, supplement with free research, enrich inline, auto-advance qualifying targets, surface edge cases and warm intros to Kay, dedup against Attio, hand off to outreach-manager
- **Kay:** Spot-check auto-approved targets, decide on edge cases and warm intro routing, tighten criteria if needed
- **Outreach Manager:** All outreach drafting (email, call list, follow-ups) — separate skill

### ICP Calibration Loop

The ICP is a living document. Track these signals to know if it needs adjustment:

**Auto-advance feedback loop:**
- If auto-advance is producing targets Kay would reject, tighten buy box or ICP criteria. The accept/reject rate now comes from Kay's spot-checks and response data, not manual Col O review.
- Track spot-check rejection rate. If Kay rejects 2+ auto-approved targets in a single review, pause auto-advance for that niche and tighten criteria before resuming.
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

### Step 0: Outreach Channel Gate (HARD STOP — runs FIRST before any routing)

Before routing ANY approved targets to outreach-manager or jj-operations, read Col D (Outreach Channel) from WEEKLY REVIEW for this niche:

```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!B4:K20" -a kay.s@greenwichandbarrow.com -j
```

**Match the niche name to the correct row, then read Col D.**

| Col D Value | Route To | Action |
|-------------|----------|--------|
| `Salesforge Email` | skill/outreach-manager | Email sequences via Salesforge |
| `JJ-Call-Only` | skill/jj-operations call queue | JJ cold calls only. NO Salesforge. NO email sequences. |
| `Other` | **STOP. Ask Kay.** | Notify Kay: "Outreach Channel is 'Other' for {niche}. How should targets be routed?" |
| Empty/missing | **STOP. Do not route.** | Notify Kay: "Outreach Channel (Col D) is empty for {niche}. Cannot route targets." |

**This is a HARD STOP.** If Col D is empty, missing, or "Other", target-discovery MUST NOT hand targets to any downstream skill. Discovery can continue (finding and enriching targets), but routing is blocked until Kay sets the channel. Log the block in the daily briefing.

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

### Per Run (initial activation or weekly refill)
- [ ] Sheet populated with new targets (solid batch on activation, refill batch on weekly trigger)
- [ ] Auto-approved targets deduped against Attio (read-only check) and handed to outreach-manager
- [ ] Edge cases and warm intro paths surfaced in morning briefing
- [ ] Kay notified via Slack with sheet link
- [ ] Credits consumed logged

### Weekly
- [ ] Weekly tracker reviewed for pipeline throughput — trigger refill if needed
- [ ] Auto-advance accept/reject rate tracked via Kay's spot-checks and response data
- [ ] Sprint progress reviewed
- [ ] If Kay flagged bad auto-approves, criteria tightened before next run
</success_criteria>
