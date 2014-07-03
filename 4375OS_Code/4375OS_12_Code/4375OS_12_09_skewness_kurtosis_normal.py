"""
  Name     : 4375OS_12_09_skewness_kurtosis_normal.py
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
from scipy import stats,random
import numpy as np
ret = random.normal(0,1,500000)
print 'mean    =', np.mean(ret)
print 'std     =',np.std(ret)
print 'skewness=',stats.skew(ret)
print 'kurtosis=',stats.kurtosis(ret)
