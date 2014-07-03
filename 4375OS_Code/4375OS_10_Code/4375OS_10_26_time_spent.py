"""
  Name     : 4375OS_10_26_time_spent.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import time
start = time.clock()
n=10000000
for i in range(1,n):
    k=i+i+2
diff= (time.clock() - start)
print round(diff,2), 'second'

