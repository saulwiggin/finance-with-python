"""
  Name     : 4375OS_07_16_IBM_candle_stick.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter,WeekdayLocator, HourLocator, DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2
date1 = ( 2013, 10, 20)
date2 = ( 2013, 11, 10 )
ticker='IBM'
mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays    = DayLocator()               # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12
quotes = quotes_historical_yahoo(ticker, date1, date2)
if len(quotes) == 0:
    raise SystemExit
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
ax.xaxis.set_minor_formatter(dayFormatter)
plot_day_summary(ax, quotes, ticksize=3)
candlestick(ax, quotes, width=0.6)
ax.xaxis_date()
ax.autoscale_view()
plt.setp( plt.gca().get_xticklabels(), rotation=80, horizontalalignment='right')
plt.figtext(0.35,0.45, '10/29:   Open,    High,     Low,   Close')
plt.figtext(0.35,0.42, '        177.62,  182.32,   177.50,  182.12')
plt.figtext(0.35,0.32, 'Black ==> Close > Open ')
plt.figtext(0.35,0.28, 'Red   ==> Close < Open ')
plt.title('Candlesticks for IBM from 10/20/2013 to 11/10/2013')            
plt.ylabel('Price')
plt.xlabel('Date')
plt.show()
