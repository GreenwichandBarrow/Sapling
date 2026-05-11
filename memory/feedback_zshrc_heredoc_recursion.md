---
name: Never use heredoc-append for shell config when source is in the body
description: `cat >> ~/.zshrc << EOF ... source ~/.zshrc ... EOF` is an exponential bomb — terminal soft-wrap can break the EOF terminator, and each shell startup re-executes captured-but-incomplete heredoc content
type: feedback
originSessionId: d5485724-ca82-4a50-bf98-38302fa9db3d
---
When appending to a shell config file (`.zshrc`, `.bashrc`, `.profile`), NEVER use the heredoc-with-source pattern:

```
cat >> ~/.zshrc << 'EOF'
... config ...
source ~/.zshrc
EOF
```

This is an exponential file-size bomb. Two failure modes converge:

1. **Terminal soft-wrap injects newlines into the heredoc body.** If the paste buffer is wider than the terminal, soft-wrap can break long lines — including breaking the `EOF` terminator's position. The heredoc never closes cleanly and the captured body grows.
2. **`source ~/.zshrc` inside the body causes self-recursion.** Each shell startup re-executes the captured (potentially incomplete) heredoc state, which re-appends, which re-sources, which re-appends. Linear recursion compounds across sessions until file consumes all available disk.

**Why:** Caught a 2026-05-08 incident where MacBook's `~/.zshrc` had ballooned to **899 MB** from this pattern. Without the catch, Mac would have eventually refused to start new shell sessions (zsh OOM trying to source the file). Forensic backup at `~/.zshrc.corrupt-2026-05-08.bak`.

**How to apply:**
- For shell-config writes, use the Write/Edit tools directly (Claude's file primitive). Bypasses shell parser entirely. Cleanest path.
- If a CLI editor is preferred: nano or `open -e` (TextEdit). Manual edit, save, exit.
- If you MUST use shell to append: use `cat >>` interactive (no heredoc — type/paste lines, Ctrl+D to end). Or single-line `echo` with proper escaping. Either way, the body MUST NOT include `source` of the file being written.
- After any shell-config write, sanity-check file size: `ls -la ~/.zshrc` should be < 10KB for a typical user. If it's growing into MB, you've hit the recursion bomb.
- If you discover a corrupted file: back it up (`cp ~/.zshrc ~/.zshrc.corrupt-{date}.bak`), then rewrite clean with just the legitimate config lines.

**Pattern generalization:** Any shell command that appends to a file AND the body includes a re-read of that same file is at risk. Examples to watch:
- `cat >> ~/.bashrc << 'EOF' ... source ~/.bashrc ... EOF`
- `tee -a ~/.profile << 'EOF' ... . ~/.profile ... EOF`
- Any cron/launchd/systemd job that edits its own scheduling config

**Full design rationale:** `brain/traces/2026-05-08-zshrc-heredoc-recursion-gotcha.md`.
