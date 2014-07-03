"""
  Name     : 4375OS_07_06_NPV_profile_simple.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
from matplotlib.pyplot import *
cashflows=[-100,50,60,70]
rate=[]
npv=[]
x=(0,0.7)
y=(0,0)
for i in range(1,70):
    rate.append(0.01*i)
    npv.append(sp.npv(0.01*i,cashflows[1:])+cashflows[0])
plot(rate,npv),plot(x,y)
show()
