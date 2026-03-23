# Budget Metrics Definitions

## Burn Rate Calculations

### Trailing Average Burn
- Sum of all monthly net burns / number of months
- Net burn = Total expenses - Interest income
- Includes ALL expenses (one-time items inflate this)
- Use for: worst-case runway projection

### Steady-State Burn
- Trailing average MINUS identified one-time items:
  - Health insurance installments (front-loaded, ending after ~3 months in Year 2)
  - CPA annual filing ($3,200, hits once per year, typically Feb)
  - Contractor onboarding premiums (first month only)
  - Legal fees (deal-specific, not recurring)
  - Hardware purchases (one-time)
- Use for: realistic runway projection and budget planning

### Target Burn
- Calculated as: Available for Operations / Months to Deadline
- Available = Fund Balance - DD Reserve
- Represents the burn rate needed to reach the fund deadline
- If Steady-State > Target: savings needed = Steady-State - Target

## Variance Thresholds

| Level | Variance % | Action |
|-------|-----------|--------|
| Green | <5% over | No flag |
| Yellow | 5-10% over | Monitor, note in report |
| Red | >10% over | Flag with explanation required |

**Variance formula:**
- Variance $ = YTD Budget - YTD Actual (positive = under budget, good)
- Variance % = (YTD Actual - YTD Budget) / YTD Budget * 100 (positive = over budget, bad)

**Context matters:** Some variances are timing issues, not overspends:
- Health insurance installments: large in first months, zero later
- CPA annual filing: entire year's cost hits one month
- Travel/airfare: lumpy by nature (conference months vs quiet months)

When flagging a variance, always note whether it is:
1. **Structural** (permanent overspend, requires action)
2. **Timing** (front-loaded, will normalize)
3. **One-time** (not recurring)

## Runway Scenarios

Always present multiple scenarios:

| Scenario | Description |
|----------|-------------|
| Current burn | Trailing average, includes one-time items. Worst case. |
| Steady-state | Excluding one-time items. Realistic case. |
| Target | With planned savings implemented. Best case. |
| With cuts | After tech/bookkeeper savings are realized. Aspirational. |

## DD Reserve Policy

- **Default:** $40,000 held back from operational runway
- **At LOI stage:** Escalate to $80,000
- **Post-close or fund wind-down:** Release reserve back to operations
- **Typical DD costs per deal:**
  - Quality of Earnings (QofE): $15,000-25,000
  - Legal review: $5,000-10,000
  - Environmental/other: $5,000-10,000
  - Total per full DD: $25,000-45,000

## Investor Reporting Fields

These four fields are what the investor-update skill needs:

| Field | Definition | Source |
|-------|-----------|--------|
| `budget_remaining` | Fund Balance (total cash in bank accounts) | Balance Sheet: Total Bank Accounts |
| `budget_pct` | Fund Balance / Owner Investments * 100 | Calculated |
| `burn_rate` | Steady-state monthly net burn | Calculated from trailing P&Ls |
| `runway_months` | Available for Operations / Steady-state burn | Calculated |
