---
name: Weekly Operating Schedule
description: Daily agent run schedule and Kay's morning review cadence — baseline every day plus layered weekly skills
type: project
---

## Daily Baseline (Every Weekday)

### Agents Run Overnight (before Kay sits down)
- Pipeline Manager scans yesterday's calendar, email, Granola, Superhuman draft status, target sheet
- Meeting Action Item Extraction: scans Granola notes from prior day's meetings → extracts proposed action items
- Outreach Manager prepares 4-6 personalized email drafts in Superhuman
- Target Discovery adds new approved targets to Attio + outreach queue
- Niche signal detection runs passively during Granola/Gmail processing

### Kay Reviews Every Morning (~30 min)
- Reviews and sends 4-6 email drafts in Superhuman
- Reviews proposed meeting action items from prior day's Granola notes → approves/rejects → approved items create Motion tasks
- Reviews pipeline stage change recommendations → approves/rejects Attio updates
- Reviews stale deals or overdue nurture contacts flagged by pipeline manager
- Reviews any unsent thank-you drafts (escalating urgency at 24h and 48h)

### JJ
- Calls all day Monday-Friday from his call list
- Gets daily Slack notification in #jj-calls with names, phones, scripts, sheet link
- Logs outcomes in master sheet columns R-U (Call Status, Call Date, Call Notes, Owner Sentiment)

## Weekly Layer (on top of daily baseline)

| Day | Extra Agents Run (overnight before) | Kay's Extra Review (morning) |
|-----|-------------------------------------|------------------------------|
| **Sunday night** | Target Discovery (fresh weekly batch), Outreach Manager (JJ's Monday call list), Conference Discovery (next week's options) | — |
| **Monday** | — | Baseline + conference options ready. Pick next week's conference during travel. |
| **Tuesday night** | **Niche Intelligence** runs | Baseline + investor call prep (calls are always Wed). |
| **Wednesday** | Claude posts Niche Intel Report link to #operations by 10am | Baseline only. Niche intel reviewed live on analyst call. (Alternating weeks: investor meeting or team meeting.) |
| **Thursday** | — | Baseline only. |
| **Friday night** | **Weekly Tracker** runs | Baseline + weekly metrics ready. Glance at tracker. Light day. |

## Skill-to-Day Mapping

| Skill | Runs | Output Ready For |
|-------|------|-----------------|
| Pipeline Manager | Every night | Every morning |
| Outreach Manager | Every night | Every morning (4-6 drafts in Superhuman) |
| Target Discovery | Sunday night + Mon-Fri | Monday (fresh list) + daily additions |
| Conference Discovery | Sunday night | Monday morning (during travel) |
| Niche Intelligence | Tuesday night | Wednesday morning (before analyst meeting) |
| Weekly Tracker | Friday night | Friday morning |
| Meeting Brief | 2 nights before meeting | Morning before meeting day |

## Key Design Decisions

- Exercise Tue/Fri mornings is non-negotiable
- Agents run overnight so Kay never waits for output
- Kay's morning routine is identical every day — drafts, action items, pipeline
- Conference follow-ups always next morning, never same day
- Thank-you emails within 24-48 hours, escalating nudges if unsent
- Pipeline manager asks questions one at a time
- No em dashes in email drafts
- All cadence timing in business days (Mon-Fri), no weekend sends
- Wednesday midday meeting alternates between analyst (niche review), investor, and team
- JJ notified via Slack (#jj-calls), Kay notified via Slack (#ai-operations)

**Why:** Kay did the heavy lift building this system to get her time back. 30 minutes of review and clicking send, not hours of manual work.
