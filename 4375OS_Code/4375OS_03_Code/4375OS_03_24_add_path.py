"""
  Name     : 4375OS_03_24_add_path.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def add_path(myFolder):
    import sys
    if myFolder not in sys.path:
        sys.path.append(myFolder)
