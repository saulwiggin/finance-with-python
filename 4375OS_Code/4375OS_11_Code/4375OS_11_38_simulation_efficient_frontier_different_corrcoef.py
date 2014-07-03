"""
  Name     : 4375OS_11_38_simulation_efficient_frontier_different_corr.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/9/2014
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import scipy as sp
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
from scipy.optimize import minimize
# Step 1: inpt area
mean_0=(0.15,0.25) # mean returns for 2 stocks
std_0= (0.10,0.20) # standard deviations for 2 sotcs
n=1000             # number of simuations (returns) for each stock
corr_=(0.1,0.5,0.8)
# Step 2: Generate two uncorrelated time series 
n_stock=len(mean_0)
sp.random.seed(12345) # could generate the same random numbers 
x11=sp.random.normal(loc=0,scale=1,size=n)
x12=sp.random.normal(loc=0,scale=1,size=n)
n_corr=len(corr_)
style_=['-.','--','-']

for j in range(n_corr):
    # Step 3: Generate two correlated time series 
    corr2=corr_[j]
    index_=pd.date_range(start=dt(2001,1,1),periods=n,freq='d')
    x21=pd.DataFrame(x11,index=index_)
    x22=pd.DataFrame(corr2*x11+sqrt(1-corr2**2)*x12,index=index_)
    y1=mean_0[0]+x21*std_0[0]
    y2=mean_0[1]+x22*std_0[1]
    # step 4: generate a return matrix called R
    R0=pd.merge(y1,y2,left_index=True,right_index=True)
    R=np.array(R0)
    # Step 5: define a few functions
    def objFunction(W, R, target_ret):
        stock_mean=np.mean(R,axis=0)  
        port_mean=np.dot(W,stock_mean)           # portfolio mean
        cov=np.cov(R.T)                          # var-covar matrix
        port_var=np.dot(np.dot(W,cov),W.T)       # portfolio variance
        penalty = 2000*abs(port_mean-target_ret) # penalty 4 deviation 
        return np.sqrt(port_var) + penalty       # objective function 
        #print('stock mean=',stockMean)
    # Step 6: estimate optimal portfolo for a given return 
    out_mean,out_std,out_weight=[],[],[] 
    stockMean=np.mean(R,axis=0)    
    print('hahastyle[j]',stockMean)
    for r in np.linspace(np.min(stockMean), np.max(stockMean), num=100):
        W = ones([n_stock])/n_stock   # starting:equal w 
        b_ = [(0,1) for i in range(n_stock)]             # bounds
        c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. })# constraint
        result=minimize(objFunction,W,(R,r),method='SLSQP',constraints=c_, bounds=b_)    
        if not result.success:
            raise BaseException(result.message) 
        out_mean.append(round(r,4))               # a few decimal places
        std_=round(np.std(np.sum(R*result.x,axis=1)),6)
        out_std.append(std_)
        out_weight.append(result.x) 
    # Step 7A: plot the efficient frontier
    plt.plot(out_std,out_mean,style_[j],label='corr='+str(corr2),linewidth=3)
# Step 7B: plot the efficient frontier
stockMean2=[round(stockMean[0],3),round(stockMean[1],3)]
title('Simulation for an Efficient Frontier with diffrent correlations')
xlabel('Standard Deviation of the Porfolio')
ylabel('Return of the portfolio')
figtext(0.2,0.85,' mean = '+str(stockMean2))
figtext(0.2,0.80,' std  ='+str(std_0))
figtext(0.2,0.75,' corr ='+str(corr_))
plt.plot(np.array(std_0),np.array(stockMean),'o',markersize=10)
plt.legend(loc='lower right')
plt.show()