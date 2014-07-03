"""
  Name     : 4375OS_11_12_simulate_stock_price.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
S0 = 9.15             # stock price at time zero
T =1.                 # maturity date (in years)
n_steps=100.          # number of steps
mu =0.15              # expected annual return 
sigma = 0.2           # volatility (annualized)
sp.random.seed(12345) # seed() 
n_simulation = 5      # number of simulations
dt =T/n_steps
S = sp.zeros([n_steps], dtype=float)
x = range(0, int(n_steps), 1)
for j in range(0, n_simulation):
    S[0]= S0
    for i in x[:-1]:
        e=sp.random.normal()
        S[i+1]=S[i]+S[i]*(mu-0.5*pow(sigma,2))*dt+sigma*S[i]*sp.sqrt(dt)*e;
    plot(x, S)
figtext(0.2,0.8,'S0='+str(S0)+',mu='+str(mu)+',sigma='+str(sigma))
figtext(0.2,0.76,'T='+str(T)+', steps='+str(int(n_steps)))
title('Stock price (number of simulations = %d ' % n_simulation +')')
xlabel('Total number of steps ='+str(int(n_steps)))
ylabel('stock price')
show()
