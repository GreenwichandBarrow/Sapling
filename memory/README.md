# Memory directory

Canonical location for Claude Code memory files. Lives in the repo so all nodes (iMac, MacBook, VPS) read from a single git-tracked source.

## How it works

Claude Code expects memory at `~/.claude/projects/<path-keyed>/memory/` — different absolute path on each device:

| Device | Expected path |
|---|---|
| iMac | `~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory` |
| MacBook | `~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory` |
| VPS (server) | `~/.claude/projects/-home-ubuntu-projects-Sapling/memory` |

Each device symlinks its expected path to this directory. All nodes read the same files. Edits get auto-pushed by Sapling's git hooks and pulled by the other nodes.

## First-time setup on a new node

After cloning Sapling and confirming `memory/` is present in the repo, run:

```bash
# iMac / MacBook
mkdir -p ~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations
rm -rf ~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory
ln -s "/Users/kaycschneider/Documents/AI Operations/memory" \
      ~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory
```

```bash
# VPS (server)
mkdir -p ~/.claude/projects/-home-ubuntu-projects-Sapling
rm -rf ~/.claude/projects/-home-ubuntu-projects-Sapling/memory
ln -s ~/projects/Sapling/memory \
      ~/.claude/projects/-home-ubuntu-projects-Sapling/memory
```

Verify with:

```bash
ls -la ~/.claude/projects/<your-path>/memory  # should show a symlink
head -3 ~/.claude/projects/<your-path>/memory/MEMORY.md  # should print "# Memory Index"
```

## Concurrent-edit caveat

Two nodes writing simultaneously can produce a git conflict. Sapling's hooks auto-resolve most cases; the rest take one Claude prompt. If running Claude on Mac and VPS at the same time, pull before writing.

## History

- Pre-2026-05-10: `memory-snapshot/` was a manual rsync taken 2026-04-13 for MacBook restore. Single point-in-time, never updated.
- 2026-05-10: Live memory moved into repo at `memory/`. Symlink scheme established. `memory-snapshot/` deleted.
