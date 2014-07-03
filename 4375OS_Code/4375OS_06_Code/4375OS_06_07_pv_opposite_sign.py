"""
  Name     : 4375OS_06_07_pv_opposite_sign.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp

print round(sp.pv(0.1,5,0,100),2)

print round(sp.pv(0.1,5,0,-100),2)

