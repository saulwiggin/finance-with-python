"""
  Name     : 4375OS_03_03_pv_f_with_comments.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
def npv_f(rate, cashflows):
    """Objective  : estimate NPV value
         rate     : discount rate
         cashflows: cashflows
         e.g.
         >>>npv_f(0.1, [-100.0, 60.0, 60.0, 60.0])
         49.211119459053322
    """
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1 + rate)**i
    return total
