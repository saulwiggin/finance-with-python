"""
  Name     : 4375OS_06_28_external_file_loadtext.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as ny
x=ny.loadtxt("c:/temp/test.csv",delimiter=',',skiprows=1)
