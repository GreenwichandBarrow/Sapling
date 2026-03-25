# G&B Industry Scorecard Structure

## Per-Niche xlsx Architecture

Each niche gets its own standalone scorecard xlsx file, stored in its Drive folder alongside the one-pager pptx.

**Structure of each niche xlsx:**
- **Tab 1: INITIAL SCREEN** -- Pass/fail gate on 4 criteria (margins, recurring revenue, growth, Growth TAM). Must pass all 4 to proceed to detailed scoring.
- **Tab 2: Industry Scorecard** -- Detailed 7-category scoring with weighted formulas (renamed from TEMPLATE tab in the master). Sub-criteria scored as +/+/-/-, formulas auto-calculate weighted totals.
- **Tab 3+: Company Scorecards** -- Added by deal-evaluation skill as individual acquisition targets within the niche are scored. Each company gets its own tab.

**Template source:** `brain/library/internal/scorecard/G&B Industry & Company Scorecard Template.xlsx`

**The xlsx is the source of truth for scores.** The one-pager pptx reflects the score in its Assessment/Status section. The Industry Research Tracker Google Sheet summarizes scores for cross-niche comparison. If there is ever a discrepancy, the xlsx wins.

**Naming convention:** `{Niche Name} Scorecard {Month} {Year}.xlsx`
**Location:** Same Drive folder as the niche one-pager, under WEEKLY REVIEW subfolder (`1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT`)

---

Source: `G&B Industry & Company Scorecard Template.xlsx`
- **Original Drive ID:** `1kCCbEBpAgwX2TMn095W8-EzUUqvXIpWO`
- **Updated copy (3/20/2026, with INITIAL SCREEN tab):** `1_67yuJOFLvBX-1U5hEpTAO1q74-fr4aH`
- **Location:** MANAGER DOCUMENTS / G&B MASTER TEMPLATES (Drive folder: `19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx`)
- **Local copy:** `brain/library/internal/scorecard/G&B Industry & Company Scorecard Template.xlsx`
- **Completed scorecards** (with filled-in data) are in the older file: `G&B Scorecard Industry & Company 7.24.25.xlsx` (also saved locally)

## INITIAL SCREEN (Tab 1 — Pass/Fail Gate)

Run BEFORE the Industry Scorecard. All 4 must pass to proceed.

| Criterion | Pass Threshold | What to evaluate |
|-----------|---------------|------------------|
| Margins | 15%+ EBITDA | Typical EBITDA margins for companies in this industry |
| Recurring Revenue | Existing or convertible | Is there contractual/subscription revenue, or a clear path to convert? |
| Industry Growth | Above GDP (~3%+) | Industry CAGR relative to GDP growth |
| Growth TAM | $500M+ market size | Total addressable market. $500M is the investor floor — below this is a red flag. |

**Target TAM (informational — NOT scored, NOT a gate):**
- Number of independently owned acquisition candidates in this niche
- Determines sprint duration: 50+ = long, 20-50 = focused, 10-20 = fast, <10 = very fast
- Reported as a column on the Industry Research Tracker (like QSBS)

## Industry Scorecard (Tab 2 — 9 criteria, weighted, score 1-4)

| Category | Criterion | Weight | 4 (Best) | 3 | 2 | 1 (Worst) | What to evaluate |
|----------|-----------|--------|-----------|---|---|-----------|------------------|
| Growth | Industry Growth | 10% | 20%+ CAGR | 10-20% CAGR | 5-10% | <5% CAGR | CAGR trends with 5-7yr staying power in fragmented & sizable market |
| Growth | Future Growth | 10% | All trends = tailwinds | Majority tailwinds | Mix | Majority headwinds | LTM revenue growth, historic growth, resilience in downturn, macro trends |
| Size | Business Quality / TAM | 10% | >$1.5B | $750M-1.5B | $300M-750M | <$300M | Scalability, TAM vs number operating in space |
| Size | Market Position | 10% | No competitive entrance possible | Major barriers to entry | Some barriers | No barriers | Market share, penetration, switching costs, differentiation, pricing power |
| Criticality | Revenue Concentration | 10% | Co has power over suppliers & customers | Power over one, parity with other | Supplier or customer has power | Both have power over co | % revenue from top 5 customers, retention, underserved customers |
| Criticality | Predictable Revenue | 15% | Majority recurring | Mostly recurring | Mix of recurring/project/seasonal | Limited recurring | % recurring revenue |
| Criticality | Operating Efficiency | 10% | >25% | 20-25% | 15-20% | <15% | EBITDA margins |
| Penetration | Revenue Sustainability | 10% | Highly fragmented, no major cos | Small cos established | A few formidable players | 1-2 cos control market | Competitive intensity, fragmentation, CLV, CAC ratio |
| KS Fit | KS Fit | 15% | 4/4 criteria | 3/4 | 2/4 | 1/4 | B2B, 50%+ recurring, 15%+ margins, steady/growing |

**KS Fit Criteria:**
- Tier 1: 50%+ Recurring Revenue, Healthy Margins 15%+, Steady or Growing
- Tier 2: B2B, $15M+ Rev, $1.5M+ EBITDA

## Detailed Scorecard (TEMPLATE tab, 7 categories, weighted)

Used for deep-dive scoring of individual niches:

### 1. Growth, Penetration & Catalyst (25%)
- Growth relative to GDP (5yr CAGR): + = >3x GDP, +/- = 1-3x GDP, - = at/below GDP
- Industry penetration: catalyst strength
- Future growth expectations: tailwinds vs headwinds
- Evidence to support catalyst

### 2. Size & Fragmentation (10%)
- Number of players: + = thousands, +/- = hundreds, - = dozens
- Market share concentration: + = largest <10%, +/- = largest <25%, - = largest >50%

### 3. Industry Economics (10%)
- Average gross margins: + = 60-90%, +/- = 40-60%, - = 10-40%
- Average EBITDA margins: + = 30-60%, +/- = 10-30%, - = <10%
- Average ROTC: + = >20%, +/- = 10-20%, - = <10%

### 4. Mission Criticality (15%)
- Customer feedback quality
- Clarity of value proposition
- Customer switching costs: high / replaceable with effort / easy to replace

### 5. Exogenous Risks (10%)
- Tech adoption/obsolescence visibility
- Regulatory risk frequency
- Liability risks
- Cyclicality
- Exposure to trends

### 6. Porter's Five Forces (15%)
- VC-backed startup prevalence
- Level of competition
- New entrants
- Supplier power
- Customer power
- Threat of substitutes

### 7. Value Creation Opportunities (10%)
- Business complexity
- Professionalization opportunities

### 8. Impact & Externalities (5%)
- Net impact to society
- Positive/negative externalities

## Company Scorecard (score 1-10, weighted)

Used when evaluating specific acquisition targets:

| Criterion | Weight | 10 (Best) | 5 (Mid) | 1 (Worst) |
|-----------|--------|-----------|---------|-----------|
| Clear Value Proposition & Mission Criticality | 15% | Clear, mission critical | Partial clarity | Unclear, non-critical |
| Market is Hospitable & Sizeable | 15% | 35%+ penetration, strong tailwinds | Growing in smaller segments | Slow growth in target segments |
| Right to Win at ICP | 10% | Wins frequently, strong fit | Needs brand elevation | Poor ICP fit |
| Customer Retention | 10% | 100% gross / 110% net | 95% gross (industry) | Churn risk |

## Existing Completed Scorecards (tabs in xlsx)

- Home Services (10/16/25)
- Estate Planning & Trust SaaS (8/11/25)
- B2B Licensing (17/2/26)
- Specialty Insurance Brokerage (Fine Art & Collectibles)
- PostOp SaaS (4/8-4/11/25)
- Art Platform (4/28/25)
- Art Storage (8/29/25)
- Escrow SaaS (10/16/25)
