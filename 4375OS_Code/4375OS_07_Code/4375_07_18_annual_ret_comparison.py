"""
  Name     : 4375OS_07_18_annual_ret_comparison.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo
stocks = ('IBM', 'DELL', 'WMT', 'C', 'AAPL')
begdate=(2013,1,1)
enddate=(2013,11,30)
def ret_annual(ticker):
    x = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
    logret = log(x.aclose[1:]/x.aclose[:-1])
    return(exp(sum(logret))-1)
performance = []
for ticker in stocks:
    performance.append(ret_annual(ticker))
y_pos = np.arange(len(stocks))
plt.barh(y_pos, performance, left=0, alpha=0.3)
plt.yticks(y_pos, stocks)
plt.xlabel('Annual returns ')
plt.title('Performance comparisons (annual return)')
plt.show()