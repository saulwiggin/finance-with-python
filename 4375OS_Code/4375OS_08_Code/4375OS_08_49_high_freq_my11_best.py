"""
  Name     : 4375OS_08_49_high_frequency_my11_best.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd, numpy as np, datetime 
ticker='AAPL'
path='http://www.google.com/finance/getprices?q=ttt&i=60&p=5d&f=d,o,h,l,c,v'
x=np.array(pd.read_csv(path.replace('ttt',ticker),skiprows=7,header=None))
date=[]
for i in arange(0,len(x)):
    if x[i][0][0]=='a':
        t= datetime.datetime.fromtimestamp(int(x[i][0].replace('a','')))
        print ticker, t, x[i][1:]
        date.append(t)
    else:
        date.append(t+datetime.timedelta(minutes =int(x[i][0])))
final=pd.DataFrame(x,index=date)
final.columns=['a','Open','High','Low','Close','Vol']
del final['a']
final.to_csv('c:/temp/abc.csv'.replace('abc',ticker))

  

