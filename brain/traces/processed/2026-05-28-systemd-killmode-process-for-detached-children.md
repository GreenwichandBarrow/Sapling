---
review_status: applied
schema_version: "1.1.0"
date: 2026-05-28
type: trace
title: "systemd KillMode=process required for `setsid nohup & disown` detached children in Type=oneshot services"
people: ["[[entities/kay-schneider]]"]
companies: ["[[entities/greenwich-and-barrow]]"]
tags:
  - date/2026-05-28
  - trace
  - person/kay-schneider
  - topic/systemd-cgroup-detached-children
  - topic/post-call-analyzer
  - topic/scheduled-skill-failure-mode
  - skill/post-call-analyzer
---

## Trigger

Kay reported zero Slack messages from post-call-analyzer all week (5/24-5/28), despite the skill's expected "ONE message per call to #ai-operations" behavior. Three calls had transcripts available in Granola (Oswaldo Ponce 5/26, Team TB JJ 5/27, Jeff Stevens 5/27) — none produced Slack output, none had the Google Doc analysis filed, none updated Attio notes via the scheduled fire. The 5/13 + 5/15 historical runs had succeeded (logs show "Slack: posted to #ai-operations"), so the pipeline was known-good at some point and silently broke.

## Decision

APPROVE — add `KillMode=process` to the `[Service]` block of `~/.config/systemd/user/post-call-analyzer-poll.service`, then `systemctl --user daemon-reload && systemctl --user restart post-call-analyzer-poll.timer`. Single-line unit edit, reversible, fixes the silent-failure for all future fires.

## Alternatives Considered

1. **Add `RemainAfterExit=yes` instead of `KillMode=process`.** Would keep the oneshot service marked active after ExecStart finishes, which prevents cgroup reap. Rejected: leaves the service in an "active" state perpetually, which corrupts `systemctl status` semantics for monitoring and breaks the launchd-debugger's exit-0-vs-running detection.
2. **Refactor the detached invocation to use `systemd-run --user --scope` from inside the poll script.** Would spawn the headless run in its own transient unit, fully escaping the parent cgroup. Rejected — larger change, requires reworking `scripts/run-skill.sh` invocation contract, and the wrapper is shared by 10+ skills.
3. **Move the headless analyzer from detached fire-and-forget to inline-execution inside the poll script.** Would simplify the architecture and remove the cgroup issue entirely. Rejected — poll script is `Type=oneshot` with `TimeoutStartSec=600` and headless Claude runs can take 5-15 minutes per call; running 3 calls inline would blow the timeout and block the next poll.
4. **Wait one more day to see if the racy cgroup-kill becomes deterministic-pass instead of deterministic-fail.** Rejected — Kay flagged the issue directly; downstream skills (Attio notes, To Do staging, morning briefing) depend on post-call-analyzer landing call outcomes; waiting compounds the damage.

## Reasoning

The poll script (`scripts/post_call_analyzer_poll.sh:109-114`) tries to detach the headless Claude run with `setsid nohup … & disown`. `setsid` creates a new session ID and a new process group, which is sufficient to escape a parent shell's job control. **But it does NOT escape systemd's cgroup-based process tracking.** systemd assigns every service a cgroup; when a `Type=oneshot` service's ExecStart PID exits and there is no `KillMode=process` directive, the default `KillMode=control-group` reaps every PID still associated with the cgroup — including detached children that thought they were free.

Evidence collected: 5/26 + 5/27 poll logs show "headless run launched (pid 1354754/1468457)" then immediate "poll complete" + `systemd: Finished` at the same second. The wrapper's `=== post-call-analyzer ===` header from `run-skill.sh` never appears in any per-call log file — meaning the wrapper never ran. `processed.json` shows the 5/26 + 5/27 calls got `processed_at: 2026-05-28T14:08:07` from a manual interactive run earlier today, not from the scheduled fires.

Ruled out: Slack webhook (env var matches, 5/13 + 5/15 succeeded), Attio token (separate from this path), Granola polling (logs show notes correctly queued).

Why it worked 5/13 + 5/15 and not the week of 5/24: cgroup-kill timing is a race between systemd's `sd_notify` ack of ExecStart completion and the child's `execv` of the wrapper. The race apparently became deterministic-fail after a systemd-user-manager package upgrade (suspected) or a kernel cgroup-v2 behavior change. Unimportant to confirm the trigger — the fix is correct regardless.

## Why This Trace Matters

This failure mode applies to ANY systemd `Type=oneshot` service that tries to spawn a detached long-running child via `setsid nohup & disown` or `&` + `disown` patterns. Future skills that use the same pattern (e.g., a `Type=oneshot` poller invoking a headless Claude run for niche-intelligence-mode-X, deal-evaluation-mode-Y, etc.) will hit this same trap. Default the unit to `KillMode=process` whenever the script intentionally detaches a child. If the child must outlive the parent, `KillMode=control-group` (default) is wrong.

Also matters as a Type=oneshot wrapper-design rule: oneshot services are for synchronous "do thing and exit" semantics. Fire-and-forget child processes are a deliberate design choice that requires explicit cgroup-escape configuration. The two patterns are not natively compatible.

## Key Insight

`setsid` escapes shell job control but NOT systemd's cgroup tracking. To make a detached child survive its systemd parent's exit, either (a) set `KillMode=process` on the parent service (kills only the ExecStart PID at exit, leaves the cgroup's other PIDs alone), or (b) spawn the child in its own transient unit via `systemd-run --user --scope`. The combination "Type=oneshot + child-via-setsid + no KillMode override" is broken-by-default and the breakage is racy enough to pass for weeks before becoming deterministic.
