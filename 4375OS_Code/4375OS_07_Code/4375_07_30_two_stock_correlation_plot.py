"""
  Name     : 4375OS_07_30_two_stock_correlation_plot.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.pyplot import *
from matplotlib.finance import quotes_historical_yahoo
import numpy as np
def ret_f(ticker,begdate,enddate):
            p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
            return((p.open[1:] - p.open[:-1])/p.open[1:])
begdate=(2013,1,1)
enddate=(2013,2,9)
ret1=ret_f('IBM',begdate,enddate)
ret2=ret_f('^GSPC',begdate,enddate)
n=min(len(ret1),len(ret2))
s=np.ones(n)*2
t=range(n)
line=np.zeros(n)

plot(t,ret1[0:n], 'ro',s )
plot(t,ret2[0:n], 'bd',s)
plot(t,line,'b',s)

figtext(0.4,0.8,"Red for IBM, Blue for S&P500")
xlim(1,n)
ylim(-0.04,0.07)
title("Comparions between stock and market retuns")
xlabel("Day")
ylabel("Returns")
show()


