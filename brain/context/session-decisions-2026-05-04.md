---
date: 2026-05-04
type: context
title: "Session Decisions — 2026-05-04"
tags: ["date/2026-05-04", "context", "topic/session-decisions", "topic/broker-channel-build", "topic/intermediary-templates", "topic/website-revamp"]
---

## Decisions

- **APPROVE** Phase 3 pipeline-manager surgery interpretation — 8 lines of Intermediary Pipeline residue removed; Active Deals list logic untouched.
- **APPROVE** USE-GOG-FALLBACK for `gmail-draft.sh` — gog already wraps Gmail API; wrapper script unnecessary.
- **APPROVE** BOTH-FIRE chain for CIM auto-trigger + auto-ack reply (internal Drive/Attio work + broker-facing reply).
- **APPROVE** new doctrine: ALL intermediary email drafts MUST originate from a canonical template (Intermediary Email Templates Doc OR Conference Engagement Templates Sheet). No ad-hoc body copy.
- **REJECT** visual signature embedding (logo card / buy-box graphic / both). One-pager attachment only (Megan Lawlor pattern).
- **APPROVE** new templates added to canonical Intermediary Email Templates Google Doc: CIM RECEIVED, THANK YOU, DAY 5 FOLLOW-UP, DECLINE POST-REVIEW, NDA SIGNED.
- **REJECT** Day 12 soft-close — cadence reduced from 3-touch to 2-touch (Day 0 + Day 5 only) for Brokers + IBs.
- **REJECT** "Need more info" path after CIM screen — too rare for broker engagement; replaced with "Move to owner call" pattern.
- **APPROVE** conference-engagement skill audit — already template-driven by design; added explicit doctrine reference.
- **APPROVE** capacity letter requests for Guillermo Lavergne + Jeff Stevens — surface in next meeting prep brief, no email beforehand.
- **APPROVE** Day 5 follow-up rewrite — collapsed 3 soft signals into single confident sentence ("Bumping my note to the top of your inbox. Would love to find 20 min whenever it works.").

## Actions Taken

- **UPDATED** `pipeline-manager/SKILL.md` — 8 Intermediary Pipeline residue lines surgically removed (532, 679-681, 703, 779-781, 807, 837, 859-863, 1212).
- **UPDATED** `pipeline-manager/SKILL.md` Step 5 added — CIM auto-ack chain pulls template from canonical doc via `gog docs export`. Hard gate: skip + warning if template not found, no ad-hoc fallback.
- **UPDATED** `pipeline-manager/SKILL.md` line 871-873 — "Need more info" replaced with "Move to owner call" (triggers deal-eval Phase 4 with `pending_owner_call: true`).
- **UPDATED** `pipeline-manager/SKILL.md` line 879 — "Pass" path now templated (DECLINE POST-REVIEW lookup from canonical doc).
- **UPDATED** `pipeline-manager/SKILL.md` line 1211 — `gmail-draft.sh` reference replaced with `gog gmail draft`. Thank-you path classified by recipient: intermediary→template-driven, non-intermediary→ad-hoc allowed.
- **UPDATED** `outreach-manager/SKILL.md` line 631 — master template doc ID updated from superseded `1_cNsAPC...` to live `1gTQoCb...`.
- **UPDATED** `outreach-manager/SKILL.md` line 651 — cadence rewritten: Brokers + IBs = 2-touch (Day 0 + Day 5), Lawyers + CPAs = ONE-AND-DONE.
- **UPDATED** `conference-engagement/SKILL.md` — added explicit doctrine reference enforcing template-only drafts.
- **UPDATED** `CLAUDE.md` pre-flight checklist — added intermediary template doctrine line with both canonical source IDs (Doc + Sheet).
- **CREATED** `memory/feedback_no_intermediary_drafts_outside_template.md` — doctrine memory, indexed in MEMORY.md.
- **CREATED** `memory/project_broker_email_one_pager_only.md` — visual signature decision, indexed in MEMORY.md.
- **CREATED** canonical Google Doc additions (3 PROPOSED batches via `gog docs write --append`): CIM RECEIVED + THANK YOU + visual sig note + doctrine note (round 1), THANK YOU template (round 2), Day 5 + DECLINE POST-REVIEW + NDA SIGNED (round 3).
- **UPDATED** canonical Google Doc — Day 5 body rewrite ("Bumping my note to the top of your inbox. Would love to find 20 min whenever it works.") via 3-step find-replace; THANK YOU header typo `{Brokers` → `(Brokers` fixed; CIM RECEIVED orphan close paragraph deleted via index-range `gog docs delete`.
- **UPDATED** `entities/guillermo-lavergne.md` — Pending Discussion Topics section added with capacity letter ask.
- **UPDATED** `entities/jeff-stevens.md` — Pending Discussion Topics section added with capacity letter ask.

## Deferred

- **DEFER** broker-channel one-pager creation to **2026-05-05** — Kay wants to pair with website iteration so they're aligned. Pre-existing draft already in Drive.
- **DEFER** 10 broker first-touch emails to **2026-05-05** — today's first 5 missed; expanding to 10 tomorrow. Apollo enrichment running tonight in parallel session.
- **DEFER** code-level PreToolUse stop hook for intermediary draft enforcement — sufficient layers exist (CLAUDE.md pre-flight + skill code template-gates + canonical-source mandatory lookups). Building a real PreToolUse hook would have high false-positive rate (recipient classification + template-source verification both stateful). Revisit if a doctrine violation actually slips through in practice.
- **DEFER** vault snapshot refresh of `brain/outputs/2026-05-04-broker-outreach-templates.md` — happens on /goodnight (Drive doc has 9 templates vs snapshot's 4).

## Open Loops

- Broker-channel one-pager file does not exist yet. Day 0 + Day 5 templates reference attachment that needs creation. Blocking for outreach if pipeline starts firing tomorrow morning before one-pager is built. **RESOLVED in iMac PM session — see below.**
- Broker list verification + Apollo enrichment status: verification DONE per Kay; Apollo enrichment running in another session tonight. Outcome lands tomorrow morning.
- 10 broker emails for tomorrow not yet drafted — will fire from outreach-manager Subagent 3 once enriched targets land.
- Capacity letter ask sits in Pending Discussion Topics for Guillermo + Jeff. Will surface in next meeting brief for each. No external action until then.

---

# iMac Terminal Session (PM) — Broker-Channel Build Day 1 Continuation

## Decisions

### Attio doctrine pivot
- **APPROVE** Attio is reserved for **Active Deal Flow Pipeline only.** Cold intermediary contacts (brokers, lawyers, CPAs, IBs, family offices, association heads) live in Google Sheets — not Attio. Drove deletion of the "Outreach: Intermediary Pipeline" Attio list (24 entries emptied + shell deleted by Kay in UI).
- **APPROVE** Surgical removal of WRITE-paths in `deal-aggregator` and `outreach-manager` skills + READ-paths in `email-intelligence`, `pipeline-manager`, `meeting-brief`, `weekly-tracker` (Phases 1 + 2 of the SKILL.md cleanup; Phase 3 covered by other session). All 6 skills now point at `Intermediary Target List` Sheet (`18zzE1y...`) as canonical.

### Cold-list engagement rule (refined)
- **APPROVE** Engagement = **two-way correspondence** (inbound reply / call logged / meeting held). Outbound-only emails with no reply do NOT count as engagement; the contact stays cold and the row stays on the list.
- Example calibrations: Choate → REMOVE (strong two-way thread, just stale). BDG-CPAs → KEEP (single Nov 2025 outreach, no reply). Transworld of NY (Sam Curcio) → KEEP (single 4/30 outreach, no reply). NYBB → KEEP (Attio record only, zero engagement).

### Intermediary classification rule (the M&A=broker doctrine)
- **APPROVE** Tab placement determined by firm's homepage **self-identification**, NOT by analyst-inferred deal-size band.
- **APPROVE** **"M&A Advisor" / "M&A Advisory" label = Brokers tab.** IB tab reserved only for firms self-IDing with explicit "Investment Bank" / "Investment Banking" label (typically FINRA/SIPC). This redefines the broker/IB split going forward.
- Concrete applications: Gottesman (M&A Business Brokers self-ID) → Brokers (revert from incorrect Batch B move). Mariner/Woodbridge ("Trusted M&A Advisors") → Brokers per the new rule. MergersCorp ("leading investment banking firm") → IB. MarshBerry (FINRA/SIPC + IB self-ID) → IB. 7 IBBA-credentialed M&A advisors (Touchstone, Pillai, GillAgency, IBG, Inbar, NorthBridge, Evergreen) STAY on Brokers.

### Other doctrine codifications
- **APPROVE** Numbered list counter NEVER resets within a thread. Ascends across all messages, never duplicates. Prefer bullets when unsure.
- **APPROVE** Kay's canonical title is **Founder & CEO** in all G&B deliverables. NOT Principal / Searcher / Managing Partner.
- **APPROVE** Geography is INTERNAL-only doctrine reinforced — never on external broker copy.
- **APPROVE** Aone Partners (Glelia) is a **negative reference** in SEARCHER RESOURCES — never model G&B copy on her published artifacts. Jeremy Black is the positive reference.
- **APPROVE** Megan Lawlor pattern confirmed — broker outreach attaches a one-pager + email; closes the broker-channel-build open question.
- **APPROVE** Deal-aggregator Blocked Sources tab created — reserved for fully-unreachable sources (no web AND no email AND no API). Web-blocked-but-email-active sources (Flippa, Quiet Light, Synergy) STAY on General Sources.
- **APPROVE** Goldman SFO consolidation: Stacy Mullaney is primary contact (Family Offices R23, warm-intro path via Kay's shared contacts), Chris Gleason restored as fallback (Family Offices R24, better-positioned for the actual ask).
- **APPROVE** BusinessSellerCenter.com / Kevin Murray restored to Brokers — Batch A delete was based on incorrect "listing platform" assumption; firm is a legitimate IBBA-credentialed broker.

## Actions Taken

- **DELETED** Attio Intermediary Pipeline list — 24 entries removed via MCP, shell deleted by Kay in Attio UI.
- **UPDATED** `deal-aggregator/SKILL.md` (5 edits) + `outreach-manager/SKILL.md` (3 edits) — Phase 1 writer-side cleanup. All Intermediary Pipeline writes now route to Sheet (`18zzE1y...`).
- **UPDATED** `email-intelligence/SKILL.md` (5 edits) + `pipeline-manager/SKILL.md` (6 edits) + `meeting-brief/SKILL.md` (1 edit) + `weekly-tracker/SKILL.md` (line 134 deleted + header adjustment) — Phase 2 reader-side cleanup.
- **UPDATED** `Intermediary Target List` Sheet (multi-batch): Batch A (6 hard deletes), Batch B (8 Brokers↔IB cross-tab consolidations), Batch C (3 cross-tab moves), engagement-based removals (16 firms / 24 row clears), Gottesman + Basso revert from IB→Brokers, BusinessSellerCenter restore, Mariner/MergersCorp/MarshBerry/Valuation Resource Group/Baldridge moves (in-flight). Final populated total: **187 rows** (down from 212 at validation start).
- **CREATED** Blocked Sources tab on `G&B Deal Aggregator - Sourcing List 4.21.26` — header schema + 2 initial entries (ProNova Partners, Biz Brokerage Hub). ProNova migrated off General Sources.
- **CREATED** `G&B Broker One Pager 5.4.26` Google Doc in BROKER SEARCH folder (`1cs_bLcCNd4V3md8uhDs-Q7vYqbQwhZZ9l4cLrgmppzM`) — criteria-forward layout, anti-PE framing (HOLD.co-borrowed), mission-critical-services line (SummitView-borrowed), explicit out-of-scope list (Ironia-borrowed), Founder & CEO title applied, no logo block (peer-norm). RESOLVES the prior session's open loop.
- **CREATED** `Searcher One-Pager Reference Research 5.4.26` Google Doc in SEARCHER RESOURCES folder (`160Ud-mIK3U3VkGVZ7kAYpe2Mu_MNNJaPPfF3nIHXpNY`) — 10 references benchmarked.
- **CREATED** validation artifacts: `2026-05-04-intermediary-target-list-validation.md` + `2026-05-04-intermediary-target-list-engagement-classification.md` + `2026-05-04-intermediary-list-self-id-verification.md` + `2026-05-04-broker-list-verification-flags.md` + `searcher-one-pager-research-2026-05-04.md`. All in `brain/outputs/` and `brain/library/external/`.
- **CREATED** rollback snapshots: `intermediary-target-list-batches-A-B-C-2026-05-04.json`, `intermediary-target-list-engagement-removals-2026-05-04.json`, `intermediary-target-list-final-moves-2026-05-04.json` (in-flight).
- **CREATED** memory files (8 new, all indexed in `MEMORY.md`):
  - `feedback_brokers_stay_in_sheet_until_reply.md`
  - `feedback_numbered_items_never_reset.md`
  - `feedback_kay_title_founder_ceo.md`
  - `feedback_cold_list_attio_engagement_rule.md` (refined twice — final form has two-way nuance)
  - `feedback_classify_intermediary_by_self_id.md` (refined — final form has M&A=broker rule)
  - `feedback_blocked_sources_tab_rule.md`
  - `feedback_aone_glelia_negative_reference.md`
  - `project_megan_broker_outreach_pattern.md`

## Deferred

- **DEFER** Apollo enrichment of contact-missing rows (`[no-contact-no-email]` flagged) → **first task tomorrow AM (2026-05-05)**, runs as part of /goodmorning. Decision: NOT scheduled overnight to avoid setting up a fresh launchd job at end-of-day with no one awake to course-correct if it errors. Apollo can fire as soon as Kay opens her morning session; results in 30-60 min, ready for AM review.
- **DEFER** Website ↔ one-pager co-design (Version A mirror / B layered / C gateway) — Kay processing; revisit tomorrow.
- **DEFER** Final review pass on broker one-pager content — Kay reviews `1cs_bLcCNd4V3md8uhDs-Q7vYqbQwhZZ9l4cLrgmppzM` tomorrow.
- **DEFER** Phone number on broker one-pager — `[phone]` placeholder per no-echo-PII rule; Kay populates directly when reviewing the Doc.

## Open Loops

- Final 5 IBBA-rule moves still completing in background subagent (Mariner, MergersCorp, MarshBerry, Valuation Resource Group, Baldridge). Will land before commit.
- Broker one-pager reviewed-and-approved status: Kay reviews tomorrow AM before pairing with first 10 broker emails.
- Apollo enrichment overnight job result + Sheet state delta — surfaces in tomorrow's morning briefing.
- Website + one-pager strategic alignment (Version A/B/C) — Kay's call pending.

---

# Website Revamp Session (PM-Evening) — Day 1 of 5-Day Squarespace Rebuild

Kay engaged Claude to rebuild greenwichandbarrow.com after a 5-month contractor failed to deliver. Site needs to be live by Fri May 8 to support the broker outreach push starting today. Three-phase pipeline executed: `/socrates` framing → `/plan` 5-day execution plan → Day 1 mockup with 3 iteration corrections.

## Decisions

### /socrates framing convergence
- **APPROVE** Audience: intermediary + owner-seller, credibility-after-outreach (NOT LP, NOT sourcing).
- **APPROVE** Structural anchor: full Shoreham Partners model. Founder NOT on the site at all (no name, no photo, no LinkedIn link, no About-Kay section).
- **APPROVE** Vehicle structure: CCV (Committed Capital Vehicle). Permanent-capital language defensible. Supersedes the existing memory `feedback_kay_ceo_deal_1_not_allocator` framing of Deal 1 as "search-fund traditional."
- **APPROVE** Thesis (Hoffman-register, niche-agnostic): "Critical service businesses that engage their community, deliver exceptional customer service, and earn their customers' trust."
- **APPROVE** Build path: HTML/CSS mockup off-platform, iterate via screenshot review, translate to Squarespace at end of week.
- **APPROVE** Squarespace stays as the platform — no migration to Webflow / custom.
- **APPROVE** Iteration cadence: coded prototype + screenshot-feedback cycle, 1-2 hr/day Kay review window in parallel with broker outreach.
- **APPROVE** Save discussion brief to `brain/outputs/2026-05-04-discussion-website-revamp.md` for clean `/plan` handoff.
- **REJECT** Kay-led / hybrid anchor variants. Kay clarified: "I want to not be on it." Pure Shoreham model locked.
- **REJECT** Salvage of contractor's WIP. Kay confirmed contractor delivered nothing visible; engagement terminated, no payment.
- **REJECT** Single-page modular scroll structure (initial framing error). Shoreham is multipage. Restructured to 5 pages.

### Day 1 mockup iterations (post-/plan)
- **REJECT** Bagel-shop and pest-mgmt-prom anecdotes appearing as public site copy. Kay: *"I gave you those examples for your own context, not to be quotes on the website."* Private examples shared with Claude as conviction-builders are NOT public content. Same principle applied to the Hoffman pull quote — internal content fuel only, not public attribution.
- **REJECT** "We"-centric copy ("we hold for the long run / we don't run auctions / built for owners not for exits"). Kay: *"It sounds like private equity."* Rewrite voice as observational about owners and businesses, not promises about the firm.
- **APPROVE** Grayscale + subtle background-color imagery direction. Reference: Shoreham's "What we value" page with circular b&w pillar images on a dark teal band.
- **APPROVE** Shoreham-style 3-circle pillar layout for What We Value (Community / Service / Trust on dark band).
- **APPROVE** Distinct images per page, no repeats. Carpenter image stays on About per Kay's preference.
- **APPROVE** Visual aesthetic direction: minimalist, Cormorant Garamond serif headlines, Inter sans body, cream palette.
- **APPROVE** Legibility upgrade: body weight 400+, full-ink contrast, larger body sizes (Cormorant reserved for hero/headlines only).

## Actions Taken

- **CREATED** `brain/outputs/2026-05-04-discussion-website-revamp.md` — `/socrates` convergence brief, schema 1.2.0, captures audience/structure/anchor/thesis/build-path decisions for `/plan` handoff.
- **CREATED** `~/.claude/plans/please-share-the-plan-iridescent-bee.md` — 5-day execution plan (Mon→Fri), daily milestones, risk mitigations, verification checklist.
- **CREATED** `scratch/website-mockup-2026-05/` ephemeral project: `index.html`, `about.html`, `what-we-value.html`, `perspective.html`, `contact.html`, `assets/site.css`, `README.md`, plus `insights/`, `assets/images/`, `screenshots/day-1/` subdirs.
- **CREATED** `/tmp/g-b-screenshot/shoot.js` — puppeteer-core screenshot wrapper for full-page + viewport captures, reusable for Tue-Thu iterations.
- **DOWNLOADED** 14 Unsplash images into `scratch/website-mockup-2026-05/assets/images/` (8 craftsman/workshop set + 6 main-street/storefront set).
- **UPDATED** all 5 HTML pages through ~5 iteration passes: skeleton → multipage restructure → content rewrite (anecdotes stripped, Hoffman quote dropped, we-centric claims removed) → grayscale image filter + distinct per-page imagery + Shoreham-style 3-circle pillar layout.
- **UPDATED** `assets/site.css` — bolder body weights, higher contrast, grayscale image filter, dark-section variant, image-circle helper for Shoreham-style layout.

## Deferred

- **DEFER** Day 2 (Tue 2026-05-05) scope: pillar body copy refinement, section-order final lock, photography upgrade decision, wordmark integration from G&B BRAND KIT Drive folder (`1XFwML_hJViZi9uqhRGn1i2311uC6My3-`).
- **DEFER** Hoffman transcript essay extraction to Wed 2026-05-06. Source: `brain/library/internal/pest-management/2026-04-29-hoffman-exterminating-presentation.md`. Material is internal content fuel; essays paraphrase observations, NOT quote Hoffman directly.
- **DEFER** Squarespace credentials handoff to Thu 2026-05-07 EOD via `/tmp` file method. Required for Friday translation.
- **DEFER** Memory update for `feedback_kay_ceo_deal_1_not_allocator.md` (currently labels Deal 1 "search-fund traditional"; CCV correction logged for /calibrate pass).

## Open Loops

- Kay went to bed before reacting to latest iteration. **First-thing-Tuesday checks:** Does the PE-vibe finally drop? Do the Shoreham-style circles match the reference she sent? Should the succession image (older + younger ceramicist) come back somewhere?
- Day 2 build cannot start until Kay confirms Day 1 direction holds. If she still rejects on tone or vibe, scope shifts from "fill pillar bodies" to "rewrite again."
- Local `python -m http.server` on port 8765 left running; should be terminated and restarted Tuesday morning for clean state.
- Mockup files at `scratch/website-mockup-2026-05/` survive the night; project is ephemeral but durable until Friday Squarespace cutover.
- Website + one-pager strategic alignment (the Version A/B/C question from earlier broker-channel session) intersects this work — both copy threads need to stay coherent. Pair on Tuesday.

---

# iMac Evening Session — Conference Pipeline Recovery + Universal Launchd Hardening

Triggered by Kay catching that the Conference Pipeline looked empty. Root cause: May 3 launchd run wiped the sheet (~70 rows). Recovery → conference-discovery hardening → broader doctrine update → 3 snapshot refreshers hardened.

## Decisions

- **APPROVE** Restore Conference Pipeline from May 2, 11:54 AM version-history snapshot. Kay handled the UI restore; ~70 rows recovered.
- **APPROVE** Re-run conference-discovery in recovery mode immediately (vs. waiting until next Sunday's scheduled fire). Cost: one fresh discovery run; benefit: not a week behind on registrations.
- **APPROVE** Append all 13 net-new conference candidates to Pipeline tab (rows 80-92). Intentionally NOT auto-sorted into week-of sections — pure date-sort would scramble the hierarchical week-of headers in col A. Kay marks Decision (col C) on the sheet itself.
- **APPROVE** Add conference-discovery to hardened skill list (POST_RUN_CHECK validator + headless-sunday-prompt.md mandating pre-run snapshot).
- **APPROVE** **Doctrine update — universal POST_RUN_CHECK:** every launchd-scheduled skill needs a validator, not just mutating ones. Read-only skills get lighter validators (artifact-landed checks); no exemptions. Driven by the May 3 dashboard-green-lying-about-the-wipe finding.
- **APPROVE** Harden 3 snapshot refreshers next (attio-snapshot-refresh, jj-snapshot-refresh, apollo-credits-refresh). They feed dashboard tiles directly — silent failure = stale dashboard = bad decisions.

## Actions Taken

- **RESTORED** Conference Pipeline tab from May 2, 11:54 AM version-history snapshot.
- **CREATED** `scripts/validate_conference_discovery_integrity.py` — fails on missing pre-run snapshot or row delta > 15.
- **CREATED** `.claude/skills/conference-discovery/headless-sunday-prompt.md` — mandates pre-run snapshot at `brain/context/rollback-snapshots/conference-pipeline-pre-run-{TODAY}.json`; bans clear-then-rewrite; caps single-run archival at 15 rows.
- **UPDATED** `scripts/run-skill.sh` — added `conference-discovery:sunday` route in case-statement.
- **UPDATED** `~/Library/LaunchAgents/com.greenwich-barrow.conference-discovery.plist` — added POST_RUN_CHECK env var; reloaded; last-exit-status 0.
- **UPDATED** `CLAUDE.md` — universal POST_RUN_CHECK doctrine entry (2026-05-04). Added conference-discovery to hardened-skill list.
- **APPENDED** 13 net-new conference candidates to Pipeline (rows A80:O92, 195 cells).
- **SLACKED** AI-Operations channel: "Conference Pipeline recovered + 13 net-new conferences added" with link.
- **CREATED** `scripts/validate_attio_snapshot_integrity.py`, `scripts/validate_jj_snapshot_integrity.py`, `scripts/validate_apollo_credits_integrity.py` — each chmod +x, each verified exit 0 against current snapshot files.
- **UPDATED** `scripts/refresh-attio-snapshot.sh`, `scripts/refresh-jj-snapshot.sh`, `scripts/refresh-apollo-credits.sh` — added inline POST_RUN_CHECK call + exit-code propagation (`set -uo pipefail`, validator exit takes precedence over refresh exit if non-zero).
- **VERIFIED** all 3 snapshot-refresher plists `launchctl unload`+`load` clean; `launchctl list` shows last-exit-status 0 for all 3.
- **CREATED** `memory/feedback_no_clear_rewrite_populated_sheets.md` (or verified existing) — never `gog sheets clear` + rewrite on populated sheets.
- **CREATED** `memory/feedback_dashboard_green_can_lie.md` — exit 0 ≠ success; skill can self-detect destructive failure and stop gracefully while dashboard tile goes green.
- **UPDATED** `MEMORY.md` index with both new memory entries.
- **UPDATED** `.claude/skills/conference-discovery/SKILL.md` — added "Mandatory validator" section; corrected stale 15-column layout description to match live sheet header (`Week Of | Date | Decision | Event Name | Location | Travel | Niche | Registration Cost | Registration Paid | Reg Deadline | Est. Attendees | Attendee List | Website | Status | Agent Rec`); incident reference for May 3 wipe.
- **UPDATED** `.claude/settings.local.json` — added `Bash(gog sheets clear:*)` to permissions.deny so any future subagent attempting the wipe pattern gets blocked at the harness layer (belt-and-suspenders to the validator).

## Deferred

- **DEFER** hardening of 5-6 remaining unhardened launchd skills under the new universal doctrine: email-intelligence, calibration-workflow, external-services-probe, weekly-archive-export, weekly-snapshot, health-monitor. Recommended priority order documented in subagent audit (`logs/scheduled/` cross-reference). Batch into one follow-up session — trigger: next 30-60 min of available infra time. **Not urgent**; the 3 snapshot refreshers were the highest-leverage gap because they feed the dashboard.

## Open Loops

- 13 conference candidates appended at bottom of Pipeline (rows 80-92), unsorted into week-of sections. Kay marks Decision (col C). After her decisions, optional follow-up: re-insert into the correct week-of sections via individual row inserts (NOT pure date-sort).
- Sunday May 10 conference-discovery launchd fire — first run with the new POST_RUN_CHECK validator + headless-sunday-prompt + pre-run snapshot pattern. Watch `logs/scheduled/conference-discovery-2026-05-10-2100.log` for the validator-output line to confirm the new infrastructure is firing as designed.
- Dashboard C-Suite & Skills weekly-flow tile for the Sunday May 3 conference-discovery cell — currently still showing green. Will be replaced organically when the Sunday May 10 fire completes (per the persistence rule, past-day fired tiles persist all week, reset Sunday). No action needed.

## Key Decision Traces (non-obvious calls worth preserving)

1. **Don't auto-sort the 13 new rows by date.** Pure col-B date sort would scramble the hierarchical week-of headers in col A (single-cell rows like `["5/4"]` interspersed with data rows that have empty col A). Skill SKILL.md sort-validation expects flat structure; reality is hierarchical. Logged as an open-loop manual reconciliation rather than auto-resolved. *Reason future agents might be tempted to "just sort it" and break the structure.*

2. **Broaden POST_RUN_CHECK from mutating-only to all-launchd-skills (Kay's call, 2026-05-04).** Trigger reasoning: read-only skills can ALSO have silent failure modes that mislead the dashboard. Conference-discovery exited 0 because it gracefully self-detected a wipe and stopped — wrapper saw success, dashboard went green, the wipe sat undetected until Kay caught it visually. Read-only skills aren't immune to this class of bug; their silent-zero is just less visible. Universal-validator doctrine closes the gap.
