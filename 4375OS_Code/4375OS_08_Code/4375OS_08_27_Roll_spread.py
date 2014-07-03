"""
  Name     : 4375OS_08_27_Roll_spread.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
ticker='IBM'
begdate=(2013,9,1)
enddate=(2013,11,11)
data= quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
p=data.aclose
#print(p[0])
d=diff(p)
cov_=cov(d[1:],d[:-1])
if cov_[0,1]<0:
   print("Roll spread for %s", ticker, 'is', round(2*sqrt(-cov_[0,1]),3))
else:
   print("Cov is positive for %s",ticker, 'positive', round(cov_[0,1],3))
   
