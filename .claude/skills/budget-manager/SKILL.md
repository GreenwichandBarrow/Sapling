---
name: budget-manager
description: "Fund budget tracking, runway forecasting, tech stack audits, and bookkeeper transition. Ingests monthly P&L from bookkeeper, reconciles actuals vs approved budget, calculates runway, flags variances. Feeds investor-update with budget data."
user_invocable: true
---

<objective>
Manage the G&B search fund budget so Kay never has to manually track expenses or runway.

The fund has $551,825 invested with a February 2027 deadline. Every dollar and every month matters. This skill:
- Tracks what was actually spent vs what was budgeted
- Forecasts how many months of runway remain
- Flags when categories are over budget
- Inventories the tech stack and finds savings
- Manages the transition from bookkeeper to Kick + Claude

**4 modes:** `monthly`, `runway`, `tech-audit`, `transition`

Invoke: `/budget monthly`, `/budget runway`, `/budget tech-audit`, `/budget transition`

## Trigger Flow (Monthly Mode)

The monthly mode is trigger-based, NOT scheduled. The pipeline-manager detects Anthony's monthly reports during its morning email scan and triggers the flow:

```
Anthony emails P&L + BS PDFs
  → Pipeline-manager morning scan detects bookkeeper reports
  → Pipeline-manager saves PDFs to MONTHLY REPORTING/{MONTH YEAR} folder on Drive
  → Pipeline-manager creates brain/inbox item: "Monthly financials received"
  → Morning briefing surfaces under "Other items":
    "Monthly P&L received from Anthony. Run /budget monthly?"
  → Kay approves → budget-manager monthly mode runs
```

**Detection signal:** Email from StartVirtual or Anthony containing PDF attachments with "Profit and Loss" or "Balance Sheet" in the filename or subject.

**Why trigger-based:** Anthony's delivery schedule varies. A fixed schedule (e.g., first Friday) would run with no data if he's late. This ensures we only run when real data exists.

**Future state:** When confident, remove the approval step and auto-run on detection.
</objective>

<essential_principles>
## What Kay Cares About

1. **How much runway do I have?** The single most important number. Fund balance minus DD reserve, divided by steady-state burn rate.
2. **Am I on track vs the budget my investors approved?** Variance flags for any category >10% over YTD prorated budget.
3. **Where can I cut costs?** Tech stack overlap, unused subscriptions, bookkeeper replacement.
4. **Feed investor reporting.** Quarterly investor updates need one bullet: `$XXXK (XX% remaining of $550K raised) [context]`. Two data points only — dollar amount and percentage. No burn rate or runway.

Kay does not want to be in the weeds of bookkeeping. She wants a monthly "here's where you stand" with actionable flags. Think of this as a CFO brief, not an accounting report.

## Locations

- **Budget Dashboard Sheet:** `MANAGER DOCUMENTS / ACCOUNTING / BUDGET`
  - Sheet ID: `1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0`
  - Tab 1: Monthly Actuals vs Budget
  - Tab 2: Runway Forecast
  - Tab 3: Tech Stack Inventory
  - Tab 4: Transition Tracker
- **Vault Reference:** `brain/context/budget.md` (approved budget, COA mapping, DD reserve policy)
- **Vault Reports:** `brain/outputs/YYYY-MM-DD-budget-report-{month-year}.md`
- **Bookkeeper Reports:** Drive folder `BOOKKEEPING / MONTHLY REPORTING` (folder ID: `1Z__A8AXWBCwQN7x1nK2fqaqhVKlJBJOb`)
  - Subfolders: JANUARY 2026, FEBRUARY 2026, etc. (monthly P&L + Balance Sheet PDFs)
  - YTD folder for cumulative reports
  - Suggested COA.xlsx for QBO-to-budget category mapping

## Key Financial Parameters

- **Fund total:** $551,825
- **Fund deadline:** February 2027
- **DD reserve:** $40,000 (graduated to $80,000 at LOI stage)
- **Target monthly burn:** $17,300 (based on $190K available / 11 remaining months)
- **Steady-state burn (current):** $19,000-22,000/month
- **Interest income:** ~$500-600/month

## Data Source Phases

| Phase | Source | Period |
|-------|--------|--------|
| Phase 1 (current) | Anthony/StartVirtual monthly P&L + BS PDFs from Drive | Mar-May 2026 |
| Phase 2 (parallel run) | PDFs + Kick export (reconcile both) | May 2026 |
| Phase 3 (post-transition) | Kick export only | Jun 2026+ |
</essential_principles>

<modes>
## Mode 1: Monthly (`/budget monthly`)

**Trigger:** Kay runs this after Anthony delivers the monthly P&L and Balance Sheet (typically first week of following month).

**Pipeline (3 sequential agents):**

### Agent 1: Document Ingester

**Task:** Download the newest P&L and Balance Sheet PDFs from the MONTHLY REPORTING Drive folder. Read both PDFs. Extract structured financial data.

**Steps:**
1. List subfolders in MONTHLY REPORTING (folder ID: `1Z__A8AXWBCwQN7x1nK2fqaqhVKlJBJOb`)
2. Find the newest month folder (or YTD folder for cumulative data)
3. Download P&L and Balance Sheet PDFs via `gog drive download`
4. Read both PDFs and extract every line item into structured JSON
5. Map QBO account names to budget categories using the COA crosswalk in `brain/context/budget.md`

**Output JSON — keys MUST match QBO Chart of Accounts from `brain/context/budget.md`:**
```json
{
  "period": "2026-02",
  "p_and_l": {
    "owners_distribution_regular_wages": 12692.32,
    "payroll_expenses_payroll_taxes": 1172.17,
    "payroll_expenses_health_accident_plans": 8250.00,
    "payroll_expenses_business_insurance": 54.78,
    "contractors_outsourcing": 394.00,
    "contractors_contract_labor": 490.00,
    "office_expenses_rent_lease": 1000.00,
    "office_expenses_office_supplies": -9.04,
    "office_expenses_postage": 1.04,
    "office_expenses_apps_software_crm_storage": 318.25,
    "office_expenses_apps_software_office_use": 584.56,
    "databases_research": 282.00,
    "advertising_marketing": 247.39,
    "travel_airfare": 0,
    "travel_car_rides": 178.27,
    "travel_meals_entertainment": 1720.16,
    "travel_vehicle_gas": 47.92,
    "professional_fees_accounting": 3200.00,
    "bank_fees_service_charges": 4.56,
    "other_income_interest": 532.00,
    "total_expenses": 30628.38,
    "net_income": -30096.38
  },
  "balance_sheet": {
    "checking": 16403.23,
    "savings": 239320.45,
    "total_cash": 255723.68,
    "total_assets": 257045.43,
    "owner_investments": 551825.01,
    "retained_earnings": -233379.26,
    "net_income_ytd": -61400.32
  }
}
```

**Stop hook:** Both PDFs downloaded and parsed. All major categories have values. Cash balance extracted and non-zero.

### Agent 2: Budget Reconciler

**Task:** Compare extracted actuals to approved budget. Calculate variances. Compute burn rate and runway.

**Steps:**
1. Read approved budget from `brain/context/budget.md`
2. Read prior month data from Budget Dashboard Tab 1 (to compute YTD)
3. Calculate:
   - Monthly prorated budget = Annual Budget / 12
   - YTD prorated budget = Monthly prorated * months elapsed
   - Variance $ = YTD Budget - YTD Actual (positive = under budget)
   - Variance % = (YTD Actual - YTD Budget) / YTD Budget * 100
4. Flag any category where YTD actual exceeds YTD prorated budget by >10%
5. For each flag, add context (is this a timing issue like health installments, or a real overspend?)
6. Calculate burn rate:
   - Trailing average (all months available)
   - Steady-state (exclude one-time items: health installments, CPA filing, contractor onboarding)
7. Calculate runway:
   - Available for operations = Fund Balance - DD Reserve ($40K, or $80K if in LOI stage)
   - Months remaining = Available / Steady-state burn
   - Projected zero date
   - Buffer vs fund deadline

**Output:** Reconciled data + variance flags + runway metrics.

### Agent 3: Report Writer

**Task:** Write outputs to three destinations.

**Destination 1: Google Sheet**
```bash
SHEET_ID="1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0"

# Tab 1: Add new month column with actuals
gog sheets update "$SHEET_ID" "'Monthly Actuals vs Budget'!{NEXT_COL}1:{NEXT_COL}39" --values-json '{...}'

# Tab 1: Update YTD columns (O-R)
gog sheets update "$SHEET_ID" "'Monthly Actuals vs Budget'!O3:R39" --values-json '{...}'

# Tab 2: Refresh runway forecast
gog sheets update "$SHEET_ID" "'Runway Forecast'!B4:B28" --values-json '{...}'
```

**Destination 2: Vault**
Create `brain/outputs/YYYY-MM-DD-budget-report-{month-year}.md` following output schema. Include:
- Fund position table
- Monthly P&L summary
- Variance flags with explanations
- Runway analysis (multiple scenarios)
- Action items

**Destination 3: Slack**
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Budget Report: {Month} {Year}\nFund Balance: ${balance} ({pct}% remaining)\nMonthly Burn: ${burn}\nRunway: {months} months (steady-state)\nVariance Flags: {count}\nDashboard: https://docs.google.com/spreadsheets/d/1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0/edit"
  }'
```

**Validation (before Slack):**
- Sheet month column populated (verify with `gog sheets get`)
- Vault file exists and has frontmatter
- Fund balance is non-zero
- Runway calculation is non-negative
- If any validation fails: report what is missing, do NOT send Slack

---

## Mode 2: Runway (`/budget runway`)

**Trigger:** On demand, or invoked by investor-update skill as data source.

**Single agent. No sub-agents needed.**

**Steps:**
1. Read Budget Dashboard Tab 2 (Runway Forecast) via `gog sheets get`
2. If data is stale (>45 days old), warn Kay and suggest running `/budget monthly` first
3. Return structured JSON for investor-update consumption:

```json
{
  "budget_remaining": 255724,
  "budget_pct": 46.3,
  "burn_rate": 19500,
  "runway_months": 11,
  "dd_reserve": 40000,
  "available_for_operations": 215724,
  "fund_deadline": "2027-02",
  "as_of_date": "2026-02-28"
}
```

4. If invoked standalone (not by another skill), also print a human-readable summary.

---

## Mode 3: Tech Audit (`/budget tech-audit`)

**Trigger:** On demand. Run monthly during active search sprint. Quarterly once acquisition closes.

**3 parallel agents, then sequential synthesis:**

### Agent A: Subscription Scanner
**Task:** Find all recurring charges.
1. Search Gmail for payment receipts in last 90 days:
   ```bash
   gog gmail search "subject:(receipt OR invoice OR payment OR subscription OR charge) after:{90_DAYS_AGO}" --json --limit 50
   ```
2. Extract: tool name, amount, frequency, date
3. Cross-reference with P&L "Apps & Software" line items from latest budget report

### Agent B: Stack Mapper
**Task:** Map what tools the system actually uses.
1. Read `.claude/skills/*/SKILL.md` and extract tool dependencies (Attio, Gmail, Drive, Slack, Motion, Linkt, etc.)
2. Read `brain/context/budget.md` tech stack section
3. Read Budget Dashboard Tab 3 for current inventory
4. Flag tools that appear in receipts but NOT in any skill or workflow

### Agent C: Consolidator
**Task:** Merge findings and recommend cuts.
1. Combine Agent A (costs) + Agent B (usage) into a single inventory
2. For each tool, assess: is it actively used by a skill? Is there overlap with another tool?
3. Draft numbered recommendations (1 item at a time for Kay):
   - KEEP (essential, no overlap)
   - EVALUATE (trial period, needs decision by date)
   - CUT CANDIDATE (overlap identified, low/no usage)
   - DOWNGRADE (cheaper tier available)
4. Calculate total potential monthly/annual savings
5. Update Tab 3 of Budget Dashboard
6. Create vault output: `brain/outputs/YYYY-MM-DD-tech-stack-audit.md`
7. Slack notification with savings estimate + sheet link

---

## Mode 4: Transition (`/budget transition`)

**Trigger:** On demand. Temporary mode for bookkeeper replacement.

**Single agent.**

**Steps:**
1. Read Tab 4 (Transition Tracker) from Budget Dashboard
2. For each milestone, check current status
3. Flag overdue items (target date < today AND status != Done)
4. Report progress and next action
5. When all milestones are Done, suggest removing this mode and Tab 4

**Milestones:**
1. Anthony completes March close (Apr 7)
2. Evaluate Kick (research + CPA compatibility) (Apr 7)
3. Kick account created + configured (Apr 8)
4. Bank feed connected (Apr 10)
5. Historical data imported (Apr 14)
6. April transactions categorized in Kick (Apr 30)
7. Parallel run: Anthony + Kick for April (May 5)
8. Reconciliation (May 7)
9. Notify Anthony of cancellation (May 7)
10. Full Kick + Claude for May onward (Jun 1)
</modes>

<integration>
## Investor-Update Integration

The quarterly investor deck gets exactly **one bullet** on budget. Single line, inline format:

```
• $255K (46% remaining of $550K raised) [context note]
```

That's it. Three data points in one sentence: dollar amount, percentage of fund, brief context (e.g., "slightly under budget", "on track", "elevated due to DD costs").

Historical examples from actual quarterly updates:
- Q1: `$478K (86% remaining of $550K raised)`
- Q2: `$433K (79% remaining of $550K raised) slightly under budget`
- Q3: `$359K (65% remaining of $550K raised)`

No burn rate, no runway months, no DD reserve, no table. Those are internal numbers for Kay's CFO brief (monthly mode), not for investors.

**Preferred method:** Invoke `/budget runway` — it returns more fields but investor-update MUST only use `budget_remaining` and `budget_pct`.

**Fallback method:** Read directly from Budget Dashboard Tab 2:
```bash
gog sheets get "1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0" "'Runway Forecast'!A25:B26" --json
```
</integration>
