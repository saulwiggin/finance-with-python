"""
  Name     : 4375OS_08_66_read_from_binary_file.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import array
infile=open("c:/temp/tmp.bin", "rb") 
s=infile.read()                # read all bytes into a string 
d=array.array("f", s)          # "f" for float 
print(d)
infile.close()
