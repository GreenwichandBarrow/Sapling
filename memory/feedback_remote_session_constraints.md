---
name: Remote session constraints — no browser-OAuth tasks
description: When Kay is on Remote Control (away from Mac), don't propose tasks that require browser-based OAuth or admin console access.
type: feedback
originSessionId: ed3ad1c6-9dba-4abb-b157-7867abbc3c13
---
When Kay flags she's on Remote Control / "I'm Remote" / replying via remote interface, she's away from her Mac. Defer any action that requires browser access, OAuth re-auth flows, or admin-console interaction. Common deferrals:

- **Smithery / Attio MCP token re-auth** — requires browser OAuth flow at smithery.ai. Not remote-friendly.
- **Google Workspace OAuth re-consent** — same browser dependency.
- **Streamlit visual eyeball checks** — page renders on `localhost:8501`, not visible from remote.
- **Manual file uploads via web UIs** (Google Drive web, Attio web).

**Why:** Stated 2026-04-25 when Kay deferred the Attio token re-auth (Decision #7) with "I'm Remote." Trying to push browser-required tasks during remote sessions creates dead-end recommendations.

**How to apply:**
- If a recommendation requires browser/OAuth/admin-UI, mark it explicitly as "needs Mac" and offer to defer to next desk session.
- For things I can still do from Claude Code (file edits, vault writes, Bash commands, MCP tool calls that don't need re-auth), proceed normally.
- For things she can do from phone/remote (review draft text, approve YES/NO, dictate edits, send Superhuman reply she has open), proceed normally.
- When the same task surfaces again in a future session, note it was previously remote-deferred — surface as "ready to do now" once she's at the Mac.
