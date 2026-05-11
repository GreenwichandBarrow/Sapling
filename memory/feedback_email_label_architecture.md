---
name: Email label architecture — 9 Auto Labels across 4 accounts
description: Kay uses Superhuman Auto Labels for content classification + Split Inbox for priority. Final taxonomy locked April 13, 2026.
type: feedback
originSessionId: 4bdde090-de44-4ba3-971a-ad1a0b83d208
---
Kay's email system uses Superhuman across 4 Gmail accounts: `kay.s@greenwichandbarrow.com` (G&B work), `kaycschneider@gmail.com` (career/network/personal), `kaycfofana@gmail.com` (family/kids), `kaystrash23@gmail.com` (signups + Yahoo archive).

Email organization is split between two orthogonal Superhuman systems:
- **Split Inbox** = priority filter (who matters / how urgent). Owns the "to action" / "important" / "read later" axis.
- **Auto Labels** = content classification (what kind of email). Owns the topic/category axis.

Labels and Auto Labels do NOT do priority work. Do not propose `To Action`, `FYI`, `Read Later`, `Action Required`, or `Respond` as Auto Labels — those are Split Inbox's job.

**The 9 Auto Labels (created on all 4 accounts, April 13 2026):**

| # | Auto Label | AI Prompt |
|---|---|---|
| 1 | `Search Fund` | M&A learning, peer searchers, search-fund conferences (BK Growth, ETA), investor updates, G&B operations. NOT active deal opportunities. |
| 2 | `Family & Friends` | Personal mail from family members or close friends about life, kids, or relationships. |
| 3 | `Personal & Network` | Kay's personal life (events, fashion, social plans, hobbies) OR professional networking (intros, coffee chats, relationship building). |
| 4 | `Finance & Legal` | Banking, credit cards, statements, taxes, investments, accounting, contracts, government, IRS, lawyers. |
| 5 | `Home` | Real estate, utilities, household services, home maintenance, property. |
| 6 | `Travel & Expenses` | Flight/hotel/reservation confirmations; travel itineraries; receipts, invoices, order/purchase confirmations. |
| 7 | `Subscriptions & Education` | Newsletters, promotions, marketing, social, mass mail, courses, school emails, conference content. |
| 8 | `Meetings` | Calendar invites, meeting requests, scheduling links (Calendly, SavvyCal), video call invitations. |
| 9 | `Deal Flow` | Inbound deal opportunities, CIMs, teasers, blind profiles, broker pitches, intermediary deal flow, owner replies to acquisition outreach. |

**Skill integration:**
- `email-intelligence` skill should read the `Deal Flow` Auto Label as the primary trigger for CIM auto-flow, Active Deal Fast-Path, and DIRECT/BLAST/NEWSLETTER classification on G&B (and any other account where deal flow may land).
- `Search Fund` Auto Label is for educational/operational mail, NOT deal flow — do not trigger pipeline-manager off `Search Fund` alone.

**Critical Superhuman behaviors learned April 13:**
- Labels under the `[Superhuman]/` namespace (including Superhuman's own `[Superhuman]/AI/Marketing` etc.) are **invisible to the L label picker**. Renaming a label within `[Superhuman]/` keeps it hidden. Must lift labels OUT of `[Superhuman]/` to make them user-accessible.
- Superhuman's "+ New Label" UI creates **Auto Labels** (rule-backed, with required Include criterion), NOT plain Gmail labels. Plain Gmail labels can only be created in Gmail web settings. For Auto Label rules: AI Prompt is the most flexible field — one sentence describing what the label catches.
- Superhuman's AI auto-categorization may re-create renamed `[Superhuman]/AI/*` labels because its classifier expects those exact target names. Workaround: Gmail filter that auto-relabels.

**Why we did NOT restructure existing Gmail labels:**
Kay's existing G&B labels (DEAL FLOW, INDUSTRY RESEARCH, OUTREACH, TEAM, RECEIPTS) are working and well-organized. Renaming them to nest under `Search Fund/` was churn for marginal gain on a high-stakes account. Auto Labels go forward; existing Gmail labels stay as historical organization.
