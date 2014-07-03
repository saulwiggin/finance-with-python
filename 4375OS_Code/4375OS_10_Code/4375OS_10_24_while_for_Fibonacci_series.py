"""
  Name     : 4375OS_10_24_while_for_Fibonacci_series.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def fib(n):
    """Print a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b
