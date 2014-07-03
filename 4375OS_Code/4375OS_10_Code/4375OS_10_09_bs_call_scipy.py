"""
  Name     : 4375OS_10_09_bs_call_scipy.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from math import sqrt, log, pi,exp
from scipy.stats import norm

def bs_call(S,X,T,r,sigma):
    """
       Objective: Black-Schole-Merton option model
              S : Stock price
              X : exercise price
              T : maturity date in years
              r : risk-free rate
              sigma: volatility
        Example:
         >>> bs_call2(40,40,1,0.1,0.2)
         5.307874373215604
    """
    d1 = (log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*norm.cdf(d1)-X*exp(-r*T)*norm.cdf(d2)
   
print bs_call(40,40,1,0.1,0.2)