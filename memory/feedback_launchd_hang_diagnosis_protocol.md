---
name: Launchd "hang" diagnosis protocol — verify before escalating
description: Before reporting a scheduled skill as hung/failed based on log appearance, check launchctl exit codes + artifact mtime + file open-handle count. Headless claude runs buffer output and look frozen for 60+ minutes even when running normally.
type: feedback
originSessionId: f8be9c15-9637-4853-b0f6-7cf93e164c94
---
Before escalating a scheduled skill as "hung" or "failed" based on log appearance, run the verification protocol. **Headless claude runs buffer output and only flush at completion** — a log frozen at "attempt 1 of 3" for 60+ minutes can be a normal long-running execution, not a hang.

**Verification protocol (in order):**
1. `launchctl list | grep greenwich | grep <skill>` — check the **last exit code column**. Exit 0 = ran clean even if log looks frozen. Non-zero = real failure.
2. `ls -la <expected artifact path>` — check artifact mtime. If freshly written, the run completed.
3. `ps aux | grep -E "claude.*<skill>" | grep -v grep` — orphan claude processes still running? If yes and parent PID is `launchd` (PID 1), it's a real hang. If parent is a user shell (`zsh -il`), it's an interactive Kay session, not a launchd-spawned hang.
4. Tail the latest log file fully — sometimes the completion line ("Finished claude run: ..., exit: 0") is at the bottom but mid-log appears stalled.

**Known cause of slow-but-clean runs:** MCP server retries against rotated/stale credentials add 2-3 minutes per call. Right after a credential rotation (Apollo, Attio, etc.), expect 70-80 min runtimes for skills that hit those MCP servers heavily — they DO complete, just slowly. Cache stabilizes within 24h.

**Why:** I escalated email-intelligence + relationship-manager as "hung" on 2026-04-28 morning briefing. Both ran cleanly to completion in 70-80 min (3-4x normal because of 4/27 MCP rotation aftermath). Wasted Kay's attention on a non-issue and required me to retract a briefing item. Same pattern almost certainly will recur after future credential rotations or any skill that writes infrequently.

**How to apply:**
- Treat "log frozen" as a NEUTRAL signal, not a failure signal.
- Never escalate to a 🔴 briefing item based on log appearance alone.
- Use the protocol's 4 checks. If all four pass (exit 0, artifact fresh, no orphan processes, completion line in log), the run is fine — say so or stay silent, don't escalate.
- If any check fails, THEN escalate with specific evidence ("exit 137 = OOM kill" / "artifact mtime 96h stale" / "orphan PID 12345 parented to launchd").

**Optional future hardening (not blocking):** Add `stdbuf -oL -eL` wrapper around `claude -p` invocations in `scripts/run-skill.sh` so output flushes line-by-line and removes the false-frozen appearance. Also worth adding per-attempt `timeout 1800` so a TRUE hang gets killed for retry — currently no per-attempt timeout exists, which IS a real gap if something genuinely hangs.

**Precedent:** 2026-04-28 morning briefing #2 (retracted same session). Investigation by background agent confirmed both jobs ran to completion at 8:09am (email-intel) and 8:10am (rel-manager) with exit 0.
