"""
  Name     : 4375OS_09_06_normal_graph.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import exp,sqrt,stats
x = arange(-3,3,0.1)
y=stats.norm.pdf(x)
plot(x,y)
show()
