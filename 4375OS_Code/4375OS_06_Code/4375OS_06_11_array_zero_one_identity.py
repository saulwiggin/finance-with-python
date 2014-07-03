"""
  Name     : 4375OS_06_11_array_zeros_ones_identity.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import numpy as np
a=np.zeros(10)                #  array with 10 zeros
print a

b=np.zeros((3,2),dtype=float) #  3 by 2 with zeros
print b

c=np.ones((4,3),float)        #  4 by 3 with all ones
print c

d=np.array(range(10),float)   #  0,1, 2,3 .. up to 9
print d

e1=np.identity(4)             #  identity 4 by 4 matrix
print e1

e2=np.eye(4)                  #  same as above
print e2

e3=np.eye(4,k=1)              #  1 start from k  
print e3

f=np.arange(1,20,3,float)     #  from 1 to 19 interval 3
print f

g=np.array([[2,2,2],[3,3,3]]) #  2 by 3
print g

h=np.zeros_like(g)            #  all zeros
print h

i=np.ones_like(g)            #  all ones
print i


