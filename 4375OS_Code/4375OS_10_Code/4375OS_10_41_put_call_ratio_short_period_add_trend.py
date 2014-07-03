"""
  Name     : 4375OS_10_41_put_call_ratio_short_period_add_trend.py
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
import matplotlib.pyplot as plt
from datetime import datetime
import statsmodels.api as sm
data=pd.read_csv('c:/temp/totalpc.csv',skiprows=2,index_col=0,parse_dates=True)
data.columns=('Calls','Puts','Total','Ratio')
begdate=datetime(2013,6, 1)
enddate=datetime(2013,12,31)

data2=data[(data.index>=begdate) & (data.index<=enddate)]
x=data2.index
y=data2.Ratio
x2=range(len(x))
x3=sm.add_constant(x2)
model=sm.OLS(y,x3)
results=model.fit()
#print results.summary()
alpha=round(results.params[0],3)
slope=round(results.params[1],3)
y3=alpha+dot(slope,x2)
y2=ones(len(y))
title('Put-call ratio')
xlabel('Date')
ylabel('Put-call ratio')
ylim(0,1.5)
plot(x, y, 'b-')
plot(x, y2,'r-.')
plot(x,y3,'y+')

plt.figtext(0.3,0.35,'Trend: intercept='+str(alpha)+', slope='+str(slope))
show()