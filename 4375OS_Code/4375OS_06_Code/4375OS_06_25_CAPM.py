"""
  Name     : 4375OS_06_25_CAPM.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import stats
stock_ret = [0.065, 0.0265, -0.0593, -0.001,0.0346]
mkt_ret  = [0.055, -0.09, -0.041,0.045,0.022]
beta, alpha, r_value, p_value, std_err =stats.linregress(stock_ret,mkt_ret)

print 'beta=',beta,'alpha=',alpha

