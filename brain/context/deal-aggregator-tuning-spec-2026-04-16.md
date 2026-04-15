---
date: 2026-04-16
type: context
title: "Deal Aggregator Tuning Spec — Vertical SaaS Pivot"
tags:
  - date/2026-04-16
  - context
  - topic/deal-aggregator
  - topic/tuning-spec
  - topic/vertical-saas
  - topic/gb-charter
---

# Deal Aggregator Tuning Spec — Vertical SaaS Pivot

**Context:** Deal 1 locked as Vertical SaaS on 2026-04-14 (Charter-level pivot). DealsX sheet restructured to 3 Charter-aligned niches: Enterprise Software & Data Platforms, Specialty Healthcare Software, Female-Led Vertical SaaS. Luxury niches (Private Club, Jewelry ERP, Specialty Food ERP) TAM-failed at $500M gate — parked as HoldCo Stage 3/4 candidates, not Deal 1. Deal-aggregator must pivot from service-business broker scanning to SaaS deal flow while retaining luxury coverage for HoldCo-stage opportunism.

## 1. Current state

Deal-aggregator scans broker platforms (Business Exits, DealForce, Rejigg, Flippa), email inbound (CIMs, broker blasts via email-scan-results), and industry-specific sources for **Premium Pest Management, Specialty Insurance Brokerage, and Estate Management**. Revenue floor is $1.5M, buy box is $1-5M EBITDA / $3-20M revenue / independently owned. Matches posted to Slack #active-deals one-per-message with thumbs up/down workflow. Target: 1-3 evaluable deals/day. Sources skew toward main-street service businesses — pest-control brokers (PCO Bookkeepers, Keystone), insurance M&A (Sica Fletcher, MarshBerry), property management (Exit Strategies Group). The skill is architecturally sound but the **thesis inputs are obsolete** for Deal 1.

## 2. What changes — SaaS filter delta

**Hard filters (Deal 1 screen, stacked on revenue floor):**
- ARR $3-10M (replaces revenue-based floor for SaaS; keep $1.5M floor for HoldCo-stage luxury catches)
- Founded 2021 or earlier (5+ years operating history)
- 10-50 employees
- Bootstrapped — **zero VC/PE funding** (hard stop; check Crunchbase/PitchBook signal)
- B2B only (B2C auto-reject)
- 85%+ GRR, 20%+ YoY growth (flag if disclosed; mark "unverified" if not)

**Moat requirement — 2 of 5 required:**
(1) system of record, (2) deep integrations, (3) regulatory/compliance lock-in, (4) multi-party workflow, (5) physical-world tethering. Listing must plausibly hit 2+ to surface as thesis match.

**Disqualifiers (auto-reject, no Slack):**
PE-owned, VC-funded, California HQ (soft — flag if exceptional), aviation software, lending/credit SaaS, B2C, horizontal SaaS (Slack/Notion-style), <$3M ARR, <5yrs operating, AI-disruptable thin wrappers (content-gen, generic chatbots, single-LLM-call products).

## 3. New sources to add — SaaS deal flow

**Primary SaaS marketplaces:**
- **MicroAcquire / Acquire.com** — largest SaaS marketplace, searchable, registration required. Filter: $3M+ ARR, B2B, bootstrapped.
- **FE International** (already listed — activate: Kay must register as buyer).
- **Quiet Light Brokerage** — SaaS-heavy, email list + listings.
- **Website Closers — SaaS vertical** (websiteclosers.com/technology).
- **Empire Flippers — SaaS tier** ($1M+ listings).
- **Flippa SaaS filter** (already scanned, re-filter for $3M+ ARR B2B only).

**SaaS-specialist M&A advisors:**
- **Founderpath** — bootstrapped SaaS deal flow, founder network.
- **SaaS Group** (saas.group) — strategic acquirer, market signals.
- **SaaS Capital** — lender + market data, deal comps.
- **Software Equity Group (SEG)** — middle-market SaaS advisory, quarterly reports.
- **AE Studio / Boring Business** — boring-SaaS acquisition content, occasional deal flow.

**Community / signal channels:**
- **SaaS Mafia newsletter** — curated deals, weekly.
- **Vertical SaaS Slack communities** (Bruce's Blue Frame network, Datacor alumni, Adam Coffey ECP network — Kay to request invites).
- **MicroConf / SaaStr ETA tracks** — off-market signal via attendee lists.
- **Boring Portfolio, Tiny Seed alumni** — bootstrapped SaaS exits.
- **IT ExchangeNet** — technology-focused M&A marketplace.

**Charter sub-vertical scanners (route via Niche 1-3 on DealsX sheet):**
- **Specialty Healthcare Software:** Home Health Tech Report, HIStalk classifieds, Healthcare IT News M&A tracker.
- **Enterprise SW & Data Platforms:** Compliance/regtech newsletters (Regulatory Compliance Watch), ERP M&A advisors (Software Equity Group vertical ERP practice).
- **Female-Led Vertical SaaS:** All Raise network signals, Female Founders Fund portfolio exits, Chief network deal chatter.

## 4. Sources to deprioritize (retain, lower priority)

Three luxury niches still active on DealsX sheet as HoldCo-stage candidates. Keep scanning but **demote to weekly cadence, not daily**, and **route matches to #active-deals with "HoldCo candidate" tag**, not Deal 1 Slack priority:

- **Pest:** PCO Bookkeepers, Keystone, Cetane, DealFlow Agent, Anticimex — weekly scan.
- **Insurance:** Sica Fletcher, MarshBerry, Reagan, Agency Checklists — weekly scan (retain for Deal 2 Engine prep).
- **Estate management:** Exit Strategies Group, Synergy — biweekly scan.
- **Associations:** NPMA, IIABA, IREM, NARPM — monthly scan.

Rationale: luxury niches are HoldCo Stage 3/4 and Engine (insurance = Deal 2). They're real, just not urgent. Don't burn daily budget on them.

## 5. Scoring updates — SaaS-specific inputs

New scoring inputs (append to existing buy-box screen):

| Input | Weight | Source |
|---|---|---|
| ARR growth YoY | High | Listing / CIM |
| Gross margin | High | CIM (target 75%+) |
| NRR / GRR | High | CIM (85%+ GRR hard) |
| Churn % | High | CIM |
| Integration count / partner depth | Medium | Website, listing |
| Regulatory moat presence | High | Industry inference |
| Bootstrapped status | Hard filter | Crunchbase/PitchBook |
| Years operating | Hard filter | Listing |
| AI-disruptability flag | Hard filter | Sub-agent judgment |

**Charter sub-vertical weighting:**
- **Niche 1 matches (Enterprise SW & Data Platforms):** +10 pts, includes luxury catch-net sub-verticals.
- **Niche 2 matches (Specialty Healthcare Software):** +15 pts (Adam Coffey's ECP pattern, proven exit template).
- **Niche 3 matches (Female-Led Vertical SaaS):** +15 pts (right-to-win, jewel-adjacent).
- Buy-box match in un-screened vertical SaaS sub-niche: +5 pts, route to niche-intelligence as discovery signal.

## 6. Output format changes — email-scan-results artifact

Add SaaS-specific fields to the per-deal output block:

```markdown
- **{Company}** — {Source} | ARR: {$X.XM} | Growth: {X%} | GRR: {X%} | Margin: {X%} | Employees: {n} | Founded: {YYYY} | Funding: {Bootstrapped/Seed/VC/PE} | Moats: {list 2+ of 5} | AI-risk: {Low/Med/High} | Match: {Niche 1/2/3 / Buy-box new / HoldCo candidate} | {Link}
```

Flag any deal where a hard filter field is "not disclosed" as **"NEEDS CIM"** — same Slack priority but cues Kay the data gap exists.

## 7. Integration points

- **target-discovery:** Deal-aggregator surfaces broker-sourced deals; target-discovery handles cold targets per Charter niche 1-3. No overlap — dedup by company name against Attio.
- **email-intelligence:** CIM auto-trigger already active. Add SaaS-keyword boost (ARR, NRR, churn, integrations) to classification confidence; route SaaS CIMs to deal-evaluation same-day (active deal urgency rule).
- **pipeline-manager:** Morning briefing line stays "deal-aggregator — {n} new deals posted to Slack"; add breakdown: "{n} Deal 1 (SaaS) / {n} HoldCo-stage."
- **Attio Intermediary Pipeline:** New SaaS-specialist intermediaries (Acquire.com, Founderpath, SaaS Group) get entity + "Identified" stage entries on first contact.

## 8. Implementation checklist — SKILL.md edits

1. **`<objective>` block:** Update `Inputs` to reference SaaS Reference Doc (Drive ID `14S067rkvZPy3Jp5LkphP8DOqhajtRdc-xRi4bIe92YU`) as the Deal 1 buy box authority.
2. **Channel 1 platform list:** Add new "SaaS marketplaces" and "SaaS-specialist advisors" sub-sections; demote current luxury brokers to weekly cadence with explicit note.
3. **Step 0 (load active theses):** Keep, but rewrite to read DealsX sheet Niches 1/2/3 as primary and WEEKLY REVIEW luxury rows as secondary (HoldCo-candidate tag).
4. **Scanning process step 5:** Add SaaS hard filters (ARR, founding year, employees, funding, B2B, moats) ahead of revenue floor. Auto-reject VC/PE-funded.
5. **Step 6 match classification:** Add third type — "HoldCo candidate" — for luxury niche matches post-Charter.
6. **Channel 3 (industry-specific):** Add Charter sub-vertical sources listed in Section 3 above; keep luxury sources at weekly.
7. **`<niche_signals>`:** Add SaaS-specific pattern detection (consolidation waves in vertical SaaS sub-niches, bootstrapped exits clustering).
8. **`<stop_hooks>` scan hook:** Add SaaS field enforcement — ARR, funding, founded year, moat count must be captured or flagged "NEEDS CIM".
9. **`<success_criteria>`:** Update Phase 2 target to "1-3 Deal 1 (SaaS) + 0-1 HoldCo-stage per day." Add 4-week review of SaaS source yield.
10. **Slack template:** Add ARR / Growth / Funding / Moats line to the deal message body.

## 9. Migration risks

- **Over-tune to SaaS, lose pest/insurance flow entirely.** Insurance is Deal 2 — we need flow when Deal 1 closes. Weekly cadence is the floor, not zero.
- **False SaaS disqualifications.** CIMs don't always disclose GRR/churn upfront. "NEEDS CIM" tag prevents premature rejection.
- **PE-owned SaaS false negatives.** Bootstrapped vs seed-funded distinction is nuanced — seed + no follow-on may still qualify if cap table is clean. Sub-agent judgment required; flag edge cases for Kay.
- **California soft filter.** Many SaaS deals are CA-based. Flag, don't auto-reject.
- **Horizontal vs vertical SaaS confusion.** Sub-agent must verify ICP concentration before classifying. If >70% of customers are in one industry, it's vertical.
- **Volume dip during transition.** Budget 2 weeks of below-target flow while new sources onboard.

## 10. Success criteria — measurable after 2 weeks

- [ ] **Source coverage:** All 10+ new SaaS sources accessible daily (platforms scraped or registered). Binary pass/fail per source.
- [ ] **Deal yield:** 7-day rolling average of 1-3 Deal 1 (SaaS) deals/day by end of week 2.
- [ ] **HoldCo flow maintained:** ≥3 HoldCo-stage deals/week surfaced across luxury niches (not zero).
- [ ] **CIM conversion:** ≥50% of SaaS matches result in CIM request within 5 business days of Slack flag.
- [ ] **Filter precision:** <10% of Kay's thumbs-down reactions cite "wrong buy box" (vs "wrong fit"). If higher, hard filters are mis-tuned.
- [ ] **No PE/VC leakage:** Zero VC/PE-funded deals surfaced as Deal 1 candidates. Any leak = immediate source recalibration.
- [ ] **Intermediary network growth:** ≥2 new SaaS-specialist advisors added to Attio Intermediary Pipeline in 2 weeks.
- [ ] **Integration with deal-evaluation:** Every SaaS CIM triggers deal-evaluation within 24 hours (active-deal urgency rule).

Review at 4 weeks: full Charter-alignment audit. If Deal 1 flow <1/day rolling average by week 4, expand sources (add IT ExchangeNet tier-2, cold-email SaaS-specialist boutiques, join 2+ vertical SaaS Slacks).
