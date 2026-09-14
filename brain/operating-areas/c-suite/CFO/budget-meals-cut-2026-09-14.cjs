const fs = require('fs');
const cp = require('child_process');
const crypto = require('crypto');
const assert = require('assert/strict');
const path = require('path');
const prefix = path.join(__dirname, '2026-09-14-budget-meals-cut-v2');
const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const write = (p, x) => fs.writeFileSync(p, JSON.stringify(x, null, 2) + '\n');
const hash = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const originals = Object.fromEntries(fs.readdirSync(__dirname).filter(n => /^2026-09-(12|14)-budget-(followup|runway)/.test(n)).map(n => [path.join(__dirname,n),hash(path.join(__dirname,n))]));
assert.ok(!fs.existsSync(prefix+'-calculations.json'), 'Version already exists; refuse overwrite');
const m = read(path.join(__dirname,'2026-09-14-budget-followup-calculations.json'));
const old = read(path.join(__dirname,'2026-09-14-budget-followup-cash-ledger.json'));
const round = n => Math.round((n+Number.EPSILON)*100)/100;
const money = n => '$'+round(n).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});
const fields = ['other_allowance','payroll','insurance','health','dealsx','conference','website'];
const cost = d => fields.reduce((n,k)=>n+d[k],0);
let cash = m.cash.total, savings = 0;
const ledger = old.map(d => {
  const date = new Date(d.date+'T00:00:00Z');
  const days = new Date(Date.UTC(date.getUTCFullYear(),date.getUTCMonth()+1,0)).getUTCDate();
  const saving = d.date >= '2026-09-14' ? 1112.08/days : 0;
  savings += saving;
  const x = {...d,other_allowance:d.other_allowance-saving};
  cash -= cost(x); x.end_cash = cash; return x;
});
assert.deepEqual(ledger.slice(0,13),old.slice(0,13));
assert.ok(Math.abs(savings-1112.08*(17/30+4+7/28))<1e-8);
const outflows = ledger.reduce((n,d)=>n+cost(d),0);
const gap = outflows+m.cash.dd_reserve-m.cash.total;
m.status = 'calculated; live verification pending';
m.normalized_monthly_burn_unrounded -= 1112.08;
m.normalized_monthly_burn = round(m.normalized_monthly_burn_unrounded);
m.halfpay_monthly_equivalent_unrounded -= 1112.08;
delete m.halfpay_monthly_equivalent_display_basis;
m.halfpay_rounding_note = 'Exact components govern: full18698.846667; half11297.903333. Dated scenarios retain weekly employer cash3415.82.';
m.normalized_other_monthly_allowance = 1108.22;
m.approved_changes = {...m.approved_changes,total_monthly:1582.95,meals_monthly:1005.13,meals:'User confirmed meals/entertainment no longer through fund; removed September14 inclusive',september_savings:round(1582.95*17/30),horizon_savings:round(1582.95*(17/30+4+7/28)),incremental_meals_september_savings:round(1005.13*17/30),incremental_meals_horizon_savings:round(savings)};
m.normalized_bridge.push(['Meals/entertainment removed from fund September14 inclusive',-1005.13]);
Object.assign(m.approved_changes,{total_monthly:1689.90,medical_repeat_allowance_removed:106.95,september_savings:round(1689.90*17/30),horizon_savings:round(1689.90*(17/30+4+7/28)),incremental_meals_horizon_savings:round(1005.13*(17/30+4+7/28)),incremental_meals_and_oneoff_monthly:1112.08,incremental_meals_and_oneoff_horizon_savings:round(savings)});
m.normalized_bridge.push(['One-off computer setup purchase, not medical; remove future repeat allowance September14',-106.95]);
Object.assign(m.timed,{other_total:round(ledger.reduce((n,d)=>n+d.other_allowance,0)),total_outflows:round(outflows),shortfall_to_protected_reserve:round(gap),unfunded_end_cash:round(cash),first_reserve_breach:ledger.find(d=>d.end_cash<m.cash.dd_reserve)?.date,approved_cut_cash_savings:m.approved_changes.horizon_savings,incremental_meals_cut_cash_savings:round(savings)});
m.monthly_gap_to_target = round(gap/m.timed.approved_savings_month_equivalents);
m.normalized_runway_months_comparison = round(m.cash.operations_before_commitments/m.normalized_monthly_burn_unrounded);
const factor = m.payroll.incremental_savings_factor;
for(const s of m.scenarios){
  const needed = gap-s.health_cash_savings, weekly = needed/s.reduced_payments/factor;
  s.gross_monthly_cut_exact = weekly*52/12;
  s.gross_monthly_cut = round(s.gross_monthly_cut_exact);
  s.gross_monthly_remaining = round(m.payroll.weekly_gross*52/12-s.gross_monthly_cut_exact);
  s.gross_cut_percent = round(weekly/m.payroll.weekly_gross*100);
  s.weekly_cut_rounded_up = Math.ceil(weekly*100)/100;
  s.weekly_gross_remaining = round(m.payroll.weekly_gross-s.weekly_cut_rounded_up);
  s.gross_monthly_cut_no_employer_tax_savings = round(needed/s.reduced_payments*52/12);
  s.employer_tax_savings_monthly = round(s.gross_monthly_cut_exact*(factor-1));
  assert.ok(Math.abs(cash+weekly*factor*s.reduced_payments+s.health_cash_savings-38000)<1e-7);
}
for(const a of m.alternating_paychecks){
  let balance=m.cash.total,breach=null;
  for(const d of ledger){
    balance-=cost(d); if(a.skipped_dates.includes(d.date)) balance+=d.payroll;
    if(!breach && balance<38000) breach=d.date;
    if(d.date==='2027-01-23'){a.jan23_cash=round(balance);a.jan23_reserve_shortfall=round(38000-balance);}
  }
  a.ending_cash=round(balance);a.reserve_shortfall=round(38000-balance);a.first_reserve_breach=breach;
}
for(const h of m.health_only) h.residual_gap=round(gap-h.total_maximum);
m.timed.incremental_meals_cut_cash_savings=round(1005.13*(17/30+4+7/28));
m.timed.incremental_meals_and_oneoff_cash_savings=round(savings);
m.assumptions[0]='August31 verified cash anchor; no September feed. September1-13 unchanged. Office/postage577.82 already removed; incremental meals1005.13 plus one-off106.95 repeat allowance removed September14 inclusive. Actual-calendar-day proration; no retroactive savings.';
m.assumptions[3]='Other allowance1108.22/month from Sep14;2798.12 through Sep13. Meals zero per user. ChatGPT217.75 KEEP. Travel rides/parking/gas189.70 retained. User confirms Aug6 Walgreens106.95 was one-off computer setup items while traveling, NOT medical; no future purchase planned. Office Supplies/Computer Accessories is proposed classification, not bookkeeper-posted. Historical actuals/QBO unchanged pending Anthony.';
m.assumptions[7]='Pending cancellation by user, NOT confirmed done: DocSend16.33; Howie35 unverified ongoing; Art Newspaper24 plus0.72 already in bank fees. All remain in base until confirmed. Voice10 and Slack15 unverified allowances retained; Voice may overlap Workspace. No research.';
m.assumptions[12]=m.halfpay_rounding_note;
m.pending_cancellations=[{item:'DocSend',monthly:16.33},{item:'Howie',monthly:35,ongoing_verified:false},{item:'The Art Newspaper',monthly:24,bank_fee:0.72}].map(x=>({...x,status:'Pending cancellation; user-owned, not confirmed done',removed_from_base:false}));
m.medical={monthly:0,prior_repeat_allowance:106.95,transaction:'2026-08-06 Walgreens',detail:'User-confirmed computer setup items while traveling, NOT medical',basis:'One-off office purchase; no future purchase planned',proposed_classification:'Office Supplies/Computer Accessories',bookkeeper_posted:false,historical_actuals_changed:false,removed_from_base:true,effective:'2026-09-14'};
for(const x of m.monthly_itemization){
  if(x.item==='Travel meals'){x.monthly=0;x.basis='User-confirmed removal from fund September14 inclusive';}
  if(x.item==='Medical'){x.monthly=0;x.basis='User confirms Aug6 Walgreens computer setup items while traveling, not medical. One-off; no future planned. Proposed Office Supplies/Computer Accessories, pending Anthony; historical actuals unchanged';}
  if(x.item==='Howie'||x.item==='Art Newspaper') x.basis+='; pending user cancellation, not confirmed done; retained';
}
for(const x of m.inventory_audit) if(['DocSend','Howie','The Art Newspaper'].includes(x.tool)){x.status='PENDING CANCELLATION / not confirmed done';x.evidence+=' User intends cancellation September14; cost retained until confirmed.';}
assert.ok(Math.abs(m.monthly_itemization.reduce((n,x)=>n+x.monthly,0)-m.normalized_monthly_burn_unrounded)<1e-8);
assert.ok(Math.abs(m.normalized_monthly_burn_unrounded-18698.846666667)<1e-7);
assert.ok(Math.abs(m.halfpay_monthly_equivalent_unrounded-11297.903333333)<1e-7);
const sheet='1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0';
const gog=args=>JSON.parse(cp.execFileSync('gog',[...args,'--json'],{encoding:'utf8',maxBuffer:8e6}));
const fetch=range=>gog(['sheets','get',sheet,range]);
const ranges={runway:"'Runway Forecast'!A1:Z",tech:"'Tech Stack Inventory'!A1:Z100"};
const before=Object.fromEntries(Object.entries(ranges).map(([k,r])=>[k,fetch(r)]));
write(prefix+'-prewrite.json',before);
const values=structuredClone(before.runway.values), tech=structuredClone(before.tech.values);
const set=(r,c,x)=>{while(values[r-1].length<c)values[r-1].push('');values[r-1][c-1]=String(x);};
const b=(r,x)=>set(r,2,x);
b(3,'Aug31 VERIFIED cash; Sep14 meals-cut v2 MODEL; no September feed');
for(const r of [7,25,30,78])b(r,m.normalized_monthly_burn);
for(const r of [8,31])b(r,m.normalized_runway_months_comparison);
for(const r of [9,32])b(r,m.timed.first_reserve_breach);
for(const r of [10,47])b(r,round(gap));
for(const r of [11,34])b(r,m.monthly_gap_to_target);
b(12,'August bank statements + initial Sep14 model + user-confirmed meals removal Sep14');
b(13,'Sep14 inclusive: office/postage577.82 already removed; meals1005.13 plus106.95 one-off repeat allowance now removed. Walgreens was computer setup items, NOT medical, per user; proposed office reclass pending Anthony, historical actuals unchanged. ChatGPT217.75 and conference1300 retained. Pending vendor cancellations remain in base.');
set(41,1,'Other allowance:2798.12 to Sep13;1108.22 from Sep14');b(41,m.timed.other_total);b(45,m.timed.total_outflows);
m.scenarios.forEach((s,i)=>[s.gross_monthly_cut,s.gross_monthly_remaining,s.employer_tax_savings_monthly,s.health_cash_savings,s.first_reduced_payment,s.reduced_payments].forEach((v,j)=>set(51+i,2+j,v)));
m.alternating_paychecks.forEach((a,i)=>[a.skipped_count,a.retained_count,a.savings,a.ending_cash,a.reserve_shortfall,a.first_reserve_breach].forEach((v,j)=>set(61+i,2+j,v)));
m.health_only.forEach((h,i)=>set(66+i,3,h.residual_gap));
set(78,1,'Rebuilt monthly base after office407.42 + postage170.40 + meals1005.13 + one-off106.95 cuts');b(80,round(m.normalized_monthly_burn_unrounded-19635.76));b(81,m.halfpay_monthly_equivalent_unrounded);
for(let i=0;i<11;i++)set(83+i,1,m.assumptions[i]);
set(92,1,m.assumptions[9]+' '+m.halfpay_rounding_note);
b(94,m.alternating_paychecks.map(a=>`${a.first_skipped}: ${money(a.jan23_cash)} / ${money(a.jan23_reserve_shortfall)}`).join('; '));
b(95,m.monthly_gap_basis+' Pending cancellations not completed; costs retained. No payroll, health, tasks, email, Slack or commits. Initial Sep14 and Sep12 artifacts immutable.');
const pendingRows=[];
tech.forEach((r,i)=>{if(['DocSend','Howie'].includes(r[0])){r[6]='PENDING CANCELLATION / not confirmed done';r[8]+=' Sep14: user intends cancellation; retain current cost until confirmed. Howie ongoing charge remains unverified.';pendingRows.push(i+1);}});
assert.ok(!tech.some(r=>/art newspaper/i.test(r[0]||'')),'Unexpected Art Newspaper row; inspect before proceeding');
const plan=[];
const diff=(tab,a,z,limit)=>{for(let i=0;i<limit;i++)for(let j=0;j<26;j++)if(String(a[i]?.[j]??'')!==String(z[i]?.[j]??''))plan.push({range:`'${tab}'!${String.fromCharCode(65+j)}${i+1}`,values:[[z[i][j]]]});};
diff('Runway Forecast',before.runway.values,values,95);diff('Tech Stack Inventory',before.tech.values,tech,tech.length);
write(prefix+'-write-plan.json',plan);
m.rollback_snapshot=prefix+'-prewrite.json';m.report_path=prefix+'-report.md';
write(prefix+'-calculations.json',m);write(prefix+'-cash-ledger.json',ledger);
for(const [k,r] of Object.entries(ranges))assert.deepEqual(fetch(r).values,before[k].values,'Concurrent edit; refusing stale write');
for(const p of plan)gog(['sheets','update',sheet,p.range,'--values-json',JSON.stringify(p.values),'--input','RAW']);
const after=Object.fromEntries(Object.entries(ranges).map(([k,r])=>[k,fetch(r)]));write(prefix+'-postverify.json',after);
for(const [k,expected] of [['runway',values],['tech',tech]])for(let i=0;i<Math.max(expected.length,after[k].values.length);i++)for(let j=0;j<26;j++)assert.equal(String(after[k].values[i]?.[j]??''),String(expected[i]?.[j]??''),`${k}:${i+1}/${j+1}`);
assert.deepEqual(after.runway.values.slice(95),before.runway.values.slice(95));
assert.deepEqual(after.runway.values.slice(15,24),before.runway.values.slice(15,24));
for(const [p,h] of Object.entries(originals))assert.equal(hash(p),h);
m.status='complete; live verified';
m.validation={live_cells_match:true,historical_rows_96_onward_preserved:true,historical_burn_actuals_preserved:true,initial_sep14_and_sep12_hashes_unchanged:true,original_hashes:originals,september_1_to_13_unchanged:true,itemization_reconciles:true,inventory_pending_rows:pendingRows,art_newspaper_row_not_created:true,no_payroll_health_email_slack_tasks_commits:true};
write(prefix+'-calculations.json',m);
const table=(heads,rows)=>'| '+heads.join(' | ')+' |\n| '+heads.map(()=>'---').join(' | ')+' |\n'+rows.map(r=>'| '+r.join(' | ')+' |').join('\n');
fs.writeFileSync(m.report_path,`---
schema_version: 1.1.0
date: 2026-09-14
type: budget-report
status: published
skill_origin: budget-manager
kay_approved: null
projects: []
tags: [date/2026-09-14, output, output/budget-report, status/published]
---

# September 14 Meals Cut, Version 2

Sources: [[operating-areas/c-suite/CFO/2026-09-14-budget-runway-update|Initial September14 report]], [[operating-areas/c-suite/CFO/2026-09-14-budget-followup-calculations.json|Initial model]]. This version: [[operating-areas/c-suite/CFO/2026-09-14-budget-meals-cut-v2-calculations.json|Model]] and [[operating-areas/c-suite/CFO/2026-09-14-budget-meals-cut-v2-cash-ledger.json|Ledger]]. No new research or bank feed.

## Confirmed Change

Meals/entertainment1005.13/month and the106.95 repeat allowance for a one-off computer setup purchase removed from September14 inclusive only:1112.08/month incremental cut. Office/postage577.82/month was already removed and is not subtracted again. Incremental September saving ${money(1112.08*17/30)}; incremental saving through February7 ${money(savings)}. September1-13 unchanged.

Full monthly base **${money(m.normalized_monthly_burn)}**, exact18698.846667. Hypothetical half-pay equivalent **${money(m.halfpay_monthly_equivalent_unrounded)}**, exact11297.903333. Other allowance1108.22/month.

DocSend16.33 and Howie35 remain in the base and existing inventory rows are pending cancellation, not done. Howie ongoing billing is unverified. Art Newspaper24 plus0.72 in bank fees remains pending user cancellation; no live inventory row exists and none was created. No double-counted fee. User-owned tasks are handled by the parent, not this update.

ChatGPT217.75 retained. Conference1300 retained once, planned/unbooked. **User-confirmed factual correction:** August6 Walgreens106.95 was computer setup items purchased while traveling, NOT medical. It was one-off with no future purchase planned, so the forward repeat allowance is zero from September14. **Office Supplies/Computer Accessories is a proposed classification, not bookkeeper-posted.** Historical actuals and QBO remain unchanged pending Anthony's reclassification. Parent handles the chat draft; no email sent.

## Monthly Itemization

${table(['Item','Monthly','Basis'],m.monthly_itemization.map(x=>[x.item,money(x.monthly),x.basis]))}

## Dated Forecast

August31 verified cash ${money(m.cash.total)}; DD reserve ${money(m.cash.dd_reserve)}. Modeled outflows through February7 ${money(outflows)}; ending cash ${money(cash)}; reserve funding gap **${money(gap)}**. First reserve breach ${m.timed.first_reserve_breach}. Additional monthly savings required from September14 ${money(m.monthly_gap_to_target)}. Normalized comparison ${m.normalized_runway_months_comparison} months is not a dated cash result.

${table(['First skipped paycheck','Feb7 cash','DD gap','Jan23 cash','Jan23 gap','First breach'],m.alternating_paychecks.map(a=>[a.first_skipped,money(a.ending_cash),money(a.reserve_shortfall),money(a.jan23_cash),money(a.jan23_reserve_shortfall),a.first_reserve_breach]))}

${table(['Hypothetical scenario','Effective','Gross monthly cut','Gross remaining','Employer tax savings/mo','Health cash savings'],m.scenarios.map(s=>[s.label,s.effective,money(s.gross_monthly_cut),money(s.gross_monthly_remaining),money(s.employer_tax_savings_monthly),money(s.health_cash_savings)]))}

Health-only residual gaps: ${m.health_only.map(h=>money(h.residual_gap)).join('; ')} (October then January). No compensation changes executed.

## Assumptions

${m.assumptions.map(s=>'- '+s).join('\n')}

## Verification

Live snapshot: [[operating-areas/c-suite/CFO/2026-09-14-budget-meals-cut-v2-prewrite.json|Prewrite]]. Read-back: [[operating-areas/c-suite/CFO/2026-09-14-budget-meals-cut-v2-postverify.json|Postverify]]. All intended cells match; current Runway Forecast scenarios, gaps and assumptions updated within rows1:95. Historical rows96 onward and burn actuals unchanged. Initial September14 and all September12 source hashes unchanged. Itemization reconciles. No emails, Slack, payroll changes, tasks or commits. Old September12 publisher not executed.
`);
console.log(JSON.stringify({status:m.status,full:m.normalized_monthly_burn_unrounded,half:m.halfpay_monthly_equivalent_unrounded,savings:round(savings),gap:round(gap),outflows:round(outflows),monthly_gap:m.monthly_gap_to_target,breach:m.timed.first_reserve_breach,alternating:m.alternating_paychecks,report:m.report_path,validation:m.validation},null,2));
