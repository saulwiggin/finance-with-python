"""
  Name     : 4375OS_12_11_volatility_clustering_SP500.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
import numpy as np
ticker='^GSPC'
begdate=(1987,11,1)
enddate=(2006,12,31)
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = (p.aclose[1:] - p.aclose[:-1])/p.aclose[1:]
title('Illustration of volatility clustering (S&P500)')
ylabel('Daily returns')
xlabel('Date')
x=p.date[1:]
plot(x,ret)
