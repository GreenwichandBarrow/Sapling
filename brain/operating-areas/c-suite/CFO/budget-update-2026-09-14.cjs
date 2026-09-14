const fs = require('fs');
const cp = require('child_process');
const crypto = require('crypto');
const assert = require('assert/strict');
const path = require('path');
const dir = __dirname;
const prefix = path.join(dir, '2026-09-14-budget-followup');
const oldModelPath = path.join(dir, '2026-09-12-budget-followup-calculations.json');
const oldLedgerPath = path.join(dir, '2026-09-12-budget-followup-cash-ledger.json');
const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const write = (p, x) => fs.writeFileSync(p, JSON.stringify(x, null, 2) + '\n');
const hash = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const originals = Object.fromEntries([oldModelPath, oldLedgerPath].map(p => [p, hash(p)]));
const m = read(oldModelPath), old = read(oldLedgerPath);
const round = n => Math.round((n + Number.EPSILON) * 100) / 100;
const money = n => '$' + round(n).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
const fields = ['other_allowance','payroll','insurance','health','dealsx','conference','website'];
const cost = d => fields.reduce((n, k) => n + d[k], 0);
let cash = m.cash.total, savings = 0;
const ledger = old.map(d => {
  const date = new Date(d.date + 'T00:00:00Z');
  const days = new Date(Date.UTC(date.getUTCFullYear(), date.getUTCMonth() + 1, 0)).getUTCDate();
  const saving = d.date >= '2026-09-14' ? 577.82 / days : 0;
  savings += saving;
  const x = {...d, other_allowance: d.other_allowance - saving};
  cash -= cost(x);
  x.end_cash = cash;
  return x;
});
assert.deepEqual(ledger.slice(0,13), old.slice(0,13));
assert.ok(Math.abs(savings - 577.82 * (17/30 + 4 + 7/28)) < 1e-8);
const outflows = ledger.reduce((n,d) => n + cost(d), 0);
const gap = outflows + m.cash.dd_reserve - m.cash.total;
m.status = 'calculated; live verification pending';
m.run_date = '2026-09-14';
m.normalized_monthly_burn = 19810.93;
m.normalized_other_monthly_allowance = 2220.30;
m.payroll.monthly_total_unrounded = m.payroll.weekly_employer_total * 52/12;
m.normalized_monthly_burn_unrounded = m.payroll.monthly_total_unrounded + 2750 + 8.94*52/12 + 2220.30;
m.halfpay_monthly_equivalent_unrounded = m.normalized_monthly_burn_unrounded - m.payroll.monthly_total_unrounded/2;
m.halfpay_monthly_equivalent_display_basis = 12409.985;
m.halfpay_rounding_note = 'Exact component totals govern: full 19810.926666667; half 12409.983333333. Rounded full19810.93 less rounded payroll14801.89/2 yields comparison12409.985 only; dated scenarios use weekly cash3415.82.';
m.approved_changes = {effective:'2026-09-14',office_purchases_monthly:407.42,printing_postage_monthly:170.40,total_monthly:577.82,september_savings:round(577.82*17/30),horizon_savings:round(savings),chatgpt:'KEEP essential daily;217.75/month unchanged',meals:'1005.13/month retained; removal not approved',conference:'1300 planned/unbooked pending decision; retained once'};
m.normalized_bridge.push(['Stop future office purchases from September14',-407.42],['Stop printing/postage from September14',-170.40]);
Object.assign(m.timed, {other_total:round(ledger.reduce((n,d)=>n+d.other_allowance,0)),total_outflows:round(outflows),shortfall_to_protected_reserve:round(gap),unfunded_end_cash:round(cash),first_reserve_breach:ledger.find(d=>d.end_cash<m.cash.dd_reserve)?.date,projected_sep14_opening_cash_not_bank_fact:round(ledger[12].end_cash),approved_savings_month_equivalents:17/30+4+7/28,approved_cut_cash_savings:round(savings)});
m.monthly_gap_to_target = round(gap / m.timed.approved_savings_month_equivalents);
m.monthly_gap_basis = 'Additional monthly savings effective September14 through February7 inclusive; 4.816666667 calendar-month equivalents, not retroactive September1.';
m.normalized_runway_months_comparison = round(m.cash.operations_before_commitments / m.normalized_monthly_burn_unrounded);
const factor = m.payroll.incremental_savings_factor;
for (const s of m.scenarios) {
  const needed = gap - s.health_cash_savings;
  const weekly = needed / s.reduced_payments / factor;
  s.gross_monthly_cut_exact = weekly * 52/12;
  s.gross_monthly_cut = round(s.gross_monthly_cut_exact);
  s.gross_monthly_remaining = round(m.payroll.weekly_gross*52/12-s.gross_monthly_cut_exact);
  s.gross_cut_percent = round(weekly/m.payroll.weekly_gross*100);
  s.weekly_cut_rounded_up = Math.ceil(weekly*100)/100;
  s.weekly_gross_remaining = round(m.payroll.weekly_gross-s.weekly_cut_rounded_up);
  s.gross_monthly_cut_no_employer_tax_savings = round(needed/s.reduced_payments*52/12);
  s.employer_tax_savings_monthly = round(s.gross_monthly_cut_exact*(factor-1));
  assert.ok(Math.abs(cash + weekly*factor*s.reduced_payments+s.health_cash_savings-38000)<1e-7);
}
for (const a of m.alternating_paychecks) {
  let balance = m.cash.total, breach = null;
  for (const d of ledger) {
    balance -= cost(d);
    if(a.skipped_dates.includes(d.date)) balance += d.payroll;
    if(!breach && balance < 38000) breach = d.date;
    if(d.date === '2027-01-23') {
      a.jan23_cash = round(balance);
      a.jan23_reserve_shortfall = round(38000-balance);
      a.jan23_skipped_count = a.skipped_dates.filter(x=>x<=d.date).length;
    }
  }
  a.ending_cash = round(balance);
  a.reserve_shortfall = round(38000-balance);
  a.first_reserve_breach = breach;
}
for (const h of m.health_only) h.residual_gap = round(gap-h.total_maximum);
m.assumptions[0] = 'Cash forecast starts September1 from August31 verified bank anchor; no September feed. Sep1-13 unchanged; approved577.82/month cuts start September14, prorated by actual calendar-month days. No retroactive savings.';
m.assumptions[3] = 'Other allowance2220.30/month from Sep14 (previous2798.12 through Sep13). Office407.42 and printing/postage170.40 stopped. ChatGPT217.75 KEEP essential daily. Meals1005.13 retained; cut NOT approved. Travel1194.83 is allowance, not a recurring bill.';
m.assumptions[5] = 'Conference1300 planned/unbooked pending decision, modeled once October1, not a booked obligation. Website348 expected November11; tax unknown. No conference savings assumed.';
m.assumptions.push(m.monthly_gap_basis,m.halfpay_rounding_note,'All salary/health scenarios hypothetical; no payroll instructions or elections changed.');
const chat = m.inventory_audit.find(x=>x.tool==='ChatGPT / OpenAI');
chat.status = 'KEEP / essential daily';
chat.evidence = 'Aug08 billed217.75; user confirmed September14 essential daily. Retain217.75/month unchanged; no downgrade saving assumed.';
m.monthly_itemization = [
  ['Gross salary',m.payroll.weekly_gross*52/12,'Recurring; inferred weekly cash cadence'],
  ['Employer payroll tax',m.payroll.weekly_employer_tax*52/12,'Recurring estimate; observed rate'],
  ['Healthcare',2750,'Recurring; full day-5 payments modeled'],
  ['Business insurance',8.94*52/12,'Recurring; inferred weekly cadence'],
  ['Software including Gusto fee',472.91,'Recurring base; includes Gusto106.90 and other tech366.01; ChatGPT217.75 KEEP'],
  ['Bookkeeping',247,'Recurring'],
  ['Art Newspaper',24,'Allowance; recurring cadence unverified; fee in bank allowance'],
  ['Bank fees',3.81,'Allowance'],
  ['Travel meals',1005.13,'Variable allowance; removal NOT approved'],
  ['Travel rides',60.93,'Variable allowance'],
  ['Travel parking',2.50,'Variable allowance'],
  ['Travel gas',126.27,'Variable allowance'],
  ['Medical',106.95,'Variable allowance; not healthcare premium'],
  ['Vehicle repairs',110.80,'Variable allowance'],
  ['Howie',35,'Unverified vendor allowance'],
  ['Google Voice',10,'Unverified vendor allowance; may overlap Workspace'],
  ['Slack',15,'Unverified vendor allowance']
].map(([item,monthly,basis])=>({item,monthly,basis}));
assert.ok(Math.abs(m.monthly_itemization.reduce((n,x)=>n+x.monthly,0)-m.normalized_monthly_burn_unrounded)<1e-8);
assert.ok(Math.abs(m.monthly_itemization.slice(4).reduce((n,x)=>n+x.monthly,0)-2220.30)<1e-8);
const sheet = '1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0';
const gog = args => JSON.parse(cp.execFileSync('gog',[...args,'--json'],{encoding:'utf8',maxBuffer:8e6}));
const fetch = () => gog(['sheets','get',sheet,"'Runway Forecast'!A1:G"]);
const before = fetch();
write(prefix+'-prewrite.json',before);
m.rollback_snapshot = prefix+'-prewrite.json';
const values = structuredClone(before.values);
const set = (r,c,x) => {while(values[r-1].length<c) values[r-1].push(''); values[r-1][c-1]=String(x);};
const b = (r,x) => set(r,2,x);
b(2,m.run_date); b(3,'Aug31 VERIFIED cash; Sep14 MODEL update, no September feed');
for(const r of [7,25,30,78]) b(r,m.normalized_monthly_burn);
set(8,1,'Normalized runway comparison; Aug31 operations / new monthly base');
for(const r of [8,31]) b(r,m.normalized_runway_months_comparison);
set(9,1,'Projected first DD reserve breach (dated ledger)');
for(const r of [9,32]) b(r,m.timed.first_reserve_breach);
for(const r of [10,47]) b(r,round(gap));
for(const r of [11,34]) b(r,m.monthly_gap_to_target);
set(11,1,'Additional monthly savings needed from Sep14');
b(12,'August bank statements + Sep12 model + user-confirmed Sep14 cuts');
b(13,'Office407.42 + printing/postage170.40 stopped Sep14; no retroactive savings. ChatGPT217.75 KEEP; meals1005.13 retained. Salary/health scenarios hypothetical; no changes executed.');
set(41,1,'Other allowance:2798.12 to Sep13;2220.30 from Sep14'); b(41,m.timed.other_total);
set(43,1,'Conference planned/unbooked pending decision');
b(45,m.timed.total_outflows);
set(48,1,'Projected Sep14 opening NOT BANK FACT'); b(48,m.timed.projected_sep14_opening_cash_not_bank_fact);
m.scenarios.forEach((s,i)=>[s.gross_monthly_cut,s.gross_monthly_remaining,s.employer_tax_savings_monthly,s.health_cash_savings,s.first_reduced_payment,s.reduced_payments].forEach((v,j)=>set(51+i,2+j,v)));
m.alternating_paychecks.forEach((a,i)=>[a.skipped_count,a.retained_count,a.savings,a.ending_cash,a.reserve_shortfall,a.first_reserve_breach].forEach((v,j)=>set(61+i,2+j,v)));
m.health_only.forEach((h,i)=>set(66+i,3,h.residual_gap));
set(78,1,'Rebuilt monthly base after office407.42 + postage170.40 cuts');
b(80,round(m.normalized_monthly_burn-19635.76));
set(81,1,'Half-pay monthly equivalent (exact components)'); b(81,m.halfpay_monthly_equivalent_unrounded);
for(let i=0;i<11;i++) set(83+i,1,m.assumptions[i]);
set(92,1,m.assumptions[9]+' Unrounded monthly payroll14801.886667; full base19810.926667; half12409.983333.');
set(94,1,'Jan23 every-other-pay cash / DD gap (first skipped date)');
b(94,m.alternating_paychecks.map(a=>`${a.first_skipped}: ${money(a.jan23_cash)} / ${money(a.jan23_reserve_shortfall)}`).join('; '));
set(95,1,'Monthly gap basis / scope'); b(95,m.monthly_gap_basis+' No payroll, health, task, tech-sheet, email or Slack changes.');
assert.deepEqual(values.slice(95),before.values.slice(95));
assert.deepEqual(values.slice(15,24),before.values.slice(15,24));
// Bound each write to contiguous changed cells within one existing row.
const plan = [];
for(let i=0;i<95;i++) {
  for(let j=0;j<7;) {
    if(String(values[i]?.[j]??'')===String(before.values[i]?.[j]??'')){j++;continue;}
    const start=j, cells=[];
    while(j<7 && String(values[i]?.[j]??'')!==String(before.values[i]?.[j]??'')) cells.push(values[i][j++]);
    plan.push({range:`'Runway Forecast'!${String.fromCharCode(65+start)}${i+1}:${String.fromCharCode(64+j)}${i+1}`,values:[cells]});
  }
}
write(prefix+'-write-plan.json',plan);
m.report_path = path.join(dir,'2026-09-14-budget-runway-update.md');
m.validation = {live_cells_match:false,original_hashes:originals};
write(prefix+'-calculations.json',m); write(prefix+'-cash-ledger.json',ledger);
const guard = fetch();
assert.deepEqual(guard.values,before.values,'Live sheet changed during preparation; refusing stale write');
write(prefix+'-prewrite.json',guard);
for(const p of plan) gog(['sheets','update',sheet,p.range,'--values-json',JSON.stringify(p.values),'--input','RAW']);
const after = fetch();
write(prefix+'-postverify.json',after);
for(let i=0;i<values.length;i++) for(let j=0;j<7;j++) assert.equal(String(after.values[i]?.[j]??''),String(values[i]?.[j]??''),`cell ${i+1}/${j+1}`);
assert.deepEqual(after.values.slice(95),before.values.slice(95));
assert.deepEqual(after.values.slice(15,24),before.values.slice(15,24));
for(const [p,h] of Object.entries(originals)) assert.equal(hash(p),h);
m.status = 'report and dashboard complete; verified';
m.validation = {...m.validation,live_cells_match:true,historical_rows_96_onward_preserved:true,historical_burn_actuals_preserved:true,september_1_to_13_unchanged:true,original_sep12_files_immutable:true,itemization_reconciles:true,no_tech_sheet_write:true,no_email:true,no_slack:true,no_payroll_or_health_change:true,no_tasks_or_commits:true,bounded_ranges_written:plan.length};
write(prefix+'-calculations.json',m);
const table = (headers,rows) => '| '+headers.join(' | ')+' |\n| '+headers.map(()=>'---').join(' | ')+' |\n'+rows.map(r=>'| '+r.join(' | ')+' |').join('\n');
const report = `---
schema_version: 1.2.0
date: 2026-09-14
type: budget-report
status: published
skill_origin: budget-manager
kay_approved: null
projects: []
tags: [date/2026-09-14, output, output/budget-report, status/published]
---

# September 14 Budget Forecast Update

Source: [[outputs/2026-09-12-budget-runway-followup-aug-2026|September 12 budget report]]. New artifacts: [[operating-areas/c-suite/CFO/2026-09-14-budget-followup-calculations.json|Updated model]] and [[operating-areas/c-suite/CFO/2026-09-14-budget-followup-cash-ledger.json|Dated ledger]]. Original September12 artifacts remain immutable. [Live Runway Forecast](${m.sources.dashboard}). No new research or bank feed.

## Confirmed Changes

Stop future office purchases407.42/month and printing/postage170.40/month from September14:577.82/month. September savings ${money(m.approved_changes.september_savings)} (17/30); savings through February7 ${money(savings)}. September1-13 unchanged. ChatGPT217.75/month KEEP, essential daily. Meals1005.13/month remain: removal NOT approved. Conference1300 remains planned/unbooked pending decision, included once October1. No payroll or health change authorized or executed.

## Estimated Monthly Budget

${table(['Line item','Monthly estimate','Basis'],m.monthly_itemization.map(x=>[x.item,money(x.monthly),x.basis]))}

Other operating allowance subtotal:2220.30. Software472.91 includes Gusto106.90 plus other tech366.01; ChatGPT217.75 is included, not added again. Travel subtotal1194.83. Variable categories reflect retained estimates, not confirmed repeat bills; Howie/Voice/Slack are explicitly unverified. Office purchases and printing/postage are zero going forward.

Full-pay exact monthly total:19810.926666667, displayed **${money(m.normalized_monthly_burn)}**. Half-pay exact monthly equivalent:12409.983333333, displayed **${money(m.halfpay_monthly_equivalent_unrounded)}**. Payroll including employer tax is14801.886666667 unrounded; half is7400.943333333. The earlier rounded comparison12409.985 comes from19810.93 minus14801.89/2, not the exact component sum. Rounded individual rows may differ from totals by one cent. Half-pay is hypothetical and affects salary/employer tax only; healthcare and Gusto fee remain unchanged.

## One-Time Forecast Outflows

DealsX3220 once September28; conference1300 once October1 pending decision; website348 pretax November11. These are outside the normalized monthly base. Existing timing and uncertainty assumptions retained.

## Dated Runway

August31 verified cash ${money(m.cash.total)}; protected reserve ${money(m.cash.dd_reserve)}. September14 projected opening ${money(m.timed.projected_sep14_opening_cash_not_bank_fact)} is a model, not bank fact. Total outflows through February7 ${money(outflows)}, including other allowance ${money(m.timed.other_total)}. Ending cash ${money(cash)}; reserve funding gap **${money(gap)}**. First projected reserve breach ${m.timed.first_reserve_breach}. Additional monthly saving required from September14: ${money(m.monthly_gap_to_target)} across4.816666667 calendar-month equivalents. Normalized runway comparison ${m.normalized_runway_months_comparison} months is not a dated cash result.

## Every Other Paycheck

Hypothetical reduction, not deferral or payroll instruction. Weekly employer cash3415.82; existing skipped dates retained. Healthcare2750/month and fixed payroll fee unchanged. Both evaluation dates inclusive; all reserve gaps below are against38000.

${table(['First skipped','Feb7 cash','Feb7 reserve gap','Jan23 cash','Jan23 reserve gap','First breach'],m.alternating_paychecks.map(a=>[a.first_skipped,money(a.ending_cash),money(a.reserve_shortfall),money(a.jan23_cash),money(a.jan23_reserve_shortfall),a.first_reserve_breach]))}

## Other Hypothetical Scenarios

${table(['Scenario / effective','Gross monthly cut','Gross remaining','Employer tax saving/mo','Health cash saved'],m.scenarios.map(s=>[s.label+' / '+s.effective,money(s.gross_monthly_cut),money(s.gross_monthly_remaining),money(s.employer_tax_savings_monthly),money(s.health_cash_savings)]))}

Health-only maximum cuts: October start leaves gap ${money(m.health_only[0].residual_gap)}; January start leaves ${money(m.health_only[1].residual_gap)}. No scenario is an approved compensation/health change.

## Assumptions

${m.assumptions.map(s=>'- '+s).join('\n')}

## Verification

Live pre-write snapshot saved; all intended current cells read back and matched. Only ${plan.length} bounded ranges within rows1:95 changed. Rows96 onward and historical burn actuals unchanged. September1-13 ledger entries unchanged. Source file SHA256 hashes unchanged. Itemization reconciles. Tech inventory sheet untouched; new model records ChatGPT KEEP. No emails, Slack, payroll, health, tasks, commits or old publish-script execution.
`;
fs.writeFileSync(m.report_path,report);
assert.ok(fs.statSync(m.report_path).size>1000);
console.log(JSON.stringify({status:m.status,monthly:m.normalized_monthly_burn,exact:m.normalized_monthly_burn_unrounded,half_exact:m.halfpay_monthly_equivalent_unrounded,gap:m.timed.shortfall_to_protected_reserve,outflows:m.timed.total_outflows,alternating:m.alternating_paychecks,report:m.report_path,validation:m.validation},null,2));
