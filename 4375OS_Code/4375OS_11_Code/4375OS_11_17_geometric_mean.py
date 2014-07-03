"""
  Name     : 4375OS_11_17_geomean_ret_function.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def geomean_ret(returns):
    """
      Objective: estimte 
        returns: returns array
      Example:
      >>> returns=[0.01,0.02,-0.03,0.015,0.10]
      >>> geomean_ret(returns)
      0.022140040774623948
      >>> mean(returns)
      0.023
      >>> 
    """
    product = 1
    for ret in returns:
        product *= (1+ret)
    return product ** (1.0/len(returns))-1
