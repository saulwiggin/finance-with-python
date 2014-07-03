"""
  Name     : 4375OS_09_04_profit_loss_put.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
s = arange(30,70,5)
x=45
p=2
y=(abs(x-s)+x-s)/2
y2=zeros(len(s))
x3=[x, x]
y3=[-30,10]
ylim(-30,50)
plot(s,y)
plot(s,y2,'-.')
plot(s,-y)
plot(x3,y3)
title("Profit/Loss function for a put option")
xlabel('Stock price')
ylabel('Profit (loss)')
plt.annotate('Put option buyer', xy=(35,12), xytext=(35,45),
             arrowprops=dict(facecolor='red',shrink=0.01),)
plt.annotate('Put option seller', xy=(35,-10), xytext=(35,-25),
             arrowprops=dict(facecolor='blue',shrink=0.01),)
plt.annotate('Exercise price', xy=(45,-30), xytext=(50,-20),
             arrowprops=dict(facecolor='black',shrink=0.01),)
show()






