"""
  Name     : 4375OS_09_29_binomial_tree_call_option_American.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

# American option 
from math import exp,sqrt
def binomialCallAmerican(s,x,T,r,sigma,n=100):
    deltaT = T /n
    u = exp(sigma * sqrt(deltaT))
    d = 1.0 / u
    v = [[0.0 for j in xrange(i + 1)] for i in xrange(n + 1)]
    a = exp(r * deltaT)
    p = (a - d) / (u - d)
    for j in xrange(i+1):
        v[n][j] = max(s * u**j * d**(n - j) - x, 0.0)
    for i in xrange(n-1, -1, -1):
        for j in xrange(i + 1):
            v1=exp(-r*deltaT)*(p*v[i+1][j+1]+(1.0-p)*v[i+1][j])
            v2=max(x-s,0)
            v[i][j]=max(v1,v2)
    return v[0][0]
