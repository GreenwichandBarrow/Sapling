---
name: nightly-tracker-audit
description: "Nightly audit of Industry Research Tracker: process Tabled/Killed moves, re-sort WEEKLY REVIEW, move Drive folders."
user_invocable: true
context_budget:
  skill_md: 1000
  max_references: 1
  sub_agent_limit: 1000
---

<objective>
Lightweight nightly job that keeps the Industry Research Tracker clean. Runs every night at 11pm ET via launchd.

**What it does:**
1. Read WEEKLY REVIEW tab
2. Move any Tabled niches to TABLED tab
3. Move any Killed niches to KILLED tab
4. Re-sort WEEKLY REVIEW (Active-Outreach > Active-Long Term > Active-Diligence > Under Review > New > Ideation)
5. Remove blank rows between niches
6. Move Drive folders to matching status subfolders
7. Re-number Rank column sequentially

**What it does NOT do:**
- Score niches (that's niche-intelligence)
- Discover targets (that's target-discovery)
- Change statuses (only Kay changes statuses via the dropdown)
</objective>

<workflow>
## Step 1: Read WEEKLY REVIEW

```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!A3:K30" -a kay.s@greenwichandbarrow.com -j
```

Column mapping:
| Col | Field |
|-----|-------|
| A | Rank |
| B | Niche Hypothesis |
| C | Current Status (ORANGE — agent-trigger) |
| D | Outreach Channel (ORANGE — agent-trigger) |
| E | Score |
| F | QSBS |
| G | Target Pool |
| H | Quick notes |
| I | Red flags noted |
| J | Start Date |
| K | Days in Review |

## Step 2: Process Tabled Niches

For each row where Col C = "Tabled":
1. Read full row data (A-K)
2. Append to TABLED tab with same columns A-K, plus:
   - Col L: Date Tabled (today)
   - Col M: Why Tabled (from Quick notes or Red flags, or "Moved by nightly audit")
3. Delete the row from WEEKLY REVIEW
4. Move Drive folder to TABLED folder (1_k_c1F11ZNrv4MilATFrURLHdkNx0kRx)

## Step 3: Process Killed Niches

For each row where Col C = "Killed":
1. Read full row data (A-K)
2. Append to KILLED tab with same columns A-K, plus:
   - Col L: Date Killed (today)
   - Col M: Why Killed (from Quick notes or Red flags, or "Moved by nightly audit")
3. Delete the row from WEEKLY REVIEW
4. Move Drive folder to KILLED folder (19xsNk5KTVHF2jb6m_li8IAGjcw34nlMX)

## Step 4: Re-sort and Clean

1. Collect all remaining non-empty rows
2. Sort by status priority:
   - Active - Outreach (1st)
   - Active - Long Term (2nd)
   - Active - Diligence (3rd)
   - Under Review (4th)
   - New (5th)
   - Ideation (6th)
3. Within same status, sort by Score descending
4. Re-number Rank column (1, 2, 3...)
5. Clear all data rows, write sorted data back with no blank rows

## Step 5: Validate — MANDATORY

**Wrapper-level POST_RUN_CHECK validator** (authoritative): `scripts/validate_nightly_tracker_audit_integrity.py`

Runs after `claude -p` exits, regardless of skill-internal logic. Catches the silent-success failure mode where Claude exits 0 but WEEKLY REVIEW still has Tabled/Killed rows lingering, blank gaps, or non-sequential rank.

**Copyable invocation (manual run):**
```bash
python3 "/Users/kaycschneider/Documents/AI Operations/scripts/validate_nightly_tracker_audit_integrity.py"
```

The launchd wrapper (`scripts/run-skill.sh`) overrides EXIT_CODE on POST_RUN_CHECK failure and emits a Slack alert prefixed `VALIDATOR FAILED`. Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead: `ai-ops-jrj.2`.

**In-line invariants (informational; validator is authoritative):**
- Row count after = row count before minus moved rows
- No blank rows between niches
- Rank is sequential 1..N
- Moved niches appear in TABLED or KILLED tab
</workflow>

<drive_folders>
## Drive Folder IDs

| Status | Folder ID |
|--------|-----------|
| WEEKLY REVIEW | 1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT |
| IDEATION | 1fQNl6mogJW-6u5XJeE5uYQGsDPx495_O |
| TABLED | 1_k_c1F11ZNrv4MilATFrURLHdkNx0kRx |
| KILLED | 19xsNk5KTVHF2jb6m_li8IAGjcw34nlMX |

To find a niche's Drive folder:
```bash
gog drive ls -a kay.s@greenwichandbarrow.com --parent {status_folder_id} -j
```
Match by niche name.

To move a folder:
```bash
gog drive move {folder_id} --parent {target_status_folder_id} -a kay.s@greenwichandbarrow.com -j
```
</drive_folders>

<success_criteria>
- [ ] All Tabled niches moved to TABLED tab
- [ ] All Killed niches moved to KILLED tab
- [ ] WEEKLY REVIEW sorted by status priority, no blank rows
- [ ] Rank column is sequential
- [ ] Drive folders match tab placement
- [ ] No data lost (row count validates)
</success_criteria>
