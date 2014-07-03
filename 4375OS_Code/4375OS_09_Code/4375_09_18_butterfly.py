"""
  Name     : 4375OS_09_18_butterfly.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import matplotlib.pyplot as plt
sT = arange(30,80,5)
x1=50;    c1=10
x2=55;    c2=7
x3=60;    c3=5   
y1=(abs(sT-x1)+sT-x1)/2-c1
y2=(abs(sT-x2)+sT-x2)/2-c2
y3=(abs(sT-x3)+sT-x3)/2-c3
butter_fly=y1+y3-2*y2
y0=zeros(len(sT))
ylim(-20,20)
xlim(40,70)
plot(sT,y0)
plot(sT,y1)
plot(sT,-y2,'-.')
plot(sT,y3)
plot(sT,butter_fly,'r')
title("Profit-loss for a Butterfly")
xlabel('Stock price')
ylabel('Profit (loss)')
plt.annotate('Butterfly', xy=(53,3), xytext=(42,4),
             arrowprops=dict(facecolor='red',shrink=0.01),)
plt.annotate('Buy 2 calls with x1, x3 and sell 2 calls with x2', xy=(45,16))
plt.annotate('   x2=(x1+x3)/2', xy=(45,14))
plt.annotate('   x1=50, x2=55, x3=60',xy=(45,12))
plt.annotate('   c1=10,c2=7, c3=5', xy=(45,10))
plt.show()






