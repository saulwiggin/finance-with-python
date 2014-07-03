"""
  Name     : 4375OS_08_32_CAPM_beta.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import statsmodels.api as sm
from matplotlib.finance import quotes_historical_yahoo
def ret_f(ticker,begdate, enddate):
    p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
    return((p.aclose[1:] - p.aclose[:-1])/p.aclose[:-1])
begdate=(2013,1,1)
enddate=(2013,11,9)
y=ret_f('IBM',begdate,enddate)
x=ret_f('^GSPC',begdate,enddate)
x=sm.add_constant(x)
model=sm.OLS(y,x)
results=model.fit()
print results.summary()
