"""
  Name     : 4375OS_08_36_52week_high_low.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
from datetime import datetime
from dateutil.relativedelta import relativedelta
ticker='IBM'
enddate=datetime.now()
begdate=enddate-relativedelta(years=1)
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
x=p[-1]
y=np.array(p.tolist())[:,-1]
high=max(y)
low=min(y)
print("    Today,                    Price     High   Low,  % from low ")
print(x[0], x[-1], high, low, round((x[-1]-low)/(high-low)*100,2))
