---
name: Pipeline Cleanup March 2026
description: Full pipeline cleanup context from 4-week scan, corrections from Kay, and pending actions
type: project
---

## Pipeline Cleanup (2026-03-17)

### Corrections from Kay

**People classifications:**
- **Stan Rodos / Crate Capital** = fellow searcher and friend → Network pipeline. NOT a broker. He forwards deal leads from brokers he uses.
- **Austin Yoder / Magrathea Partners** = fellow searcher using OpenClaw for AI outreach. Nearing end of search with LOI in diligence. Intro via Guillermo (Ashford Ventures). Follow-up email SENT 2026-03-17.
- **Jeff Stevens / Anacapa Partners** = lead investor, NOT intermediary. In Investor pipeline.
- **Katie Walker / Plexus Capital** = lender, NOT investor. In Intermediary pipeline at "Warmed" (correct). In-person meeting April 17. Introduced through Will (investor). Hit it off, 2 phone calls already.
- **Colin Woolway / NJBSoft** = fellow searcher, acquired 6 months ago. Same shared office. Recommended by another investor for his process. Network pipeline.
- **Jess** = personal friend (mom friend, HR at Google). NOT pipeline relevant. Skip.
- **RH Guesthouse** = dinner with investor's wife. She's an artist. Skip pipeline.
- **Blue Rider / Whitney / LA events (Feb 25 week)** = ALL CANCELED due to NY blizzard. No pipeline action.
- **Eric Dreyer / Eight Quarter Advisors** = broker who sent art restoration deal to Stan. New intermediary lead to add.

### Deal updates:
- **Love Transfers** = received financials, said NO → move to Closed / Not Proceeding
- **CHROMATIC fine art services** = reached out, they responded, then no-showed the call → move to Closed / Not Proceeding

### Dan Tanzilli meeting notes:
- Met at The TwentyTwo (2026-03-17)
- Intro via Karaugh Brown (Whitney Museum)
- Dan offering to intro Kay to **art attorneys** (1 specific, but also pointing to the category as niche-specific intermediaries)
- **Schwarzman** = example of art advisory business model (niche idea, not an intro)
- **iLevel** = installer company that was for sale (deal lead to research)
- Art advisory as a potential niche to explore
- Wall St article on generational wealth transfer

### Duplicates:
- Kay wants to KEEP separate entries when they represent different contacts at same company
- Need to resolve individual names to distinguish real duplicates from multiple contacts

### Completed actions (2026-03-17):
- Third Eye (Dan Tanzilli) → Need to Send Thank You (DONE)
- VeryFair (Anton Bogdanov) → Nurture Occasionally (DONE)
- Magrathea Partners (Austin Yoder) → Need to Send Thank You (DONE)
- Anacapa Partners (Jeff Stevens) → YR 2 Q1 (DONE)
- Love Transfers → Closed / Not Proceeding (DONE)
- CHROMATIC → Closed / Not Proceeding (DONE)
- JV CPA PC duplicate deleted (was dupe of Richards Vissicchio Douglass) (DONE)
- Cromwell Harbor name fixed (Andrew Freiman, Will Thorndike) (DONE)
- VeryFair name fixed (Anton Bogdanov) (DONE)
- Eight Quarter Advisors (Eric Dreyer) → added to Intermediary at Identified (DONE)
- Austin Yoder follow-up email SENT by Kay
- Dan Tanzilli thank you draft in Gmail
- Eric Dreyer outreach draft in Gmail
- Motion tasks created: Dan thank you, Eric outreach, Denning follow-up, Nikki Higgins reply, Anton LinkedIn reply

### Network Pipeline Restructuring (in progress)
Decided to move network relationship tracking from List entries (company-based) to **People records with custom attributes**. This solves the duplicate company problem (CHANEL x7 = 7 different people).

Custom attributes created on People object:
1. **Relationship Type** (select): Fellow Searcher, Industry Expert, Advisor, Former Colleague, Friend/Personal, Operator/Owner, Investor Contact, Art World, Lender
2. **Nurture Cadence** (select): Weekly, Monthly, Quarterly, Occasionally, Dormant
3. **Value to Search** (text): how they help the acquisition search
4. **Next Action** (text): next follow-up needed
5. **How Introduced** (text): who connected you, context

Test record: Dan Tanzilli fully populated and confirmed by Kay.

### Migration Status (overnight 2026-03-17)
- Agent processed 49 of 95 unique companies (some companies had multiple entries)
- 36 People records updated successfully
- 21 companies had no People records matched (need manual resolution)
- Remaining 46 companies not yet touched
- Migration log NOT written (agent timed out before finishing)
- Known errors to fix in review: Stan Rodos tagged "Art World" should be "Fellow Searcher"
- Morgan Stanley / Blue Rider Group = legit art world contact (Blue Rider is MS Private Wealth subdivision focused on fine art collectors/foundations)
- Kay MUST review all changes before we continue. Present changes in batches for approval.

### Pending actions:
- Review the 36 completed updates with Kay (present 5 attributes per person)
- Fix Stan Rodos relationship_type to "Fellow Searcher"
- Resolve the 21 "no people found" entries
- Process remaining 46 companies (with Kay's review)
- Once migration complete, retire the Network List
- Update pipeline-manager skill to query People records for network relationship management
- Duplicate resolution happens naturally during migration (each person gets one record)
- Denning Rodriguez follow-up email (draft not yet created)
- Nikki Higgins reply (draft not yet created)
- 35 "Identified" deals in Active Deals = art insurance brokerages, will address with outreach skill
- Investigate Superhuman MCP Server for direct email drafting (avoids Gmail API draft sync issue)

**Why:** Pipeline was never consistently maintained in SalesFlare. Attio migration brought over stale data. This cleanup establishes a clean baseline for the daily pipeline-manager automation.

**How to apply:** Complete this cleanup, then daily pipeline-manager runs keep it current going forward.
