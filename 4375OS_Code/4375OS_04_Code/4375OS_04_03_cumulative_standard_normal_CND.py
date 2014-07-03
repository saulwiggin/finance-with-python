"""
  Name     : 4375OS_04_03_cumulative_standard_normal_CND.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from math import *
def CND(X):
    """
    Objective: cumulative stardard normal distribution 

    X: input value
    
    e.g., 
          >>> CND(0)
              0.5000000005248086
          >>> CND(1)
              0.8413447404368684
          >>> CND(-1)
              0.15865525956313165
          >>> 1-CND(-1)
              0.8413447404368684
          >>> 
    """
    (a1,a2,a3,a4,a5)=(0.31938153,-0.356563782,1.781477937,-1.821255978,1.330274429)
    L = abs(X)
    K=1.0/(1.0+0.2316419*L)
    w=1.0-1.0/sqrt(2*pi)*exp(-L*L/2.)*(a1*K+a2*K*K+a3*pow(K,3)+a4*pow(K,4)+a5*pow(K,5))
    if X<0:
        w = 1.0-w
    return w

