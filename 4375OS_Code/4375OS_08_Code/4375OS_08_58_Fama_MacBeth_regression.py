"""
  Name     : 4375OS_08_58_Fama_MacBeth_regression.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from datetime import datetime
import numpy as np
import pandas as pd
n = 252
np.random.seed(12345)
begdate=datetime(2013, 1, 2)
dateRange = pd.date_range(begdate, periods=n)
x0= pd.DataFrame(np.random.randn(n, 1),columns=['ret'],index=dateRange)
y0=pd.Series(np.random.randn(n), index=dateRange)
print pd.ols(y=y0, x=x0)


from datetime import datetime
import numpy as np
import pandas as pd
n = 252
np.random.seed(12345)
begdate=datetime(2013, 1, 2)
dateRange = pd.date_range(begdate, periods=n)
def makeDataFrame():
    data=pd.DataFrame(np.random.randn(n,7),columns=['A','B','C','D','E','F','G'],
    index=dateRange)
    return data
data = {
    'A': makeDataFrame(),
    'B': makeDataFrame(),
    'C': makeDataFrame()
}
Y = makeDataFrame()
print(pd.fama_macbeth(y=Y,x=data))
