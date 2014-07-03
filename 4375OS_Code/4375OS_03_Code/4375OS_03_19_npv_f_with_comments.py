"""
  Name     : 4375OS_03_19_IRR_f_with_comments.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def IRR_f(cashflows, iterations=100):
    """
        Objective: estimte IRR (Internal Rate of Return)
        e.g., 
        >>>x=[-100.0, 60.0, 60.0, 60.0]
        >>>IRR_f(x)
        0.36309653947517645
    """
    rate = 1.0
    investment = cashflows[0]
    for i in range(1, iterations+1):
        rate*=(1-npv_f(rate, cashflows) / investment)
    return rate
