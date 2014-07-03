"""
  Name     : 4375OS_06_19_logic_array.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
x=np.array([True,False,True,False],bool)
a=any(x)  	# if one item is TRUE then return TRUE
print a

b=all(x)  	# if all are TRUE then return TRUE
print b

cashFlows=np.array([-100,50,40,30,100,-5])
a=cashFlows>0  # [False,True,True,True,True,False]
print a

d=np.logical_and(cashFlows>0, cashFlows<60)
print d

