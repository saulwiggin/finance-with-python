"""
  Name     : 4375OS_09_03_profit_loss_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

s = arange(30,70,5)
x=45
c=2.5
y=(abs(s-x)+s-x)/2 -c
y2=zeros(len(s))
ylim(-30,50)
plot(s,y)
plot(s,y2,'-.')
plot(s,-y)
title("Profit/Loss function for a call option")
xlabel('Stock price')
ylabel('Profit (loss)')
plt.annotate('Call option buyer', xy=(55,15), xytext=(35,20),
             arrowprops=dict(facecolor='blue',shrink=0.01),)
plt.annotate('Call option seller', xy=(55,-10), xytext=(40,-20),
             arrowprops=dict(facecolor='red',shrink=0.01),)
show()






