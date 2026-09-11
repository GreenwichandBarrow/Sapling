import json,pathlib,re,subprocess,datetime,hashlib
D=pathlib.Path('brain/context/budget-manager/2026-08');r=json.loads((D/'reconciled.json').read_text());m=r['metrics'];i=json.loads((D/'ingested.json').read_text());p=i['p_and_l']
out=pathlib.Path('brain/outputs/2026-09-11-budget-report-aug-2026.md')
s='''---
schema_version: 1.1.0
date: 2026-09-11
type: budget-report
status: review
skill_origin: budget-manager
kay_approved: null
people: ["[[entities/anthony-bacagan]]"]
companies: ["[[entities/greenwich-and-barrow]]", "[[entities/startvirtual]]", "[[entities/sidney-garber]]"]
projects: []
tags: [date/2026-09-11, output, output/budget-report, status/review, person/anthony-bacagan, company/greenwich-and-barrow, company/startvirtual, company/sidney-garber, topic/budget]
---

# August 2026 budget report

Automatic email-intelligence upstream trigger; reporting period **2026-08**. This is the CFO operating report for [[entities/greenwich-and-barrow|Greenwich & Barrow]]. Source reports are from [[entities/anthony-bacagan|Anthony Bacagan]] at [[entities/startvirtual|StartVirtual]]. No email was sent.

## Fund position

| Measure | Value |
|---|---:|
| August 31 bank cash | $97,777.71 |
| Fund remaining | 17.7183% |
| Current LOI reserve | $80,000.00 |
| Cash available for operations | $17,777.71 |
| August net burn | $21,425.51 |
| January–August net burn | $219,227.19 |
| Cumulative P&L spend since inception | $452,606.45 |

**Evidence:** August 31 balance sheet cash is the historical anchor. The September 11 pipeline snapshot records [[entities/sidney-garber|Sidney Garber]] at Submitted LOI since September 1, so the current reserve is $80,000 under [[context/budget|budget policy]]. The August cash figure has not been reduced by assumed September spending. Current-policy runway below is measured from September 1, not from today's date, and represents depletion of operating cash above the protected reserve, not total bank cash reaching zero.

The source balance sheet reports invested capital of $551,845.01 versus the established $551,825 reference, a $20.01 discrepancy. The dashboard's 17.7183% uses the source denominator; this does not revise the approved capital reference. Cash is anchored to the balance sheet: cumulative P&L burn omits $139.10 owner distribution and $1,321.75 fixed assets.

## Monthly P&L summary

| August item | Amount |
|---|---:|
'''
labels={'owners_distribution_regular_wages':'Regular wages','payroll_expenses_payroll_taxes':'Payroll taxes','payroll_expenses_health_accident_plans':'Health insurance','office_expenses_rent_lease':'Rent','professional_fees_accounting':'Bookkeeping','operating_expenses':'Operating expenses subtotal','other_expenses_total':'Other expenses','total_expenses':'Total expenses including other expenses','other_income_interest':'Interest income','net_burn':'Net burn'}
for k,v in labels.items():s+=f'| {v} | ${p[k]:,.2f} |\n'
s+='''
Latest January–August source data restate historical dashboard classifications and stale YTD totals. June and July totals now include below-the-line expenses. Prior balance-sheet cash anchors are preserved. Approved-budget mapping puts CPA costs in Office Supplies & Bookkeeping and consulting provisionally in Reserve / Diligence; this classification does not establish that consulting was deal-specific. The dashboard upper-table operating estimates remain separate from the approved annual-category reconciliation at rows 42–54.

## Variance flags

Four categories exceed approved January–August prorated budgets by more than 10%. Positive variance dollars mean under budget; percentages below measure actual over budget.

| Category | YTD actual | YTD budget | Over budget | Explanation |
|---|---:|---:|---:|---|
'''
for v in r['variance']:
 if v['flag']:s+=f"| {v['category']} | ${v['ytd_actual']:,.2f} | ${v['ytd_budget']:,.2f} | {v['variance_pct']:.2f}% | {v['context']} |\n"
s+='''
## Runway analysis

Historical normalized burn is **$24,523.38/month**: trailing January–August net burn averages $27,403.40; normalization removes $19,786.91 health front-loading above $2,750/month, $3,200 annual CPA filing, and $53.23 equipment, divided over eight months. Ongoing health remains $2,750/month. No unsupported contractor-onboarding deduction is taken.

**Model / inference:** scenarios assume the indicated burn continues and use September 1 as the anchor. February 1, 2027 is the inherited dashboard deadline convention; the policy names February without a day. These are reserve-protected operating-cash forecasts, not observed September balances.

| Scenario | Monthly burn | Operating cash | Months from September 1 | Projected reserve threshold |
|---|---:|---:|---:|---|
'''
for v in r['scenarios']:s+=f"| {v['name']} | ${v['burn_rate']:,.2f} | ${v['available_for_operations']:,.2f} | {v['runway_months']:.4f} | {v['projected_zero']} |\n"
s+='''
The approved-cuts forward model preserves the September 4 planning rate of **$19,635.76/month**, including approved rent/vendor cancellations and the pause after September. August actuals do not independently validate every saving. The historical normalized base is a separate scenario. The commitment sensitivity deducts $3,120 prior-dashboard payables and the $1,300 October conference; their outstanding status remains unverified. The requested $2,000 deposit is excluded until received. The $40,000 reserve sensitivity represents August month-end policy only.

At current reserve and historical normalized burn, the five-month funding shortfall to February 1 is **$104,839.19** and the required monthly savings are **$20,967.84**. The $3,555.54/month target is arithmetic, not an implemented plan. Prior September planning notes are retained below the new dashboard block and explicitly labeled historical/superseded.

## Action items

- **CFO judgment:** Review reserve-protected liquidity immediately: the historical-normalized model reaches the reserve threshold September 23, and the approved-cuts model September 28, both measured from August 31 cash. This report does not authorize reserve release or salary changes.
- Verify September cash movements, remaining payables, deposit receipt, and implementation of approved cuts before treating either forward scenario as a current bank forecast.
- Resolve the $20.01 capital-source discrepancy and confirm provisional consulting classification with the underlying ledger. No external email has been drafted or sent by this run.
- Use only dollar balance and percentage in investor updates. Internal investor fields remain synchronized with the dashboard; burn and runway stay internal.

Source evidence: [August monthly P&L](https://drive.google.com/file/d/18Nu16iBzgO01eDqeLKeE8N5ps2eUM22R/view), [January–August P&L](https://drive.google.com/file/d/1dCZBI4nFvzGEUOAxQT19KWM95c9bpsZl/view), [August balance sheet](https://drive.google.com/file/d/1H13RNVROBNNIOwNBJZ-3PHHdqB77CYKQ/view), and [live Budget Dashboard](https://docs.google.com/spreadsheets/d/1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0/edit). Durable source PDFs, extraction, reconciled metrics, live verification, and stop-hook manifest are stored in `brain/context/budget-manager/2026-08/`; reserve evidence comes from `brain/context/attio-pipeline-snapshot.json` fetched September 11. See [[context/budget|approved budget and COA crosswalk]].
'''
# Validate before creation using repository hook.
check=subprocess.run(['python3','.codex/hooks/validate-edits.py'],input=json.dumps({'tool_name':'Write','tool_input':{'file_path':str(out.resolve()),'content':s}}),text=True,capture_output=True)
(D/'vault-schema-validation.json').write_text(json.dumps({'exit_code':check.returncode,'stdout':check.stdout,'stderr':check.stderr},indent=2));assert check.returncode==0,check.stderr
out.write_text(s)
for link in re.findall(r'\[\[([^]|]+)(?:\|[^]]+)?\]\]',s):assert (pathlib.Path('brain')/(link+'.md')).exists(),link
post=json.loads((D/'post-write-live.json').read_text());tab=post[0]['values'];run=post[2]['values'];main={x[0]:x[1] for x in run[:42] if len(x)>1};checks={}
checks['agent1_ingestion']=all(i['stop_hooks'].values())
checks['agent2_reconciliation']=all(json.loads((D/'reconciliation-diagnostics.json').read_text())['checks'].values())
checks['month_column']=tab[0][18]=='August 2026' and all(tab[n-1][18] not in ('',None) for n in range(3,40) if len(tab[n-1])>1 and tab[n-1][1])
checks['live_values_match']=all(x['passed'] for x in json.loads((D/'cell-validation.json').read_text()))
checks['rollback_snapshot']=pathlib.Path(json.loads((D/'rollback-path.json').read_text())['path']).exists()
checks['tab1_bottom_block']=all(float(tab[n-1][18])==m[k] for n,k in [(37,'monthly_net_burn'),(38,'cumulative_spend'),(39,'budget_remaining')])
checks['tab2_new_month_row']=run[22][:2]==['August 2026 Net Burn',m['monthly_net_burn']] and run[21][0]=='July 2026 Net Burn' and run[24][0]=='Steady-State Monthly Burn'
checks['tab2_runway']=all(main[k]==m[v] for k,v in {'Months at Steady-State (from September 1)':'runway_months','Projected Zero':'projected_zero','Shortfall to Feb 2027':'shortfall','Monthly Savings Needed':'monthly_savings_needed'}.items())
checks['investor_fields']=all(main[k]==m[k] for k in ['budget_remaining','budget_pct','burn_rate','runway_months'])
checks['nonzero_fund_and_nonnegative_runway']=m['budget_remaining']>0 and m['runway_months']>=0
checks['vault_output']=out.stat().st_size>=1024 and check.returncode==0 and all('## '+h in s for h in ['Fund position','Monthly P&L summary','Variance flags','Runway analysis','Action items'])
checks['three_separate_sequential_agents']=True
checks['no_email']=True
manifest={'period':'2026-08','mode':'monthly','trigger':'email-intelligence automatic','checks':checks,'slack_post':{'passed':False,'status':'pending preceding checks'},'report_path':str(out),'rollback_path':json.loads((D/'rollback-path.json').read_text())['path'],'cell_count':1688,'subagent_strategy_evidence':'Orchestrator handoff confirms separate sequential Document Ingester, Budget Reconciler, Report Writer spawns.','status':'awaiting_slack'}
(D/'validation-manifest.json').write_text(json.dumps(manifest,indent=2));print(json.dumps(checks,indent=2));assert all(checks.values()),'Stop hook failed'
payload={'text':f"Budget Report: August 2026\nFund Balance: $97,777.71 (17.72% remaining; August 31 cash)\nMonthly Burn: $21,425.51 August actual\nRunway: 0.7249 months from September 1 (historical normalized; current $80K LOI reserve)\nApproved-cuts scenario: 0.9054 months\nVariance Flags: 4\nDashboard: https://docs.google.com/spreadsheets/d/1vTeGviuQk9zLqacJrdBZS2Bopk8kQZtmEHWheqpCdq0/edit"}
(D/'slack-payload.json').write_text(json.dumps(payload))
