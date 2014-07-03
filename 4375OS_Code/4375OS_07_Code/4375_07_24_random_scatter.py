"""
  Name     : 4375OS_07_24_random_scatter.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from pylab import *
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
scatter(X,Y)
show()
