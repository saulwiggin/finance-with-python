"""
  Name     : 4375OS_11_19_daily_to_annual.py
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
ticker='IBM'           # input value 1
begdate=(1926,1,1)     # input value 2
enddate=(2013,12,31)   # input value 3
n_forecast=15.         # input value 4

def geomean_ret(returns):
    product = 1
    for ret in returns:
        product *= (1+ret)
    return product ** (1.0/len(returns))-1

x=quotes_historical_yahoo(ticker,begdate,enddate,asobject=True,adjusted=True)
logret = log(x.aclose[1:]/x.aclose[:-1])
date=[]
d0=x.date
for i in range(0,size(logret)):
    date.append(d0[i].strftime("%Y"))
y=pd.DataFrame(logret,date,columns=['logret'],dtype=float64)
ret_annual=exp(y.groupby(y.index).sum())-1
ret_annual.columns=['ret_annual']

n_history=len(ret_annual)
a_mean=mean(np.array(ret_annual))
g_mean=geomean_ret(np.array(ret_annual))
future_ret=n_forecast/n_history*g_mean+(n_history-n_forecast)/n_history*a_mean
print 'Arithmetric mean=',round(a_mean,3), 'Geomean=',round(g_mean,3),'forecast=',future_ret