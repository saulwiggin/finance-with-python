"""
  Name     : 4375OS_12_10_skewness_kurtosis_SP500.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
             
             
       Table 1: Descriptive Statistics for S&P Daily Return Data (1927 ~ 2008)
Sample Number       20,319
Mean               0.026%
Standard Deviation 1.182%
Kurtosis           18.347
Skewness             -0.098
Maximum Daily Return 16.61%
Minimum Daily Return -20.47%
                         
"""
from scipy import stats
from matplotlib.finance import quotes_historical_yahoo
import numpy as np
ticker='^GSPC'
begdate=(1926,1,1)
enddate=(2013,12,31)
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = (p.aclose[1:] - p.aclose[:-1])/p.aclose[1:]
print 'S&P500  n       =',len(ret)
print 'S&P500  mean    =',round(np.mean(ret),8)
print 'S&P500  std     =',round(np.std(ret),8)
print 'S&P500  skewness=',round(stats.skew(ret),8)
print 'S&P500  kurtosis=',round(stats.kurtosis(ret),8)