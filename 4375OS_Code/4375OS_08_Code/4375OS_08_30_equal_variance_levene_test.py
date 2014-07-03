"""
  Name     : 4375OS_08_30_equal_variance_levene_test.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
from matplotlib.finance import quotes_historical_yahoo

begdate=(2013,1,1)
enddate=(2013,11,9)
def ret_f(ticker,begdate,enddate):
     p = quotes_historical_yahoo(ticker,begdate, enddate,asobject=True,adjusted=True)
     return((p.open[1:] - p.open[:-1])/p.open[1:])
y=ret_f('IBM',begdate,enddate)
x=ret_f('DELL',begdate,enddate)
print(sp.stats.bartlett(x,y))



