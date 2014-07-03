"""
  Name     : 4375OS_10_05_loop_through_array.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
  
"""

import numpy as np
x = np.arange(10).reshape(2,5)
for y in np.nditer(x):
    print y

