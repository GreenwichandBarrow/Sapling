---
name: Superhuman drafts via superhuman-cli
description: Superhuman has its own draft system (not Gmail). Use superhuman-cli MCP server to create native drafts, not gog gmail drafts.
type: feedback
---

Superhuman does NOT use Gmail's draft system. They built a proprietary draft service. Gmail API drafts (via gog) will NEVER appear in Superhuman.

**Why:** Superhuman ignores Gmail's native Drafts folder entirely. No amount of header/label tweaking fixes this.

**How to apply:**
- Use `superhuman-cli` via **Bash CLI**, NOT the `superhuman_draft` MCP tool (which uses Gmail API under the hood and creates invisible drafts)
- CLI command: `cd ~/.local/share/superhuman-cli && CDP_PORT=9400 bun run src/cli.ts draft create --account kay.s@greenwichandbarrow.com --to "email" --subject "subject" --body "body"`
- This creates drafts via CDP (Chrome DevTools Protocol) directly in Superhuman's native draft system
- Refresh tokens first if expired: `CDP_PORT=9400 bun run src/cli.ts account auth`
- Requires Superhuman running with `--remote-debugging-port=9400` (handled by LaunchAgent)
- Account for G&B work: `kay.s@greenwichandbarrow.com`
- **Signature:** Superhuman has Kay's full signature built in. Only sign off with "Very best,\nKay" — do not include title, email, website, or confidentiality notice
- **BUG (2026-03-23):** The `superhuman_draft` MCP tool created a Gmail API draft that was invisible in Superhuman. The Eric Dreyer response needs to be re-created via the CLI in the next session.
- **DO NOT use `mcp__superhuman__superhuman_draft`** — it routes through Gmail API. Always use Bash CLI instead.
