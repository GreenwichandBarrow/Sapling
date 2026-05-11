---
name: systemd Environment= quoting fix in generate_systemd_units.py
description: Generator must wrap whole Environment= assignment in quotes when value contains whitespace, and escape inner " and \. Fixed 2026-05-08 for the email-intel/relationship-manager migration. 7 .service files were silently broken pre-fix.
type: project
originSessionId: 245b9334-d58f-45df-8978-a6d8673c0ca7
---
`scripts/generate_systemd_units.py` had a silent bug that broke POST_RUN_CHECK env vars on 7 server-side `.service` files. Patched 2026-05-08 during the email-intelligence + relationship-manager migration.

**The bug:** generator emitted `Environment=KEY=VALUE` directly. Per `systemd.exec(5)`, `Environment=` splits its argument on whitespace and only accepts `KEY=VALUE` tokens. When VALUE contained whitespace (e.g. `python3 "/path/to/validator.py"`), systemd parsed two tokens — first `KEY=python3` (accepted but truncated), then the bare path (rejected as "Invalid environment assignment, ignoring: ..."). Net effect: POST_RUN_CHECK was set to literally `python3` with no script path, and the wrapper's validator step silently no-opped.

**Why this mattered:** CLAUDE.md `feedback_mutating_skill_hardening_pattern.md` makes POST_RUN_CHECK validators mandatory for every scheduled skill. The bug nullified the validator for every skill whose POST_RUN_CHECK had whitespace — silently. Affected 7 skills: conference-discovery, jj-operations-sunday, launchd-debugger, niche-intelligence, nightly-tracker-audit, relationship-manager, target-discovery-sunday. Caught only because `systemd-analyze --user verify` (run with proper `XDG_RUNTIME_DIR=/run/user/$UID`) emits the warning explicitly.

**The fix:** added `format_env_line(key, value)` helper. If value contains whitespace, wrap the whole `KEY=VALUE` in `"..."` and escape inner `"` and `\` per `systemd.exec(5)`. Three call sites updated (LOG_PREFIX, POST_RUN_CHECK, generic env loop). Output for relationship-manager now reads:
```
Environment="POST_RUN_CHECK=python3 \"%h/projects/Sapling/scripts/validate_relationship_manager_integrity.py\""
```
This is semantically identical to the launchd value, so `run-skill.sh` parses POST_RUN_CHECK the same way regardless of platform.

**How to apply (going forward):**
- After regenerating systemd units (e.g. when adding a new scheduled skill), run `systemd-analyze --user verify ~/.config/systemd/user/<unit>.{service,timer}` with `XDG_RUNTIME_DIR=/run/user/$(id -u)` set. Look for "Invalid environment assignment" warnings — they indicate the bug recurred.
- The fix lives in `scripts/generate_systemd_units.py` on both the MacBook and the server. The iMac branch may or may not have it depending on which tree picked up the patch first — verify with `grep -q format_env_line scripts/generate_systemd_units.py` before regenerating from any tree.
- SSH path to server: `ubuntu@agent-vps-7731c88b`, repo at `/home/ubuntu/projects/Sapling`.
