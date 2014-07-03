"""
  Name     : 4375OS_10_07_loop_through_dictionary.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

d = {'x': 5, 'a': 2, 'd': 15} 
for key in d:
    print 'key = ', key, ' while value = ', d[key]
   
for k,v in d.items():
    print k,v
    