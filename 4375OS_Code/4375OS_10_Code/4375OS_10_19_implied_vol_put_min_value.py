"""
  Name     : 4375OS_10_19_implied_vol_put_min_value.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def implied_vol_put_min(S,X,T,r,p):
    """Objective: estimate implied volatility based on call
          S   : current stock price
          T   : maturity date in years
          r   : risk-free rate
       sigma  : volatility
        p     : put price
    """
    from scipy import log,exp,sqrt,stats
    implied_vol=1.0
    min_value=1000.
    for i in range(10000):
        sigma=0.0001*(i+1)
        d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
        d2 = d1-sigma*sqrt(T)
        put=X*exp(-r*T)*stats.norm.cdf(-d2)-S*stats.norm.cdf(-d1)
        abs_diff=abs(put-p)
        if abs_diff<=min_value:
            min_value=abs_diff
            implied_vol=sigma
            k=i
    print 'k, implied_vol, put, abs_diff'
    return k,implied_vol, put,abs_diff
