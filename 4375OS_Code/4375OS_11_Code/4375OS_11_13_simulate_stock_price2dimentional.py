"""
  Name     : 4375OS_11_13_simulate_stock_price2dimentional.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
from scipy import zeros, sqrt, shape
import scipy as sp
#from pylab import *
S0 = 9.15             # stock price at time zero
T =1.                 # years
n_steps=100.          # number of steps
mu =0.15              # expected annual return 
sigma = 0.2           # volatility (annual)
sp.random.seed(12345) # fix those randome numbers
n_simulation = 8      # number of simulation

dt =T/n_steps

S = zeros([n_simulation, n_steps], dtype=float)
x = range(0, int(n_steps), 1)
for j in range(0, n_simulation, 1):
        S[j,0]= S0
        for i in x[:-1]:
            e=sp.random.normal()
            S[j,i+1]=S[j,i]+S[j,i]*(mu-0.5*pow(sigma,2))*dt+sigma*S[j,i]*sqrt(dt)*e;
        plot(x, S[j])
title('Stock price simulations (number of simulations = %d ' % n_simulation +')')
xlabel('Steps  [ T='+str(T)+' dt='+str(dt)+' ]')
ylabel('stock price')
show()
