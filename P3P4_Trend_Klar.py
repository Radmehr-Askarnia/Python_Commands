# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:24:52 2020

@author: radmehr.a
"""

import matplotlib.pyplot as plt
import pandas as pd

xlsx = pd.ExcelFile(r"D:\1.P3P4\Trendstatistiken.xlsx")
df = xlsx.parse('Trend_Stats')


df_Date = df['Date']
df_Target = df['Target']
df_Case = df['Count_Cases']

df_Date_1 = df_Date.iloc[-30:]
df_Case_1 = df_Case.iloc[-30:]
df_Target_1 = df_Target.iloc[-30:]

df_Date_2 = df_Date.iloc[-60:-30]
df_Case_2 = df_Case.iloc[-60:-30]

df_Date_1 = df_Date_1.to_frame()
df_Case_1 = df_Case_1.to_frame()
df_Target_1 = df_Target_1.to_frame()
df_Date_2 = df_Date_2.to_frame()
df_Case_2 = df_Case_2.to_frame()
df_Date_1 = df_Date_1.reset_index()
df_Case_1 = df_Case_1.reset_index()
df_Target_1 = df_Target_1.reset_index()
df_Date_2 = df_Date_2.reset_index()
df_Case_2 = df_Case_2.reset_index()

df_1 = df_Date_1['Date']
df_1 = df_1.to_frame()
df_1['Count_Cases'] = df_Case_1['Count_Cases']
df_1['Target'] = df_Target_1['Target']

#df_1['Target'] = ['0']

df_2 = df_Date_1['Date']
df_2 = df_2.to_frame()
df_2['Count_Cases'] = df_Case_2['Count_Cases']


plt.plot('Date', 'Count_Cases', data=df_1, marker='o', markerfacecolor='blue', 
              markersize=12, color='skyblue', linewidth=4)

dfr = df_1['Count_Cases']
y = pd.Series(dfr)

for i, v in enumerate (y):
    plt.text(i - 0.25, v + 3, str(v), color='blue', fontweight='bold')
    #plt.text(i, v, " "+str(v), color='blue', va='center', fontweight='bold')

plt.plot('Date', 'Count_Cases', data=df_2, marker='o', markerfacecolor='blue', 
              markersize=10, color='Red', linewidth=3, alpha=0.15)

plt.xticks(rotation='vertical')
plt.plot('Date', 'Target', data=df_1, marker='o', markersize=10, color='#59b300', linewidth=5) #, linestyle = '--'

         
plt.ylabel('Count_Cases', color = 'Blue')
plt.title('Daily_Trend', color = 'Blue', fontsize = '22')


