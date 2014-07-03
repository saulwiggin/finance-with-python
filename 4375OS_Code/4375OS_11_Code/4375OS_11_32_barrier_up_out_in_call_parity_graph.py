"""
  Name     : 4375OS_11_40_barrier_up_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
s0=9.15              # stock price at time zero
x=9.15               # exercise price
barrier=10.15        # barrier
T =0.5               # maturity date (in years)
n_steps=30.          # number of steps
r =0.05              # expected annual return 
sigma = 0.2          # volatility (annualized)
sp.random.seed(125)  # seed() 
n_simulation = 5     # number of simulations
dt =T/n_steps    
S = sp.zeros([n_steps], dtype=float)
time_= range(0, int(n_steps), 1)
c=p4f.bs_call(s0,x,T,r,sigma)
sp.random.seed(124)
outTotal, inTotal= 0.,0.
n_out,n_in=0,0
for j in range(0, n_simulation):
    S[0]= s0
    inStatus=False
    outStatus=True
    for i in time_[:-1]:
        e=sp.random.normal()
        S[i+1]=S[i]*exp((r-0.5*pow(sigma,2))*dt+sigma*sp.sqrt(dt)*e)
        if S[i+1]>barrier:
            outStatus=False
            inStatus=True
    plot(time_, S)
    if outStatus==True:
        outTotal+=c;n_out+=1
    else:
        inTotal+=c;n_in+=1
S=sp.zeros(int(n_steps))+barrier
plot(time_,S,'.-')
upOutCall=round(outTotal/n_simulation,3)
upInCall=round(inTotal/n_simulation,3)
figtext(0.15,0.8,'S='+str(S0)+',X='+str(x))
figtext(0.15,0.76,'T='+str(T)+',r='+str(r)+',sigma=='+str(sigma))
figtext(0.15,0.6,'barrier='+str(barrier))
figtext(0.40,0.86, 'call price            ='+str(round(c,3)))
figtext(0.40,0.83,'up_and_out_call ='+str(upOutCall)+' (='+str(n_out)+'/'+
str(n_simulation)+'*'+str(round(c,3))+')')
figtext(0.40,0.80,'up_and_in_call ='+str(upInCall)+' (='+str(n_in)+'/'+
str(n_simulation)+'*'+str(round(c,3))+')')
title('Up-and-out and up-and-in parity (# of simulations = %d ' % n_simulation +')')
xlabel('Total number of steps ='+str(int(n_steps)))
ylabel('stock price')
show()


