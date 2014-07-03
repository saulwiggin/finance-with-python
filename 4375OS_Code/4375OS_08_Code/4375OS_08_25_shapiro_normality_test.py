"""
  Name     : 4375OS_08_25_shapiro_normality_test.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import stats
import numpy as np

x=np.random.randn(1000)
print stats.shapiro(x)
