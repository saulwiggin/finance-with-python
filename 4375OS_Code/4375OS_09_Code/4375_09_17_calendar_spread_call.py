"""
  Name     : 4375OS_09_17_calendar_spread_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import matplotlib.pyplot as plt
import p4f
sT = arange(20,70,5)
s=40
x=40
T1=0.5
T2=1
sigma=0.3
r=0.05
payoff=(abs(sT-x)+sT-x)/2
call_01=p4f.bs_call(s,x,T1,r,sigma)  # short
call_02=p4f.bs_call(s,x,T2,r,sigma)  # long
profit_01=payoff-call_01
call_03=p4f.bs_call(sT,x,(T2-T1),r,sigma)
calendar_spread=call_03-payoff+call_01 -call_02
y0=zeros(len(sT))
ylim(-20,20)
xlim(20,60)
plot(sT,call_03,'b-.')
plot(sT,call_02-call_01-payoff,'b-.')
plot(sT,calendar_spread,'r')
plot([x,x],[-20,-15])
title("Calendar spread with calls")
xlabel('Stock price at maturity (sT)')
ylabel('Profit (loss)')
plt.annotate('Buy a call with T1  and sell a call with T2', xy=(25,16))
plt.annotate('where T1<T2', xy=(25,14))
plt.annotate('Calendar spread', xy=(25,-3), xytext=(22,-15),
             arrowprops=dict(facecolor='red',shrink=0.01),)
plt.annotate('Value of the call (T2) at maturity', xy=(45,7), xytext=(25,10),
             arrowprops=dict(facecolor='blue',shrink=0.01),)
plt.annotate('Proflit/loss with call 1 only', xy=(50,-10), xytext=(30,-10),
             arrowprops=dict(facecolor='blue',shrink=0.01),)
plt.annotate('Exersise price', xy=(x+0.5,-20+0.5))
plt.show()






