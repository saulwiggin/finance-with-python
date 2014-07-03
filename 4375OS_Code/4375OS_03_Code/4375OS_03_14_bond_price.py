"""
  Name     : 4375OS_03_13_bond_price.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def bond_price(c,r,n,face_value):
    """
    Objective: estimte price of a bond
     c:       coupon payment
     r      : discount rate 
     n      : number of period
     face_value: principal
     e.g.,
          >>> bond_price(10,0.08,10,1000)
          530.2943020740986
    """
    return(c/r*(1-1/(1+r)**n) + face_value/(1+r)**n)
