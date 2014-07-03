"""
  Name     : 4375OS_11_22_barrier_down_and_in_put.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
import p4f
s0=40.            # today stock price 
x=40.             # exercise price
barrier=37        # barrier level
T=0.5             # maturity in years
r=0.05            # risk-free rate
sigma=0.2         # volatility (annualized)
n_simulation=1000 # number of simulations 

def down_and_in_put(s0,x,T,r,sigma,n_simulation,barrier):
    n_steps=100.    
    dt=T/n_steps
    total=0
    for j in range(0, n_simulation):
        sT=s0
        in_=False
        for i in range(0,int(n_steps)):
            e=sp.random.normal()
            sT*=sp.exp((r-0.5*sigma*sigma)*dt+sigma*e*sp.sqrt(dt))
            if sT<barrier:
                in_=True
                #print 'sT=',sT
        #print 'j=',j ,'out=',out
        if in_==True:
            total+=p4f.bs_put(s0,x,T,r,sigma)
    return total/n_simulation    
result=down_and_in_put(s0,x,T,r,sigma,n_simulation,barrier)
print 'up-and-out-call = ', round(result,3)