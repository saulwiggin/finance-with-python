"""
  Name     : 4375OS_08_67_efficient_portfolio3stocks.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
             
Efficient porfolio (mean-variance) :ticker used
('IBM', 'WMT', 'C')
Sharpe ratio for equal-weighted portfolio
[ 0.33333333  0.33333333  0.33333333]
0.634645504708
Optimization terminated successfully.
         Current function value: -0.669702
         Iterations: 30
         Function evaluations: 58
Optimal weights are 
[ 0.49713116  0.31047116  0.19239769]
final Sharpe ratio is 
0.669701971388
>>> 
"""
from matplotlib.finance import quotes_historical_yahoo
import numpy as np
import pandas as pd
import scipy as sp
from scipy.optimize import fmin
# Step 1: input area
ticker=('IBM','WMT','C')   # tickers
begdate=(1990,1,1)         # beginning date 
enddate=(2012,12,31)       # ending date
rf=0.0003                  # annual risk-free rate
# Step 2: define a few functions
# function 1: 
def ret_annual(ticker,begdate,enddte):
    x=quotes_historical_yahoo(ticker,begdate,enddate,asobject=True,adjusted=True)
    logret = log(x.aclose[1:]/x.aclose[:-1])
    date=[]
    d0=x.date
    for i in range(0,size(logret)):
        date.append(d0[i].strftime("%Y"))
    y=pd.DataFrame(logret,date,columns=[ticker])
    return exp(y.groupby(y.index).sum())-1
# function 2: estimate portfolio variance 
def portfolio_var(R,w):
    cor = sp.corrcoef(R.T)
    std_dev=sp.std(R,axis=0)
    var = 0.0
    for i in xrange(n):
        for j in xrange(n):
            var += w[i]*w[j]*std_dev[i]*std_dev[j]*cor[i, j]
    return var
# function 3: estimate sharpe ratio
def sharpe(R,w):
    var = portfolio_var(R,w)
    mean_return=mean(R,axis=0)
    ret = sp.array(mean_return)
    return (sp.dot(w,ret) - rf)/sqrt(var)
# function 4: for given n-1 weights, return a negative sharpe ratio
def negative_sharpe_n_minus_1_stock(w):
    w2=sp.append(w,1-sum(w))
    return -sharpe(R,w2)        # using a return matrix here!!!!!!
# Step 3: generate a return matrix (annul return)
n=len(ticker)              # number of stocks
x2=ret_annual(ticker[0],begdate,enddate) 
for i in range(1,n):
    x_=ret_annual(ticker[i],begdate,enddate) 
    x2=pd.merge(x2,x_,left_index=True,right_index=True)
# using scipy array format 
R = sp.array(x2)
print('Efficient porfolio (mean-variance) :ticker used')
print(ticker)
print('Sharpe ratio for an equal-weighted portfolio')
equal_w=sp.ones(n, dtype=float) * 1.0 /n 
print(equal_w)
print(sharpe(R,equal_w))
# for n stocks, we could only choose n-1 weights
w0= sp.ones(n-1, dtype=float) * 1.0 /n 
w1 = fmin(negative_sharpe_n_minus_1_stock,w0)
final_w = sp.append(w1, 1 - sum(w1))
final_sharpe = sharpe(R,final_w)
print ('Optimal weights are ')
print (final_w)
print ('final Sharpe ratio is ')
print(final_sharpe)
