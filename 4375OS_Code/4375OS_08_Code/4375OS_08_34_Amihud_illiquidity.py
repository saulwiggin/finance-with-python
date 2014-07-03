"""
  Name     : 4375OS_08_34_Amihud_illiquidity.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import statsmodels.api as sm
from matplotlib.finance import quotes_historical_yahoo
begdate=(2013,10,1)
enddate=(2013,10,30)
ticker='IBM'  #WMT
data= quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
p=np.array(data.aclose)
dollar_vol=np.array(data.volume*p)
ret=np.array((p[1:] - p[:-1])/p[1:])
illiq=mean(np.divide(abs(ret),dollar_vol[1:]))
print("Aminud illiq=", illiq)




