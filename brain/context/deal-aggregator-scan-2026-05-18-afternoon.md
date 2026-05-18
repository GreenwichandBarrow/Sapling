---
date: 2026-05-18
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 2
email_deals: 0
dealsx_replies: 0
buy_box_source: live
morning_artifact_missing: false
---
# Deal Aggregator Scan — 2026-05-18 (Afternoon Top-Up)

Afternoon (`--afternoon`) lightweight rescan: email channel + time-sensitive platforms only (Rejigg / Flippa / Everingham & Kerr). Full Channel 1 + 3 + 4 sweep was the morning run's job (`deal-aggregator-scan-2026-05-18.md`, 1 deal surfaced — DealsX reply). Buy-boxes (Services / Insurance / SaaS) and active niches re-read live this run; no Kay edits detected since morning. Morning artifact present and untouched.

## Deals Surfaced (sent to Slack individually)

None this afternoon. No time-sensitive platform listing cleared the buy-box gate AND matched an active-niche corpus. No new email-inbound deal landed after the morning email-intelligence run.

## Email Inbound Deals

None today. `brain/context/email-scan-results-2026-05-18.md` present and re-parsed: Sections 2 & 7 both "None" — no CIMs, no NDA/teaser/blind-profile emails, no broker BLAST with listing-signal keywords after the morning run. Helen Guo / SMB Deal Hunter "It's finally out!" confirmed (morning + afternoon) as a product-launch newsletter, not a per-listing broker blast. No new email-driven deal flow this afternoon.

## DealsX Proprietary Outreach Replies

None new this afternoon. The single DealsX interested-lead notification this cycle (Greg Bruyere / Tristate, gregb@tristate-stl.com, St. Louis MO — Prospect Geni 2026-05-17 19:38) was already surfaced and Slack-posted by the morning run, and is present in `deal-aggregator-fingerprints.jsonl` (company_hash `0e5d5fd793234718e84b4150d787b06b90efb9cf`, industry `dealsx-lead`, St. Louis MO). Manual dedup applied (the fingerprint helper `check` subcommand remains broken on this Linux VPS — see infra note) → already-posted, Slack skipped. Counts toward today's daily volume under the morning run, not double-counted here (`dealsx_replies: 0` this artifact by design).

## Near Misses (not Slacked)

- **No new listings parsed this afternoon** — Rejigg and Flippa returned no server-rendered listings without browser automation (agent-browser not installed on this VPS); Everingham & Kerr is email/relationship-only with no public offerings page; email channel produced no new deal flow. Nothing reached buy-box screening this run.
- **infra: fingerprint helper `check` broken on Linux VPS** — `scripts/deal-aggregator-fingerprint.sh check` invokes `date -u -v-30d` (BSD/macOS syntax); fails `date: invalid option -- 'v'` under `set -e` whenever the store file exists. `hash` and `add` work (portable `date -u +%Y-%m-%d`). Dedup performed manually this run (store has 1 record, the AM DealsX lead). Carried from the 2026-05-18 morning artifact — recommend porting cutoff to GNU `date -u -d "-30 days" +%Y-%m-%d` with an OS guard. (Unchanged since morning.)
- **infra: agent-browser not installed on this VPS** — `agent-browser: command not found`. JS-shell / login-gated fallback unavailable, so Rejigg and Flippa cannot be recovered this run. Surfaced for retry, not silently dropped. (Carried from morning artifact — unchanged.)

## Listings Reviewed (full log)

Zero listings were scraped or parsed this run (Rejigg login/JS-gated, Flippa JS-shell, E&K email-only, email channel no new deals). Header emitted with no data rows per the Results File template.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|

## Source Scorecard

Rows = the time-sensitive sources actually scanned this afternoon (not the full morning source list). `Matches` / `Last Match Date` from `deal-aggregator-fingerprints.jsonl`.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General (time-sensitive) | blocked (single-attempt) | 200 (JS/login-gated, no listings) | 0 | 0 | — |
| Flippa | General (time-sensitive) | blocked (single-attempt) | 200 (JS shell, no SSR listings) | 0 | 0 | — |
| Everingham & Kerr | Email-only broker (time-sensitive) | active (verified email-only — site live, no public offerings page; no afternoon blast in email-scan-results) | 200 | 0 | 0 | — |
| Email channel (email-scan-results-2026-05-18.md) | Email Inbound (Ch.2/6) | active | n/a | 0 | 1 (AM DealsX lead, already posted) | 2026-05-18 |

Note on blocked status: Rejigg + Flippa marked `blocked (single-attempt)` not `blocked (verified)` because the documented fallback (agent-browser) is not installed on this VPS, so a verifying second-attempt could not be made. Per `feedback_test_before_concluding_channel_dead`, these are surfaced for retry once browser automation is available, not declared dark.

## Volume Check

- Deals surfaced this afternoon (net-new): 0
- Deals surfaced today total (morning + afternoon): 1 (DealsX inbound reply — Greg Bruyere / Tristate, surfaced AM)
- 7-day rolling average: ~0.3/day (fingerprint store holds 1 record over the trailing window; afternoon runs are top-ups, primary volume is the morning full sweep)
- Target: 1-3/day — BELOW TARGET (afternoon top-up added no incremental volume; time-sensitive platform recovery is gated on agent-browser install + fingerprint-helper port — both standing infra items carried from the morning artifact)
