"""
  Name     : 4375OS_07_21_risk_return_graph2.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
from matplotlib.finance import quotes_historical_yahoo
stocks = ('IBM', 'GE', 'WMT', 'C', 'AAPL')
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
labels = ['{0}'.format(i) for i in stocks]
plt.subplots_adjust(bottom = 0.1)
color=np.array([ 0.18,  0.96,  0.75,  0.3,  0.9])
plt.scatter(vol, ret, marker = 'o',  c=color,s = 1000,
    cmap = plt.get_cmap('Spectral'))
for label, x, y in zip(labels, vol, ret):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
plt.title('Return-volatility 2-dimentional graph')
plt.xlabel('Volatility (annualized)')
plt.ylabel('Return (annualized)')
plt.show()
