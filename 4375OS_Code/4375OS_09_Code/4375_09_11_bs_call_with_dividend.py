"""
  Name     : 4375OS_09_11_bs_call_with_dividend.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import log,exp,sqrt,stats
def bs_call_div(S0,X,T,r,sigma,d1,T1):
    """Objective: estimate call for stock with one known dividend
       S0: current stock price
       T : maturity date in years
       r : risk-free rate
       sigma: volatility
       d1: dividend
       T1: dividend date T1<T
    """
    S=s0-exp(-r*T*d1)
    d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)

S0=40.
d=1.5
r=0.015
T1=1./12.
T=6./12.
x=42.
sigma=0.2
print bs_call_div(S0,x,T,r,sigma,d,T1)