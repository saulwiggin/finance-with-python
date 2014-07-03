"""
  Name     : 4375OS_10_39_implied_vol_American_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
             
   >>> binomialCallAmerican(s,150,2./12.,0.003,0.2)
   35.17513170782366
   >>> binomialCallAmerican(s,160,2./12.,0.003,0.2)
   25.3618113670993
   >>> 
"""
from pandas.io.data import Options
from math import exp,sqrt
import urllib
import re

def binomialCallAmerican(s,x,T,r,sigma,n=100):
    deltaT = T /n
    u = exp(sigma * sqrt(deltaT))
    d = 1.0 / u
    a = exp(r * deltaT)
    p = (a - d) / (u - d)
    v = [[0.0 for j in xrange(i + 1)] for i in xrange(n + 1)]
    for j in xrange(i+1):
        v[n][j] = max(s * u**j * d**(n - j) - x, 0.0)
    for i in xrange(n-1, -1, -1):
        for j in xrange(i + 1):
            v1=exp(-r*deltaT)*(p*v[i+1][j+1]+(1.0-p)*v[i+1][j])
            v2=max(x-s,0)
            v[i][j]=max(v1,v2)
    return v[0][0]

def implied_vol_American_call(s,x,T,r,c):
    implied_vol=1.0
    min_value=1000
    for i in range(1000):
        sigma=0.001*(i+1)
        c2=binomialCallAmerican(s,x,T,r,sigma)
        abs_diff=abs(c2-c)
        if abs_diff<min_value:
            min_value=abs_diff
            implied_vol=sigma
            k=i
        #print 'i=',i,'c=', c,'c2=',c2,'k=',k,'min_value=',min_value
    return implied_vol        

def today_price(ticker):
    file = urllib.urlopen("http://finance.yahoo.com/q?s=" +ticker+"&ql=1")
    text = file.read()
    pattern='<span id="yfs_l84_' + ticker + '">(.+?)</span>'
    return re.findall(re.compile(pattern), text)
          
ticker='ibm'
m=2
y=2014 #numpy.float64(
s=np.float64(today_price(ticker))
r=0.0003
T=2./12.0
x = Options(ticker,'yahoo')
puts,calls = x.get_options_data(month=m,year=y)
print 'done'

n=len(calls.Strike)
for i in range(1):    # take times for n result
    x=calls.Strike[i]
    c=(calls.Bid[i]+calls.Ask[i])/2.0
    if c >0:
        vol=implied_vol_American_call(s,x,T,r,c)
        print x,c,vol
    