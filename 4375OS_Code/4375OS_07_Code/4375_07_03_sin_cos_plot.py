"""
  Name     : 4375OS_07_03_sin_cos_plot.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from pylab import *
x = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(x), np.sin(x)
plot(x,C),plot(x,S)
show()
