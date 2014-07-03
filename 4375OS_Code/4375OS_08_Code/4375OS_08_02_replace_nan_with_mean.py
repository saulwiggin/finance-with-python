"""
  Name     : 4375OS_08_02_replace_nan_with_mean.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import numpy as np
x=pd.Series([0.1,0.02,-0.03,np.nan,0.130,0.125])
m=np.mean(x)
y=x.fillna(m)

