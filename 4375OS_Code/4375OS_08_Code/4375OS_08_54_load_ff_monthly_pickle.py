"""
  Name     : 4375OS_08_54_load_ff_monthly_pickle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import pandas as pd
ffMonthly=pd.load('c:/temp/ffMonthly.pickle')
print ffMonthly.head()