"""
  Name     : 4375OS_07_19_risk_return_graph.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo
stocks = ('IBM', 'DELL', 'WMT', 'C', 'AAPL')
begdate=(2013,1,1)
enddate=(2013,11,30)
def ret_annual(ticker):
    x = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
    logret = log(x.aclose[1:]/x.aclose[:-1])
    return(exp(sum(logret))-1)
def vol_annual(ticker):
    x = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
    ret=(x.aclose[1:]-x.aclose[:-1])/x.aclose[:-1]
    return(std(ret))
ret=[]
vol=[]
for ticker in stocks:
    ret.append(ret_annual(ticker))
    vol.append(vol_annual(ticker))
title('Risk and Return tradeoff')
xlabel("Volatility")
ylabel("Return")
#set_xticklabels(stocks)
plt.scatter(vol,ret,s=200);
plt.show()
