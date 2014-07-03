"""
  Name     : 4375OS_11_15_simulatioin_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
from scipy import zeros, sqrt, shape
import scipy as sp
S0 = 40.      # stock price at time zero
X=   40.      # exercise price
T =0.5        # years
r =0.05       # risk-free rate
sigma = 0.2   # volatility (annual)
n_steps=100.          # number of steps
sp.random.seed(12345) # fix those randome numbers
n_simulation = 5000   # number of simulation
dt =T/n_steps
call = zeros([n_simulation], dtype=float)
x = range(0, int(n_steps), 1)
for j in range(0, n_simulation):
    sT=S0
    for i in x[:-1]:
        e=sp.random.normal()
        sT*=exp((r-0.5*sigma*sigma)*dt+sigma*e*sqrt(dt))
        call[j]=max(sT-X,0)
call_price=mean(call)*exp(-r*T)
print 'call price = ', round(call_price,3)