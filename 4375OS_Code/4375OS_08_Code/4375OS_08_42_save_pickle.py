"""
  Name     : 4375OS_08_42_save_pickle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import numpy as np
np.random.seed(1234)
a = pd.DataFrame(randn(6,5))
a.save('c:/temp/a.pickle')
k=load("c:/temp/a.pickle")
print(k)
