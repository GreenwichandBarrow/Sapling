---
name: pbcopy-through-SSH pattern for remote-secret extraction
description: Default pattern for extracting a secret value from the Sapling Linux server into Kay's iMac clipboard for paste-into-1Password — value never traverses any Claude transcript or scrollback.
type: reference
originSessionId: cb6ccfff-6f04-4d9c-b811-0029a06b3b65
---
When Kay needs to extract a secret from the Sapling Linux server (e.g.,
`scripts/.env.launchd`) and paste it into 1Password without the value ever
appearing in any Claude conversation transcript, terminal scrollback, or
log, use:

```bash
ssh ubuntu@agent-vps-7731c88b 'source ~/projects/Sapling/scripts/.env.launchd 2>/dev/null; printf "%s" "$VAR_NAME"' | pbcopy
```

Then sanity-check with `pbpaste | wc -c` (byte count only — doesn't reveal
the value).

**Why this pattern:**
- `source` natively parses bash syntax — works whether the var is `export
  KEY=val`, bare `KEY=val`, single-quoted, or double-quoted. No fragile
  sed/cut/awk pipelines, no shell-quoting nightmares.
- `printf "%s"` writes exactly the value, no trailing newline.
- Single-quoting around the entire ssh command argument prevents any
  variable expansion or escape-interpretation on the Mac side; the remote
  bash is the only interpreter.
- Output flows: server → ssh transport → Mac stdin → pbcopy. The value
  lands in Kay's clipboard ONLY. It never appears in:
  - server claude's conversation (the value is in a pipe, not a tool result)
  - Mac terminal scrollback (it's piped, not echoed)
  - process listings (server-side `printf` doesn't expose argv)
- Mac claude can't see it either — the pbcopy happens entirely on Kay's
  iMac, server claude only generated the extraction one-liner.

**How to apply:**
- For each new credential migration, replace `$VAR_NAME` with the variable
  name being extracted. Send the one-liner to Kay; she runs it on Mac
  Terminal.app and confirms `pbpaste | wc -c` matches expected length.
- If the source file isn't `.env.launchd`, swap the path. `source` will
  parse any bash-syntax env file.
- For the receiving side, use UUID-based `op://` references (`op://VAULT/<uuid>/field`)
  if the 1P item title contains em-dashes, trailing whitespace, or other
  characters that the title-based form rejects. UUIDs are stable across
  renames and don't break if Kay reformats titles later.

**When to recommend it:**
- Any time a server-side secret needs to land in 1P (rotation, new credential,
  vault migration).
- Worked clean for all 5 items in the 2026-05-10 sweep (4 Slack webhooks +
  GOG keyring password); zero leaks.

**Don't substitute lossy alternatives:**
- DO NOT use `grep + cut + sed` to extract — the shell-escape complexity
  through ssh's `"..."` wrapper produces silent truncation bugs (hit on
  first attempt 2026-05-10; switched to `source + printf` second attempt).
- DO NOT have Claude read the file directly with the Read tool — the value
  lands in transcript. CLAUDE.md secret-handling doctrine forbids this.
- DO NOT have Claude `cat`/`head`/`tail`/`grep VALUE-PRINTING-PATTERN` the
  file — the secret-file-guard hook blocks correctly, but the intent should
  match the doctrine without relying on the hook.

Source: 2026-05-10 server credential migration session. Mac Claude has the
same pattern filed memory-side.
