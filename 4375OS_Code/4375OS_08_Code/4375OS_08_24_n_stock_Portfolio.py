"""
  Name     : 4375OS_08_24_n_stock_portfolio.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import pandas as pd
tickers=['IBM','dell','wmt']
final=pd.read_csv('http://chart.yahoo.com/table.csv?s=^GSPC',usecols=[0,6],index_col=0)
final.columns=['^GSPC']
for ticker in tickers:
    print ticker
    x = pd.read_csv('http://chart.yahoo.com/table.csv?s=ttt'.replace('ttt',ticker),usecols=[0,6],index_col=0)
    x.columns=[ticker]
    final=pd.merge(final,x,left_index=True,right_index=True)
    
    
    
    
    
    