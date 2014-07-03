"""
  Name     : 4375OS_08_64_spread_from_TORQcq.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
cq=pd.load('c:/temp/TORQcq.pickle')
x=cq[cq.index=='MO']
spread=mean(x.ofr-x.bid)
rel_spread=mean(2*(x.ofr-x.bid)/(x.ofr+x.bid))
print round(spread,5)
print round(rel_spread,5)

