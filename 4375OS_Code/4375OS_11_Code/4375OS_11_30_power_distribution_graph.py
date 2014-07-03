"""
  Name     : 4375OS_11_38_pwer_distribution_graph.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
a = 5.     # shape
n= 1000    # number of random values
s = np.random.power(a, n)
count, bins, ignored = plt.hist(s, bins=30)
x = np.linspace(0, 1, 100)
y = a*x**(a-1.)
smooth_y = n*np.diff(bins)[0]*y
plt.plot(x, smooth_y)
plt.show()