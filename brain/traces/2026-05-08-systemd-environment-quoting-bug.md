---
schema_version: 1.1.0
date: 2026-05-08
type: trace
importance: critical
target: "skill:generate_systemd_units"
tags: ["date/2026-05-08", "trace", "domain/infrastructure", "pattern/silent-regression", "topic/systemd", "topic/post-run-check", "topic/server-migration", "status/applied"]
---

# Systemd Environment= quoting bug — silent POST_RUN_CHECK regression across 7 services

## Trigger

During step 2 of tonight's timer migration, server-Claude flagged that 7 .service files had silently-truncated POST_RUN_CHECK env vars. The values were literally `python3` with no script path — meaning POST_RUN_CHECK validators were running as `python3` (no script), exiting cleanly with no validation, and silently passing.

Without the catch, every server-side scheduled skill that depends on POST_RUN_CHECK (per the universal hardening doctrine) would have been a no-op. The entire validator-gating layer would have been a lie.

## Decision

Add `format_env_line()` helper to `scripts/generate_systemd_units.py` that wraps full assignment in `"..."` and escapes inner `"` and `\` per `systemd.exec(5)`. Re-emit + reinstall all 7 affected services on the server. Verify clean post-fix.

## Alternatives Considered

- **Hand-edit each .service file.** Rejected — 7 files, error-prone, and the bug would silently re-emerge whenever the generator regenerates. Fix the source.
- **Skip the fix, document as known issue.** Rejected — the universal POST_RUN_CHECK doctrine (broadened 2026-05-04 after conference-discovery wiped 70 rows) was specifically designed to prevent silent-success failure modes. A no-op validator IS a silent-success.
- **Per-service `EnvironmentFile=` instead of inline `Environment=`.** Considered — would sidestep quoting entirely. Rejected for now because it changes the deployment pattern and adds a per-skill .env file. Marginal benefit; current fix is sufficient.

## Reasoning

The bug pattern is:

```
# generator emitted:
Environment=POST_RUN_CHECK=python3 /path/to/validate.py

# systemd parsed:
POST_RUN_CHECK=python3   # truncated at first whitespace
# /path/to/validate.py becomes a separate (ignored) token
```

systemd accepts the malformed line without error. The Environment= directive uses whitespace as a separator for *multiple key=value pairs*, but if a single value contains whitespace, the entire value must be quoted. The generator was emitting unquoted values, so any value with a space silently truncated.

Why it's specifically dangerous:
1. systemd does NOT error on the malformed line (silent acceptance).
2. The skill's POST_RUN_CHECK runs successfully (just runs `python3` with no script and exits 0).
3. The wrapper sees exit 0 from validator, treats as PASS.
4. Real validation never runs. Real failures never surface to Slack.

This is the "silent success failure mode" pattern from `feedback_mutating_skill_hardening_pattern.md` 4/19 + 5/3 incidents.

The fix wraps the entire assignment in double quotes:

```
Environment="POST_RUN_CHECK=python3 /path/to/validate.py"
```

Inner `"` and `\` escaped per systemd.exec(5).

## Why This Trace Matters

Two reasons:

1. **The pattern is recurring across infrastructure.** Any time a value contains whitespace and is consumed by a parser that uses whitespace as a separator, this risk exists. Future generators (cron, launchd, systemd, Docker, etc.) are vulnerable to the same bug. The defense pattern (always quote the full assignment when emitting key=value lines) generalizes.

2. **Silent-validator-regression is the most expensive failure mode.** A noisy failure surfaces to Slack within minutes; a silent failure can persist for weeks before someone notices a missing artifact. The universal POST_RUN_CHECK doctrine exists precisely to catch this class of failure — but the doctrine itself can be bypassed if the validator command is malformed at infrastructure layer. Defense-in-depth requires both the doctrine AND infrastructure-level checks that the doctrine is actually firing.

Adjacent improvement: a unit test for `generate_systemd_units.py` that asserts POST_RUN_CHECK values with whitespace are correctly quoted in emitted .service files. Filed as future-session work.

## Key Insight

**Validators that exit 0 because they aren't actually running pass the same as validators that ran and confirmed success.** The wrapper layer cannot distinguish "POST_RUN_CHECK ran cleanly" from "POST_RUN_CHECK is `python3` with no script and exited 0 trivially." Defense requires either (a) validators that print structured success markers the wrapper greps for, or (b) infrastructure-level assertions that the validator command itself is well-formed before launching the service. Tonight's fix is option (b) at the generator level.
