"""
  Name     : 4375OS_10_06_loop_through_all_tickers.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
  location : http://canisius.edu/~yany/yanMonthly.pickle
"""
# location of the data set http://canisius.edu/~yany/yanMonthly.pickle

import pandas as pd
x=pd.load('c:/temp/yanMonthly.pickle')
stocks=x.index.unique()
for item in stocks[:10]:
  print item
  # add your codes here