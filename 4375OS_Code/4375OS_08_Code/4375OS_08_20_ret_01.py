"""
  Name     : 4375OS_08_20_ret_01.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import numpy as np
p=np.array([1,1.1,0.9,1.05])
ret=(p[:-1]-p[1:])/p[1:]
print p
print(p[:-1])
print(p[1:])
print ret
