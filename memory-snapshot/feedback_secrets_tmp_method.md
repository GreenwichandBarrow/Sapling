---
name: Use /tmp file method for secrets and links
description: When Kay needs to pass sensitive info (links, keys, tokens), always recommend the /tmp file method first — it's the one that works reliably
type: feedback
---

When Kay needs to route secrets, links, or sensitive info to the terminal, always recommend the /tmp file method FIRST:

```bash
cat > /tmp/filename.txt
# paste content, Enter, Ctrl+D
```

Then read with: `cat /tmp/filename.txt`

**Why:** Environment variable export (`export VAR=value`) doesn't carry across shell sessions. The /tmp file method works every time. Kay confirmed this on 3/20/2026 after multiple failed attempts with other methods.

**How to apply:** Whenever Kay asks "how do I give you a link/key/secret through the terminal," immediately recommend the /tmp file method. Don't suggest env vars or other approaches first.
