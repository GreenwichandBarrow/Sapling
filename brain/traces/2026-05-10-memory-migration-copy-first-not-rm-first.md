---
schema_version: 1.1.0
date: 2026-05-10
type: trace
importance: high
target: "doctrine:destructive-actions"
tags: ["date/2026-05-10", "trace", "domain/infra", "topic/memory-migration", "topic/symlink", "topic/destructive-operations", "pattern/copy-first-delete-second", "status/applied"]
---

# Copy-first-then-delete is the only safe order for symlink-swap migrations

## Trigger

Kay pasted a 4-line shell sequence to migrate the auto-memory directory at
`~/.claude/projects/-home-ubuntu-projects-Sapling/memory/` into a symlink
pointing at the in-repo `~/projects/Sapling/memory/`:

```
rm -rf ~/.claude/projects/-home-ubuntu-projects-Sapling/memory
ln -s ~/projects/Sapling/memory ~/.claude/projects/-home-ubuntu-projects-Sapling/memory
```

The literal interpretation: delete the auto-memory dir, then symlink to the
in-repo dir which presumably has equivalent content from Mac's earlier push.

## Decision

**Do NOT execute the literal sequence.** Instead:

1. `git fetch` and check that the in-repo `memory/` actually exists after pull.
2. **Enumerate every file in the auto-memory location** and verify each is also
   in `~/projects/Sapling/memory/` post-pull. If any file is missing → COPY
   it into the repo dir before deleting.
3. Compare the **MEMORY.md indexes** — repo MEMORY.md must reference every
   memory the auto-location's MEMORY.md references. If the indexes diverge,
   reconcile by appending entries.
4. **Only then** `rm -rf` the auto-location and `ln -s` to the repo dir.
5. Verify with `head -3 MEMORY.md` returning the expected `# Memory Index`.

## Alternatives Considered

- **Trust Mac's push to cover all memories.** Cheap. Wrong here because the
  server had written 3 memories during today's sessions (Magic DNS feedback,
  pbcopy-through-SSH reference, KeyReach/DealsX project) that never made it
  back to git. Mac's push captured Mac's view only.
- **Just run Kay's literal sequence and trust the symlink to recover.** The
  symlink is symmetric — it links new state to repo — but it can't recover
  files that don't exist anywhere. Once `rm -rf` runs, server-only memories
  are gone. Mac's clone has no copy because they were never pushed.
- **Diff first, repair in-place, then symlink.** What I did. 3 server-only
  memories surfaced and got copied before the delete.

## Reasoning

**Symlink-swap migrations are destructive even though the target "looks like"
the source.** The mental model "I'm pointing the same name at a different
backing store" works only when both backing stores have the same content.
When they don't, the `rm -rf` step silently destroys whatever exists only
in the old backing store.

Three specific files were at risk and would have been lost without the
pre-check:
- `feedback_use_magic_dns_for_references.md` (session 82171e9c, written
  this morning)
- `reference_pbcopy_through_ssh_for_remote_secrets.md` (session cb6ccfff,
  written during the credential migration earlier today)
- `project_keyreach_dealsx_relationship.md` (this session, written ~10 min
  before the migration request)

The repo's MEMORY.md had 501 entries and looked comprehensive. **Looking
comprehensive isn't being comprehensive.** Mac's snapshot was complete for
Mac; it knew nothing about today's server writes.

## Why This Trace Matters

Future agents will be asked to do symlink-swap migrations or similar
"point name X at backing store Y" operations. The naive sequence —
`rm -rf old; ln -s new old` — is destructive and silent.

If Kay says "just run these 4 lines," do NOT take it as permission to skip
the integrity check. Kay's literal commands are usually written with the
*intent* of preserving state; verifying that the new backing store actually
has every file before deleting the old one is part of executing on her
intent, not second-guessing her commands.

This is a specific instance of a general principle: **for any operation
that destroys state visible only in one location, snapshot or copy first.**
Trust nothing about the equivalence of the source and the destination until
you've verified it.

## Key Insight

The cost of pausing to enumerate-and-compare before destructive ops is
~30 seconds of `ls`/`diff`/`cp`. The cost of skipping that step and losing
unique state is catastrophic for memory specifically (memories ARE the
learning loop — you can't recover them from git if they were never in git).

For symlink-swap migrations specifically: **never `rm -rf` the source until
you've personally diffed both directories** and copied over any files that
exist only in one. The integrity check is the migration; the symlink is
just the bookkeeping.
