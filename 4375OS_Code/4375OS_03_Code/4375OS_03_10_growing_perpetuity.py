"""
  Name     : 4375OS_03_10_growing_perpetuity.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def pv_grow_perpetuity(c,r,q):
    """ 
     Objective: estimate present value of a growing 
                perpetuity
        r: discount rate
        q: growth rate of perpetuity
        c: period payment
        e.g., (p106)
          > perpetuity_f(30000,0.08,0.04) 
          [1] 750000
    """
    return(c/(r-q))
