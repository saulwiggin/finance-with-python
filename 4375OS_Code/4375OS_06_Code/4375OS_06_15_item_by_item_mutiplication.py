"""
  Name     : 4375OS_06_15_item_by_item_multiplication.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
x=np.array([[1,2,3],[4,5,6]],float)    # 2 by 3
y=np.array([[2,1,2],[4,0,5]],float)    # 2 by 3
xy=x*y                                 # 2 by 3

print x
print y
print xy
