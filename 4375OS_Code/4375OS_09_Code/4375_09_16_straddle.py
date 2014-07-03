"""
  Name     : 4375OS_09_16_straddle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import matplotlib.pyplot as plt
sT = arange(30,80,5)
x=50;  c=2; p=1
straddle=(abs(sT-x)+sT-x)/2-c + (abs(x-sT)+x-sT)/2-p
y0=zeros(len(sT))
ylim(-6,20)
xlim(40,70)
plot(sT,y0)
plot(sT,straddle,'r')
plot([x,x],[-6,4],'g-.')
title("Profit-loss for a Straddle")
xlabel('Stock price')
ylabel('Profit (loss)')
plt.annotate('Point 1='+str(x-c-p), xy=(x-p-c,0), xytext=(x-p-c,10),
             arrowprops=dict(facecolor='red',shrink=0.01),)
plt.annotate('Point 2='+str(x+c+p), xy=(x+p+c,0), xytext=(x+p+c,13),
             arrowprops=dict(facecolor='blue',shrink=0.01),)
plt.annotate('exercise price', xy=(x+1,-5))
plt.annotate('Buy a call and buy a put with the same exericse price',xy=(45,16))
plt.show()






