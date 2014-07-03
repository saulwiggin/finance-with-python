"""
  Name     : 4375OS_08_40_Pastor_Stambaugh.py
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
begdate=(2013,1,1)
enddate=(2013,1,31)
data = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = (data.aclose[1:]-data.aclose[:-1])/data.aclose[:-1]
dollar_vol=np.array(data.aclose[1:])*np.array(data.volume[1:])
date=[]
d0=data.date
for i in range(0,size(ret)):
    date.append(''.join([d0[i].strftime("%Y"),d0[i].strftime("%m"),d0[i].strftime("%d")]))
tt=pd.DataFrame(ret,np.array(date,dtype=int64),columns=['ret'])
tt2=pd.DataFrame(dollar_vol,np.array(date,dtype=int64),columns=['dollar_vol'])
ff=pd.load('c:/temp/ffDaily.pickle')
tt3=pd.merge(tt,tt2,left_index=True,right_index=True)
final=pd.merge(tt3,ff,left_index=True,right_index=True)
y=final.ret[1:]-final.Rf[1:]
x1=final.Mkt_Rf[:-1]
x2=sign(np.array(final.ret[:-1]-final.Rf[:-1]))*np.array(final.dollar_vol[:-1])
x3=[x1,x2]
n=size(x3)
x=np.reshape(x3,[n/2,2])
x=sm.add_constant(x)
results=sm.OLS(y,x).fit()
print results.params