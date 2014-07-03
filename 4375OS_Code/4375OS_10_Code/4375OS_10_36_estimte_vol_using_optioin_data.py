"""
  Name     : 4375OS_10_36_volatility_skewness.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from pandas.io.data import Options
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
            return sigma

ticker='IBM'
m=2
y=2014
s=185.08
x = Options(ticker,'yahoo')
calls, puts = x.get_options_data(month=m,year=y)
print 'done'

n=len(calls.Strike)
for i in range(n):
    x=calls.Strike[i]
    c=(calls.Bid[i]+calls.Ask[i])/2.0
    if c >0:
        vol=implied_vol_call(s,x,2./12.,0.03,c)
        print x,c,vol
    