"""
  Name     : 4375OS_08_51_VaR.py
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
from scipy.stats import norm
n_shares=50                      # input 1
confidence_level=0.99            # input 2
n_days=10                        # input 3
z=norm.ppf(confidence_level)
ticker='WMT'
begdate=(2012,1,1)
enddate=(2012,12,31)
x=quotes_historical_yahoo(ticker,begdate,enddate,asobject=True,adjusted=True)
ret = (x.aclose[1:]-x.aclose[:-1])/x.aclose[:-1]
position=n_shares*x.close[0]
VaR=position*z*std(ret)*sqrt(n_days)
print("Holding=",position, "VaR=", round(VaR,4), "in ", n_days, "Days")
