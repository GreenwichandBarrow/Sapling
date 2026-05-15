---
name: post-loi
description: "Post-LOI due diligence through closing (~90 days). Event-driven phases: deal cabinet setup, parallel DD workstreams, financing, weekly DD meetings, red flag escalation, purchase agreement, closing. Picks up where deal-evaluation Phase 5A ends."
# WARNING: 2.4x over archetype cap; refactor pending per item 2.
archetype: orchestrator
context_budget:
  skill_md: 500
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
---

<objective>
Manage the full post-LOI lifecycle from signed LOI through closing day.

This skill picks up where deal-evaluation Phase 5A (LOI generation) ends. Once Kay has a signed LOI, this skill orchestrates due diligence, financing, and closing.

**This is a framework.** It will evolve as Kay completes her first deal. Build the skeleton, refine from experience.

**Core question:** Does reality match what the seller represented, and can we close this deal on terms that work?
</objective>

<essential_principles>
## Drive Architecture

All deal documents live in a single deal cabinet:
```
ACTIVE DEALS / {COMPANY} / DEAL {YEAR} /
  OUTREACH/
  CALLS/
  DILIGENCE/
    QOE/
    LEGAL/
    INSURANCE/
    OPERATIONS/
    ENVIRONMENTAL/
  MODELS/
  FINANCIALS/
  CIM/
  NOTES/
  DD-MEETINGS/
  CLOSING/
```

The DILIGENCE/ subfolders and DD-MEETINGS/ and CLOSING/ folders are created by this skill at LOI signing. The parent deal folder already exists from deal-evaluation Phase 1.

Private folder (Kay only) remains:
```
MANAGER DOCUMENTS / DEALS IN REVIEW / {COMPANY} /
```

## Timeline (Target ~90 Days)

| Week | Phase |
|------|-------|
| 0 | LOI signed, deal cabinet expanded, systems updated |
| 1-2 | Internal DD: Kay + analyst validate fundamentals |
| 2-4 | External DD: QoE firm, legal, insurance engaged |
| 2-8 | Parallel DD workstreams running |
| 1-8 | CIM built incrementally (10-page blocks every 2 weeks) |
| 4-10 | Financing: SBA + equity capital calls |
| 8-10 | Purchase agreement drafting and negotiation |
| ~12 | Closing |

Weekly DD meetings with advisors/seller run throughout.

## Event-Driven Triggers

This skill does NOT run on a schedule. Each phase triggers the next:
- LOI countersigned detected -> Phase 1
- DD workstream findings filed -> Phase 4 (meeting prep)
- Material issue surfaced -> Phase 5 (red flag escalation)
- All DD workstreams complete -> Phase 6 (purchase agreement)
- Purchase agreement signed -> Phase 7 (closing)

## Communication Rules

- Slack notifications (#strategy-active-deals) for milestone events only
- Investor updates at key milestones: LOI signed, DD complete, closing date set
- No em dashes in emails. Sign off "Very best, Kay"
- Always open emails with a warm nicety
- Show person names, not just companies
</essential_principles>

<phases>
## Phase 1: LOI Signed — Deal Cabinet & System Updates

**Trigger:** Countersigned LOI detected (Kay confirms LOI is fully executed)

### Sub-Agent 1: Deal Cabinet Expansion
**Task:** Expand existing deal folder with DD-specific subfolders and create Motion project.
**Tools:** gog drive, Motion API

**Steps:**
1. Verify existing deal folder in ACTIVE DEALS / {COMPANY} / DEAL {YEAR}
2. Create DD subfolders under DILIGENCE/:
   - QOE/, LEGAL/, INSURANCE/, OPERATIONS/, ENVIRONMENTAL/
3. Create DD-MEETINGS/ folder (for weekly meeting prep docs)
4. Create CLOSING/ folder (for purchase agreement, funds flow, entity docs)
5. Create Motion project: "{Company} — Due Diligence"
   - Set target close date (Kay provides or default to LOI date + 90 days)
   - Create task groups for each DD workstream
   - Tasks with dependencies and due dates relative to close date:
     - **Week 1:** Engage QoE firm, engage legal counsel, notify insurance broker
     - **Week 2:** Kick off QoE, request legal document list from seller
     - **Week 2-4:** Customer interview scheduling, key employee meetings
     - **Week 4:** QoE preliminary findings review
     - **Week 6:** QoE final report, legal DD memo
     - **Week 8:** All DD workstreams complete — go/no-go checkpoint
     - **Week 8-10:** Purchase agreement drafts
     - **Week 10-12:** Closing prep, funds flow, entity setup
6. Update Attio: move deal to "LOI Signed" stage

**Returns:**
```json
{
  "diligence_folders": {"QOE": "", "LEGAL": "", "INSURANCE": "", "OPERATIONS": "", "ENVIRONMENTAL": ""},
  "dd_meetings_folder_id": "",
  "closing_folder_id": "",
  "motion_project_id": "",
  "target_close_date": "",
  "attio_updated": true
}
```

**Stop Hook:**
- [ ] All DD subfolders created under DILIGENCE/
- [ ] DD-MEETINGS/ and CLOSING/ folders exist
- [ ] Motion project created with task groups and dependencies
- [ ] Attio stage updated to "LOI Signed"

### Sub-Agent 2: Investor & Stakeholder Notification
**Task:** Notify investors and key stakeholders of signed LOI.
**Tools:** Slack, gog gmail

**Steps:**
1. Send Slack notification to #strategy-active-deals:
   ```
   LOI Signed: {Company Name}
   TEV: ${X}M | EBITDA: ${X}M | Multiple: {X}x
   Target Close: {date}
   Deal Cabinet: {folder_url}
   ```
2. Draft investor update email (brief -- 3-4 sentences):
   - LOI signed with {Company}
   - High-level terms (TEV, structure)
   - DD timeline and expected capital call timing
   - Next investor update milestone
3. Present draft to Kay for review

**Stop Hook:**
- [ ] Slack notification sent
- [ ] Investor email draft presented to Kay

### Phase 1 Deliverable
Present to Kay:
- Confirmation of deal cabinet expansion (links to new folders)
- Motion project link with task overview
- Investor email draft for review
- Reminder to engage QoE firm and legal counsel

---

## Phase 2: Due Diligence Workstreams (Parallel)

**Trigger:** Phase 1 complete. Workstreams run in parallel, each tracked independently.

### 2A: Quality of Earnings (QoE)
**Owner:** External QoE firm (Kay engages)

**Agent tasks:**
1. Create QoE tracking doc in DILIGENCE/QOE/:
   - Document request list (from QoE firm)
   - Findings log (as reports come in)
   - Open items tracker
2. As QoE reports are filed, extract key findings and flag:
   - Revenue quality (recurring vs. one-time)
   - EBITDA adjustments (add-backs validated or rejected)
   - Working capital normalization
   - Any material discrepancies from seller's representations

### 2B: Legal DD
**Owner:** Legal counsel (Kay engages)

**Agent tasks:**
1. Create legal DD checklist in DILIGENCE/LEGAL/:
   - Corporate structure and governance
   - Material contracts review
   - Litigation history and pending claims
   - IP ownership and protection
   - Employment agreements and key employee terms
   - Real property leases
   - Regulatory compliance
2. Track findings and flag items needing Kay's attention

### 2C: Insurance DD
**Owner:** Insurance broker

**Agent tasks:**
1. Create insurance review doc in DILIGENCE/INSURANCE/:
   - Current coverage summary
   - Gaps identified
   - Reps & warranties insurance quotes
   - Tail coverage needs

### 2D: Operations DD
**Owner:** Kay + analyst

**Agent tasks:**
1. Create operations DD tracker in DILIGENCE/OPERATIONS/:
   - Customer interview schedule and notes
   - Key employee retention plan status
   - Technology/systems inventory
   - Supplier/vendor relationships
2. Schedule customer interviews (Kay provides contact list)
3. File interview notes as they happen

### 2E: CIM (Incremental Build)

**Steps:**
1. Every 2 weeks, compile a 10-page block of the CIM
2. Block 1 (Week 2): Industry analysis
3. Block 2 (Week 4): Company overview and history
4. Block 3 (Week 6): Financial analysis and projections
5. Block 4 (Week 8): Management and operations
6. Save each increment to CIM/ folder
7. By Week 8: Full 40-page CIM assembled

**Stop Hook (per workstream):**
- [ ] Tracking doc/checklist created in correct DILIGENCE subfolder
- [ ] Findings logged as they arrive
- [ ] Material issues escalated via Phase 5

---

## Phase 3: Financing

**Trigger:** Runs in parallel with DD, starting Week 4

**Steps:**
1. SBA loan process:
   - Track lender engagement and document requests
   - File lender correspondence in CLOSING/
   - Monitor approval timeline
2. Equity capital calls:
   - When Kay decides timing, draft capital call notice to investors
   - Track commitments received
   - File in CLOSING/
3. Structure finalization:
   - Update financial model with final debt/equity split
   - Document final deal structure in CLOSING/

**Stop Hook:**
- [ ] Lender package submitted
- [ ] Capital call notices drafted (when Kay triggers)
- [ ] Final structure documented

---

## Phase 4: Weekly DD Meetings

**Trigger:** First DD meeting scheduled (typically Week 1, recurring weekly)

**Steps:**
1. Before each weekly meeting, auto-generate prep doc in DD-MEETINGS/:
   - File name: "{date} DD Meeting Prep - {Company}.md"
   - Content:
     - **DD Status Dashboard:** Each workstream status (green/yellow/red)
     - **New Findings This Week:** From all workstream trackers
     - **Open Items:** Unresolved questions, pending document requests
     - **Decisions Needed:** Items requiring Kay or seller input
     - **Next Week Focus:** Upcoming milestones from Motion project
2. After meeting, Kay or agent logs decisions and action items
3. Update Motion tasks based on meeting outcomes

**Stop Hook:**
- [ ] Prep doc generated before each meeting
- [ ] All workstream statuses reflected
- [ ] Decisions and action items logged post-meeting

---

## Phase 5: Red Flag Escalation

**Trigger:** Any DD workstream surfaces a material issue

**A material issue is:**
- QoE adjustment that changes EBITDA by >10%
- Undisclosed litigation or regulatory action
- Key customer concentration risk (>25% revenue)
- Key employee flight risk without retention plan
- Environmental or regulatory liability
- Seller misrepresentation on any material fact

**Steps:**
1. Immediately notify Kay via Slack (#strategy-active-deals):
   ```
   RED FLAG: {Company} -- {workstream}
   Issue: {brief description}
   Impact: {estimated financial/risk impact}
   Options memo ready: {link}
   ```
2. Create options memo in DD-MEETINGS/:
   - Issue description with supporting evidence
   - Financial impact analysis
   - Options: (1) Renegotiate terms, (2) Walk away, (3) Proceed with mitigation
   - Recommendation (if clear)
3. Present to Kay for decision
4. After decision: create vault trace at `brain/traces/{date}-dd-red-flag-{company}.md`
   - Document the issue, options considered, decision made, reasoning
5. If renegotiate: update financial model, draft revised terms
6. If walk: trigger decline process (similar to deal-evaluation Phase 5B)

**Stop Hook:**
- [ ] Kay notified immediately
- [ ] Options memo created with evidence
- [ ] Decision captured in vault trace
- [ ] Systems updated based on decision (model, Attio, etc.)

---

## Phase 6: Purchase Agreement

**Trigger:** All DD workstreams complete, Kay confirms go-ahead

**Steps:**
1. DD completion checkpoint:
   - Verify all workstream trackers show complete
   - Compile final DD summary memo in CLOSING/
   - Confirm no unresolved red flags
2. Send Slack notification:
   ```
   DD Complete: {Company}
   All workstreams clear. Moving to purchase agreement.
   DD Summary: {link}
   ```
3. Track purchase agreement drafts:
   - File all drafts and redlines in CLOSING/
   - Log negotiation points and resolutions
   - Track signing timeline
4. Draft investor update: DD complete, moving to closing
5. Update Attio stage to appropriate closing stage

**Stop Hook:**
- [ ] DD summary memo in CLOSING/
- [ ] Slack notification sent
- [ ] Purchase agreement drafts tracked in CLOSING/
- [ ] Investor update drafted

---

## Phase 7: Closing

**Trigger:** Purchase agreement fully executed

**Steps:**
1. Create closing checklist in CLOSING/:
   - Funds flow memo
   - Entity setup (NewCo formation docs)
   - Final lender requirements
   - Insurance binders
   - Employment agreements for key employees
   - Seller transition plan
   - Day 1 operating plan
2. Track each item to completion
3. On closing day:
   - Confirm funds transferred
   - Update Attio: move to "Closed / Won"
   - Slack notification to #strategy-active-deals:
     ```
     CLOSED: {Company Name}
     Greenwich & Barrow has acquired {Company}.
     ```
   - Draft investor closing announcement
4. Create vault trace: `brain/traces/{date}-deal-closed-{company}.md`
   - Full deal arc: LOI terms vs. final terms
   - DD findings that mattered
   - Timeline (planned vs. actual)
   - Lessons for next acquisition
5. Create Day 1 plan doc in CLOSING/:
   - First 30/60/90 day priorities
   - Key employee meetings scheduled
   - Customer communication plan
   - System/process handover checklist

**Stop Hook:**
- [ ] Closing checklist complete (all items checked)
- [ ] Attio updated to "Closed / Won"
- [ ] Investor announcement drafted
- [ ] Vault trace created
- [ ] Day 1 plan documented
</phases>

<execution_flow>
## Invocation

**Primary trigger:** Kay confirms a signed LOI exists.
```
/post-loi {company name}
```

The skill detects current state and picks up at the right phase:
- No DD folders exist -> Phase 1
- DD folders exist, workstreams active -> Phase 2-4 (ongoing)
- Red flag surfaced -> Phase 5
- DD complete, Kay confirms -> Phase 6
- Purchase agreement signed -> Phase 7

## Sub-Agent Summary

| Agent | Phase | Task | Parallel? |
|-------|-------|------|-----------|
| 1: Cabinet Expansion | 1 | Expand folders, create Motion project, update Attio | Yes (with Agent 2) |
| 2: Stakeholder Notify | 1 | Slack + investor email draft | Yes (with Agent 1) |
| DD workstream agents | 2 | Track findings per workstream | All parallel |
| Meeting prep agent | 4 | Generate weekly DD meeting prep docs | Recurring |
| Red flag agent | 5 | Escalation memo + options | On-demand |

## Integration Points

- **deal-evaluation:** This skill starts where Phase 5A ends. Deal folder, financial model, scorecard, and Thumbs Up/Down deck already exist.
- **investor-update:** Use for milestone investor communications (LOI signed, DD complete, closing).
- **motion:** All DD tasks tracked as a Motion project with dependencies.
- **Attio:** Stage progression: "LOI Signed" -> closing stages -> "Closed / Won" or "Closed / Not Proceeding".
- **Vault:** Traces for red flag decisions and closing summary.
</execution_flow>

<success_criteria>
## Success Criteria

### Phase 1 Complete (LOI Signed)
- [ ] DD subfolders created under DILIGENCE/
- [ ] DD-MEETINGS/ and CLOSING/ folders exist
- [ ] Motion project created with workstream task groups
- [ ] Attio updated to "LOI Signed"
- [ ] Slack notification sent
- [ ] Investor email draft presented to Kay

### Phase 2 Complete (DD Workstreams)
- [ ] Each active workstream has a tracking doc in its subfolder
- [ ] Findings logged as they arrive
- [ ] Material issues escalated via Phase 5
- [ ] 40-page CIM assembled by Week 8

### Phase 4 Complete (Weekly Meetings)
- [ ] Prep doc generated before each meeting
- [ ] All workstream statuses current
- [ ] Decisions and action items logged post-meeting

### Phase 5 Complete (Red Flag -- if triggered)
- [ ] Kay notified within 1 hour of discovery
- [ ] Options memo with evidence and recommendation
- [ ] Decision captured in vault trace
- [ ] Systems updated based on Kay's decision

### Phase 6 Complete (Purchase Agreement)
- [ ] DD summary memo finalized
- [ ] Purchase agreement drafts tracked
- [ ] Investor update sent
- [ ] Attio stage updated

### Phase 7 Complete (Closing)
- [ ] All closing checklist items complete
- [ ] Funds confirmed transferred
- [ ] Attio: "Closed / Won"
- [ ] Investor announcement drafted
- [ ] Vault trace with full deal arc
- [ ] Day 1 plan documented

### Validation (run before milestone notifications)
```python
checks = {
    "deal_folder": folder_exists(deal_folder_id),
    "dd_subfolders": all_dd_folders_exist(),
    "motion_project": motion_project_active(),
    "attio_stage": attio_stage_matches_current_phase(),
    "no_open_red_flags": all_red_flags_resolved_or_accepted(),
}

for check, passed in checks.items():
    if not passed:
        raise ValidationError(f"STOP: {check} failed. Fix before proceeding.")
```

## Evolution Notes

This skill is a **framework built before first use.** After Kay's first deal passes through this process, refine:
- Task durations and dependencies (actual vs. estimated)
- DD checklist items (what mattered, what was noise)
- Red flag thresholds (calibrate from real findings)
- Meeting prep format (what Kay actually needs week-to-week)
- CIM structure and pacing
- Investor communication cadence and content
</success_criteria>
