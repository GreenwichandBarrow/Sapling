---
schema_version: 1.1.0
date: 2026-04-27
type: context
title: "Deal Aggregator Scan — 2026-04-27 (Afternoon)"
deals_found: 0
sources_scanned: 9
sources_blocked_verified: 1
sources_blocked_single_attempt: 3
email_deals: 0
tags: [date/2026-04-27, context, output/deal-aggregator-scan, topic/deal-aggregator, status/draft]
---

# Deal Aggregator Scan — 2026-04-27 (Afternoon Top-Up)

**Important context:** The 6:00 AM ET morning run failed silently. Claude responded as if a parallel scan was already in flight (hallucinated PID 29034), exited 0, and wrote no artifact. Fingerprint store is empty (0 bytes since 4/22). This afternoon run was therefore expanded to do compensating Channel 1 coverage — but **only the lightweight afternoon-spec sources, not the full morning rotation.** Channel 3 (industry-specific niche brokers beyond Sica Fletcher / Agency Checklists) was deliberately not run this afternoon — flagged below as a coverage gap to recover tomorrow.

## Deals Surfaced (sent to Slack individually)

**ZERO MATCHES.** No listing passed the buy-box gate against any of the 8 active niches.

## Email Inbound Deals

**ZERO.** `email-scan-results-2026-04-27.md` confirms: 0 CIMs, 0 broker blasts, 0 NDAs, 0 introductions. Quiet weekend window with newsletter / political / vendor noise only.

## Near Misses (not Slacked)

- **CA Property Tax Consultants** (Business Exits) — $6.7M rev / $4.7M EBITDA / 70% margin. Rejected: advisory services to wealthy individuals ≠ B2B services to luxury businesses (per `feedback_niche_search_direction.md`); California soft-flag also applies. Margin profile interesting — pattern-match flag only.
- **CA Staffing Firm — Recurring Revenue** (Business Exits) — $7.8M rev / $3.2M EBITDA / 41% margin. Rejected: generic "staffing" without HNW/estate/household descriptor; would need disclosure of luxury household-staffing focus to score against Estate Management corpus. Below Services revenue floor ($10M).
- **GovCon IT Firm** (Business Exits) — $19.7M rev / $3.4M EBITDA. Rejected: GovCon vertical does not match any active niche; SaaS box requires luxury/HNW vertical, not federal-services.
- **GovCon ERP SaaS** (Business Exits) — $14M rev / $2.6M EBITDA. Rejected: federal-services SaaS, fails vertical-luxury requirement.
- **B2B Experiential Marketing** (Business Exits) — $14.3M rev / $3.3M EBITDA / 23% margin. Rejected: marketing/advisory services, not luxury B2B operator.
- **Sica Fletcher 5 closed-deal announcements** (Safe Harbour, O'Neill, Quantum, Centennial, Surety Bonds) — Rejected as listings: these are completed sell-side advisor announcements, not for-sale. None disclosed art/collectibles/HNW specialty descriptors → not niche 7 thesis matches even if they were active. Counted as niche signals only.
- **Agency Checklists 2 closed retail-agency transactions** (Cushman/Bergeron MA, MountainOne/Morey MA) — Rejected for same reason: closed deals, retail mass-market agencies, no specialty descriptors.

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — (fingerprint store empty since 4/22) |
| Rejigg | General | blocked (single-attempt) — JS shell on /businesses | 200 | 0 | 0 | — |
| Flippa | General | blocked (single-attempt) — JS shell | 200 | 0 | 0 | — |
| Everingham & Kerr | General | active but no live listings page (closed-transaction case studies only) | 200 | 0 | 0 | — |
| DealForce | General | login-gated — registration required | 200 | 0 | 0 | — |
| BizBuySell | General | blocked (single-attempt) — 403 | 403 | 0 | 0 | — |
| Quiet Light | General | blocked (verified) — Cloudflare 403, persistent | 403 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 5 (closed deals only) | 0 | — |
| Agency Checklists | Niche-Specific (Insurance) | active | 200 | 2 (closed deals only) | 0 | — |

**Sources NOT scanned this afternoon (full Channel 1 + 3 not in afternoon spec):** PCO Bookkeepers, Keystone Business Advisors, Cetane, DealFlow Agent, Anticimex (Pest); MarshBerry, Reagan Consulting (Insurance); Exit Strategies Group, Synergy Business Brokers (Estate Mgmt); NPMA, IIABA, IREM, NARPM (Association deal boards); Acquire.com, BizScout, Kumo, FE International, Searchfunder, Website Closers (gated platforms — none registered yet).

**Coverage gap to recover:** with morning run dark, today's full Channel 3 niche-specific coverage was missed. Sica Fletcher and Agency Checklists were the only niche-specific sources pulled.

## Volume Check

- Deals surfaced today: **0**
- 7-day rolling average: not computable (fingerprint store empty since 4/22 — calibration data lost; needs rebuild)
- Target: 1–3/day — **BELOW TARGET**
- Status: 🔴 zero deal flow today is a real signal, not a coverage artifact. Even with 4 unblocked sources Business Exits inventory was 100% off-thesis (15/30 construction-or-healthcare-services, the rest GovCon/franchise/manufacturing). Channel 1 broker platforms are not producing for our buy-box.

## Niche Signals (passed to niche-intelligence Tuesday 11pm fire)

- **Insurance retail consolidation wave continuing** — 7 closed retail/Main-Street agency deals across MA/FL/MD/CO/GA in last 30 days (5 Sica Fletcher + 2 Agency Checklists). All generic retail — zero specialty-line (art/jewelry/wine/equine/marine/aviation) deals surfaced. Validates buy-box guardrail: avoid PE-consolidator-owned shops, since the consolidator wave dominates retail M&A. Also signals that niche 7 (Specialty Insurance) proprietary deal flow needs Kay's warm-network channel (her existing approach), not broker platforms.
- **Business Exits ~3-5% historical match rate** — this scan: 30 listings, 0 matches. Channel weight should drop further; not pulling our weight.
- **California-advisory recurring near-miss pattern** — 2 of 30 listings this week were CA advisory/services with 40-70% margins. Repeating pattern: high-margin CA advisory shops surface, all fail thesis (wrong layer per `feedback_niche_search_direction`). Worth surfacing in Friday digest as a "the filters are working as intended" signal, not action.
- **Massachusetts insurance retail clustering** — 3 of 7 insurance deals in MA in 30 days. Not relevant to specialty-art thesis but flag if Kay's MA network surfaces broker contacts.
- **Channel 1 platform hardening accelerating** — 4 of 9 sources hardened against unauthenticated WebFetch this run (Rejigg, Flippa, BizBuySell, Quiet Light). agent-browser install + first-login becomes a real coverage requirement, not optional.

## System Health Issues Surfaced

1. **🔴 Morning run silent failure (6:00 AM ET)** — Claude hallucinated a parallel run, exited 0, no artifact written. Pattern not seen before. Suggests anti-double-fire prompt logic in headless mode is misfiring without an actual prior run to detect. Needs investigation — either the headless-prompt template, the wrapper's lockfile check, or a recent claude-code update is at fault. **First-pass diagnosis target: `scripts/run-skill.sh` lockfile + `.claude/skills/deal-aggregator/headless-morning-prompt.md` (if exists).**
2. **🟡 Fingerprint store empty since 4/22** — `brain/context/deal-aggregator-fingerprints.jsonl` is 0 bytes. 5 days of dedup data lost. Either: (a) zero matches across all of 4/22–4/26 (possible — long weekend + Sat/Sun no-fire), or (b) earlier writes failed silently. Calibration baselines for trend detection rely on this — needs rebuild from `brain/context/deal-aggregator-scan-{date}.md` historical artifacts.
3. **🟡 4-source coverage gap (Channel 1)** — Rejigg, Flippa, BizBuySell, Quiet Light all need agent-browser to fetch. Skill spec mentions agent-browser as the fallback path but it's not installed. One install + Kay logged-in once = ~40% of Channel 1 sources unblocked.

## Stop Hooks Self-Audit

- [x] Step 0b (buy-boxes) — all three Drive docs freshly read this run (Services 47L, Insurance 50L, SaaS 46L)
- [x] Step 0c (keyword corpus) — DEALSX corpus resolved for 7 niches; "Private art advisory firms" had blank DealsX field, corpus built from WR row Niche Hypothesis + Quick notes per spec
- [x] Each scanned listing has source / URL / industry / financials (or "not disclosed") / geography
- [x] Buy-box category routing applied (Services for niches 1–5,8; Insurance for niche 7; SaaS for niche 6)
- [x] Data Availability Rule enforced — no listing auto-rejected on missing fields; rejections only on disclosed-and-failed criteria or hard-exclude industry matches
- [x] Hard-excludes applied per matching buy-box (construction, healthcare, manufacturing, franchise, restaurants, etc.)
- [x] Zero matches reported as "No matches" — not fabricated
- [x] Source scorecard row count = sources scanned (9 rows, 9 sources)
- [x] No source marked `blocked (verified)` without two-attempt verification (Quiet Light has documented persistent Cloudflare 403; others marked `single-attempt`)
- [x] No Slack notifications fired (zero matches → silent correct per skill spec; morning briefing reports count only)
