"""
  Name     : 4375OS_08_16_TORQcq_pickle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import pandas as pd
df=pd.read_csv('c:/temp/cq.csv',index_col=0)
df.to_pickle('h:/public_html/TORQcq.pickle')