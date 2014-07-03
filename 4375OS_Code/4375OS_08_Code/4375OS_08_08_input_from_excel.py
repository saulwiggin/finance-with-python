"""
  Name     : 4375OS_08_08_input_from_excel.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
infile=pd.ExcelFile('c:/temp/test.xlsx')
x=infile.parse('Sheet1',header=None)