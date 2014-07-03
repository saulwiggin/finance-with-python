"""
  Name     : 4375OS_03_15_IRR_f.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


def IRR_f(cashflows, iterations=100):
    rate = 1.0
    investment = cashflows[0]
    for i in range(1, iterations+1):
        rate*=(1-npv_f(rate, cashflows) / investment)
    return rate

