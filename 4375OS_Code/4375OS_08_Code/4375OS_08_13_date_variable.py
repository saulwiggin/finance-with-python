"""
  Name     : 4375OS_08_13_date_variable.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
url='http://chart.yahoo.com/table.csv?s=IBM'
x=pd.read_csv(url,index_col=0,parse_dates=True) 
print x.head()
