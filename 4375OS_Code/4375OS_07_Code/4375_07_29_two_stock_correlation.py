"""
  Name     : 4375OS_07_29_two_stock_correlation.py
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

begdate=(2013,1,1)
enddate=(2013,12,9)

ticker='IBM'
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = (p.open[1:] - p.open[:-1])/p.open[1:]
ticker='DELL'
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret2 = (p.open[1:] - p.open[:-1])/p.open[1:]

n=min(len(ret),len(ret2))

print np.corrcoef(ret[:n],ret2[:n])
