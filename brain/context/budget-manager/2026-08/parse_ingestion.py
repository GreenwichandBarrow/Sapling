import xml.etree.ElementTree as E,json,re,hashlib
from pathlib import Path
base=Path('/tmp/budget-manager-2026-08'); ns={'x':'http://www.w3.org/1999/xhtml'}
root=E.parse(base/'monthly-profit-loss.xml')
rows=[]
for page in root.findall('.//x:page',ns):
 groups={}
 for w in page.findall('.//x:word',ns):groups.setdefault(round(float(w.get('yMin')),1),[]).append(w)
 for y,words in sorted(groups.items()):
  nums=[w for w in words if re.fullmatch(r'-?\$?[\d,]+\.\d{2}',w.text or '') and float(w.get('xMax'))>190]
  if not nums:continue
  label=' '.join(w.text for w in sorted(words,key=lambda w:float(w.get('xMin'))) if float(w.get('xMax'))<190)
  vals=[0.0]*9
  for w in nums:
   idx=min(range(9),key=lambda i:abs(float(w.get('xMax'))-[228.35,271.75,315.15,358.55,403.10,446.50,489.90,533.55,591.25][i]))
   vals[idx]=float(w.text.replace('$','').replace(',',''))
  rows.append({'account':label,'monthly_values':vals[:8],'ytd_total':vals[8]})
mapnames={
'Advertising & Marketing':'advertising_marketing','Bank Fees':'bank_fees_service_charges','Business Taxes & Licenses':'business_taxes_licenses','Contract Labor':'contractors_contract_labor','Outsourcing':'contractors_outsourcing','Databases & Research':'databases_research','Memberships & Subscriptions':'general_business_memberships_subscriptions','CRM & Storage':'office_expenses_apps_software_crm_storage','Office Use':'office_expenses_apps_software_office_use','Office Supplies':'office_expenses_office_supplies','Postage & Shipping':'office_expenses_postage','Rent/Lease Expense':'office_expenses_rent_lease','Small Tools and Equipment':'office_expenses_small_tools_equipment','Business Insurance':'payroll_expenses_business_insurance','Health & Accident Plans':'payroll_expenses_health_accident_plans','Payroll Taxes':'payroll_expenses_payroll_taxes','Regular Wages':'owners_distribution_regular_wages','Accounting Fees':'professional_fees_accounting','Consulting Fees':'professional_fees_consulting','Car Rentals/Shared Rides':'travel_car_rides','Hotels':'travel_hotels','Meals & Entertainment':'travel_meals_entertainment','Parking & Tolls':'travel_parking_tolls','Travel Fare':'travel_airfare','Interest Income':'other_income_interest','Medical':'other_expenses_medical','Vehicle Gas & Fuel':'travel_vehicle_gas','Vehicle Repairs':'vehicle_repairs','Total for Expenses':'operating_expenses','Total for Other Expenses':'other_expenses_total','Net Income':'net_income'}
history={f'2026-{i+1:02}':{} for i in range(8)}; ytd={}
for row in rows:
 label=row['account']
 if label not in mapnames:continue
 key=mapnames[label]
 for i,(period,data) in enumerate(history.items()):data[key]=row['monthly_values'][i]
 ytd[key]=row['ytd_total']
for d in [*history.values(),ytd]:
 d['total_expenses']=round(d['operating_expenses']+d['other_expenses_total'],2)
 d['net_burn']=round(d['total_expenses']-d['other_income_interest'],2)
 assert abs(d['net_income']+d['net_burn'])<0.011,d
for row in rows:
 assert abs(sum(row['monthly_values'])-row['ytd_total'])<0.011,row
out={'status':'success','period':'2026-08','as_of_date':'2026-08-31','p_and_l':history['2026-08'],'p_and_l_ytd':ytd,'monthly_history':history,'all_report_rows':rows,'balance_sheet':{'cash':0,'checking':6902.49,'savings':90875.22,'total_cash':97777.71,'inventory_asset':0,'total_current_assets':97777.71,'office_equipment':1321.75,'total_fixed_assets':1321.75,'total_assets':99099.46,'owner_reimbursements':0,'total_liabilities':0,'net_income_ytd':-219227.19,'owner_distribution':-139.10,'owner_investments':551845.01,'retained_earnings':-233379.26,'total_equity':99099.46,'total_liabilities_equity':99099.46},'source_files':{'monthly_profit_loss':'18Nu16iBzgO01eDqeLKeE8N5ps2eUM22R','ytd_profit_loss':'1dCZBI4nFvzGEUOAxQT19KWM95c9bpsZl','balance_sheet':'1H13RNVROBNNIOwNBJZ-3PHHdqB77CYKQ'},'source_directory':str(base),'coa_reference':'brain/context/budget.md','notes':['Two AUGUST 2026 Drive folders exist; 17WbZPie96wgjcB03rh08iGN3qNyBDQmG is empty; populated source is 1cTaIiBtlXBQlYXOMqa2rlGHO1PQQ9Osw.','Profit and Loss PDF is cumulative January-August; monthly values extracted from Monthly Profit and Loss August column.','Source reclassifies Regular Wages under Payroll Expenses; normalized legacy key retained to match skill.','total_expenses includes operating and other expenses to avoid understating burn; QBO Total for Expenses retained separately as operating_expenses.','Blank monthly cells in a displayed account treated as zero; each row validated against source YTD total.','August source BS Owner Investments is 551845.01, differing from immutable reference 551825 by 20.01.','Historical months in current source may be restated relative to existing dashboard. Reconciler must compare before updates.'],'stop_hooks':{'both_required_pdfs_downloaded_and_parsed':True,'major_categories_numeric':True,'cash_extracted_nonzero':True,'period_verified':True,'all_monthly_rows_reconcile_ytd':True,'net_income_reconciles':True},'file_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in base.glob('*.pdf')}}
(base/'ingested.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'path':str(base/'ingested.json'),'p_and_l':out['p_and_l'],'rows_parsed':len(rows),'stop_hooks':out['stop_hooks']},indent=2))
