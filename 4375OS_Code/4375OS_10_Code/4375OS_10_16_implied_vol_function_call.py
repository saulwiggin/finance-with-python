"""
  Name     : 4375OS_10_16_implied_vol_function_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def implied_vol_call(S,X,T,r,c):
    """Objective: estimate implied volatility based on call
          S   : current stock price
          T   : maturity date in years
          r   : risk-free rate
       sigma  : volatility
        c     : call price
      Example :
       >>> implied_vol_call(40,40,1.,0.1,5.31)
       (39, 0.2, 0.0021293661356418525)
       >>>         
    """
    from scipy import log,exp,sqrt,stats
    for i in range(200):
        sigma=0.005*(i+1)
        d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
        d2 = d1-sigma*sqrt(T)
        diff=c-(S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2))
        if abs(diff)<=0.01:
            return i,sigma, diff
