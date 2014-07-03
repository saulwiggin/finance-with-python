"""
  Name     : 4375OS_08_30_merge_two_datasets_by_date.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
import numpy as np
import pandas as pd
import statsmodels.api as sm
ticker='IBM'
begdate=(2008,10,1)
enddate=(2013,11,9)
x = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)

t=pd.DataFrame(logret,np.array(date,dtype=int64),columns=['ret'])
ret=exp(t.groupby(t.index).sum())-1
ff=pd.load('c:/temp/ffMonthly.pickle')
final=pd.merge(ret,ff,left_index=True,right_index=True)
y=final.ret
x=final[['Mkt_Rf','SMB','HML']]
x=sm.add_constant(x)
results=sm.OLS(y,x).fit()
print results.params