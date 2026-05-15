# Calibration Proposal — 2026-05-14 (PENDING APPROVAL)

**Status:** No proposals applied. No traces archived. No VERSION bump. Apply-options prompt was dismissed; this file persists the synthesis so it can be acted on later (re-run `/calibrate` or apply specific items by number).

**Scope:** 35 traces from 2026-05-08 through 2026-05-14.
**Backlog flagged:** 115 unreviewed traces from 2026-04-10 through 2026-05-07 deferred to a follow-up calibration.
**Agents:** 3 analysts converged tightly. Coordinator polled but did not post a final synthesis post before the session converged; orchestrator (chat) synthesized directly from analyst returns.
**Chatroom:** `brain/traces/agents/2026-05-14-calibrate.md`

---

## Pattern Map (cluster summary)

| Cluster | Traces | Severity | Already in Memory? |
|---------|--------|----------|--------------------|
| A — Validator/wrapper hardening (silent-success archetype) | 5 | high | Partial (`feedback_signals_not_validation`) |
| B — 1Password / credential migration architecture | 7 | high | Partial (`feedback_all_skills_use_1password`, `reference_pbcopy_through_ssh_for_remote_secrets`) |
| C — Symlink / destructive-op safety | 1 | high | No |
| D — MCP-first doctrine + PKCE-on-headless | 2 | medium (confirming) | YES (3-layer applied); PKCE note missing from server CLAUDE.md |
| E — Task-tracker auto-emitted receipts (NOISE) | 15 | critical | No |
| F — Project-tab / Drive organization | 3 | low (confirming) | YES |
| G — Shell / zshrc heredoc | 1 | medium (confirming) | YES |

**Meta-pattern of the week:** Server migration was the dominant theme — 14 of 35 traces (40%) were Hetzner cutover, systemd hardening, or 1Password credential architecture. The recurring sub-pattern is **"silent success" failures** — operations that exit cleanly but produced wrong/no/destructive state. `feedback_silent_failures_are_the_core_concern.md` names the concern; this batch shows the defense pattern keeps being one-off rediscovered per case.

---

## Proposals (deduplicated, ranked)

### 🔴 CRITICAL (1)

#### 1. Suppress task-tracker rollback-receipt traces

- **Target:** `skill:task-tracker-manager` — `.claude/skills/task-tracker-manager/SKILL.md` + `scripts/task_tracker.py` (lines 486, 540, 852 per simplicity-advocate)
- **Source traces (15):** all `2026-05-12-task-tracker-schedule-to-day-slot-{mon,tue,fri}-*.md`, `2026-05-14-task-tracker-schedule-to-day-slot-{thu,sat}-1.md`, `2026-05-12-task-tracker-promote-mon-{8,9}.md`, `2026-05-12-task-tracker-sync-done-status-synced-2.md`, `2026-05-11-task-tracker-archive-apr-27-may-3.md`, `2026-05-11-task-tracker-projects-create-gantt-deal-aggregator-expansion.md`
- **Importance:** critical
- **Proposed by:** all 3 agents independently
- **Change:** Extend the existing 5/8 `append`-silence to the verb set `[append, schedule-to-day-slot, promote, sync-done-status, archive, projects-create-gantt]`. Receipts route to `logs/scheduled/task-tracker-{date}.log` instead of `brain/traces/`. Trace ONLY when verb encounters non-trivial reasoning (promote-refused with reason, ambiguity surfaced, conflict detected). Update SKILL.md guardrail #4 to list the silenced verbs and rationale ("Slot-placement and promote are scheduling actions, not decisions between alternatives").

### 🟡 HIGH (4)

#### 2. Bulk-archive backlog receipts before next calibration

- **Target:** process / one-shot script
- **Source:** general observation (115-trace backlog 4/10-5/7)
- **Importance:** high
- **Proposed by:** simplicity-advocate, pattern-recognizer
- **Change:** Run `grep -L "## Reasoning\|## Decision\|## Alternatives" brain/traces/*task-tracker*.md` against the 4/10-5/7 backlog. Bulk-move receipt-shaped files to `brain/traces/_archive_receipts/` (preserves audit trail, removes from active calibration scope). Estimate: cuts backlog from 115 → ~60-70 substantive traces. **Prerequisite:** lands after #1 so the script silences future emissions before sweeping the past.

#### 3. Validator-doctrine memory: positive-signal + authoritative-source binding

- **Target:** `memory:feedback_validator_doctrine` (new file)
- **Source traces:** `2026-05-08-systemd-environment-quoting-bug`, `2026-05-09-load-env-grep-quoted-values`, `2026-05-10-systemd-envfile-per-service-not-blanket`, `2026-05-12-rogue-status-validator-codification`, `2026-05-08-mutating-skill-shadow-mode-unsafe`
- **Importance:** high
- **Proposed by:** architecture-strategist, pattern-recognizer
- **Change:** Create `memory/feedback_validator_doctrine.md` with three rules:
  - (a) Validators must print **structured success markers** the wrapper greps for — exit-0 alone is insufficient (no-op trivially exits 0; POST_RUN_CHECK="python3" without a script will silently pass).
  - (b) Validators reference **authoritative source for legal value sets** (Sheets data-validation rule, dropdown definition, schema enum) at validator-load time — never accumulate from observed state. Hand-maintained `ALLOWED_*` constants drift and codify rogue values.
  - (c) Classify **mutating skills as cutover-only** before migration; shadow-mode assumes idempotency that mutating skills don't have.
  - Add MEMORY.md index entry. Cross-reference from `feedback_signals_not_validation.md` and `feedback_silent_failures_are_the_core_concern.md`.

#### 4. Destructive-operation PreToolUse hook (NOT a CLAUDE.md preflight)

- **Target:** `hook:new:destructive_op_guard` — `.claude/hooks/router/handlers/destructive_op_guard.py` + 1-line ref in `claude-md`
- **Source trace:** `2026-05-10-memory-migration-copy-first-not-rm-first`
- **Importance:** high
- **Proposed by:** all 3 agents (architecture proposed CLAUDE.md → simplicity challenged → pattern agreed → resolved as hook)
- **Change:** Build a PreToolUse hook that detects `rm -rf`, `unlink -r`, `ln -sfn` (symlink-replace) patterns where source/target paths overlap or live under repo/memory/.config. Forces a printed `ls -la` enumerate-and-compare gate (env var `DESTRUCTIVE_OP_VERIFIED=1` or `--force-after-enum` flag). Matches `secret-file-guard` and `gog-sheets-delimiter-guard` hook precedent. Add 1-line cross-ref in `/home/ubuntu/projects/Sapling/CLAUDE.md` under "Before handling secrets" pointing at the hook (no new preflight section — protects always-loaded context).

#### 5. Add "skill rollback receipts" anti-pattern to decision-traces

- **Target:** `skill:decision-traces` — `.claude/skills/decision-traces/SKILL.md` `<anti_patterns>` section
- **Source:** general observation (5/8 `append` calibration + 5/14 `promote`/`schedule` calibration)
- **Importance:** high
- **Proposed by:** simplicity-advocate
- **Change:** Add anti-pattern #6: "Skill rollback receipts — `{verb} executed, snapshot at /path, rollback via cp X Y`. Test: Is there reasoning? Are alternatives named? If the trace is purely 'what happened + where to undo it,' route to `logs/scheduled/{skill}-{date}.log` instead. Operational receipts are not decisions." Add a parallel note to `create-agent-skills` SKILL.md so new skills bake in the right output-channel decision up front.

### 🟢 MEDIUM (2)

#### 6. Credential-migration playbook memory (NOT a new skill)

- **Target:** `memory:playbook_credential_migration` (new file)
- **Source traces:** `2026-05-09-1password-integration-architecture`, `load-env-grep-quoted-values`, `op-personal-plan-vault-workaround`, `rotation-urgency-tiering`, `2026-05-10-pbcopy-through-ssh-secret-extraction`, `uuid-based-op-references`, `bashrc-clean-over-conditional-resolution`
- **Importance:** medium
- **Proposed by:** all 3 agents (architecture proposed skill → simplicity challenged → pattern agreed → resolved as memory)
- **Change:** Single playbook memory consolidating: (1) Classify rotation urgency (direct API key = same-session; channel-scoped = same-day; server-only = defer). (2) Extract via pbcopy-through-SSH (zero on-screen exposure). (3) Store in 1Password GB Server vault (not Personal — SA can't access). (4) Use UUID-based `op://` refs not title-based (em-dash trap). (5) Update `.env.launchd` to `op://` refs; verify load-env.sh substitution works. (6) Update consumer scripts/services per-service (audit, don't blanket-strip). (7) Clean bashrc/zshrc (no conditional `op read` magic). **Graduation rule:** if pattern fires 3+ times in a 12-month window, promote to skill (per `feedback_strategic_thresholds_need_grounding`).

#### 7. OAuth-on-headless note in user CLAUDE.md

- **Target:** `claude-md:user` — `/home/ubuntu/CLAUDE.md`
- **Source traces:** `2026-05-08-granola-mcp-same-session-pkce`, `2026-05-08-mcp-first-integration-doctrine`
- **Importance:** medium
- **Proposed by:** architecture-strategist, pattern-recognizer
- **Change:** Add 3-line note under "How to Help the User": "**OAuth/PKCE on headless server:** for any MCP/CLI requiring PKCE OAuth (Granola, future tools), run an interactive `claude` session on the server (not `claude -p`). PKCE state lives in-process; same-session callback URL relay is required. Don't attempt SSH port forwarding — the URL itself contains the auth code; just paste it back into the same interactive session." Cross-reference existing `feedback_granola_mcp_same_session_pkce` memory.

---

## Conflicts Resolved

| # | Issue | Architecture position | Simplicity / Pattern position | Resolution |
|---|-------|------------------------|--------------------------------|------------|
| 6 | credential-migration | New skill | Playbook memory (one-shot event, no recurrence pressure) | **Memory.** Graduate to skill if fires 3+ times. |
| 4 | destructive-op rule | New CLAUDE.md preflight section | PreToolUse hook (CLAUDE.md root already 280+ lines) | **Hook + 1-line CLAUDE.md ref.** Matches secret-file-guard precedent. |

---

## Learnings Only (no code changes)

- **Silent-success archetype** spans 6 high-importance traces this batch. The defense pattern (positive-signal verification with byte-payload smoke test) is being one-off rediscovered per case rather than systematized. Proposal #3 codifies it.
- **MCP-first integration doctrine** (cluster D) is fully graduated and producing confirming signals — no new action.
- **Drive/project-tab organization** (cluster F) is fully graduated — no new action.
- **Cross-validator audit follow-up:** scan `scripts/validate_*_integrity.py` for hand-maintained `ALLOWED_*` constants (~5 validators currently). Low-priority; #3 enables it.

---

## Open Loops

- **115 unreviewed traces** from 2026-04-10 through 2026-05-07 deferred to follow-up calibration after #1 + #2 land (otherwise calibration agents will burn tokens reading pre-fix `append` receipts).
- **Coordinator agent** polled the chatroom but did not post a final `→ CLOSE` synthesis post before the session converged. Orchestrator synthesized directly from analyst returns.

---

## Next Steps

To act on this proposal, choose one:

1. **Apply all 7 + commit** — tell me "apply all from 2026-05-14 proposal."
2. **Apply selected** — tell me "apply 1, 3, 4 from 2026-05-14 proposal" (etc.).
3. **Discuss before applying** — flag a specific proposal for refinement.
4. **Discard** — `rm .claude/calibration-proposals/2026-05-14-pending-review.md` (chatroom + analyst outputs would also need cleanup if unwanted).
