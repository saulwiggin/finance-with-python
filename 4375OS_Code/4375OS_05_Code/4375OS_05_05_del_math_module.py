"""
  Name     : 4375OS_05_05_del_math_module.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import math 
print math.sqrt(3)
del math
print math.sqrt(3)   # you will see an errer message

