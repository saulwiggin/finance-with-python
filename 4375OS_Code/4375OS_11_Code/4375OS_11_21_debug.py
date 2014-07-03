"""
  Name     : 4375OS_11_21_simulate_stock_price.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
S0 = 9.15  
T =1       
n_steps=10
mu =0.15              
sigma = 0.2
n_simulation =  10
dt =T/n_steps    
S = sp.zeros([n_steps], dtype=float)
x = range(0, int(n_steps), 1)
for j in range(0, n_simulation):
    S[0]= S0
    for i in x[:-1]:
        e=sp.random.normal()
        S[i+1]=S[i,j]+S[i]*(mu-0.5*pow(sigma,2))*dt+sigma*S[i]*sp.sqrt(dt)*e;
    plot(x, S)
figtext(0.2,0.8,'S0='+str(S0)+',mu='+str(mu)+',sigma='+str(sigma))
figtext(0.2,0.76,'T='+str(T)+', steps='+str(int(n_steps)))
title('Stock price (number of simulations = %d ' % n_simulation +')')
xlabel('Total number of steps ='+str(n_steps)))
ylabel('stock price')
show()
