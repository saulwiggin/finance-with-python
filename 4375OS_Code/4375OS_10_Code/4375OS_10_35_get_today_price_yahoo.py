"""
  Name     : 4375OS_10_35_get_today_price_yahoo.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import urllib
import re
stocks=['ibm', 'dell', 'goog']
for i in range(len(stocks)):
    file = urllib.urlopen("http://finance.yahoo.com/q?s=" +stocks[i] + "&ql=1")
    text = file.read()
    pattern='<span id="yfs_l84_' + stocks[i] + '">(.+?)</span>'
    price = re.findall(re.compile(pattern), text)
    print "For ",stocks[i].upper(), " the price is ", price
    