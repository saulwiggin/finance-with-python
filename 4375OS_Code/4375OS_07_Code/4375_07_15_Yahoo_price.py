"""
  Name     : 4375OS_07_15_Yahoo_price.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import datetime
import matplotlib.finance as finance
import matplotlib.mlab as mlab

ticker = 'IBM'
begdate = datetime.date(2013,1,1)
enddate = datetime.date.today()

price = finance.fetch_historical_yahoo(ticker, begdate, enddate)
r = mlab.csv2rec(price); price.close()
r.sort()


