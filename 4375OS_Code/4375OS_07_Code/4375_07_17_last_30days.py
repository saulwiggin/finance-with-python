"""
  Name     : 4375OS_07_17_last_30days.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
import datetime
import matplotlib.finance as finance
myticker = 'IBM'
begdate = datetime.date(2013,1,1)
enddate = datetime.date.today()
price = finance.fetch_historical_yahoo(myticker, begdate, enddate)
r = mlab.csv2rec(price); price.close()
r.sort()
r = r[-30:]  # get the last 30 days
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close, 'o-')
ax.set_title('Fig. 1: IBM last 30 days with gaps on weekends')
fig.autofmt_xdate()

N = len(r)
ind = np.arange(N)  # the evenly spaced plot indices
def format_date(x, pos=None):
    thisind = np.clip(int(x+0.5), 0, N-1)
    return r.date[thisind].strftime('%Y-%m-%d')
fig, ax = plt.subplots()
ax.plot(ind, r.adj_close, 'o-')
plt.xlabel("Every Monday shown")
ax.set_title('Fig 2: IBM last 30 days evenly spaced plot indices')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()

plt.show()

