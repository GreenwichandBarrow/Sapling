const fs = require('fs');
const cp = require('child_process');
const path = require('path');
const root = '/home/ubuntu/projects/Sapling';
const out = __dirname;
const sheet = '1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0';
const round = n => Math.round((n + Number.EPSILON) * 100) / 100;
const money = n => '$' + round(n).toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2});
const write = (p, data) => fs.writeFileSync(p, typeof data === 'string' ? data : JSON.stringify(data,null,2)+'\n');
const dates = [];
for (let d = new Date('2026-09-01T00:00:00Z'); d <= new Date('2027-02-07T00:00:00Z'); d.setUTCDate(d.getUTCDate()+1)) dates.push(d.toISOString().slice(0,10));
const payroll = dates.filter(d => new Date(d).getUTCDay() === 2);
const insurance = dates.filter(d => new Date(d).getUTCDay() === 1);
const healthDates = ['2026-09-05','2026-10-05','2026-11-05','2026-12-05','2027-01-05','2027-02-05'];
const salary = 3173.08, tax = 242.74, factor = 1 + tax/salary;
const other = 2798.12;
const monthly = (salary+tax)*52/12 + 2750 + 8.94*52/12 + other;
const cash = 97777.71, reserve = 38000;
const horizon = payroll.length*(salary+tax)+insurance.length*8.94+6*2750+other*5.25+3220+1300+348;
const gap = horizon + reserve - cash;
const scenarios = [];
for (const [effective, first] of [['2026-09-14','2026-09-15'],['2026-10-01','2026-10-06']]) {
  const n = payroll.filter(d => d>=first).length;
  for (const [label, h, count] of [['Salary only',0,0],['Combined: health reduced $1000 from January',1000,2],['Combined: health reduced $2750 from January (upper bound)',2750,2],['Combined: health reduced $1000 from October',1000,5]]) {
    const needed = gap-h*count;
    const weeklyCut = Math.ceil(needed/n/factor*100)/100;
    scenarios.push({label,effective,first_reduced_payment:first,reduced_payments:n,health_monthly_reduction:h,health_payments_reduced:count,health_cash_savings:h*count,
      gross_monthly_cut_exact:needed/n/factor*52/12,gross_monthly_cut:round(needed/n/factor*52/12),
      gross_monthly_remaining:round(salary*52/12-needed/n/factor*52/12),gross_cut_percent:round(needed/n/factor/salary*100),
      weekly_cut_rounded_up:weeklyCut,weekly_gross_remaining:round(salary-weeklyCut),
      gross_monthly_cut_no_employer_tax_savings:round(needed/n*52/12),
      employer_tax_savings_monthly:round(needed/n/factor*52/12*(factor-1)),
      projected_bank_at_target_with_unrounded_cut:reserve});
  }
}
const ledger = [];
let balance = cash;
for (const d of dates) {
  const date = new Date(d), daysInMonth = new Date(Date.UTC(date.getUTCFullYear(),date.getUTCMonth()+1,0)).getUTCDate();
  const recurring = other/daysInMonth;
  const pay = payroll.includes(d)?salary+tax:0;
  const ins = insurance.includes(d)?8.94:0;
  const health = healthDates.includes(d)?2750:0;
  const deals = d==='2026-09-28'?3220:0;
  const conference = d==='2026-10-01'?1300:0;
  const website = d==='2026-11-11'?348:0;
  balance -= recurring+pay+ins+health+deals+conference+website;
  ledger.push({date:d,other_allowance:recurring,payroll:pay,insurance:ins,health,dealsx:deals,conference,website,end_cash:balance});
}
const alternating = ['2026-09-15','2026-09-22','2026-10-06'].map(first => {
  const skipped = payroll.filter(d=>d>=first).filter((d,i)=>i%2===0);
  let running = cash, breach = null;
  for (const day of ledger) {
    running -= day.other_allowance + day.payroll + day.insurance + day.health + day.dealsx + day.conference + day.website;
    if (skipped.includes(day.date)) running += salary+tax;
    if (breach===null && running<reserve) breach=day.date;
  }
  return {first_skipped:first,skipped_dates:skipped,skipped_count:skipped.length,retained_count:payroll.length-skipped.length,savings:round(skipped.length*(salary+tax)),ending_cash:round(running),reserve_shortfall:round(reserve-running),first_reserve_breach:breach};
});
const model = {
  status:'calculated; dashboard write pending',run_date:'2026-09-12',bank_anchor_date:'2026-08-31',target_date:'2027-02-07',target_inclusive:true,
  cash:{checking:6902.49,savings:90875.22,total:cash,dd_reserve:reserve,operations_before_commitments:cash-reserve,operations_after_dealsx_conference:cash-reserve-4520,operations_after_website:cash-reserve-4868},
  historical:{august_gross_expenses:21669.33,august_interest:243.82,august_net_burn:21425.51,august_ingested:'2026-09-11',january_august_net_burn:219227.19,annual_accounting_actual:3200},
  payroll:{weekly_gross:salary,weekly_net:2319.28,weekly_bank_tax:1096.54,weekly_employee_withholding:853.80,weekly_employer_tax:tax,weekly_employer_total:salary+tax,annual_gross:round(salary*52),monthly_gross:round(salary*52/12),monthly_employer_tax:round(tax*52/12),monthly_total:round((salary+tax)*52/12),incremental_savings_factor:factor},
  normalized_bridge:[['August gross expenses',21669.33],['Remove rent paid in August; lease canceled September',-2000],['Remove Linkt',-199.99],['Remove Apollo / ZenLeads same vendor',-64.24],['Remove prepaid annual New Yorker',-209],['Replace four payroll runs with 52/12 average',round((salary+tax)*52/12-13663.28)],['Replace five weekly insurance charges with 52/12 average',round(8.94*52/12-44.70)],['Unverified recurring vendor allowances: Howie35, Voice10, Slack15',60]],
  normalized_monthly_burn:round(monthly),normalized_other_monthly_allowance:other,normalized_interest:0,
  timed:{payroll_dates:payroll,payroll_count:payroll.length,payroll_total:round(payroll.length*(salary+tax)),insurance_dates:insurance,insurance_count:insurance.length,insurance_total:round(insurance.length*8.94),health_dates:healthDates,health_total:16500,other_month_equivalents:5.25,other_total:round(other*5.25),dealsx_unpaid:3220,conference:1300,website_renewal_pretax:348,total_outflows:round(horizon),shortfall_to_protected_reserve:round(gap),unfunded_end_cash:round(cash-horizon),first_reserve_breach:ledger.find(x=>x.end_cash<reserve).date,projected_sep12_opening_cash_not_bank_fact:round(ledger.find(x=>x.date==='2026-09-11').end_cash)},
  scenarios, alternating_paychecks:alternating,
  health_only:[{effective:'2026-10-01',payments:5,maximum_monthly_reduction:2750,total_maximum:13750,residual_gap:round(gap-13750)},{effective:'2027-01-01',payments:2,maximum_monthly_reduction:2750,total_maximum:5500,residual_gap:round(gap-5500)}],
  assumptions:['Cash forecast starts September 1 from August 31 bank anchor; no actual September feed. Elapsed September is included once, never restarted at September 12.', 'Tuesday payroll cadence inferred from August; September 14 effective date assumes payroll cutoff permits September 15 payment reduction. October 1 effective date modeled as first reduced payment October 6. Earned-wage/pay-period limits and payroll approval not verified.', 'Monday business insurance and day-5 health cadence inferred from August; timing not verified beyond August. February health is a full cash payment, not 7/28.', 'Other expenses prorated by calendar days; August variable spending retained as allowance, not a claim every charge recurs. Includes supplies407.42 postage170.40 travel1194.83 and other217.75.', 'DealsX3220 paid once on assumed September28; only August/September reduction approved. No October recurring charge is a planning assumption pending pause confirmation, supported by user-reported tracker row364 due September28.', 'Conference1300 placed October1; planned unbooked. Website348 expected November11 from prior renewal date and July2026 price notice; tax unknown and not added.', 'Attio prepaid through March26 2027; Canva April120 and 1Password May52.13 treated annual prepaid through horizon; Canva term should be verified. New Yorker209 annual renewal confirmed August6.', 'Howie35 Voice10 Slack15 per month are uncertainty allowances, not verified August charges. Google Voice may overlap Workspace. No further optional vendor research.', 'No future interest assumed. No deposit2000 or uncertain1500; no nonprofit salary income. Annual accounting3200 historical, not recurring; no future filing due date confirmed.', 'Employer-tax savings factor derives from observed payroll, not a payroll-engine quote. January tax resets and fixed payroll fees may differ. Gusto106.90 monthly fee retained unchanged.', 'Healthcare scenarios are hypothetical premium/reimbursement reductions, not current savings or elections. Reduced reimbursement alone shifts cost to household; only lower actual premium is household savings. January scenarios include Jan5 and Feb5 cash payments.'],
  sources:{checking:'https://drive.google.com/file/d/1URb7XRndQaJKNmmWHlOL5SSLq3CnYiW-/view',savings:'https://drive.google.com/file/d/1zA85LZixlc90k2BHX3nKNYdZ2Eu8nBx4/view',monthly_pl:'https://drive.google.com/file/d/18Nu16iBzgO01eDqeLKeE8N5ps2eUM22R/view',ytd_pl:'https://drive.google.com/file/d/1dCZBI4nFvzGEUOAxQT19KWM95c9bpsZl/view',balance_sheet:'https://drive.google.com/file/d/1H13RNVROBNNIOwNBJZ-3PHHdqB77CYKQ/view',dashboard:`https://docs.google.com/spreadsheets/d/${sheet}/edit`,claude_receipt:'https://mail.google.com/mail/u/0/#all/1a04432048f698da',attio_receipt:'https://mail.google.com/mail/u/0/#all/19d27f7678cc6473',howie_receipt:'https://mail.google.com/mail/u/0/#all/19c9ac4e0f48b895',squarespace_notice:'https://mail.google.com/mail/u/0/#all/19f698937aad858a',new_yorker:'https://mail.google.com/mail/u/0/#all/19f20f79f34be6aa'}
};
if (Math.abs(ledger.at(-1).end_cash-(cash-horizon))>0.001) throw Error('Ledger mismatch');
write(path.join(out,'2026-09-12-budget-followup-calculations.json'),model);
write(path.join(out,'2026-09-12-budget-followup-cash-ledger.json'),ledger);
console.log(JSON.stringify({artifact:path.join(out,'2026-09-12-budget-followup-calculations.json'),burn:model.normalized_monthly_burn,gap:model.timed.shortfall_to_protected_reserve,breach:model.timed.first_reserve_breach,scenarios},null,2));
if (!process.argv.includes('--publish')) process.exit(0);

const gog = args => JSON.parse(cp.execFileSync('gog',args.concat('--json'),{encoding:'utf8',maxBuffer:8e6}));
const fetch = range => gog(['sheets','get',sheet,range]);
const ranges = ["'Runway Forecast'!A1:K230","'Tech Stack Inventory'!A1:K40","'Monthly Actuals vs Budget'!A1:X55"];
const resuming = process.argv.includes('--resume');
const snapPath=resuming ? path.join(root,'brain/context/rollback-snapshots/budget-dashboard-2026-09-12-followup-1789258045643.json') : path.join(root,'brain/context/rollback-snapshots/budget-dashboard-2026-09-12-followup-'+Date.now()+'.json');
const snapshot = resuming ? JSON.parse(fs.readFileSync(snapPath,'utf8')) : {at:new Date().toISOString(),sheet,ranges:{}};
if(!resuming){for (const range of ranges) snapshot.ranges[range] = fetch(range);write(snapPath,snapshot);}
const actuals=snapshot.ranges[ranges[2]].values;
if (actuals[0][18]!=='August 2026'||Number(actuals[38][18])!==cash||Number(actuals[36][18])!==21425.51) throw Error('August live actuals mismatch; no writes');
const tech = snapshot.ranges[ranges[1]].values;
const findings = {
 'Linkt':[0,199.99,'CUT CANDIDATE / canceled but charged','Aug01 LINKT AI199.99. Canceled per user; no refund observed. Forward0 conditional on stop; no September feed.'],
 'Claude Code':[21.78,21.78,'KEEP / billed amount verified','Aug27 receipt2224-1411-2756: monthly Pro20 + NY tax1.78 =21.78. Advertised17 not this monthly bill; no annual switch assumed.'],
 'Attio CRM':[839.20/12,0,'KEEP / prepaid annual','Mar26 paid839.20:828 annual less57.21 unused-time credit +68.41 tax; covers through Mar26 2027. Full uncredited renewal at same tax would901.49. No cash renewal before target.'],
 'SquareSpace':[348/12,0,'KEEP / renewal allowance','No August debit. July16 price notice348 annual, next renewal after Aug12. Prior Nov11 renewal implies Nov11 2026; include348 once, tax unverified.'],
 'QuickBooks':[41.37,41.37,'KEEP','Aug03 Intuit/QBooks41.37; retain with bookkeeping.'],
 'Superhuman':[0,0,'KEEP CANCELED','No August debit; May22 cancellation recorded in prior inventory. No September feed; zero forecast, not current vendor confirmation.'],
 'Howie':[35,0,'EVALUATE / unverified ongoing','No August debit. Feb26 3030 Labs receipt35 monthly Feb26-Mar26, disproves unsupported25/month or120/year. Reserve35/month pending current billing verification.'],
 'Google Workspace':[28.08,28.08,'KEEP','Aug01 GOOGLE SVCS28.08, replaces28.85.'],
 'Google One':[2.16,2.16,'EVALUATE / possible overlap','Aug17 Google One2.16; separate debit. Retain until storage need verified.'],
 'Google Voice':[10,0,'EVALUATE / allowance only','No separate August debit or renewal receipt verified. Retain10/month uncertainty allowance; may overlap Workspace.'],
 'ChatGPT / OpenAI':[217.75,217.75,'CUT CANDIDATE / hypothetical downgrade','Aug08 billed217.75; repeated elevated charge. Retained in base. Potential195.97/month only if reduced to21.78 all-in; no plan change made.'],
 'Canva':[10,0,'KEEP / assumed annual prepaid','No August debit; Apr23 invoice120 paid. Annual cadence per prior inventory, term not stated in email; treated prepaid through target, renewal timing uncertain.'],
 'Slack':[15,0,'EVALUATE / allowance only','No August debit or current invoice verified. Retain15/month uncertainty allowance, not verified annual billing.'],
 'Granola':[15.24,15.24,'KEEP','Aug15 billed15.24; workflow uses meeting notes.'],
 'GitHub':[0,0,'KEEP / free per inventory','No August debit; free-tier assumption retained.'],
 'Cursor':[0,0,'KEEP / free per inventory','No August debit; free-tier assumption retained.'],
 'Apollo':[0,64.24,'KEEP CANCELED / September unverified','Aug02 APOLLO.IO64.24. Apollo and ZenLeads are same vendor; count once. Canceled per user in September. Forward0; no September feed.'],
 'Hetzner':[15.03,15.03,'KEEP','Aug14 debit14.59 + foreign fee0.44 =15.03. Fee already in bank-fee bridge; no duplicate addition.'],
 'Tailscale':[8.71,8.71,'KEEP','Aug22 billed8.71.'],
 '1Password':[52.13/12,0,'KEEP / prepaid annual','No August debit; prior May statement evidence52.13 annual. No renewal assumed before target; monthly equivalent is not future cash.'],
 'DealsX / KeyReach':[0,0,'PAUSE ASSUMPTION / pending confirmation','UNPAID July1520 + August/September combined1700 =3220. Reduction approved only Aug/Sep. No recurring after September is assumption from prior pause and user-reported row364 dueSep28, NOT vendor-confirmed.'],
 'AI Consultant / Dodo Digital':[0,0,'KEEP STOPPED','No August Dodo debit; user confirms1000/month removed July onward. Do not subtract again from August base.'],
 'DocSend':[16.33,16.33,'KEEP / bill above advertised','Aug30 billed16.33 versus Personal15 pretax. Prior15.59 stale. Use16.33 cash; invoice tax breakdown unverified.'],
 'BizBuySell':[0,0,'KEEP FREE','No August debit; June20 free downgrade per prior inventory. No September verification.']
};
const rows=[['Tool','Category','Billing Evidence','Planning Monthly Equivalent','August Cash Debit','Potential NEW Savings/Mo','Status','Cash Timing / Assumptions','Source / Notes','Annualized Equivalent','Forecast Basis']];
const audit=[];
for (const r of tech.slice(1)) {
  if (!r[0] || r[0]==='TOTAL COSTS') continue;
  const f=findings[r[0]];
  if(!f) throw Error('Unmapped inventory row '+r[0]);
  const saving=r[0]==='ChatGPT / OpenAI'?195.97:0;
  rows.push([r[0],r[1],f[3],round(f[0]),f[1],saving,f[2],'Monthly equivalents are NOT all future cash debits','August statement + cited receipts / user corrections',round(f[0]*12),'See runway cash bridge']);
  audit.push({tool:r[0],monthly_equivalent:round(f[0]),august_debit:f[1],status:f[2],evidence:f[3]});
}
const additions=[['StartVirtual VA',0,0,'KEEP STOPPED','VA1040/month removed July onward; zero August outsourcing. Separate from active bookkeeping.'],['StartVirtual bookkeeping',247,247,'KEEP','Aug02 SVTRUEBOOKKEEPING247. Not the canceled VA.'],['Gusto payroll service',106.90,106.90,'KEEP','Aug04 service fee106.90. Fixed fee retained; do not reduce with wages.'],['New Yorker',209/12,209,'KEEP / prepaid annual','Aug06 annual209; July1 renewal email confirms one-year term. No repeat before target.'],['The Art Newspaper',24.72,24.72,'EVALUATE','Aug01 charge24 plus foreign fee0.72. Retained recurring allowance; cadence unverified.']];
for(const [tool,cost,paid,status,evidence] of additions){rows.push([tool,'Additional bank vendor',evidence,round(cost),paid,0,status,'Already included in bridge or removed as prepaid; never add twice','August checking',round(cost*12),'See runway bridge']);audit.push({tool,monthly_equivalent:round(cost),august_debit:paid,status,evidence});}
rows.push(['TOTAL PLANNING EQUIVALENTS','','Not a cash-runway subtotal',round(rows.slice(1).reduce((s,r)=>s+r[3],0)),round(rows.slice(1).reduce((s,r)=>s+r[4],0)),195.97,'Updated 2026-09-12','Annual/prepaid and uncertainty allowances explicitly separated','Potential new savings2351.64/year, hypothetical; canceled savings already reflected',round(rows.slice(1).reduce((s,r)=>s+r[9],0)),'DO NOT add this total to August bridge']);
const runway=[['Budget Dashboard','Greenwich & Barrow'],['Last Updated','2026-09-12'],['As of','Aug31 VERIFIED cash; Sep12 MODEL update, no September feed'],['Fund Balance',cash],['DD Reserve',reserve],['Available for Operations',cash-reserve],['Steady-State Monthly Burn',round(monthly)],['Months at Steady-State (from September 1)',round((cash-reserve)/monthly)],['Projected Reserve Threshold (cash-timed)',model.timed.first_reserve_breach],['Shortfall to Feb 7 2027 (cash-timed)',round(gap)],['Monthly Gross Salary Cut: Sep14 effective',scenarios[0].gross_monthly_cut],['Dashboard Source','August bank statements + Friday close + user Sep12 corrections'],['Notes','No payroll or health changes. No future interest/deposit/nonprofit income. Cash-timed ledger governs; monthly equivalent is comparison only.'],[],['BURN RATE']];
for(const r of snapshot.ranges[ranges[0]].values.slice(15,24))runway.push(r.slice(0,2));
runway.push(['Steady-State Monthly Burn',round(monthly)],[],['INVESTOR REPORTING'],['budget_remaining',cash],['budget_pct',round(cash/551825*100)],['burn_rate',round(monthly)],['runway_months',round((cash-reserve)/monthly)],['projected_reserve_threshold',model.timed.first_reserve_breach],['target_cash_date','2027-02-07'],['salary_cut_sep14_gross_monthly',scenarios[0].gross_monthly_cut],[],['CASH-TIMED MODEL','Amount / Count'],['Payroll payments Sep1-Feb2',23],['Payroll total',model.timed.payroll_total],['Health full payments Sep5-Feb5',16500],['Weekly insurance22 payments',model.timed.insurance_total],['Other operating allowance5.25 months',model.timed.other_total],['DealsX unpaid ONCE',3220],['October conference unbooked',1300],['Website expected November renewal pretax',348],['Total modeled outflows',round(horizon)],['Target DD reserve',38000],['Cash funding gap',round(gap)],['Projected Sep12 opening NOT BANK FACT',model.timed.projected_sep12_opening_cash_not_bank_fact],[],['HYPOTHETICAL SCENARIOS','Gross monthly cut','Gross remaining','Employer tax saving/mo','Health cash savings','First reduced payment','Payroll runs']);
for(const s of scenarios)runway.push([s.label+' / '+s.effective,s.gross_monthly_cut,s.gross_monthly_remaining,s.employer_tax_savings_monthly,s.health_cash_savings,s.first_reduced_payment,s.reduced_payments]);
runway.push([],['ALTERNATING WEEKLY PAYCHECKS; monthly healthcare unchanged','Skipped','Retained incl elapsed Sep','Cash saved','Feb7 cash','Gap to38000 DD','First DD breach']);
for(const a of alternating)runway.push([a.first_skipped,a.skipped_count,a.retained_count,a.savings,a.ending_cash,a.reserve_shortfall,a.first_reserve_breach]);
runway.push([],['HEALTH ONLY','Max cash savings','Remaining gap'],['October1:2750 reduction x5',13750,round(gap-13750)],['January1:2750 reduction x2',5500,round(gap-5500)],[],['NORMALIZED BRIDGE','Monthly change']);
for(const b of model.normalized_bridge)runway.push(b);
runway.push(['Rebuilt monthly baseline',round(monthly)],['Old unvalidated forward figure superseded',19635.76],['Difference to old figure',round(monthly-19635.76)],[],['ASSUMPTIONS / LIMITATIONS']);
for(const a of model.assumptions)runway.push([a]);
runway.push(['Monday tasks user-reported','Existing rows365/366: book October conference; contact NY health broker. No tracker read or write in this audit.'],['Bead limitation','Creation attempted; repository has no active database. No task infrastructure changes.']);
runway.push([],['PRIOR PLANNING CONTEXT - SUPERSEDED BY SEPTEMBER 12 MODEL'],...snapshot.ranges[ranges[0]].values.slice(35));
runway[8][0]='Projected Zero';
runway[9][0]='Shortfall to Feb 2027';
runway[10]=['Monthly Savings Needed',round(gap/5.25)];
runway[31][0]='projected_zero';
runway[33]=['monthly_gap_to_target',round(gap/5.25)];
if(runway.length>230)throw Error('Runway exceeds bounded write');
const padded=(arr,n,w)=>Array.from({length:n},(_,i)=>Array.from({length:w},(_,j)=>arr[i]?.[j]??''));
const techPlan=[tech[0]];
for(const original of tech.slice(1)) {
  if(!original[0] || original[0]==='TOTAL COSTS')continue;
  const r=rows.find(r=>r[0]===original[0]);
  techPlan.push([r[0],original[1],r[2],r[3],r[3],r[5],r[6],original[7]||'', 'August cash '+money(r[4])+'. Prepaid allocations and unverified allowances are not future monthly cash debits; see runway report.',r[9],r[9]]);
}
const techTotal=round(techPlan.slice(1).reduce((s,r)=>s+r[3],0));
techPlan.push(['TOTAL COSTS','','Planning equivalents; includes prepaid allocations',techTotal,techTotal,195.97,'Updated 2026-09-12','', 'New savings are hypothetical; canceled savings already reflected.',round(techTotal*12),round(techTotal*12)]);
const plans=[{range:"'Runway Forecast'!A1:K230",values:padded(runway,230,11)},{range:"'Tech Stack Inventory'!A1:K40",values:padded(techPlan,40,11)},{range:"'Monthly Actuals vs Budget'!B32:C32",values:[['DD Reserve (held cash; Sep12 policy)',38000]]}];
write(path.join(out,'2026-09-12-budget-followup-write-plan.json'),plans);
const receipt=[];
for(const plan of plans){
  if(!plan.values.length)throw Error('Empty write');
  // Re-fetch immediately before each bounded write and preserve a rollback copy.
  receipt.push({range:plan.range,before:fetch(plan.range)});
  write(path.join(out,'2026-09-12-budget-followup-prewrite.json'),receipt);
  gog(['sheets','update',sheet,plan.range,'--values-json',JSON.stringify(plan.values),'--input','RAW']);
}
const checks=[];
for(const plan of plans){const live=fetch(plan.range);for(let i=0;i<plan.values.length;i++)for(let j=0;j<plan.values[i].length;j++){const expected=plan.values[i][j],got=live.values?.[i]?.[j]??'';const matches=typeof expected==='number' ? got!=='' && Math.abs(Number(got)-expected)<0.00001 : String(got)===String(expected);if(!matches)throw Error(`Post-write mismatch ${plan.range} ${i},${j}`);}checks.push({range:plan.range,verified:true,live});}
const after=fetch(ranges[2]).values;
for(let i=0;i<actuals.length;i++)for(let j=0;j<actuals[i].length;j++){if(i===31&&(j===1||j===2))continue;if(String(actuals[i][j]??'')!==String(after[i]?.[j]??''))throw Error('Historical actuals changed');}
write(path.join(out,'2026-09-12-budget-followup-postverify.json'),checks);
model.status='dashboard written and live verified';model.rollback_snapshot=snapPath;model.inventory_audit=audit;model.validation={live_cells_match:true,august_actuals_and_ytd_preserved:true,inventory_original_rows_audited:24,additional_vendors:5,no_email:true,no_slack:true,no_payroll_or_health_change:true};
write(path.join(out,'2026-09-12-budget-followup-calculations.json'),model);
const reportPath=path.join(root,'brain/outputs/2026-09-12-budget-runway-followup-aug-2026.md');
const scenarioTable=scenarios.map(s=>`| ${s.label}; ${s.effective} | ${s.first_reduced_payment}; ${s.reduced_payments} | ${money(s.gross_monthly_cut)} | ${money(s.gross_monthly_remaining)} | ${money(s.employer_tax_savings_monthly)} | ${money(s.health_cash_savings)} |`).join('\n');
const vendorTable=audit.map(a=>`| ${a.tool} | ${money(a.august_debit)} | ${money(a.monthly_equivalent)} | ${a.status}: ${a.evidence} |`).join('\n');
const report=`---
schema_version: 1.1.0
date: 2026-09-12
type: budget-report
status: review
skill_origin: budget-manager
kay_approved: null
people: []
companies: ["[[entities/greenwich-and-barrow]]", "[[entities/live-oak-bank]]", "[[entities/startvirtual]]", "[[entities/dealsx]]", "[[entities/dodo-digital]]", "[[entities/squarespace]]", "[[entities/superhuman]]", "[[entities/bizbuysell]]"]
projects: []
tags: [date/2026-09-12, output, output/budget-report, status/review, topic/budget, topic/runway, company/greenwich-and-barrow, company/live-oak-bank, company/startvirtual, company/dealsx, company/dodo-digital, company/squarespace, company/superhuman, company/bizbuysell]
---

# August Bank Audit and February 7 Runway

For [[entities/greenwich-and-barrow|Greenwich & Barrow]]. Supersedes forward assumptions, not historical actuals, in [[outputs/2026-09-11-budget-report-aug-2026|Friday's August report]]. [[context/budget|Current reserve policy]] is now **$38,000**, explicitly authorized September 12; LOI remains under negotiation. No payroll or healthcare election has been changed. No email, Slack, or personal tracker writes.

## Fund Position

[[entities/live-oak-bank|Live Oak]] August statements reconcile exactly: checking **$6,902.49** + savings **$90,875.22** = **$97,777.71 at August 31**. This is the newest bank evidence found in BOOKKEEPING/CHECKING and BOOKKEEPING/SAVINGS, not a live September balance. July31 combined cash119203.22 less August net burn21425.51 equals97777.71. Savings transferred25000 to checking; checking has an additional offsetting2000 credit/debit pair on Aug19, not a deposit refund. Checking debits23669.33 less offsetting transfer2000 =21669.33 expenses; savings interest243.82 yields21425.51 net burn.

Cash above DD is59777.71; after **unpaid [[entities/dealsx|DealsX]]3220** and conference1300,55257.71 remains; after expected website348 renewal,54909.71 remains. DealsX is July1520 plus August/September combined1700, not1600. Count the payable once because no August payment appears and user confirms it remains unpaid. Only August/September pricing reduction is approved. Zero recurring October onward is a **planning assumption**, supported by the prior pause and user-reported row364 dueSep28, not vendor confirmation.

Requested2000 deposit is unreceived and excluded. Possible1500 is uncertain and excluded. Nonprofit has no revenue; personally funded nonprofit salary is circular and excluded. No future interest credited in base. Historical source capital551845.01 differs from approved551825 by20.01; forecast uses bank cash and does not manufacture capital.

## Monthly P&L Summary

Friday's full monthly pipeline was already complete: source PDFs parsed, August columnS present, YTD columnsU:X populated, bottom cash/burn rows correct, August burn row in runway present. Live verification preserved all historical cells. August gross expenses21669.33, interest243.82, net burn21425.51; January-August net burn219227.19. Historical annual accounting actual is **3200**, not approximate3000. It is not recurring; August active bookkeeping247 is distinct from canceled VA1040.

## Variance Flags

Existing approved-category YTD overspends remain: payroll taxes/benefits666.50%, travel177.32%, office/bookkeeping66.86%, marketing/software/research62.45%. No investor-approved annual budget was rewritten. Only operational held-cash reserve label/value was changed. Prior normalized24523.38 is historical, not the new forward model; prior19635.76 was unvalidated and is superseded.

## Runway Analysis

### Payroll Evidence

Four August runs: gross12692.32/4 =3173.08 weekly; employer tax970.96/4 =242.74. March/June five-run totals15865.40 and1213.70 corroborate this. Bank GUSTO NET2319.28 + GUSTO TAX1096.54 =3415.82 employer cost. Employee withholding3173.08-2319.28=853.80; employer portion1096.54-853.80=242.74. **Never add all GUSTO TAX to gross salary.**

Gross annual165000.16, monthly13750.01; employer tax annual12622.48, monthly1051.87; combined monthly14801.89 (unrounded14801.886667). Gusto fee106.90 remains separately in operating costs. Incremental employer savings factor **1 +242.74/3173.08 = ${factor.toFixed(9)}** is an evidence-based proportional assumption, not verified marginal payroll-engine output. January tax resets, fixed fees and pay-period cutoffs can change savings.

### Normalized Monthly Bridge

| Step | Monthly amount/change |
|---|---:|
${model.normalized_bridge.map(([label,n])=>`| ${label} | ${money(n)} |`).join('\n')}
| **Rebuilt monthly baseline before interest** | **${money(monthly)}** |

This is753.0 higher than the old19635.76 (exact difference${money(monthly-19635.76)}). Composition: employer payroll14801.89 + health2750 + weekly insurance38.74 + other operating allowance2798.12. Other allowance is August nonpayroll spending, less rent/canceled vendors/prepaid New Yorker, plus60 uncertainty allowances. It retains supplies407.42, postage170.40, travel1194.83, other expenses217.75, bookkeeping247, fixed payroll fee106.90 and observed software. Variable spending is a conservative allowance, not an assertion furniture, repairs, or medical purchases recur. No new travel cut imposed. Canceled VA1040 and AI consultant1000 already zero in August, so no second subtraction. Annual accounting3200 already absent from August, so no second subtraction. Annual prepaid tools are not added again. Website renewal is a one-time cash item rather than29/month in the cash model.

### Cash-Timed Bridge Through February 7 Inclusive

| Component | Calculation | Cash outflow |
|---|---|---:|
| Payroll | 23 Tuesday payments Sep1-Feb2 x3415.82 | ${money(model.timed.payroll_total)} |
| Health | 6 full payments Sep5-Feb5 x2750 | $16,500.00 |
| Business insurance | 22 Mondays Sep7-Feb1 x8.94 | ${money(model.timed.insurance_total)} |
| Other operating allowance | 2798.12 x(5 +7/28 months) | ${money(model.timed.other_total)} |
| DealsX unpaid | July1520 +Aug/Sep1700, once | $3,220.00 |
| October conference | Planned, unbooked | $1,300.00 |
| Website renewal | Expected Nov11, quoted pretax348 | $348.00 |
| **Total** | | **${money(horizon)}** |
| **Funding gap protecting DD** | total +38000 -97777.71 | **${money(gap)}** |

Do not substitute20388.75 x5.25 for this dated model: payroll counts differ from52/12; February health is paid in full; one-time commitments have separate dates. The model includes elapsed September once. September12 opening **modeled** cash is${money(model.timed.projected_sep12_opening_cash_not_bank_fact)}, never presented as bank-confirmed. Base first crosses DD on **${model.timed.first_reserve_breach}**. Negative unfunded February ending cash${money(cash-horizon)} is mathematical shortfall, not a forecast that the account can actually overdraft.

### Hypothetical Cuts

| Scenario/effective date | First reduced pay; count | Gross salary cut/mo | Remaining gross salary/mo | Employer tax savings/mo | Health savings through target |
|---|---|---:|---:|---:|---:|
${scenarioTable}

Formula: **gross weekly cut = (55040.96 - total healthcare cash savings) / (remaining reduced checks x1.076499805)**; monthly equivalent =weekly cut x52/12. These are minimum arithmetic cuts with no contingency. Calculations JSON gives exact unrounded results and weekly cuts rounded upward to cents. September14 is only feasible if payroll cutoff and earned-wage treatment permit September15 reduction; otherwise use next actual payroll date. October1 scenario assumes October6 first reduced cash payment. No implementation authorized.

With **no incremental employer-tax savings**, salary-only gross monthly cut rises to${money(scenarios[0].gross_monthly_cut_no_employer_tax_savings)} for September14 or${money(scenarios[4].gross_monthly_cut_no_employer_tax_savings)} for October1. This sensitivity avoids treating the observed rate as guaranteed savings.

**Health-only is insufficient:** even eliminating all2750 from October yields13750 across five payments, leaving${money(gap-13750)} gap. If delayed until January, two payments save at most5500, leaving${money(gap-5500)}. Zero premium is only an upper-bound arithmetic test, not a feasible plan. The1000/month scenarios are illustrative, not a broker quote. January benefit starts only if a new premium/election actually takes effect and both January/February payments fall. Reducing company reimbursement without reducing premium shifts cash costs to the household; it is not household savings. Broker exploration creates **zero current savings**.

### Vendor Audit

All24 pre-existing inventory entries reviewed; five missing bank/service entries added. Product labels below refer to tools/services; provider context includes [[entities/startvirtual]], [[entities/dodo-digital]], [[entities/squarespace]], [[entities/superhuman]], and [[entities/bizbuysell]]. Monthly equivalents below mix prepaid allocation and recurring allowances, deliberately **not** summed into the cash forecast. The bridge governs.

| Tool/service | August bank debit | Planning monthly equivalent | Finding |
|---|---:|---:|---|
${vendorTable}

No September feed: absence of an August charge supports a stopped-service assessment only through August, not current vendor confirmation. Linkt cancellation did not stop Aug1 charge199.99. Apollo/ZenLeads charged64.24 Aug2; September cancellation is user evidence, not observed bank stoppage. Potential NEW software savings: **195.97/month /2351.64 annualized** from hypothetical ChatGPT downgrade to21.78 all-in; price and eligibility unverified, not included in base. All other canceled savings already reflected; do not claim them again. At most optional subscriptions can reduce part of a much larger payroll/health gap.

## Action Items and Limitations

${model.assumptions.map(a=>'- '+a).join('\n')}
- User reports Monday Sep14 conference booking and NY broker tasks already saved in rows365/366. No tracker changes needed or made. Bead creation attempted but no active database found; no initialization/migration performed.
- Verify actual September cash and payroll cutoff before acting on cuts. Confirm vendor pause before October billing. No new emails or Slack generated.
- Accounting3200 is historical; a future filing bill or website tax would increase gap dollar-for-dollar. Any unplanned DD above38000, unknown renewal or post-September DealsX invoice is outside base.

## Sources and Verification

${Object.entries(model.sources).map(([label,url])=>`- [${label}](${url})`).join('\n')}
- [[outputs/2026-09-11-budget-report-aug-2026|Friday report]] and [[context/budget|budget policy]]. User September12 corrections govern payables, reserve, cancellations and pending receipts.
- Structured model: [[operating-areas/c-suite/CFO/2026-09-12-budget-followup-calculations.json]]. Dated ledger: [[operating-areas/c-suite/CFO/2026-09-12-budget-followup-cash-ledger.json]]. These JSON audit artifacts are not vault notes.
- Pre-write snapshot: ${snapPath}. Each changed range also re-fetched immediately before write. Post-write cells matched exactly; August actuals/YTD unchanged except operational reserve label/value. Full verification: [[operating-areas/c-suite/CFO/2026-09-12-budget-followup-postverify.json]].
`;
const alternateSection = '\n## Every Other Weekly Paycheck\n\nHealthcare remains $2,750 MONTHLY. Salary-related Gusto cash debits are $3,415.82 WEEKLY. Monthly healthcare and the fixed payroll-service fee are unchanged when checks are skipped. Compensation must be reduced, not deferred.\n\n| First skipped pay | Skipped checks | Saved | Feb7 cash | Gap to $38K reserve | First reserve breach |\n|---|---:|---:|---:|---:|---|\n' + alternating.map(a=>[a.first_skipped,a.skipped_count,money(a.savings),money(a.ending_cash),money(a.reserve_shortfall),a.first_reserve_breach].join(' | ')).map(r=>'| '+r+' |').join('\n') + '\n\nSeptember15 case skipped dates: '+alternating[0].skipped_dates.join(', ')+'. It retains 12 of 23 modeled checks, including the first two elapsed September checks. No September bank feed or payroll cutoff verified. Dates remain estimates.\n\nThe dated model exceeds the monthly-average calculation by $2,909.73: payroll timing +$853.96, full February healthcare +$2,062.50, and insurance timing -$6.71, with cent rounding. Six monthly reimbursements are modeled September-February; 23 weekly checks September1-February2.\n';
write(reportPath,report+alternateSection);
write(path.join(root,'brain/outputs/2026-09-12-tech-stack-audit.md'),`---\nschema_version: 1.1.0\ndate: 2026-09-12\ntype: tech-stack-audit\nstatus: review\nskill_origin: budget-manager\nkay_approved: null\npeople: []\ncompanies: ["[[entities/greenwich-and-barrow]]"]\nprojects: []\ntags: [date/2026-09-12, output, output/tech-stack-audit, status/review, topic/budget, company/greenwich-and-barrow]\n---\n\n# August Tech Stack Audit\n\nFor [[entities/greenwich-and-barrow]]. All24 existing rows plus5 bank/service additions audited. See [[outputs/2026-09-12-budget-runway-followup-aug-2026#Vendor Audit|full evidence, amounts, dates, and source links]].\n\nKEEP essential services; EVALUATE unmatched Howie/Voice/Slack allowances; CUT CANDIDATE ChatGPT downgrade, hypothetical195.97/month and2351.64/year, not implemented. Linkt199.99 and Apollo64.24 still billed in August despite forward cancellation assumptions. No September feed. No new savings counted from already-canceled tools. Inventory and all totals recomputed and live verified; cash forecast excludes prepaid annual renewals outside the horizon.\n`);
model.report_path=reportPath;model.status='report and dashboard complete; verified';write(path.join(out,'2026-09-12-budget-followup-calculations.json'),model);
console.log(JSON.stringify({status:model.status,reportPath,snapPath,inventoryRows:audit.length,checks:model.validation},null,2));
