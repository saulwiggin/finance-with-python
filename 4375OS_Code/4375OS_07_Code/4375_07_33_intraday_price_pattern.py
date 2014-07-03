"""
  Name     : 4375OS_07_33_intra_day_price_pattern.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd, numpy as np, datetime 
ticker='AAPL'
path='http://www.google.com/finance/getprices?q=ttt&i=60&p=1d&f=d,o,h,l,c,v'
p=np.array(pd.read_csv(path.replace('ttt',ticker),skiprows=7,header=None))
date=[]
for i in arange(0,len(p)):
    if p[i][0][0]=='a':
        t= datetime.datetime.fromtimestamp(int(p[i][0].replace('a','')))
        date.append(t)
    else:
        date.append(t+datetime.timedelta(minutes =int(p[i][0])))
final=pd.DataFrame(p,index=date)
final.columns=['a','Open','High','Low','Close','Vol']
del final['a']
x=final.index
y=final.Close
title('Intraday price pattern for ttt'.replace('ttt',ticker))
xlabel('Price of stock')
ylabel('Intro-day price pattern')
plot(x,y)
show()



