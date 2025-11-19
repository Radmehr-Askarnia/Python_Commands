"""
Created on Sun Oct  6 15:37:22 2019

@author: radmehr.a
"""

import seaborn as sns
sns.set()
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))
plt.title('Heatmap_Plot', fontname="Times New Roman", fontweight="bold", fontsize="24", color="Brown")

label = plt.xlabel("x-label", fontsize="14") #, rotation = 45
label.set_color("White")

label = plt.ylabel("y-label", fontsize="14")
label.set_color("White")

file_name = r"D:\1.P1P2\Heatmap_Neu.xlsx"
df = pd.read_excel(file_name, sheet_name = 'Sheet1')

df['Date']=df['Date'].dt.date
df = df.iloc[-100:] #Select last 100 stats

data = df.pivot("Region", "Date", "Count_Cases")
data = data.fillna(0)
sns.set(font_scale= 1.3)
ax = sns.heatmap(data, linewidths=0, annot=True, vmin=0, vmax=20, 
                 cmap= 'RdYlGn_r', cbar_kws={"shrink": 0.85})  #fmt="d", 

plt.xlabel('Date')
plt.ylabel('Region')


