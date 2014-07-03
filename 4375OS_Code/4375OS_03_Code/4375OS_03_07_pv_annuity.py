"""
  Name     : 4375OS_03_07_pv_annuity.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def pv_annuity(c,r,n):
    return c/r*(1-1/(1+R)**n)
