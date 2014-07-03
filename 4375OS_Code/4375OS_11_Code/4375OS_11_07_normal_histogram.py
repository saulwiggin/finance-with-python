"""
  Name     : 4375OS_11_07_normal_histogram.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
import matplotlib.pyplot as plt
sp.random.seed(12345)
x=sp.random.normal(0.08,0.2,1000)
plt.hist(x, 15, normed=True)
plt.show()
    
    
    
    
