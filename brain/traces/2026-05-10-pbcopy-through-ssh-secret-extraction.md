---
schema_version: 1.1.0
date: 2026-05-10
type: trace
importance: high
target: "doctrine:secrets-management"
tags: ["date/2026-05-10", "trace", "domain/security", "topic/secrets-management", "topic/credential-extraction", "topic/ssh", "pattern/zero-screen-exposure", "status/applied"]
---

# pbcopy-through-SSH for remote secret extraction — zero on-screen exposure

## Trigger

After Kay confirmed the server's 1Password Service Account token is read-only and can't write to GB Server vault, server claude proposed a manual extraction-and-paste workflow:

1. SSH into server.
2. Run `grep '^export GOG_KEYRING_PASSWORD' ~/.bashrc`.
3. Copy the value from terminal output.
4. Paste into the 1Password app on iMac.

Kay then asked the sharp follow-up question: **"doesn't that expose the key again?"**

This forced a re-examination of the workflow's exposure surfaces.

## Decision

**Adopt `pbcopy-through-SSH` as the default extraction pattern for ALL future remote-secret-to-1Password workflows. Reject the grep-then-manual-copy approach.**

The pattern:

```
ssh ubuntu@<host> '<value-suppressing extraction>' | tr -d '\n' | pbcopy
```

Where `<extraction>` is a one-liner that runs on the server and prints just the secret value to stdout — which then flows through the encrypted SSH tunnel back to the Mac, gets piped to `pbcopy`, lands in the Mac clipboard. **Value never displays on screen anywhere.**

Specific extractions per source-file format:

- `~/.bashrc` / `~/.zshrc` (`export VAR="value"`):
  ```
  grep "^export VARNAME" ~/.bashrc | sed "s/^[^=]*=//; s/^\"//; s/\"$//"
  ```
- `scripts/.env.launchd` (`VAR="value"` no export):
  ```
  grep "^VARNAME=" scripts/.env.launchd | sed "s/^[^=]*=//; s/^\"//; s/\"$//"
  ```
- plist/systemd EnvironmentVariables: extract via `plutil`/`systemctl show`, never `cat`.

After paste into 1Password, **immediately clear clipboard** with `pbcopy < /dev/null`.

## Alternatives Considered

- **Original proposal (server claude): grep on server, copy from terminal.** The exposure: value displays on Kay's Mac Terminal screen, lives in scrollback until cleared. Mitigations possible (`clear && history -c`, close window), but each is a step that can be skipped or forgotten. The value also briefly exists in the SSH session's pseudo-TTY output before reaching the Mac, though that flows over the encrypted tunnel.
- **Use `op item edit` from server.** Blocked: server's Service Account token is read-only by design (good security posture — server can resolve secrets but can't modify them).
- **Use `op item edit` from Mac with personal account.** Possible (Kay's Mac has full personal-account access to GB Server vault), but doesn't solve the extraction problem — you still need to get the value FROM the server TO the local CLI.
- **Generate a new keyring password instead of preserving the existing one.** Considered for `GOG_KEYRING_PASSWORD` specifically: if the keyring can be re-encrypted with a new password, we sidestep extraction entirely. Rejected because it risks breaking existing OAuth tokens stored in the keyring if not done carefully, and the migration time-window had higher-impact work in flight.
- **Manual passphrase input instead of automated extraction.** Kay types the value into 1P from memory (if she remembered it). Doesn't apply here — keyring password was auto-generated, not memorized.

## Reasoning

The framework: **categorize secret-handling workflows by where the value appears, then minimize each surface independently.**

For any extract-and-store workflow, the value can appear on:

1. **Source filesystem** — already there before extraction; reading it doesn't add exposure.
2. **Network transport** — encrypted (SSH) is acceptable; unencrypted (HTTP, plain telnet) is not.
3. **Remote terminal output (stdout)** — only if extraction prints to stdout instead of piping.
4. **Local terminal display** — only if the SSH client renders the output to screen.
5. **Local terminal scrollback** — only if step 4 happens AND scrollback is preserved.
6. **System clipboard** — required for paste-into-1P; minimize duration.
7. **Agent transcripts** — forbidden; mitigated by using clean Mac Terminal.app, not Cursor/Claude Code (per `feedback_credential_extraction_clean_terminal.md`).
8. **Process listings** — only if value passed as CLI argument; mitigated by piping (env vars and stdin-pipe don't appear in `ps`).

The grep-then-copy approach exposes the value at surfaces 3, 4, and 5 — three places a leak can happen, three places needing mitigation.

The pbcopy-through-SSH approach exposes the value only at surfaces 2 (encrypted, acceptable) and 6 (clipboard, ~5 sec until `pbcopy < /dev/null`). Two places, both already minimal.

Kay's question — "doesn't that expose the key again?" — was the trigger that surfaced this. Her instinct is the right one for any future extraction: ask where the value lives at each step, minimize each surface. The pbcopy-through-SSH pattern emerged from honoring the question.

## Outcome

Used the pattern for all 5 remaining secrets in today's migration:

- `GOG_KEYRING_PASSWORD` (extracted from `~/.bashrc`)
- `SLACK_WEBHOOK_OPERATIONS` (extracted from `scripts/.env.launchd`)
- `SLACK_WEBHOOK_ACTIVE_DEALS` (extracted from `scripts/.env.launchd`)
- `SLACK_WEBHOOK_STRATEGY_OPS` (extracted from `scripts/.env.launchd`)
- `SLACK_WEBHOOK_SVA` (extracted from `scripts/.env.launchd`)

All 5 extracted, pasted into respective 1P items, clipboards cleared, `op:// `references swapped into source files, smoke tests passed. **Zero on-screen exposure across all extractions.**

Pattern memorialized in `feedback_credential_extraction_clean_terminal.md` as the default approach for any future remote-secret-to-1Password migration.

## Why This Trace Matters

Future agents migrating credentials, rotating leaked secrets, or onboarding new services to 1Password will face the "extract and paste" workflow repeatedly. Without this trace, they'll likely reach for `grep > copy from screen` because it's the obvious mental model. This trace establishes the materially-better pattern as the default and explains WHY (surface count reduction).

It also models the meta-lesson: when the user asks "doesn't that expose X?" — that's not a confused question, it's a calibration signal. The right response is to re-derive the workflow honoring the surface they're asking about, not to reassure them the existing approach is "good enough."

## Key Insight

The number of surfaces a secret touches during a workflow is the right metric for evaluating workflow safety, not whether each individual surface is "acceptable." Every surface is a leak vector with non-zero probability of mitigation failure (forgot to clear scrollback, screenshot taken at wrong moment, AI tool reading pane content). Halving the surface count halves the failure modes. **The right secret-handling workflow is the one with the fewest surfaces, not the one that's easiest to type.**
