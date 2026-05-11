---
name: Credential extraction in clean terminal only
description: Any step that prints a secret value to a terminal (grep on .env, ssh + cat for inspection, op read for manual paste) must happen in macOS Terminal.app or iTerm2 — never Cursor's integrated terminal, never Claude Code's bash, never any AI-instrumented surface.
type: feedback
originSessionId: a17b3644-0a92-410f-8373-2fd4fc54f69d
---
When a workflow requires Kay to see a secret value in her terminal (e.g. extracting an existing keyring password to paste into 1Password, reading an op:// resolved value to verify length, inspecting a token before rotation), the terminal MUST be a clean, non-AI-instrumented surface.

**Allowed:** macOS Terminal.app, iTerm2, plain SSH session opened from one of those.

**Forbidden:** Cursor integrated terminal, VS Code integrated terminal, any Claude Code session's bash, any IDE with AI features that capture pane output.

**Why:** "The value lands in your terminal but never in claude's conversation" only holds if the terminal isn't an AI-instrumented surface. Integrated terminals can have telemetry, transcript logging, code-completion features that read pane content, or — in Claude Code's case — direct visibility into bash output. A grep that's "safe in your terminal" leaks into the agent transcript if the terminal IS the agent.

**How to apply:**
- When drafting credential-extraction instructions for Kay, explicitly name the terminal: "Open macOS Terminal.app (NOT Cursor, NOT Claude Code)…"
- After the extraction step, recommend `clear && history -c` or closing the window so values don't sit in scrollback.
- This rule sits alongside the existing CLAUDE.md secret doctrine (`grep -c` / `awk` for variable names only inside agent sessions). The two rules together: agent uses value-suppressing patterns; human extraction happens in clean terminal.

**Preferred pattern: pbcopy-through-SSH (avoids on-screen exposure entirely).** When the workflow is "extract a secret from a remote machine and paste into 1Password," pipe directly from server through encrypted SSH tunnel into Mac clipboard — value never displays:

```
ssh ubuntu@<host> '<extraction>' | tr -d '\n' | pbcopy
```

Where `<extraction>` is a value-suppressing-on-the-server one-liner like `grep "^export VARNAME" ~/.bashrc | sed "s/^[^=]*=//; s/^\"//; s/\"$//"` for `~/.bashrc` (export VAR="value") or `grep "^VARNAME=" file | sed "s/^[^=]*=//; s/^\"//; s/\"$//"` for .env (VAR="value" no export).

Then in 1Password app: Cmd+V to paste, save. Then immediately `pbcopy < /dev/null` to clear clipboard.

Result: value lives only in encrypted SSH stream + clipboard for ~5 seconds, never on screen, never in scrollback.

**Source — pattern proven 2026-05-10** during full 1Password migration (Attio + Apollo + GOG keyring + 4 Slack webhooks). Used for all 5 secrets, all migrated cleanly, no on-screen exposure.

**Source:** 2026-05-10 — Kay caught this herself during the GOG_KEYRING_PASSWORD migration, asking "shouldn't I do this in regular terminal, not cursor, not claude" before acting on the instruction. Correct instinct, codifying so it's not re-derived each time.
