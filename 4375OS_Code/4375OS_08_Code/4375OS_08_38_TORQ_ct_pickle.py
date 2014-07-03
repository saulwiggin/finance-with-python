"""
  Name     : 4375OS_08_38_TORQ_ct_pickle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
df=pd.read_csv('c:/temp/ct.csv',index_col=0)
df.to_pickle('h:/public_html/ct.pickle')