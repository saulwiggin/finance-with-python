"""
  Name     : 4375OS_10_27_binary_search_01.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from bisect import bisect_left
def binary_search(data, x, lo=0, hi=None):  
    """
       Example:
       >>> data=range(1000000)
       >>> x=3500
       >>> binary_search(data,x)
       3500    
    """
    hi = hi if hi is not None else len(data)    
    position = bisect_left(data,x,lo,hi)          
    return (position if position != hi and data[position] == x else -1)