---
name: motion
description: >-
  Create and manage tasks and projects in Motion via API. Use when user wants to
  create tasks, projects, check task status, update tasks, or manage work in Motion.
invocation: user
context_budget:
  skill_md: 200
  max_references: 2
---

<objective>
Execute Motion project management operations via the REST API — create projects, create/update/delete tasks, manage recurring tasks, and query task/project status.
</objective>

<essential_principles>
1. **Order of operations:** Workspace (exists) → Project (optional, create first if needed) → Task. Always confirm workspace ID before creating.
2. **Due dates required for auto-scheduled tasks:** If `autoScheduled` is not explicitly `null`, `dueDate` is mandatory.
3. **Projects are immutable via API:** Projects can only be created and read — no update or delete. Name them carefully on creation.
4. **Rate limit awareness:** 12 requests/minute for individual workspace. Batch operations need pacing.
5. **Confirm destructive ops:** Task deletion and status changes should be confirmed with the user before execution.
6. **No credential exposure:** Never echo or commit the API key in logs or output.
</essential_principles>

<quick_start>
1. All requests use header: `X-API-Key: {key}` and `Content-Type: application/json`
2. Base URL: `https://api.usemotion.com/v1`
3. Primary workspace: `ws_fnSjxkfnWpcCPke4cknr9r` (My Tasks - Private)
4. Load `references/api-reference.md` for full endpoint details, field specs, and examples
</quick_start>

<routing>
| Intent Pattern | Endpoint | Method |
|---------------|----------|--------|
| create project | /projects | POST |
| list projects | /projects?workspaceId={id} | GET |
| create task | /tasks | POST |
| update task | /tasks/{id} | PATCH |
| delete task | /tasks/{id} | DELETE |
| list tasks | /tasks?workspaceId={id} | GET (paginated, 50/page) |
| move task | /tasks/{id}/move | PATCH |
| create recurring task | /recurring-tasks | POST |
| add comment | /comments | POST |
</routing>

<when_to_use>
- User wants to create tasks or projects in Motion
- User asks to check, update, or manage Motion tasks
- Migrating tasks from another tool into Motion
- Setting up recurring tasks or project structures
- Querying task status or project progress

Do NOT use when:
- User wants to update/rename a project (not supported by API — direct them to Motion UI)
- User wants sub-projects or project hierarchy (not supported)
- User needs calendar/scheduling features beyond task auto-scheduling
</when_to_use>

<gotchas>
- Projects CANNOT be updated or deleted via API — only created and read
- `dueDate` is required unless `autoScheduled` is explicitly set to `null`
- Duration "NONE" is stored as "REMINDER"
- Recurring task priority only accepts HIGH or MEDIUM (not ASAP or LOW)
- Task list returns 50 per page — use `cursor` param with `meta.nextCursor` to paginate
- Schedule names are case-sensitive (use "Work hours" as returned by GET /schedules)
- The API key owner is auto-assigned to tasks if `assigneeId` is omitted
</gotchas>

<success_criteria>
- [ ] Correct endpoint and method used
- [ ] Required fields provided (name, workspaceId, dueDate for scheduled tasks)
- [ ] Project created before tasks that reference it
- [ ] Rate limits respected (max 12 req/min)
- [ ] Destructive operations confirmed before execution
- [ ] No API key exposed in output
</success_criteria>
