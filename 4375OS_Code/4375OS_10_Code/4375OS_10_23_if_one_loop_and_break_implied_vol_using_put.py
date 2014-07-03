"""
  Name     : 4375OS_10_23_if_one_loop_and_break_implied_vol_using_put.py
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
sigma_old=0.005
sign_1=sign(p-p4f.bs_put(S,K,T,r,sigma_old))
while(1==1):
    sigma=0.0001*(i+1)
    sign_2=sign(p-p4f.bs_put(S,K,T,r,sigma))
    i+=1
    if sign_1*sign_2<0:
        break
    else:
        sigma_old=sigma
print('i, implied-vol, diff')
print(i,(sigma_old+sigma)/2, diff)
