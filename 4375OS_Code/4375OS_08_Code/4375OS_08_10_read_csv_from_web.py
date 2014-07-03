"""
  Name     : 4375OS_08_10_read_from_web.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import pandas as pd
x=pd.read_csv("http://chart.yahoo.com/table.csv?s=IBM")
print x.head()
