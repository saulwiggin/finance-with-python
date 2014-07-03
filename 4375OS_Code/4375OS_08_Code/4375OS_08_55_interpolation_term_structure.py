"""
  Name     : 4375OS_08_55_interpolation_term_structure.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
x=pd.Series([0.29,0.57,np.nan,1.34,np.nan,np.nan,np.nan,np.nan,2.7])
y=x.interpolate()
print y
