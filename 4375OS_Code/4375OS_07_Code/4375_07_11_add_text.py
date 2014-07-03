"""
  Name     : 4375OS_07_11_add_text.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from pylab import *
x = [0,1,2]
y = [2,4,6]
plot(x,y)
figtext(0.2, 0.7, 'North & West')
figtext(0.7, 0.2, 'East & South')
show()
