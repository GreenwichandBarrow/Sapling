---
schema_version: 1.1.0
date: 2026-05-07
type: trace
title: "Server replaces Mac runtime, except Granola sidecar"
had_human_override: false
importance: high
target: "claude-md, process"
tags: ["date/2026-05-07", "trace", "topic/server-migration", "topic/granola", "topic/architecture", "status/locked", "pattern/single-source-of-truth"]
---

# Trace: Server Replaces Mac Runtime, Except Granola Sidecar

## Context

Kay signed up for Hetzner Cloud + Tailscale 2026-05-07 morning with the goal of running the AI Operations system on an always-on server instead of her Macs. The architectural choice — server as single source of truth (REPLACE) vs server as another node alongside Macs (MIRROR) — surfaced during Phase 2 planning of the Linux migration.

## Decisions

### Server runtime model
**AI proposed:** Hybrid (A2) — server is main brain, iMac is Granola sidecar.

**Chosen:** Server replaces Mac runtime entirely. Both Macs become thin clients that SSH (via Tailscale) into the server. Vault, scheduled jobs, dashboard, Claude sessions all live on the server. **One exception: Granola.** No Linux client; transcripts in `~/Library/Application Support/Granola/` only. Post-call-analyzer reads that local cache via launchd `WatchPaths` — stays on the iMac as a "Granola sidecar" with output sync to the server (Phase 4 follow-up).

**Reasoning:** Single source of truth eliminates the entire class of problems that consumed today's morning (436 commits ahead, two macOS hosts diverging, MacBook blind to iMac work). Once everything runs on the server, the Macs become interchangeable thin clients. Granola is the one workload that genuinely cannot move to Linux right now. Sidecar boundary is small (one launchd job, one Python poller, one output dir to sync) and well-understood.

**Pattern:** #pattern/single-source-of-truth

### Alternatives rejected
**AI proposed:** A1 (drop Granola integration), A3 (replace Granola with Linux-friendly tool), B (mirror — each Mac runs its own + server is a peer).

**Chosen:** Reject all three.

**Reasoning:** A1 retires real value (auto-extracted action items + decisions + email drafts from calls). A3 is a separate project with its own risks; revisit later if Granola becomes unstable. B doesn't solve branch divergence (today's iMac/MacBook/main split was the entire reason for provisioning a server) and keeps Mac as critical infrastructure.

## Learnings

The architectural rule going forward: **server runs everything by default; only Mac-locked apps stay on Mac.** Granola is currently the only Mac-locked dependency. Any future skill should default to server-resident; the burden of proof falls on any proposal to keep work on a Mac.

A future agent that doesn't know "Granola = macOS-only" might propose moving post-call-analyzer to the server during cleanup, breaking it silently. Same agent might propose mirroring Mac state to server thinking it's safer, reintroducing the divergence problem we just spent half a day fixing. Granola is the model exception — well-bounded, externally-imposed constraint — not a precedent for keeping things local.
