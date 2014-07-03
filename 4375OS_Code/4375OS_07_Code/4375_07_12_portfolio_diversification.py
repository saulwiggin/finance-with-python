"""
  Name     : 4375OS_07_12_portfolio_diversification.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import matplotlib.pyplot as plt

year=[2009,2010,2011,2012,2013]
ret_A=[0.102,-0.02, 0.213,0.12,0.13]
ret_B=[0.1062,0.23, 0.045,0.234,0.113]
port_EW=(np.array(ret_A)+np.array(ret_B))/2.

plt.figtext(0.2,0.65,"Stock A")
plt.figtext(0.15,0.4,"Stock B")
plt.xlabel("Year")
plt.ylabel("Returns")

plt.plot(year,ret_A,lw=2)
plt.plot(year,ret_B,lw=2)
plt.plot(year,port_EW,lw=2)

plt.title("Indiviudal stocks vs. an equal-weighted 2-stock portflio")
plt.annotate('Equal-weighted Portfolio', xy=(2010, 0.1), xytext=(2011., 0),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.ylim(-0.1,0.3)
plt.show()









