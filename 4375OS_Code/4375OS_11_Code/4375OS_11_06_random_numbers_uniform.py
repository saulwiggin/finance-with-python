"""
  Name     : 4375OS_11_06_random_numbers_uniform.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

# generate 10 numbers betweeen 1 and 100

import scipy as sp
sp.random.seed(123345)
x=sp.random.uniform(low=1,high=100,size=10)

print x[0:5]