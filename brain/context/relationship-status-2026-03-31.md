---
date: 2026-03-31
scan_timestamp: 2026-03-31T08:00:00Z
type: relationship-status
contacts_reviewed: 12
overdue_count: 2
auto_resolved_count: 5
---

# Relationship Status — 2026-03-31

## Section 1: Overdue Contacts (Action Required)

### 1. Britta Nelson — OVERDUE (Quarterly cadence, 106 days since last contact)
- **Attio:** Art World / Quarterly cadence
- **Last interaction:** 2025-12-16 (calendar meeting). Last email: 2025-11-25.
- **Threshold:** 98 days (14 weeks). She is 8 days past due.
- **Email in last 7 days:** None found.
- **Why she matters:** Gallery director at David Zwirner (top gallery). Reviewed Kay's art storage target list, provided art logistics contacts (Articheck), mentioned insurance broker lead. Operational insider with no recurring reason to stay in touch — needs a warm touchpoint.
- **Suggested action:** Short "what are you working on" note. Can reference Frieze/art fair season as natural hook (Art Basel Hong Kong just passed, Frieze NY is May).
- **Email:** britta.nelson@gmail.com / britta@davidzwirner.com

### 2. August Felker — OVERDUE (No cadence set, but ~4+ months silent)
- **Attio:** No nurture_cadence set (should be Quarterly). Last interaction: 2025-11-19 (meeting), last email: 2025-11-14. That is 137 days — nearly 20 weeks.
- **Email in last 7 days:** None found.
- **Why he matters:** Insurance brokerage owner (Oberle Risk) who was acquired via search fund — the contact who triggered Kay's entire insurance thesis in October 2025. Offered to review future opportunities. This is a river guide who has gone cold.
- **Suggested action:** Re-engage. He offered to review opportunities when Kay first met him — now is a natural time to loop back with an update on how the thesis has developed. Short note, no ask.
- **Email:** august.felker@oberle-risk.com
- **Note:** Recommend setting Quarterly nurture cadence in Attio.

---

## Section 2: Auto-Resolved (No Action Needed)

| Contact | Cadence | Last Contact | Status |
|---------|---------|-------------|--------|
| [[entities/guillermo-lavergne\|Guillermo Lavergne]] | Bi-weekly (investor) | 2026-03-25 (meeting) | On track. Next call 2026-04-08. |
| [[entities/jeff-stevens\|Jeff Stevens]] | Monthly (lead investor) | 2026-03-25 (email + meeting) | On track. Email thread active this week. |
| [[entities/dan-tanzilli\|Dan Tanzilli]] | Monthly | 2026-03-26 (email thread active) | Within window. 5 days ago. |
| Austin Yoder | Quarterly | 2026-03-23 (email) | Within window. 8 days ago. |
| Harrison Wells | Occasionally | 2026-03-26 (email + invoice) | Active. Invoice/notes thread closed this week. |
| Kate Reibel | No cadence set | 2026-03-24 (meeting) + 2026-03-25 (email) | Very active. Art advisory validation underway. |
| Margot Romano | No cadence set | 2026-03-30 (email) + 2026-04-03 (meeting booked) | Active. Calendar meeting Friday. |

---

## Section 3: Pending Intros

### 1. Naomi Baigell → Jonathan (art storage owner)
- **Status:** Offered intro in 2025 (Sept/Oct). No follow-through confirmed in Gmail.
- **Last interaction with Naomi:** 2025-10-10 (email).
- **Days since:** 172 days. Art storage niche is now tabled per sprint status.
- **Recommendation:** Hold. Art storage is not an active sprint. Re-activate if/when art storage thesis moves to active diligence.

### 2. Q4 Investor Update (all 12 investors)
- **Status:** Q4 2025 (ended Feb 7) was never sent. No Q1 2026 update found in Gmail search.
- **Days overdue:** ~52 days past Q4 close.
- **Recommendation:** Flag for Kay. The investor-update skill is built and ready. The AI operational buildout (all 10 skills live) is the headline narrative Kay wanted. This is the moment to send it. Suggest running `/investor-update` this week.

---

## Section 4: Warm Intro Opportunities

### 1. Sarah de Blasio → active insurance targets
- **Cadence:** Quarterly. Last interaction: 2026-01-23 (67 days). Due at ~14 weeks = not overdue until ~2026-05-02.
- **Context:** VP at Chartwell Fine Art (EPIC Brokers). Strong personal connection. Introduced Kay widely at Art Basel. Identified as SHORT LIST for when a fine art insurance brokerage deal surfaces.
- **Recommendation:** No action today — within cadence window. Flag for May touchpoint unless a specific deal surfaces first, in which case contact immediately.

### 2. Margot Romano → April 3 call is the intro opportunity
- **Status:** Call is already on the calendar for Friday 2026-04-03.
- **Context:** Bank of America Art Services. Previously introduced Emily (Risk Strategies) and Sarah (Chartwell). Active email thread yesterday.
- **Recommendation:** Use Friday's call to ask about any insurance brokerage contacts she hasn't yet introduced — she has already produced two high-value intros.

---

## Data Notes
- Attio `nurture_cadence` field is populated on ~5 of the key relationship contacts reviewed. Several important river guides (August Felker, Naomi Baigell) have no cadence set.
- Attio filter API does not support `is_not_empty` on select fields via current MCP tooling — full nurture cadence list was assembled by direct search on named contacts from vault + memory.
- Recommend: set Quarterly cadence on August Felker in Attio after this briefing.
