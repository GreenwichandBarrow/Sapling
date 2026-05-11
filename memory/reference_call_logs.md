---
name: Call Logs folder and template
description: Per-company call log docs for JJ in OPERATIONS/CALL LOGS, template in Master Templates. Claude pre-populates, JJ fills in outcomes, Claude syncs to target sheet overnight.
type: reference
---

## Call Logs

**Folder:** OPERATIONS / CALL LOGS
- Folder ID: `1nGSQIa28fhQ9dXuKdMks_172gyxAinEs`

**Template:** G&B Call Log Template 3.19.26.docx
- Template ID: `1nvvdOU7I5NLAwxrYgHIFTRNrEZmc67X8`
- Location: G&B MASTER TEMPLATES

**Naming:** "Call Log - {Company Name} {M.DD.YY}.docx"

## Workflow
1. Claude creates 4-6 call log docs overnight from template
2. Pre-populates company info from Linkt data in target sheet
3. Customizes script with company-specific operational signal
4. Slack to JJ at 10am with links to each doc
5. JJ reads script, makes call, fills in Call Outcome + Call Notes
6. Claude reads docs overnight, syncs to target sheet columns R-U

## Doc → Sheet Mapping
| Call Log Field | Target Sheet Column |
|---|---|
| Call Status | R: JJ: Call Status |
| Call Date | S: JJ: Call Date |
| Call Notes (summarized) | T: JJ: Call Notes |
| Owner Sentiment | U: JJ: Owner Sentiment |
