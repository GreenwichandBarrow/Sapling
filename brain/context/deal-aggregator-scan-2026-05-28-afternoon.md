---
date: 2026-05-28
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 1
email_deals: 0
dealsx_replies: 0
morning_artifact_present: true
---
# Deal Aggregator Scan — 2026-05-28 (Afternoon)

Afternoon top-up run (2pm ET, headless). Per SKILL.md afternoon-run spec: re-read buy-boxes + active niches; rescan ONLY time-sensitive platforms (Rejigg, Flippa, Everingham & Kerr) + email channel; skip full Channel 1 + 3 sweep (morning run covered those — 17 Active sources, 80 listings reviewed, 0 PASS, 4 NEAR-MISS, 2 FLAG).

Buy-boxes re-read live from Drive (Services / Insurance / SaaS) — no edits since morning. WEEKLY REVIEW + DEALSX tabs re-read — no niche toggles or corpus changes since morning. Corpus paths per active niche identical to morning artifact (all 8 active niches resolved cleanly).

**Result: zero PASS, zero NEAR-MISS, zero FLAG this afternoon → zero Slack posts to `#active-deals`.** Flippa homepage produced 9 sub-scale SaaS/content listings (all far below the SaaS $3M ARR floor + horizontal/B2C hard-excludes), Rejigg /businesses login-gated (single-attempt — Kay re-auth needed), Everingham & Kerr site is historical-only (no active listings ever posted publicly — email-only intermediary). No new email-scan-results artifact produced this afternoon (email-intelligence runs once at 7am headless), so Channel 2 re-read = same 10 morning broker-BLAST listings already screened in morning artifact (all HARD-REJECT carried forward). No new `dealsx.notifaction@gmail.com` Lead Interested notifications observed in the morning email-scan window.

## Deals Surfaced (sent to Slack individually)

None today. Zero listings passed both the buy-box financial gate AND an active-niche corpus match this afternoon.

## Email Inbound Deals

None new this afternoon. Channel 2 re-read of [[brain/context/email-scan-results-2026-05-28]] surfaces the same 10 morning broker-BLAST listings (5 Helen Guo SMB Deal Hunter + 4 Flippa Marketplace digest + 1 Quiet Light single-listing alert) — all HARD-REJECTED in the morning artifact, fingerprints unchanged, not re-Slacked. No CIMs, NDA confirmations, broker BLASTs targeted at G&B, intro forwards, or other deal-specific emails landed since the 7am email-intelligence run.

## DealsX Proprietary Outreach Replies

None today. No `dealsx.notifaction@gmail.com` "Lead Interested" notifications in today's email-scan-results.

## Near Misses (not Slacked)

- **No afternoon NEAR-MISS items.** Flippa homepage SaaS listings (MRR $86–$9,624 / ARR $1K–$115K) sit one to two orders of magnitude below the SaaS Buy Box ARR floor ($3M minimum) and overwhelmingly horizontal or B2C — corpus mismatch + financial gate failure, classified HARD-REJECT not NEAR-MISS.
- Morning artifact's 4 NEAR-MISS items (GovCon IT Firm, B2B Experiential Marketing, Government Contract ERP, California Property Tax Consultants) carry forward in the morning record; not re-listed here per separate-artifact discipline.

## Listings Reviewed (full log)

Every listing scraped or parsed during this afternoon run, regardless of verdict. Sort: PASS → NEAR-MISS → FLAG → HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Flippa | Mergify (Shopify App) | Canada | $115K ARR ($9,624 MRR) | undisclosed | undisclosed | Horizontal SaaS / Shopify app | HARD-REJECT | Non-US + ARR below $3M floor + horizontal SaaS hard-exclude |
| Flippa | Bot Grabber | US | $39K ARR ($3,290 MRR) | undisclosed | undisclosed | Horizontal B2B SaaS | HARD-REJECT | ARR below $3M floor + horizontal SaaS hard-exclude |
| Flippa | Education SaaS Platform | India | $62K ARR ($5,130 MRR) | undisclosed | undisclosed | Ed-tech SaaS | HARD-REJECT | Non-US + ARR below $3M floor + horizontal ed-tech off-thesis |
| Flippa | Tradevipe | Brazil | $61K ARR ($5,115 MRR) | undisclosed | undisclosed | B2B SaaS | HARD-REJECT | Non-US + ARR below $3M floor |
| Flippa | Porn Blocker App (iOS/Windows) | Michigan US | $110K ARR ($9,154 MRR) | undisclosed | undisclosed | B2C / prosumer SaaS | HARD-REJECT | ARR below $3M floor + B2C/prosumer SaaS hard-exclude |
| Flippa | smashhaus.com | California US | $107K ARR ($8,923 MRR) | undisclosed | undisclosed | SaaS marketplace / entertainment | HARD-REJECT | ARR below $3M floor + CA soft-flag + entertainment off-thesis |
| Flippa | Free Birds Magazine | UK | $1K ARR ($86 MRR) | undisclosed | undisclosed | Travel content | HARD-REJECT | Non-US + sub-scale + consumer content off-thesis |
| Flippa | FFMI Calculator Online Tool | Colorado US | $108/yr ($9 MRR) | undisclosed | undisclosed | Health calculator / content | HARD-REJECT | Sub-scale ($108 ARR) + consumer content off-thesis |
| Flippa | Longhorn Menu | Texas US | $768/yr ($64 MRR) | undisclosed | undisclosed | Food content / AdSense | HARD-REJECT | Sub-scale + consumer content off-thesis |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | login-gated | 200 | 0 | 0 | — |
| Flippa | General | active | 200 | 9 | 0 | — |
| Everingham & Kerr | General | active (no live listings) | 200 | 0 | 0 | — |
| Email Channel (re-read morning artifact) | General | active | n/a | 0 (no new since morning) | 0 | — |

**Notes:**
- `Rejigg` — landing page (`/`) is marketing-only; `/businesses` route loaded but listing content is login-gated (only navigation header rendered, no listing data). Marked `login-gated` per SKILL.md scorecard status values; surface to Kay for re-auth (Kay has Rejigg account per Sourcing Sheet — session may have expired). Classified as `blocked (single-attempt)` for frontmatter accounting since only one route was probed this afternoon (root path `/` was reached but listings live behind `/businesses` auth). Will retry on tomorrow's morning run via the documented email-alert path (Rejigg's primary scrapable channel is the deal-match email digest, not the web platform).
- `Flippa` — homepage scrape succeeded (9 sub-scale SaaS/content listings). All clear the JS-shell concern that historically routes Flippa to agent-browser; the public homepage carousel renders server-side without auth. None of the 9 listings approach the SaaS Buy Box $3M ARR floor (highest = Mergify at ~$115K ARR), so corpus matching was moot — all HARD-REJECT on financial gate + horizontal/B2C/non-US axes.
- `Everingham & Kerr` — site confirmed historical-only (100+ closed transactions 1988–present, no live listings publicly posted — broker is email-only per Sourcing Sheet). No afternoon email blast observed in today's email-scan window (morning artifact: 0 Everingham emails). Marked `active` (site reachable, model correctly understood) with 0 listings reviewed — consistent with email-only intermediary classification.
- `Email Channel` — afternoon re-read of [[brain/context/email-scan-results-2026-05-28]] returns the same 10 broker-BLAST listings already screened in the morning artifact (5 Helen Guo + 4 Flippa Marketplace digest + 1 Quiet Light). No new email-scan-results-afternoon artifact exists (email-intelligence is weekday 7am only). Fingerprints unchanged → zero new Slack posts. Zero new DealsX `Lead Interested` notifications.
- **Channel 4 (Association deal boards), Channel 5 (New introductions), Channel 6 (DealsX replies)** — skipped per afternoon-run spec; morning run covered Channel 5 (Greg Pitkoff intro → relationship infra, not deal flow) and Channel 6 (zero DealsX replies). Channel 4 is morning-run-only by design.

## Volume Check

- Deals surfaced this afternoon: 0
- Combined today (morning + afternoon): 0
- 7-day rolling average: 0 (consistent with 2026-05-26 + 2026-05-27 + 2026-05-28 morning — zero PASS on four consecutive headless runs across both daily fires)
- Target: 1-3/day — **BELOW TARGET**

**Below-target note:** Afternoon top-up adds 9 Flippa homepage SaaS/content listings to the day's reviewed total (~89 listings combined morning + afternoon), still yielding zero PASS. Afternoon-specific signal: Flippa homepage inventory is dominated by sub-$10K MRR Shopify apps + content sites + B2C utilities — orders of magnitude below the SaaS Buy Box gate. Confirms the morning artifact's note that broker-marketplace inventory is broad/generalist while G&B's active-niche corpus (8 niches, weighted to specialty/luxury services + vertical SaaS for luxury) is narrow — corpus mismatch is the dominant filter on both daily fires. Reinforces [[feedback-industry-is-output-of-network]] doctrine: network-mapping-first thesis (women-led network + warm-intro paths) produces signal where marketplace screens produce noise.

Recommended follow-up (not actioned this run — surfacing only): Rejigg session re-auth would let the afternoon top-up actually screen Rejigg deal-match listings instead of bouncing at login. Kay's call.
