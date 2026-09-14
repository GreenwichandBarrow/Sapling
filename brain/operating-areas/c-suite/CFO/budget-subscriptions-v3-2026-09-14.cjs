const fs = require('fs');
const cp = require('child_process');
const crypto = require('crypto');
const assert = require('assert/strict');
const path = require('path');
const prefix = path.join(__dirname, '2026-09-14-budget-subscriptions-v3');
const prior = path.join(__dirname, '2026-09-14-budget-meals-cut-v2');
const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const write = (p, x) => fs.writeFileSync(p, JSON.stringify(x, null, 2) + '\n');
const hash = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const originals = Object.fromEntries(fs.readdirSync(__dirname).filter(n => /^2026-09-(12|14)-budget-/.test(n)).map(n => [path.join(__dirname,n),hash(path.join(__dirname,n))]));
assert.ok(!fs.existsSync(prefix+'-calculations.json'), 'Version already exists');
const m = read(prior+'-calculations.json'), old = read(prior+'-cash-ledger.json');
const round = n => Math.round((n+Number.EPSILON)*100)/100;
const money = n => '$'+round(n).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});
const fields = ['other_allowance','payroll','insurance','health','dealsx','conference','website'];
const cost = d => fields.reduce((n,k)=>n+d[k],0);
let cash=m.cash.total, savings=0, septemberSavings=0;
const ledger=old.map(d=>{
  const date=new Date(d.date+'T00:00:00Z');
  const days=new Date(Date.UTC(date.getUTCFullYear(),date.getUTCMonth()+1,0)).getUTCDate();
  const saving=d.date<'2026-09-14'?0:(16.33+(d.date<'2026-12-14'?35:0))/days;
  savings+=saving;
  if(d.date.startsWith('2026-09'))septemberSavings+=saving;
  const x={...d,other_allowance:d.other_allowance-saving};
  cash-=cost(x);x.end_cash=cash;return x;
});
assert.deepEqual(ledger.slice(0,13),old.slice(0,13));
assert.ok(Math.abs(savings-(16.33*(17/30+4+7/28)+35*(17/30+2+13/31)))<1e-8);
for(let i=0;i<ledger.length;i++)for(const k of fields.filter(k=>k!=='other_allowance'))assert.equal(ledger[i][k],old[i][k]);
const outflows=ledger.reduce((n,d)=>n+cost(d),0), gap=outflows+m.cash.dd_reserve-m.cash.total;
m.status='calculated; live verification pending';
delete m.validation;
m.version=3;
m.normalized_monthly_burn_unrounded-=51.33;
m.normalized_monthly_burn=round(m.normalized_monthly_burn_unrounded);
m.halfpay_monthly_equivalent_unrounded-=51.33;
m.normalized_other_monthly_allowance=1056.89;
m.after_pause={effective:'2026-12-14',howie_monthly_allowance:35,actual_billing_confirmed:false,full_monthly_unrounded:m.normalized_monthly_burn_unrounded+35,halfpay_monthly_unrounded:m.halfpay_monthly_equivalent_unrounded+35,other_monthly_allowance:1091.89};
m.halfpay_rounding_note='During pause full18647.516667; hypothetical half11246.573333. From Dec14 full18682.516667; half11281.573333 includes UNVERIFIED Howie35 allowance, not confirmed actual billing. Weekly employer cash3415.82 unchanged.';
const vendorNote='User Sep14: DocSend canceled, zero from Sep14. Howie paused3 months no charge; assumed Sep14-Dec13 inclusive; reinstate UNVERIFIED35 allowance Dec14 absent renewal cancellation, NOT confirmed actual billing. Newspaper cancellation email sent only; retain24 plus0.72 already in bank fees pending confirmed effective date.';
m.subscription_changes={effective:'2026-09-14',evidence:'User confirmation September14; no email search',docsend:{status:'canceled',monthly:0,removed_monthly:16.33},howie:{status:'paused; no charge',monthly:0,pause_start:'2026-09-14',assumed_pause_end:'2026-12-13',resume_allowance_date:'2026-12-14',resume_allowance:35,actual_billing_confirmed:false},newspaper:{status:'Cancellation email sent only; effective date unconfirmed',monthly:24,bank_fee:0.72,retained:true},monthly_reduction_during_pause:51.33,monthly_reduction_after_pause:16.33,september_savings:round(septemberSavings),horizon_savings:round(savings)};
m.approved_changes.total_monthly=1741.23;
m.approved_changes.total_monthly_after_howie_pause=1706.23;
m.approved_changes.september_savings=round(1689.90*17/30+septemberSavings);
m.approved_changes.horizon_savings=round(1689.90*(17/30+4+7/28)+savings);
m.approved_changes.subscription_changes=m.subscription_changes;
m.normalized_bridge.push(['DocSend canceled September14',-16.33],['Howie UNVERIFIED allowance removed during Sep14-Dec13 pause; restore35 Dec14',-35]);
Object.assign(m.timed,{other_total:round(ledger.reduce((n,d)=>n+d.other_allowance,0)),total_outflows:round(outflows),shortfall_to_protected_reserve:round(gap),unfunded_end_cash:round(cash),first_reserve_breach:ledger.find(d=>d.end_cash<m.cash.dd_reserve)?.date,approved_cut_cash_savings:m.approved_changes.horizon_savings,incremental_subscription_cash_savings:round(savings)});
m.monthly_gap_to_target=round(gap/m.timed.approved_savings_month_equivalents);
m.normalized_runway_months_comparison=round(m.cash.operations_before_commitments/m.normalized_monthly_burn_unrounded);
const factor=m.payroll.incremental_savings_factor;
for(const s of m.scenarios){
  const needed=gap-s.health_cash_savings, weekly=needed/s.reduced_payments/factor;
  s.gross_monthly_cut_exact=weekly*52/12;
  s.gross_monthly_cut=round(s.gross_monthly_cut_exact);
  s.gross_monthly_remaining=round(m.payroll.weekly_gross*52/12-s.gross_monthly_cut_exact);
  s.gross_cut_percent=round(weekly/m.payroll.weekly_gross*100);
  s.weekly_cut_rounded_up=Math.ceil(weekly*100)/100;
  s.weekly_gross_remaining=round(m.payroll.weekly_gross-s.weekly_cut_rounded_up);
  s.gross_monthly_cut_no_employer_tax_savings=round(needed/s.reduced_payments*52/12);
  s.employer_tax_savings_monthly=round(s.gross_monthly_cut_exact*(factor-1));
  assert.ok(Math.abs(cash+weekly*factor*s.reduced_payments+s.health_cash_savings-38000)<1e-7);
}
for(const a of m.alternating_paychecks){
  let balance=m.cash.total,breach=null;
  for(const d of ledger){
    balance-=cost(d);if(a.skipped_dates.includes(d.date))balance+=d.payroll;
    if(!breach&&balance<38000)breach=d.date;
    if(d.date==='2027-01-23'){a.jan23_cash=round(balance);a.jan23_reserve_shortfall=round(38000-balance);}
  }
  a.ending_cash=round(balance);a.reserve_shortfall=round(38000-balance);a.first_reserve_breach=breach;
}
for(const h of m.health_only)h.residual_gap=round(gap-h.total_maximum);
m.assumptions[0]+=' V3 removes DocSend16.33 and Howie35 from Sep14, restoring Howie35 allowance Dec14. Calendar-day proration retained.';
m.assumptions[3]=m.assumptions[3].replace('Other allowance1108.22/month from Sep14;2798.12 through Sep13.','Other allowance1056.89/month Sep14-Dec13;1091.89 from Dec14;2798.12 through Sep13.');
m.assumptions[7]=vendorNote+' Voice10 and Slack15 unverified allowances retained; Voice may overlap Workspace.';
m.assumptions[12]=m.halfpay_rounding_note;
m.pending_cancellations=[{item:'The Art Newspaper',monthly:24,bank_fee:0.72,status:'Cancellation email sent; effective date unconfirmed',removed_from_base:false}];
for(const x of m.monthly_itemization){
  if(x.item==='Software including Gusto fee'){x.monthly=456.58;x.basis='Recurring base excluding canceled DocSend16.33 from Sep14; Gusto106.90 fixed fee and ChatGPT217.75 unchanged';}
  if(x.item==='Howie'){x.monthly=0;x.basis='User-confirmed no-charge3 month pause. Assumed Sep14-Dec13; UNVERIFIED35 allowance restored Dec14, not confirmed actual billing';}
  if(x.item==='Art Newspaper')x.basis='Cancellation email sent only;24 retained pending confirmed effective date;0.72 fee remains within bank fees';
}
for(const x of m.inventory_audit){
  if(x.tool==='DocSend'){x.monthly_equivalent=0;x.status='CANCELED';x.evidence='Historical Aug30 debit16.33 unchanged. User confirms canceled Sep14; forward cost0.';}
  if(x.tool==='Howie'){x.monthly_equivalent=0;x.status='PAUSED / no charge';x.evidence=m.monthly_itemization.find(i=>i.item==='Howie').basis;}
  if(x.tool==='The Art Newspaper'){x.status='CANCELLATION EMAIL SENT / effective date unconfirmed';x.evidence='User Sep14 confirms email sent only; retain24 plus0.72 fee.';}
}
assert.ok(Math.abs(m.monthly_itemization.reduce((n,x)=>n+x.monthly,0)-m.normalized_monthly_burn_unrounded)<1e-8);
assert.ok(Math.abs(m.normalized_monthly_burn_unrounded-18647.516667)<1e-6);
assert.ok(Math.abs(m.halfpay_monthly_equivalent_unrounded-11246.573333)<1e-6);
const sheet='1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0';
const gog=args=>JSON.parse(cp.execFileSync('gog',[...args,'--json'],{encoding:'utf8',maxBuffer:8e6}));
const fetch=range=>gog(['sheets','get',sheet,range]);
const ranges={runway:"'Runway Forecast'!A1:Z",tech:"'Tech Stack Inventory'!A1:Z100"};
const before=Object.fromEntries(Object.entries(ranges).map(([k,r])=>[k,fetch(r)]));
write(prefix+'-prewrite.json',before);
const values=structuredClone(before.runway.values),tech=structuredClone(before.tech.values);
const set=(r,c,x)=>{while(values[r-1].length<c)values[r-1].push('');values[r-1][c-1]=String(x);};
const b=(r,x)=>set(r,2,x);
b(3,'Aug31 VERIFIED cash; Sep14 subscription v3 MODEL; no September feed');
for(const r of [7,25,30,78])b(r,m.normalized_monthly_burn);
for(const r of [8,31])b(r,m.normalized_runway_months_comparison);
for(const r of [9,32])b(r,m.timed.first_reserve_breach);
for(const r of [10,47])b(r,round(gap));
for(const r of [11,34])b(r,m.monthly_gap_to_target);
b(12,'August bank statements + v2 model + user-confirmed subscription changes Sep14');
b(13,vendorNote+' Prior office/postage, meals and one-off removals retained; historical actuals unchanged.');
set(41,1,'Other allowance:2798.12 to Sep13;1056.89 Sep14-Dec13;1091.89 Dec14 onward');b(41,m.timed.other_total);b(45,m.timed.total_outflows);
m.scenarios.forEach((s,i)=>[s.gross_monthly_cut,s.gross_monthly_remaining,s.employer_tax_savings_monthly,s.health_cash_savings,s.first_reduced_payment,s.reduced_payments].forEach((v,j)=>set(51+i,2+j,v)));
m.alternating_paychecks.forEach((a,i)=>[a.skipped_count,a.retained_count,a.savings,a.ending_cash,a.reserve_shortfall,a.first_reserve_breach].forEach((v,j)=>set(61+i,2+j,v)));
m.health_only.forEach((h,i)=>set(66+i,3,h.residual_gap));
set(77,1,'V2 bridge unverified allowances60; Howie35 removed in v3 total during pause');
set(78,1,'Rebuilt monthly base: v2 cuts plus DocSend16.33 canceled and Howie35 paused');
b(80,round(m.normalized_monthly_burn_unrounded-19635.76));b(81,m.halfpay_monthly_equivalent_unrounded);
for(let i=0;i<11;i++)set(83+i,1,m.assumptions[i]);
set(92,1,m.assumptions[9]+' '+m.halfpay_rounding_note);
b(94,m.alternating_paychecks.map(a=>`${a.first_skipped}: ${money(a.jan23_cash)} / ${money(a.jan23_reserve_shortfall)}`).join('; '));
b(95,m.monthly_gap_basis+' '+m.halfpay_rounding_note+' Newspaper24.72 retained. No actual payroll changes; parent owns task completion.');
const inventoryRows=[];
tech.forEach((r,i)=>{
  if(!['DocSend','Howie'].includes(r[0]))return;
  const howie=r[0]==='Howie';
  r[2]=howie?'No-charge pause Sep14-Dec13 assumed; UNVERIFIED35 allowance resumes Dec14 absent renewal cancellation; not confirmed actual billing':'User confirms canceled Sep14; no forward charge. Historical Aug30 debit16.33 unchanged';
  r[3]='0';r[4]='0';r[5]='0';r[6]=howie?'PAUSED / no charge':'CANCELED';r[8]=r[2];r[9]='0';r[10]='0';
  inventoryRows.push(i+1);
});
assert.equal(inventoryRows.length,2);
assert.ok(!tech.some(r=>/art newspaper/i.test(r[0]||'')));
// Group changed adjacent cells to bound writes without replacing unrelated live cells.
const plan=[];
for(const [tab,a,z,limit] of [['Runway Forecast',before.runway.values,values,95],['Tech Stack Inventory',before.tech.values,tech,tech.length]]){
  for(let i=0;i<limit;i++)for(let j=0;j<26;j++){
    if(String(a[i]?.[j]??'')===String(z[i]?.[j]??''))continue;
    const start=j,row=[];
    while(j<26&&String(a[i]?.[j]??'')!==String(z[i]?.[j]??'')){row.push(z[i][j]);j++;}
    plan.push({range:`'${tab}'!${String.fromCharCode(65+start)}${i+1}:${String.fromCharCode(64+j)}${i+1}`,values:[row]});j--;
  }
}
assert.ok(plan.length>0);
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
m.validation={live_cells_match:true,historical_rows_96_onward_preserved:true,historical_actuals_preserved:true,v2_and_prior_hashes_unchanged:true,original_hashes:originals,september_1_to_13_unchanged:true,itemization_reconciles:true,inventory_rows:inventoryRows,newspaper_row_not_added:true,payroll_unchanged:true,parent_owns_task_completion:true};
write(prefix+'-calculations.json',m);
const table=(heads,rows)=>'| '+heads.join(' | ')+' |\n| '+heads.map(()=>'---').join(' | ')+' |\n'+rows.map(r=>'| '+r.join(' | ')+' |').join('\n');
fs.writeFileSync(m.report_path,`---
schema_version: 1.1.0
date: 2026-09-14
type: budget-report
status: published
skill_origin: budget-manager
kay_approved: null
kay_approval_date: null
people: []
companies: []
projects: []
published_url: null
tags: [date/2026-09-14, output, output/budget-report, status/published]
---

# September 14 Subscription Update, Version 3

Source: [[operating-areas/c-suite/CFO/2026-09-14-budget-meals-cut-v2-report|V2 report]]. V3 [[operating-areas/c-suite/CFO/2026-09-14-budget-subscriptions-v3-calculations.json|model]] and [[operating-areas/c-suite/CFO/2026-09-14-budget-subscriptions-v3-cash-ledger.json|dated ledger]]. User confirmation only; no email search or new bank feed.

## Subscription Changes

${vendorNote}

Monthly burn during pause: **${money(m.normalized_monthly_burn_unrounded)}**; hypothetical half-pay equivalent **${money(m.halfpay_monthly_equivalent_unrounded)}**. From December14: **${money(m.after_pause.full_monthly_unrounded)}** / **${money(m.after_pause.halfpay_monthly_unrounded)}** with the unverified35 allowance reinstated. No actual payroll changes. Incremental modeled savings: September ${money(septemberSavings)}; through February7 ${money(savings)}. Calendar-day proration; September1-13 unchanged.

## Current Itemization

${table(['Item','Monthly during pause','Basis'],m.monthly_itemization.map(x=>[x.item,money(x.monthly),x.basis]))}

## Dated Forecast

August31 verified cash ${money(m.cash.total)}; protected DD reserve ${money(m.cash.dd_reserve)}. Outflows through February7 ${money(outflows)}; modeled ending cash ${money(cash)}; reserve funding gap **${money(gap)}**. First reserve breach **${m.timed.first_reserve_breach}**. Additional monthly savings required from September14 **${money(m.monthly_gap_to_target)}**. Normalized comparison **${m.normalized_runway_months_comparison} months** uses August31 operations cash, not a verified September14 balance or dated exhaustion estimate.

${table(['First skipped paycheck','Feb7 cash','DD gap','Jan23 cash','Jan23 gap','First breach'],m.alternating_paychecks.map(a=>[a.first_skipped,money(a.ending_cash),money(a.reserve_shortfall),money(a.jan23_cash),money(a.jan23_reserve_shortfall),a.first_reserve_breach]))}

${table(['Hypothetical scenario','Effective','Gross monthly cut','Gross remaining','Employer tax savings/mo','Health cash savings'],m.scenarios.map(s=>[s.label,s.effective,money(s.gross_monthly_cut),money(s.gross_monthly_remaining),money(s.employer_tax_savings_monthly),money(s.health_cash_savings)]))}

Health-only residual gaps: ${m.health_only.map(h=>money(h.residual_gap)).join('; ')} (October then January). Fixed Gusto service fee106.90, bookkeeping247 and bank fees3.81 retained; newspaper0.72 bank fee included once. All payroll and healthcare alternatives remain hypothetical.

## Assumptions

${m.assumptions.map(s=>'- '+s).join('\n')}

## Verification

[[operating-areas/c-suite/CFO/2026-09-14-budget-subscriptions-v3-prewrite.json|Live rollback snapshot]] and [[operating-areas/c-suite/CFO/2026-09-14-budget-subscriptions-v3-postverify.json|Live read-back]] saved. All intended values match; dashboard writes bounded to current rows1:95 and the existing two inventory rows. Historical rows96 onward and historical burn actuals unchanged. V2 and prior artifacts hash-verified unchanged. Newspaper inventory row not added. No email, Slack, actual payroll changes, task completion or commits; parent owns completion.
`);
assert.ok(fs.statSync(m.report_path).size>1000);
console.log(JSON.stringify({status:m.status,full:m.normalized_monthly_burn_unrounded,half:m.halfpay_monthly_equivalent_unrounded,after_pause:m.after_pause,savings:round(savings),gap:round(gap),outflows:round(outflows),monthly_gap:m.monthly_gap_to_target,breach:m.timed.first_reserve_breach,runway:m.normalized_runway_months_comparison,report:m.report_path,write_ranges:plan.length},null,2));
