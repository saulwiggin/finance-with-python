"""
  Name     : 4375OS_08_59_moving_beta.py
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
    return((p.aclose[1:] - p.aclose[0:-1])/p.aclose[:-1])
begdate=(1962,1,1)
enddate=(2013,11,9)
y0=pd.Series(ret_f('IBM',begdate,enddate))
x0=pd.Series(ret_f('^GSPC',begdate,enddate))
model = pd.ols(y=y0, x=x0, window=252)
