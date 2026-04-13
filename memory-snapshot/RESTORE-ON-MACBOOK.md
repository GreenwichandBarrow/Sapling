# How to restore memory on MacBook

After cloning/pulling Sapling on the new machine, run:

```bash
mkdir -p ~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory
rsync -a "$(pwd)/memory-snapshot/" ~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory/
```

Then verify MEMORY.md is loaded by starting a Claude Code session and asking "what do you know about me?" — should reflect saved feedback rules.

Snapshot taken: 2026-04-13 mid-day session #1
