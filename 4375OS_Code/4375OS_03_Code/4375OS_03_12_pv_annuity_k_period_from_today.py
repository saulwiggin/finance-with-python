"""
  Name     : 4375OS_03_12_pv_annuity_k_period_from_today.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def pv_annuity_k_period_from_today(n,c,r,k_period_from_today=0):
    """
  Objective            : estimate present value of an annuity 
         n             : number of payments    
         c             : payment amount
         r             : discount
    k_period_from_today: 1st payment is k periods from today
                         default is zero
         formula       : pv_annuity(n,c,r)/(1+r)**k_period_from_today
         e.g.,
         >>> pv_annuity_k_period_from_today(29,1,0.08,1)
         10.331857417201558
         >>> pv_annuity_k_period_from_today(29,1,0.08)
         11.158406010577684
    """
    return pv_annuity(n,c,r)/(1+r)**k_period_from_today