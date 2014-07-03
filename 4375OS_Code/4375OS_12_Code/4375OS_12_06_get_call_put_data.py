"""
  Name     : 4375OS_12_06_get_call_put_data.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
from pandas.io.data import Options
import datetime
def get_option_data(tickrr,exp_date):
    x = Options(ticker,'yahoo')
    puts,calls = x.get_options_data(expiry=exp_date)
    return puts, calls

ticker='IBM'
exp_date=datetime.date(2014,2,28)
puts, calls =get_option_data(ticker,exp_date)
print puts.head()
print calls.head()
