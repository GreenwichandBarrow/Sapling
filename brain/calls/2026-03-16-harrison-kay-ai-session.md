---
schema_version: "1.1.0"
date: 2026-03-16
type: call
call_id: 56e32842-5b68-4450-97d5-694f3726a4b8
source: granola
classification_type: partner
people: ["[[entities/harrison-wells]]", "[[entities/kay-schneider]]"]
companies: ["[[entities/dodo-digital]]", "[[entities/greenwich-and-barrow]]"]
tags:
    - date/2026-03-16
    - call
    - person/harrison-wells
    - person/kay-schneider
    - company/dodo-digital
    - company/greenwich-and-barrow
    - topic/claude-code
    - topic/workflow-architecture
    - topic/automation
    - source/granola
---

# Harrison <> Kay: AI Session

**Date:** 2026-03-16
**Time:** 1:30 PM
**Attendees:** [[entities/kay-schneider|Kay Schneider]] (kay.s@greenwichandbarrow.com), [[entities/harrison-wells|Harrison Wells]] (harrison@dododigital.ai)

---

## Notes

### Workflow Architecture & Best Practices
- Complex workflows require structured approach with main orchestrator agent
- Sub agents handle specific tasks with defined deliverables
- Sub agent stop hooks confirm file creation before proceeding
- External context files store persistent knowledge (learnings.md for industry insights)
- All agents create output files for future agent reference
- Test individual sub agents before full workflow integration

### Weekly Report Workflow Design
- Step 1: Parallel data gathering from multiple sources (newsletters, email, Granola, Drive)
- Step 2: Niche identification using specialized sub agent (reference learnings.md, check tracker)
- Step 3: One-pager creation with template framework and stop hook validation
- Step 4: Scorecard evaluation using external reference file
- Step 5: Final report compilation and Google Sheets integration

### Technical Setup & Automation
- Cron job scheduling for Friday automation requires always-on system
- Mac can run overnight processes while sleeping (confirmed working)
- Alternative: $5/month cloud server if needed
- Use /clear command to start fresh conversations
- Plan mode recommended for complex workflow implementation

---

## AI Analysis

### Action Items
- [ ] Build out workflow using discussed framework @kay
- [ ] Test individual sub agents before full integration @kay
- [ ] Create learnings.md context file with industry insights @kay
- [ ] Available for follow-up session @harrison

### Signals
- **Engagement:** High — [[entities/kay-schneider|Kay]] actively building out [[entities/harrison-wells|Harrison's]] framework
- **Progress:** Advancing from individual skills to full workflow orchestration
- **Next milestone:** End-to-end weekly report automation

---
*Auto-classified by Call Classifier*
