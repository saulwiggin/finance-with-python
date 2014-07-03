"""
  Name     : 4375OS_11_35_boostrapping_01.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
x=range(1,11)
print x

for i in range(5):
    y=np.random.permutation(x)
    print y
