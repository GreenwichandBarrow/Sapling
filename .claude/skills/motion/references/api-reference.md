# Motion API Reference

Base URL: `https://api.usemotion.com/v1`
Auth: `X-API-Key` header with API key value.

## Rate Limits

| Tier | Limit |
|------|-------|
| Individual | 12 requests/minute |
| Team | 120 requests/minute |
| Enterprise | Custom (contact Motion) |

## Workspaces

Your workspace IDs:

| Workspace | ID | Type |
|-----------|----|------|
| Personal Workspace | `ws_1ure41XPTrza1CF8mzdbbD` | TEAM |
| My Tasks (Private) | `ws_fnSjxkfnWpcCPke4cknr9r` | INDIVIDUAL (primary) |

User ID: `ec89VwbOHIfT1O6vhzYoV9pANCu1` (Kay Schneider)

### GET /workspaces

Returns all workspaces with their statuses, labels, and type.

### GET /users?workspaceId={id}

Returns users in a workspace.

### GET /users/me

Returns current authenticated user (id, name, email).

---

## Statuses

Available in both workspaces:

| Status | Default? | Resolved? |
|--------|----------|-----------|
| Backlog | no | no |
| Blocked | no | no |
| Canceled | no | no |
| Completed | no | **yes** |
| In Progress | no | no |
| Todo | **yes** | no |

Pass status by **name** (string) when creating/updating tasks.

### GET /statuses?workspaceId={id}

---

## Schedules

Available schedules (pass by **name** string):

| Schedule | Hours |
|----------|-------|
| Work hours | Mon-Fri 9-5 |
| Day | Mon-Fri 9-5 |
| Night | Mon-Fri 6pm-9pm |
| Personal hours | Mon-Fri 8-9am + 5-9pm, Sat-Sun 8am-9pm |
| Anytime (24/7) | Every day 12am-11:59pm |
| 9-5 all week | Every day 9-5 |

### GET /schedules

---

## Projects

### Order of Operations

Projects are **optional**. Tasks can exist without a project. The correct order is:

1. **Workspace** (already exists, just need the ID)
2. **Project** (optional -- create if you want to group tasks)
3. **Task** (can reference projectId or omit it)

### POST /projects -- Create Project

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Project name |
| `workspaceId` | string | Workspace ID |

**Optional fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `dueDate` | ISO 8601 datetime | none | Project due date |
| `description` | string | none | HTML accepted |
| `labels` | string[] | [] | Label names |
| `priority` | string | MEDIUM | ASAP, HIGH, MEDIUM, LOW |
| `projectDefinitionId` | string | none | Template ID; requires `stages` |
| `stages` | object[] | none | Required with projectDefinitionId |

**Example:**

```bash
curl -X POST "$BASE/projects" \
  -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
  -d '{
    "name": "My Project",
    "workspaceId": "ws_fnSjxkfnWpcCPke4cknr9r",
    "dueDate": "2026-04-01T00:00:00.000Z",
    "description": "Project description here",
    "priority": "HIGH"
  }'
```

**Response** returns full project object with `id`, `statusId`, `priorityLevel`, `createdTime`, etc.

### GET /projects?workspaceId={id}

Returns all projects in a workspace. Response: `{ "projects": [...] }`

### GET /projects/{id}

Returns a single project by ID.

### Update/Delete Projects

**Projects CANNOT be updated or deleted via API.** PATCH and DELETE both return 404. Projects must be managed through the Motion UI.

---

## Tasks

### POST /tasks -- Create Task

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Task title |
| `workspaceId` | string | Workspace ID |
| `dueDate` | ISO 8601 datetime | **Required for auto-scheduled tasks** |

**Optional fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `projectId` | string | none | Associate with a project (optional) |
| `description` | string | none | GitHub Flavored Markdown |
| `priority` | string | MEDIUM | ASAP, HIGH, MEDIUM, LOW |
| `duration` | int or string | none | Minutes (int > 0), "NONE", or "REMINDER" |
| `status` | string | workspace default (Todo) | Status name string |
| `labels` | string[] | [] | Label names |
| `assigneeId` | string | current user | User ID to assign |
| `autoScheduled` | object or null | object | Set null to create unscheduled task |

**autoScheduled sub-fields:**

| Field | Type | Default | Values |
|-------|------|---------|--------|
| `startDate` | ISO 8601 date | none | Date trimmed to start of day |
| `deadlineType` | string | SOFT | HARD, SOFT, NONE |
| `schedule` | string | Work Hours | Must match a schedule name exactly |

**Key behaviors:**
- If `autoScheduled` is provided (or omitted), the task is auto-scheduled and `dueDate` is **required**.
- If `autoScheduled` is explicitly `null`, the task is unscheduled and `dueDate` is optional.
- If `duration` is "NONE", the response returns `"REMINDER"`.
- `description` is stored as HTML (markdown input is converted).
- Tasks are auto-assigned to the API key owner if `assigneeId` is omitted.

**Example -- auto-scheduled task with project:**

```bash
curl -X POST "$BASE/tasks" \
  -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
  -d '{
    "name": "Review quarterly report",
    "workspaceId": "ws_fnSjxkfnWpcCPke4cknr9r",
    "projectId": "pr_Yd1nX6xLvnzubHPUu7hkTP",
    "dueDate": "2026-03-20T23:59:59.000Z",
    "autoScheduled": {
      "startDate": "2026-03-15",
      "deadlineType": "HARD",
      "schedule": "Work hours"
    },
    "description": "Review and finalize the quarterly report.",
    "priority": "HIGH",
    "duration": 60,
    "status": "In Progress"
  }'
```

**Example -- unscheduled task, no project:**

```bash
curl -X POST "$BASE/tasks" \
  -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
  -d '{
    "name": "Quick reminder",
    "workspaceId": "ws_fnSjxkfnWpcCPke4cknr9r",
    "autoScheduled": null,
    "priority": "LOW",
    "duration": "NONE"
  }'
```

### GET /tasks?workspaceId={id}

Returns paginated tasks. Response: `{ "tasks": [...], "meta": { "nextCursor": "...", "pageSize": 50 } }`

Use `meta.nextCursor` as query param `cursor` to paginate.

### GET /tasks/{id}

Returns a single task by ID.

### PATCH /tasks/{id} -- Update Task

All fields from create are available (all optional on update). Pass only the fields you want to change.

```bash
curl -X PATCH "$BASE/tasks/{id}" \
  -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
  -d '{
    "status": "Completed",
    "priority": "HIGH"
  }'
```

### DELETE /tasks/{id}

Deletes a task. Returns empty response on success (HTTP 204-ish, empty body).

```bash
curl -X DELETE "$BASE/tasks/{id}" -H "X-API-Key: $KEY"
```

### PATCH /tasks/{id}/move -- Move Task

Moves a task to a different workspace. Body: `{ "workspaceId": "target_workspace_id" }`.

```bash
curl -X PATCH "$BASE/tasks/{id}/move" \
  -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
  -d '{ "workspaceId": "ws_1ure41XPTrza1CF8mzdbbD" }'
```

---

## Recurring Tasks

### POST /recurring-tasks -- Create Recurring Task

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Task name |
| `workspaceId` | string | Workspace ID |
| `assigneeId` | string | User ID |
| `frequency` | object | Recurrence pattern |

**Optional fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `description` | string | none | Task description |
| `duration` | int or "REMINDER" | none | Minutes or reminder |
| `deadlineType` | string | SOFT | HARD or SOFT |
| `priority` | string | MEDIUM | HIGH or MEDIUM only |
| `startingOn` | ISO 8601 date | none | Start date |
| `idealTime` | string | none | HH:mm format |
| `schedule` | string | Work Hours | Schedule name |

### GET /recurring-tasks?workspaceId={id}

### DELETE /recurring-tasks/{id}

---

## Comments

### POST /comments -- Create Comment

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `taskId` | string | yes | Task to comment on |
| `content` | string | no | GitHub Flavored Markdown |

### GET /comments?taskId={id}

---

## Custom Fields

### POST /custom-fields -- Create Custom Field
### GET /custom-fields?workspaceId={id}
### DELETE /custom-fields/{id}
### POST /custom-fields/{id}/projects/{projectId} -- Add to Project
### POST /custom-fields/{id}/tasks/{taskId} -- Add to Task
### DELETE /custom-fields/{id}/projects/{projectId} -- Remove from Project
### DELETE /custom-fields/{id}/tasks/{taskId} -- Remove from Task

---

## Priority Values

Used across tasks and projects:

| Value | Description |
|-------|-------------|
| `ASAP` | Highest priority, scheduled immediately |
| `HIGH` | High priority |
| `MEDIUM` | Default |
| `LOW` | Low priority |

## Deadline Types

| Value | Description |
|-------|-------------|
| `HARD` | Must complete by due date |
| `SOFT` | Target date, can slip (default) |
| `NONE` | No deadline pressure |

## Task Response Shape

```json
{
  "id": "tk_...",
  "name": "string",
  "description": "<p>HTML string</p>",
  "duration": 30,
  "dueDate": "ISO 8601",
  "deadlineType": "SOFT|HARD|NONE",
  "parentRecurringTaskId": null,
  "completed": false,
  "completedTime": null,
  "updatedTime": "ISO 8601",
  "startOn": "YYYY-MM-DD",
  "creator": { "id": "", "name": "", "email": "" },
  "workspace": { "id": "", "name": "", "type": "", "statuses": [...], "labels": [] },
  "project": { "id": "", "name": "", "description": "" } | null,
  "status": { "name": "", "isDefaultStatus": bool, "isResolvedStatus": bool },
  "priority": "ASAP|HIGH|MEDIUM|LOW",
  "labels": [],
  "assignees": [{ "id": "", "name": "", "email": "" }],
  "scheduledStart": "ISO 8601" | null,
  "scheduledEnd": "ISO 8601" | null,
  "schedulingIssue": false,
  "createdTime": "ISO 8601",
  "lastInteractedTime": "ISO 8601",
  "customFieldValues": {},
  "chunks": []
}
```

## Project Response Shape

```json
{
  "id": "pr_...",
  "name": "string",
  "description": "string (HTML)",
  "workspaceId": "ws_...",
  "statusId": "tst_...",
  "priorityLevel": "ASAP|HIGH|MEDIUM|LOW",
  "managerId": "user_id" | null,
  "createdByUserId": "user_id",
  "dueDate": "ISO 8601",
  "startDate": "ISO 8601" | null,
  "createdTime": "ISO 8601",
  "updatedTime": "ISO 8601",
  "completedTime": null,
  "type": "NORMAL",
  "color": "gray|sky|...",
  "duration": 0,
  "taskCount": 0,
  "completedTaskCount": 0,
  "canceledTaskCount": 0,
  "scheduledStatus": "ON_TRACK|PAST_DUE|UNFIT_SCHEDULABLE" | null,
  "estimatedCompletionTime": "ISO 8601" | null,
  "labels": [],
  "customFieldValues": {},
  "stages": [],
  "variableInstances": []
}
```

## Quick Reference: Order of Operations

```
1. GET  /workspaces                     -- get workspace IDs
2. GET  /schedules                      -- get available schedule names
3. POST /projects (optional)            -- create project if grouping tasks
4. POST /tasks                          -- create task(s), optionally linking to project
5. PATCH /tasks/{id}                    -- update task status/priority/etc
6. DELETE /tasks/{id}                   -- remove task when done
```

## Gotchas

- `dueDate` is required when `autoScheduled` is not explicitly `null`.
- Projects cannot be updated or deleted via API -- only created and read.
- The `schedule` field value is case-sensitive: use "Work hours" (lowercase h) as returned by GET /schedules, though "Work Hours" (capital H) also works in task creation.
- Duration "NONE" is accepted on input but stored/returned as "REMINDER".
- Descriptions are auto-wrapped in `<p>` tags when stored.
- Task list pagination: 50 per page, use `cursor` query param with `meta.nextCursor`.
- Recurring task `priority` only accepts HIGH or MEDIUM (not ASAP or LOW).
- The API key owner is auto-assigned to tasks if `assigneeId` is omitted.

## Note

A test project named "API Test Project - Delete Me" (`pr_j4t1MP5W6huF1kPzX4cdkd`) was created during API research but cannot be deleted via API. Delete it manually in the Motion UI.
