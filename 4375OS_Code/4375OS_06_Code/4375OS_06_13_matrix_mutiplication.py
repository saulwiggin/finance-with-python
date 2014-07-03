"""
  Name     : 4375OS_06_13_matrix_multiplication.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np

x=np.array([[1,2,3],[4,5,6]],float)      # 2 by 3

y=np.array([[1,2],[3,3],[4,5]],float)    # 3 by 2

xy=np.dot(x,y)                           # 2 by 2

print x
print y
print xy