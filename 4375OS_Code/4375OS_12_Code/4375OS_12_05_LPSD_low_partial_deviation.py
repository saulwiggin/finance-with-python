"""
  Name     : 4375OS_12_05_LPSD_lower_partial_standard_deviation.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
             
"""
from scipy import stats
from matplotlib.finance import quotes_historical_yahoo
import numpy as np
import pandas as pd
ticker='IBM'
begdate=(2009,1,1)
enddate=(2013,12,31)
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = (p.aclose[1:] - p.aclose[:-1])/p.aclose[1:]
date_=p.date
x=pd.DataFrame(data=ret,index=date_[:-1],columns=['ret'])
ff=load('c:/temp/ffDaily.pickle')
final=pd.merge(x,ff,left_index=True,right_index=True)
k=final.ret-final.Rf
k2=k[k>0]
LPSD=np.std(k2)*np.sqrt(252)
print ' LPSD (annualized) for ', ticker, 'is ',round(LPSD,3)