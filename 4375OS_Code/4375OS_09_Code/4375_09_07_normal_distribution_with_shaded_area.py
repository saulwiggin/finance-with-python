"""
  Name     : 4375OS_09_06_normal_distrition_with_shaded_area.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
from scipy import exp,sqrt,stats
from matplotlib import pyplot as plt
z=0.325

def f(t):
    return stats.norm.pdf(t)

ylim(0,0.45)
x = np.arange(-3,3,0.1)
y1=f(x)
plt.plot(x,y1)
x2= np.arange(-4,z,1/40.)
plt.annotate('z= '+str(z),xy=(z,0.01))
plt.fill_between(x2,f(x2))
plt.show()