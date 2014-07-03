"""
  Name     : 4375OS_10_12_while_loop_less_than_n.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

i=1
def while_less_than_n(n,k=1):
    i=1
    while True:
        if i<n:
            print i
            i+=k
        else:
            return 'done'

    
    
    