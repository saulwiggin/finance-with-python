"""
  Name     : 4375OS_08_35_yahoo_finance.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
ticker='IBM'
begdate=(2013,1,1)
enddate=(2013,11,15)
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)



