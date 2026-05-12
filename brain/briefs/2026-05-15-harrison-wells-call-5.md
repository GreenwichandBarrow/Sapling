---
schema_version: "1.0.0"
date: 2026-05-15
type: brief
title: "Coaching Call Prep: Harrison Wells (Call #5)"
people: ["[[entities/harrison-wells]]", "[[entities/kay-schneider]]"]
companies: ["[[entities/dodo-digital]]", "[[entities/greenwich-and-barrow]]"]
tags:
  - date/2026-05-15
  - brief
  - person/harrison-wells
  - person/kay-schneider
  - company/dodo-digital
  - company/greenwich-and-barrow
  - topic/ai-coaching
  - topic/claude-infrastructure
  - topic/server-migration
  - topic/post-call-analyzer
  - topic/family-office-personal-project
  - topic/learnings-md
  - source/claude
---

# Coaching Call Prep: Harrison Wells (Call #5)
Friday 2026-05-15, 12:00-1:00pm ET
Format: G&B pre-circulates challenges list; Harrison comes with concrete recommendations.

---

## Relationship Arc

- **2026-03-05** — First session (Harrison <> G&B). Connected via Fireflies. Initial scope: Claude Code architecture.
- **2026-03-11** — AI session #2. Architecture deep-dive.
- **2026-03-13** — Reschedule turn for AI session #3.
- **2026-03-16** — AI session #3. Workflow architecture + sub-agent patterns + learnings.md concept + Mac-overnight cron viability.
- **2026-03-20** — Invoice paid (inbox closed).
- **2026-03-24** — Launchd advice exchange.
- **2026-04-30** — Coaching session #4 (vendor classification). G&B caught Harrison up on a month of self-directed build. Harrison reframed next phase = operational reliability. Engagement scope locked: $1,200/mo, up to 2 hrs 1:1 + async, Stripe monthly. **Action items Harrison committed:** Server Setup + Tailscale walkthrough email, Engagement scope/invoice (received + paid), "Ask Harrison" MCP install email, name of secure-API-key tool. **Action items G&B committed:** Hetzner migration, /think (later /socrates) skill, learnings.md per skill, 1Password CLI for keys.
- **2026-05-08** — Harrison's "all up and running?" email (Fri 20:29).
- **2026-05-10** — G&B drafted bullet-list follow-up reply (cmux, 1P server vault migration, MCP-first/API-second/local update, Socrates skill, Command Center on server with iPhone home-screen). Held for Sunday-send rule.
- **2026-05-11** — G&B sent the Monday-morning follow-up (Magic DNS live edit) with 5/15 agenda teaser: Family Office personal project setup discussion.

---

## Current Engagement Stage

- **Engagement:** Active, month-to-month, $1,200/mo (Stripe). Renews on the 1st.
- **Format change from prior cadence:** G&B sends prep list in advance (this brief operationalizes that).
- **Outstanding from 4/30:** "Ask Harrison" MCP install email + secure-API-key tool name. Neither arrived. Mark for live mention.

---

## Agenda — Ordered by Priority

### 1. Granola transcript → folder trigger analysis (post-call-analyzer pipeline)

**The pipeline:** server `post-call-analyzer-poll.timer` polls every ~5 min via Granola MCP, gates on `started_at + 90min` buffer (Granola exposes no `ended_at` per `project_granola_mcp_shape.md`), pulls transcript when content lands, writes vault call note, drafts follow-up Gmail, posts ONE Slack per call.

**The issue:**
- 2026-05-12 morning email-scan-results recorded: *"Granola MCP OAuth requires re-auth — `mcp__granola__authenticate` surfaced as the only available tool; headless run cannot complete the PKCE callback. No Granola meetings ingested this fire; if any calls happened since last successful poll, they remain queued."*
- Server is headless. PKCE OAuth state lives in-process. Per `feedback_granola_mcp_same_session_pkce.md`, the only working pattern is: interactive `claude` session on server → `authenticate` → manually relay the failed-callback URL from a Mac browser back into the SAME session → `complete_authentication`. Scheduled `claude -p` subprocesses can't span the two tool calls.
- So every time the Granola MCP token expires, the scheduled poll breaks silently and G&B has to ssh in and manually re-auth interactively.

**Question for Harrison:**
- How do other Dodo Digital clients survive PKCE-OAuth MCPs on headless servers — is there a token-refresh pattern, a long-lived service-account path, or is the answer "switch to Granola Enterprise API key for static auth"? Are you aware of any Granola roadmap on a public API or webhook that would let us bypass MCP entirely?
- Secondary: if no good answer, what's the cleanest re-auth detector? Right now the discovery happens via the morning email-scan-results note. A Slack alert the moment the MCP returns only `authenticate` would close the loop.

### 2. Family Office personal project — separate-but-adjacent architecture

**Framing (from 5/10 session-decisions + 5/11 email teaser):** separate project for running G&B's principal's household (household ops, family finances, calendar, kids/dog, etc.), separate from G&B work. Want Harrison's input on:
- **Repo strategy** — new repo, sub-repo, or sibling vault inside same repo?
- **Vault strategy** — separate Obsidian vault, sub-vault inside Sapling, or shared vault with namespace separation (`brain/family/` vs `brain/`)?
- **How to operate two side-by-side cleanly** — context contamination (entities leaking across), MCP/credential isolation (different Google account?), launchd vs systemd job scoping, single-CLAUDE.md vs project-CLAUDE.md.

**Question for Harrison:**
- Have you seen the family-office-on-Claude pattern at any other client? What's the canonical separation? Specifically: is the right cut at **repo level** (full isolation, two Claude Code workspaces) or **project level** (one repo, two CLAUDE.md projects, one shared skills library)?
- How to keep cross-project pollution from memory/MEMORY.md? Two indices or namespace prefixes?

### 3. Other infra issues to surface

Pull from 5/10 session-decisions "Deferred" section + open loops.

| Item | Status | Question for Harrison |
|---|---|---|
| **15 iMac-path files in `scripts/`** | Path-sweep needed; some scripts still reference Mac paths post-Hetzner cutover | Worth a one-shot grep-and-replace pass with a regression test, or a per-file audit? |
| **Per-service systemd `EnvironmentFile` audit** | P2 bead; every fire emits ~7 "Ignoring invalid environment assignment 'export VAR=op://...'" warnings because systemd doesn't support `export` or resolve `op://`. Some services may legitimately need keys at process start | Best pattern: ExecStartPre op-inject drop-in, shell wrapper, or remove `EnvironmentFile=` per-service? Industry default? |
| **`bd` CLI not installed on VPS** | Working around via `scratch/{date}-pending-beads.md` holding pen — friction for VPS-primary trial | Install path + auth — is `bd` storage local-only or syncable via git? |
| **learnings.md propagation across ~42 skills** | Promised 4/30; pilot landed on pipeline-manager; remaining ~41 skills don't have it yet | Auto-generation pattern, or human-curated per-skill? Stop-hook pattern for "before/after" loading? |
| **Conference-discovery 5/10 corruption regression** | Sunday 5/10 run moved "week of" section dividers + changed some "attending events" dropdown values despite validator. Same regression class that triggered the 2026-05-04 hardening | Why did the existing `validate_conference_discovery_integrity.py` not catch this? Three hypotheses: (a) check missing for non-append-zone movement, (b) check missing for dropdown-value preservation, (c) agent routed around the validator. Want a read on the safer design — strict cell-range allowlist, or content-hash diff outside append zone? |
| **Mutating skills with no POST_RUN_CHECK** | deal-aggregator (3 variants — main + --afternoon + --digest-mode) noted in `project_deal_aggregator_validator_gap.md` as Phase 4.5 cleanup | OK to ship per existing pattern, or want a different shape for read-mostly skills? |
| **"Ask Harrison" MCP + secure-API-key tool name** | Both promised 4/30, neither arrived | Just remind live. |

---

## What to Push For (this call)

1. **Concrete Granola MCP re-auth path** — either a vendor workaround or a confirmation that "switch to Enterprise API key when available" is the right plan.
2. **Architectural verdict on Family Office split** — G&B needs a decision, not a discussion. Push Harrison to recommend repo-level vs project-level.
3. **Validator-design pattern for the conference-discovery regression class** — Harrison's specialty. Cell-range allowlist or content-hash diff?
4. **Two outstanding email asks closed** — Ask Harrison MCP install instructions + secure-API-key tool name.

---

## What to Share About G&B Since 4/30

Light context only — most landed in the 5/11 email already:
- cmux deployed (multi-session terminal multiplexer).
- 1P server vault migration complete (7/7 production secrets on `op://` references).
- MCP-first/API-second/local-only-with-principal-approval doctrine codified in CLAUDE.md.
- Socrates skill (similar to Hermes pattern) built and registered. Three-phase pipeline: `/socrates → /plan → execute`.
- Command Center on server, iPhone home-screen access via Magic DNS + Tailscale Serve.
- Phase 4.5 complete: Mac sidecar for post-call-analyzer retired; server timer is sole processor.
- VPS-primary trial in effect since 5/10 evening.

## What NOT to Over-Share

- Pipeline-specific deal names (Harrison is infra coach, not deal partner).
- Family Office personal-life logistics beyond the architectural question.
- LP names or investor-update specifics.

---

## Open Questions Carried From 4/30

1. Server Setup + Tailscale walkthrough email — received & executed; Hetzner cutover complete. **Close.**
2. Engagement scope + invoice — received & paid 5/1. **Close.**
3. Ask Harrison MCP install email — NOT received. **Surface.**
4. Name of secure-API-key tool he was blanking on — NOT received. 1P CLI ended up being the route. **Surface as "we picked 1P; what was the tool you were thinking of?"**

---

## Logistics

- **Source of truth for the call:** vault entity [[entities/harrison-wells]], call notes in [[calls/2026-04-30-harrison-wells-coaching-session]], `brain/inbox/2026-05-01-prep-harrison-call-may-15.md`, `brain/context/session-decisions-2026-05-10.md`.
- **Gmail thread:** live Gmail fetch unavailable this session (GOG keyring not decryptable in subagent context); rely on 5/10 session-decisions for the email content. The Sunday draft + Monday send-with-Magic-DNS-live edit is the latest correspondence.
- **Granola call ID for the call note:** to be assigned post-call via post-call-analyzer (assuming Granola MCP re-auth is complete by Friday 12pm).

---

## Calibration Notes

- 4/30 Granola auto-summary captured 4 of 9 action items (44%). Coaching/strategy calls need full-transcript re-read post-call. Apply same rule to this call note.
- Format-change discipline: G&B pre-circulates challenges list (this brief). Harrison comes with recommendations. Don't let the call drift into discovery mode — that defeats the format change agreed 4/30.
