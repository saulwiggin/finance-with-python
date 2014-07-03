"""
  Name     : 4375OS_08_60_moving_beta_annual.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib.finance import quotes_historical_yahoo
def ret_f(ticker,begdate, enddate):
    p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
    return((p.aclose[1:] - p.aclose[:-1])/p.aclose[:-1])
begdate=(1962,1,1)
enddate=(2013,11,9)
y0=pd.Series(ret_f('IBM',begdate,enddate))
x0=pd.Series(ret_f('^GSPC',begdate,enddate))
d=quotes_historical_yahoo('^GSPC', begdate, enddate,asobject=True, adjusted=True).date[0:-1]
lag_year=d[0].strftime("%Y")
y1=[]
x1=[]
beta=[]
index0=[]
for i in range(1,len(d)):
    year=d[i].strftime("%Y")
    if(year==lag_year):
        x1.append(x0[i])
        y1.append(y0[i])
    else:
        model=pd.ols(y=pd.Series(y1),x=pd.Series(x1))  
        print(lag_year, round(model.beta[0],4))
        beta.append(model.beta[0])
        index0.append(lag_year)
        x1=[]
        y1=[]
        lag_year=year
