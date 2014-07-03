"""
  Name     : 4375OS_12_16_simulate GARCH_from_R.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com



for (i in (m + 1):(n +nStart+ m)) {
      h[i] = omega + sum(alpha * (abs(eps[i - (1:order.alpha)]) - 
          gamma * (eps[i - (1:order.alpha)]))^delta) + sum(beta * 
          h[i - (1:order.beta)])
       eps[i] = h[i]^deltainv * z[i]
       y[i] = mu + sum(ar * y[i - (1:order.ar)]) + sum(ma * 
       eps[i - (1:order.ma)]) + eps[i]
}

data = cbind(y = y[(m + 1):(n+nStart+ m)],sigma = h[(m + 1):(n + nStart+m)]^deltainv, 
z = z[(m + 1):(n +nStart+ m)])
data = data[-(1:nStart), ]
colnames(data) <- c("garch", "sigma", "eps")
"""

import scipy as sp
import numpy as np
sp.random.seed(12345)
m=2
n=100        # n is the number of observations
nDrop=100   # we need to drop the first seveal observations
delta=2
omega=1e-6
alpha=(0.05,0.05)
beta=0.8
mu=ar=ma=ar=0.0
gamma=(0.0,0.0)
order_ar    =size(ar)
order_ma    =size(ma)
order_beta  =size(beta)
order_alpha =size(alpha)
z0=sp.random.standard_normal(n+nDrop)
deltainv=1/delta
spec_1=spec_2=spec_3=np.array([2])
z = np.hstack((spec_1,z0))
t=np.zeros(n+nDrop)
h = np.hstack((spec_2,t))
y = np.hstack((spec_3,t))
eps0 = h**deltainv  * z

for i in range(m+1,n +nDrop+m-1):
    t1=sum(alpha[::-1]*abs(eps0[i-2:i]))   # reverse alpha =alpha[::-1]
    t2=eps0[i-order_alpha-1:i-1]
    t3=t2*t2
    t4=np.dot(gamma,t3.T)  
    t5=sum(beta* h[i-order_beta:i-1])
    h[i]=omega+t1-t4+ t5
    eps0[i] = h[i]**deltainv * z[i]
    t10=ar * y[i-order_ar:i-1]
    t11=ma * eps0[i -order_ma:i-1]
    y[i]=mu+sum(t10)+sum(t11)+eps0[i]
    #y[i] = mu + sum(ar * y[i - (1:order.ar)]) + sum(ma *  #eps[i - (1:order.ma)]) + eps[i]
    #print i
garch=y[nDrop+1:]    
sigma=h[nDrop+1:]**0.5
eps=eps0[nDrop+1:]
x=range(1,len(garch)+1)    

plot(x,garch,'r')
plot(x,sigma,'b')
#plot(x,eps,'g')
title('GARCH(2,1) process')
figtext(0.2,0.8,'omega='+str(omega)+', alpha='+str(alpha)+',beta='+str(beta))
figtext(0.2,0.75,'gamma='+str(gamma))
figtext(0.2,0.7,'mu='+str(mu)+', ar='+str(ar)+',ma='+str(ma))

show()
    
    

