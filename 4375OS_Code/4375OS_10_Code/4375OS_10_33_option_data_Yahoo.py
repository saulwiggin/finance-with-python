"""
  Name     : 4375OS_10_33_option_data_Yahoo.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from pandas.io.data import Options
x = Options('IBM','yahoo')
puts,calls = x.get_options_data()

print calls.head()