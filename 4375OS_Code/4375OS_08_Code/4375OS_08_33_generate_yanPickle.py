"""
  Name     : 4375OS_08_33_generate_yanPickle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
df=pd.read_csv('c:/temp/yanMonthly.csv',index_col=0)
df.to_pickle('h:/public_html/yanMonthly.pickle')