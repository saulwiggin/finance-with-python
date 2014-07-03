"""
  Name     : 4375OS_03_23_PMT_annuity.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

#--------------------------------------------------------#
#--- Estimate Payment of an annuity ---------------------#
#--------------------------------------------------------#
def PMT(n,r,pv,fv):
    """
    Objective: estimate period payment (like Excel function)
       n    : number of periods
       r    : discount rate
       pv   : present value 
       fv   : period payment
       e.g.,
         >>>PMT(10,0.08,100000,0)
         14902.948869707534
    """
    return (pv-fv/(1+r)**n)*r/(1-1/(1+r)**n)
   