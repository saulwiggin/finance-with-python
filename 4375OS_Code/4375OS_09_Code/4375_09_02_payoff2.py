"""
  Name     : 4375OS_09_02_payoff2.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

s = arange(10,80,5)
x=30
y=(abs(s-x)+s-x)/2
ylim(-10,50)
plot(s,y)
show()




