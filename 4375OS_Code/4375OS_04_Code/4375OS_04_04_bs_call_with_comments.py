"""
  Name     : 4375OS_04_04_bs_with_comments.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from math import log,sqrt, exp,pi

def bs_call(S,X,T,r,sigma):
    """
  Objective: estimate a call option based on the Black-Scholes model
   
   S    : current stock price
   X    : exercise price
   T    : maturity date in years
   r    : risk-free compounded continuously
   sigma: volatility 

   Note : assume that the CND function is available
   e.g., 
        >>> bs_call(40,40,0.5,0.03,0.2)
            2.5484087180803208
        >>> bs_call(10,12,1,0.03,0.23)
            0.37646153125346604
        >>> 

    """
    d1 = (log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*CND(d1)-X*exp(-r*T)*CND(d2)

# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# Cumulative standard normal distribution 
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
def CND(X):
    (a1,a2,a3,a4,a5)=(0.31938153,-0.356563782,1.781477937,-1.821255978,1.330274429)
    L = abs(X)
    K=1.0/(1.0+0.2316419*L)
    w=1.0-1.0/sqrt(2*pi)*exp(-L*L/2.)*(a1*K+a2*K*K+a3*pow(K,3)+a4*pow(K,4)+a5*pow(K,5))
    if X<0:
        w = 1.0-w
    return w

