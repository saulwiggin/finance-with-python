"""
  Name     : 4375OS_09_01_payoff.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def payoff_call(sT,x):
    """Objective: estimate payoff of a call
       sT: terminal price
        X: exercise price
        Examples
        >>> payoff_call(50,40)
        10
        >>> payoff_call(35,40)
        0
        >>> 
    """
    return (sT-x+abs(sT-x))/2
