"""
  Name     : 4375OS_11_10_select_m_values_from_n_values.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
n_stocks_available=500
n_stocks=20

x=sp.random.uniform(low=1,high=n_stocks_available,size=n_stocks)
y=[]
for i in range(n_stocks):
    y.append(int(x[i]))
#print y
final=unique(y)
print final
print len(final)