---
schema_version: "1.0.0"
date: 2026-04-08
type: context
title: "Deal Evaluation Skill Audit"
tags:
  - date/2026-04-08
  - context
  - topic/deal-evaluation
  - topic/system-audit
  - source/claude
---

# Deal Evaluation Skill Audit (April 8, 2026)

Pressure test of `.claude/skills/deal-evaluation/SKILL.md` to ensure the system can handle a real CIM-to-recommendation in under 4 hours.

## 1. Template Status (All 7)

| # | Template | Drive ID | Status | Name | Size | Last Modified |
|---|----------|----------|--------|------|------|---------------|
| 1 | Buy-Box Screen | `1MEIkGgyhoF2P3Iwt3U3-8fCGTpDIwF5trTI3mCuk-xw` | PASS | G&B Buy-Box Screen Template | 16,952 bytes | 2026-04-07 |
| 2 | NDA Template | `1bdK5h6hY8RP49_etMQGUCNurR1L7sG3rb5NKCruHUyE` | PASS | G&B LLC NDA Template | 20,410 bytes | 2026-04-07 |
| 3 | LOI Template | `1d6ooLHHOvPHCamz37RhcVyD7zXWfcNHvNpBtYF4GQ-E` | PASS | G&B LOI Template | 21,843 bytes | 2026-03-20 |
| 4 | Financial Model | `1d6hhIf6sCRWMNf3gj30g23rYQAQbig2m` | PASS | G&B Financial Model Template.xlsx | 60,796 bytes | 2026-04-07 |
| 5 | Company Scorecard | `1kCCbEBpAgwX2TMn095W8-EzUUqvXIpWO` | PASS | G&B Industry & Company Scorecard Template.xlsx | 19,768 bytes | 2026-03-20 |
| 6 | Thumbs Up/Down | `1JV_B2IzUYYf66o-oDPTtNv-IHWc3nBQb5TQzthSovbg` | ISSUE | G&B Thumbs Up Down Template | 58,139 bytes | 2026-03-19 |
| 7 | Email Templates | `1_04RPBCKs4HsSBn2FzUIU4gt3acidB0d` | PASS | G&B Email Templates.docx | 40,557 bytes | 2026-03-19 |

**Template 6 Issue (Thumbs Up/Down):** Template has 2 slides with some `{{placeholders}}` (`BUSINESS_DESCRIPTION_1-5`, `LIKE_1-4`, `VALIDATE_1-3`, `FINANCIAL_MODEL_LINK`) but is MISSING the majority of placeholders that SKILL.md references. The COMPANY SNAPSHOT section on Slide 1 (company name, website, HQ, sector, industry, founded, employees, source, stage, valuation) has no `{{placeholder}}` text -- it appears to use tables or shapes with static labels but no replaceable tokens. The DEAL OVERVIEW section similarly lacks `{{placeholders}}` for financials/customers/sellers/keyman/growth/industry notes and metrics. The `create-from-template` command will only replace `{{KEY}}` patterns it finds in the presentation text.

**Result:** The `gog slides create-from-template --replacements` call will silently ignore ~20 of the ~30 replacement keys in the SKILL.md spec because those placeholders don't exist in the template. The Thumbs Up/Down would come out half-empty.

## 2. Folder Status

| Folder | ID | Status | Name |
|--------|-----|--------|------|
| ACTIVE DEALS parent | `18EWix44hnWOkq_pLqdxuWir39RY4K8v5` | PASS | ACTIVE DEALS (under ANALYST) |
| DEALS IN REVIEW parent | `1j8vx4DuJeOCBO7dh4lGzIWi2k2T868iv` | PASS | DEALS IN REVIEW (under MANAGER DOCUMENTS) |
| ABC COMPANY template | `1Ao4pF-DbwOo_ZADcD4EvVvJuogvEK0NI` | PASS | ACTIVE DEALS - FOLDER TEMPLATE |
| Template subfolders | (7 folders) | PASS | OUTREACH, CALLS, DILIGENCE, MODELS, FINANCIALS, CIM, NOTES |

**Folder hierarchy confirmed:**
- Shared Drive root > ANALYST (`1kUz7hJ3we-xTyabmytDH1u2egacbx5FL`) > ACTIVE DEALS > {COMPANY} > DEAL {YEAR} > 7 subfolders
- Shared Drive root > MANAGER DOCUMENTS (`1Amo_JGxtbHy-fmSVTzbyc3WRQJAWtrOM`) > DEALS IN REVIEW > {COMPANY}

**Note on Scorecard location:** The Company Scorecard template lives in `DRAFTS` subfolder (`14KX1aGhsOnUZaVhm1xGkt08ksgIhCwv7`) under MASTER TEMPLATES, while all other templates are directly in MASTER TEMPLATES (`19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx`). Not a functional issue (copy by ID works regardless) but worth noting for organization.

**Folder copy limitation:** `gog drive copy` only copies individual files, NOT folders. Phase 1 Sub-Agent 1 must create the full folder hierarchy with 9 sequential `gog drive mkdir` calls (company folder, deal year folder, 7 subfolders), not a single folder copy. The template folder is a reference for structure, not a copyable artifact.

## 3. Attio Active Deals Pipeline Status

**Pipeline:** Active Deals -- Owners (list ID: `0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b`)
**Parent object:** Companies
**API Slug:** `active_deals_owners`

**Stages (10 total, all confirmed via API):**

| # | Stage | Status ID | Maps to Skill Phase |
|---|-------|-----------|-------------------|
| 1 | Identified | `4c74c706-...` | Phase 1 entry / Intermediary PASS |
| 2 | Contacted | `5c9abae9-...` | Post-outreach |
| 3 | First Conversation | `f6f7ea43-...` | Phase 1 trigger (post-call) |
| 4 | Second Conversation | `476741ab-...` | Deepening relationship |
| 5 | NDA Executed | `1728a00f-...` | Phase 1 complete |
| 6 | Financials Received | `4b9d02f9-...` | Phase 3 trigger |
| 7 | Active Diligence | `33dfbdab-...` | Phase 3-4 (evaluation in progress) |
| 8 | LOI / Offer Submitted | `11a10867-...` | Phase 5A |
| 9 | LOI Signed | `4f94cb22-...` | Handoff to post-loi skill |
| 10 | Closed / Not Proceeding | `c855fed6-...` | Phase 5B |

**Pipeline health:** All existing entries (50+) are at "Closed / Not Proceeding" stage. No active deals currently in pipeline. Stages are well-defined and map cleanly to skill phases.

**ISSUE: SKILL.md stage name mismatch.** The Intermediary Inbound Pathway (Step 2A, line 150) references creating an entry at "Identified" -- which exists and is correct. However, the skill never explicitly maps which stage to set at each phase transition. The skill should have a stage-transition table so subagents know exactly which Attio stage to set at each phase boundary.

**Slack webhook:** `SLACK_WEBHOOK_ACTIVE_DEALS` is configured in `scripts/.env.launchd` and referenced in the skill. Verified present.

## 4. Dry Run: CIM Arrives (API Call Sequence)

### Intermediary Inbound Pathway (most likely first-deal scenario)

**Hour 0: CIM arrives via email**

1. `email-intelligence` (scheduled 7am) detects CIM attachment from broker email
2. Auto-triggers `deal-evaluation` with `source: intermediary-inbound`

**Step 1: Buy-Box Screen (15 min)**
```
API calls:
1. gog drive copy "1MEIkGgyhoF2P3Iwt3U3-8fCGTpDIwF5trTI3mCuk-xw" "Buy-Box Screen - {Company} {M.DD.YY}" --parent "{NOTES_FOLDER_ID}"
   PROBLEM: NOTES folder doesn't exist yet -- need to create deal folder first, but buy-box screen is supposed to be FAST (before full folder setup)
2. gog docs edit "{new_doc_id}" "[PLACEHOLDER]" "actual value"  -- multiple calls
3. curl Slack webhook (1 call)
```
**BOTTLENECK: Chicken-and-egg.** The buy-box screen doc goes in `ANALYST / ACTIVE DEALS / {COMPANY} / NOTES /` but the deal folder hasn't been created yet (that's Phase 1). The skill needs to either: (a) create a minimal folder structure before the buy-box screen, or (b) save the buy-box screen to a temp location and move it later.

**Step 2: If PASS, proceed to Phase 1**

**Phase 1: Folder Setup + Email Draft (20 min)**
```
Sub-Agent 1 (Folder Setup):
1. gog drive mkdir "{COMPANY NAME}" --parent "18EWix44hnWOkq_pLqdxuWir39RY4K8v5"  -- shared folder
2. gog drive mkdir "DEAL 2026" --parent "{company_folder_id}"
3-9. gog drive mkdir "{SUBFOLDER}" --parent "{deal_year_id}"  -- x7 subfolders
10. gog drive mkdir "{COMPANY NAME}" --parent "1j8vx4DuJeOCBO7dh4lGzIWi2k2T868iv"  -- private folder
11. gog drive copy "1bdK5h6hY8RP49_etMQGUCNurR1L7sG3rb5NKCruHUyE" "Greenwich & Barrow LLC NDA - {Company}" --parent "{deal_folder_id}"
12. gog docs edit "{nda_id}" "[COMPANY LEGAL NAME]" "{actual_name}"
13. gog docs edit "{nda_id}" "[DATE]" "{today}"
14. gog drive download "{nda_id}" --format=pdf --out="/tmp/nda.pdf"
    PROBLEM: gog drive download exports to local filesystem, not back to Drive. Need to upload the PDF back.
15. gog drive upload "/tmp/nda.pdf" --parent "{deal_folder_id}"

Sub-Agent 2 (Email Draft):  -- parallel with Sub-Agent 1
1. Read call notes / CIM content
2. Draft email using Template #9
3. Create draft via superhuman-draft.sh
```
**BOTTLENECK: PDF export-and-re-upload.** The skill says "Export as PDF (via gog drive export)" but `gog drive export` doesn't exist. The actual command is `gog drive download --format=pdf` which downloads locally. Then needs `gog drive upload` back to Drive. Two-step process, not one.

**Phase 3: Financial Evaluation (1-2 hours)**
```
Sub-Agent 3a (Data Extractor): -- parallel with 3b
1. gog drive download "{financials_file_id}" --out="/tmp/financials.xlsx"
2. Python/openpyxl parsing locally
3. Output: JSON with clean financial data

Sub-Agent 3b (Company Research): -- parallel with 3a
1. Web search (multiple queries)
2. LinkedIn research
3. Glassdoor/Indeed
4. Save research brief to Drive: gog drive upload or gog docs create

Sub-Agent 3c (Model Builder): -- after 3a
1. gog drive copy "1d6hhIf6sCRWMNf3gj30g23rYQAQbig2m" "G&B Financial Model - {Company}.xlsx" --parent "{private_folder_id}"
   PROBLEM: Financial Model is an .xlsx file on Drive. gog drive copy works for files.
   But populating specific cells (C37-E37, C40-E40, N17, N18) in a copied .xlsx on Drive
   requires downloading, editing locally with openpyxl, re-uploading. Can't edit cells in
   a Drive-hosted .xlsx directly via gog.
2. gog drive download "{model_copy_id}" --out="/tmp/model.xlsx"
3. openpyxl: open, write cells, save
4. gog drive upload "/tmp/model.xlsx" --parent "{private_folder_id}"
   PROBLEM: This creates a NEW file, doesn't update the existing one. Would need to
   delete the old copy first, or use a different approach.
```
**BOTTLENECK: Excel file editing round-trip.** Every .xlsx edit requires download-edit-upload, which creates duplicate files unless the old one is deleted. The Financial Model and Scorecard both have this issue.

**Phase 4: Scorecard + Thumbs Up/Down (30 min)**
```
Sub-Agent 4a (Scorecard): -- parallel with 4b
1. Same download-edit-upload pattern as 3c for .xlsx scorecard
   (gog drive copy, download, openpyxl, upload)

Sub-Agent 4b (Thumbs Up/Down):
1. Write replacements JSON to /tmp
2. gog slides create-from-template "1JV_B2IzUYYf66o-oDPTtNv-IHWc3nBQb5TQzthSovbg" "{Company} - Thumbs Up Down" --replacements /tmp/replacements.json --parent "{deal_folder_id}"
   PROBLEM: Only ~10 of ~30 placeholders will actually get replaced (see Template 6 issue above)
3. Slack notification with all links
```

**Phase 5A (if Go): LOI Generation (30 min)**
```
1. gog drive download "{model_id}" to read Kay's assumptions
2. gog drive copy LOI template
3. Multiple gog docs edit calls for each placeholder (~15 replacements)
4. Present to Kay
```

### Total API calls for full pipeline: ~40-50 gog commands + Attio updates + Slack webhooks

## 5. Identified Risks and Gaps

### CRITICAL (Would break on first real deal)

| # | Risk | Impact | Fix | Time to Fix |
|---|------|--------|-----|-------------|
| 1 | **Thumbs Up/Down template missing ~20 placeholders** | Slide 1 company snapshot and deal overview sections would be empty after `create-from-template`. Deck would look unprofessional. | Add all `{{PLACEHOLDER}}` text to the Google Slides template in the correct text boxes | 1 hour |
| 2 | **Buy-box screen folder dependency** | Buy-box screen doc needs to go in NOTES subfolder, but folder doesn't exist yet during fast intermediary screen | Add a "quick folder setup" step before buy-box screen: create company folder + NOTES subfolder only, then full structure in Phase 1 | 30 min (skill edit) |
| 3 | **No Apps Script for G&B branding** | Copied Google Docs won't have G&B formatting (logo, Avenir font, confidential footer). NDA and LOI copies inherit template formatting, but Buy-Box Screen copies may not if template wasn't pre-formatted | Either: (a) pre-format all templates manually once, or (b) build the Apps Script. Option (a) is faster. | (a) 30 min per template, (b) 2-3 hours |
| 4 | **Excel round-trip creates duplicates** | Financial Model and Scorecard edits via download-openpyxl-upload create new files, leaving the original empty copy orphaned | Use `gog drive delete` on the empty copy after re-upload, or use Drive API update endpoint if available | 15 min (add cleanup step to skill) |

### MODERATE (Would degrade quality but not block)

| # | Risk | Impact | Fix | Time to Fix |
|---|------|--------|-----|-------------|
| 5 | **No PDF export command** | SKILL.md references `gog drive export` which doesn't exist. Actual command is `gog drive download --format=pdf`. Subagent would fail on first try. | Update SKILL.md to use correct command | 5 min |
| 6 | **Skill doesn't specify Attio stage transitions** | Subagents won't know which stage to set at each phase boundary. Currently just says "update Attio" without specifying the exact stage title to use | Add stage transition table to SKILL.md | 15 min |
| 7 | **No folder copy in gog** | SKILL.md implies copying the template folder. Actual implementation requires 9 sequential `gog drive mkdir` calls | Already implicit in the skill but should be made explicit | 10 min |
| 8 | **Email Templates is a .docx, not readable via gog** | Sub-Agent 2 needs to read Template #9 content, but .docx on Drive requires download and local parsing | Download .docx, parse with python-docx, or hardcode email templates in the skill | 30 min |

### LOW (Nice to have)

| # | Risk | Impact | Fix | Time to Fix |
|---|------|--------|-----|-------------|
| 9 | **Scorecard in DRAFTS subfolder** | Minor organizational inconsistency -- scorecard template is in DRAFTS under MASTER TEMPLATES while all others are directly in MASTER TEMPLATES | Move file in Drive | 2 min |
| 10 | **No openpyxl verification** | Skill assumes openpyxl is installed in the environment. If not, Phase 3c and 4a fail. | Test: `python3 -c "import openpyxl"` | 5 min to verify/install |
| 11 | **LOI template has art advisory language** | LOI template references "artistic standards" and "partner" structure, which is specific to art advisory deals. Generic deals would need different language. | Create a generic LOI variant or add conditional sections | 1 hour |

## 6. Recommended Fix Priority

**Before first deal (do now):**
1. Fix Thumbs Up/Down template -- add all `{{PLACEHOLDER}}` tokens to Slides (Critical #1)
2. Update SKILL.md: correct `gog drive export` to `gog drive download --format=pdf` (Moderate #5)
3. Update SKILL.md: add Attio stage transition table (Moderate #6)
4. Update SKILL.md: add explicit mkdir sequence for folder creation (Moderate #7)
5. Pre-format all Google Doc templates with G&B branding if not already done (Critical #3)
6. Add Excel round-trip cleanup logic (Critical #4)
7. Add buy-box screen quick-folder-setup step (Critical #2)

**Total estimated fix time: 3-4 hours**

**After first deal (learn and iterate):**
- Build Apps Script for G&B branding automation
- Create generic LOI variant (non-art-advisory)
- Hardcode email templates in skill to avoid .docx parsing
- Add openpyxl verification to skill prerequisites
