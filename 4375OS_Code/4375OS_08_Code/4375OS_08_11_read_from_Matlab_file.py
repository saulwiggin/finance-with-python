"""
  Name     : 4375OS_08_11_read_from_Matlab_file.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from __future__ import print_function
import scipy.io as sp
matData = sp.loadmat('c:/temp/poc_data.mat')
