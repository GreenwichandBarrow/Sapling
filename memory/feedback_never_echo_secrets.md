---
name: Never echo secrets or links into conversation
description: When reading secrets, links, or sensitive data from /tmp files, NEVER echo the contents into the conversation output. Read silently via Bash and suppress output.
type: feedback
---

When reading sensitive data from /tmp files (links, API keys, tokens, share URLs), NEVER let the content appear in tool output or conversation text.

**Why:** Kay shared a OneDrive link via /tmp file on 3/20/2026 and it was echoed into the conversation via tool output. This exposed a private share link in the chat history. Kay was upset.

**How to apply:**
- Read /tmp secrets with: `cat /tmp/filename.txt 2>/dev/null` and assign to a variable inside the script — never print/echo
- Use pattern: `LINK=$(cat /tmp/filename.txt) && echo "Link loaded successfully"` — confirms receipt without showing content
- For WebFetch or any tool that takes a URL: construct the call inside Bash so the URL never appears in tool parameters visible in conversation
- ALWAYS truncate/redact sensitive values in any output shown to the user
- This applies to: share links, API keys, tokens, passwords, webhook URLs, any PII
