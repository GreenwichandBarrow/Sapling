---
date: 2026-06-02
type: context
title: "Session Decisions — 2026-06-02 (Tue: tech-stack reconciliation + runway-to-Feb-2027 path WITHOUT salary cut; DealsX contract read (no minimum, mid-June cancel); bookkeeper Kick blocked by CPA ($247 not $1K); conference attendance back-filled to Feb-2025 launch → 28-event record; $700/mo protected conference budget; Camilla operating approach)"
tags:
  - date/2026-06-02
  - context
  - topic/session-decisions
  - topic/budget-runway
  - topic/tech-stack
  - topic/conference-attendance
  - topic/dealsx-cancellation
  - topic/bookkeeper-transition
  - topic/camilla-approach
  - company/dealsx
  - company/startvirtual
  - status/done
---

# Session Decisions — 2026-06-02

Long single-thread working session: budget/runway reconciliation, DealsX contract review, and a full back-fill of the conference attendance record. Source of truth for figures = Budget Dashboard (`Runway Forecast` + `Tech Stack Inventory` tabs) and Conference Pipeline `Attended` tab.

## Decisions

### Tech stack (budget reconciliation vs bank statements)
- **APPROVE** — Add DocSend ($70/mo) to tech stack + dashboard.
- **APPROVE** — 1Password corrected $3 → $52/mo.
- **PASS** — QuickBooks left at rounded $41 (Kay: "no need to update" to $41.37).
- **APPROVE** — Corrections: Claude $100 → $217.75/mo (largest tech line, was undercounted), Tailscale $0 → $8.71 (no longer free), add BizBuySell $24.95. Total monthly tech ≈ $1,062.65.
- **Decision** — Dodo Digital ($1,000) = consulting / one-time → NOT tech stack (excluded). Superhuman = cancelled (final bill 5/22) → $0, excluded.
- Informational — macOS "Passwords" / moving to Codex CANNOT replace 1Password (headless VPS + scheduled skills need a service-account secrets resolver; Keychain is device-local). No action taken.

### Runway to Feb 2027 — chosen path: NO salary cut
- **Decision (judgment call)** — Investor *suggested* Kay pause salary; Kay manages the fund herself and chose to close the runway gap via **cost levers, keeping salary as an emergency backstop only.** See trace [[traces/2026-06-02-runway-to-feb-2027-no-salary-cut]].
- **PASS** — "numbers don't matter, bottom line is the same" — accepted Plan of Record without re-deriving exact figures.
- Levers: JJ off Jul 1 (communicated), DealsX off ~Aug 1, office summer pause (Jul+Aug) or full-cancel backstop, discretionary trim ~$600/mo (coffee+rides), conferences PROTECTED.

### DealsX cancellation
- **Decision** — Read executed engagement letter (Prospect Geni, signed 4/13–4/19): **month-to-month, no minimum term, no early-termination penalty.** Kay's "3-month minimum" recollection is NOT in the signed contract.
- **DEFER** — Kay will email cancellation **mid-June** (giving pest + LinkedIn a final ~2-week run), not immediately. Get DealsX's engaged-target list FIRST ($25K success-fee tail + 1-yr non-circ survive termination). Fee = $1,581.14/mo via PAYPAL*PAYONEERINC.

### Bookkeeper
- **Decision** — Bookkeeper → Kick is **BLOCKED (CPA won't accept Kick)**; QBO must stay. Bookkeeper (SV True) actual cost **$247/mo, not ~$1K** — the ~$1K figure in budget docs was wrong, and is immaterial to runway.

### Conferences
- **Decision** — Conference & Networking = **$700/mo PROTECTED line**; discretionary trim comes from coffee/rides, never conferences; big registrations (>$300) + out-of-region trips = discrete pre-approved one-offs. See trace [[traces/2026-06-02-conferences-protected-budget-line]].
- **Decision** — Back-fill conference attendance to **Feb-2025 launch**. Happy hours (One Hanover ×4) + NYU FCU annual meeting are **NOT conferences** → removed. See trace [[traces/2026-06-02-happy-hours-not-conferences]].
- **APPROVE** — Remaining **28-event** Attended record confirmed correct (incl. Dec-2025 Miami/Art Basel cluster validated as attended).

### Operating approach (from 2026-06-02 Camilla call)
- **Decision** — Outreach channel order **LinkedIn → Instagram → email**; focus **conferences + brokers/intermediaries** for the next few months; **Camilla** supports industry evaluation + receives broker listings + all email listings for triage (she already knows the buy-box/scorecard). Working approach, not yet codified as defaults — revisit ~late June. Captured in [[project-camilla-approach-jun2026]].

## Actions Taken
- **UPDATED** — Budget Dashboard `Tech Stack Inventory` tab: DocSend added, 1Password $52, Claude $217.75, Tailscale $8.71, BizBuySell added, totals.
- **UPDATED** — `dashboard/data/tech_stack.yaml` (same five changes).
- **CREATED** — Budget Dashboard `Runway Forecast` "PLAN OF RECORD — No Salary Cut" block + A/B/C scenario model + reality-check + conference-budget check (rows 34-64).
- **UPDATED/CREATED** — Conference Pipeline `Attended` tab: back-filled Feb-2025 → May-2026, sorted chronologically, removed non-conferences → **final 28 events**. (Caught + fixed a 3-blank-row glitch a background agent introduced.)
- **CREATED** memory — [[project-bookkeeper-kick-blocked-by-cpa]], [[project-camilla-approach-jun2026]].
- **UPDATED** memory — [[project-dealsx-jj-windown-by-summer]] (JJ communicated/off Jul 1; full DealsX contract terms; Payoneer $1,581 descriptor), MEMORY.md index.
- **READ** — DealsX executed engagement letter (Drive, VENDOR AGREEMENTS/DEALSX).

## Deferred
- **DealsX cancellation email** → mid-June (~Jun 11-12); pull engaged-target list first. (Claude offered to draft the notice on Kay's say-so + a /schedule reminder.)
- **Office note to friend-landlord** (summer pause Jul+Aug, or reduction; full-cancel backstop) → when Kay is ready; draft offered.
- **Verify DealsX May billing** — only one PAYPAL*PAYONEERINC charge in 60 days (4/21); confirm whether a May invoice is outstanding.
- **Cheaper QBO-compatible bookkeeper path** (Kick dead) → open.
- **Codify Camilla approach as defaults** → revisit ~late June after run-in.
- **May P&L from [[entities/anthony-bacagan|Anthony]] (StartVirtual)** imminent → will refine runway anchor (currently Apr-30 close).

## Open Loops (carry to tomorrow)
- DealsX cancellation prep (mid-June) + engaged-target list + draft notice.
- Office summer-pause ask (draft ready).
- Cheaper bookkeeper path.
- DealsX May-billing verification.
- May P&L ingestion → runway refresh.
