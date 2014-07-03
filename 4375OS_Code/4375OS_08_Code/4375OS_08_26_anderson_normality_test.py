"""
  Name     : 4375OS_08_26_Anderson_normality_test.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
from scipy import stats
ticker='IBM'
begdate=(2013,1,1)
enddate=(2013,11,9)
x = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True,adjusted=True)
ret= (x.aclose[1:]-x.aclose[:-1])/x.aclose[:-1]
print(stats.anderson(ret, dist='norm'))