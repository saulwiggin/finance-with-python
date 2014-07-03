"""
  Name     : 4375OS_08_61_minimization_01.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy.optimize import minimize
def y_f(x):
    return (3+2*x**2)
x0=100
res = minimize(y_f,x0,method='nelder-mead',options={'xtol':1e-8,'disp': True})
print(res.x) 