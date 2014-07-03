"""
  Name     : 4375OS_11_02_random_numbers_normal_with_seed.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
sp.random.seed(123345)
for i in range(10):
    print sp.random.normal()