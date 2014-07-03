"""
  Name     : 4375OS_08_12_Series.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x = pd.date_range('1/1/2013', periods=252)
data = pd.Series(randn(len(x)), index=x)
print data.head()
print data.tail()
