"""
  Name     : 4375OS_10_37_volatility_skewness.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from pandas.io.data import Options
def implied_vol_call_min(S,X,T,r,c):
    """Objective: estimate implied volatility based on call
          S   : current stock price
          T   : maturity date in years
          r   : risk-free rate
       sigma  : volatility
        c     : call price
    """
    from scipy import log,exp,sqrt,stats
    implied_vol=1.0
    min_value=1000
    for i in range(10000):
        sigma=0.0001*(i+1)
        d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
        d2 = d1-sigma*sqrt(T)
        c2=S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)
        abs_diff=abs(c2-c)
        #print 'i=',i,'c=', c,'c2=',c2,'abs_diff=',abs_diff,'min_value=',min_value
        if abs_diff<min_value:
            min_value=abs_diff
            implied_vol=sigma
            k=i
    return implied_vol
    
ticker='IBM'
m=2
y=2014
s=185.08
r=0.0003
T=2./12.0
x = Options(ticker,'yahoo')
puts,calls = x.get_options_data(month=m,year=y)
print 'done'

n=len(calls.Strike)
for i in range(n):
    x=calls.Strike[i]
    c=(calls.Bid[i]+calls.Ask[i])/2.0
    if c >0:
        vol=implied_vol_call_min(s,x,T,r,c)
        print x,c,vol
    