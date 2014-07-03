"""
  Name     : 4375OS_08_50_January_effect.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
import numpy as np
import scipy as sp
from datetime import datetime
ticker='IBM'
begdate=(1962,1,1)
enddate=(2013,11,22)
x = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
logret = log(x.aclose[1:]/x.aclose[:-1])
date=[]
d0=x.date
for i in range(0,size(logret)):
    t1=''.join([d0[i].strftime("%Y"),d0[i].strftime("%m"),"01"])
    date.append(datetime.strptime(t1,"%Y%m%d"))
y=pd.DataFrame(logret,date,columns=['logret'])
retM=y.groupby(y.index).sum()
ret_Jan=retM[retM.index.month==1]
ret_others=retM[retM.index.month!=1]
print(sp.stats.bartlett(ret_Jan.values,ret_others.values))
#(1.1592293088621082, 0.28162543233634485)