"""
  Name     : 4375OS_11_02_random_numbers_from_normal.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

# generate 10 random numbers from a standard normal distribution 
# generate 20 random numbers from a normal distribution 
import scipy as sp
x=sp.random.normal(loc=0,scale=1,size=10)     # stardard normal
y=sp.random.normal(loc=0.5,scale=0.2,size=20) # normal 