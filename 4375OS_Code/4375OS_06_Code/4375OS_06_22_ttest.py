"""
  Name     : 4375OS_06_22_ttest.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
from scipy import stats
np.random.seed(124)          # get the same random values
x=np.random.normal(0,1,100)  # mean=0,std=1 
skew=stats.skew(x)           # skewness is -0.2297 
print stats.ttest_1samp(x,0) # if the mean is zero
#(array(1.176), 0.24228)     # T-value and P-value
