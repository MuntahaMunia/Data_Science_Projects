# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 17:01:07 2022

@author: Munia's PC
"""

import win32com.client as win32
import os,time,pathlib
import pandas as pd
import numpy as np
import cx_Oracle
from datetime import datetime

connection = cx_Oracle.connect(
    user ="xxx"
    password = "xxxx"
    dsn ="OracelServerName")
print("Successfully connected to Oracle Database")

query1 = """
select * from Table
"""
DF = pd.read_sql(query1, con = connection)
print(DF)
with pd.ExcelWriter(r'path to where to save the file.xlsx', engine = 'xlsxwriter') as writer:
    DF.to_excel(writer,sheet_name='file name', index=False)
    
def DF():
    outlook = win32.Dispatch('outlook.application')
    """
    file = pathlib.Path("file.xlsx")
    """
    
    if 1 == 1:
        body = '''\
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
         
         mail = outlook.CreateItem(0)
         mail.subject = "Sample Email "+datetime.today().strftime('%Y-%m-%d')
         mail.to = 'muntaha.munia@outlook.com'
         mail.HTMLBody = body
         mail.Attachements.Add(r'path to where to save the file.xlsx')
         From = 'muntaha.munia@outlook.com'
         
         mail.Send()
    else:
        print("condition not met")
        
DF()
    