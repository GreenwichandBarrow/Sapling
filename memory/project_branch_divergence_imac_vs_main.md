---
name: Branch divergence — iMac branch is 419 commits ahead of main
description: RESOLVED 2026-05-18 — DISSOLVED, not merged. No local repos exist; Mac+MacBook are thin SSH clients into one VPS, so nothing can diverge. Historical record only; do not action a/b/c.
type: project
originSessionId: 326c69dd-5175-4205-89f6-eb4a9ec64ab8
---

> **RESOLVED 2026-05-18 — problem dissolved, not solved.** Kay confirmed
> *"the macbook and mac both access through vps now. nothing on cursor or
> direct terminal."* There are no local clones on any machine — both Mac and
> MacBook are SSH windows into the single VPS repo. With no local repo there
> is nothing to diverge: the a/b/c resolution choice below is **moot — do not
> action it**. This entry is retained for history only. See
> [[project_vps_primary_workflow]] resolution block + trace
> [[traces/2026-05-18-mac-macbook-thin-clients-single-vps]].

**State (as of 2026-05-06):** The iMac branch `imac-mid-day-save-2026-04-22` has accreted 419 commits since Kay last synced to main. Branch was originally created as a "save" branch on 2026-04-22 but became the de facto trunk because main was never touched.

Kay's MacBook tracks main (or a branch close to main). Until 2026-05-06, the MacBook had not seen ANY of the iMac's work since 2026-04-22 — including the socrates skill (created 2026-05-03), recent morning-briefing format changes, memory updates, today's bridge build, the post-call-analyzer spec, all entity edits, all calls/, briefs/, traces/, outputs/.

**Why:** Kay invoked `/socrates` on her MacBook today and it failed because the skill was not on main. Diagnosis surfaced the 419-commit gap.

**Quick fix applied 2026-05-06:** Cherry-picked socrates skill + slash command (`6bc0a91 update config`) onto main via worktree. Pushed as commit `dfdf7fe`. Kay's MacBook can now `git pull origin main` and use `/socrates`. **The structural gap remains** — only the socrates files were synced, not the other 418 commits' worth of work.

**How to apply:**
- Treat as an unresolved project — needs decision before drift compounds further.
- Three resolution options surfaced on 2026-05-06 evening:
  - **(a) Full merge iMac branch → main now.** One-shot catch-up. Risk: 419 commits is a lot to merge in one shot; conflicts grow with delay; uncommitted iMac state needs careful staging.
  - **(b) Rename iMac branch to `working` and have both machines track it.** Both machines pull/push to one shared working branch. No branch coordination ever. Recommended option per COO suggestion. Lowest ongoing complexity.
  - **(c) Status quo + cherry-pick on demand.** Keep main frozen, iMac branch as trunk, MacBook cherry-picks specific files when she notices gaps. Fragile. Today's socrates miss is what (c) looks like in practice.
- Open question for Kay: pick (a) / (b) / (c).

**Side effect to watch:** Future merges between main and the iMac branch will resolve cleanly because the same socrates file diff already exists on both. But if more cherry-picks accumulate before a full sync, divergence pattern may produce confusing merge conflicts later.

**Source:** Discovered during 2026-05-06 socrates skill push request. Worktree-based cherry-pick avoided disturbing 4 uncommitted local files (apollo/attio/external-services snapshots + new red-bridge script). Decision deferred to next session.
