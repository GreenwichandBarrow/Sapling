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

**Channel-aware enrichment (CRITICAL):** Read Col D (Outreach Channel) from WEEKLY REVIEW BEFORE invoking list-builder. The channel determines enrichment depth:
- `Kay Email` → invoke list-builder in `email-first` mode (full inline enrichment, all 9 stop hooks). Claude drafts in Superhuman, Kay reviews and sends.
- `DealsX Email` → Sam's team handles list building + enrichment + mass email/LinkedIn outreach. target-discovery runs warm intro check + Attio dedup on Sam's list only (see DealsX List Ingestion section).
- `JJ-Call-Only` → invoke list-builder in `calls-first` mode (volume load, 5 stop hooks, 0 credits)

**Pipeline stages:** Under Review → Active-Outreach → Long Term → Tabled/Killed

**Inputs from other skills:**
- **skill/niche-intelligence** — activated niche with one-pager, scorecard, buy-box target validation, ICP criteria
- **skill/pipeline-manager** — existing Attio contacts in this niche, intermediary referrals, deals already in pipeline (to avoid duplicates)

**Outputs to other skills (routed by Outreach Channel — Col D on WEEKLY REVIEW):**
- `Kay Email` → Approved targets go to skill/outreach-manager Kay Email subagent for Claude-drafted Superhuman emails + Attio entry at "Identified"
- `DealsX Email` → Approved targets (from Sam's list, after warm intro + Attio dedup) go to skill/outreach-manager DealsX Coordination subagent. Provide templates + exclusion list to Sam. Sam handles sending.
- `JJ-Call-Only` → Approved targets go to skill/jj-operations call queue. No email sequences. JJ cold calls only.
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
4. **Email verification** (Apollo people match, 1 credit — ONLY email source)
5. **Warm intro check** (HARD STOP — Attio, vault, Gmail network search)
6. **Write complete row** → only after all phases pass, warm intro cleared

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

**Not a gate** — some people genuinely don't have LinkedIn (common in fine art world). Mark Col Q as "No LinkedIn presence" and move on.

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
| Warm intro path found | **Write to "Do Not Call" tab** with all enriched data + Col S note: "WARM INTRO: {connection} — {path details}". Also surface in morning briefing: "{Name}, {Company} — warm intro via {connection}. Personal draft or cold outreach?" Kay decides. |
| No warm intro path | Proceed to Phase F (assemble row). |

**Why this exists:** Warm intros are higher-conversion than cold email. If Kay has a path to the owner through her network, burning that with a cold outreach cadence is worse than no outreach at all. The warm intro check MUST run before the target enters any automated pipeline.

#### Phase F: Assemble Complete Row
Only after Phases A-E complete, assemble the row with all columns populated. Then check the Write Gate.

**CRITICAL: Apollo People Search (`/mixed_people/search`) returns `None` for names and LinkedIn URLs without credit spend.** The "free" endpoint only confirms people exist at a company. Do NOT rely on it for owner names or LinkedIn profiles. Use web search (Phase B and C) instead.

### Art Storage Niche: Activity Report Cross-Reference (STOP HOOK)
When discovering targets for the art storage niche, cross-reference every candidate against the Activity Report (Google Sheet) which contains companies already contacted in prior outreach rounds. Do NOT rediscover or re-add companies that are already on the Activity Report.

### Write Gate (HARD RULE)
**No row hits the Full Target List tab until it meets ALL of these:**
- Col C (Website) — populated and verified (loads a real page, not a redirect to a parent company)
- Col K (Owner Name) — real person identified, not "Unknown"
- Col M (Email) OR Col N (Phone Company) OR Col O (Phone Owner) OR Col Q (LinkedIn Owner) — at least one contact method. LinkedIn DM is a valid outreach channel.
- Col Q (LinkedIn Owner) — populated with URL, or explicitly "No LinkedIn presence"
- Col R (LinkedIn Company) — populated with URL, or explicitly "No company page"
- Col F (Employees) — sourced number or LinkedIn range, never unsourced estimate

This applies to ALL sources. No exceptions. If enrichment can't meet this bar after reasonable effort, log the company name in the daily briefing as "could not enrich" with what's missing. Do NOT add it to the sheet with blank fields for Kay to catch.

### Sheet Structure

Append to the niche sprint's master sheet ("{Niche} - Target List") in TARGET LISTS folder. One master sheet per niche sprint — do NOT create new sheets per run. New results append to the "Full Target List" tab.

If the master sheet doesn't exist yet (first run of a new sprint), **COPY the template sheet**:

```bash
gog drive copy 1wIK4Jv56QIZejcmpq-gGrCWAPe07eJWUbKsWTRwh778 "{Niche} - Target List" -a kay.s@greenwichandbarrow.com --parent 1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc -j
```

Template: "G&B Target List Template" in MANAGER DOCUMENTS / G&B MASTER TEMPLATES (folder ID: 19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx)

**Template tabs:** Full Target List | Do Not Call | Niche Context | Associations | Call Log M.DD.YY

**Template columns A-W (23 columns):**
- A: Source, B: Company, C: Website, D: Headquarters, E: Industry, F: Employees
- G: Rev Source, H: Revenue, I: Year Founded, J: Ownership
- K: Owner Name, L: Owner Title, M: Email
- N: Phone (Company), O: Phone (Owner)
- P: LinkedIn Connection, Q: LinkedIn (Owner), R: LinkedIn (Company)
- S: Agent Notes (MUST start with "RECOMMEND: Approve" or "RECOMMEND: Pass" + reasoning)
- T: JJ: Call Status, U: JJ: Call Date, V: JJ: Call Notes, W: JJ: Owner Sentiment

Targets that fail screening are not written to the sheet. Warm intro targets go to the "Do Not Call" tab (and surface in morning briefing for Kay).

**Phone number formatting:** Always:
1. Strip country code prefix (`+1` or `+1 `)
2. Reformat to `(XXX) XXX-XXXX`
3. Write with `--input RAW` (NEVER use USER_ENTERED for phone numbers — Sheets interprets `+1` prefix as a formula, causing #ERROR!)

### Step 3: Auto-Advance & Triage

#### Auto-Advance Stop Hook (CRITICAL)

This checklist runs sequentially for EVERY target BEFORE it is written to the Full Target List tab. If any hard stop triggers, skip remaining checks and reject the target (do not write to sheet).

**Hard Stops (block auto-advance, set do not write to sheet):**

1. **PE ownership check.** Search for PE/VC ownership signals: Apollo org data, web search `"{company name}" "portfolio company" OR "acquired by" OR "backed by"`. If PE ownership detected → do not write to sheet, Col S (Agent Notes) = "PE-owned ({evidence})". STOP — skip remaining checks.
2. **Email verification check.** Read Apollo email status from Phase D enrichment. If status is guessed, unavailable, or bounced AND no LinkedIn Owner URL exists → do not write to sheet, Col S (Agent Notes) = "Email not verified ({status})". STOP — skip remaining checks. (If email is unavailable but LinkedIn Owner exists, target is still valid as a LinkedIn DM target — do not pass.)
3. **Generic email check.** If the only email is a generic address (info@, office@, contact@, hello@, admin@, general@, gallery@, art@) → do not write to sheet, Col S (Agent Notes) = "Email not verified (generic)". STOP — skip remaining checks. Generic emails are never used for outreach.
4. **Wrong domain email check.** If Apollo returned an email on a different domain than the company (e.g., university email, previous employer) → do not write to sheet, Col S (Agent Notes) = "Email not verified (wrong domain)". STOP — skip remaining checks.
5. **Owner identification check.** Read "Owner Name" column. If name is "Unknown", blank, or generic (e.g., "Info", "Admin", "Contact", "Office") → do not write to sheet, Col S (Agent Notes) = "Owner not identified". STOP — skip remaining checks.
6. **HQ country verification (CRITICAL).** Do NOT trust Apollo HQ data alone — Apollo often lists a US satellite office as HQ for international firms. Verify by checking the company LinkedIn page and/or website "About" page for actual headquarters location. If HQ is outside the US → do not write to sheet, Col S (Agent Notes) = "International HQ ({actual location})". STOP — skip remaining checks.
7. **Solo practitioner check.** Cross-reference Apollo employee count against LinkedIn company page and website team page. If the firm appears to be a solo practitioner or 1-2 person operation regardless of what Apollo says → do not write to sheet, Col S (Agent Notes) = "Solo practitioner ({evidence})". STOP — skip remaining checks. Apollo employee counts are frequently inflated for small firms.
8. **Business type verification.** Check the company website to confirm it is actually the type of business in the target niche (e.g., art advisory, not a design firm, gallery, auction house, or art moving company). If the business doesn't match the niche → do not write to sheet, Col S (Agent Notes) = "Not {niche} ({actual business type})". STOP — skip remaining checks.
9. **Company age check.** Check "Year Founded" (from Apollo or website). If the company is less than 5 years old → do not write to sheet, Col S (Agent Notes) = "Too young (founded {year})". STOP — skip remaining checks.

**Soft Filters (flag but do NOT block auto-advance):**

10. **California check.** If HQ state is California → add note in "Agent Notes": "CAUTION: California-based". Do not block.
11. **Very small company check.** If verified employee count is 5-9 → add note in "Agent Notes": "CAUTION: Small team ({count} employees)". Do not block. (Under 5 is caught by hard stop #7.)
12. **Young owner check.** Estimate owner age from LinkedIn (college graduation year + 22). If owner appears under 35 → add note in "Agent Notes": "CAUTION: Owner appears under 35 (est. ~{age})". Do not block, but flag for review. Owners in their 20s-early 30s are rarely thinking about succession.

**Warm Intro Check (routes differently, not a block — already ran in Phase E):**

13. **Warm intro check.** This was already executed in Phase E before the target reached the sheet. If Phase E flagged a warm intro path, the target was written to the "Do Not Call" tab and surfaced in the morning briefing. This check is a safety net: if a target somehow reached auto-advance without Phase E running, re-run warm-intro-finder now. If warm intro found → write to "Do Not Call" tab with Col S note: "WARM INTRO: {connection} — {path details}". Route to morning briefing: "{Name}, {Company} — warm intro via {connection}. Personal draft or cold outreach?"

**Edge Case Routing:**

14. **Multi-flag edge case.** If a target passes all hard stops but has 2+ soft filter flags from checks 10-12 → do NOT auto-advance. Route to morning briefing as edge case. Format: "{Name}, {Company} — multiple flags: {list flags}. Approve or Pass?"

Only targets that clear all hard stops, have 0-1 soft flags, and have no warm intro path proceed to auto-advance below.

---

After the stop hook, the agent scores each target against buy box criteria AND niche ICP criteria. Targets are triaged into three buckets:

**Auto-Approve (no Kay review needed):**
Targets that PASS all buy box + ICP criteria AND clear the stop hook above. Agent writes the target to the Full Target List tab and flows them to the appropriate channel based on Outreach Channel (Col D): Kay Email → outreach-manager Kay Email subagent, DealsX Email → outreach-manager DealsX Coordination subagent, JJ-Call-Only → jj-operations. Col S notes: "AUTO-APPROVED: meets all criteria." (plus any soft filter cautions appended).

**Warm Intro Path (write to Do Not Call tab + surface in morning briefing):**
Targets where warm-intro-finder (checking Attio, vault, Gmail, network) finds a connection. Write to "Do Not Call" tab with warm intro details in Col S. Surface for Kay to decide: personal draft or cold outreach cadence.
Briefing format: "{Name}, {Company} — warm intro via {path}. Personal draft or cold outreach?"

**Edge Cases (surface in morning briefing):**
Targets with borderline size, geography (California soft filter), unclear ownership, possible PE backing, or 2+ soft filter flags. Surface for Kay to decide: approve or pass.
Briefing format: "{Name}, {Company} — {reason for review}. Approve or Pass?"

Kay no longer reviews every target. She spot-checks outputs. If she sees bad targets flowing through, she tightens the criteria (see ICP Calibration Loop).

### Step 4: Attio Dedup Check (Read-Only)
Before handing off to outreach-manager:
- Check every approved target against Attio Active Deals. If the person/company already exists in the pipeline, flag them on the target sheet (Col S: "Already in Attio") and skip.
- If they're already receiving outreach from conference-discovery (pre-conference email in flight), exclude from cold outreach.
- **Do NOT create Attio records.** Target-discovery only writes to the Google Sheet. Outreach-manager creates Attio entries at "Identified" stage after auto-approval. This keeps the CRM clean — only approved targets enter the pipeline.

### Step 5: Handoff to Outreach Manager
Pass approved, deduped targets to skill/outreach-manager's cold outreach subagent with:
- Company name, website, headquarters
- Owner name, title, email, phone (company + owner), LinkedIn
- LinkedIn Owner URL (Col Q) — for LinkedIn DM drafting and connection degree lookup
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
- If auto-advance is producing targets Kay would reject, tighten buy box or ICP criteria. The accept/reject rate now comes from Kay's spot-checks and response data, not manual review.
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

<calls_first_flow>
## Calls-First Flow (JJ-Call-Only Niches)

When Col D = `JJ-Call-Only`, the entire discovery pipeline changes. Three phases replace the single inline enrichment:

### Phase 1: Volume Load (on activation + monthly refill)

Invoke list-builder in `calls-first` mode. Target: 500-1000 companies.

**Reduced stop hooks (5 of 9):**
1. PE ownership check — still critical
2. HQ country verification — still matters
3. Business type verification — confirm it's actually pest control (or whatever the niche is)
4. Company age check — skip if < 5 years old
5. Solo practitioner check — via Apollo employee count only (no cross-reference needed)

**Skipped stop hooks:**
- Email verification, generic email, wrong domain email — no email in Phase 1
- Owner identification check — no owner name in Phase 1

**Auto-advance:** Targets passing 5 reduced stop hooks are written directly to the "Full Target List" tab. Kay spot-checks.

### Phase 2: Sunday Night Pipeline (Sunday 11pm ET)

**This is a single sequential pipeline that runs every Sunday night. All steps must complete before jj-operations creates the week's Call Log tabs on Monday morning. The order is critical — SELECT this week's 200 first, THEN enrich those exact rows, THEN screen, THEN create tabs.**

**Design invariant:** the 200 rows enriched Sunday night MUST be the same 200 rows jj-operations prep writes to Mon–Fri Call Log tabs. Steps 1 and 4 read from the identical row set — no drift.

#### Step 1: Select This Week's Call Pool (row selection, 0 credits)
Pick the exact 200 targets that will populate Mon–Fri Call Log tabs. This is the **master row set** that Steps 2–5 operate on.

1. Read "Full Target List" tab, all rows
2. Filter to rows where Col T (JJ: Call Status) is empty (uncalled)
3. Sort by row number (ascending — oldest on list first)
4. Take top 200
5. Persist row numbers to a scratch artifact: `brain/context/jj-week-pool-{YYYY-MM-DD}.md` (source of truth for Steps 2–5)
6. Log: "Phase 2 Step 1: {n} rows selected (target 200)"

**If fewer than 200 uncalled rows remain:** flag in Monday briefing — list is running low, trigger target-discovery Phase 1 monthly refill.

#### Step 2: Owner Enrichment (Apollo primary → Linkt optional → web research fallback)
Enrich owner name + title + LinkedIn on every row in Step 1's pool where Col K (Owner Name) is blank. This is the ONLY enrichment step — Phase 1 intentionally loads companies without owners.

**Primary path: Apollo `/people/match` via list-builder skill:**
1. For each pool row with Col K blank: call Apollo `/people/match` by company domain (one owner-title match per company)
2. Write owner name (Col K), title (Col L), owner LinkedIn (Col Q), email (Col M) from Apollo response
3. Credit cost: 1 credit per match × up to 200 rows = ~200 credits/week
4. Log: "Phase 2 Step 2 (Apollo): {n}/{pool_size} matched, {credits} credits burned"

**Optional supplement: Linkt (while subscription active — currently through 2026-05-30):**
1. For Apollo un-matches, optionally run Linkt person-match as a second source
2. Linkt sometimes catches LinkedIn profiles Apollo misses (different enrichment provider backbones)
3. Skip entirely if Linkt credits are scarce or subscription is lapsed
4. Log: "Phase 2 Step 2 (Linkt supplement): {n}/{remaining} additional matches"

**Fallback path: free web research (for rows neither Apollo nor Linkt match):**
1. For still-un-matched rows: web research (company website, LinkedIn People tab, Google)
2. Write owner name (Col K), title (Col L), owner LinkedIn (Col Q) from research
3. Log: "Phase 2 Step 2 (Web): {n}/{remaining} owners identified via research"

**Subscription notes:** Apollo is the always-on canonical source (list-builder skill). Linkt is time-limited and optional. When Linkt subscription ends, remove the Linkt step without re-architecting — Apollo + web research is sufficient.

#### Step 3: PE Re-Screen (on newly enriched rows only)
Re-check pool rows enriched in Step 2 for PE/VC ownership. Owner research often surfaces acquisition info (e.g., "John Smith, former owner — company acquired by Rentokil 2022").

1. For each newly enriched row: search `"{company name}" "acquired by" OR "portfolio company" OR "backed by" OR "subsidiary"`
2. Also flag: franchise models, government entities, non-target business types
3. PE-owned → move to "Do Not Call" tab with Col S: "PE-OWNED: {evidence}". Remove from pool artifact; backfill pool from next-in-queue rows (go back to Step 1 logic for one replacement round).
4. Government/franchise → delete from Full Target List (not acquisition targets). Same backfill rule.
5. Log: "Phase 2 Step 3: {n} PE-owned removed, {n} govt/franchise removed, {n} backfilled"

#### Step 4: Warm Intro Check (on final pool)
Run warm-intro-finder on every row in the post-Step-3 pool (all have owner names by now).

1. For each row: check Attio, Gmail, vault entities for connections to owner or company
2. Warm intro found → move to "Do Not Call" tab with Col S: "WARM INTRO: {connection} — {path details}". Backfill pool same as Step 3.
3. Surface in Monday morning briefing: "{Name}, {Company} — warm intro via {connection}. Personal draft or cold outreach?"
4. Log: "Phase 2 Step 4: {n} warm intros found, {n} backfilled"

#### Step 5: Create Week's Call Log Tabs (hand off to jj-operations)
After Steps 1–4 complete, the pool is clean: exactly 200 rows, all enriched, PE-screened, warm-intro-cleared.

1. jj-operations prep reads the pool artifact from Step 1 (post-backfill final state)
2. Distributes 40/day across Mon–Fri tabs
3. Writes owner name, title, phone, LinkedIn into each tab's Col K–Q alongside the company data
4. Target: 100% Tier-1 coverage (no blank Col K rows on call tabs)

**Cost:** up to ~200 Linkt credits/week through 5/30; 0 credits after (web-research fallback).

### Phase 3: Post-Engagement Enrichment (triggered by jj-operations harvest)

When JJ connects with an owner and gets positive sentiment:
1. jj-operations harvest updates call outcome on sheet
2. If Call Status = "Connected" AND Sentiment = "Interested" or "Neutral":
   - Run Apollo `/people/match` for email reveal (1 credit)
   - Run warm-intro-finder (check if Kay has a connection for warmer follow-up)
   - Flag for pipeline-manager: "JJ connected with {owner} at {company}. Ready for follow-up."
3. If owner said "send me more info" → draft follow-up email in Superhuman

**Cost:** ~1 credit per positive engagement. At 5-10% connect rate, ~5-10 credits/week.

### Weekly Timeline

| Day | Time | What Happens |
|-----|------|-------------|
| Sunday | 11pm | Phase 2 Step 1: Select this week's 200-row pool (Col T empty, oldest first) |
| Sunday | 11pm | Phase 2 Step 2: Owner enrichment on the pool (Linkt primary → web research fallback) |
| Sunday | 11pm | Phase 2 Step 3: PE re-screen on newly enriched pool rows (backfill pool as needed) |
| Sunday | 11pm | Phase 2 Step 4: Warm intro check on final pool (backfill as needed) |
| Sunday | 11pm | Phase 2 Step 5: jj-operations prep creates 5 Call Log tabs from the cleaned pool |
| Monday | 10am | Slack to JJ: week's sheet link + call guide |
| Mon-Fri | 10am-2pm | JJ calls 40 targets/day |
| Mon-Fri | 4pm | jj-operations harvest: update Full Target List, trigger Phase 3 for positive calls |
| Friday | | Weekly tracker reports: calls made, connection rate, enrichment pipeline depth |

### Stop Hook: Call-Tab Enrichment Integrity

**This pipeline's contract is:** the 200 rows enriched Sunday night are the exact same 200 rows JJ calls Mon–Fri. If that invariant breaks, JJ's tabs show blank Col K (Owner Name) and his shift is wasted.

Before the Sunday pipeline emits "done", run this check:

1. Read the pool artifact from Step 1 (200 row numbers)
2. Read the post-Step-4 pool (should be 200 rows after backfills)
3. Read the 5 Call Log tabs created in Step 5
4. Assert: every row number in the final pool appears on exactly one Mon–Fri Call Log tab
5. Assert: every Mon–Fri Call Log tab row has Col K (Owner Name) populated
6. If ANY tab has a blank Col K row: block completion, log the row numbers, escalate to Monday morning briefing as **"ENRICHMENT INTEGRITY FAILURE"**

Enforced by `.claude/hooks/enrichment_integrity_check.py` (see implementation at that path).
</calls_first_flow>

<dealsx_list_ingestion>
## DealsX List Ingestion (DealsX Email Niches)

When Col D = `DealsX Email`, Sam Singh's team at DealsX handles list building, enrichment, and mass email + LinkedIn outreach. target-discovery does NOT run the full 6-phase pipeline. Instead, target-discovery's role is limited to two critical guard rails on Sam's list.

**Current DealsX niches:** Fractional CFO, Specialty Insurance Brokerage, Estate Management.

### What Sam Handles (Phases A-D equivalent)
- Company discovery (his own sources)
- Owner identification
- Email/LinkedIn enrichment
- Mass email + LinkedIn outreach sequences

### What target-discovery Handles (Phase E + Phase F only)

#### Phase E: Warm Intro Check (HARD STOP — same as Kay Email flow)
**This is the most critical step.** Sam must NOT cold-email anyone in Kay's network. Before Sam sends any batch:

1. Receive Sam's target list (CSV or shared sheet)
2. Run warm-intro-finder against EVERY name on the list: check Attio People records, vault entities, Gmail history, network contacts
3. Flag any warm intro matches: "{Name}, {Company} — warm intro via {connection}. EXCLUDE from DealsX batch." Write these to the "Do Not Call" tab on the niche's target sheet.
4. Return exclusion list to outreach-manager DealsX Coordination subagent, who communicates it to Sam

**Why this is non-negotiable:** If Sam cold-emails someone Kay has a personal relationship with, it damages the relationship and Kay's reputation. This check runs BEFORE Sam sends, not after.

#### Phase F: Attio Dedup + ICP Screening
1. **Attio dedup** — Check every target on Sam's list against Attio Active Deals. If the person/company already exists in the pipeline, exclude from Sam's batch.
2. **Conference overlap** — If a target is already receiving outreach from conference-discovery, exclude.
3. **ICP screening (simplified)** — Sam already pre-screens for basic fit, but run these hard stops as a safety net:
   - PE ownership check
   - HQ country verification
   - Business type verification (is it actually the right niche?)

**Output:** Return to outreach-manager DealsX Coordination subagent:
- Exclusion list (warm intros + Attio duplicates + conference overlap + ICP failures) with reasons
- Cleared list (targets safe for Sam to contact)

### Timing
- Sam sends his list before each batch
- target-discovery runs Phase E + F within 24 hours
- Cleared list returned to Sam via outreach-manager before he sends

### What target-discovery Does NOT Do for DealsX Niches
- No Apollo searches (Sam builds his own lists)
- No inline enrichment (Sam handles this)
- No sheet population (Sam manages his own tracking)
- No auto-advance logic (Sam decides send timing)
- No email drafting (Sam handles outreach copy)
</dealsx_list_ingestion>

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
| `Kay Email` | skill/outreach-manager Kay Email subagent | Claude drafts in Superhuman, Kay reviews and sends. Full inline enrichment pipeline (Phases A-F). |
| `DealsX Email` | skill/outreach-manager DealsX Coordination subagent | Sam's team handles list building + mass email/LinkedIn. target-discovery runs warm intro check + Attio dedup on Sam's list only (see DealsX List Ingestion). Provide templates + exclusion list to Sam. |
| `JJ-Call-Only` | skill/jj-operations call queue | JJ cold calls only. No email sequences. |
| `Other` | **STOP. Ask Kay.** | Notify Kay: "Outreach Channel is 'Other' for {niche}. How should targets be routed?" |
| Empty/missing | **STOP. Do not route.** | Notify Kay: "Outreach Channel (Col D) is empty for {niche}. Cannot route targets." |

**This is a HARD STOP.** If Col D is empty, missing, or "Other", target-discovery MUST NOT hand targets to any downstream skill. Discovery can continue (finding and enriching targets), but routing is blocked until Kay sets the channel. Log the block in the daily briefing.

### Step 1: Sheet Validation
- Confirm Google Sheet in TARGET LISTS folder has new rows with today's date
- Verify phone numbers are formatted correctly: `(XXX) XXX-XXXX`

### Step 1b: Contact Completeness Check (STOP HOOK)
Read every row on the Full Target List tab. For each row, check cols K-R (Owner Name, Title, Email, Phone, LinkedIn Owner, LinkedIn Company):

```bash
gog sheets get {SHEET_ID} "Full Target List!B:R" -a kay.s@greenwichandbarrow.com -p
```

**Flag every row missing ANY of these:**
- Col C (Website) — empty (mandatory for all targets, no exceptions)
- Col K (Owner Name) — empty or "Unknown"
- Col F (Employees) — empty or unsourced estimate
- ALL of Col M (Email), Col N (Phone Company), Col O (Phone Owner), AND Col Q (LinkedIn Owner) empty — must have at least one contact method

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
- Confirm target data was passed to the correct downstream skill based on Col D (Kay Email → outreach-manager Kay Email subagent, DealsX Email → outreach-manager DealsX Coordination subagent, JJ-Call-Only → jj-operations)
- Confirm every target has at least one contact method (Email OR Phone OR LinkedIn Owner)
- Flag targets with LinkedIn-only contact (no email/phone) — outreach-manager routes these to LinkedIn DM instead of email outreach

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
- [ ] Warm intro targets written to "Do Not Call" tab
- [ ] Kay notified via Slack with sheet link
- [ ] Credits consumed logged

### Weekly
- [ ] Weekly tracker reviewed for pipeline throughput — trigger refill if needed
- [ ] Auto-advance accept/reject rate tracked via Kay's spot-checks and response data
- [ ] Sprint progress reviewed
- [ ] If Kay flagged bad auto-approves, criteria tightened before next run
</success_criteria>
