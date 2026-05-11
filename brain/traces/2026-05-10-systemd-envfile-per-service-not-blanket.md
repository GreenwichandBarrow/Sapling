---
schema_version: 1.1.0
date: 2026-05-10
type: trace
importance: high
target: "doctrine:systemd-env-resolution"
tags: ["date/2026-05-10", "trace", "domain/infra", "topic/systemd", "topic/environment-file", "topic/1password-references", "topic/post-call-analyzer", "pattern/per-service-audit-not-blanket-fix", "status/applied"]
---

# Per-service audit, not blanket-strip, when fixing systemd EnvironmentFile op:// noise

## Trigger

Diagnosed `post-call-analyzer-poll.timer` at Kay's request and found the
service journal flooded — every 5-min fire emits ~7 lines like:

```
post-call-analyzer-poll.service: Ignoring invalid environment assignment
  'export ATTIO_API_KEY=op://GB Server/Attio API Key/password':
  /home/ubuntu/projects/Sapling/scripts/.env.launchd
```

Root cause: systemd's `EnvironmentFile=` directive doesn't support the
`export VAR=...` shell syntax and doesn't resolve `op://` URIs — it parses
only literal `KEY=value` pairs. The service still "Finishes" cleanly
because the poll script `post_call_analyzer_mcp_poll.py` doesn't read any
of those env vars at process start (it only does Granola MCP detection
via `claude -p`). So the warnings are cosmetic for this service — but
~2K warning lines/day in the journal drown real errors.

I proposed: "remove `EnvironmentFile=%h/projects/Sapling/scripts/.env.launchd`
from this service unit, same fix probably applies to other timer services."

Kay's verdict: defer the cleanup, P2 bead it, and **do not blanket-fix**.

## Decision

**REJECT the blanket-strip across all `*.service` units.** Treat each
service as its own audit:

1. For each `*.service` in `~/.config/systemd/user/`, identify which env
   vars the `ExecStart` binary/script actually consumes at process start
   (`grep -E "os.environ.get|getenv|\\$VAR"` in the target).
2. If the script reads **zero** of those vars → safe to **remove**
   `EnvironmentFile=scripts/.env.launchd` from the unit.
3. If the script reads any of them → either (a) drop-in resolver that
   op-injects values into a runtime .env file systemd can parse, or
   (b) wrap `ExecStart` in a shell that sources `load-env.sh` and
   exports resolved values before exec.
4. Reload daemon + verify journal goes quiet on the next fire.

## Alternatives Considered

- **Blanket-strip `EnvironmentFile=scripts/.env.launchd` from every service.**
  Tempting because the file *can never work* under `EnvironmentFile=` —
  the syntax is fundamentally wrong (`export` prefix invalid, `op://`
  unresolved). Wrong here because the warning is the only signal that
  the service has been silently running without its credentials. Strip
  the line without auditing what each script needs and any service that
  actually requires those vars at process start will silently no-op
  Slack posts, Attio writes, Gmail drafts, etc. — and we won't notice
  because the warning was the canary.
- **Fix `.env.launchd` format so systemd CAN parse it.** Means resolving
  `op://` references at file-write time and storing literal values on
  disk — defeats the purpose of the 1Password migration (the whole point
  is on-disk plaintext lives nowhere).
- **Per-service audit + targeted fix** (what we chose). Slower. Surfaces
  actual env-consumption per script as a documented inventory, not
  an inference.

## Reasoning

The journal warning is **load-bearing diagnostic** for any service that
actually needs the env vars. Removing it without knowing whether the
service needs the values is exactly the class of "fix" that hides bugs
instead of fixing them.

Concrete example of what could silently break: a notional
`scheduled-sender.service` that posts Slack notifications and reads
`SLACK_WEBHOOK_OPERATIONS` from env at process start. If we strip the
`EnvironmentFile=` to silence its warnings, the next fire reads
`os.environ.get("SLACK_WEBHOOK_OPERATIONS")` → returns None → posts
nothing → no error → no warning → silent failure for as long as we don't
look at the Slack channel.

The cost of the audit is bounded — there are ~20 user-mode services.
Each takes 1-2 minutes to inspect (`grep` the ExecStart target for env
consumption). Total: ~30-45 minutes. The cost of blanket-strip is
unbounded because the failure mode is silent.

## Why This Trace Matters

The instinct to blanket-fix repetitive warnings is strong and usually
wrong when the warnings come from *configuration* rather than *code*.
Configuration warnings often hide intent — they were put there for a
reason that may or may not still apply.

Future agent looking at journal noise should ask: "what does this warning
*tell* the operator?" before asking "how do I make this warning go away?"
In this case the warning tells us: "this `EnvironmentFile=` line is
non-functional." That's useful information. The right reaction is
"verify each service that has the non-functional line doesn't actually
need it," not "remove the lines."

## Key Insight

**When warnings have a uniform cause across many services, that's a sign
the warnings are *cosmetic by accident, not by design*.** Each service
may have its own answer to "do you need the vars this `EnvironmentFile=`
was supposed to provide?" The uniformity of the warning hides the
non-uniformity of the underlying need.

Per-service audit is the discipline that scales linearly with service
count but produces a correct fix every time. Blanket-strip is constant-
time but produces wrong fixes proportional to how many services
actually needed the env vars. For a small N (20 services), audit wins
on expected cost-of-mistakes.

Captured as P2 bead by Kay from Mac side. Server captured bead intent
in `scratch/2026-05-10-pending-beads.md` because `bd` CLI not yet
installed on VPS.
