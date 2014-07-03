"""
  Name     : 4375OS_11_36_boostrapping_function.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
def boots_f(data,n_obs,replacement=None):
    """
     Objective: generate Bootstrapping with or without replacement
     Condition: the number of data set is higher thatn the number of choice
     
     Example #1: without replacement
     >>> data=range(100)
     >>> boots_f(data,10)
     array([29, 11, 44, 65, 17,  7, 73, 84, 35, 94])
  
    
    """
    
    n=len(data)
    if (n<n_obs): 
        print "n is less than n_obs"
    else:
        if replacement==None:
            y=np.random.permutation(data)
            return y[0:n_obs]
        else:
            y=[]
            for i in range(n_obs):
                k=np.random.permutation(data)
                y.append(k[0])
            return y

