"""
  Name     : 4375OS_10_25_impliws_col_using_put.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import p4f 
S=40;K=40;T=0.5;r=0.05;sigma=0.2;p=1.77
diff=1;i=1
while abs(diff)>0.01:
    sigma=0.005*(i+1)
    diff=p-p4f.bs_put(S,K,T,r,sigma)
    i+=1
print('i, implied-vol, diff')
print(i,sigma, diff)
