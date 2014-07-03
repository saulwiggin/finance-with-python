"""
  Name     : 4375OS_03_22_dir2_default_input_value.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

# with a default input value
def dir2(path='c:\python32'):
    from os import listdir
    print(listdir(path))    
