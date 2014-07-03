"""
  Name     : 4375OS_10_08_nested_loop.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

n1=2
n2=3
for x in xrange(1, n1+1):
    for y in xrange(1, n2+1):
        print '%d * %d = %d' % (x, y, x*y)