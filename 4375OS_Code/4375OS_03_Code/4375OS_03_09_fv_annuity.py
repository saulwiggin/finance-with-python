"""
  Name     : 4375OS_03_09_fv_annuity.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def fv_annuity(c,r,n):
    return c/r*((1+R)**n-1)
