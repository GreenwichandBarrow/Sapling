---
name: gogcli
description: >-
  Interact with Google services via the gog CLI. Use when user wants to
  send email, check calendar, manage Drive files, read/write Sheets,
  create Docs, manage contacts, tasks, forms, slides, chat, or any
  Google Workspace operation from the terminal.
archetype: simple
context_budget:
  skill_md: 150
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
invocation: user
---

<objective>
Execute Google Workspace operations via the `gog` CLI (gogcli) — Gmail, Calendar, Drive, Docs, Sheets, Slides, Contacts, Tasks, Forms, Chat, Apps Script, Classroom, Keep, Admin, Groups, and People.
</objective>

<essential_principles>
1. **JSON for scripting:** Use `--json` when output will be parsed or piped. Default human-friendly output for display.
2. **Account awareness:** Always check which account is active. Use `--account` or `GOG_ACCOUNT` when the user has multiple accounts.
3. **Least privilege:** Prefer `--readonly` and scoped `--services` when full access isn't needed.
4. **Confirm destructive ops:** Deletions, sends, and permission changes should be confirmed with the user before execution.
5. **Date handling:** Calendar and Tasks use timezone-aware dates. Use `--timezone` or `GOG_TIMEZONE` for clarity. See `docs/dates.md` for formats.
6. **No credential exposure:** Never echo, log, or commit OAuth tokens, client secrets, or keyring passwords.
</essential_principles>

<quick_start>
1. Check auth status: `gog auth status`
2. List accounts: `gog auth list`
3. Route user request to the correct service (see routing table)
4. Use `--json` when you need to parse output
5. For multi-step operations, confirm intent before executing
</quick_start>

<usage>
```bash
/gogcli send email to jane about the meeting    # Gmail send
/gogcli what's on my calendar today             # Calendar events
/gogcli find the Q4 report in Drive             # Drive search
/gogcli add a task to buy groceries             # Tasks
/gogcli check my unread mail                    # Gmail search
```
</usage>

<routing>
| Intent Pattern | Service | Reference |
|---------------|---------|-----------|
| send/compose/draft/reply email | Gmail | references/commands.md → Gmail |
| search/read/label mail | Gmail | references/commands.md → Gmail |
| calendar/events/schedule/meeting/freebusy | Calendar | references/commands.md → Calendar |
| upload/download/share/search files | Drive | references/commands.md → Drive |
| create/edit/export document | Docs | references/commands.md → Docs |
| create/read/write/format spreadsheet | Sheets | references/commands.md → Sheets |
| create/export/edit presentation | Slides | references/commands.md → Slides |
| contacts/people/directory | Contacts/People | references/commands.md → Contacts |
| tasks/todo/tasklist | Tasks | references/commands.md → Tasks |
| forms/survey/quiz | Forms | references/commands.md → Forms |
| chat/message/DM/spaces | Chat | references/commands.md → Chat |
| classroom/course/roster/grades | Classroom | references/commands.md → Classroom |
| notes/keep | Keep | references/commands.md → Keep |
| users/groups/admin/workspace | Admin/Groups | references/commands.md → Admin |
| auth/login/accounts/credentials | Auth | references/commands.md → Auth |
| apps script/run function | Apps Script | references/commands.md → Apps Script |
</routing>

<when_to_use>
- User wants to interact with any Google service from the terminal
- Automating Google Workspace workflows (email + calendar + sheets pipelines)
- Reading/writing Google Sheets data for analysis or reporting
- Sending emails or managing drafts
- Checking calendar availability or creating events
- Uploading/downloading/sharing Drive files
- Managing Google Tasks or Forms

Do NOT use when:
- User needs Google Cloud Platform (GCP) infrastructure ops — use `gcloud` CLI instead
- User needs Google Analytics, Ads, or Search Console — different APIs/tools
- The operation requires a browser-only flow with no CLI equivalent
</when_to_use>

<auth_troubleshooting>
If commands fail with auth errors:
1. `gog auth status` — check current state
2. `gog auth list --check` — validate tokens
3. `gog auth add <email> --services <service> --force-consent` — re-authorize
4. For Workspace-only features (Keep, Admin, Groups): needs service account with domain-wide delegation
</auth_troubleshooting>

<output_modes>
- Default: human-friendly tables (TTY)
- `--json`: structured JSON (scripting/parsing)
- `--plain`: stable TSV (piping to awk/cut)
- Hints/progress always go to stderr
</output_modes>

<success_criteria>
- [ ] Correct service identified from user intent
- [ ] Correct `gog` command constructed with proper flags
- [ ] Account specified if user has multiple accounts
- [ ] Destructive operations confirmed before execution
- [ ] Output format matches downstream use (JSON for parsing, default for display)
- [ ] No credentials exposed in output or logs
</success_criteria>
