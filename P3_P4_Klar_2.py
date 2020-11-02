# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 18:18:49 2020

@author: radmehr.a
"""

import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns
import numpy as np


xlsx1 = pd.ExcelFile(r"D:\1.P3P4\Files\Heute\1.xlsx")
xlsx2 = pd.ExcelFile(r"D:\1.P3P4\Files\Heute\2.xlsx")
xlsx3 = pd.ExcelFile(r"D:\1.P3P4\Files\Heute\2.xlsx")
xlsxr = pd.ExcelFile(r"D:\1.P3P4\Trendstatistiken.xlsx")
#xlsxk = pd.ExcelFile(r"D:\1.P3P4\AP3P4_das_Resultat.xlsx") #Read File for Draw Trend
xlsxHN = pd.ExcelFile(r"D:\1.P3P4\Heatmap_Neu.xlsx")

df1 = xlsx1.parse('Sites Level 4G')
df2 = xlsx2.parse('2G')
df3 = xlsx3.parse('3G')
dfr = xlsxr.parse('Trend_Stats')
#dfk = xlsxk.parse('Trend_Stats')  #Read Sheet for Draw Trend
dfHN = xlsxHN.parse('Sheet1')

dfr['Date'] = pd.to_datetime(dfr['Date'], format = ('%Y-%m-%d'))
dfr['Date'] = pd.to_datetime(dfr['Date']).dt.strftime('%Y-%m-%d')

new_header = df1.iloc[0]
df1 = df1[1:]
df1.columns = new_header
df1 = df1.drop([1])
new_header = df2.iloc[0]
df2 = df2[1:]
df2.columns = new_header
df2 = df2.drop([1])
new_header = df3.iloc[0]
df3 = df3[1:]
df3.columns = new_header
df3 = df3.drop([1])

df1['TECH'] = pd.Series(['LTE' for x in range(len(df1.index))]) 
df2['TECH'] = pd.Series(['GSM' for x in range(len(df1.index))]) 
df3['TECH'] = pd.Series(['WCDMA' for x in range(len(df1.index))]) 

df1.rename(columns={'4G LTE ENODB':'SITE_ID'},inplace = True)
df1['NE'] = df1['SITE_ID']
df2.rename(columns={'Zone':'Zone_Priority'},inplace = True)
df2.rename(columns={'2G BSC':'NE'},inplace = True)
df2.rename(columns={'2G BTS':'SITE_ID'},inplace = True)
df3.rename(columns={'3G NODEB':'SITE_ID'},inplace = True)
df3.rename(columns={'3G RNC':'NE'},inplace = True)

df1['Physical_Site'] = df1.SITE_ID.str.slice(1,6)
df2['Physical_Site'] = df2.SITE_ID.str.slice(0,5)
df3['Physical_Site'] = df3.SITE_ID.str.slice(1,6)


frames = [df1, df2, df3]
dff = pd.concat(frames, sort = True)


dff.loc[dff['Site_Priority'].isnull(),'Site_Priority']=0
dff.loc[dff['Site_Priority'] == 0, 'Site_Priority'] = 'P4' 

cols_to_order = ['Physical_Site', 'SITE_ID','NE','Site_Priority','TECH','Region','Province','City','Vendor','Zone_Priority','FLM NAME']
new_columns = cols_to_order + (dff.columns.drop(cols_to_order).tolist())
dff = dff[new_columns]

dff = dff.loc[dff['Site_Priority'].isin(['P3','P4'])]

dff.Province[dff.Province== 'ESFEHAN'] = 'ESFAHAN' # To Match With Tableau
dff.Province[dff.Province== 'SISTAN_BALOCHESTAN'] = 'Sistan and Baluchestan'
dff.Province[dff.Province== 'KHORASAN SHOMALI'] = 'North Khorasan'
dff.Province[dff.Province== 'HAHARMAHAL_BAKHTYARI'] = 'Chahar Mahall and Bakhtiari'

dff.columns = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R', 'S'] #Name:'A' not used


cond1 = dff.M < 99.2
cond2 = dff.N < 99.2
cond3 = dff.O < 99.2
cond4 = dff.P < 99.2
cond5 = dff.Q < 99.2
cond6 = dff.R < 99.2
cond7 = dff.S < 99.2

temp1 = pd.concat([cond4,cond5,cond6,cond7],axis=1)
dff['Count_Days_4'] = temp1.sum(axis=1)
df4 = dff.loc[dff['Count_Days_4'].isin(['4'])]
del df4['Count_Days_4']
del dff['Count_Days_4']

temp2 = pd.concat([cond1,cond2,cond3,cond4,cond5,cond6,cond7],axis=1)
dff['Count_Days_7'] = temp2.sum(axis=1)
df7 = dff.loc[dff['Count_Days_7'].isin(['7'])]
del df7['Count_Days_7']
del dff['Count_Days_7']


Heute = datetime.strftime(datetime.now(), '%Y-%m-%d')
Einen_Tag_Zuvor = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
Zwei_Tage_Zuvor = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
Drei_Tage_Zuvor = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')
Vier_Tage_Zuvor = datetime.strftime(datetime.now() - timedelta(4), '%Y-%m-%d')
Funf_Tage_Zuvor = datetime.strftime(datetime.now() - timedelta(5), '%Y-%m-%d')
Sechs_Tage_Zuvor = datetime.strftime(datetime.now() - timedelta(6), '%Y-%m-%d')
Sieben_Tage_Zuvor = datetime.strftime(datetime.now() - timedelta(7), '%Y-%m-%d')


df4.columns = ['Physical_Site', 'SITE_ID','NE','Site_Priority','TECH','Region','Province','City','Vendor','Zone_Priority','FLM NAME', Sieben_Tage_Zuvor, Sechs_Tage_Zuvor, Funf_Tage_Zuvor, Vier_Tage_Zuvor,Drei_Tage_Zuvor, Zwei_Tage_Zuvor, Einen_Tag_Zuvor]
df4.columns = map(lambda x: str(x).upper(), df4.columns)
df4 = df4.sort_values(['REGION'], ascending = True) 
df4.groupby(['PHYSICAL_SITE','SITE_ID']).first()
#df4.first()



Zeit_Trend = datetime.strftime(datetime.now()- timedelta(1), '%Y-%m-%d')
Zahl_Trend = df4['PHYSICAL_SITE'].nunique()
Null_Trend = '0'


dfrr = pd.DataFrame({'Date': [Zeit_Trend] ,'Count_Cases': [Zahl_Trend], 'Target': [Null_Trend]})
Bigdata = dfr.append(dfrr, ignore_index=False)

df8 = df4['REGION'].value_counts()
df8 = df8.to_frame()
df8 = df8.reset_index(inplace=False)
df8['Date'] = Zeit_Trend
df80 = df8['Date']
df81 = df8['REGION']
df82 = df8['index']
#Zeit_Trend_HN = pd.DataFrame({Zeit_Trend})

dfr8 = pd.DataFrame({'Date': df80 ,'Count_Cases': df81, 'Region': df82})
Bigdata2 = dfHN.append(dfr8, ignore_index=False)

#Draw Trend
"""
sns.set(style="whitegrid")
data = pd.DataFrame(values, dates, columns=["A", "B", "C"])
sns.lineplot(data=data, palette="tab10", linewidth=2.5)
"""


df7.columns = ['Physical_Site', 'SITE_ID','NE','Site_Priority','TECH','Region','Province','City','Vendor','Zone_Priority','FLM NAME', Sieben_Tage_Zuvor, Sechs_Tage_Zuvor, Funf_Tage_Zuvor, Vier_Tage_Zuvor,Drei_Tage_Zuvor, Zwei_Tage_Zuvor, Einen_Tag_Zuvor]
df7.columns = map(lambda x: str(x).upper(), df7.columns)
df7 = df7.sort_values(['REGION'], ascending = True) 
df7.merge(df7.groupby(['PHYSICAL_SITE','SITE_ID']).first())
#df7.first()



def background_gradient(rg):
    color =  'background-color: #ffcccc' if rg < 99.2  else 'background-color: #ccccff'
    return color


def highlight_cells(x):
    color = ' #990000' if x < 99.2 else '#000099'
    return 'color: %s' % color

df4 = df4.style.\
applymap(highlight_cells, subset=[Sieben_Tage_Zuvor, Sechs_Tage_Zuvor, Funf_Tage_Zuvor, Vier_Tage_Zuvor,Drei_Tage_Zuvor, Zwei_Tage_Zuvor, Einen_Tag_Zuvor]).\
applymap(background_gradient, subset = [Sieben_Tage_Zuvor, Sechs_Tage_Zuvor, Funf_Tage_Zuvor, Vier_Tage_Zuvor,Drei_Tage_Zuvor, Zwei_Tage_Zuvor, Einen_Tag_Zuvor]).\
set_properties(**{'text-align': 'center', 'border-style' :'solid', 'border-width' :'thin'})

df7 = df7.style.\
applymap(highlight_cells, subset=[Sieben_Tage_Zuvor, Sechs_Tage_Zuvor, Funf_Tage_Zuvor, Vier_Tage_Zuvor,Drei_Tage_Zuvor, Zwei_Tage_Zuvor, Einen_Tag_Zuvor]).\
applymap(background_gradient, subset = [Sieben_Tage_Zuvor, Sechs_Tage_Zuvor, Funf_Tage_Zuvor, Vier_Tage_Zuvor,Drei_Tage_Zuvor, Zwei_Tage_Zuvor, Einen_Tag_Zuvor]).\
set_properties(**{'text-align': 'center','border-style' :'solid', 'border-width':'thin'})



writer1 = pd.ExcelWriter(r'D:\1.P3P4\AP3P4_das_Resultat.xlsx', engine= 'xlsxwriter')
writer2 = pd.ExcelWriter(r"D:\1.P3P4\Trendstatistiken.xlsx", engine= 'xlsxwriter')
writer3 = pd.ExcelWriter(r"D:\1.P3P4\Heatmap_Neu.xlsx", engine= 'xlsxwriter')
df4.to_excel(writer1, '4_Days', index = False)
df7.to_excel(writer1, '7_Days', index = False)
Bigdata.to_excel(writer2, 'Trend_Stats', index = False)
Bigdata2.to_excel(writer3, 'Sheet1', index = False)


writer1.save()
writer2.save()
writer3.save()
