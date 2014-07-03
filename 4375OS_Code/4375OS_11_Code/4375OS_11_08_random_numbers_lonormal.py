"""
  Name     : 4375OS_11_08_random_lognormal.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
sp.random.seed(12345)
x=sp.random.lognormal(0,1,100)

print x[0:5]

    
    
