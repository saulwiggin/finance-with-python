"""
  Name     : 4375OS_08_22_daily_to_annual.py
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
begdate=(1990,1,1)
enddate=(2012,12,31)
x=quotes_historical_yahoo(ticker,begdate,enddate,asobject=True,adjusted=True)
logret = log(x.aclose[1:]/x.aclose[0:-1])
date=[]
d0=x.date
for i in range(0,size(logret)):
    date.append(d0[i].strftime("%Y"))
y=pd.DataFrame(logret,date,columns=['ret_annual'])
ret_annual=exp(y.groupby(y.index).sum())-1

print ret_annual.head()
