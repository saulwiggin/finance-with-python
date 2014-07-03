"""
  Name     : 4375OS_08_43_generate_crsp_monthly_pickle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import numpy as np
d=pd.read_csv("C:/temp/crspMonthly.csv")
d.ret=d.ret.replace(-99,np.nan)
d.prc=d.prc.replace(-99,np.nan)
d.loc[d['vol']<0,'vol'] = np.nan
crspMonthly=d
crspMonthly.to_pickle("C:/temp/crspMonthly.pickle")
