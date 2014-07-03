"""
  Name     : 4375OS_04_01_bs_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from math import *

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
