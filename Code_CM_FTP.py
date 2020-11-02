# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:47:16 2020

@author: radmehr.a
"""


import os
import ftplib
import re

ftp = ftplib.FTP('10.130.200.133', 'ftpuser', 'Changeme_123')
ftp.cwd("/opt/oss/server/var/fileint/cm/autoExport")   
regex = re.compile(r'([A-Z]{1}\d{4})',re.IGNORECASE)

data = []

for i in ftp.nlst():
    if regex.findall(i) != []:
        data.append(i)

file1 = open(r"D:\CHR\Huawei\CM\Site_List_2.txt",'w')

for i in data:
    i = i.replace('MeContext=','')
    file1.write(i)
    file1.write('\n')

"""
os.chdir(r"D:\CHR\Huawei\CM\Site_List_2.txt")
for filename in (r"D:\CHR\Huawei\CM\Site_List_2.txt"):
    os.rename(filename, filename.replace('CMExport_', ''))
"""



file2 = open(r"D:\CHR\Huawei\CM\Site_List_2.txt",'w')
for i in data:
    i = i.replace('CMExport_', '').replace('.xml', '').replace(',', '_')
    file2.write(i)
    file2.write('\n')

"""    
for j in data:
    j = j.replace('.xml', '')
    file2.write(i)
    file2.write(j)
    file2.write('\n')
"""
    
"""
rootdir = r'D:\CHR\Huawei\CM\Site_List_2.txt'
str = str.replace("CMExport_","")
for filename in os.listdir(rootdir):
    if str in filename:    
        filepath = os.path.join(rootdir, filename)
        newfilepath = os.path.join(rootdir, filename.replace(str, ""))
        os.rename(filepath, newfilepath)
"""

file1.close()
file2.close()
#file3.close()
os.chdir