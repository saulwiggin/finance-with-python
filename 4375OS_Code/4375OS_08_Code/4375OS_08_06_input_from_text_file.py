"""
  Name     : 4375OS_08_06_input_from_text_file.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_table('c:/temp/ff_monthly.txt',skiprows=4)
