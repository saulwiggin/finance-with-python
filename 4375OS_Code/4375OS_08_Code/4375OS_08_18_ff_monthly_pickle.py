"""
  Name     : 4375OS_08_08_ff_monthly_pickle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
file=open("c:/temp/ff_monthly.txt","r")
data=file.readlines()
f=[]
index=[]
for i in range(4,size(data)):
       t=data[i].split()
       index.append(int(t[0]))
       for j in range(1,5):
           k=float(t[j])
           f.append(k/100)
n=len(f)       
f1=np.reshape(f,[n/4,4])
ff=pd.DataFrame(f1,index=index,columns=['Mkt_Rf','SMB','HML','Rf'])
ff.to_pickle("c:/temp/ffMonthly.pickle")
ff.head()
