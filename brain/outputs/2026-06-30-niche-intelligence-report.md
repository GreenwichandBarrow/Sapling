---
schema_version: 1.2.0
date: 2026-06-30
type: output
output_type: niche-intelligence-report
status: done
skill_origin: niche-intelligence
run_mode: tuesday
runner: Codex/systemd
trace: "[[traces/agents/2026-06-30-niche-intelligence]]"
tags: [date/2026-06-30, output, output/niche-intelligence-report, status/done, source/codex-systemd, topic/niche-intelligence]
---

# Niche Intelligence Report - 2026-06-30

## Machine-Parseable Summary

```yaml
run_date: 2026-06-30
run_mode: tuesday
runner: Codex/systemd
niches_evaluated: 4
niches_identified: 1
one_pagers_written: 1
scorecards_written: 1
tracker_updated: true
chatroom: brain/traces/agents/2026-06-30-niche-intelligence.md
sidecar: brain/trackers/niches/niche-intel-2026-06-30.json
new_niches:
  - name: Geotechnical Engineering & Construction Materials Testing for Infrastructure/Commercial Construction
    score: 2.31
    status: New
    tracker_tab: WEEKLY REVIEW
    tracker_row: 34
    tracker_rank: 31
    drive_folder_id: 1ZclGPvVxMK56mUY-VdMt4bRtCsOhoWWR
    one_pager_file_id: 1oU08ske_pU3r4hGcZKNR0zGvv3Yfmqqt
    scorecard_file_id: 1InaIkTuA4LCjqBBpZOdT1SHeAdLTUIvH
```

## Run Summary

The Tuesday headless run completed under Codex/systemd. The chatroom is [[traces/agents/2026-06-30-niche-intelligence]].

Step 1 gathered recent and historical signals. RECENT covered web/social, newsletters, Granola/vault calls, Gmail deal flow/investor mail, vault research, and passive inbox signals. HISTORICAL covered vault calls and targeted older Gmail history, with source gaps documented for unavailable OneNote SEARCH FUND extraction and missing raw ChatGPT export.

Step 1b synthesized the gather posts into the five required outputs: Cross-Source Signal Matrix, Named Company Registry, Contact-to-Niche Map, Lead Lifecycle Tracker, and Convergence Report. The strongest signals reinforced existing tracker rows, especially premium/specialty pest, specialty/HNW/trade-risk insurance, facilities/HOA/commercial building services, fire/life-safety/EV testing, and scoped art/HVA services.

Step 2 evaluated four net-new or adjacency candidates from synthesis. One candidate advanced: Geotechnical Engineering & Construction Materials Testing for Infrastructure/Commercial Construction. Three did not advance this cycle: septic/liquid waste services, medical-grade water filtration service/filters, and specialty steel / industrial MRO.

## Candidate Advanced

### Geotechnical Engineering & Construction Materials Testing for Infrastructure/Commercial Construction

**Score:** 2.31 / 3.00  
**Verdict:** Moderate / promising adjacency; target validation needed.  
**Tracker:** Added to WEEKLY REVIEW row 34, rank 31, status New.  
**Drive folder:** https://drive.google.com/drive/folders/1ZclGPvVxMK56mUY-VdMt4bRtCsOhoWWR  
**One-pager:** https://docs.google.com/presentation/d/1oU08ske_pU3r4hGcZKNR0zGvv3Yfmqqt/edit?usp=drivesdk  
**Scorecard:** https://docs.google.com/spreadsheets/d/1InaIkTuA4LCjqBBpZOdT1SHeAdLTUIvH/edit?usp=drivesdk

**Initial screen:** Passed. The niche has evidence of 15%+ EBITDA in a live deal signal, reoccurring project-based demand from public and commercial QA/QC requirements, above-GDP growth in geotechnical engineering and material testing segments, and Growth TAM above the $500M floor.

**Market TAM:** Identifier cited U.S. geotechnical engineering at about $9.05B in 2025, projected to $17.0B by 2035, and U.S. material testing at about $2.01B in 2025, projected to $2.43B by 2031.

**Target TAM:** Sufficient to advance to one-pager and scoring, but not yet enough to activate outreach without target discovery. The next validation question is whether there are 50+ acquirable regional geotechnical/CMT/special-inspection firms after excluding broad AEC firms, environmental-only firms, and PE-backed platforms.

**Key risks:** Construction cyclicality, utilization management, licensed PE and certified-technician dependency, E&O/professional-liability exposure, and risk of sliding into generic civil engineering or project-only work.

## Candidates Evaluated But Not Advanced

**Septic pumping / non-hazardous liquid waste services:** Real market with repeat service behavior, but weaker fit for G&B due to fleet intensity, environmental liability, lower Kay-fit, and likely micro-operator skew. Kept as watchlist only.

**Medical-grade water filtration service and replacement filters:** Attractive healthcare/lab end-market and recurring consumables, but the investable service-only target pool was not proven. The deal signal appeared manufacturer-heavy.

**Specialty steel / industrial MRO:** Too broad as stated and often inventory/capex-heavy. It fails the niche test unless a narrower service-only installed-base maintenance thesis is later supported by new evidence.

## Deliverables

- Chatroom: `brain/traces/agents/2026-06-30-niche-intelligence.md`
- One-pager local file: `/tmp/geotechnical-engineering-cmt-onepager.pptx`
- Scorecard local file: `/tmp/geotechnical-engineering-cmt-scorecard.xlsx`
- Tracker pre-write snapshot: `/tmp/weekly-review-prewrite-2026-06-30-geotech.json`
- Tracker final verification snapshot: `/tmp/weekly-review-final-2026-06-30-geotech.json`
- Integrity sidecar: `brain/trackers/niches/niche-intel-2026-06-30.json`

## Source Coverage Diagnostics

- RECENT web/social: partial. `last30days` Reddit search returned 403; HN and Polymarket returned no usable hits; X/Twitter and YouTube were unavailable in this headless setup. Web search produced usable public validation.
- RECENT Gmail: complete for targeted labels using read-only `--gmail-no-send`.
- RECENT Granola/vault calls: partial-complete; date-only Granola query worked and vault notes supplemented.
- HISTORICAL calls and Gmail: partial-complete for calls, complete for targeted older Gmail sweep using read-only `--gmail-no-send`.
- HISTORICAL OneNote: unavailable in this environment.
- HISTORICAL raw ChatGPT export: unavailable; no `selected_business_conversations.json` found.

## Tracker Update

WEEKLY REVIEW was re-fetched before writing. The new row was written by header map and verified by re-reading the sheet. Exact-match verification count for the niche hypothesis was 1.

Row values written:

| Header | Value |
| --- | --- |
| Rank | 31 |
| Niche Hypothesis | Geotechnical Engineering & Construction Materials Testing for Infrastructure/Commercial Construction |
| Current Status | New |
| Score | 2.31 |
| QSBS | Unknown / confirm with tax |
| Target Pool | 50+ likely nationally; exact deduped target count pending |
| Start Date | 2026-06-30 |

## Open Loops

- Target-discovery should validate a deduped list of 50+ acquirable regional geotechnical/CMT/special-inspection firms before any outreach activation.
- OneNote SEARCH FUND extraction remains unavailable in the headless environment.
- Raw ChatGPT export was not present on this VPS.
