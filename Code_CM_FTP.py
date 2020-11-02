# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:47:16 2020

@author: radmehr.a
"""

import os
import ftplib
import re

ftp = ftplib.FTP('11.111.111.111', 'FTP', 'ABCD')
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


file2 = open(r"D:\CHR\Huawei\CM\Site_List_2.txt",'w')
for i in data:
    i = i.replace('CMExport_', '').replace('.xml', '').replace(',', '_')
    file2.write(i)
    file2.write('\n')

file1.close()
file2.close()
os.chdir
