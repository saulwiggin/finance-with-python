"""
  Name     : 4375OS_10_34_get_option_data_given_year_month.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from pandas.io.data import Options
ticker='IBM'
month=2
year=2014
x = Options(ticker,'yahoo')
puts,calls = x.get_options_data(month,year)

print puts.head()

