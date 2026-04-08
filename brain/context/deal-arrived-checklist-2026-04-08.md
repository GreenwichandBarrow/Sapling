---
schema_version: "1.0.0"
date: 2026-04-08
type: context
title: "Deal Arrived - First 48 Hours Checklist"
tags:
  - date/2026-04-08
  - context
  - topic/deal-evaluation
  - topic/checklist
  - source/claude
---

# Deal Arrived: First 48 Hours Checklist

Practical runbook for when the first real deal arrives. Two pathways: Intermediary Inbound (CIM from broker) or Direct Owner (post-call).

---

## Pathway A: Intermediary Inbound (CIM from broker)

### Hour 0-1: CIM Arrives + Fast Screen

- [ ] **Detect CIM.** email-intelligence flags attachment from broker, or Kay forwards manually
- [ ] **Create minimal folder.** `gog drive mkdir "{COMPANY}" --parent "18EWix44hnWOkq_pLqdxuWir39RY4K8v5"` + `DEAL 2026` + `NOTES` subfolder (just enough to file the buy-box screen)
- [ ] **File CIM to Drive.** Download from email, upload to `{COMPANY}/DEAL 2026/CIM/`
- [ ] **Run buy-box screen.** Copy template (`1MEIkGgyhoF2P3Iwt3U3-8fCGTpDIwF5trTI3mCuk-xw`), populate with CIM data
- [ ] **Quick Screen metrics.** Assess: Margins (Strong/Moderate/Weak), Recurring Revenue (High/Moderate/Low), Industry Growth (Strong/Moderate/Weak)
- [ ] **Score against buy box.** Revenue $10-50M, EBITDA $2-5M, margins 15%+, 10+ years, <15% customer concentration, B2B, founder-owned, US-based
- [ ] **Determine verdict.** PASS / FLAG / FAIL / RELATIONSHIP / INSUFFICIENT
- [ ] **Slack notification.** Post to #strategy-active-deals with verdict, key numbers, reasoning, doc link
- [ ] **Present to Kay.** Include verdict, one-line summary, and question: "Proceed to Phase 1?"

### Hour 0-1 (PASS verdict): Respond to broker

- [ ] **Draft reply email.** Thank broker, express interest, request intro to owner. Use `superhuman-draft.sh`
- [ ] **Present draft to Kay.** She reviews and sends
- [ ] **Check NDA situation.** Did broker include their NDA/CA? If not, ask Kay: send G&B's or request broker's?
- [ ] **Create Attio entry.** Add company to Active Deals -- Owners pipeline at "Identified" stage
- [ ] **Create vault inbox item.** `brain/inbox/YYYY-MM-DD-intermediary-deal-{slug}.md`

### Hour 0-1 (FAIL verdict): Decline gracefully

- [ ] **Draft decline email.** Short, honest reason, invite future deal flow in G&B's sweet spot
- [ ] **Present draft to Kay.** She reviews and sends
- [ ] **Log in vault.** `brain/traces/YYYY-MM-DD-intermediary-decline-{slug}.md`
- [ ] **Tag broker in Attio.** Append `deal_types_sent`, `deals_passed`
- [ ] **Do NOT create Active Deals entry**

---

## Pathway B: Direct Owner (Post-Call)

### Hour 0-1: Post-Call Setup

- [ ] **Detect call.** Granola transcript or vault call note logged
- [ ] **Create deal folders (Sub-Agent 1, parallel with email draft):**
  - [ ] Shared: `ANALYST/ACTIVE DEALS/{COMPANY}/DEAL 2026/` with 7 subfolders (OUTREACH, CALLS, DILIGENCE, MODELS, FINANCIALS, CIM, NOTES)
  - [ ] Private: `MANAGER DOCUMENTS/DEALS IN REVIEW/{COMPANY}/`
  - [ ] Use `gog drive mkdir` x9 (not folder copy -- gog can't copy folders)
- [ ] **Copy and populate NDA (Sub-Agent 1):**
  - [ ] `gog drive copy "1bdK5h6hY8RP49_etMQGUCNurR1L7sG3rb5NKCruHUyE" "Greenwich & Barrow LLC NDA - {Company}" --parent "{deal_folder}"`
  - [ ] `gog docs edit` to replace `[COMPANY LEGAL NAME]` and `[DATE]`
  - [ ] `gog drive download "{nda_id}" --format=pdf --out="/tmp/nda.pdf"` (NOT `gog drive export`)
  - [ ] `gog drive upload "/tmp/nda.pdf" --parent "{deal_folder}"`
- [ ] **File call notes** to CALLS/ subfolder
- [ ] **Draft thank-you + NDA + financials request email (Sub-Agent 2, parallel):**
  - [ ] Read call notes for personalization
  - [ ] Use Email Template #9 (download .docx, extract template text)
  - [ ] Personalize: owner name, company, specific financial items for business type
  - [ ] Create draft via `superhuman-draft.sh`
  - [ ] Attach NDA PDF reference
- [ ] **Present to Kay:** Email draft + NDA PDF + folder confirmation
- [ ] **Create Attio entry** at "First Conversation" stage
- [ ] **Kay reviews, signs NDA in Adobe, sends email**

---

## Hour 1-4: Deep Evaluation (After Financials Arrive)

Financials arrive via email. Phase 2 auto-files them. Phase 3 auto-triggers.

### Phase 3: Financial Evaluation (3 parallel subagents)

- [ ] **3a: Data Extractor** (parallel with 3b)
  - [ ] Download financials from Drive
  - [ ] Extract clean data: revenue (3 years), EBITDA (3 years), margins, LTM, customer concentration
  - [ ] Handle mixed formats: Excel (read directly), PDF (Claude PDF reading), scanned (flag for manual review)
  - [ ] Output: structured JSON with data quality assessment
  - [ ] Honest about data quality -- `needs_manual_review` if numbers are unclear

- [ ] **3b: Company Researcher** (parallel with 3a)
  - [ ] Company website, LinkedIn, Glassdoor, news/press
  - [ ] Owner profile: age estimate, tenure, succession signals
  - [ ] Competitor landscape: 3+ competitors identified
  - [ ] Industry data: market size, growth rate, regulatory drivers
  - [ ] Output: research brief (max 1500 words) saved to NOTES/

- [ ] **3c: Model Builder** (after 3a completes)
  - [ ] Copy Financial Model template to DEALS IN REVIEW: `gog drive copy "1d6hhIf6sCRWMNf3gj30g23rYQAQbig2m" "G&B Financial Model - {Company}.xlsx" --parent "{private_folder}"`
  - [ ] Download copy, populate historical cells only (C37-E37 revenue, C40-E40 EBITDA, N17 LTM EBITDA, N18 LTM period) via openpyxl
  - [ ] Re-upload populated model, delete empty copy
  - [ ] DO NOT touch projections, assumptions, deal structure cells

- [ ] **Update Attio** to "Financials Received" stage

### Phase 4: Scorecard + Thumbs Up/Down (auto-triggers after Phase 3)

- [ ] **4a: Pre-Scorecard** (parallel with 4b)
  - [ ] Copy Scorecard template: `gog drive copy "1kCCbEBpAgwX2TMn095W8-EzUUqvXIpWO" ...`
  - [ ] Score 70% hard gate criteria from 3a (financials) + 3b (research)
  - [ ] Leave 30% discretionary blank: "Kay to assess: culture fit, growth story, personal conviction"
  - [ ] Save to shared MODELS/ subfolder

- [ ] **4b: Pre-Thumbs Up/Down** (parallel with 4a)
  - [ ] Write replacements JSON to /tmp with all available data
  - [ ] `gog slides create-from-template "1JV_B2IzUYYf66o-oDPTtNv-IHWc3nBQb5TQzthSovbg" "{Company} - Thumbs Up Down" --replacements /tmp/replacements.json --parent "{deal_folder}"`
  - [ ] NOTE: Only placeholders that exist in template will be replaced (see audit for gap list)
  - [ ] "What We Like" / "What We Need to Validate" / Recommendation: leave as "Kay to complete"

- [ ] **Slack notification** to #strategy-active-deals with all links (model, scorecard, deck, research)
- [ ] **Update Attio** to "Active Diligence" stage

---

## Hour 4-24: Kay Reviews + Decision

- [ ] **Kay reviews Financial Model** -- toggles assumptions, tests scenarios
- [ ] **Kay completes 30% discretionary** on Scorecard
- [ ] **Kay completes "What We Like / Validate"** on Thumbs Up/Down
- [ ] **Kay makes go/no-go decision**

### If GO (Phase 5A):

- [ ] **Generate LOI:**
  - [ ] Read Kay's model for final terms (N15 valuation, N17 LTM EBITDA, etc.)
  - [ ] Copy LOI template: `gog drive copy "1d6ooLHHOvPHCamz37RhcVyD7zXWfcNHvNpBtYF4GQ-E" "G&B LOI - {Company}" --parent "{deal_folder}"`
  - [ ] Populate all ~15 placeholders via `gog docs edit`
  - [ ] Flag sections needing Kay's review (DD items, partner language, real property)
  - [ ] NOTE: Current LOI template has art-advisory-specific language. If deal is not art advisory, flag for Kay.
- [ ] **Present LOI to Kay** with terms summary table
- [ ] **Update Attio** to "LOI / Offer Submitted"
- [ ] **Kay finalizes and sends LOI**
- [ ] **Handoff to post-loi skill** when LOI is signed (Attio stage: "LOI Signed")

### If NO-GO (Phase 5B):

- [ ] **Ask Kay:** Primary reason for passing? Anyone to introduce them to?
- [ ] **Draft decline email** (Template 10a standard, or 10b with warm handoff)
- [ ] **Present draft to Kay**
- [ ] **After Kay sends:**
  - [ ] Update Attio to "Closed / Not Proceeding"
  - [ ] Create vault trace: `brain/traces/{date}-deal-decline-{company}.md`
  - [ ] Log: company, reason, scorecard accuracy, lessons learned

---

## Hour 24-48: Decision Trace (Always)

- [ ] **Ask Kay:** "What was the deciding factor?" and "Anything the scorecard/model didn't capture?"
- [ ] **Create vault trace:** `brain/traces/{date}-deal-evaluation-{company}.md`
- [ ] **Capture:** outcome, deciding factor, scorecard accuracy, model assumptions that held/broke, process improvements
- [ ] **Feed into /calibrate** for system improvement

---

## Attio Stage Transition Map

| Event | Set Attio Stage To |
|-------|-------------------|
| Intermediary screen PASS | Identified |
| First owner email sent | Contacted |
| First call completed | First Conversation |
| Second call completed | Second Conversation |
| NDA signed | NDA Executed |
| Financials received | Financials Received |
| Phase 3-4 evaluation begins | Active Diligence |
| LOI sent to owner | LOI / Offer Submitted |
| LOI countersigned | LOI Signed |
| Deal declined or dead | Closed / Not Proceeding |

## Known Issues (See Audit for Full Details)

1. Thumbs Up/Down template missing most placeholders -- needs template update before first deal
2. `gog drive export` doesn't exist -- use `gog drive download --format=pdf`
3. Excel editing requires download-edit-upload round-trip with cleanup
4. No Apps Script for G&B branding yet -- templates must be pre-formatted
5. LOI template has art-advisory-specific language
