"""
  Name     : 4375OS_09_14_sigma_against_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import p4f as pf
s0=30
T0=0.5
r0=0.05
x0=30
sigma=np.arange(0.05,0.8,0.05)
call=pf.bs_call(s0,x0,T0,r0,sigma)

plot(sigma,call,'b')
show()