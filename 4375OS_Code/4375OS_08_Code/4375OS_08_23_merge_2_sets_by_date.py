"""
  Name     : 4375OS_08_23_merge_2_sets_by_date.py
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
ticker='IBM'
begdate=(2013,10,1)
enddate=(2013,11,9)
x = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
k=x.date
date=[]
for i in range(0,size(x)):
    date.append(''.join([k[i].strftime("%Y"),k[i].strftime("%m"),k[i].strftime("%d")]))

x2=pd.DataFrame(x['aclose'],np.array(date,dtype=int64),columns=[ticker+'_adjClose'])
ff=pd.load('c:/temp/ff_daily.pickle')
final=pd.merge(x2,ff,left_index=True,right_index=True)