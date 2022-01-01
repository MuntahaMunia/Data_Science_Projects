# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 17:48:18 2022

@author: Munia's PC
"""

import win32com.client as win32
import os,time,pathlib
import pandas as pd
import numpy as np
import cx_Oracle
from datetime import datetime
from shareplum import datetime
from shareplum import Office365
from shareplum.site import Version

connection = cx_Oracle.connect(
    user ="xxx"
    password = "xxxx"
    dsn ="OracelServerName")
print("Successfully connected to Oracle Database")

query1 = """
select * from Table1
"""
query2 = """
select * from Table2
"""
 
DF1 = pd.read_sql(query1, con = connection)
print(DF1)

DF2 = pd.read_sql(query2, con = connection)
print(DF2)


date = datetime.today().strftime('%Y-%m-%d')

with pd.ExcelWriter(r'path to where to save the file.xlsx', engine = 'xlsxwriter') as writer:
    DF1.to_excel(writer,sheet_name='Tab name', index=False)
    DF2.to_excel(writer,sheet_name='Tab name', index=False)
    

outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'muntaha.munia@outlook.com'
mail.Subject = "Sample Email "+datetime.today().strftime('%Y-%m-%d')
mail.HTMLBody = '''\
        <html>
            <head></head>
            <body>
                <p>Hello Muntaha,<br><br>
                
                     <p>Please see the attached file.<br>
                     <br> Thanks and Best Regards,
                     <br>Muntaha Munia<br><br>
                     <front colog = "red">
                     Please note, this is an automated email, do not reply.<t1>
                     </front>
                 </p> 
             </body>
             </style>
         </html>   
         '''
mail.Attachements.Add(r'path to where to save the file.xlsx')
From = 'muntaha.munia@outlook.com'
mail.Send()
    
authcookie = Office365('sharepoint link', username = 'xxx' , password = 'xxxx').GetCookies()
site = Site('Sharepoint location', version = Version.v365 , authcookie=authcookie);
folder = site.folder('folder name in sharepoint')
with open(r"path to where to save the file_{}.xlsx".format(date),mode = 'rb') as file:
    fileContent = file.read()
folder.upload_file(fileContent, "file name_{}.xlsx".format(date))