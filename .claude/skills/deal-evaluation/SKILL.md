---
name: deal-evaluation
description: "Deal evaluation pipeline — post-call follow-up, NDA generation, financials intake, financial modeling, company scorecard, Thumbs Up/Down deck, LOI generation, decline handling. Triggered after first owner call or when financials arrive."
user_invocable: true
---

<objective>
Manage the full deal evaluation lifecycle from first owner call through go/no-go decision.

This skill picks up where pipeline-manager leaves off. Pipeline-manager handles sourcing through first contact. This skill handles everything from post-call follow-up through LOI or decline.

**Core question:** Does this deal work for Kay's personal economics, and does it pass the company scorecard for the analyst and investors?
</objective>

<essential_principles>
## Two Folder Architecture (CRITICAL)

Every deal has TWO folders. Never mix them.

**Shared folder** — analyst can see:
```
ANALYST / ACTIVE DEALS / {COMPANY} / DEAL {YEAR} /
  OUTREACH/
  CALLS/
  DILIGENCE/
  MODELS/        ← analyst's models only
  FINANCIALS/    ← raw financials from owner
  CIM/
  NOTES/
```
- **Parent folder ID:** Find ACTIVE DEALS under ANALYST
- **Template folder ID:** `1Ao4pF-DbwOo_ZADcD4EvVvJuogvEK0NI` (ABC COMPANY template)

**Private folder** — Kay only:
```
MANAGER DOCUMENTS / DEALS IN REVIEW / {COMPANY} /
```
- **Parent folder ID:** `1j8vx4DuJeOCBO7dh4lGzIWi2k2T868iv`
- Contains: G&B Financial Model with Kay's personal terms, equity modeling, exit scenarios

## Templates (Native Google Docs in Master Templates)

| Template | Drive ID | Type |
|----------|----------|------|
| Buy-Box Screen | `1MEIkGgyhoF2P3Iwt3U3-8fCGTpDIwF5trTI3mCuk-xw` | Google Doc |
| NDA Template | `1bdK5h6hY8RP49_etMQGUCNurR1L7sG3rb5NKCruHUyE` | Google Doc |
| LOI Template | `1d6ooLHHOvPHCamz37RhcVyD7zXWfcNHvNpBtYF4GQ-E` | Google Doc |
| Financial Model | `1d6hhIf6sCRWMNf3gj30g23rYQAQbig2m` | Excel (.xlsx) |
| Company Scorecard | `1kCCbEBpAgwX2TMn095W8-EzUUqvXIpWO` | Excel (.xlsx) |
| Thumbs Up/Down | `1JV_B2IzUYYf66o-oDPTtNv-IHWc3nBQb5TQzthSovbg` | Google Slides |
| Email Templates | `1_04RPBCKs4HsSBn2FzUIU4gt3acidB0d` | Word (.docx) |

## Email Rules
- Always open with a warm nicety before substance
- Sign off "Very best, Kay" — signature is built in
- No em dashes — use periods, commas, line breaks
- Show person names, not just companies
</essential_principles>


<intermediary_inbound_pathway>
## Intermediary Inbound Pathway (Fast Buy-Box Screen)

**Trigger:** Pipeline-manager flags an inbound deal from an intermediary and Kay approves screening. Invoked with `source: intermediary-inbound` and `intermediary: {name}`.

**Key principle:** Intermediary deals get a FAST response. These people send deals to multiple buyers simultaneously. A same-day or next-morning reply keeps Kay top-of-mind. Every hour of delay is a competitive disadvantage.

### Step 1: Automated Buy-Box Screen

Run against available information from the CIM, teaser, or email body:

| Criterion | Target | Hard Fail? |
|-----------|--------|------------|
| Revenue | $10-50M (services) / $5-40M (SaaS) | Soft — size is situational |
| EBITDA | $2-5M | Soft — size is situational |
| Margins | 15%+ | Yes |
| Years in business | 10+ | Yes |
| Owner profile | Founder-owned, succession-relevant (age 55+, no successor, retirement planning) | Soft |
| Geography | US-based, prefer non-coastal for value | Soft |
| Customer concentration | <15% single customer | Yes |
| Industry fit | B2B, recurring/contractual revenue, compliance-driven, fragmented market | Soft |

**Size is situational:** A sub-scale business can still be a fit if it's a platform play in a fragmented niche (bolt-on acquisition strategy), has exceptional margins, or is in a thesis-aligned space with clear roll-up potential. The buy-box screen flags below-range size but does NOT auto-reject. The full evaluation continues.

**Scoring:**
- All hard-fail criteria met + 2+ soft criteria → **PASS** (proceed)
- Any hard-fail criterion missed → **FAIL** (decline)
- Hard-fail criteria met but size below range + strong thesis fit → **FLAG** (continue evaluation with size noted)
- Hard-fail criteria met but insufficient info on 2+ soft criteria → **INSUFFICIENT** (request more info)

### Buy-Box Screen Deliverable (ALL outcomes — PASS, FLAG, FAIL, INSUFFICIENT)

Regardless of the screening outcome, ALWAYS produce:

1. **Buy-Box Screen Google Doc** — Copy template (`1MEIkGgyhoF2P3Iwt3U3-8fCGTpDIwF5trTI3mCuk-xw`), populate with CIM data, save to `ANALYST / ACTIVE DEALS / {COMPANY} / NOTES /`. Name: "Buy-Box Screen - {Company Name} {M.DD.YY}"
2. **Slack ping to #active-deals** — Single message containing:
   - Verdict (PASS/FLAG/FAIL)
   - Key numbers (revenue, EBITDA, margins)
   - One-line reasoning
   - Links: CIM, Buy-Box Screen doc, Deal folder

**The Buy-Box Screen doc includes a QUICK SCREEN section with three pre-scorecard metrics:**

| Metric | What to assess | Rating |
|--------|---------------|--------|
| **Margins** | Gross margins and EBITDA margins from CIM financials | Strong (20%+ EBITDA) / Moderate (10-20%) / Weak (<10%) |
| **Recurring Revenue** | Revenue model: contractual, subscription, project-based, one-time | High (80%+ recurring/contractual) / Moderate (50-80%) / Low (<50%) |
| **Industry Growth** | Market CAGR and key demand drivers from CIM industry section + web research | Strong (8%+ CAGR) / Moderate (3-8%) / Weak (<3%) |

These three map directly to the IDEATION tab columns (E: Margins, F: Recurring Revenue) and inform whether the full company scorecard is worth running. Include them in the Buy-Box Screen doc.

**Stop Hook (must pass before Slack):**
- [ ] Buy-Box Screen doc exists in NOTES subfolder
- [ ] Doc is populated (not empty template)
- [ ] Financial summary table has data
- [ ] Quick Screen section (Margins, Recurring Revenue, Industry Growth) is populated
- [ ] Verdict line is present
- [ ] Slack message includes doc link + CIM link + deal folder link

### Step 2A: Screen PASSES

1. Log deal in vault: `brain/inbox/YYYY-MM-DD-intermediary-deal-{company-slug}.md`
2. Present to Kay: "Buy-box screen passed. Revenue ${X}M, EBITDA ${X}M, {X}% margins, {years} years. Proceed to Phase 1?"
3. On approval, proceed to **Phase 1 (Post-Call Follow-Up)** with these modifications:
   - **Skip NDA generation** — intermediary deals typically come with the intermediary's own NDA or CA already in place. If no NDA/CA was included, ask Kay whether to send G&B's NDA or request the intermediary's.
   - **Email draft targets the intermediary**, not the owner directly (unless the intermediary explicitly invited direct contact). Frame as: "Thank you for sending this over. We'd like to learn more. Can you arrange an introduction to the owner?"
   - **Source field** in all vault files and Attio: `Intermediary Referral — {intermediary name} ({firm})`
   - **Attio Active Deals entry** created at "Identified" with intermediary linked

### Step 2B: Screen FAILS

1. Draft polite decline email to the intermediary:
   - Keep it SHORT — intermediaries send dozens of deals and don't want lengthy explanations
   - Thank them for thinking of Kay
   - Give a brief, honest reason: "outside our size range", "industry doesn't align with our thesis", "customer concentration concern"
   - Explicitly invite future deal flow: "Please keep us in mind for B2B services businesses in the $10-50M revenue range with 15%+ margins"
   - Sign off "Very best, Kay"
2. Log in vault: `brain/traces/YYYY-MM-DD-intermediary-decline-{company-slug}.md`
   - Capture: company, intermediary, reason for passing, what buy-box criteria failed
3. Tag the intermediary's Attio record:
   - `deal_types_sent: [{industry/type}]` (append)
   - `deals_passed: [{company} — {reason}, {date}]` (append)
   - This builds a profile of what each intermediary sends, enabling future filtering
4. Update Attio: do NOT create an Active Deals entry for failed screens

### Step 2C: INSUFFICIENT Information

1. Draft reply to the intermediary requesting key data points:
   - Revenue (last 3 years or LTM)
   - EBITDA or seller's discretionary earnings
   - Years in business
   - Owner age and succession situation
   - Largest customer as % of revenue
   - Frame as: "This looks interesting. Before we dive deeper, could you share a few data points so we can confirm fit?"
2. Create a pending inbox item: `brain/inbox/YYYY-MM-DD-intermediary-pending-{slug}.md`
   - Tag: `source/intermediary-inbound`, `status/awaiting-info`
   - Set follow-up: if no response in 5 business days, draft a gentle nudge
3. When info arrives (detected in next Gmail scan): re-run buy-box screen automatically

### Differences from Direct Owner Deals

| Aspect | Direct Owner Deal | Intermediary Inbound |
|--------|------------------|---------------------|
| NDA | G&B sends their NDA | Use intermediary's NDA/CA (or ask) |
| First contact | Email owner directly | Email intermediary, request intro |
| Speed | Normal cadence | Same-day/next-morning response |
| Source tracking | Cold Outreach / Network | Intermediary Referral — {name} |
| JJ Day 3 call | Yes (if cold) | No (intermediary manages contact) |
| Decline handling | Standard decline email | Short decline + invite future flow |
| Information available | Usually minimal | Usually CIM/teaser with financials |
</intermediary_inbound_pathway>

<phases>
## Phase 1: Post-Call Follow-Up

**Trigger:** First owner call logged (vault call note or Granola transcript detected)

### Sub-Agent 1: Deal Folder Setup
**Task:** Create both deal folders and organize initial documents.
**Tools:** gog drive

**Steps:**
1. Create company folder in ACTIVE DEALS: `{COMPANY NAME} / DEAL {YEAR}` with all 7 subfolders (OUTREACH, CALLS, DILIGENCE, MODELS, FINANCIALS, CIM, NOTES)
2. Create company folder in DEALS IN REVIEW: `{COMPANY NAME}`
3. Copy NDA template → shared deal folder root
4. Rename: "Greenwich & Barrow LLC NDA - {Company Name}"
5. Populate via `gog docs edit`:
   - `[COMPANY LEGAL NAME]` → actual company legal name
   - `[DATE]` → today's date
6. Export as PDF (via `gog drive export`)
7. Save call notes to CALLS/ subfolder

**Returns:**
```json
{
  "shared_folder_id": "",
  "private_folder_id": "",
  "nda_doc_id": "",
  "nda_pdf_id": "",
  "subfolders": {"OUTREACH": "", "CALLS": "", "DILIGENCE": "", "MODELS": "", "FINANCIALS": "", "CIM": "", "NOTES": ""}
}
```

**Stop Hook:**
- [ ] Shared folder exists with all 7 subfolders
- [ ] Private folder exists in DEALS IN REVIEW
- [ ] NDA doc populated with correct company name and date
- [ ] NDA exported as PDF
- [ ] Call notes filed in CALLS/

### Sub-Agent 2: Email Draft
**Task:** Draft the thank-you + NDA + financials request email.
**Tools:** gog gmail (read call notes for context), email templates reference

**Steps:**
1. Read call notes / Granola transcript for personalization points
2. Draft email using Template #9 (NDA & Financials Request)
3. Personalize:
   - [Name] → owner's first name
   - [Company] → company name
   - [specific items] → adjust financials list based on business type (e.g., add equipment for manufacturing, capacity for services)
4. Attach NDA PDF
5. Present draft to Kay for review

**Returns:** Draft email text with personalization notes

**Stop Hook:**
- [ ] Email draft includes warm nicety opening
- [ ] Financials request list is present and tailored to business type
- [ ] NDA PDF is referenced for attachment
- [ ] Sign-off is "Very best, Kay"

### Phase 1 Deliverable
Present to Kay:
- Thank-you email draft (Kay reviews, tweaks, sends)
- NDA PDF (Kay signs in Adobe, attaches, sends)
- Confirmation of folder structure created

---

## Phase 2: Document Filing (Ongoing)

**Trigger:** New attachments detected from deal contacts in Gmail

This runs as a lightweight check — either invoked manually or detected by pipeline-manager during daily scan.

**Steps:**
1. Scan email thread with owner for new attachments (exclude image signatures like image001.png)
2. Classify each attachment:
   - NDA / legal docs → shared deal folder root
   - CIM / company profiles → CIM/
   - Financials (P&L, balance sheet, tax returns, xlsx) → FINANCIALS/
   - Other documents → NOTES/
3. Download and upload to appropriate subfolder
4. Update vault entity with received documents list

**Stop Hook:**
- [ ] All non-image attachments from owner are filed
- [ ] No documents left in email without a Drive copy

---

## Phase 3: Financial Evaluation

**Trigger:** Financials received from owner (detected in FINANCIALS/ folder or email)

### Sub-Agent 3: Financial Model Prep
**Task:** Extract historical data and populate the G&B Financial Model.
**Tools:** gog drive, gog sheets (or openpyxl for Excel)

**Steps:**
1. Read incoming financials (Excel, PDF, or email body)
2. Extract:
   - Revenue for 3+ years
   - EBITDA for 3+ years
   - LTM EBITDA
   - LTM period end date
3. Copy Financial Model template → DEALS IN REVIEW / {COMPANY}
4. Rename: "G&B Financial Model - {Company Name}.xlsx"
5. Populate historical data ONLY:
   - C37-E37: Revenue (3 years)
   - C40-E40: EBITDA (3 years)
   - N17: LTM EBITDA
   - N18: LTM Period
6. **Do NOT touch:** Transaction assumptions, projections, growth rates, deal structure — these are Kay's to play with

**Returns:**
```json
{
  "model_file_id": "",
  "revenue_history": [0, 0, 0],
  "ebitda_history": [0, 0, 0],
  "ltm_ebitda": 0,
  "margins": [0, 0, 0],
  "data_quality": "clean|partial|needs_manual_review"
}
```

**Stop Hook:**
- [ ] Financial model exists in DEALS IN REVIEW / {COMPANY}
- [ ] Historical revenue populated (at least 2 years)
- [ ] Historical EBITDA populated (at least 2 years)
- [ ] LTM EBITDA populated
- [ ] Model named correctly: "G&B Financial Model - {Company Name}.xlsx"
- [ ] No projection or assumption cells were modified

### Phase 3 Deliverable
Present to Kay:
- Link to Financial Model in DEALS IN REVIEW
- Quick summary: "{Company}: Revenue ${X}M, EBITDA ${X}M, {X}% margins, {trend}"
- Flag any data quality issues (missing years, inconsistencies)
- Kay plays with assumptions and decides if math works

---

## Phase 4: Scorecard & Thumbs Up/Down

**Trigger:** Kay confirms the math works in the financial model

### Sub-Agent 4: Company Scorecard
**Task:** Run the company scorecard against real financials and call notes.
**Tools:** gog drive, vault reads, Attio API

**Steps:**
1. Read the 10 scorecard criteria from the template
2. Score each criterion using:
   - Financial data from the model
   - Call notes from vault
   - Entity data from Attio
   - Any CIM or company profile received
3. Calculate total score (70% hard gates / 30% discretionary)
4. Save completed scorecard to shared folder: MODELS/

**Returns:**
```json
{
  "scorecard_file_id": "",
  "total_score": 0,
  "hard_gate_score": 0,
  "discretionary_score": 0,
  "flags": [],
  "recommendation": "proceed|caution|pass"
}
```

**Stop Hook:**
- [ ] Scorecard exists in shared folder MODELS/
- [ ] All 10 criteria scored
- [ ] Total score calculated

### Sub-Agent 5: Thumbs Up/Down Deck
**Task:** Create the deal evaluation presentation.
**Tools:** gog slides create-from-template, gog drive

**Steps:**
1. Gather all data:
   - Company info from vault entity / Attio
   - Financial data from the model
   - Call notes for qualitative assessment
   - Scorecard results
2. Create deck from template using `gog slides create-from-template`:
   ```bash
   gog slides create-from-template "{TEMPLATE_ID}" "{Company Name} - Thumbs Up Down" \
     --exact \
     --replacements /tmp/{company}_replacements.json \
     --parent "{SHARED_FOLDER_DEAL_YEAR_ID}"
   ```
3. Populate all fields:
   - Slide 1: Company snapshot, deal overview, business description, preliminary checklist
   - Slide 2: Historical financials table, link to financial model, "What We Like", "What We Need to Validate"
4. Save to shared deal folder root

**Replacements JSON structure:**
```json
{
  "{{COMPANY_NAME}}": "Actual Company Name",
  "{{WEBSITE}}": "https://...",
  "{{HEADQUARTERS}}": "City, State",
  "{{SECTOR}}": "Sector",
  "{{INDUSTRY}}": "Industry",
  "{{FOUNDED}}": "Year",
  "{{EMPLOYEES}}": "Count",
  "{{SOURCE}}": "Cold Outreach|Conference|Broker|Network",
  "{{STAGE}}": "Pre-LOI|LOI Submitted",
  "{{VALUATION}}": "$X.XM or TBD",
  "{{BUSINESS_DESCRIPTION_1}}": "...",
  "{{BUSINESS_DESCRIPTION_2}}": "...",
  "{{BUSINESS_DESCRIPTION_3}}": "...",
  "{{BUSINESS_DESCRIPTION_4}}": "...",
  "{{BUSINESS_DESCRIPTION_5}}": "...",
  "{{FINANCIALS_NOTES}}": "...",
  "{{FINANCIALS_METRICS}}": "...",
  "{{CUSTOMERS_NOTES}}": "...",
  "{{CUSTOMERS_METRICS}}": "...",
  "{{SELLERS_NOTES}}": "...",
  "{{SELLERS_METRICS}}": "...",
  "{{KEYMAN_NOTES}}": "...",
  "{{GROWTH_NOTES}}": "...",
  "{{INDUSTRY_NOTES}}": "...",
  "{{LIKE_1}}": "...",
  "{{LIKE_2}}": "...",
  "{{LIKE_3}}": "...",
  "{{LIKE_4}}": "...",
  "{{VALIDATE_1}}": "...",
  "{{VALIDATE_2}}": "...",
  "{{VALIDATE_3}}": "...",
  "{{TIMING}}": "LOI due: ...\nFormal DD start: ...\nClosing: ...",
  "{{FINANCIAL_MODEL_LINK}}": "https://docs.google.com/spreadsheets/d/..."
}
```

**Returns:**
```json
{
  "deck_id": "",
  "deck_url": "",
  "scorecard_summary": "",
  "recommendation": ""
}
```

**Stop Hook:**
- [ ] Deck exists in shared deal folder
- [ ] All company snapshot fields populated
- [ ] Financial table on slide 2 has data
- [ ] "What We Like" has at least 3 items
- [ ] "What We Need to Validate" has at least 2 items
- [ ] Link to financial model is present

### Phase 4 Deliverable
Notify via Slack (#strategy-active-deals):
```bash
curl -s -X POST "$SLACK_WEBHOOK_ACTIVE_DEALS" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Deal Evaluation Ready: {Company Name}\nScorecard: {score}/100 — {recommendation}\nDeck: {deck_url}\nModel: {model_url}\nScorecard: {scorecard_url}"
  }'
```

Kay and analyst review the deck, scorecard, and model together.

---

## Phase 5A: LOI (If Go)

**Trigger:** Kay decides to proceed

### Sub-Agent 6: LOI Generation
**Task:** Create the LOI from template with deal terms.
**Tools:** gog docs, gog drive

**Steps:**
1. Read Kay's financial model for terms:
   - Enterprise valuation (N15)
   - LTM EBITDA (N17)
   - Entry multiple (calculated)
   - Debt structure (C16-C18)
   - Equity rollover (N25)
2. Copy LOI template → shared deal folder
3. Rename: "G&B LOI - {Company Name}.doc"
4. Populate via `gog docs edit`:
   - `[COMPANY LEGAL NAME]` → company legal name
   - `[OWNER NAME]` → owner name(s)
   - `[DATE]` → today's date
   - `[ENTERPRISE VALUATION]` → from model
   - `[RUN-RATE REVENUE]` → from model
   - `[RUN-RATE EBITDA]` → from model
   - `[DEFERRED PURCHASE PRICE]` → from model
   - `[DEFERRED PURCHASE PRICE WRITTEN]` → written form
   - `[ESCROW AMOUNT]` → typically 10% of TEV
   - `[MAX ROLLOVER %]` → from model
   - `[MIN ROLLOVER %]` → from model
   - `[NON-COMPETE YEARS]` → typically 5
   - `[EXCLUSIVITY DAYS]` → typically 90
   - `[NUMBER]` → number of partners/owners
   - `[PROPERTY ADDRESS]` → if applicable, otherwise remove section
   - `[NDA DATE]` → date NDA was signed
5. Flag sections needing Kay's custom input:
   - Due diligence items (customize per business)
   - Partner-specific language (adjust for single owner vs. multi-partner)
   - Real property section (include/remove based on deal)

**Returns:**
```json
{
  "loi_doc_id": "",
  "loi_url": "",
  "terms_summary": {
    "tev": "",
    "multiple": "",
    "debt": "",
    "equity": "",
    "rollover": ""
  },
  "flags": ["sections needing manual review"]
}
```

**Stop Hook:**
- [ ] LOI doc exists in shared deal folder
- [ ] All financial placeholders populated from model
- [ ] Company name and owner names correct
- [ ] Flagged sections for Kay's review clearly marked

### Phase 5A Deliverable
Present to Kay:
- Link to LOI document
- Terms summary table
- List of sections needing manual review
- Kay reviews, finalizes, sends

---

## Phase 5B: Decline (If No-Go)

**Trigger:** Kay decides to pass

### Sub-Agent 7: Decline & Close
**Task:** Draft decline email, update systems, capture learnings.
**Tools:** gog gmail, Attio API, vault writes

**Steps:**
1. Ask Kay: "What was the primary reason for passing?"
2. Ask Kay: "Is there someone we should introduce them to?" (warm handoff option)
3. Draft decline email:
   - If warm handoff → Template 10b (Decline with Warm Handoff)
   - If standard decline → Template 10a (Decline)
   - Personalize with specific compliments about the business and reasoning
4. Present draft to Kay for review
5. After Kay sends:
   - Update Attio: move to "Closed / Not Proceeding" stage
   - Create vault trace: `brain/traces/{date}-deal-decline-{company}.md`
   - Log: company, reason for passing, what scorecard missed/got right, lessons learned

**Returns:**
```json
{
  "decline_email_draft": "",
  "attio_updated": false,
  "trace_created": false,
  "warm_handoff": false
}
```

**Stop Hook:**
- [ ] Decline email draft presented to Kay
- [ ] After Kay confirms send: Attio stage updated
- [ ] Vault trace created with decline reasoning
- [ ] If warm handoff: introduction email also drafted

---

## Phase 6: Decision Trace (Always — Go or No-Go)

**Trigger:** After Phase 5A or 5B completes

**Steps:**
1. Ask Kay: "What was the deciding factor in this deal?"
2. Ask Kay: "Is there anything the scorecard or model didn't capture that mattered?"
3. Create vault trace: `brain/traces/{date}-deal-evaluation-{company}.md`

**Trace captures:**
- Deal outcome (proceed / pass)
- Deciding factor
- Scorecard accuracy (what it got right / missed)
- Model assumptions that held / broke
- Process improvements for next time
- Any calibration recommendations

This trace feeds into `/calibrate` for system improvement.

## Future: Cross-Deal Comparison (build when volume justifies)

**Trigger:** When 5+ deals have completed scorecards (Phase 4+).

**Purpose:** Maintain a cumulative deal ranking that compares all evaluated deals — active and killed — so Kay can see how a current deal stacks against prior deals at the same stage.

**Planned capabilities:**
- Running ranking of all scored deals (sortable by scorecard total, EBITDA, margins, thesis fit)
- "How does this deal compare?" overlay during Phase 4 — shows where current deal ranks vs all prior
- Pattern detection across killed deals: "Every deal you've passed on had X characteristic"
- Pattern detection across advanced deals: "Deals that reached LOI all had Y"
- Feeds into calibration: refine buy box criteria based on what actually converts

**Not needed yet.** Current deal volume (~1-2 active at a time) doesn't justify the build. When intermediary pipeline ramps and Kay is seeing 5-10 CIMs/week, this becomes critical. Inspired by peer feedback (AI in Search group call, 3/20/2026).
</phases>

<execution_flow>
## Invocation

This skill can be triggered in multiple ways:

1. **Manual:** `/deal-evaluation {company name}` — starts from wherever the deal currently is
2. **Intermediary inbound trigger:** Pipeline-manager flags inbound deal from intermediary, Kay approves screening → runs Intermediary Inbound Pathway (fast buy-box screen) before Phase 1
3. **Phase 1 trigger:** Pipeline-manager detects first owner call logged
4. **Phase 3 trigger:** Pipeline-manager detects financials received in email
5. **Phase 5 trigger:** Kay says "proceed" or "pass" on a deal

The skill detects the current state and picks up at the right phase:
- Intermediary inbound with `source: intermediary-inbound` → Intermediary Inbound Pathway (buy-box screen first)
- No deal folder exists → Phase 1
- Deal folder exists, no financials → Phase 2 (monitor)
- Financials in folder, no model → Phase 3
- Model exists, Kay confirmed → Phase 4
- Scorecard + deck done, Kay decided → Phase 5A or 5B

## Sub-Agent Summary

| Agent | Phase | Task | Parallel? |
|-------|-------|------|-----------|
| 1: Folder Setup | 1 | Create folders, populate NDA | Yes (with Agent 2) |
| 2: Email Draft | 1 | Draft thank-you email | Yes (with Agent 1) |
| 3: Model Prep | 3 | Extract financials, populate model | Solo |
| 4: Scorecard | 4 | Run company scorecard | Yes (with Agent 5) |
| 5: Deck Builder | 4 | Create Thumbs Up/Down deck | Yes (with Agent 4) |
| 6: LOI Generator | 5A | Populate LOI template | Solo |
| 7: Decline & Close | 5B | Draft decline, update systems, trace | Solo |
</execution_flow>

<success_criteria>
## Success Criteria

### Phase 1 Complete
- [ ] Shared deal folder with 7 subfolders exists
- [ ] Private deal folder exists in DEALS IN REVIEW
- [ ] NDA populated and exported as PDF
- [ ] Thank-you email draft presented to Kay
- [ ] Call notes filed

### Phase 3 Complete
- [ ] Financial model in DEALS IN REVIEW with historical data
- [ ] Summary presented to Kay
- [ ] No projection/assumption cells touched

### Phase 4 Complete
- [ ] Company scorecard completed in shared folder
- [ ] Thumbs Up/Down deck created in shared folder
- [ ] Slack notification sent to #strategy-active-deals with all links
- [ ] All deliverable links are valid and accessible

### Phase 5 Complete (either path)
- [ ] LOI populated and presented (if go) OR decline email drafted (if no-go)
- [ ] Attio updated to correct stage
- [ ] Vault trace created capturing decision reasoning
- [ ] If decline with handoff: introduction email also drafted

### Validation (run before any Slack notification)
```python
checks = {
    "shared_folder": folder_exists(shared_folder_id),
    "private_folder": folder_exists(private_folder_id),
    "deliverables_filed": all_docs_in_correct_subfolders(),
    "attio_current": attio_stage_matches_deal_state(),
    "vault_entity": entity_exists_and_linked(),
}

for check, passed in checks.items():
    if not passed:
        raise ValidationError(f"STOP: {check} failed. Fix before notifying.")
```
</success_criteria>
