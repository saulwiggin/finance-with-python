"""
  Name     : 4375OS_11_01_random_numbers_uniform_with_seed.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

# generate 10 numbers from standard normal distribution 
import scipy as sp
x=sp.random.normal(size=10)
print x[0:5]