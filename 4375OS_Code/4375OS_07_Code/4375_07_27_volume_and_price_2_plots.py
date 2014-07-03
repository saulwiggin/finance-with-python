"""
  Name     : 4375OS_07_27_volume_and_price_2_plots.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from pylab import plotfile, show
import matplotlib.finance as finance
ticker = 'IBM'
begdate = datetime.date(2013,1,1)
enddate = datetime.date.today()
x= finance.fetch_historical_yahoo(ticker, begdate, enddate)
plotfile(x, (0,5,6))
show()


