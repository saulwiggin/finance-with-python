"""
  Name     : 4375OS_06_21_generate_random_numbers.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp

x=sp.random.rand(10) 	      # 10 random numbers from [0,1)
y=sp.random.rand(5,2)        # random numbers 5 by 2 array
z=sp.random.normal(0,1,100)  # from a standard normal

print 'x=',x
print 'y=',y
print 'z=',z
