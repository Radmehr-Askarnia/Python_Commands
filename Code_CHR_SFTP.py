# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:25:55 2020

@author: radmehr.a  ------SFTP by pysftp --> not Working
"""

import os
import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None    # disable host key checking.

sftp = pysftp.Connection(host='11.111.111.111', username='FTP', password='ABCD', cnopts=cnopts)
sftp.cwd('/export/home/omc/var/fileint/TSNBI/UMTS_PCHR/20200609/MSRNCH05')
#regex = re.compile(r'([A-Z]{1}\d{4})',re.IGNORECASE)
for attr in sftp.listdir_attr():
    print (attr.filename, attr)
    
data = []
for i in sftp.listdir():
    #if regex.findall(i) != []:
        data.append(i)
    
file1 = open(r"D:\CHR\Huawei\CHR\Sites.txt",'w') # Open file to write H LTE

for i in data:# folder_list: #range(len(folder_list[:])):
    i = i.replace('MeContext=','')
    file1.write(i)
    file1.write('\n')
    
file1.close()
os.chdir
