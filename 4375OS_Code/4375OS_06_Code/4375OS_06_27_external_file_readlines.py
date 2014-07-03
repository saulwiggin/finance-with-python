"""
  Name     : 4375OS_06_27_external_file_readlines.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

f=open("c:/yan/ibm.csv","r")
data=f.readlines()
print type(data)

