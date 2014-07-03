"""
  Name     : 4375OS_11_24_terminal_stock_price.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
from scipy import zeros, sqrt, shape
import scipy as sp
S0 = 9.15             # stock price at time zero
T =1.                 # years
n_steps=100.          # number of steps
mu =0.15              # expected annual return 
sigma = 0.2           # volatility (annual)
sp.random.seed(12345) # fix those randome numbers
n_simulation = 1000    # number of simulation
dt =T/n_steps
S = zeros([n_simulation], dtype=float)
x = range(0, int(n_steps), 1)
for j in range(0, n_simulation):
    tt=S0
    for i in x[:-1]:
        e=sp.random.normal()
        tt+=tt*(mu-0.5*pow(sigma,2))*dt+sigma*tt*sqrt(dt)*e;
        S[j]=tt
title('Histogram of terminal price')
ylabel('Number of frequenies')
xlabel('Terminal price')
figtext(0.5,0.8,'S0='+str(S0)+',mu='+str(mu)+',sigma='+str(sigma))
figtext(0.5,0.76,'T='+str(T)+', steps='+str(int(n_steps)))
figtext(0.5,0.72,'Number of terminal prices='+str(int(n_simulation)))
hist(S)
