"""
  Name     : 4375OS_06_24_optimization.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import scipy.optimize as optimize 
def my_f(x):
    return 3 + x**2
    
optimize.fmin(my_f,5)   # 5 is initial value

