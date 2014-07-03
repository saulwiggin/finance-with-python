"""
  Name     : 4375OS_04_02_APR_to_Rc.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

#----------------------------------------------------------#
#-- Convert a APR to Rc (continously compounded rate) -----#
#----------------------------------------------------------#

def Rc_f(r,m):
    """
     Objective: estimate a continously compounded rate 
        r : norminal rate
        m : number of times compounded each year
        e.g.,
         >>>Rc_f(0.1,2)
         0.09758032833886408
    """
    return m*log(1+r/m)