"""
  Name     : 4375OS_11_10_select_m_stocks_from_n_stocks.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
n_stocks=10
x=load('c:/temp/yanMonthly.pickle')
x2=unique(np.array(x.index))
x3=x2[x2<'ZZZZ']      # remove all indices
sp.random.seed(1234567)
nonStocks=['GOLDPRICE','HML','SMB','Mkt_Rf','Rf','Russ3000E_D','US_DEBT',
   'Russ3000E_X','US_GDP2009dollar','US_GDP2013dollar']
x4=list(x3)
for i in range(len(nonStocks)):
    x4.remove(nonStocks[i])
k=sp.random.uniform(low=1,high=len(x4),size=n_stocks)
y,s=[],[]
for i in range(n_stocks):
    index=int(k[i])
    y.append(index)
    s.append(x4[index])
final=unique(y)
print final
print s
