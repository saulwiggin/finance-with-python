"""
  Name     : 4375OS_03_05_fv_f_with_comments.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
def fv_f(pv,r,n):
    """
      Objective : estimate furuew value
             pv : present value
             r  : discount period rate
             n  : number of periods
       formula  : pv*(1+r)**n
        e.g.,
        >>>fv_f(100,0.1,1)
        110.00000000000001
    """
    return pv*(1+r)**n
