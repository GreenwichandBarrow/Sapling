# Target Discovery — Drive Locations

## LINKT TARGET LISTS folder
- **Folder ID:** 1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc
- **Path:** G&B Shared Drive > OPERATIONS > LINKT TARGET LISTS
- **URL:** https://drive.google.com/drive/folders/1WfbzezRkD7Kr0FOA76y99x5wV8lwRkVc

## Master Sheet (one per niche sprint)

**Naming:** "{Niche} - Target List"
**Created once** at niche sprint activation. All discovery runs append to the same sheet. Do NOT create new sheets per run.

### Tab 1: Active
Targets being outreached. Kay approved, cold calls in progress, draft-only emails queued for Kay review. New discovery results append here.

### Tab 2: Passed
Targets Kay passed on. Rows move here when Kay marks `Kay Decision` = "Pass". Pass reason preserved. Not deleted — may revisit if ICP shifts. This tab is the dataset for "why did we pass" analysis during ICP calibration.

## Header Layout (both tabs, same structure)

### Discovery Data (Codex populates)
Headers: `Source`, `Company`, `Website`, `Headquarters`, `Industry`, `Employees`, `Revenue`, `Ownership`, `Owner Name`, `Owner Title`, `Email`, `Phone`, `LinkedIn Owner`, `LinkedIn Company`.

### Kay's Review (Kay populates)
`Kay Decision` — dropdown: Approve, Pass, Maybe
`Kay Pass Reason` — dropdown: Wrong Size, PE-Backed, Wrong Industry, Wrong Geography, Already Contacted, Not a Fit, Other

### Agent Notes (Codex populates)
`Agent Notes` — research context, routing flags, niche-specific data

### Cold Calls (cold-call operator populates)
Current sheets may still use legacy `JJ:*` headers until schema cleanup. Resolve by header name at runtime.
`Cold Call Status` / legacy `JJ: Call Status` — dropdown: Not Called, Connected, Voicemail, Callback Requested, Not Interested, Wrong Number
`Cold Call Date` / legacy `JJ: Call Date`
`Cold Call Notes` / legacy `JJ: Call Notes` — freeform
`Cold Call Owner Sentiment` / legacy `JJ: Owner Sentiment` — dropdown: Interested, Neutral, Not Selling, Hostile

### ICP Calibration (Codex auto-calculates)
`ICP Match` — TRUE if Kay approved AND cold-call outcome was positive (Connected + Interested/Neutral)
`ICP Miss Reason` — auto-populated from Kay's pass reason or negative cold-call outcomes

## Row Lifecycle

1. **Codex** appends new target to **Active** tab using the discovery-data headers
2. **Kay** reviews → marks Approve, Pass, or Maybe in `Kay Decision`, reason in `Kay Pass Reason`, notes in `Agent Notes`
3. If Pass → **Codex** moves row to **Passed** tab (with all data preserved)
4. If Approve → row stays in Active, outreach-manager picks it up for Day 1 email
5. **Cold-call operator** fills in call headers as calls are made
6. **Codex** calculates `ICP Match` and `ICP Miss Reason` from Kay + cold-call data

## Column Ownership (who writes what)

| Owner | Headers | Description |
|-------|---------|-------------|
| **Codex** | Discovery-data headers | Source + all enrichment data |
| **Kay** | `Kay Decision`, `Kay Pass Reason` | Decision, reject reason |
| **Codex** | `Agent Notes` | Agent Notes (research context, routing flags) |
| **Cold-call operator** | Call status/date/notes/sentiment headers | Call status, date, notes, sentiment |
| **Codex** | `ICP Match`, `ICP Miss Reason` | ICP calibration (auto-calculated) |

**Rule:** Never write to another owner's headers.
- Codex writes: discovery-data headers, `Agent Notes`, `ICP Match`, `ICP Miss Reason`
- Kay writes: `Kay Decision`, `Kay Pass Reason` — ONLY Kay marks Approve/Pass
- Cold-call operator writes: call status/date/notes/sentiment headers

**Agent filtering:** When the agent identifies companies that are clearly disqualified (PE-backed, acquired, public, too large), it puts them directly on the Passed tab with the reason in `Agent Notes`. It does NOT fill `Kay Decision`. The Passed tab should show whether Kay passed or the agent filtered — blank `Kay Decision` = agent filtered, filled `Kay Decision` = Kay's decision.

## Dropdown Data Validation

Set on sheet creation:
- `Source`: Apollo, Association Directory, Conference List, Web Research, Intermediary Referral, Broker
- `Kay Decision`: Approve, Pass, Maybe
- `Kay Pass Reason`: Wrong Size, PE Backed, Wrong Industry, Wrong Geography, Already Contacted, Not a Fit, Other
- `Cold Call Status` / legacy `JJ: Call Status`: Not Called, Connected, Voicemail, Callback Requested, Not Interested, Wrong Number
- `Cold Call Owner Sentiment` / legacy `JJ: Owner Sentiment`: Interested, Neutral, Not Selling, Hostile

## ICP Calibration Metrics (every 2 weeks, from weekly-tracker)

Calculated from Active + Passed tabs combined:
- **Kay Accept Rate:** Approve / (Approve + Pass) — target: 70%+
- **Cold-call Connection Rate:** Connected / total called
- **Positive Sentiment Rate:** (Interested + Neutral) / Connected
- **ICP Accuracy:** ICP Match TRUE / total targets
- **Top Pass Reasons:** ranked frequency of Pass Reason values
- **Credit Efficiency:** credits spent / Kay-approved targets

Output: Google Doc in LINKT TARGET LISTS folder + vault file + Slack notification with key metrics.

## Archived Raw Exports (pre-sprint format)

Legacy Linkt exports (historical, pre-April 2026). Kept for reference:
- Specialty Insurance Compliance: 1fsHYA8ljX6rXT-HIb69ZelJZiW3h38C925ci3i8E3cg
- NYC Tri-State Private OpCo: 1_FB15QIRNb23ASPjv-0YsJprdYXufy1x0lo5UNiYg8Y
- NYC Tri-State Private Business: 12Ty5T1V6JqnTI744JvxiN5Bjp7Pwr_-KUJJjEDXnNjE
- NYC Area M&A Targets - Succession: 1D84V1Oiiwqhxug27BXUQ_TjMnLKVuygZhgq6un4fuFQ
- Tri-State M&A Targets: 1vde_LKe44IcDhdmWq96sfo8TnX53_EjQZfnC0hRkRf4
- NYC Radius - Private B2B Owner: 1jVF7aX06boU--D-xXV4YXjO4Ztt3nPwqAyMYuN2W9CA
- Linkt ICP Configurations: 1w88mO5Mgtt0a-1rb7488RcUIzE1scD-jgrdwL_gm9ck
