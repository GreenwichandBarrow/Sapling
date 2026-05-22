---
schema_version: 1.1.0
date: 2026-05-18
review_status: applied
type: trace
title: "Mac and MacBook are thin SSH clients into one VPS — no local repos, no Mac↔VPS git sync"
trace_type: infra-architecture
tags: ["date/2026-05-18", "trace", "topic/vps-workflow", "topic/server-migration", "status/resolved"]
---

# Mac and MacBook are thin SSH clients into one VPS — no local repos, no Mac↔VPS git sync

## Trigger

Kay said she was traveling and switching from her Mac to her MacBook, and asked what the transition setup should be. Claude initially gave a Mac↔VPS git-sync runbook ("`git pull origin main` on the Mac before starting, commit + push before stopping, watch for double-firing Mac launchd jobs"). Kay corrected: **"the macbook and mac both access through vps now. nothing on cursor or direct terminal."**

## Decision

There are **no local clones** of the Sapling repo on the Mac or MacBook, no Cursor, no local/direct terminal work. Both machines are pure Tailscale-SSH windows into the single VPS (`agent-vps-7731c88b`), which holds the only repo, the running session, the scheduled systemd jobs, and the continuation files. "Switching machines" = reconnect to the same VPS from the other machine and run `/pickingback`. There is no pull, no push-before-stop, no merge, no double-launchd risk, no branch-divergence dance.

## Alternatives considered

1. **Mac↔VPS git sync model** (what Claude first advised) — assumes each machine has a local repo that pulls/pushes to origin. Was true historically (see [[project_branch_divergence_imac_vs_main]] — iMac branch 419 commits ahead). **Now false** and actively misleading: instructing a `git pull` on a machine with no repo wastes Kay's time and implies a sync burden that doesn't exist.
2. **VPS-primary "trial" with Mac as secondary/read-only via git pull** ([[project_vps_primary_workflow]] as written 2026-05-10) — directionally right but stale: it still framed Mac as a git-pulling secondary surface. Kay's statement removes the local surface entirely.
3. **Thin-client model: both machines are SSH terminals into one VPS, no local state** — chosen. Matches Kay's explicit correction and the Harrison Wells migration goal ("iMac/MacBook conference-interchangeable; server = single source of truth").

## Reasoning

The branch-divergence problem ([[project_branch_divergence_imac_vs_main]], "pick a/b/c") is not *solved* by picking a merge strategy — it is **dissolved**: with no local repos there is nothing to diverge. Treating the old git-sync mental model as current produces confidently wrong transition advice every time Kay changes machines or travels. The correct answer to "how do I transition machines" is now trivial (reconnect + `/pickingback`), and the correct answer to any "should I commit/pull to sync the Mac" is "there is nothing to sync."

## Why this trace matters

Any future agent told "Kay is on her Mac / switching to MacBook / traveling" will, without this, regenerate the obsolete runbook (git pull, commit-before-stop, double-scheduler caution). All three are wrong under the thin-client architecture and cost Kay friction at exactly the moment she's mobile. The stale carry in `session-decisions-2026-05-18` Open Loop #4 ("Kay on MacBook must git pull origin main") is corrected as part of this close-out.

## Key insight

When an architecture change *removes* a problem class, retire the problem's memory — don't keep answering it. No local repo → no Mac↔VPS sync, no branch divergence, no double-launchd. Machine switch = reconnect + `/pickingback`, nothing more.
