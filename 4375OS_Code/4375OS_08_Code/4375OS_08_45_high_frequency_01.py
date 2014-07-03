"""
  Name     : 4375OS_08_45_high_frequency_01.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import re, string
import pandas as pd
ticker='AAPL'         # input a ticker
f1="c:/temp/ttt.txt"  # ttt will be replace with aboove sticker
f2=f1.replace("ttt",ticker)
outfile=open(f2,"w")
path="http://www.google.com/finance/getprices?q=ttt&i=300&p=10d&f=d,o,h,l,c,v"
path2=path.replace("ttt",ticker)
df=pd.read_csv(path2,skiprows=8,header=None)
df.to_csv(outfile,header=False,index=False)
outfile.close()
