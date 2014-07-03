"""
  Name     : 4375OS_10_21_loop_through_dictionary.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

market_cap= {"IBM":200.97, "MSFT":311.30, "WMT":253.91, "C": 158.50}
for k,v in market_cap.items():
    print k,v