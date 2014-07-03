"""
  Name     : 4375OS_08_68_efficient_frontier.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
from matplotlib.finance import quotes_historical_yahoo
import numpy as np
import pandas as pd
from numpy.linalg import inv, pinv 
# Step 1: input area
begYear,endYear = 2001,2013
stocks=['IBM','WMT','AAPL','C','MSFT']
# Step 2: define a few functions
#         function 1
def ret_monthly(ticker):
    x = quotes_historical_yahoo(ticker,(begYear,1,1),(endYear,12,31),asobject=True,adjusted=True)
    logret=log(x.aclose[1:]/x.aclose[:-1])
    date=[]
    d0=x.date
    for i in range(0,size(logret)):
        date.append(''.join([d0[i].strftime("%Y"),d0[i].strftime("%m")]))
    y=pd.DataFrame(logret,date,columns=[ticker])
    return y.groupby(y.index).sum()
#  function 2: objective function     
def objFunction(W, R, target_ret): 
    stock_mean=np.mean(R,axis=0)  
    port_mean=np.dot(W,stock_mean)           # portfolio mean
    cov=np.cov(R.T)                          # variance-covariance matrix
    port_var=np.dot(np.dot(W,cov),W.T)       # portfolio variance
    penalty = 2000*abs(port_mean-target_ret) # penalty 4 deviation from target
    return np.sqrt(port_var) + penalty       # objective function 
# Step 3: Generate a return matrix R
R0=ret_monthly(stocks[0])      # starting from 1st stock
n_stock=len(stocks)            # number of stocks
for i in xrange(1,n_stock):    # then merge with other stocks
    x=ret_monthly(stocks[i])
    R0=pd.merge(R0,x,left_index=True,right_index=True)
R=np.array(R0)
# Step 4: estimate optimal portfolo for a given return 
out_mean,out_std,out_weight=[],[],[] 
stockMean=np.mean(R,axis=0)    
for r in np.linspace(np.min(stockMean), np.max(stockMean), num=100):
    W = ones([n_stock])/n_stock                       # starting from equal weights 
    b_ = [(0,1) for i in range(n_stock)]              # bounds, here no short
    c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. }) # constraint
    result=sp.optimize.minimize(objFunction,W,(R,r),method='SLSQP',constraints=c_, bounds=b_)    
    if not result.success:                            # handle error
        raise BaseException(result.message) 
    out_mean.append(round(r,4))                       # not too many decimal places
    std_=round(np.std(np.sum(R*result.x,axis=1)),6)
    out_std.append(std_)
    out_weight.append(result.x) 
# Step 4: plot the efficient frontier
title('Efficient Frontier')
xlabel('Standard Deviation of the porfolio (Risk))')
ylabel('Return of the portfolio')
figtext(0.5,0.75,str(n_stock)+' stock are used: ')
figtext(0.5,0.7,' '+str(stocks))
figtext(0.5,0.65,'Time period: '+str(begYear)+' ------ '+str(endYear))
plot(out_std,out_mean,'--')

