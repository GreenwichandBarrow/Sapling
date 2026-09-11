import json,datetime,calendar,math
from pathlib import Path
P=Path('/tmp/budget-manager-2026-08'); d=json.loads((P/'ingested.json').read_text()); hist=d['monthly_history']; y=d['p_and_l_ytd']; bs=d['balance_sheet']; live=json.loads((P/'live-tab1.json').read_text())['values']; tab2=json.loads((P/'live-tab2.json').read_text())['values']; r=lambda x:round(x,2)
cats={
'Principal Draw':(165000,['owners_distribution_regular_wages']),
'Payroll Taxes & Benefits':(10000,['payroll_expenses_payroll_taxes','payroll_expenses_business_insurance','payroll_expenses_health_accident_plans']),
'Interns/Contractors':(15000,['contractors_contract_labor','contractors_outsourcing']),
'Travel & Business Development':(10000,['travel_airfare','travel_car_rides','travel_meals_entertainment','travel_vehicle_gas','travel_hotels','travel_parking_tolls']),
'Office Supplies & Bookkeeping':(14000,['office_expenses_rent_lease','office_expenses_office_supplies','office_expenses_postage','office_expenses_small_tools_equipment','professional_fees_accounting']),
'Reserve / Diligence Expenses':(19000,['professional_fees_consulting']),
'Marketing, Software, Research':(16000,['advertising_marketing','databases_research','office_expenses_apps_software_crm_storage','office_expenses_apps_software_office_use','general_business_memberships_subscriptions']),
'Start Up Costs':(0,[]),
'Contingency & Misc':(20000,['bank_fees_service_charges','business_taxes_licenses','other_expenses_medical','vehicle_repairs'])}
context={
'Payroll Taxes & Benefits':'Structural unbudgeted health insurance plus front-loaded installments. Health YTD $41,786.91; normalize ongoing health to $2,750/month, never zero. Taxes/insurance alone $9,312.94 exceed $6,666.67 prorated budget.',
'Travel & Business Development':'Structural YTD overspend with lumpy conference/trip timing; travel $18,488.04 already exceeds full-year $10,000 allocation.',
'Office Supplies & Bookkeeping':'Mixed timing and structural: $3,200 CPA annual filing, $9,000 rent YTD, bookkeeping continues $247/month. Approved September lease cancellation is forward savings only.',
'Marketing, Software, Research':'Mixed structural and timing: marketing includes prior DealsX catch-up; approved cancellations and pause are forward assumptions, not historical refunds.'}
variance=[]
for name,(budget,keys) in cats.items():
 actual=r(sum(y[k] for k in keys)); b=budget*8/12
 variance.append(dict(category=name,annual_budget=budget,monthly_budget=r(budget/12),ytd_actual=actual,ytd_budget=r(b),variance_dollars=r(b-actual),variance_pct=r((actual-b)/b*100) if b else None,flag=actual>b*1.1,context=context.get(name,'Within approved YTD allocation; allocation follows QBO crosswalk.')))
assert r(sum(v['ytd_actual'] for v in variance))==y['total_expenses']
trailing=y['net_burn']/8
exclusions={'health_frontload_above_2750_per_month':r(y['payroll_expenses_health_accident_plans']-2750*8),'CPA_annual_filing':3200,'hardware_small_tools':53.23}
steady=r((y['net_burn']-sum(exclusions.values()))/8)
cash=bs['total_cash']; reserve=80000; avail=r(cash-reserve); anchor=datetime.date(2026,9,1)
# Deadline Feb 2027 interpreted as Feb 1, matching prior six-month Aug->Feb dashboard convention.
months_to_deadline=5; target=r(avail/months_to_deadline)
def scenario(name,burn,available=avail,notes=''):
 months=available/burn
 whole=int(months); rem=months-whole; absolute=anchor.month-1+whole; base=datetime.date(anchor.year+absolute//12,absolute%12+1,1); zero=base+datetime.timedelta(days=round(rem*calendar.monthrange(base.year,base.month)[1]))
 return dict(name=name,burn_rate=burn,available_for_operations=available,runway_months=round(months,4),projected_zero=zero.isoformat(),notes=notes)
scenarios=[scenario('Current trailing average',r(trailing)),scenario('Steady-state historical normalized',steady),scenario('Approved cuts forward model',19635.76,notes='Retain Sep 4 live dashboard planning model; assumes approved rent/vendor cancellations and DealsX paused after September. August source does not validate every saving.'),scenario('Target to February 1',target,notes='Required mathematical target; no claim these savings are implemented.'),scenario('August month-end reserve sensitivity',steady,r(cash-40000),notes='Uses pre-Sep-1 $40K reserve; current Submitted LOI policy requires $80K.'),scenario('Approved cuts plus known commitments',19635.76,r(avail-3120-1300),notes='Deduct prior dashboard $3,120 known DealsX payables and $1,300 October conference as unverified outstanding commitments; exclude requested $2,000 deposit until received.')]
metrics=dict(budget_remaining=cash,budget_pct=round(cash/bs['owner_investments']*100,4),burn_rate=steady,runway_months=scenarios[1]['runway_months'],dd_reserve=reserve,available_for_operations=avail,as_of_date='2026-08-31',reserve_policy_as_of='2026-09-11',fund_deadline='2027-02-01',runway_anchor='2026-09-01',projected_zero=scenarios[1]['projected_zero'],trailing_average_burn=r(trailing),target_burn=target,shortfall=r(steady*5-avail),monthly_savings_needed=r(steady-target),buffer_months=round(avail/steady-5,4),ytd_net_burn=y['net_burn'],monthly_net_burn=d['p_and_l']['net_burn'],cumulative_spend=r(-bs['retained_earnings']+y['net_burn']))
# Preserve original 39-row topology and historical balance anchors; insert August pair before YTD in plan.
rows=[(a+['']*24)[:18]+['','']+(a+['']*24)[18:22] for a in live]
rows[0][18:24]=['August 2026','Aug +/-','YTD Actual','YTD Budget','Variance $','Variance %']
maprows={3:['owners_distribution_regular_wages'],4:['payroll_expenses_payroll_taxes'],5:['owners_distribution_regular_wages','payroll_expenses_payroll_taxes'],6:['payroll_expenses_health_accident_plans'],7:['payroll_expenses_business_insurance'],9:['contractors_outsourcing'],10:['contractors_contract_labor'],14:['office_expenses_rent_lease'],15:['office_expenses_office_supplies'],16:['office_expenses_postage'],17:['travel_airfare'],18:['travel_car_rides'],19:['travel_meals_entertainment'],20:['travel_vehicle_gas'],21:['bank_fees_service_charges'],22:['travel_hotels','travel_parking_tolls'],24:['office_expenses_apps_software_crm_storage'],25:['office_expenses_apps_software_office_use'],26:['databases_research'],27:['advertising_marketing'],28:['business_taxes_licenses','general_business_memberships_subscriptions','office_expenses_small_tools_equipment','other_expenses_medical','vehicle_repairs'],35:['total_expenses'],36:['other_income_interest'],37:['net_burn']}
rows[21][1]='Travel - Hotels / Parking';rows[27][1]='Other expenses - see source detail';rows[29][1]='Professional fees excluding recurring bookkeeping'; rows[10][1]='Bookkeeper (Accounting Fees)';rows[36][1]='Net Burn (All Expenses - Interest)'
changes=[]
for m,(period,v) in enumerate(hist.items()):
 col=4+2*m
 vals={rn:r(sum(v[k] for k in keys)) for rn,keys in maprows.items()}
 vals[11]=247 if period>='2026-04' else 0
 vals[30]=r(v['professional_fees_accounting']+v['professional_fees_consulting']-vals[11]);vals[32]=0;vals[33]=0
 vals[38]=r(-bs['retained_earnings']+sum(a['net_burn'] for p,a in hist.items() if p<=period))
 if period=='2026-08':vals[39]=cash
 for rn,val in vals.items():
  if m<7 and str(rows[rn-1][col])!=str(val):changes.append(dict(cell=f'{chr(65+col)}{rn}',old=rows[rn-1][col],new=val))
  rows[rn-1][col]=val
  if rows[rn-1][2] and rn<36: rows[rn-1][col+1]=r(val-float(rows[rn-1][2])/12)
for rn in set(maprows)|{11,30,32,33}:
 actual=r(sum(float(rows[rn-1][4+2*m] or 0) for m in range(8)));rows[rn-1][20]=actual
 if rows[rn-1][2]:
  budget=float(rows[rn-1][2])*8/12;rows[rn-1][21:24]=[r(budget),r(budget-actual),r((actual-budget)/budget*100) if budget else '']
rows[37][20]=metrics['cumulative_spend'];rows[38][20]=cash
# Supplemental approved allocation table explicitly distinguishes investor approval from operational line estimates.
extra=[['APPROVED YEAR 2 CATEGORY RECONCILIATION'],['Category','Annual Budget','Monthly Budget','YTD Actual','YTD Budget','Variance $','Variance %','Context']]
for v in variance:extra.append([v[k] for k in ['category','annual_budget','monthly_budget','ytd_actual','ytd_budget','variance_dollars','variance_pct','context']])
extra.append(['TOTAL',269000,r(269000/12),y['total_expenses'],r(269000*8/12),r(269000*8/12-y['total_expenses']),r((y['total_expenses']/(269000*8/12)-1)*100)])
extra.append(['Notes','Upper-table line budgets are existing operating estimates, not revised investor approvals. All monthly histories restated to August source. DD reserve is held cash, not expense.'])
# Tab2 preserve historic notes as archived context beneath new canonical blocks, including columns C:F.
new2=[['Budget Dashboard','Greenwich & Barrow'],['Last Updated','2026-09-11'],['As of','2026-08-31 cash; Sep 11 LOI reserve policy'],['Fund Balance',cash],['DD Reserve',reserve],['Available for Operations',avail],['Steady-State Monthly Burn',steady],['Months at Steady-State (from September 1)',metrics['runway_months']],['Projected Zero',metrics['projected_zero']],['Shortfall to Feb 2027',metrics['shortfall']],['Monthly Savings Needed',metrics['monthly_savings_needed']],['Dashboard Source','August 2026 P&Ls and BS; current Attio LOI snapshot'],['Notes','Reserve rises to $80K at Submitted LOI. Excludes requested deposit from cash. Deadline modeled Feb 1, 2027. Historical-normalized burn; approved-cuts scenario below.'],[],['BURN RATE']]
for period,v in hist.items():new2.append([datetime.date.fromisoformat(period+'-01').strftime('%B %Y')+' Net Burn',v['net_burn']])
new2 += [['Trailing Average Burn',r(trailing)],['Steady-State Monthly Burn',steady],[],['INVESTOR REPORTING']]+[[k,metrics[k]] for k in ['budget_remaining','budget_pct','burn_rate','runway_months','projected_zero']]+[['target_cash_date','2027-02-01'],['monthly_gap_to_target',metrics['monthly_savings_needed']],[],['RUNWAY SCENARIOS','Burn','Operating Cash','Months','Projected Zero','Assumptions']]
for s in scenarios:new2.append([s['name'],s['burn_rate'],s['available_for_operations'],s['runway_months'],s['projected_zero'],s['notes']])
new2 += [[],['PRIOR SEPTEMBER 4 PLANNING CONTEXT - HISTORICAL, SUPERSEDED MAIN METRICS']]+tab2
out=dict(status='success_with_flags',period='2026-08',metrics=metrics,variance=variance,flag_count=sum(v['flag'] for v in variance),scenarios=scenarios,steady_state_exclusions=exclusions,steady_state_method='Jan-Aug net burn minus health above $2,750/month, identified $3,200 CPA annual filing and $53.23 equipment. No assumed contractor onboarding or consulting exclusion without source. Approved Sep 4 forward cuts retained separately.',mapping_notes=['CPA/accounting maps to Office Supplies & Bookkeeping; consulting provisionally to Reserve/Diligence per crosswalk, without asserting deal-specific expense.','Membership subscriptions map to Marketing/Software; medical, licenses and vehicle repair map to Contingency.','Cash period Aug31 and reserve state Sep11 are explicitly different dates.'],data_quality_flags=['Owner Investments $551,845.01 differs from immutable reference $551,825 by $20.01. Percent uses source BS investments, retain discrepancy.','Earlier dashboard YTD wages/payroll totals were stale, restated account classifications differ, and June/July expense totals omitted below-the-line amounts; restate Jan-Aug P&L from latest source.','Prior month BS cash anchors are preserved; P&L cumulative spend excludes $139.10 owner distribution and $1,321.75 fixed asset, so cash is anchored to BS rather than inferred from P&L.','Historical normalized burn is conservative; approved vendor cuts forward plan remains separate.','Deadline day unspecified in reference; Feb1 convention retained from prior dashboard Aug->Feb six-month target.'],reserve_evidence={'path':'brain/context/attio-pipeline-snapshot.json','fetched_at':'2026-09-11T00:01:09Z','company':'Sidney Garber','stage':'Submitted LOI','stage_since':'2026-09-01T16:25:21.066600000Z'},source_paths=['brain/context/budget.md','brain/context/attio-pipeline-snapshot.json',str(P/'ingested.json'),str(P/'live-tab1.json'),str(P/'live-tab2.json')],historical_changes=changes,write_plan=[{'range':"'Monthly Actuals vs Budget'!A1:X39",'values':rows},{'range':f"'Monthly Actuals vs Budget'!A42:H{41+len(extra)}",'values':extra},{'range':f"'Runway Forecast'!A1:F{len(new2)}",'values':new2}],writer_requirements=['Re-fetch all planned ranges immediately before any mutation; save required durable rollback snapshot.','Expand grid if necessary after checking sheet metadata; prefer atomic batch write across all ranges.','Original Tab1 YTD S:V moves to U:X by full planned range rewrite; August S and T.','New August burn row follows July and precedes aggregates in rewritten Tab2; prior block copied below as historical archive.','Historical balance sheet months E:Q row39 preserved; August S39 and U39 use new cash.','Validate every planned value post-write, source month header, bottom block, month burn row, investor fields, and vault schema/sections.'],checks={'category_sum_matches_total_expenses':True,'available_cash_math':r(cash-reserve)==avail,'runway_finite_nonnegative':math.isfinite(metrics['runway_months']) and metrics['runway_months']>=0})
(P/'reconciled.json').write_text(json.dumps(out,indent=2)); (P/'write-plan.json').write_text(json.dumps(out['write_plan'],indent=2));(P/'reconciliation-diagnostics.json').write_text(json.dumps({k:out[k] for k in ['checks','historical_changes','data_quality_flags','reserve_evidence','source_paths']},indent=2))
print(json.dumps({'metrics':metrics,'flags':[v for v in variance if v['flag']],'scenarios':scenarios,'ranges':[p['range'] for p in out['write_plan']]},indent=2))
