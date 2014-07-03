"""
  Name     : 4375OS_08_21_daily_ret_to_monthly.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
import numpy as np
import pandas as pd
ticker='IBM'
begdate=(2013,1,1)
enddate=(2013,11,9)
x = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
logret = log(x.aclose[1:]/x.aclose[:-1])
yyyymm=[]
d0=x.date
for i in range(0,size(logret)):
    yyyymm.append(''.join([d0[i].strftime("%Y"),d0[i].strftime("%m")]))
y=pd.DataFrame(logret,yyyymm,columns=['ret_monthly'])
ret_monthly=y.groupby(y.index).sum()
print ret_monthly.head()

