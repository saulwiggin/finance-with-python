"""
  Name     : 4375OS_06_12_array_manipulation.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
pv=np.array([[100,10,10.2],[34,22,34]]) # 2 by 3
x=pv.flatten()                          #  matrix becomes a vector
pv2=np.reshape(x,[3,2])                 # 3 by 2 now

print pv
print x
print pv2
