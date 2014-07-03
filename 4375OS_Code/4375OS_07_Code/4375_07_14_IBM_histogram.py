"""
  Name     : 4375OS_07_14_IBM_histogram.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.pyplot import *
from matplotlib.finance import quotes_historical_yahoo
import numpy as np
import matplotlib.mlab as mlab

ticker='IBM'
begdate=(2013,1,1)
enddate=(2013,11,9)
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = (p.open[1:] - p.open[:-1])/p.open[1:]
[n,bins,patches] = hist(ret, 100)
mu = np.mean(ret)
sigma = np.std(ret)
x = mlab.normpdf(bins, mu, sigma)
plot(bins, x, color='red', lw=2)
title("IBM return distribution")
xlabel("Returns")
ylabel("Frequency")
show()


