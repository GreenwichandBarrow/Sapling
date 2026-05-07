---
date: 2026-04-26
type: output
output_type: session-decisions
title: "Session Decisions — 2026-04-26 (Sunday)"
tags: ["date/2026-04-26", "output", "output/session-decisions", "topic/session-decisions", "status/draft"]
---

# Session Decisions — 2026-04-26 (Sunday)

Heavy execution Sunday. Items 10-14 from the morning briefing substantively shipped. Pre-flight checklists into CLAUDE.md root. Cadence sweep executed (6 Attio records → Dormant). Two new launchd jobs live. Three new feedback memories shipped — including a hard rule shift on relationship-cadence surfacing and Lauren Della Monica → permanent dead-end.

## Decisions

### Pre-flight checklists into CLAUDE.md root
- **APPROVE** — Per Kay's calibration thread, "the strongest single lever" is rewriting top rules as blocking triggers loaded into every session's system prompt. Drafted 7 checklists (~35 checkpoints) covering: external messages, Sheet writes, vault writes, secrets/config, query order, re-asking Kay, morning briefing format. Inserted between "Role: Chief of Staff" and "Vault Writing Rules" so they load early.

### Frieze NY 2026 (5/13–5/17)
- **PASS / SKIP** — Verified [[entities/frieze-new-york-2026|Frieze NY 2026]] = Skip on [[outputs/conference-pipeline-sheet|Conference Pipeline sheet]] Row 26 Col C. Background: agent recon found zero named storage/logistics exhibitors, zero relevant talks, optics risk (collector-side positioning). Date corrected from 5/7-11 to 5/13-17.

### Items 10-14 today push
- **APPROVE** — Kay declared "all of these need to be done today." Reframed scope after agent findings: #13 Granola entities already done, #10 Layer 4 substantively shipped per beads `ai-ops-jrj.1-.4`, #14 deferred per Kay. Net tonight execution: pre-flight checklists, jj-prompt fix, Phase A Gaps 1+3+5-partial+6, Dashboard Items 3+6, Item 1 partial, cadence sweep.

### Lauren Della Monica → Dormant + dead-end memory
- **REJECT/DORMANT** — Kay: "I have asked this multiple times. Stop suggesting outreach to her. It is a dead end." Memory shipped (`feedback_lauren_della_monica_dead_end.md`). Attio record flipped to Dormant with explicit dead-end note in `next_action`.

### Relationship-cadence Friday-only rule
- **APPROVE/RULE** — Kay: "I find all of this noise and very stressful... we had said you will only remind me of relationship outreach cadence on fridays." Memory shipped (`feedback_relationship_cadence_friday_only.md`). Mon-Thu briefings must omit relationship-nurture / overdue-contact / cadence-debt items entirely. Active-deal cadence (NDA, financials, post-LOI) NOT in scope of this rule — those stay daily.

### Cadence-debt sweep batch (6 Attio records)
- **APPROVE** — All 6 contacts flipped to nurture_cadence: Dormant with sweep notes. Carlos duplicate flagged for manual Attio UI merge (MCP lacks native merge). Per the new Friday-only memory, this was a one-time cleanup; cadence-style surfacing won't re-appear in Mon-Thu going forward.

### Phase A sequence (Gap 1 → Gap 5 partial → Apollo credits)
- **APPROVE** — Shipped all 3. Gap 1: drafts attributed across 5 channels (kay/linkedin/dealsx/intermediary/jj). Gap 3: LinkedIn DMs split into SENT vs DRAFTED with invariant verified. Gap 5 partial: per-niche table extended with CEO-emails-7d column. Apollo credits: degraded to minute-window rate-limit data (Apollo's API-key tier doesn't expose monthly credits — OAuth-only).

### Layer 4 wrapper hardening
- **APPROVE** — Agent finding: substantively already shipped per beads `ai-ops-jrj.1-.4`. Only meaningful gap: jj-operations headless prompt time-glob (`-1500.log` → `-*.log`) — shipped. Drive folder validator deferred as non-load-bearing.

### Dashboard Item 6 — Deal Aggregator landing tile
- **APPROVE** — Live. Reads `load_scan(today)` + walks back 7 days for prior comparison. Sunday-aware UX: shows "0 on 4/23 | awaiting next scan | LAST SCAN" when today's scan hasn't fired yet (deal-aggregator is Mon-Fri only).

### Dashboard Item 3 — Calibration parser
- **APPROVE** — Live. Reads latest `brain/outputs/calibrations/*.md` directly, parses by severity (Critical/High/Medium/Low) with applied-detection. Surfaces 8 entries from 4/16 calibration with explicit "(10d ago — stale)" flag.

### Dashboard Item 1 partial — External services probe
- **APPROVE** — Agent shipped probe script + plist. 8 OK / 0 warn / 0 error / 4 OAuth-skip on first run (~0.3s). Plist loaded.

### Apollo + External services plists loaded
- **APPROVE** — Both `launchctl load`'d after Kay confirmed. Self-managing thereafter — per new memory `feedback_scheduled_vs_todo_presentation.md`, will not re-surface in checkpoints unless they fail.

### Attio MCP key swap
- **APPROVE** — New key (65B, in `/tmp/attio-key.txt`) swapped silently into `~/.claude.json` env block via JSON-aware Python. `/mcp` reconnect required to relaunch server. Verified working with `get-lists` returning 3 lists. Workspace-members 403 was scope-not-key issue (admin-tier read).

### gog calendar 404
- **PASS** — Kay clarified: gog calendar is fine, she's been using it for filters. Earlier 404 from briefing was a false alarm. Dropped from open list.

### Scheduled vs to-do presentation rule
- **APPROVE/RULE** — Kay flagged that I presented scheduled job fire times the same way as to-dos, adding to her mental queue. Memory shipped (`feedback_scheduled_vs_todo_presentation.md`). Going forward: scheduled jobs get one-line "wired up" only, surface only on failure.

### Self-correction patterns Kay closed
- **PASS** — These came in as "FYI - done" updates, dropped from active list:
  - Mark (insurance platform review) — done
  - Amanda Lo Iacono — RSVP/coffee resolved
  - Stanley Rodos (art restoration) — done
  - Megan Lawlor — schedule resolved (no further tracking)
  - Karaugh (art storage) — irrelevant, dropped
  - Jason (Hamptons pest) — meeting tomorrow TBD, ask is moot

## Actions Taken

- **CREATED:** `brain/context/session-decisions-2026-04-26.md` (this file)
- **CREATED:** `~/.claude/projects/.../memory/feedback_lauren_della_monica_dead_end.md`
- **CREATED:** `~/.claude/projects/.../memory/feedback_relationship_cadence_friday_only.md`
- **CREATED:** `~/.claude/projects/.../memory/feedback_scheduled_vs_todo_presentation.md`
- **UPDATED:** `~/.claude/projects/.../memory/MEMORY.md` (3 new index entries)
- **UPDATED:** `CLAUDE.md` — added Pre-Flight Checklists section between "Role: Chief of Staff" and "Vault Writing Rules"
- **UPDATED:** `.claude/skills/jj-operations/headless-sunday-prep-prompt.md` — `-1500.log` → `-{TODAY}-*.log` glob
- **UPDATED:** `dashboard/data_sources.py` — Phase A Gap 1 (drafts by channel), Gap 3 (LinkedIn split), Gap 5 partial (per-niche Kay sends), Gap 6 (Apollo credit loader); Item 3 (calibration parser); Item 1 (external services snapshot loader)
- **UPDATED:** `dashboard/pages/dashboard_landing.py` — Item 6 Deal Aggregator tile live wiring
- **UPDATED:** `dashboard/pages/ma_analytics.py` — Gap 5 partial new "CEO emails (7d)" column on per-niche table
- **CREATED:** `scripts/refresh_apollo_credits.py` + `scripts/refresh-apollo-credits.sh`
- **CREATED:** `scripts/probe_external_services.py` + `scripts/probe-external-services.sh`
- **CREATED:** `~/Library/LaunchAgents/com.greenwich-barrow.apollo-credits-refresh.plist` (loaded into launchd)
- **CREATED:** `~/Library/LaunchAgents/com.greenwich-barrow.external-services-probe.plist` (loaded into launchd)
- **CREATED:** `brain/context/apollo-credits-snapshot.json` (initial snapshot)
- **CREATED:** `brain/context/external-services-snapshot.json` (initial snapshot, 8 OK / 4 OAuth-skip)
- **UPDATED:** Attio People record [[entities/lauren-della-monica|Lauren Della Monica]] (8e316ceb-90f3-469e-92cb-7ad079fbed14) → nurture_cadence: Dormant + dead-end note in next_action
- **UPDATED:** Attio People record Carlos Nieto gmail (97e90c25-2017-499e-9a6f-7ce82c0b2c3e) → Dormant + duplicate-of note
- **UPDATED:** Attio People record Carlos Nieto In3o (12f84371-c37e-47ae-adb8-c3317716ccaf) → Dormant + duplicate-of note
- **UPDATED:** Attio People record Kanayo Oweazim (576f7920-71fa-4b85-993f-66238ff13e31) → Dormant
- **UPDATED:** Attio People record Ashlee Walter (adc02c49-ead1-496b-8365-7a8c8c27a9da) → Dormant + "keep in network, no scheduled outreach"
- **UPDATED:** Attio People record Robert DiMartini (28ba7b68-ae23-44c9-99ed-b1b1429767a7) → Dormant + "Kay can text directly when needed"
- **UPDATED:** `~/.claude.json` Attio MCP env block with new API key (65B from `/tmp/attio-key.txt`); backup at `~/.claude.json.bak-attio-rewire2`
- **VERIFIED:** Frieze NY 2026 = Skip on Conference Pipeline sheet Row 26 Col C
- **VERIFIED:** All 4 Granola entity stubs already exist in `brain/entities/` with full content (kristin-wihera, axial, wiggin-and-dana, saunders-street-capital)

## Deferred

- **#14 Quarterly golden source pick** — Kay: "later in the week, not today." Trigger: Kay names a Kay-approved Q3 investor update file → I wire into `.claude/skills/investor-update/examples/quarterly/`.
- **Handwrytten test wave decision** — Kay: "later in the week, not today." Trigger: Kay's go on the 50-card test wave (~$200 all-in, ~10x cheaper than her original $1,250-2,500 estimate).
- **Phase A Gap 2 — Response rate per channel** — Mon/Tue. Needs gog Gmail label scan (slow, rate-limited) + new hourly refresh script. ~1.5hr.
- **Phase A Gap 4 — New contacts per niche** — Mon/Tue. Needs Attio snapshot extension to compute week-over-week People-records-by-niche delta. ~1hr.
- **Dashboard Item 4 — M&A Analytics zones 2/2.5** — DealsX-blocked until 2026-05-07.
- **Layer 4 nightly-tracker Drive folder validator upgrade** — non-load-bearing optimization. ~30min when convenient.
- **Carlos Nieto manual merge in Attio UI** — MCP lacks native record merge; both records are now Dormant with cross-reference notes so they won't surface either way.

## Open Loops

- **Sunday 18:00 jj-operations-sunday fire** — canonical first hardened test. Verify Monday morning that 5 Mon-Fri Call Log tabs landed on Premium Pest sheet. If validator failed, Slack `#operations` will alert with `VALIDATOR FAILED` prefix.
- **Phase A Gaps 1, 3, 5-partial, 6 + Items 3, 6, 1-partial** — code shipped, untested visually on dashboard. Recommend Monday morning visual check at localhost:8501 to confirm all panels render cleanly.

## System Status

- **Attio MCP:** ✅ live (new key swapped + `/mcp` reconnect verified with `get-lists`)
- **gog:** ✅ live (calendar previously suspected 404 was false alarm — Kay clarified she's been using it for Gmail filters today)
- **Superhuman MCP:** 🟡 still expired (Bash wrapper works for drafts; this isn't blocking tonight)
- **launchd Apollo credits + external services probes:** ✅ wired up, run Mon-Fri (per scheduled-vs-todo rule, won't re-surface unless they fail)
- **Cadence-debt:** zeroed out (6 records → Dormant)

---

## Evening Session — Gmail Filter Migration + SaaS Lock-in Audit Initiation

Late afternoon / evening session. Migrated Kay's email auto-labeling system from Superhuman's LLM autolabels (locked into the app, lost on cancellation) to portable Gmail filters under `auto/*` namespace. Surfaced annual-SaaS lock-in pattern (Superhuman, Grammarly chatbot refusing pro-rated refund, Motion likely same) → hardened SaaS rule from "monthly first, annual after 30-60 days" to "NEVER annual unless monthly isn't offered." Skill audit identified 2 read-path migrations needed.

### Decisions

#### Gmail filter migration to auto/* namespace
- **APPROVE** — Replaced Superhuman's locked-in LLM autolabels with 13 `auto/*` Gmail filters. New labels: `auto/deal flow`, `auto/family & friends`, `auto/finance & legal`, `auto/home`, `auto/meetings`, `auto/personal & network`, `auto/search fund`, `auto/subscriptions & education`, `auto/travel & expenses`, `auto/tech stack`, `auto/investors`, `auto/team`, `auto/industry research`. Backfilled ~3,100 historical threads. Filters apply label only, do NOT skip inbox (per Kay's "I want to see it labeled, hit E when done" workflow).

#### 12 VIP IMPORTANT filters deleted
- **APPROVE** — Kay: "Gmail's native Important learning does the work of VIP labeling." All 12 filters routing senders (Anacapa, ML Capital, DealsX, Fireflies, etc.) to `IMPORTANT,CATEGORY_PERSONAL` deleted. Native Priority Inbox classifier replaces hardcoded rules.

#### 97 old organizational filters deleted
- **APPROVE** — Net of expanded `auto/*` coverage, 97 filters routing to legacy labels (RESOURCES/EDUCATION 29, TECH STACK 19, BANKING/ACCOUNTING 12, etc.) deleted. Old labels themselves kept (historical mail retains tags). Total filters dropped from 129 → 31.

#### Old organizational labels — KEEP (no delete)
- **PASS** — Kay's rule: don't delete labels themselves yet. Historical mail with old tags stays findable. Revisit after 2-week observation of `auto/*` performance.

#### auto/family & friends — DROPPED
- **PASS** — Kay: "drop the request for family and friends emails." Label stays dormant in Gmail, no filter built. Personal-account use case can re-activate later when she authenticates a personal Gmail into gog.

#### Megan @ ml-cap.com reclassified
- **APPROVE** — Originally proposed as `auto/investors` member based on VIP filter routing. Kay corrected: "she is not an investor, she is a fellow searcher." Reclassified to `auto/personal & network` (3 historical threads relabeled).

#### SaaS purchase rule — HARD shift
- **APPROVE/RULE** — Kay: "no annual subscriptions unless its the only option." Original soft rule (monthly first, switch to annual after 30-60 days proven use) replaced with hard rule. Memory `feedback_saas_monthly_first.md` rewritten. Receipts: Superhuman annual lock-in (no refund per Grammarly chatbot), Motion likely same, Grammarly itself.

#### Superhuman cancellation pursued
- **APPROVE** — Kay paid annual; productivity value unclear vs. Mimestream / Apple Mail + Gmail filters. Email drafted to `help@superhuman.com` (cancel + pro-rated refund). Schedule Monday 9 AM ET. Don't self-cancel until response received.

#### Motion cancellation pursued
- **APPROVE** — Likely same annual lock-in pattern. Email drafted to `support@usemotion.com` (cancel + refund OR switch to monthly). Schedule Monday 9 AM ET. Email also requests CSV export of all 210 tasks (active + completed) before cancellation processes.

#### Skill audit — 2 migrations identified
- **APPROVE** — Audit found `email-intelligence` and `pipeline-manager` use `superhuman_search` MCP for inbox/draft scanning. Drafting via `superhuman-draft.sh` wrapper KEEP-AS-IS (intentional per security model). READ paths should migrate to gog Gmail. Bead `ai-ops-eg3` created (P1, ~2-3 hr).

#### Email drafts — direct ask only (no busywork questions)
- **APPROVE/RULE** — Kay flagged that asking vendors to "please confirm: 1/2/3..." dilutes the ask and gives them an easy out. Memory `feedback_email_direct_ask_only.md` shipped. Pattern: lead with the ask, trust vendor to surface relevant data in their response.

#### Refund attempt — escalation path before self-cancel
- **APPROVE** — Order: send email FIRST (preserves leverage), wait 1-2 business days for response, only self-cancel via vendor app if refund denied. Self-cancelling first nukes leverage and often forfeits refund eligibility.

### Actions Taken

- **CREATED:** 13 `auto/*` Gmail labels on `kay.s@greenwichandbarrow.com` (Label_27 through Label_39)
- **CREATED:** 14 Gmail filters (1 `auto/family & friends` filter pending email list, dropped per Kay; the rest live)
- **CREATED:** Bead `ai-ops-sre` (P2) — tech-stack audit, monthly vs annual SaaS sweep
- **CREATED:** Bead `ai-ops-eg3` (P1) — migrate email-intelligence + pipeline-manager READ paths from Superhuman MCP to gog Gmail
- **CREATED:** Memory `feedback_gmail_filters_backfill_default.md` — always backfill matches when creating filters
- **CREATED:** Memory `feedback_refresh_state_before_bulk_destructive.md` — re-fetch live state before bulk deletes (post-mortem from self-inflicted bulk-delete-with-stale-snapshot bug)
- **CREATED:** Memory `feedback_email_direct_ask_only.md` — no "please confirm 1/2/3" busywork in email drafts
- **CREATED:** Memory `feedback_motion_api_python_not_jq.md` — Motion API has unescaped control chars; parse with Python `json.loads(strict=False)`
- **UPDATED:** Memory `feedback_saas_monthly_first.md` — hard rule (never annual unless monthly isn't offered); supersedes earlier soft 30-60-day version
- **UPDATED:** `~/.claude/projects/.../memory/MEMORY.md` index with 5 new/updated entries
- **UPDATED:** `.claude/skills/motion/SKILL.md` — added Python-not-jq parsing rule + 403 throttle behavior to essential principles
- **DELETED:** 12 VIP `IMPORTANT,CATEGORY_PERSONAL` filters
- **DELETED:** 97 old organizational filters (TECH STACK 19, BANKING 12, RECEIPTS 7, OUTREACH 7, INVESTORS 6, DEAL FLOW 4, RESOURCES/EDUCATION 29, INDUSTRY RESEARCH 4, TEAM 5, MISC 4)
- **BACKFILLED:** ~3,100+ historical threads relabeled across 9 categories (deal flow 86, finance & legal 100+500cap, meetings 411, personal & network 32+10+3, subscriptions 298+500cap, travel 129, tech stack 769, investors 241+48, team 162, industry research 38)
- **DRAFTED:** Email to `help@superhuman.com` (cancel + pro-rated refund) — Kay to schedule Monday 9 AM ET
- **DRAFTED:** Email to `support@usemotion.com` (cancel + refund + CSV export request) — Kay to schedule Monday 9 AM ET
- **VERIFIED:** Cancellation channel for Superhuman post-Grammarly acquisition routes through Grammarly billing chat; chatbot refused pro-rated refund (no escalation in that channel), so direct Superhuman support email is the parallel attempt

### Deferred (Evening Session)

- **Send Superhuman email** — Monday 2026-04-27 9 AM ET (Sunday-no-send rule)
- **Send Motion email** — Monday 2026-04-27 9 AM ET (Sunday-no-send rule)
- **Mass-delete remaining ~27 niche-specific filters** — after 2-week observation period of `auto/*` performance (target: 2026-05-10). Includes some specific bank/vendor senders auto/finance & legal misses (~10), industry research mailchimp lists (~3), team-specific routing (~3), one-off niche senders (~10).
- **ai-ops-eg3 (Superhuman READ path migration)** — schedule for next week as discrete task, ~2-3 hr work
- **Verify Gmail filter behavior in production** — watch for over-eager matches or missed senders over the next week
- **auto/family & friends filter** — dropped per Kay (label stays dormant); reactivate when she authenticates personal Gmail into gog (no fixed date)

### Open Loops (Evening Session)

- **Motion API task export retry** — running in background as task `bpvjuq7i5` (8-retry exponential backoff, fetching active + completed). Verify tomorrow whether `/tmp/motion-backup.json` populated. If success → upload to `STRATEGIC PLANNING` Drive folder as `MOTION TASKS ARCHIVE 4.26.26` Sheet. If still throttled → rely on Monday Motion support email to send CSV.
- **Grammarly cancellation flow** — Kay was mid-flow in chatbot when session ended. Bot confirmed: no pro-rated refund, no human escalation through that channel. She still needs to finalize cancellation through chatbot (turn off auto-renew) regardless of refund outcome. Should happen Monday alongside the email send.
- **Refund verdicts pending** — Superhuman direct support, Motion support. Both via Monday 9 AM emails. Decision tree: refund granted → cancellation processes naturally. Refund denied → use through term-end, switch to monthly (Motion) or migrate to Mimestream/Apple Mail (Superhuman) at next renewal.
- **Pulled-forward tech-stack audit** — bead `ai-ops-sre` was P2; based on today's discoveries (2+ confirmed annual lock-ins), should escalate to P1 and run alongside next budget-manager. Recommend morning surface in tomorrow's briefing as 🟡 decision item.

### Calibration Candidates (Evening Session)

- **Stop hook caught 2 Sunday-send recommendations** — hook is working, no escalation needed. Confirms `feedback_no_sunday_emails` rule is enforced via stop-hook layer not memory only.
- **Self-inflicted bulk-delete bug from stale snapshot** — caught + recovered + memorialized as `feedback_refresh_state_before_bulk_destructive.md`. No additional skill/hook change recommended; the rule is now durable.
- **Motion API jq parsing failure** — caught + recovered + memorialized as `feedback_motion_api_python_not_jq.md` and inlined into `.claude/skills/motion/SKILL.md` as essential principle #7. Future agents will hit this rule before reaching for jq.
- **Pattern: SaaS lock-in pain across 3 vendors today (Superhuman, Grammarly, Motion)** — recommend `budget-manager` skill auto-flag annual subscriptions in next monthly run + draft cancellation/switch emails proactively for Kay's review. NOT proposing autonomous send — preserve `draft-before-send` rule.
