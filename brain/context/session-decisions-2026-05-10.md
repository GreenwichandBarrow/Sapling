---
date: 2026-05-10
type: context
title: "Session Decisions — 2026-05-10"
tags:
  - date/2026-05-10
  - context
  - topic/session-decisions
  - topic/morning-briefing
  - topic/1password-migration
  - topic/credential-rotation
  - topic/tailscale-magic-dns
  - topic/dashboard-mobile
  - topic/harrison-wells-call
  - topic/inbox-hygiene
  - topic/vps-primary-trial
  - topic/memory-migration
  - topic/tech-stack
  - topic/keyreach
  - topic/dealsx
  - topic/gmail-filters
  - topic/post-call-analyzer
  - topic/phase-4-5
  - topic/systemd-environment-file
  - person/harrison-wells
  - person/will-bressman
  - person/lauren-young
  - person/jemden-helmsley-spear
  - person/sam-singh
  - company/helmsleyspear
  - company/dealsx
  - company/keyreach
schema_version: 1.1.0
---

# Session Decisions — 2026-05-10

Sunday. First /goodmorning ran on server claude. Resolved 5 briefing decisions, then expanded into full 1Password migration sweep (carried-forward Slack + GOG keyring + .baks cleanup), Magic DNS deployment, mobile dashboard + iPhone home-screen access, MacBook 1P CLI install, and Harrison email follow-up draft. Drafted but did NOT send Harrison email — Sunday-send rule caught at stop hook, scheduled for Monday AM.

## Decisions

### Morning briefing (5/10) — server-side run

- **PASS** Item 1 — Will Bressman (BK Growth) Monday 5/11 2pm in-person at One Hanover. No brief needed.
- **APPROVE** Item 2 — Attio API token rotation. Kay had already rotated yesterday; verified Apollo live (200) on direct curl, Attio 401 because direct `source` of `.env.launchd` loads literal `op://` strings as bearer tokens. Real Attio key resolved cleanly via `op inject`. Broadened decision into full 1P migration sweep (see below).
- **APPROVE** Item 3 — Fix `nightly-tracker-audit` GOG_ACCOUNT propagation. Confirmed running through `scripts/run-skill.sh` line 41 export, validator passes once env propagates. Resolved as byproduct of credential migration (smoke test PASSED).
- **APPROVE** Item 4 — Refill-check Premium Pest Mgmt (JJ-Call-Only) + Private Art Advisory (Kay Email). Kay handled server-side; verification of actual execution outstanding (see Open Loops).
- **APPROVE** Item 5 — Lauren Young check-in draft for Monday AM send. Kay handled server-side; verification of actual draft creation outstanding (see Open Loops).

### Full 1Password migration sweep (broadened from Item 2)

- **APPROVE** Run full inventory of all plaintext secrets across `.bashrc`, `.zshrc`, `.profile`, `scripts/.env.launchd`, `scripts/.env`, plist/systemd files. Use ONLY value-suppressing patterns per CLAUDE.md secret doctrine.
- **APPROVE** Migrate all 5 remaining plaintext secrets in this session: GOG_KEYRING_PASSWORD + 4 Slack webhooks (carried from 5/9 deferrals).
- **APPROVE** Adopt `pbcopy-through-SSH` extraction pattern as default for any future remote-secret extraction. Pipes value directly through encrypted SSH tunnel into Mac clipboard — never displays on screen, never lives in scrollback. Used for all 5 secrets, no on-screen exposure.
- **APPROVE** Option A for `~/.bashrc` cleanup — remove plaintext `GOG_KEYRING_PASSWORD` line entirely. Rejected Option B (conditional `op read` block on every shell open) — recurring API call latency + hidden behavior debugging cost. Rejected Option C (leave plaintext) — defeats migration purpose.
- **APPROVE** Delete both stale `.env.launchd.bak` files containing rotated-out Attio + Apollo values. Pure plaintext-on-disk risk, zero recovery value.
- **REJECT** Recreating GOG Keyring Password 1P item — already existed and updated earlier in session. Server claude proposed fresh-create; corrected to use existing item.

### Magic DNS deployment

- **APPROVE** Deploy Magic DNS NOW (rejected the "tomorrow" deferral). Per `feedback_default_to_now_not_later` — deferring with no actual blocker is the wrong default. Server claude wired `tailscale serve` exposing Streamlit on tailnet at `agent-vps-7731c88b:8501`.

### Dashboard mobile access

- **APPROVE** Mobile-friendly Streamlit layout for Command Center, accessible from iPhone home screen via Magic DNS URL.
- **APPROVE** Mobile table horizontal scroll fix for Deal Aggregator page (added `.gb-table-wrap { overflow-x: auto }` + `min-width: 720px` + iOS momentum scroll to `dashboard/theme.py` mobile media block).

### MacBook 1P CLI parity

- **APPROVE** Install `op` CLI on MacBook via `brew install 1password-cli` after `command -v op` returned not-found. Desktop app integration toggle alone is not the binary.
- **VERIFIED** `op vault list` returns vaults including GB Server. MacBook now has full parity with server for resolving op:// references.

### Harrison email + 5/15 prep

- **APPROVE** Draft Harrison Wells follow-up replying to his "all up and running?" message (Fri 5/8 20:29). Format: bullet list of what landed since Friday, no commentary or rationale. Five items: cmux, 1P server vault migration, skill-building MCP-first/API-second/local update, Socrates skill (similar to Hermes), Command Center on server with iPhone home-screen access. Plus one teaser line for 5/15 agenda: Family Office personal project setup discussion.
- **DEFER** Send Harrison email — caught by stop hook (Sunday-send rule). Schedule via Gmail for Monday AM ~9am ET. Email body unchanged; only "Magic DNS goes in tomorrow" line replaced with "Magic DNS live."
- **DEFER** Family Office personal project deep-dive — to be raised on 5/15 Harrison call. NOT captured in inbox prep tracker (Kay corrected: she shared as email teaser content, not as system-tracked topic).

### Harrison inbox hygiene

- **APPROVE** Mark 3 Harrison-related inbox items as `done` with resolution sections:
  - `2026-05-01-harrison-server-setup-email-watch.md` — Hetzner cutover complete 5/8, 1P migration 5/10. Email arrived; work superseded.
  - `2026-05-01-harrison-secure-api-key-tool-name.md` — 1P CLI route was the answer; full migration done.
  - `2026-05-01-build-discuss-skill.md` — Built as `/socrates`, registered in active skills, three-phase pipeline codified in CLAUDE.md.

### Memory updates (in-session)

- **UPDATED** `feedback_drafts_no_blockquote.md` — added "agent-to-agent paste (instructions Kay relays to server claude or another session)" to scope. Reinforced 2026-05-10 after wrapping paste content in `>` bars twice in one turn.
- **CREATED** `feedback_credential_extraction_clean_terminal.md` — secret-printing terminal steps go in macOS Terminal.app/iTerm2 only, never Cursor/Claude Code/any AI-instrumented integrated terminal. Kay's instinct, codified.
- **UPDATED** `feedback_credential_extraction_clean_terminal.md` — added pbcopy-through-SSH pattern section after pattern proven on all 5 secrets today.
- **UPDATED** `MEMORY.md` index — added new clean-terminal entry under Feedback.

## Actions Taken

### 1Password migration (server-side execution)

- **CREATED** 4 new 1Password items in vault GB Server: `Slack Webhook — Operations`, `Slack Webhook — Active Deals`, `Slack Webhook — Strategy Ops`, `Slack Webhook — SVA`.
- **UPDATED** `GOG Keyring Password` 1P item with extracted plaintext value (45-char keyring password from server `~/.bashrc`).
- **POPULATED** All 4 Slack webhook 1P items via pbcopy-through-SSH extraction.
- **UPDATED** `scripts/.env.launchd` — 5 secrets swapped from plaintext to `op://` references. Total: 7/7 production secrets now on op:// (Attio + Apollo from 5/9 + 5 today).
- **DELETED** Plaintext `export GOG_KEYRING_PASSWORD=...` line from server `~/.bashrc`.
- **DELETED** `scripts/.env.launchd.bak` and `scripts/.env.launchd.bak-pre-1password-2026-05-09` (both contained rotated-out values, no recovery use).

### Smoke tests (all PASSED)

- **VERIFIED** `op inject` resolves all 7 vars to expected lengths.
- **VERIFIED** nightly-tracker-audit validator runs clean (resolved Decision 3 byproduct).
- **VERIFIED** `gog gmail draft list` returns drafts (proves keyring decrypt under op://).
- **VERIFIED** Attio API live curl with op://-resolved key returns 200 OK.
- **VERIFIED** Plaintext-secret count in active files = 0.

### Magic DNS + mobile dashboard (server-side)

- **DEPLOYED** `tailscale serve` exposing Streamlit Command Center at `agent-vps-7731c88b:8501` on tailnet.
- **UPDATED** 3 files swapping `localhost:8501` → `agent-vps-7731c88b:8501`: `.claude/commands/goodmorning.md` line 81, `CLAUDE.md` line 369 (twice), plus dashboard config.
- **DEPLOYED** Mobile horizontal-scroll fix in `dashboard/theme.py` mobile @media block.
- **VERIFIED** Service restarted, HTTP 200, mobile table swipe working post hard-refresh.

### MacBook (Mac-side execution)

- **INSTALLED** `1password-cli` v2.x via Homebrew on MacBook.
- **VERIFIED** Desktop integration toggle on; `op vault list` returns vaults including GB Server.

### Vault edits (Mac-side)

- **UPDATED** `brain/inbox/2026-05-01-harrison-server-setup-email-watch.md` → status: done + Resolution section.
- **UPDATED** `brain/inbox/2026-05-01-harrison-secure-api-key-tool-name.md` → status: done + Resolution section.
- **UPDATED** `brain/inbox/2026-05-01-build-discuss-skill.md` → status: done + Resolution section.
- **UPDATED** `memory/feedback_drafts_no_blockquote.md` (agent-to-agent paste case).
- **CREATED** `memory/feedback_credential_extraction_clean_terminal.md` + pbcopy-through-SSH pattern update.
- **UPDATED** `memory/MEMORY.md` index.

### Drafts

- **DRAFTED** Harrison Wells follow-up email — 5 bullets + 5/15 Family Office teaser + day-aware close. Held for Monday AM send.

## Deferred

### Monday AM (5/11)

- **Send Harrison Wells follow-up email** — drafted today, scheduled for Mon ~9am ET via Gmail. Body unchanged except "Magic DNS goes in tomorrow" → "Magic DNS live."
- **Verify briefing decisions 4 + 5 actually executed server-side** — refill-check on Premium Pest + Private Art (was target-discovery actually triggered?), Lauren Young Monday AM check-in draft (does the Gmail draft exist?). Server claude pending confirmation as of /goodnight.
- **Brief-decisions pre-flight check** — Will Bressman 2pm in-person already PASSED today; should NOT re-surface in Mon AM briefing. Validate first server-side weekday-morning fires: deal-aggregator 06:00, relationship-manager 06:50, email-intelligence 07:00 (carried from 5/9).
- **Decide Taft (Payal) vs KeyBank (Megan) Thu 5/14 dinner pick** — carried 5/9, 5/8.
- **Reply to Allison Allen PWIPM Council ask** — carried 5+ days, escalating.

### Friday 5/15 (Harrison call prep)

- **Assemble 5/15 Harrison call challenges list** — due EOD Thursday 5/14. Topics: failing/fragile scheduled jobs, open infra decisions (learnings.md rollout), skill-build questions, anything from 4/30 followups not yet landed.
- **Family Office personal project setup discussion** — raise on 5/15 call. Kay's framing: separate project for running her home, separate from G&B work; wants Harrison's input on architecture (repo? vault? sub-vault?) and operating two side-by-side cleanly.

### Tuesday 5/12+

- **Phase 4.5 cutover** — post-call-analyzer iMac sidecar retirement (gated on Tue's first Granola call processing through server detector).
- **iMac post-call-analyzer hung process (PID 56446)** — still running shadow-mode, hung 17h on validate-edits loop (carried 5/9).
- **Server SA token rotation policy** — still no policy; tag for security review (carried 5/9).
- **Dashboard HTTPS via `tailscale serve` --https=443** — already wired with HTTP via Magic DNS today; HTTPS upgrade is the follow-up.
- **Deal-aggregator-friday cadence stagger** — Fri 06:00 collides with main (carried 5/9).
- **Add lighter validator to deal-aggregator** — 3 variants, pre-existing gap (carried 5/9).
- **learnings.md propagation** — across remaining ~42 skills (carried 5/9).
- **Generator-fix branch propagation** — `format_env_line` patch on iMac branch divergent (carried 5/9).
- **Dashboard URL update** — local CLAUDE.md/dashboard files referenced by server claude pending /goodnight commit on its side.

### Future / low priority

- **Brew upgrade gogcli** on iMac + MacBook to sync versions (carried 5/9).
- **Code change in `scripts/task_tracker.py`** to flip `append` verb (carried 5/9).
- **Create vault entities** `will-bressman.md` + `bk-growth.md`. Populate Will's Attio relationship fields (carried 5/9).
- **MacBook `~/.zshrc.corrupt-2026-05-08.bak`** (899 MB) — still on disk; safe to delete (carried 5/9).
- **Migrate remaining ~5 weekly-cadence timers** if not yet covered (carried 5/9).
- **1Password SSH Agent toggle** + `tailscale serve` HTTPS upgrade (carried 5/9).
- **"Ask Harrison" MCP install email** — still waiting on Harrison's email; can ask on 5/15 call instead.

## Open Loops

- **Server claude /goodnight pending** — dashboard, CLAUDE.md, skill SKILL.md changes still uncommitted on server side. Server claude said "holding for /goodnight." Coordinate: local committing first; server should `git pull` before its own /goodnight.
- **Briefing decisions 4 + 5 verification** — sent to server claude this turn, pending response. If not received before /goodnight, carries to Monday morning briefing.
- **Overnight scheduled-job tests** — 14:00 target-discovery-sunday (Apollo + Slack #strategy-active-deals), 18:00 jj-operations-sunday (Slack), 23:30 nightly-tracker-audit, 05:00 Mon launchd-debugger scan. Silence overnight = clean credential migration. If anything breaks, the 5am scan posts to #operations.
- **Light security flag from morning subagent** — `GOG_KEYRING_PASSWORD` value was visible in a subagent's tool output during this morning's Mon pre-flight (per server claude's note). Now moot since the keyring password is migrated to op:// and the in-bashrc plaintext is removed; but the leak event itself is recorded.

---

# Evening session — appended 2026-05-10 22:xx ET

Quiet operational evening on VPS capped by three durable shifts: (1) the memory-into-repo migration completed end-to-end on the server (Mac side already did it; server side did the symlink swap + copied 3 server-only memories that hadn't propagated), (2) commitment to VPS as primary Claude working surface with Mac moving to secondary/sync, (3) Phase 4.5 effectively complete with `com.greenwich-barrow.post-call-analyzer.plist` unloaded and retired on Mac; server `post-call-analyzer-poll.timer` is sole processor. Plus a new `/gmail-filter-add` skill, KeyReach added to tech inventory (corrected to FREE — covered by DealsX), one Gmail filter update for [[entities/jemden-helmsley-spear]], and a P2 bead captured for per-service systemd `EnvironmentFile` audit.

## Decisions (evening)

### Gmail filter — [[entities/jemden-helmsley-spear]] routing

- **APPROVE** Add `jemden@helmsleyspear.com` to the bundled-contacts OR filter for label `auto/personal & network` (Label_32). Gmail's API has no filter-patch endpoint, so executed as create-new-then-delete-old (new ID `ANe1BmhXjvfOOifhr_MS5VU9l_j1LjWXMKaUig`, old ID `ANe1Bmj4yK8XXJ95F_dQXiUiD0jCciFReNCYrQ` deleted).

### Skill creation — `/gmail-filter-add`

- **APPROVE** Build skill `/gmail-filter-add` so the create-then-delete dance is reusable. Auto-triggers on phrases like "add X to filter Y" or "add X to auto/Y". Idempotent (skips if email already in bundle), handles ambiguous label fragments by asking, creates fresh bundle if none exists, never deletes old until new is verified. Part of the Superhuman → Gmail transition. Kay's estimate: a couple times a week, declining as bundles grow.

### Tech stack — [[entities/keyreach]]

- **APPROVE** Add KeyReach to the tech inventory in 3 places: Budget Dashboard Tab 3 (Tech Stack Inventory), `dashboard/data/tech_stack.yaml` (under CRM & Pipeline next to [[entities/dealsx]]), and `dashboard/data/external_services.yaml` (health-tracked, `ok`, "signed in 2026-05-10").
- **REJECT** Initial $1,500/mo cost estimate I pulled from the budget-manager skill's documented "DealsX KeyReach $1,500/mo" line. **Kay corrected:** KeyReach is FREE on her own account for the foreseeable future, **covered by the existing $1,500/mo DealsX vendor fee** ([[entities/sam-singh]]'s service). Reverted Tab 3 cost from $1,500 → $0; Total Costs back to $792.24/mo. Budget-manager skill's `$1,500/mo DealsX` line is itself correct (that's the DealsX cost; KeyReach is bundled into it).

### Memory migration — server-side completion

- **APPROVE** Migrate auto-memory location to symlink pointing at `~/projects/Sapling/memory/` so memory writes flow into git and sync between Mac + VPS. Mac side did this earlier today (Mac's `feedback_vps_primary_work_surface.md` not yet pushed at session end). Server side executed copy-first then symlink-second to avoid losing 3 server-only memories that hadn't propagated through git (`feedback_use_magic_dns_for_references.md`, `reference_pbcopy_through_ssh_for_remote_secrets.md`, `project_keyreach_dealsx_relationship.md`).
- **APPROVE** Resolve `scripts/load-env.sh` pull conflict by removing identical local untracked copy. Pulled `aaee47d..d4a8c03` from origin/main cleanly.

### VPS-primary working surface

- **APPROVE** Commit to VPS (Sapling Linux server) as Kay's primary Claude Code environment going forward (trial). Mac becomes secondary / sync-only via `git pull`. Foundation: 1Password credential migration complete, Tailscale Serve dashboard live, memory now syncable through git, auto-commit hook landing dashboard/memory edits in-session.

### Phase 4.5 post-call-analyzer cutover — complete

- **APPROVE** Retire Mac sidecar tonight, ahead of Mon 5/11 target. Kay unloaded `com.greenwich-barrow.post-call-analyzer.plist` and moved to `LaunchAgents-retired/` at ~22:25 ET. `launchctl list | grep greenwich-barrow` empty. Server `post-call-analyzer-poll.timer` is sole processor — verified healthy via journal scan (3 days clean, ~5 min cadence, every fire exits clean, latest vault write `2026-05-08-ai-friday-real-roi-of-ai.md` at 22:12 ET).

### Systemd `EnvironmentFile` journal noise

- **DEFER** Per-service audit of `EnvironmentFile=scripts/.env.launchd` usage to Monday infra batch. Discovered during post-call-analyzer-poll diagnostic: every fire emits ~7 `Ignoring invalid environment assignment 'export VAR=op://...'` warnings because systemd's `EnvironmentFile=` doesn't support `export` syntax or resolve `op://` URIs.
- **REJECT** Blanket-strip of `EnvironmentFile=` from all services. Per Kay's call: some services may legitimately need `ATTIO_API_KEY` / `SLACK_WEBHOOK_*` / `GOG_KEYRING_PASSWORD` at process start and would silently break. Right move is enumerate every `*.service`, check what env each binary actually consumes, then per-service decision (remove EnvironmentFile, op-inject drop-in, or shell-wrapper).
- Kay beaded as P2 (human assignee) from Mac. Intent also captured server-side in `scratch/2026-05-10-pending-beads.md` because `bd` CLI not yet installed on VPS.

### Memory updates (evening)

- **CREATED** `memory/project_keyreach_dealsx_relationship.md` — captures KeyReach/DealsX bundling so future tech-audits don't propose cutting it or double-count in burn.
- **CREATED** `memory/project_vps_primary_workflow.md` — VPS-primary trial state, Phase 4.5 complete, bd-CLI install gap, scheduling-already-on-systemd correction (initial draft incorrectly said launchd → systemd was pending; corrected after Kay surfaced "I thought we already did that work").
- **UPDATED** `memory/MEMORY.md` index — appended 4 entries (3 server-only carry-forwards + new VPS-primary). Auto-commit hook (G&B Server author) landed `update memory` and `update dashboard` commits during session — newly noticed pattern.

## Actions Taken (evening)

- **UPDATED** Gmail filter for `auto/personal & network` extended from 8 → 9 addresses to include `jemden@helmsleyspear.com`.
- **CREATED** `.claude/skills/gmail-filter-add/SKILL.md` (single-file skill, no separate command, auto-triggers via phrase patterns).
- **UPDATED** Budget Dashboard Tab 3 — row 21 = KeyReach, Outreach (DealsX), Free, $0/mo, Active, "DealsX-paired". Total Costs unchanged at $792.24/mo (after the initial $1,500/mo error correction).
- **UPDATED** `dashboard/data/tech_stack.yaml` — added KeyReach under "CRM & Pipeline" with note "DealsX outreach platform · Kay's account free · covered by DealsX $1.5K/mo fee".
- **UPDATED** `dashboard/data/external_services.yaml` — added `keyreach` service block (health: ok, "Healthy · signed in 2026-05-10").
- **CREATED** 3 memory files (see Decisions above).
- **UPDATED** `memory/MEMORY.md` index — 4 new line entries (auto-committed mid-session).
- **MIGRATED** Auto-memory directory `~/.claude/projects/-home-ubuntu-projects-Sapling/memory/` → symlink to `~/projects/Sapling/memory/`. Copy-first (3 server-only files + MEMORY.md index reconcile) then `rm -rf` then `ln -s`. Verified `head -3 MEMORY.md` returns `# Memory Index`.
- **CREATED** `scratch/2026-05-10-pending-beads.md` — holding pen for per-service systemd `EnvironmentFile` audit bead intent (P2, target Mon 5/11 infra batch).
- **PULLED** `aaee47d..d4a8c03` from origin/main (Mac's memory-into-repo migration + memory-snapshot → memory rename + new memory files).
- **RESOLVED** Pull conflict on `scripts/load-env.sh` by removing identical local untracked copy.
- **VERIFIED** `post-call-analyzer-poll.timer` healthy (3 days clean, ~5 min cadence, vault write at 22:12 ET).
- **OBSERVED** Auto-commit hook (G&B Server author) landed `aaee47d`, `e56fdaa`, `8d20e64` mid-session for dashboard/data/ and memory/ paths. Pre-existing infra, newly noticed.

## Deferred (evening additions)

- **Per-service systemd `EnvironmentFile` audit** — P2 bead (Mac-beaded), Monday 2026-05-11 infra batch.
- **`bd` CLI install on VPS** — friction point for VPS-primary trial. Workaround: capture bead intents in `scratch/{date}-pending-beads.md`. Monday infra item.
- **`gmail-filter-add` slash command file** — currently phrase-trigger only; add explicit slash command if Kay finds herself typing it literally.
- **Granola Mac app / OneDrive Excel tracker / unmigrated MCPs** — documented exceptions to VPS-primary (per Kay's Mac-side `feedback_vps_primary_work_surface.md` once she pushes it).

## Open Loops (evening additions)

- **Mac-side `memory/feedback_vps_primary_work_surface.md`** — not yet pushed at session end. Likely overlaps with my server-side `memory/project_vps_primary_workflow.md`. Reconcile or merge on next Mac → VPS pull cycle. Surface in tomorrow's morning briefing.
- **Mon 2026-05-11 morning auto-fires now sole-processor** — email-intelligence (7am), relationship-manager (6:50am), deal-aggregator (6am), launchd-debugger (Sat 5am pass-through). First server-side fires with Mac sidecar fully retired. Watch morning briefing for clean artifact landing.
- **VPS-primary trial friction-capture** — log new friction points as they surface during the week (SSH latency, missing MCPs, local-only tools). Decide build-or-fall-back as patterns accumulate.
- **Phase 4.5 validation watch** — server post-call-analyzer-poll.timer as sole processor for 48-72h post-cutover. Monitor for missed calls or stale queue >30 min.
- **🔴 Conference Pipeline corruption (REGRESSION) — fix Mon AM 2026-05-11** — Kay reported during /goodnight: tonight's `conference-discovery` run moved the "week of" row section dividers (no longer grouped) AND changed some of her dropdown selections for "attending events". This is the SAME class of regression that prompted the 2026-05-04 hardening (`validate_conference_discovery_integrity.py` + pre-run rollback snapshot). The validator should have caught row-count delta OR section-divider movement OR cell-value changes outside the append zone. Two work items for Monday morning Decision list: (a) **diagnose** — pull rollback snapshot from `brain/context/rollback-snapshots/conference-pipeline-pre-run-2026-05-10.json`, diff against current live state to identify exactly which rows moved/changed, decide if revert-from-snapshot is the right move OR manual repair; (b) **harden** — update `conference-discovery` SKILL.md + validator with stop hook(s) that explicitly forbid (1) moving non-append-zone rows, (2) editing user dropdown selections, (3) any cell write outside the strict append range. If the existing validator was running, why didn't it catch this — was it disabled, missing this check, or did the agent route around it? Surface as 🔴 Decision item #1 in Monday's briefing.
