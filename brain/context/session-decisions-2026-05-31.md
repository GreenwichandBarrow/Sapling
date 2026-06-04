---
date: 2026-05-31
type: context
title: "Session Decisions — 2026-05-31 (Sun, weekly task-tracker rebuild: daily-focus themes, 15→20 slot template grow, Week→day-tab flow; build-week first rollover + canonical-file divergence; PLUS ETA-database niche review → 3 niches queued for Tue + runway/income exploration; PLUS recovered /socrates: AI-CAC → cohort/5-tier framework → insurance build-vs-buy → expert→owner-introducer sourcing fix)"
tags:
  - date/2026-05-31
  - context
  - topic/session-decisions
  - topic/task-tracker-weekly-build
  - topic/daily-focus-template
  - topic/task-tracker-20-slot-grow
  - topic/dealsx-weekly-record
  - person/eric-mendelsohn
  - person/james-emden
  - company/dealsx
  - topic/niche-intelligence
  - topic/eta-database
  - topic/runway-income
  - company/acquiring-minds
  - person/harrison-wells
  - person/samuel-curcio
  - company/dodo-digital
  - topic/gmail-filter-add
  - topic/harrison-coaching
  - topic/scheduled-skill-cost
  - topic/socrates
  - topic/revenue-quality-cohort
  - topic/insurance
  - topic/sourcing-method
  - topic/ai-cac
  - status/done
---

# Session Decisions — 2026-05-31

Long Sunday session, almost entirely Kay's personal task-tracker. First real Phase 5 `build-week` rollover fired, then diverged: Kay kept working in the prior file (`TO DO 5.24.26`) rather than the auto-created `5.31.26`, so that became canonical. Built the week around five daily-focus themes, grew the template 15→20 slots (Monday 22), and flowed the finalized Week tab out to the seven day tabs. Two silent-failure classes caught and fixed (merged-cell write drops; `FALSE`-text checkbox artifacts).

## Decisions

### Task tracker
- **APPROVE:** **Five daily-focus themes for the week** — Sun = Schedule, Mon = Outreach & Email, Tue = Send Quarterly Update, Wed = Website, Thu = Admin, Fri = Strategy. Kay created the `DAILY FOCUS` row (row 13) on the Week tab + all 7 day tabs herself; instructed **never erase/override** it. See [[brain/traces/2026-05-31-daily-focus-row-20-slot-template]].
- **APPROVE:** **Grow the tracker template 15 → 20 priority slots/day** (Monday to 22). Kay: "the 15 limit is now enough [=not enough], we need to grow the template to 20." Applied live to the Week tab + all 7 day tabs on `5.24.26`. Memory: [[feedback-sheet-writes-verify-and-grow-capacity]].
- **APPROVE:** **Keep `TO DO 5.24.26` as the canonical working file** (chose "keep the file I'm in" over migrating to the auto-created `5.31.26`). All of Kay's focus rows + edits live there. See [[brain/traces/2026-05-31-keep-prior-week-file-as-canonical]].
- **APPROVE (verb-fired):** **Eliminate empty/`FALSE` gap rows from the To Do tab** — built reusable `compact-todo` verb; removed 286 gap rows (412→166).

### G&B compliance
- **PASS (resolved, nothing to do):** **G&B "annual report"** — G&B is a Delaware LLC, which owes only the flat $300 annual franchise tax (no report). Kay confirmed she **paid it in May** → covered until 2027-06-01. Task marked Completed. The CorpNet "annual report due / expedited" emails are third-party upsells, ignore.

### Niche ideas / ETA Database (Acquiring Minds)
- **APPROVE:** **Queue 3 niches for the Tuesday niche-intel run** — EHS (Environmental, Health & Safety) compliance services, AED sales & servicing, and aerospace & defense contracting/manufacturing. Sourced from Kay's review of *The ETA Database by Acquiring Minds* (`1BWA01te6...`). Queued via `topic/niche-signal` inbox items (NOT direct tracker rows — the niche-intelligence pipeline forbids skipping the one-pager + score). See [[reference_eta_database_acquiring_minds]].
- **REJECT:** **Trade-show exhibit design/manufacturing** — travel-intensive. **Cultured marble** + **garage door/gate** — read as construction-adjacent (especially NY), even though the DB tags them Manufacturing / Home Services. Codified the soft-exclude rule: [[feedback_niche_screen_soft_excludes_construction_adjacent_travel]]; trace [[brain/traces/2026-05-31-niche-triage-construction-adjacent-travel-filter]].
- **CONFIRMED (no action):** Aerospace/defense has **no live G&B lead with financials yet** — the vault "Aerospace Defense" signals are an investor (Jeff Stevens) thread + a hard-rejected parts distributor, not a target. CFO capital-intensity validation parked until real numbers exist.

### Runway / income exploration
- **DISCUSS (no decision):** Kay asked whether any side-hustle ideas (from a Chris Koerner/DOAC podcast) fit to extend search runway. Verdict surfaced: most fail the unfair-advantage test and would burn the search's "boats." Best-fit lever = **paid buy-side / fractional deal work** (same muscle, accretive to her pipeline); and the cheaper runway lever is the **cost side** — the DealsX/JJ wind-down already in motion. No commitment made. Relates to [[user_kay_plan_b_options]], [[project_dealsx_jj_windown_by_summer]].

## Actions Taken
- **CREATED:** `compact-todo` verb in `scripts/task_tracker.py` (+ `_compact_todo` helper), wired into `build-week` step 4b, documented in `.claude/skills/task-tracker-manager/SKILL.md` (compaction doctrine + verb ref + decision matrix + trace-emission rule).
- **UPDATED:** To Do tabs on both `5.31.26` and `5.24.26` — compacted, 286 gap rows removed, Status/Type/Project/Horizon dropdown validation re-applied (API-verified).
- **CREATED/RAN:** `build-week` first Phase 5 rollover → `TO DO 5.31.26` (superseded by canonical-file decision below).
- **UPDATED:** Week tab on `5.24.26` — spread 37 day-assigned To Do tasks across day columns; grew to 20 slots; recovered 17 items that had silently dropped into a merged notes block.
- **UPDATED:** all 7 day tabs — flowed Week tab → day tabs (Sun 5 / Mon 22 / Tue 1 / Wed 4 / Thu 6 / Fri 12 / Sat 0), grew to 20 (Mon 22), cleared last week's content, re-dated `May 31–June 6`, applied + API-verified checkbox validation on the ✓ column.
- **UPDATED:** marked "File G&B annual report" task Completed.
- **CREATED:** [[feedback-sheet-writes-verify-and-grow-capacity]] memory + MEMORY.md index line.
- **DELIVERED:** Saturday + Sunday morning briefings (decisions-only).
- **CREATED:** 3 niche-signal inbox items — `brain/inbox/2026-05-31-niche-idea-{ehs-compliance-services, aed-sales-servicing, aerospace-defense}.md` (schema-validated; seeded with thesis, buy-box watch-items, female-operator proof, and an explicit capital-intensity flag for aerospace).
- **CREATED:** trace [[brain/traces/2026-05-31-niche-triage-construction-adjacent-travel-filter]].
- **CREATED:** memories [[feedback_niche_screen_soft_excludes_construction_adjacent_travel]] + [[reference_eta_database_acquiring_minds]] + 2 MEMORY.md index lines.

## Deferred
- **DealsX week-of-5/25 record logging** — Kay shared the dashboard (188 sent / 3 replied / **0 positive** / 1 bounce / open-tracking off; front-loaded Mon–Tue). Recommended: log to weekly snapshot + the wind-down loop (6/19 reassessment). Trigger: Kay's YES.
- **Saturday briefing items not answered:** investor-format kill (deferral #15, 10d+), Sam Curcio thank-you send, nurture touchpoints (Kristina Marcigliano 61d / Sarah de Blasio 30d, women-priority) — all carry to Monday.
- **3 niches → Tuesday 2026-06-02 niche-intel run.** EHS / AED / aerospace-defense queued as inbox niche-signals; the automated run ingests them, produces one-pagers + scorecards, and lands rows on the Industry Research Tracker (report to #operations ~10am Wed 6/3 for the analyst call). Trigger: Tuesday automated run.
- **CFO aerospace/defense capital-intensity validation.** Parked. Trigger: a real aerospace/defense target with financials (revenue, EBITDA, capex, asset base, purchase price) enters the pipeline.

## Open Loops
1. **🔴 Resolver pointer mismatch.** `~/.claude/config/current-tracker-sheet.json` points to `5.31.26` (auto-created), but canonical is now `5.24.26`. Until repointed, every `task_tracker.py` verb + next Sunday's `build-week` targets the WRONG file. Must repoint resolver to `5.24.26` and decide rename-to-this-week / trash the empty `5.31.26` duplicate.
2. **🔴 Code constants out of sync with live file.** `scripts/task_tracker.py` (`DAY_SLOT_FIRST_ROW`/`DAY_SLOT_LAST_ROW`, `WK_SLOT_*`, `DAY_NOTES_*`, `DAY_COL_HEADER_ROW`), `scripts/build_day_tabs.py`, `scripts/build_week_tab.py` still assume the OLD layout (no `DAILY FOCUS` row 13; 15 slots at row 14/24). Live `5.24.26` now has focus row 13, header 14, 20 slots (rows 15–34, Mon 36), Week slots grown. `promote`/`distribute-week`/`build-week`/`reformat` will misalign + could clobber the focus row. Needs code hardening before any scripted day-tab write.
3. **🔴 Monday 6/1 external-meeting briefs not generated:** Eric Mendelsohn (Archveo, 11am) + James Emden (Helmsley Spear, 12:30pm lunch). Live for tomorrow.
4. **DealsX logging decision** (above).
5. **Day-tab Type/Project dropdowns** on the new rows (below old row 29) may need `reformat` to confirm dropdowns/row-height carried.

---

## Recovered Session — 5/31 evening (Gmail filters + Harrison Call #6 brief)

> A separate, later 5/31 session (brief written 17:13) was killed by an SSH broken pipe before its own `/goodnight` could run. Kay re-pasted the transcript on 2026-06-02 and asked to run `/goodnight` so nothing was lost. The Harrison brief was already committed; the three Gmail filter changes were live Gmail-API mutations. Captured here under the day they actually happened.

### Gmail filters (gmail-filter-add)
- **UPDATED:** Added `austin@howie.ai` → **auto/tech stack** (`Label_36`). Appended to the existing **bundled** contacts filter (20 → 21 addresses). New filter `ANe1Bmj57vo8L1JsanoTr5Zkhhhq3CPqHzvoig`, replaced `ANe1BmiDXHIJPfGOkX_4nJhuMW5zPgdiyq0mtg`. Two queryless 1-off `Label_36` filters + the separate `TECH STACK` label left untouched.
- **UPDATED:** Added `andrea@womenssearchnetwork.com` → **auto/subscriptions & education** (`Label_34`). Kay chose **Filter B (named senders)** over Filter A (ESP domains) when asked (19 → 20 addresses). New filter `ANe1BmhQG-QN7GXsi7KkwXqBioQt8IBvNtfPdg`, replaced `ANe1BmgyHg-qWhA0p0AxCYgazvPqhxrxy7JkdQ`.
- **UPDATED (override):** Added `samuelcurcio@sydney.tworld.com` → **auto/deal flow** (`Label_27`) as a **standalone, non-bundled** filter — `ANe1BmhJkpqCdToizgtoZ6iUQILpRhacf1ppxQ`. Kay explicitly overrode the default bundle behavior: *"please dont bundle, just this one email should have that one filter."* Both existing bundled deal-flow filters left untouched. This surfaced [[entities/sam-transworld|Samuel Curcio]]'s previously-missing full name + email — the entity had them marked "pending." (`sydney.tworld.com` = a Transworld office subdomain, not Australia; Sam runs NY/NJ/CT buyer matches.)

### Harrison Call #6 brief (cost-driven)
- **CREATED:** `brain/briefs/2026-06-01-harrison-wells-call-6.md` for the Mon 6/1 10am coaching call with [[entities/harrison-wells]] ([[entities/dodo-digital]]). Spec from Kay: *a list of which scheduled skills are working vs. failing, framed so the discussion is about adjusting the setup to absorb impending cost increases.*
  - Reframe (Claude judgment): the dominant 6/15 cost event is **Anthropic's programmatic-billing change** (scheduled `claude -p` fleet moves off subscription → metered API; 30-day analysis ≈ **$5k/mo, ~99% Opus**; drafted Sonnet-routing policy targets ~$1k/mo), with the **Hetzner price bump secondary** — not the other way around as the verbal request implied.
  - Reliability spine: infra is currently healthy (5/29 health report 21/21 systemd timers green, 0 non-zero exits in 7d). "Keeps failing" resolves to (a) historical recurring offenders mostly patched, and (b) un-actioned work/hygiene REDs. **deal-aggregator** flagged as prime downgrade target (single most expensive ~$630/mo, not top-value per [[project_kay_skill_value_assessment]]); **conference-discovery** flagged PROTECT.
  - `validate-edits.py` hook fired once on the brand-voice rule (`Kay's` in prose); fixed to `G&B's` and resubmitted clean.

### Open Loops (recovered session)
6. **Standalone-vs-bundle default for deal-flow filters — UNANSWERED.** Claude asked whether standalone-per-email should become the default for deal-flow going forward (vs. bundling); Kay did not answer. Treat the Sam Curcio standalone as a one-off until Kay generalizes. → candidate `evolve` input for **gmail-filter-add**.
7. **meeting-brief-manager skipped the Harrison coaching call — UNANSWERED.** It classified the 6/1 10am coaching call as internal/vendor and generated no brief (only the 11am Eric Mendelsohn external brief landed). Claude offered to fix the classifier so future Harrison/coaching calls auto-generate; Kay did not answer. → `evolve` candidate for **meeting-brief-manager**. (Partially resolves Open Loop #3 above: the Harrison 10am brief now exists, hand-built; James Emden 12:30pm status still unconfirmed.)

---

## Recovered Session 2 — 5/31 evening `/socrates` (ETA database → AI-CAC → cohort/5-tier framework → insurance build-vs-buy)

> The `/socrates` continuation that ran AFTER the 5/31 goodnight (resumed via `/remote-control`) and was lost across repeated SSH broken-pipe disconnects before its own goodnight could run. Kay re-pasted the transcript on 2026-06-03 and asked to run `/goodnight` so nothing was lost. The earlier income-question + ETA-database analysis are already captured above (Niche ideas + Runway/income sections); this block covers only the strategic socrates thread. Confirmed 5/31-state: aerospace treated as no-live-lead (the 6/3 Matt Luczyk widow deal had not yet surfaced), references the 5/31 DealsX numbers and the just-queued 3 niches.

### Decisions / convergence (mostly DISCUSS — exploratory, ended unconverged on a disconnect)
- **DISCUSS (no decision):** Kay's posture on AI-inflated client-acquisition cost (~10x in sales-driven services like commercial cleaning, pest) is **defensive, not offensive** — she is NOT betting she can "fix" the sales engine with AI ("I am not so bold as to think that I can"; she hasn't even cracked it for her own sourcing yet). So the working screen is **channeled/feeder demand** (regulatory mandate, insurance-directed, government) over CAC-exposed sales-driven demand.
- **Convergence (rederived existing doctrine):** the niche question is backwards — **niches are the OUTPUT of warm owner-layer network access**, not an input. Kay reached [[feedback_industry_is_output_of_network]] from a new road (AI/CAC). Sourcing feeders named: female network, Stern + Cornell alumni, fashion/luxury, art, insurance. Caveat logged: **fashion/art/luxury are feeders, not niches** (no pure-B2C buy; use the network to reach B2B picks-and-shovels serving that world) AND they collide with Kay's **no-dress-up / no-high-travel** filter ([[project_kay_lifestyle_dress_filter]]).
- **DECISION (sourcing fix, actionable):** the real blocker is that Kay's network produces **expert/advisor intros, not owner intros**. Convert owner-level contacts (e.g., the specialty-insurance owner who called unprompted) from **lead-reviewers into owner-introducers** — ask for ONE named owner, not a lead review. Kay agreed she can make that ask ("It won't be luxury"). → trace [[traces/2026-05-31-convert-expert-contacts-to-owner-introducers]]; memory [[project_insurance_pivot_strategy]] updated.
- **DISCUSS (no decision):** **Insurance build-vs-buy.** Kay floated starting a brokerage from scratch (tolerable travel/dress "for a few years," but "not my long-term goal"). Verdict surfaced: **math favors buying** (acquire the seed, 4-6yr hold) over building from zero (no cash flow for years, the CAC battle she won't bet on, ~decade runway). Pull toward build = conviction + ready partner, not the math. No firm decision. → [[project_insurance_pivot_strategy]].
- **Surfaced (durable framework, NOT yet adopted):** the **Pacific Lake Mid-Search Summit (5/19 Boston, Will)** revenue-quality **5-tier spectrum** (contractual recurring → non-contractual recurring → repeat → actuarial → transactional), contract-penalty caveat ("3yr w/ 30-day out = 30-day contract"), retention floor (94-96% gross / 100%+ net), **cohort analysis = DD default**, and Market-Update close-rate cooling (54% 2022 cohort → 30s 2023). Resolves the CAC question: screen by **contract structure/tier, not industry label**; first-call proxy = "% revenue under contract + cancellation term." → new memory [[project_revenue_quality_cohort_framework]]. **Open: adopt as a formal buy-box layer?** (Kay to decide.)

### Calibration (Kay's strong feedback — `evolve` candidates, not edited here)
- **`/socrates` regurgitated Kay's lived experience.** Kay: "you are regurgitating everything I lived through this past year." Root cause: socrates questioned without preloading relevant memory ([[project_network_contacts]], active-thesis files). The system HAD all of it ([[project_art_storage_industry_insight]], [[project_insurance_pivot_strategy]], [[project_kay_lifestyle_dress_filter]], [[feedback_instrument_vs_lived_knowledge]]) and failed to surface it. → `evolve` **socrates**: preload thesis/network memory BEFORE questioning. ([[feedback_instrument_vs_lived_knowledge]] already exists for this failure mode.)
- **`/socrates` must not draft emails / execute.** Claude offered a drafted ask-email mid-session; Kay: "I don't want you to draft an email. You think I need Socrates to write an email?" Reinforces existing socrates framing-only rule (violated). → `evolve` **socrates**.

### Actions Taken (recovered session 2)
- **CREATED** memory [[project_revenue_quality_cohort_framework]] (Pacific Lake 5-tier / cohort / CAC convergence) + MEMORY.md index line.
- **UPDATED** memory [[project_insurance_pivot_strategy]] — build-vs-buy deliberation + experts-not-owners blocker + introducer-conversion.
- **CREATED** trace [[traces/2026-05-31-convert-expert-contacts-to-owner-introducers]].

### Open Loops (recovered session 2 → still live)
8. **Adopt the 5-tier revenue-quality / cohort / retention-floor framework as a formal buy-box layer?** — Kay to decide; would change `deal-evaluation` demands + give a one-line first-call screen.
9. **Insurance build-vs-buy** — unresolved; lean = acquire the seed, not build cold.
10. **Make the owner-introducer ask** to the specialty-insurance owner contact (convert reviewer → introducer). Kay's to send.
11. **`evolve` socrates** — preload thesis/network memory before questioning; reaffirm framing-only (no drafting).
