---
date: 2026-04-17
type: context
title: "Do Diligence (Permanent Equity) — G&B Adoption Plan"
source: "Drive folder 1vhl0CVhGRvvHaVwHLnSnSpvcJ_4c4oM6 (15 PDFs)"
tags:
  - context
  - topic/due-diligence
  - topic/owner-calls
  - topic/skill-adoption
  - date/2026-04-17
---

# Do Diligence (Permanent Equity) — G&B Adoption Plan

Decisions from 4/17 session on which PE "Do Diligence" frameworks to adopt and when.

## ADOPT NOW (before May 7 DealsX launch)

Queue into pre-owner-call brief template (used by `meeting-brief` skill for external owner meetings) and relevant sections of `deal-evaluation`.

### 1. Skeleton Talk framing → pre-call briefs for owner calls
**Source PDF:** `Do_Diligence_The_Skeleton_Talk_FINAL.pdf`
**Adoption:** When drafting pre-call briefs for owner/potential-seller meetings, include a "Skeleton Talk opener" section that reframes "tell me the messy parts" as a *favor to the seller*.
**Canonical line:** "The worst thing for both of us is a surprise at week 8" / Emily's $45M-to-not-$45M anecdote.
**Where it lives:** `meeting-brief` skill template → new section "Skeleton Talk prompts to use on this call" when classification is owner/prospect.

### 2. Red-flag list (inverted) → pre-call prep + G&B talking points
**Source PDF:** `Do_Diligence_Setting_Diligence_Objectives_FINAL.01.pdf` (page 9)
**Adoption:** The 8 red flags sellers watch for in buyers (vague funds sources, breaking chain of command, not knowing the industry, moving milestones, murky post-close plans, nitpicking valuation, etc.). G&B pre-call prep should pre-empt each one in Kay's talking points.
**Reinforces:** existing memory rules `feedback_never_say_fund`, `feedback_outreach_no_strategy_leaks`, `feedback_never_say_fund_or_lead`.
**Where it lives:** `meeting-brief` owner-call template → new section "Owner red flags this call should pre-empt" with the 8-item checklist.

### 3. Head & Shoulders → pre-LOI qualification checklist
**Source PDF:** `Do_Diligence_The_Head_and_Shoulders_Diligence_Checklist_Fillable_FINAL.pdf`
**Adoption:** 7-question owner-readiness filter. Use as **gating check inside `deal-evaluation`** — if an owner fails 4+, deal will bleed time in DD and should be scored accordingly.
**Where it lives:** `deal-evaluation` skill → new early-phase gate titled "Owner readiness filter (Head & Shoulders)".

## PARK — Build into `post-loi` skill after May 7

Kay's priorities through May 7 are sourcing-focused (river guide, conferences, deal aggregator). After May 7, focus shifts to `deal-evaluation` + `post-loi`, with these PDFs as references.

| PDF | Adoption target |
|---|---|
| `Do_Diligence_The_Checklist_fillable_CR_FINAL.pdf` | Master DD question bank → becomes G&B's data-room outline inside `post-loi` |
| `Do_Diligence_Diligence_Timeline_FINAL.pdf` | 6-stage phase map → reference inside `post-loi` |
| `Do_Diligence_Build_Your_Diligence_Team_FINAL.pdf` | Team-assembly template → shrink PE's 8-role team to Kay-sized (QB=Kay, Finance=QoE firm, Legal=M&A attorney, Tax=tax advisor, Ops=SVA bench) |
| `Do_Diligence_Attorney_Hiring_Worksheet_Fillable_FINAL.pdf` | M&A counsel selection checklist — pull out when Kay engages first M&A attorney |
| `Do_Diligence_Intermediary_Hiring_Worksheet_Fillable_FINAL.pdf` | Reference for evaluating their intermediary on sell side |
| `Do_Diligence_Due_Diligence_Expectations_FINAL.pdf` | Buyer-behavior norms → weekly DD meeting template inside `post-loi` (with Kay-calibrated pace, NOT PE's 1-day turnaround) |
| `Do_Diligence_Lies_Damned_Lies_and_Honest_Mistakes_FINAL.pdf` | Fraud detection reference during DD; not a template |

## SKIP / Reject

### Not building out (decided 4/17)
- **Table Turn canonical-answer one-pager** — Kay declined. "Not necessary, we haven't had any traction to speak of." Revisit if/when owner response rates hit a level where this matters.

### PE framings NOT to adopt wholesale
- "Full-time in-house diligence team" — G&B outsources (QoE, M&A attorney). Searcher norm, not weakness.
- "1-business-day turnaround" — PE has headcount. G&B promises 2-3 days, doesn't match PE pace.
- "We never retrade" — PE bravado. On first deal, preserve right to renegotiate on material findings.
- **30-year partnership language** — ALIGNED with G&B Charter (Bridge/Engine/Community/Jewel). **Borrow selectively** for investor update + owner collateral, but frame as G&B's, not PE's.

### Budget flag — NOT APPLICABLE
PE quotes $100-150K legal on sub-$50M deals. Research agent recommended budgeting $150-200K for first deal. **Kay rejected:** "Those costs roll into the deal costs, which are covered by investors and bank. I don't manage that and it's not paid by the search fund budget." Do not add to `budget-manager`.

## Sequencing

- **Now → May 7:** Focus on source-grounding (river guide, conferences, deal aggregator). Adopt #1-3 above into `meeting-brief` and `deal-evaluation` templates in the background (Claude's work, Kay reviews post-May 7 before anything goes live).
- **May 7+:** Build out `deal-evaluation` skill in earnest, with Do Diligence references woven in.
- **Post-first-LOI:** Wire the "park" list into `post-loi` skill.

## Drive reference
All 15 PDFs live at: https://drive.google.com/drive/folders/1vhl0CVhGRvvHaVwHLnSnSpvcJ_4c4oM6
