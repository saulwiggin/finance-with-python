"""
  Name     : 4375OS_06_03_npv_f_scipy.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
cashflows=[50,40,20,10,50]
npv=sp.npv(0.1,cashflows) #estimate NPV 
print round(npv,2)

