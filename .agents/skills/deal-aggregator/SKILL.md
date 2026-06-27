---
name: deal-aggregator
description: "Daily aggregation of prepped deals — businesses actively selling. Scans broker platforms, email inbound (CIMs, broker blasts), and association deal boards. Target: 1-3 evaluable deals/day surfaced to Kay via Slack."
# WARNING: 3.1x over archetype cap; refactor pending per item 2.
archetype: router
context_budget:
  skill_md: 650
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
---

<objective>
Surface prepped deals — businesses that are actively selling — from every non-DealsX channel, every day. These are deals Kay can evaluate immediately: they have financials, a teaser, or a CIM available.

**This is distinct from cold outreach.** DealsX, outreach-manager, and JJ calls target owners who aren't selling yet. This skill finds businesses already on the market.

**Target: 1-3 evaluable deals per day.** If the skill consistently surfaces fewer, expand source coverage. The funnel needs volume.

**Sources:**
1. Broker platforms (searchable listing sites)
2. Email inbound (CIMs, broker blasts, intro forwards — read from email-scan-results artifact)
3. Industry-specific deal sources (niche brokers and M&A advisors)
4. Association deal boards (classified sections, member transition programs)
5. DealsX Proprietary Outreach Replies (owners who replied with interest to DealsX cold outreach — see Channel 6)

**This skill does NOT:**
- Run or manage DealsX cold outreach itself (Sam's team owns the contact universe; DealsX is cold-email infra per `feedback_dealsx_is_cold_email_infra`). It DOES surface the inbound REPLIES that outreach produces (Channel 6).
- Trigger target-discovery from DealsX activity. DealsX-channel niches skip target-discovery entirely (`feedback_dealsx_skip_target_discovery`). A reply is inbound deal flow, never a refill signal.
- Draft outreach to owners (broker is the gatekeeper for broker-sourced deals)
- Enter deals into Attio (pipeline-manager handles that when NDA is signed)
- File documents into ACTIVE DEALS folders (pipeline-manager handles that)
- Scan Gmail directly (email-intelligence handles scanning, writes artifacts this skill reads)

<credentials>
## Credentials (read first)

**1Password is the first rung — always.** Before any op://-backed CLI (this skill uses `gog sheets`/`gog drive` + `$SLACK_WEBHOOK_ACTIVE_DEALS` + `$SLACK_WEBHOOK_OPERATIONS`):
```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
```
Exports `GOG_KEYRING_PASSWORD`, `SLACK_WEBHOOK_ACTIVE_DEALS`, `SLACK_WEBHOOK_OPERATIONS`. **NEVER `source scripts/.env.launchd` raw** — hook-blocked; see `feedback_op_env_before_op_backed_cli`.

If `${#SLACK_WEBHOOK_ACTIVE_DEALS}` = 0 after sourcing, surface to Kay — 1Password resolve broken. Do NOT log "Slack unavailable" or skip deal-surfacing without confirming the var is actually empty.

Google access also resolves through `gog` with `GOG_KEYRING_PASSWORD` from `op-env.sh`. If any `gog sheets`, `gog docs`, or `gog drive` call appears unauthenticated, run `gog auth list --check` after sourcing `op-env.sh` before reporting an outage. Do not bypass 1Password by looking for ad hoc OAuth files first.

Gmail safety is strict: this skill may create Gmail drafts only where explicitly specified. It must never send, draft-send, forward, autoreply, or call any Gmail send API. All Gmail draft work uses `gog gmail drafts create --account kay.s@greenwichandbarrow.com --gmail-no-send ...`; Kay sends manually.
</credentials>

**This skill DOES:**
- Scan all broker platforms daily for buy-box matches
- Read email-scan-results for inbound deals (CIMs, broker blasts, direct broker emails)
- Scan industry-specific deal sources for niche-relevant listings
- Monitor association deal boards
- Flag every match via Slack (#active-deals) — one message per deal, thumbs up/down workflow
- Feed listing patterns to niche-intelligence as market signals
- Process new broker introductions (research, classify, add to rotation)

**Inputs:**
- **Buy-box docs** (Google Drive, `Deal Aggregator` folder) — single source of truth for all filter criteria. Read at the start of every run. Never use cached or hardcoded bands.
  - **Services Buy Box** — doc ID `14hf5QaKtcP_Um0u_P0LZyUM_zvv7haWVVkgGmRL9iyc` — applies to Premium Pest, Estate Management, Specialty Coffee Equipment, Art Storage, Private Art Advisory, High-End Commercial Cleaning, and all new-niche non-SaaS non-Insurance listings
  - **Insurance Buy Box** — doc ID `1lkxntRwn3FOPXig86qF36eNyUS0BfbMumfNuIyInD-M` — applies to Specialty Insurance Brokerage only
  - **SaaS Buy Box** — doc ID `1I8r8w0FPJUepfBxM6HM7V_q4ibmitybIBF6w6sMQumU` — applies to Vertical SaaS for Luxury and all new-niche SaaS listings
- **Industry Research Tracker** (Sheet: `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins`, WEEKLY REVIEW tab) — active niche list read at scan start
- **email-scan-results artifact** (`brain/context/email-scan-results-{date}.md`) — inbound deal emails classified by email-intelligence
- **skill/pipeline-manager** — Intermediary Target List Sheet (broker stages, relationship status)

**Data Availability Rule (applies to every buy-box criterion):** Missing data on a listing is never grounds to auto-reject. Apply each criterion only when the corresponding field is disclosed. If a field is not disclosed, the deal is NOT rejected on that criterion — it is flagged for review. A deal with several "not disclosed" fields but no disclosed-and-failed fields still passes the buy-box gate.

**Outputs:**
- Deal matches → individual Slack notifications → Kay reacts thumbs up/down → pipeline-manager takes over on NDA
- Niche signals → niche-intelligence (new thesis ideas, market patterns)
- New intermediary entities → Intermediary Target List Sheet (`18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`)
- Dashboard health snapshot → `brain/context/deal-aggregator-status.json`
</objective>

<funnel_effectiveness>
## Funnel Effectiveness Layer

The goal is not only to run scans; the goal is to improve qualified deal flow. Every run should make it clear whether the bottleneck is source coverage, source quality, email availability, screening strictness, or surfacing UX.

### Daily classification lanes

Every reviewed listing belongs to exactly one lane:

- `PASS` — clears buy-box gate and matches an active thesis corpus. Slack-posted, subject to fingerprint dedup.
- `BROKER-OPPORTUNISTIC` — clears disclosed financial/structural gates, comes from a broker/platform/opportunistic channel, has no hard-exclude, but does not match an active thesis corpus. Artifact-only by default; not Slack-posted unless Kay later approves a broker-opportunistic rule.
- `NEAR-MISS` — promising enough to learn from but missing a required disclosed criterion, too sparse to evaluate, or useful for corpus tuning.
- `HARD-REJECT` — fails a disclosed-and-failed buy-box criterion, hard-exclude, or clearly ineligible geography/category.
- `FLAG` — ambiguous or undisclosed-field-heavy; requires human review but should not be fabricated into a pass.

**Broker-opportunistic lane purpose:** protect the funnel from being too narrow. If a financially viable broker listing is outside current active theses, preserve it for CIO review instead of burying it in generic near misses. This is especially important while G&B is tuning the source roster and active niche corpus.

### Email leg reliability

Email-inbound deal flow is a first-class leg. The morning run should not silently treat a missing email artifact as normal.

If `brain/context/email-scan-results-{date}.md` is missing:
1. Retry a small bounded wait/check loop before declaring missing.
2. Record `email_scan_status: missing` in frontmatter and dashboard status.
3. Add a visible Near Misses / Volume Check note: "email leg unavailable."
4. Do not scan Gmail directly; email-intelligence owns Gmail access and writes the artifact.

Retired 2026-06-19: the separate afternoon recovery run is no longer scheduled. Email leg reliability is handled by the 7am email-intelligence artifact and the single 7:30am deal-aggregator run; missing email artifacts surface in Good Morning instead of triggering another daily deal-aggregator status overwrite.

### Dashboard status output

If `email-scan-results` contains listing rows from a sender/source that is not already in the static source roster, the run must add that source to the Source Scorecard using the correct channel (`Newsletter` for broker blasts/saved-search digests, `Direct email` for a one-off deal email addressed to Kay). Parsed listing sources must not disappear from dashboard Source Coverage.

Current Good Morning deal-aggregator structure (2026-06-26): mirror the dashboard tab, in this order: `Surfaced matches`, `Sources covered`, `Manual check sources`. Do not invent ad hoc labels such as `Ops`, `Source registration / access`, or `New surfaced deals` unless they map into one of those three lines.

Current dashboard Source Coverage doctrine (2026-06-20):
- Dashboard Source Coverage is an operating roster, not a historical experiment log. Do not show legacy source-test rows unless Kay confirms she is signed up or actively receiving deal flow from that source.
- Paused / hidden unless reactivated: Empire Flippers, Flippa, Quiet Light, Website Closers, SMB Deal Hunter, Synergy Business Brokers, GP Bullhound, PCO Bookkeepers, and Sica Fletcher.
- Empire Flippers, Flippa, Quiet Light, and Website Closers are SaaS / digital-heavy and remain out while SaaS is deprioritized.
- Source Coverage is also Kay's relationship/source guide. Each source row should show: source name, status, this week reviewed/matches, and this month reviewed/matches. This makes stale broker/intermediary sources visible without showing raw debug tables.
- Newsletter roster includes BizBuySell, BizQuest, BizScout, Business Exits, Calder Capital, DealForce, Everingham & Kerr, Rejigg, Transworld Business Advisors, Viking Mergers, Axial, and Baton. Calder Capital is active because Kay signed up for the newsletter on 2026-06-20. BizQuest, BizScout, and Baton are active profile-backed sources because Kay added profiles on 2026-06-26.
- Direct email means a named intermediary/contact/broker relationship sending Kay a particular deal reference. Current direct-email roster: Benchmark International; Eric Mendelson (firm name TBD); Bob Williamson / Cetane; Matt Luczyk / Peapack; Richard / Stone Hill Advisors; Carlos / In3O; IAG M&A Advisors; DealsX replies (temporary through DealsX sunset).
- Never show a generic `Direct deal email` source row, Kay/self-sent message, Google Voice text notification, or meet-greenwichandbarrow system message on the dashboard. Normalize domain variants such as `quietlight.com`, `websiteclosers.com`, `greenwichandbarrow.com`, `meet-greenwichandbarrow.com`, and `txt.voice.google.com` before source-coverage display. If a direct deal email cannot be attributed to a named contact/source, surface the attribution gap in Good Morning / plumbing notes, not as a dashboard source.

Every weekday morning run writes `brain/context/deal-aggregator-status.json` with:

```json
{
  "date": "YYYY-MM-DD",
  "mode": "morning|afternoon|digest",
  "artifact": "brain/context/deal-aggregator-scan-YYYY-MM-DD.md",
  "email_scan_status": "live|missing|cached|late_recovered",
  "deals_found": 0,
  "broker_opportunistic": 0,
  "near_misses": 0,
  "sources_scanned": 0,
  "sources_covered": {
    "marketplace": 0,
    "email_newsletters": 0,
    "direct_email": 0
  },
  "manual_check_sources": [],
  "sources_blocked_verified": 0,
  "sources_blocked_single_attempt": 0,
  "volume_status": "ON TRACK|BELOW TARGET|ABOVE TARGET|CRITICAL",
  "needs_attention": []
}
```

Good Morning / dashboard rendering contract for the `Deal Aggregator` section:

1. `Surfaced matches` — show the count of surfaced matches from `deals_found` plus volume context against the 1-3/day target, e.g. `0 surfaced matches; below 1-3/day target`. Include broker-opportunistic/near-miss counts only if they change Kay's review decision.
2. `Sources covered` — show the channel split in one line: `{marketplace} marketplace; {email_newsletters} email newsletters; {direct_email} direct email`. If the split is unavailable, use `sources_scanned` once as a fallback and mark the split as unavailable so the plumbing gap is visible.
3. `Manual check sources` — list only sources Kay must manually check today because automation cannot cover them or access is blocked. If none, write `N/A`. Do not list sources already covered by the run.

Manual digest mode must **not** update `brain/context/deal-aggregator-status.json`. That file is the daily dashboard contract and must continue to point at the latest weekday morning scan artifact. If a manual digest needs machine-readable status, write a separate digest-specific artifact instead of overwriting daily status.
</funnel_effectiveness>

<channels>
## Channels

### Channel 1: Platform Scanning (Daily)
Scan searchable broker platforms for new listings matching the buy box.

**General broker platforms (cross-industry):**
- Business Exits (businessexits.com/listings/) — email + searchable, consistently accessible
- DealForce (dealforce.com) — Generational Equity buyer platform; Kay added saved search 2026-06-20, email alerts expected from DealForce / Generational sender domains; route alerts through email-intelligence.
- Rejigg (rejigg.com) — automated deal match emails + searchable
- BizQuest (bizquest.com) — BizBuySell/LoopNet-adjacent marketplace; profile added by Kay 2026-06-26. Treat as active profile-backed email/newsletter source; test public scrape only as secondary coverage.
- DealMatch (domain/account TBD) — recommended in NY ETA/SMB chat on 2026-06-16; add to source-scout queue, verify URL/registration and whether email digest exists before live scan
- Baton Market (baton.com) — registered by Kay 2026-06-19; profile confirmed active 2026-06-26. Sender observed: `chat@baton.com` and `no-reply@alerts.baton.com`, already labeled `auto/deal flow`. Treat as active email-alert marketplace source; email-intelligence captures alerts and deal-aggregator classifies in the morning run.

**AI-powered marketplaces (confirmed scrapable):**
- DealFlow Agent (dealflowagent.com) — landing page only, no live listings (4/21: `/listings` 404, marketing-buyer-counts content only). Monitor for marketplace launch; not a live-flow source.

**AI-powered marketplaces (profile-backed / scrapability TBD):**
- BizScout (bizscout.com) — Partial public marketplace via "DealOS"; profile added by Kay 2026-06-26. Treat as active profile-backed email/newsletter source; test buyer-tier access and public scrape as secondary coverage.

**AI-powered marketplaces (need Kay to register first — scrapability TBD):**
- Acquire.com (acquire.com) — SaaS/digital-heavy. Likely login-gated. Register and re-test.
- Kumo (kumo.so) — Did not resolve on initial fetch; retest before adding.

**Deal-sharing communities:**
- Searchfunder (searchfunder.com) — member deal board + email digest. Kay has annual membership. Path: enable email alerts in notification settings → email-intelligence picks up digest → deal-aggregator classifies matches. Backend scraping not available on member tier.

**General broker platforms (email-only, no searchable platform):**
- BizBuySell (bizbuysell.com) — saved-search / membership emails only; Kay confirmed 2026-06-20 this should be treated as newsletter/email flow, not active marketplace scraping
- Everingham & Kerr (everkerr.com) — most active broker, email listings
- Calder Capital (caldergr.com) — M&A advisor/broker email source; Kay requested active email-source coverage 2026-06-20; route deal emails through email-intelligence.
- Transworld Business Advisors — broker newsletter / multi-listing email source, including Samuel Curcio / Transworld Business Advisors NY blasts. Classify as newsletter in dashboard source coverage when email-intelligence extracts listing rows.
- Benchmark International (embracebenchmark.com) — email deal flow, advisory only
- Viking Mergers (vikingmergers.com) — periodic newsletter/deal blasts; active but low-priority because Viking is not highly present in the Northeast

**Relationship-only intermediaries (no public listings):**
- Woodbridge International (woodbridgegrp.com) — homepage accessible, no public listings
- Paine Pacific (painepacific.com) — few public listings, mostly NDA-gated
- IAG M&A Advisors (iagmerger.com) — Kay has account, advisory
- ProNova Partners (pronovapartners.com) — 403 blocked, relationship-only

**Paused SaaS / digital sources (do not scan while SaaS is deprioritized):**
- Flippa (flippa.com) — paused 2026-06-20; emails may still arrive but should not be scanned or counted as active source unless SaaS is reactivated
- Quiet Light (quietlight.com) — paused 2026-06-20; emails may still arrive but should not be scanned or counted as active source unless SaaS is reactivated
- Website Closers (websiteclosers.com) — paused 2026-06-20; do not scan or count as active source unless SaaS is reactivated

**Gated platforms (need Kay's registration / source-scout validation):**
- FE International (app.feinternational.com) — requires buyer registration
- DealMatch — URL/account/scrapability TBD; source recommended by peer, validate before daily rotation
- Baton Market — registered 2026-06-19 and profile confirmed active 2026-06-26; now active via email alerts from `chat@baton.com`, `no-reply@alerts.baton.com`, and Baton domain. Web marketplace may remain login-gated; primary path is email-intelligence.

**Scanning process:**

**Step 0a — Load active niches + DealsX references (REQUIRED before scanning):**
Read the Industry Research Tracker WEEKLY REVIEW tab:
```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "'WEEKLY REVIEW'!A3:I20" -a kay.s@greenwichandbarrow.com --json
```
Row 3 is headers: Rank, Niche Hypothesis, Current Status, Outreach Channel, Score, QSBS, Target Pool, Quick notes, DealsX Niche. Filter for rows where Current Status starts with "Active" (Active-Outreach or Active-Long Term). For each active row, capture:
- "Niche Hypothesis" field (G&B's narrow thesis name — authoritative)
- "DealsX Niche" field (foreign-key reference to the DEALSX tab; may be blank)

**Step 0c — Load keywords from DEALSX tab (REQUIRED for listing matching):**
Read the DEALSX tab for the keyword corpus per niche:
```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "'DEALSX'!B5:I20" -a kay.s@greenwichandbarrow.com --json
```
Relevant DEALSX fields: "Niche" (Sam's broad DealsX-submitted names), "Quick notes" (Industries/Types sub-verticals), "Keywords" (pre-tokenized match corpus).

For each active niche from Step 0a, resolve its keyword corpus:
- IF the row's "DealsX Niche" field on WEEKLY REVIEW is populated → match that value against the "Niche" field on DEALSX → pull the "Quick notes" field AND the "Keywords" field from that DEALSX row as the primary corpus (Industries/Types sub-verticals + tokenized match terms). Also pull the WEEKLY REVIEW "Quick notes" field as supplementary signal — DEALSX is more robust and takes precedence, but WR Quick notes can add niche-specific color not captured on DEALSX. Combine all three into a single matching corpus.
- IF the "DealsX Niche" field on WEEKLY REVIEW is blank (e.g., Private art advisory firms — no DealsX equivalent) → build the matching corpus from the WEEKLY REVIEW row itself. Specifically:
  1. "Niche Hypothesis" field — full string + key noun phrases tokenized (e.g., "Private art advisory firms" → "art advisory", "art advisor", "private advisory", "art consulting", etc.)
  2. "Quick notes" field — extract industry-descriptive terms, business-model phrases, customer-profile language, and any named sub-verticals
  3. Any other populated fields on that WR row ("Target Pool", "Outreach Channel") that contain industry language
  Combine these into a match corpus for the niche. Log "DealsX reference blank for {niche}; corpus built from WR row (Niche Hypothesis + Quick notes)" in the scan artifact for visibility and calibration.

**Codex-native corpus enrichment:** Do not rely on DealsX naming alone. For every active niche, add G&B-native synonyms from the WEEKLY REVIEW row, the relevant buy-box doc language, prior `BROKER-OPPORTUNISTIC` and `NEAR-MISS` themes, and obvious broker-market language. Log the enrichment path in the artifact so weak corpora can be improved in CIO review.

**Step 0d — Load new-niche watchlist from latest Niche Intelligence (REQUIRED):**
Read the latest `brain/trackers/niches/niche-intel-YYYY-MM-DD.json` sidecar and any `WEEKLY REVIEW` rows with Current Status `New`. These are NOT active theses and must not become `PASS` / Slack-posted solely because they match. They are a watchlist corpus used to upgrade relevant listings into `BROKER-OPPORTUNISTIC`, `NEAR-MISS`, or `FLAG` with a clear `new-niche-watchlist` note for CIO review and next niche-intelligence calibration.

Current watchlist additions from the 2026-06-23 Niche Intelligence assessment:
- **Luxury Amenity Management for Commercial/Residential Real Estate** — corpus: luxury amenity management, amenity operator, amenity operations, building amenities, resident amenities, tenant amenities, fitness center management, spa management, pool management, concierge staffing, lifestyle programming, club amenities, Class-A amenities, multifamily amenity management, hospitality amenity services, portfolio amenity contracts.
- **Premium Physical Security Integration & Lifecycle Maintenance for Luxury Retail and Class-A Commercial Portfolios** — corpus: physical security integration, security systems integrator, access control, video surveillance, CCTV, intrusion detection, visitor management, managed video, hosted access control, preventive maintenance, lifecycle maintenance, luxury retail security, Class-A commercial security, multisite security standards, RMR security, monitoring contracts. Exclude pure cybersecurity software unless it is bundled with physical security integration or managed physical-security service contracts.
- **Asset-Light Boat and Yacht Transport Coordination for Marinas, Dealers, Brokers, and Seasonal Owners** — corpus: boat transport, yacht transport, marine transport coordination, boat hauling brokerage, yacht hauling brokerage, oversize permits, escort coordination, marina logistics, dealer transport, yacht broker logistics, seasonal boat moves, boat-show transport, asset-light carrier coordination, marine logistics. Prefer asset-light coordinator/broker models; fleet-heavy towing/hauling without coordination or recurring marina/dealer relationships is at most `FLAG`.

A watchlist match should be logged in Listings Reviewed as `new-niche-watchlist: {niche name}`. If it also clears financial/structural gates and has no hard-exclude, classify as `BROKER-OPPORTUNISTIC` rather than generic `NEAR-MISS`; otherwise preserve as `FLAG`/`NEAR-MISS` with the watchlist signal.

**Step 0b — Load buy-box criteria (REQUIRED before scanning):**
Read the three buy-box docs from the Deal Aggregator Drive folder. These are the single source of truth for all filter criteria. Never use cached or hardcoded bands; always re-read on every run so the skill reflects Kay's current criteria.

**Current Kay screening calibration (2026-06-07):** The funnel has been too tight because Kay's prefiltering was becoming the roadblock. Preserve more reviewable opportunities when the qualitative signal is strong.

- **Positive signals to elevate:** recurring revenue and reoccurring/repeat revenue patterns, cohort/customer durability (retention, renewal behavior, churn, repeat purchasing, contract length, concentration), and criticality of the service (must-have workflow, compliance/safety/revenue-critical service, low willingness to switch).
- **EBITDA bands:** `$3M+` EBITDA is preferred. `$750K-$3M` EBITDA is reviewable when recurring revenue, cohort durability, or service criticality is strong. `<$750K` EBITDA is below the current lower bound unless Kay explicitly asks for a special-case review.
- **Hard no categories:** retail and restaurants are hard no unless Kay explicitly reverses this in CIO review.
- **Behavioral rule:** do not auto-reject a broker/platform opportunity solely because EBITDA is below `$3M` if it is at least `$750K` and has strong recurring/reoccurring revenue, cohort/customer durability, or service-criticality evidence. Route it to `BROKER-OPPORTUNISTIC` or `FLAG` with the key signals preserved.
- **Formal docs:** the Drive buy-box docs remain the durable source of truth. If a Drive doc conflicts with this calibration, log the conflict in the artifact and preserve the item for CIO review rather than silently discarding it.
```bash
gog docs cat 14hf5QaKtcP_Um0u_P0LZyUM_zvv7haWVVkgGmRL9iyc -a kay.s@greenwichandbarrow.com > /tmp/buybox-services.txt
gog docs cat 1lkxntRwn3FOPXig86qF36eNyUS0BfbMumfNuIyInD-M -a kay.s@greenwichandbarrow.com > /tmp/buybox-insurance.txt
gog docs cat 1I8r8w0FPJUepfBxM6HM7V_q4ibmitybIBF6w6sMQumU -a kay.s@greenwichandbarrow.com > /tmp/buybox-saas.txt
```
Parse each doc's financial bands, structural requirements, industry hard-excludes, and geography filters. Each doc begins with the Data Availability Rule — absence of a disclosed field never auto-rejects; it flags for review.

**Category routing — which buy-box applies to which listing:**
- Specialty Insurance Brokerage listings → Insurance Buy Box
- Vertical SaaS listings (any vertical) → SaaS Buy Box
- All other listings (pest, estate mgmt, coffee, art storage, art advisory, cleaning, or new-niche non-SaaS non-Insurance) → Services Buy Box
- **Broker-channel listings (per source `Type` in OPPORTUNISTIC table below)** → **Broker-Channel Buy Box** (PENDING BUILD per Kay 5/3 — geography window not yet locked; until built, broker-channel listings still route to the matching Services/Insurance/SaaS buy-box above and are screened against it).

**Channel-type routing (per Kay 5/3 — pending broker buy-box build):**

The Sourcing Sheet's `Type` field is recorded for each match for future routing. Once the Broker-Channel Buy Box doc is built (geography window + short criteria list per Kay's 5/3 spec), `OPPORTUNISTIC` channels will route there instead of the niche buy-box.

| Source Type | Status |
|---|---|
| `Marketplace`, `AI Marketplace`, `Private Deal Network` | STRICT — niche buy-box (current behavior) |
| `Email-only broker`, `Newsletter blast`, `Advisory + Deal Platform`, `Marketplace + Email`, `Email-only broker + Buyer Portal` | OPPORTUNISTIC — niche buy-box for now; will route to Broker-Channel Buy Box once built |
| `Strategic Acquirer`, `Industry Publication`, `News + Community`, `Advisory` (intel-only) | INTEL only — niche signals, no Slack ping |

CALIFORNIA soft-exclude per `feedback_no_california` applies on all modes — flag, don't auto-kill.

**Scraper routing — which fetch tool to use per source:**

Default: WebFetch. If WebFetch returns 403 / 401 / JS shell / Cloudflare challenge, route through `agent-browser` (installed via `npm i -g agent-browser && agent-browser install`). Known JS-shell / Cloudflare-blocked / 403 sources that MUST use agent-browser:

- businessesforsale.com — 403
- Any gated marketplace requiring login (Acquire, FE International, Axial, Kumo post-registration)

Command pattern for agent-browser scrapes:
```bash
agent-browser open "https://www.bizbuysell.com/businesses-for-sale/?industry=insurance-agency&min-price=1000000&max-price=10000000" \
  && agent-browser wait --load networkidle \
  && agent-browser snapshot -i > /tmp/bbs-listings.txt
```

For login-required sources: use `--profile ~/.deal-aggregator` to persist session across runs. First login is manual; subsequent scrapes auto-authenticate. State file set in `AGENT_BROWSER_ENCRYPTION_KEY` env var.

Stop hook: if agent-browser is not installed, log "BROWSER_AUTOMATION_UNAVAILABLE: {source} skipped, requires agent-browser install" in the scan artifact and continue. Do NOT silently drop the source — surface the gap.

1. Sub-agent visits each platform's listing page (via WebFetch OR agent-browser per routing above)
2. Scrape new listings since last scan (track by listing ID or date)
3. For each listing, extract every field the listing discloses: company description, industry, revenue (or ARR for SaaS / commission revenue for insurance), EBITDA, asking price, geography, operating history, ownership structure, employee count, recurring-revenue evidence, reoccurring/repeat revenue evidence, cohort/customer durability evidence, and service-criticality evidence
4. Determine category (Services / Insurance / SaaS) per routing above; apply the matching buy-box
5. Screen: for each buy-box criterion, either confirm pass (disclosed + passes), flag fail (disclosed + fails → auto-reject), or mark "not disclosed" (do not reject; flag for review)
6. Deal passes the gate if: no disclosed criterion fails AND no industry hard-exclude matches AND thesis or new-niche match exists
7. Two types of passing matches:
   - **Thesis match** — fits an active niche thesis from Step 0a. High priority.
   - **Buy-box match, new niche** — passes the buy-box gate but sits in an industry not on the active thesis list. Route to niche-intelligence as a discovery signal.
8. Broker/platform listings that clear disclosed financial/structural gates but do not match an active thesis corpus become `BROKER-OPPORTUNISTIC`, not generic `NEAR-MISS`, when the source type is broker/platform/opportunistic and no hard-exclude applies. Also route `$750K-$3M` EBITDA listings to `BROKER-OPPORTUNISTIC` or `FLAG` when they show strong recurring/reoccurring revenue, cohort/customer durability, or service-criticality signals and are not retail/restaurants.

**Slack notification — ONE per deal (FINGERPRINT CHECK REQUIRED FIRST):**

Before every Slack send, compute the listing fingerprint and check the cross-day dedup store:

```bash
FP=$("$WORKDIR/scripts/deal-aggregator-fingerprint.sh" hash "$INDUSTRY" "$REVENUE_BAND" "$GEOGRAPHY")
STATUS=$("$WORKDIR/scripts/deal-aggregator-fingerprint.sh" check "$FP")
if [ "$STATUS" = "DUP" ]; then
  # Skip Slack; already posted within last 30 days
  continue
fi

# NEW listing — post to Slack then append fingerprint
curl -s -X POST "$SLACK_WEBHOOK_ACTIVE_DEALS" \
  -H "Content-Type: application/json" \
  -d '{"text":"🔔 Deal match\nSource: {Platform or Broker}\nCompany: {Name or blind profile}\nIndustry: {Industry description}\nRevenue: {Revenue} | EBITDA: {EBITDA} | Margins: {margin%}\nGeography: {Geography or \"Not disclosed\"}\nMatch type: {Thesis match / Buy-box match, new niche}\nTeaser:\n{Link to listing or teaser document}\n\n👍 = pursue  |  👎 = pass"}'

"$WORKDIR/scripts/deal-aggregator-fingerprint.sh" add "$FP" "$SOURCE" "$LISTING_URL" "$INDUSTRY" "$REVENUE_BAND" "$EBITDA_BAND" "$GEOGRAPHY"
```

Fingerprint helper: `scripts/deal-aggregator-fingerprint.sh` (hash | check | add). Store: `brain/context/deal-aggregator-fingerprints.jsonl`. TTL: 30 days.

**CRITICAL: Each deal gets its own Slack message.** Kay and her analyst react individually.

**NO COMMENTARY IN SLACK POSTS.** Team channels (#active-deals, #strategy-active-deals) get raw deal facts only — no analyst notes, no filter gating ("would need Jake/Adam SaaS filter"), no motivation reads ("seller is 'curious' not 'exploring'"), no thesis framing. Internal reasoning belongs in terminal dialogue with Kay, not in team-facing Slack. The `👍/👎` workflow IS the commentary channel — Kay and her analyst discuss via reactions, not via pre-written notes in the post.

**Morning briefing:** Report count only: "deal-aggregator — {n} new deals posted to Slack". Kay reviews deals on Slack, not in the briefing.

### Channel 2: Email Inbound
Read `brain/context/email-scan-results-{date}.md` for deal-related emails classified by email-intelligence.

**What to surface:**
- CIMs received (any industry) — immediate Slack notification
- Broker blast emails with specific deals matching buy box or thesis
- Direct broker emails with deal teasers or blind profiles
- NDA requests or follow-ups on previously flagged deals

**What to skip:**
- Newsletter content (market commentary without specific deals)
- Broker marketing (capability presentations, tombstones)
- Deals already flagged from platform scanning (dedup by company name/description — see Cross-Day Deduplication below)

### Cross-Day Deduplication (background, not surfaced to Kay)

Implemented via `scripts/deal-aggregator-fingerprint.sh` (hash | check | add). Store: `brain/context/deal-aggregator-fingerprints.jsonl` — append-only JSONL, 30-day TTL.

**Fingerprint rule:** `company_hash` = SHA-1 of normalized (industry | revenue_band | geography). Two listings with the same hash = same deal, regardless of source.

**Every Slack notification call site MUST use the helper:** see the Slack notification block above. No direct `curl` to the webhook without a prior `check` call. Hard requirement — duplicated Slacks erode signal.

**Exposure:** Runs silently. Never surface dedup activity in the morning briefing or Slack. It's hygiene, not a feature.

### Afternoon Run (`--afternoon` flag)

The skill runs twice on weekdays: 7:30am ET (morning, full run — after email-intelligence's 7am artifact lands) and 2pm ET (afternoon, top-up run). The Codex/systemd wrapper passes `--afternoon` for the second timer.

**Morning run (default, no flag):**
- Full Channel 0a/0b/0c load
- Full scan of all accessible platforms (Channels 1 + 3)
- Read `email-scan-results-{date}.md` (email-intelligence 7am run has completed)
- Write `brain/context/deal-aggregator-scan-{date}.md`

**Afternoon run (`--afternoon`):**
- Re-read buy-boxes + active niches (in case Kay edited during the day)
- Rescan ONLY the email-driven channels (Channel 2) + time-sensitive non-SaaS platforms (Rejigg, Everingham & Kerr afternoon blasts)
- Check fingerprint store for any deals that landed after morning run
- Write `brain/context/deal-aggregator-scan-{date}-afternoon.md` (separate artifact, do NOT overwrite morning)
- Slack notify new (non-fingerprinted) matches
- Lightweight — skip full Channel 1 + 3 scans; morning run already covered those

### Channel 3: Industry-Specific Deal Sources

Scan niche-specific platforms and brokers that specialize in the active thesis industries.

**Premium Pest Management:**
- PCO Bookkeepers & M&A Specialists (pcobookkeepers.com) — Advisory only, Dan Gordon (CPA), $1B+ in sell-side transactions. Monitor newsletter/blog.
- Keystone Business Advisors (keystonebusinessadvisors.com/business-listings/) — Registration required. Pest control up to $50M revenue.
- Cetane (cetane.com/industries/pest-control/) — Lower middle market M&A advisory, no public listings.
- DealFlow Agent (dealflowagent.com/home-services/pest-control) — landing page only (4/21: no live seller listings, marketing-buyer-counts only). Intel source, not live flow.
- Anticimex (us.anticimex.com/selling-your-business/) — Strategic acquirer, market intelligence only.

**Specialty Insurance Brokerage:**
- Sica Fletcher (sicafletcher.com/announcements) — #1 insurance M&A advisory, JS-rendered, relationship-only.
- MarshBerry (marshberry.com) — Investment banking + consulting for insurance, relationship-gated.
- Reagan Consulting (reaganconsulting.com) — Insurance M&A advisory, no public marketplace.
- Agency Checklists (agencychecklists.com) — Tracks insurance M&A transactions quarterly, public, scrapable.

**Estate Management Companies:**
- Exit Strategies Group (exitstrategiesgroup.com/propertymanagement/) — Property management M&A advisory, sell-side focused.
- Synergy Business Brokers (synergybb.com/businesses-for-sale/real-estate-businesses-for-sale/) — Real estate management listings, publicly browsable.

### Channel 4: Association Deal Boards

Monitor for off-market opportunities through industry associations.

**Pest Management:**
- NPMA (npmapestworld.org) — 5,000 members. Monitor newsletters and PestWorld conference for transition announcements.
- State PMAs — Check state-level pest management associations for classified sections.

**Insurance:**
- IIABA / Big I (independentagent.com) — Agency perpetuation planning resources, member network transitions.
- State insurance agent associations — classifieds and transition programs.

**Estate Management:**
- IREM (irem.org) — Institute of Real Estate Management, member networking.
- NARPM (narpm.org) — National Association of Residential Property Managers, occasional member transitions.

### Channel 6: DealsX Proprietary Outreach Replies

DealsX runs cold outreach on G&B's behalf (Sam's team owns the contact universe). When an owner replies with interest, DealsX forwards a lead notification. These are **inbound deal flow** — surface them; they count toward the daily 1-3 evaluable-deals target and show the DealsX funnel is producing.

**Detection — a DealsX reply notification is any email matching ALL of:**
- Sender is `Prospect Geni <dealsx.notifaction@gmail.com>` (the DealsX lead-notification sender; "Prospect Geni" is DealsX's notification alias, NOT a person or separate tool), OR a forwarded reply from `@dealsx.io` referencing a DealsX-sent thread
- Subject contains `Lead Interested` (current notification template) OR is a forwarded owner reply to DealsX outreach
- Read these from `brain/context/email-scan-results-{date}.md` (email-intelligence classifies them; this skill does not scan Gmail directly per the existing scanning rule)

**Notification structure (calibration reference, current template):** plain-text, ONE lead per notification, fields = Lead Name, Lead Email, Lead Website, Lead LinkedIn. No deal financials, no teaser, no CIM — it is a contact handoff, not a packaged deal. Treat each lead as a deal-flow signal to surface, not a screened buy-box match.

**Routing (per `feedback_dealsx_is_cold_email_infra` + `feedback_dealsx_skip_target_discovery`):**
- Surface as inbound deal flow only. Do NOT screen against the buy-box gate (no financials disclosed — Data Availability Rule means it would flag-not-reject anyway, so screening adds no value here).
- Do NOT trigger target-discovery, list-builder, or any refill action. DealsX owns the contact universe; a reply is not a pipeline-empty signal.
- Do NOT enter into Attio (pipeline-manager owns Attio on NDA, same as every other channel).
- One Slack message per lead to `#active-deals` (same fingerprint-dedup discipline as Channel 1, fingerprint on `dealsx | {company-domain}`):
```
🔔 DealsX reply — owner responded to outreach
Lead: {Lead Name}
Company: {Lead Website}
Contact: {Lead Email} | {LinkedIn or "—"}
Source: DealsX Proprietary Outreach
Note: inbound contact handoff — no financials yet. Voice-sensitive reply design is Kay's call.

👍 = pursue  |  👎 = pass
```
- These count toward the daily evaluable-deals volume and appear in the results file under a dedicated section (see Results File).

### Channel 5: New Introductions
When Kay receives a broker introduction (detected via email-scan-results).

1. **Detect** — Read email-scan-results for introduction signals
2. **Research** — Visit broker's website. Assess: searchable platform? Industries? Deal sizes? Relevant to active theses?
3. **Add to system:**
   - Create entity in `brain/entities/{slug}.md`
   - Add to Intermediary Target List Sheet (`18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`)
   - If scrapable → add to scanning rotation
   - If email-only → classify as email-only intermediary
4. **Draft response** — Gmail draft only (`gog gmail drafts create --account kay.s@greenwichandbarrow.com --gmail-no-send ...`): short, warm, offer NDA, don't over-explain. NEVER send, draft-send, forward, or autoreply.
5. **Update this skill** — Add new platform to scanning list if applicable

**Classify new intermediaries:**
- **Platform** → "Register as buyer on their site"
- **Boutique** → "Send broker intro email to managing director"
- **Industry specialist** → "Introduce as buyer in their specialty"
- **Association** → "Research membership and deal flow programs"

**Track registration:** After Kay registers or sends broker email, watch for deal flow within 4 weeks. Flag if no flow after 4 weeks.
</channels>

<niche_signals>
## Niche Signal Detection

Every listing scanned generates data. Track patterns:

### Thesis Validation
- Multiple listings in same niche across brokers → market exists and businesses trade
- Listing prices and multiples → market comp data
- Geographic clustering → regional opportunities

### New Thesis Discovery
- Listing fits buy box but in unscreened niche → create `brain/inbox/` item for niche-intelligence
- Recurring industry across platforms → possible consolidation wave
- Format: "Broker signal: {n} {industry} businesses listed in past {period} across {platforms}. Average: ${revenue} revenue, ${EBITDA} EBITDA. Consider for screening?"

### What NOT to signal
- One-off listings in random industries
- Listings obviously outside buy box (PE-backed, $100M+ revenue, franchise)
- Duplicate listings across platforms
</niche_signals>

<folder_management>
## ACTIVE DEALS Folder Management

**Normal flow (email-based):**
1. Deal-aggregator flags match → Slack ping to Kay
2. Kay signs NDA (on platform or via email)
3. Broker emails NDA confirmation and/or CIM
4. Pipeline-manager detects email, creates ACTIVE DEALS folder, files documents, creates Attio entry at "NDA Signed"

**Edge case (platform-only unlock):**
1. Kay signs NDA on platform → no email sent
2. Kay creates folder manually in ACTIVE DEALS
3. Pipeline-manager overnight scan detects new folder, creates Attio entry
</folder_management>

<results_file>
## Results File

**REQUIRED after every run.** Write to `brain/context/deal-aggregator-scan-{YYYY-MM-DD}.md`:

```markdown
---
date: {YYYY-MM-DD}
deals_found: {n}
sources_scanned: {n}
sources_blocked_verified: {n}
sources_blocked_single_attempt: {n}
email_deals: {n}
dealsx_replies: {n}
broker_opportunistic: {n}
email_scan_status: {live|missing|cached|late_recovered}
---
# Deal Aggregator Scan — {date}

## Deals Surfaced (sent to Slack individually)
1. **{Company/Profile}** — {Source} | {Revenue} | {EBITDA} | {Match type} | {Link}

## Email Inbound Deals
1. **{Company/Profile}** — {Broker} | {Type: CIM/Teaser/Blast} | {Details}

## DealsX Proprietary Outreach Replies
Inbound owner replies to DealsX cold outreach (Channel 6). Contact handoffs — no financials. Surfaced to Slack, count toward daily volume, do NOT trigger target-discovery.
1. **{Lead Name}** — {Lead Website} | {Lead Email} | {LinkedIn or "—"}

## Broker Opportunistic Review
Financially plausible broker/platform listings that do not match an active thesis corpus. Artifact-only by default; use this lane for CIO review and corpus/source tuning.
1. **{Company/Profile}** — {Source} | {Revenue} | {EBITDA} | {Industry} | Key signals: {recurring/cohort/criticality} | Why it matters | {Link}

## Near Misses (not Slacked)
- {listing} — {reason not flagged}

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens (e.g. broker-buy-box reruns, dual-filter retroactive replays) a 5-minute query instead of a 90-minute artifact-mining exercise. Aggregate counts in Source Scorecard tell you HOW MANY listings each source produced; this section tells you WHICH listings and WHY each was tagged the way it was.

Required when ≥ 1 listing was reviewed. If zero listings were reviewed (every source blocked), emit the table header only, with no data rows. Sort: PASS first, then NEAR-MISS, then FLAG, then HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| {Source} | {Listing headline or blind-profile descriptor} | {state, or "undisclosed"} | {Revenue or "undisclosed"} | {EBITDA or "undisclosed"} | {Margin% or "undisclosed"} | {Industry per listing} | {recurring/reoccurring revenue / cohort durability / service criticality / "not disclosed"} | {PASS / BROKER-OPPORTUNISTIC / NEAR-MISS / HARD-REJECT / FLAG} | {one-line reason if not PASS, else blank} |

Verdict definitions:
- `PASS` — clears buy-box gate AND matches an active niche corpus. Slack-posted (subject to fingerprint dedup).
- `BROKER-OPPORTUNISTIC` — clears disclosed financial/structural gate from a broker/platform/opportunistic channel, has no hard-exclude, but no active-niche corpus match; OR sits in the `$750K-$3M` EBITDA review band with strong recurring/reoccurring revenue, cohort/customer durability, or service-criticality signal. Artifact-only, not Slack-posted by default.
- `NEAR-MISS` — partially promising, sparse, or useful for thesis/corpus tuning, but not enough for pass or broker-opportunistic review.
- `HARD-REJECT` — fails buy-box on a disclosed-and-failed criterion, hits an industry hard-exclude, or geography hard-excluded.
- `FLAG` — undisclosed-field heavy or ambiguous; logged for human review without auto-rejection.

Forbidden: do not summarize listings into aggregate counts only. Every listing that was scraped or parsed gets one row in the Listings Reviewed log.

## Source Scorecard

Every source scanned this run MUST appear as a row — no exceptions. Missing rows = scan agent skipped a source and the run fails its stop hook.

Dashboard source categories are intentionally limited to three audience-facing buckets:
- `Marketplace` — searchable listing sites or buyer platforms the skill scrubs directly.
- `Newsletter` — recurring broker/platform blasts, saved-search alerts, or membership digests parsed from email.
- `Direct email` — any intermediary, broker, advisor, or contact email addressed to Kay with a particular deal reference.

Manual deal-source work is separate from reviewed sources. Only marketplace-style sources that require login, setup, registration, or manual search should appear in the manual queue; direct relationship/email sources should not be shown as manual marketplace work.

Dashboard deal status is binary for Kay: `Matches` = PASS rows; `Filtered out` = every non-PASS row, including broker-opportunistic, near-miss, flag, and hard-reject. Keep internal lanes in artifacts if useful for calibration, but do not expose a separate borderline/learning metric on the dashboard.

Every `auto/deal flow` source observed in the current-week email artifact must be accounted for in Source Scorecard unless it is explicitly paused. Current active email/newsletter/direct sources that must not disappear from dashboard coverage: BizBuySell, BizQuest, BizScout, Calder Capital, DealForce / Generational, Transworld Business Advisors, Everingham & Kerr, Business Exits, Baton, Axial, DealsX replies, and direct intermediary forwards. Current paused/ignored sources: Flippa, Quiet Light / quietlight.com, Website Closers / websiteclosers.com, and SMB Deal Hunter. If an observed active sender has zero listing rows, include a scorecard row with `Listings Reviewed: 0` and a status reason rather than letting the source vanish.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | Marketplace | active | 200 | 12 | 0 | 2026-04-14 |
| BizBuySell | Newsletter | active email/newsletter | — | email-derived | 1 | 2026-04-22 |
| Quiet Light | Marketplace | dormant | — | 0 | — | — |
| Sica Fletcher | Marketplace | active | 200 | 8 | 0 | 2026-04-18 |
| (… one row per source in Sourcing Sheet "Active" status …) | | | | | | |

**Status values:**
- `active` — source fetched successfully, listings parsed
- `blocked (verified)` — primary fetch failed AND fallback fetch failed (two attempts). Source is genuinely dark.
- `blocked (single-attempt)` — primary fetch failed, fallback not attempted. Surface for manual retry on next run.
- `login-gated` — registered but session expired; surface to Kay for re-auth
- `dormant` — marked Dormant on Sourcing Sheet; not scanned this run

**Data sources for the scorecard:**
- `Matches` and `Last Match Date` — queried from `brain/context/deal-aggregator-fingerprints.jsonl` filtered by source + date
- `Listings Reviewed` — counted by the scan agent per source (every listing parsed, whether matched or not)
- `Status` and `HTTP` — logged by the scan agent at fetch time

## Volume Check
- Deals surfaced today: {n}
- Broker-opportunistic review items: {n}
- 7-day rolling average: {n}
- Target: 1-3/day — {ON TRACK / BELOW TARGET / ABOVE TARGET}
- Email leg: {live|missing|cached|late_recovered}
- Funnel bottleneck: {source coverage / email leg / screening strictness / source quality / healthy}
```
</results_file>

<weekly_digest>
## Weekly Source-Productivity Digest (Phase 2)

**Retired as a separate scheduled run 2026-06-19.** Weekly/source-productivity review is folded into the single weekday morning deal-aggregator artifact and Good Morning review. Manual `/deal-aggregator --digest-mode` remains available for forensic/source-review work, but no Friday timer should run it automatically.

**Purpose:** Give Kay a single weekly artifact to decide which sources are earning their slot, which new sources should be added, and which should be retired. No auto-writes — proposals are approval-gated.

**Reads:**
- Last 7 days of `brain/context/deal-aggregator-scan-{date}.md` (daily scorecards)
- Last 30 days of `brain/context/deal-aggregator-fingerprints.jsonl` (source → match attribution)
- Last 7 days of `brain/context/email-scan-results-{date}.md` (inbound broker/newsletter signals for scouting)
- `G&B Deal Aggregator - Sourcing List` sheet (ID `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw`) — General Sources + Niche-Specific Sources tabs

**Writes:**
- `brain/trackers/weekly/{YYYY-MM-DD}-deal-aggregator-digest.md` — single artifact, schema-validated
- Slack ping to `SLACK_WEBHOOK_OPERATIONS` ONLY when ≥1 proposed change OR volume = 🔴 (silence = healthy, per health-monitor convention)

### Digest File Format

```markdown
---
date: {YYYY-MM-DD}
type: tracker
title: "Deal Aggregator Weekly Digest — {date}"
window_start: {YYYY-MM-DD}
window_end: {YYYY-MM-DD}
volume_7d_avg: {float}
volume_status: {✅ / ⚠️ / 🔴}
proposed_additions: {n}
proposed_retirements: {n}
tags: [date/{YYYY-MM-DD}, tracker, topic/deal-aggregator, topic/weekly-digest]
---

# Deal Aggregator Weekly Digest — {date}

## 1. Source Productivity (Last 7 Days)

| Source | Category | 7d Matches | 7d Listings Reviewed | Last Match | Trend |
|--------|----------|-----------:|---------------------:|-----------|:-----:|
| … | … | … | … | … | ↑ / ↓ / → |

Trend arrow: compare this week's match count to prior week's (prior digest file or prior 7-day window of fingerprints). `↑` = +50% or more, `↓` = -50% or more, `→` = within ±50%.

## 2. Volume Check

- 7-day rolling average: {n}/day
- Target: 1–3/day
- Status: {✅ On track / ⚠️ Below target / 🔴 Critical}
- Email leg health: {live/missing count over scheduled days}
- Broker-opportunistic items: {n} this week, with top themes
- Source blockers: {blocked verified/single-attempt/login-gated}
- Funnel diagnosis: {source coverage / email leg / screening strictness / source quality / healthy}

## 3. Proposed Additions

(From Source Scout subagent — see spec below.)

1. **{Source name}** — {category} | {URL}
   - Why: {signal that surfaced it — newsletter mention, inbound email, niche-broker reference}
   - Recommended tab: {General Sources / Niche-Specific Sources → {niche}}
   - Access: {Free / Register / Relationship-only}
   - **RECOMMEND: Add to {tab}** → YES / NO / DISCUSS

## 4. Proposed Retirements

1. **{Source name}** — {category} | 0 matches since {date} | Last verified alive: {date}
   - Why: {30+ days no match, still-alive verified, not earning its slot}
   - **RECOMMEND: Move to Dormant on Sourcing Sheet** → YES / NO / DISCUSS

## 5. Recommended Actions (Kay's Review Bucket)

Summary list — 1 line per proposal with its YES/NO/DISCUSS for quick approval. Include source additions/retirements, email-leg fixes, browser-fallback fixes, and broker-opportunistic corpus/source tuning. On YES for source-sheet changes, Codex writes the change to the Sourcing Sheet; on NO/DISCUSS, no write.
```

### Source Scout Subagent

Spec: runs inside the Friday digest only. Not invoked during daily scans (would add scan-time cost to a skill already taking ~44 min).

**Scouting side (new-source discovery):**
1. Read last 7 days of `brain/context/email-scan-results-{date}.md` — enumerate all sender domains in the inbox window.
2. Cross-reference each sender domain against the Sourcing Sheet General + Niche tabs.
3. For every sender domain NOT on the Sourcing Sheet:
   - Filter out known non-source senders (personal domains, internal `@greenwichandbarrow.com`, calendar/reminder noise)
   - Classify the remaining: broker platform, M&A advisory, newsletter, industry publication
   - Web-verify the URL resolves (`gog webfetch` or agent-browser if blocked)
   - Propose: `{source_name, url, category, recommended_tab, rationale, evidence_message_id}`
4. Additionally, scan newsletter body text for AI-marketplace launches and niche-broker names mentioned by industry publications (Agency Checklists → insurance, IA Magazine → insurance, NPMA → pest, IREM → estate mgmt, CMM Online → cleaning).

**Retirement side (stale detection):**
1. For every source on the Sourcing Sheet with `Status: Active`:
   - Query `brain/context/deal-aggregator-fingerprints.jsonl` — when was the last match attributed to this source?
   - If no match in 30+ days → candidate for retirement
2. Before flagging a candidate, verify the source is still alive:
   - URL resolves (GET 200)
   - Domain still registered (no NXDOMAIN)
   - For email-only sources: Gmail query for recent emails from the domain — if silent in last 30 days, reinforce retirement signal; if active, re-classify as "active but no buy-box matches" (keep, don't retire)
3. Per `feedback_test_before_concluding_channel_dead`: Sica Fletcher was mis-labeled 404 for days in April. Any retirement proposal must show the three live-checks passed or document which one failed.

**Never auto-writes to the Sourcing Sheet.** All outputs go into the digest vault file. Kay approves in Friday briefing (or via direct reply to the Slack ping) → that approval triggers the sheet write in a separate invocation.

### Sourcing Sheet Write (Post-Approval Only)

After Kay approves a proposed addition or retirement:
- **Addition:** Append a row to the appropriate tab (General Sources or Niche-Specific Sources) with columns: Status, Source, Type, Access, URL, Notes (+ Niche for Niche tab). Status = "Active" for additions.
- **Retirement:** Update the existing row's Status column to "Dormant". Do NOT delete rows — preserves history.
- Trace: write an entry to `brain/traces/{date}-deal-aggregator-source-change.md` using trace schema (schema_version 1.1.0, inline array tags per `feedback_trace_schema_format`).
- Pre-write snapshot of the sheet stored per `feedback_subagent_sheet_write_safety` — enables rollback if a write clobbers an unintended row.
</weekly_digest>

<wrapper_hardening>
## Wrapper Hardening (POST_RUN_CHECK)

Per `feedback_mutating_skill_hardening_pattern.md`, every scheduled mutating skill ships with a wrapper-level integrity validator. Deal-aggregator now has one scheduled mode wired into `scripts/run-agent-skill.sh`:

| Mode | Headless prompt | Validator command (POST_RUN_CHECK) |
|------|-----------------|-------------------------------------|
| Morning (`deal-aggregator:`) | `headless-morning-prompt.md` | `python3 scripts/validate_deal_aggregator_integrity.py --mode morning --date $TODAY` |

Retired modes (`--afternoon`, `--digest-mode`) remain manual/forensic only and must not be enabled as systemd timers. The duplicate scheduled modes caused dashboard/status overwrites and Good Morning communication mismatch.

**What the validator checks:**
- Today's artifact exists at the expected path (morning / afternoon / digest)
- File size ≥ 200 bytes (catches empty stubs)
- YAML frontmatter is present and well-formed, with `date:` matching the run date
- All required section headers are present (6 daily sections from 2026-05-04 afternoon onward — date-gated; previously 5 / 5 digest sections)

**Failure path:** Validator non-zero → wrapper overrides skill exit code → Slack alert posts to `SLACK_WEBHOOK_OPERATIONS` with "VALIDATOR FAILED" prefix. This catches the silent-success failure mode where Codex exits 0 without writing the artifact (4/27 + 4/30 morning incidents — the run emitted operator-question framings instead of executing, exited cleanly, and the absence was only noticed when the afternoon top-up flagged "morning artifact missing").

Wired 2026-05-02 during the legacy launchd-debugger investigation; now enforced by the Codex/systemd runner. Pattern source: `memory/feedback_mutating_skill_hardening_pattern.md`.
</wrapper_hardening>

<stop_hooks>
## Sub-Agent Stop Hooks

### Scan Stop Hook
- [ ] Step 0b completed: all three buy-box docs were freshly read from Drive this run (Services, Insurance, SaaS). Cached or hardcoded bands = hard fail.
- [ ] Step 0c completed: keyword corpus resolved for EVERY active niche. For any niche where the WEEKLY REVIEW "DealsX Niche" field is blank, the corpus was built from the WR row itself (Niche Hypothesis + Quick notes + other populated fields). Niche-name-alone matching is NOT acceptable when other WR row data is available. This is a hard requirement.
- [ ] Step 0d completed: latest Niche Intelligence `New` rows / sidecar were loaded as watchlist corpus. Watchlist matches must be logged as `new-niche-watchlist: {niche}` and are not PASS/Slack eligible unless Kay separately promotes the niche to active.
- [ ] Every match includes: source, listing URL, company description, industry, revenue/EBITDA (or "not disclosed"), geography
- [ ] Listing URL is a working link (not a search results page or homepage)
- [ ] Each listing routed to the correct buy-box category (Services / Insurance / SaaS) per the routing rule
- [ ] Data Availability Rule enforced: no listing auto-rejected on a missing field. Auto-reject only triggers on disclosed-and-below or disclosed-and-failed criteria.
- [ ] Industry hard-excludes applied per the matching buy-box doc (Services / Insurance / SaaS)
- [ ] Match classified as "Thesis match" or "Buy-box match, new niche"
- [ ] No duplicate listings (dedup across platforms AND email inbound)
- [ ] Zero matches = report "No matches" — never fabricate
- [ ] Scan artifact logs, for each niche, which corpus path was used: "DealsX keywords" or "WR row enrichment (Niche Hypothesis + Quick notes)" — so underperforming niches can be calibrated next cycle
- [ ] Broker-opportunistic lane populated for financially plausible broker/platform listings that do not match active niche corpus but have no hard-exclude.
- [ ] `brain/context/deal-aggregator-status.json` written for dashboard consumption.

### Source Scorecard Stop Hook (Phase 2)
- [ ] The run artifact separates source coverage into two concepts: (1) automated run coverage — sources the skill actually scrubs or reads from email when it runs, categorized only as Marketplace, Newsletter, or Direct email; (2) Manual deal sources to aggregate — marketplace-style sources that require login, setup, registration, or manual search. Direct relationship/email sources do not belong in the manual marketplace queue. Do not blend these into one source list.
- [ ] Every source with `Status: Active` on the Sourcing Sheet has a row in the scan artifact's `## Source Scorecard`. Row count = Active row count on the sheet. Mismatch = scan agent skipped a source → hard fail.
- [ ] No source marked `blocked` without a verification second-attempt. If only one fetch attempt was made, the status MUST be `blocked (single-attempt)`, NOT `blocked (verified)`. Precedent: Sica Fletcher mis-labeled 404 for days in April 2026 — `feedback_test_before_concluding_channel_dead` exists specifically to prevent this.
- [ ] `Matches` and `Last Match Date` columns pulled from the fingerprint JSONL, not fabricated. If fingerprint store is empty for a source, `Matches` = 0 and `Last Match Date` = "—".

### New Introduction Stop Hook
- [ ] Entity created in vault with proper schema
- [ ] Intermediary Target List Sheet entry
- [ ] Website researched and scrapability assessed
- [ ] Draft response in Gmail draft-only mode (`gog gmail drafts create --account kay.s@greenwichandbarrow.com --gmail-no-send ...`) — short, warm, offers NDA; never send

### Friday Digest Stop Hook (Phase 2)
- [ ] Digest file exists at `brain/trackers/weekly/{YYYY-MM-DD}-deal-aggregator-digest.md`
- [ ] All 5 required sections present: Source Productivity, Volume Check, Proposed Additions, Proposed Retirements, Recommended Actions
- [ ] Each proposed addition includes rationale + recommended tab + access method
- [ ] Each proposed retirement includes 3 live-check results (URL resolves, domain registered, email channel status)
- [ ] Trend column populated via prior-week comparison (not fabricated)
- [ ] Slack notification sent ONLY IF ≥1 proposed change OR volume status = 🔴. Silent digest on a healthy week = correct behavior.
- [ ] No auto-writes to the Sourcing Sheet — all proposals await Kay's approval
</stop_hooks>

<validation>
## Validation

### Daily Check
- [ ] All accessible platforms scanned
- [ ] Email inbound deals from email-scan-results processed
- [ ] Matches sent to Slack individually with links
- [ ] Results file written with volume check
- [ ] Dashboard status JSON written with email leg status, blocked-source counts, broker-opportunistic count, and needs-attention list

### Weekly
- [ ] Niche signals compiled and sent to niche-intelligence
- [ ] Platform scanning status (any sites changed/blocked?)
- [ ] Volume trend: are we hitting 1-3/day? If not, identify gaps and expand sources.

### Guardrails
- **Never contact an owner directly** on a broker-sourced deal. Always go through the broker.
- **Buy-box filter criteria come from the three Drive docs plus Kay's current calibration above.** The Drive docs are the durable criteria store; if they conflict with Kay's latest calibration, log the conflict and preserve the item for CIO review rather than silently dropping it.
- **Data Availability Rule is absolute.** A listing that doesn't disclose a field is never auto-rejected on that field. Flag for review, continue scoring against disclosed fields.
- **Hard-excludes apply per the matching buy-box doc's Industry Hard-Excludes section, when disclosed on the listing.** No external lists, no blacklists maintained — scope is pass-through review of existing deals only.
- **Retail and restaurants are current hard no categories.** Do not preserve them for broker-opportunistic review unless Kay explicitly asks for a special-case look.
</validation>

<success_criteria>
## Success Criteria

### Phase 1 (Current — get volume flowing)
- [ ] All accessible platforms scanned daily
- [ ] Email inbound deals surfaced same-day
- [ ] Industry-specific sources scanned for each active niche
- [ ] Slack notifications working with thumbs up/down workflow
- [ ] Results file written daily with volume tracking

### Phase 2 (Source stewardship — landed 2026-04-22)
- [ ] Daily scan artifact includes `## Source Scorecard` with per-source match counts + listings reviewed + last match date
- [ ] Every "blocked" source was verified via a second fetch attempt before being marked `blocked (verified)`
- [ ] Friday 7:30 AM ET digest file written to `brain/trackers/weekly/{date}-deal-aggregator-digest.md` with all 5 sections
- [ ] Source Scout subagent surfaces proposed additions (from week's inbox/newsletter signals) and proposed retirements (30+ days no match + 3 live-checks passed)
- [ ] No auto-writes to the Sourcing Sheet — every addition/retirement awaits Kay's explicit approval
- [ ] Slack notification to `#operations` only when ≥1 proposed change OR volume = 🔴 (silent on healthy weeks)
- [ ] Rolling 7-day average trending toward 1–3 deals/day target

### Phase 3 (future — autonomous closed-loop)
- [ ] Kay's approval on a proposal triggers an immediate sheet write (no separate invocation)
- [ ] Source Scout proposals surface in Friday /goodmorning briefing directly, not a separate Slack ping
- [ ] Trend detection surfaces category-level insights ("niche-specific sources are 3× more productive this month than general platforms") to inform buy-box re-weighting
</success_criteria>
