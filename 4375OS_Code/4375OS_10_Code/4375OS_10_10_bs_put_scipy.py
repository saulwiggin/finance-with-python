"""
  Name     : 4375OS_10_10_bs_put_scipy.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
from math import sqrt, log, pi,exp
from scipy.stats import norm
def bs_put(S,X,T,r,sigma):
    """
       Objective: Black-Schole-Merton option model
              S : stock price
              X : exericse price
              T : maturity date
              r : risk-free rate
              p : price of a put option 
        Example :
       >>> put=bs_put(40,40,1,0.1,0.2)
       >>> round(put,3)
       1.501
    """
    d1 = (log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return X*exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)

put=bs_put(40,40,1,0.1,0.2)
print round(put,3)