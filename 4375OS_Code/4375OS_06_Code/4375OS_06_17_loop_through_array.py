"""
  Name     : 4375OS_06_17_loop_through_array.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
cash_flows=np.array([-100,50,40,30,25,-10,50,100])
for cash in cash_flows:
    print cash
