---
date: 2026-05-08
type: context
title: "Session Decisions — 2026-05-08"
tags:
  - date/2026-05-08
  - context
  - topic/session-decisions
  - topic/morning-briefing
  - topic/server-migration
  - topic/phase-4
  - topic/post-call-analyzer
  - topic/granola-mcp
  - topic/timer-migration
  - topic/macbook-setup
  - topic/calibration
  - person/will-bressman
  - person/allison-allen
  - person/harrison-wells
schema_version: 1.1.0
---

# Session Decisions — 2026-05-08

Friday. Phase 3.5 foundation completion + Phase 4 (Granola sidecar handoff) end-to-end commission + 8-timer launchd→systemd migration + MacBook conference-prep. Major architectural learnings on MCP-first integration doctrine, Granola same-session-PKCE workaround, and silent-validator-regression generator bug averted. One of the highest-leverage system-build days since launch.

## Decisions

### Morning briefing (5/8)

- **APPROVE** Item 1 — Kill hung relationship-manager (PID 34126, elapsed 2h53m at briefing time). Self-corrected: process actually completed cleanly at 9:51am via attempt-2 retry after API timeout. Kill-attempt failed because process had exited. Calibration moment: ps-elapsed alone isn't proof of hung; check log tail too.
- **REJECT** Item 3 — Generate briefs for Will + Jackson Niketas. Kay said no briefs necessary; corrected name to **Will Bressman** (not Bruce Krasnow), at BK Growth (one of Kay's main investors). Will Bressman + BK Growth verified in Attio (record_ids `bc13021f-0ed1-4d26-9665-14099a74f730` + `98aaac90-42ca-4c6d-9f10-8663159322c7`). Three relationship fields blank on Will's Attio record — flagged as gap.
- **APPROVE** Item 4 — Apply 5 critical calibration proposals (delegated to background agent, all 5 landed cleanly + auto-committed by iMac autocommit hook).
- **DEFER** Item 2 — [[entities/allison-allen|Allison Allen]] PWIPM Council reply (4th day carried; women-network-priority + pest mgmt Active-Outreach lens; not actioned today).
- **DEFER** Item 5 — Taft (Payal) vs KeyBank (Megan) Thu 5/14 dinner pick (week-long carry; not actioned today).

### MCP-first integration doctrine (graduated 2026-05-08)

- **APPROVE** Save MCP-first / API-second / ask-Kay-third doctrine to memory `feedback_integration_priority_mcp_api_local.md`. Precipitated by Phase 4 design near-miss where original architecture watched iMac local Granola cache before realizing the Granola MCP server (`https://mcp.granola.ai/mcp`) was already wired and used by 3 existing skills.
- **APPROVE** Add CLAUDE.md preflight block `### Before building any new skill or skill integration` so the rule loads every session, not just on memory recall.
- **APPROVE** Add Step 0 `Integration Priority Check` to `create-agent-skills` SKILL.md so the rule fires at the action moment when actually authoring/modifying a skill.
- **APPROVE** Multi-layer defense: memory + CLAUDE.md preflight + SKILL.md step. All three reference each other so the rule survives if any one layer drifts.

### Phase 4 design (Granola sidecar handoff)

- **REJECT** Original A/B/C iMac→server sync mechanisms (commit-push, rsync over Tailscale, launchd WatchPaths-rsync). Scoped wrong because they assumed iMac is the only listener.
- **APPROVE** Option 1 — Server-side polling via Granola MCP. Replaces iMac sidecar entirely. One source of truth across all 3 devices (iMac, MacBook, phone) via Granola Cloud.
- **APPROVE** 5-minute polling cadence (`OnUnitActiveSec=5min`). Rate-limit verdict GREEN at 0.07% of capacity (Granola docs: 25 req/5sec burst, 5 req/sec sustained). Webhooks confirmed not yet supported by Granola (on roadmap).
- **REJECT** 10-minute cadence (original plan). Faster cadence trivially safe and matches Granola AI-summary processing lag floor.
- **APPROVE** Strict sequencing: Phase 3.5 foundations FIRST, then Phase 4 rebuild. Avoids inverting sequencing where 1 skill drives 4 foundation decisions in service of itself. Foundations reusable for every other skill migration.
- **APPROVE** "All today" — Phase 3.5 + Phase 4 + cleanup all on 5/8 (Kay's call, originally framed as "weekend with breaks" but compressed to single-day push).

### Phase 3.5 foundations

- **APPROVE** Foundation check script `scripts/phase-3.5-foundation-check.sh` (5 checks: gog CLI, MCP reachability, vault sync, Slack webhook, Python deps). Idempotent, value-suppressing patterns for secret files per CLAUDE.md.
- **APPROVE** Install gogcli on Linux server via `brew install gogcli` (NOT Go source build). Linux bottle exists at homebrew-core (`x86_64_linux` + `arm64_linux`). Earlier auto-install fuzzy-matched `cargo-geiger` because foundation script searched for `gog` not `gogcli`.
- **APPROVE** Wrap iMac credentials.json (`{client_id, client_secret}` flat shape) in v0.15.1 Google Cloud Console format `{installed:{...}}` before scp to server. iMac runs gog v0.13.0; server v0.15.1 expects different format.
- **APPROVE** `gog auth tokens export ... --out /tmp/gog-token.json` (long flag, NOT `-o`) for v0.13.0 token export. Server-Claude's brief used `-o`; needed correction.
- **APPROVE** Option B for Linux gog keyring: `GOG_KEYRING_BACKEND=file` + `GOG_KEYRING_PASSWORD=<random-32>` env vars, persisted to `~/.bashrc` + `scripts/.env.launchd` (chmod 600).
- **REJECT** Option A — gnome-keyring + headless D-Bus. Fragile, brittle across boot, adds attack surface for one secret.
- **APPROVE** Single commit for foundation-check fix + hourly snapshot churn ride-along (matches repo's existing "update X" message style).

### Phase 4 implementation

- **APPROVE** Spawn implementation agent on server-side (not iMac). Server has live MCP, gog, vault sync — better env match for testing as it codes. Killed initial iMac agent (`a2d6454a4f1959f5c`) cleanly, re-briefed server-Claude.
- **APPROVE** 8 files committed in `55c2f31`: `scripts/post_call_analyzer_mcp_poll.py` (new), `headless-on-trigger-prompt.md` (replaced), `SKILL.md` (updated), `validate_post_call_analyzer_integrity.py` (updated), `systemd/post-call-analyzer-poll.{service,timer}` (new hand-authored), `schemas/vault/research-prompt.yaml` + `socrates-question.yaml` (new).
- **APPROVE** Hand-author systemd unit pair (NOT generator-emitted) — generator excludes post-call-analyzer because there's no source plist to translate (this is a fresh server-side detector).
- **APPROVE** 5th routing bucket `Thought Analysis` with sub-routes: factual unknowns → `brain/inbox/{date}-{slug}-research-prompt.md`; strategic frames → `brain/inbox/{date}-{slug}-socrates-question.md`. Tiebreaker: socrates-question for higher leverage.
- **APPROVE** Drop deferred-content gate (MCP returns server-summarized transcripts; lazy-flush problem dissolves).
- **APPROVE** Drop business-hours gate (server runs 24/7; no need for clock-based gating).
- **APPROVE** Idempotency keyed off Granola cloud meeting ID (NOT local doc_id).
- **APPROVE** iMac sidecar coexistence during shadow mode: both detectors share `processed.json`; whichever detector wins the race writes queue first, other no-ops on next tick.

### Granola MCP authentication on server

- **REJECT** `claude -p` subprocess approach for OAuth. Cross-process PKCE state breaks: in-process listener exits with subprocess; next subprocess has no flow to complete.
- **REJECT** Path A original (SSH tunnel + interactive Claude). Granola MCP `authenticate` tool didn't print URL inline — designed to auto-open desktop browser, fails silently on headless server.
- **APPROVE** Path A revised — interactive `claude` session on server with manual URL copy from browser → terminal. Single-process keeps PKCE state alive across `mcp__granola__authenticate` and `mcp__granola__complete_authentication` tool calls. Bypasses SSH tunneling entirely.
- **CONFIRMED** Granola MCP authenticated on Linux server. `mcp__granola__list_meetings` returns real data.

### Generator bug discovery + fix

- **DISCOVERED** `scripts/generate_systemd_units.py` was emitting `Environment=KEY=VALUE` without quoting. Any value with whitespace silently broke systemd parse. Blast radius: 7 .service files had silently-truncated POST_RUN_CHECK env vars (literally `python3` with no script path) — every one a missing-validator regression vs iMac launchd.
- **APPROVE** Patch with `format_env_line()` helper that wraps full assignment in `"..."` and escapes inner `"` and `\` per `systemd.exec(5)`.
- **APPROVE** Re-emit + reinstall all 7 affected services on server. Verify clean (`systemd-analyze --user verify`). Generator fix synced to iMac via git pull (verified `format_env_line` count = 4 in local file).

### Timer migration tonight (8 timers launchd → systemd)

- **APPROVE** Snapshot trio: `attio-snapshot-refresh`, `jj-snapshot-refresh`, `apollo-credits-refresh`. All 3 smoke-tested PASS, server timers enabled, iMac plists `launchctl unload`'d + moved to `~/Library/LaunchAgents-retired/` (reversible).
- **APPROVE** Morning briefing pair: `email-intelligence`, `relationship-manager`. Long-running (~1-2 hrs per fire) so can't real-time smoke-test; install + enable + verify cadence + trust Monday auto-fire. iMac plists stay active for shadow-mode coverage.
- **CORRECTED** Pipeline-manager isn't a scheduled skill (runs on-demand when Kay says good morning). Original "morning briefing trio" plan was a misnomer; it's a pair.
- **APPROVE** Daily skills: `deal-aggregator` (3 variants — standard + afternoon + friday) + `launchd-debugger`. Same install-and-enable pattern. iMac plists stay overnight; first auto-fire validation = `launchd-debugger` Saturday 5am, `deal-aggregator` Monday 6am.
- **APPROVE** Enable all 3 deal-aggregator variants on server (Mon-Fri 6am + Mon-Fri 14:00 + Friday 06:00 digest-mode). iMac fired all 3; missing 2 on server would be a regression.
- **DEFER** `nightly-tracker-audit` migration to Saturday. Mutates Google Sheets; shadow-mode (both fire) creates double-write risk. Cutover (not shadow) is the correct pattern, best done with eyes-on Saturday morning.
- **DEFER** Stagger Friday 6am collision (`deal-aggregator` + `deal-aggregator-friday` both fire 6am Fri). Pre-existing iMac pattern, not a regression we introduced. Tag for post-conference cleanup.
- **DEFER** Add lighter "did artifact land" validator to deal-aggregator. Pre-existing gap (not introduced tonight). Tag for Phase 4.5 cleanup batch.

### MacBook conference-prep

- **DISCOVERED** 899 MB corrupt `~/.zshrc` on MacBook from heredoc-recursion gotcha. The pattern `cat >> ~/.zshrc << 'EOF'` with `source ~/.zshrc` inside the captured body never terminated cleanly, AND each shell startup re-sourced and re-appended → exponential blowup. MacBook-Claude diagnosed + rewrote clean 5-line file + backed up corrupt version to `~/.zshrc.corrupt-2026-05-08.bak`.
- **APPROVE** MacBook Tailscale install + sign-in (kay.s@ identity). Granola already pre-installed on MacBook.
- **APPROVE** vps function added to MacBook `~/.zshrc`: `vps() { ssh -t ubuntu@100.67.36.25 'bash -lc "cd ~/projects/Sapling && claude"'; }`. SSH test PASS to `agent-vps-7731c88b`.
- **CONFIRMED** gog CLI already installed on MacBook (v0.12.0 at `/opt/homebrew/bin/gog`, credentials present, `gog auth list` returns `kay.s@greenwichandbarrow.com`). Step 6 of MacBook checklist already done. No transfer needed.
- **NOTED** gog version drift across machines: MacBook 0.12.0 / iMac 0.13.0 / server 0.15.1. CLI syntax shifted between versions (`gog accounts list` v0.13 vs `gog auth list` v0.15+). Cleanup item — `brew upgrade gogcli` on iMac + MacBook in future session.

### Will Bressman + BK Growth Attio gap

- **DISCOVERED** Will Bressman (will@bkgrowth.com, Partner at BK Growth, one of Kay's main G&B investors) has 3 relationship fields blank on Attio: `nurture_cadence`, `relationship_type`, `how_introduced`, `next_action`. Vault entity does NOT exist (only `will-cotton.md` is in `brain/entities/`). BK Growth company entity also missing despite the 4/10 call note tagging `client/bk-growth`.
- **DEFER** Create `entities/will-bressman.md` + `entities/bk-growth.md` vault entities. Not blocking tonight; surface when Will-related work next surfaces.

### Harrison Wells status update

- **DRAFTED** Harrison email: full 6-step checklist completed + a few cron migrations still working through. Phase 4 stripped from peer message (Harrison doesn't know about it; outside his scope). Plain text per `feedback_drafts_no_blockquote`.

## Actions Taken

### Phase 3.5 foundations
- **CREATED** `scripts/phase-3.5-foundation-check.sh` (executable, 7136 bytes). Pushed in `c911e86`.
- **EXECUTED** Foundation check on server: 12/12 green after gog install + credential transfer + keyring config.
- **TRANSFERRED** gog credentials iMac → server via Tailscale scp (`/tmp/gog-client.json` wrapped in v0.15.1 format + `/tmp/gog-token.json` exported via `gog auth tokens export ... --out`). Local /tmp wiped after transfer.
- **CONFIGURED** Server gog with `GOG_KEYRING_BACKEND=file` + `GOG_KEYRING_PASSWORD=<random-32>` in `~/.bashrc` + `scripts/.env.launchd`. Live API verification: real Gmail labels returned.

### Phase 4 implementation
- **COMMITTED** `55c2f31` (server-side): 8 files, 891 insertions / 165 deletions. Phase 4 architecture deployed.
- **AUTHENTICATED** Granola MCP on Linux server via interactive same-session PKCE workaround.
- **COMMISSIONED** Phase 4 with real call traffic. AI Friday webinar (today's 1pm) processed end-to-end: vault note + Slack ping + iMac dedup verified.

### Generator bug fix
- **PATCHED** `scripts/generate_systemd_units.py` with `format_env_line()` helper.
- **RE-EMITTED** + reinstalled 7 affected services on server. All verify clean post-fix.

### Timer migration (8 timers enabled)
- **ENABLED** + smoke-tested 3 snapshot timers on server: attio + jj + apollo. Next-fire 18:00 EDT today.
- **RETIRED** 3 iMac plists: `~/Library/LaunchAgents-retired/com.greenwich-barrow.{attio,jj,apollo}-snapshot-refresh.plist`.
- **ENABLED** 5 long-running timers: email-intelligence (Mon 7am), relationship-manager (Mon 6:50am), deal-aggregator + afternoon + friday variants, launchd-debugger (Sat 5am).
- **VERIFIED** systemd-analyze clean for all enabled units; POST_RUN_CHECK env vars correctly populated post-generator-fix.

### MacBook setup
- **INSTALLED** Tailscale on MacBook (homebrew cask) + signed in with kay.s@ identity. MacBook now in tailnet at `100.65.50.2` as `kays-macbook-air`.
- **REWROTE** MacBook `~/.zshrc` clean (via MacBook-Claude) — 5 lines, vps function added, corrupt 899 MB version backed up to `.corrupt-2026-05-08.bak`.
- **VERIFIED** SSH from MacBook → server via Tailscale: `ssh ubuntu@agent-vps-7731c88b 'hostname && date'` returned `agent-vps-7731c88b` + current time.
- **CONFIRMED** gog on MacBook (v0.12.0) already authenticated, no setup needed.

### Calibration applied (5 critical proposals)
- **APPLIED** Proposal #1 — Pipeline-manager preflight covers D+0 + D+1 (`.claude/skills/pipeline-manager/SKILL.md`).
- **APPLIED** Proposal #2 — Strip trace emission from task-tracker `append` verb (SKILL.md updated; **code change in `scripts/task_tracker.py` still owed**).
- **APPLIED** Proposal #3 — New CLAUDE.md preflight "Before adding any new template, cadence step, decision branch, or threshold."
- **APPLIED** Proposal #4 — Voice doctrine bullets added to "Before writing any external message" + new memory `feedback_no_soft_signal_stacking.md`.
- **APPLIED** Proposal #5 — Refresh outdated POST_RUN_CHECK memory index line in MEMORY.md.
- Calibration deliverable status: `applied` (was `draft`).

### Memory updates
- **CREATED** `feedback_integration_priority_mcp_api_local.md` (MCP-first / API-second / ask-Kay-third doctrine).
- **CREATED** `feedback_no_soft_signal_stacking.md` (calibration #4).
- **UPDATED** MEMORY.md index with both new entries + broadened POST_RUN_CHECK index line.

### CLAUDE.md updates
- **ADDED** Pre-flight block `### Before building any new skill or skill integration` after `### Before research / network discovery`.
- **ADDED** Pre-flight block `### Before adding any new template, cadence step, decision branch, or threshold` (calibration #3).
- **ADDED** 3 voice bullets to `### Before writing any external message` section (calibration #4).

### create-agent-skills SKILL.md
- **ADDED** `### Step 0: Integration Priority Check (MANDATORY before any design)` before existing Step 1 (Choose Type). Cites `feedback_integration_priority_mcp_api_local.md`.

### Drafted (not sent)
- Harrison Wells status update — peer email summary of Phase 3.5 + timer migration progress (Phase 4 stripped per scope).

## Deferred

- **2026-05-09 (Saturday)** Migrate `nightly-tracker-audit` from iMac launchd to server systemd. Cutover pattern (not shadow) because it mutates Google Sheets. Eyes-on validation Saturday morning.
- **2026-05-09 (Saturday)** Build `vps-toolkit` (or `server-ops`) skill — teaches Claude vps alias semantics, `claude -p` subprocess + ssh patterns, install_systemd_units workflow, and the canonical paste-block-to-server-Claude pattern. Per Harrison's email recommendation.
- **2026-05-11 Monday morning** Phase 4.5 cutover: validate first real Monday call processes cleanly through server detector. If green: `launchctl unload` iMac post-call-analyzer plist + delete or `.deprecated` rename `scripts/post_call_analyzer_poll.py` + strip "encrypted-cache decryption fallback" paragraph from SKILL.md.
- **This week** Carried 4th day in a row: [[entities/allison-allen|Allison Allen]] PWIPM Council reply.
- **This week** Carried week-long: Taft (Payal) vs KeyBank (Megan) Thu 5/14 dinner pick.
- **Post-conference cleanup** Stagger `deal-aggregator-friday` cadence (currently Friday 6am collides with main `deal-aggregator`). One-line plist edit + regenerate. Pre-existing iMac pattern, not a regression.
- **Post-conference cleanup** Add lighter "did artifact land" validator to deal-aggregator. Pre-existing gap, in the "unhardened skills" bucket.
- **Future session** Apply remaining 12 deferred calibration proposals (10 high + 6 medium + 1 low).
- **Future session** `brew upgrade gogcli` on iMac + MacBook to sync versions (currently 0.12 / 0.13 / 0.15.1).
- **Future session** Code change in `scripts/task_tracker.py` to flip `append` verb from trace-emit to log-emit (calibration #2; SKILL.md doc updated, code change still owed).
- **Future session** Create vault entities `will-bressman.md` + `bk-growth.md`. Populate Will's Attio relationship fields (nurture_cadence, relationship_type, how_introduced, next_action all blank).
- **Future session** Migrate remaining 5-7 weekly-cadence timers (conference-discovery, niche-intelligence, weekly-tracker, calibration-workflow, jj-operations-sunday, weekly-snapshot, weekly-archive-export). Most fire weekly so non-urgent.

## Open Loops

- **Phase 4.5 cutover** — gated on Monday's first real call processing cleanly through the server detector. iMac sidecar in shadow mode through the weekend.
- **Email-intelligence + relationship-manager Monday 6:50/7am** — first server-side auto-fire. If both produce clean artifacts matching iMac's parallel run, retire iMac plists Monday afternoon. If either fails, stay on iMac and debug.
- **launchd-debugger Saturday 5am + deal-aggregator Monday 6am** — first server-side auto-fires. Same shadow-mode validation pattern.
- **Granola MCP token persistence** — token landed on disk via interactive Claude session. Future `claude -p` subprocesses (including the systemd timer's detector calls) inherit auth. Watch for token expiration / refresh handling in subsequent days.
- **gog CLI on server** — currently working but `gog accounts list` syntax (used today on iMac) vs `gog auth list` (correct on v0.15.1) is a low-grade footgun. Cleanup planned with brew upgrade.
- **MacBook ~/.zshrc.corrupt backup** — 899 MB file at `~/.zshrc.corrupt-2026-05-08.bak`. Safe to delete after Kay confirms vps alias works clean.
- **6-8 weekly-cadence timers** still on iMac launchd. Most fire weekly so won't be tested until next week's cycle. Migrate as time allows.
- **Generator pattern** — when next regenerating systemd units from iMac, the patched generator (`format_env_line`) is now in place. Risk: if someone later edits `generate_systemd_units.py` and removes the helper, silent regression returns. Worth a unit test in a future session.
