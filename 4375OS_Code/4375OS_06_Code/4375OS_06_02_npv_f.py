"""
  Name     : 4375OS_06_02_npv_f.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np

def npv_f(rate, values):
    cashFlows = np.asarray(values)
    return (cashFlows/ (1+rate)**np.arange(1,len(cashFlows)+1)).sum(axis=0)
