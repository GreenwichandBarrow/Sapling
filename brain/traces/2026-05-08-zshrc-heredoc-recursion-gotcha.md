---
schema_version: 1.1.0
date: 2026-05-08
type: trace
importance: high
target: process
tags: ["date/2026-05-08", "trace", "domain/shell", "pattern/recursion-blowup", "topic/zshrc", "topic/heredoc", "topic/macbook-setup", "status/applied"]
---

# Heredoc + source recursion = exponential ~/.zshrc blowup

## Trigger

While adding the `vps()` shell function to MacBook's `~/.zshrc`, multiple terminal-paste attempts produced parse errors and "out of memory" responses. Eventually MacBook-Claude diagnosed: `~/.zshrc` had ballooned to **899 MB**.

Root cause: the iMac instructions used `cat >> ~/.zshrc << 'EOF'` followed by `source ~/.zshrc` inside the captured body. The heredoc was never terminated cleanly because Terminal soft-wrap injected newlines into the body. When `source ~/.zshrc` ran, it re-executed the captured (still-not-terminated) heredoc text, which re-appended itself, which re-sourced, which re-appended... exponential blowup until the file consumed nearly a GB.

Each shell startup amplified the recursion. Without the catch, the file would have eventually consumed all available disk.

## Decision

Two fixes:
1. Rewrite `~/.zshrc` clean (preserved Kay's 2 legitimate lines: `alias cc=...` + `export PATH=...`, then added `vps()`). Backed up corrupt 899 MB version to `~/.zshrc.corrupt-2026-05-08.bak` for forensic review.
2. **Doctrine update:** never use `cat >> file << 'EOF'` for shell config when `source <file>` appears anywhere in the body. Use direct file Write tool instead, or use a heredoc that doesn't reference the file being written.

## Alternatives Considered

- **Manual edit in TextEdit/nano.** Slower but avoids the heredoc entirely. Should be the default for shell-config writes — heredocs only for short, single-purpose appends.
- **`echo` line-by-line.** Works but quoting nested `"` and `'` for the vps function is brittle. Multiple lines means multiple chances for parse errors.
- **Use `cat >>` interactive (without heredoc).** Type/paste lines, Ctrl+D to end. Avoids the EOF terminator problem but still has the same source-self-recursion risk if `source ~/.zshrc` is in the input.
- **Use the Write tool directly** (Claude's file-write primitive). The cleanest path. Doesn't go through shell parser, doesn't trigger heredoc state, doesn't accidentally execute `source`.

## Reasoning

Three preconditions made this a bug:

1. **Heredoc body included `source ~/.zshrc`.** The user instruction was "append the function block, then source the file so the alias is live in current session." Reasonable in concept; toxic in execution.

2. **Terminal soft-wrap injected newlines into the heredoc body.** When the paste buffer was wider than the terminal, soft-wrap broke long lines. Some of those breaks landed inside the heredoc, breaking the EOF terminator's position.

3. **Each `source` re-executes the entire file from scratch.** Including any partially-completed heredoc state that got captured from previous failed attempts. This is what made the recursion exponential rather than linear — each shell startup re-played all prior failed appends.

The fix isn't to find a "better heredoc" — it's to recognize that shell-config writes should never use `cat >> file << 'EOF'` when the body includes anything that re-reads `file`. Use a non-shell file-write mechanism (Claude's Write tool, or a text editor) that bypasses the shell parser entirely.

## Why This Trace Matters

This was a near-miss — caught by MacBook-Claude before the file consumed enough disk to cause a system failure. Without the catch, Kay's MacBook would eventually have refused to start new shell sessions (zsh would OOM trying to source the file).

The pattern generalizes: any time a shell command appends to a file AND the body of the append includes a re-read of that same file, recursion is possible. Examples to watch:

- `cat >> ~/.bashrc << 'EOF' ... source ~/.bashrc ... EOF`
- `tee -a ~/.profile << 'EOF' ... . ~/.profile ... EOF`
- Any `cron` job that edits its own crontab

Future shell-config writes should default to Write/Edit tools, not heredocs.

## Key Insight

**Heredocs that contain a self-referential read of the file being written are exponential bombs.** The terminal-soft-wrap-injection trigger is incidental; the recursion is structural. Once you recognize the pattern, the rule becomes: shell-config writes use Write/Edit, not heredocs. Heredocs are fine for one-shot file creation that doesn't include `source`/`exec`/`. file` of the target.
