"""
  Name     : 4375OS_06_03_bs_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import log,exp,sqrt,stats
def bs_call(S,X,T,r,sigma):
    """
    Objective: estimate Black-Scholes-Merton call price
    S: stock price
    X: exercise price
    T: maturity date in years
    r: risk-free rate
    sigma: standard deviation of returns
    
    Example:
    >>>print bs_call(20,20,0.5,0.05,0.15)
    1.10542302373
    """
    d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)
    