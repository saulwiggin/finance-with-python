"""
  Name     : 4375OS_06_09_show_all_functions_numpy2.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
print dir(np)  
x=np.array(dir(np))
print 'number of functions contained =', len(x)            # showing the length of the array

print x[200:210]        
