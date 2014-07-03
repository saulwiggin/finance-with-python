"""
  Name     : 4375OS_10_38_put_call_ratio.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com

  Step 1: go to http://www.cboe.com/
  Step 2: click "quotes & data" on the menu bar
  Step 3: choolse "CBOE volume and Put/call ratios
  Step 4: Choose "CBOE Total Exchange Volume and Put/Call Ratios 
          (11-01-2006 to present)" under current
  Assume that the file named totalpc.csv is saved under c:\temp\.
"""

import pandas as pd
from matplotlib.pyplot import *
data=pd.read_csv('c:/temp/totalpc.csv',skiprows=2,index_col=0,parse_dates=True)
data.columns=('Calls','Puts','Total','Ratio')
x=data.index
y=data.Ratio
y2=ones(len(y))
title('Put-call ratio')
xlabel('Date')
ylabel('Put-call ratio')
ylim(0,1.5)
plot(x, y, 'b-')
plot(x, y2,'r')
show()