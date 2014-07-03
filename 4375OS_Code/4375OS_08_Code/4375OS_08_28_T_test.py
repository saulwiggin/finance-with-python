"""
  Name     : 4375OS_08_28_T_test.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import stats
from matplotlib.finance import quotes_historical_yahoo
ticker='ibm'
begdate=(2013,1,1)
enddate=(2013,11,9)
p=quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret=(p.aclose[1:] - p.aclose[:-1])/p.aclose[:-1]
print('        Mean        T-value       P-value  '  )
print(round(mean(ret),5), stats.ttest_1samp(ret,0))
