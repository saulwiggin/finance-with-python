"""
  Name     : 4375OS_10_32_option_data_CBOE.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
  web pge  : http://www.cboe.com/DelayedQuote/QuoteTableDownload.aspx
  enter "ibm"
  A few lines are given below.
  IBM (INTL BUSINESS MACHINES),185.08,-0.27,
Dec 29 2013 @ 19:06 ET,Bid,184.60,Ask,185.24,Size,1x2,Vol,3382117,
Calls,Last Sale,Net,Bid,Ask,Vol,Open Int,Puts,Last Sale,Net,Bid,Ask,Vol,Open Int,
13 Dec 125.00 (IBM1327L125),0.0,0.0,58.65,61.90,0,0,13 Dec 125.00 (IBM1327X125),0.0,0.0,0.0,0.01,0,0,
13 Dec 125.00 (IBM1327L125-4),0.0,0.0,58.65,62.00,0,0,13 Dec 125.00 (IBM1327X125-4),0.0,0.0,0.0,0.01,0,0,
13 Dec 125.00 (IBM1327L125-8),0.0,0.0,58.40,62.15,0,0,13 Dec 125.00 (IBM1327X125-8),0.0,0.0,0.0,0.01,0,0,
13 Dec 125.00 (IBM1327L125-A),0.0,0.0,58.30,61.90,0,0,13 Dec 125.00 (IBM1327X125-A),0.0,0.0,0.0,0.01,0,0,
13 Dec 125.00 (IBM1327L125-B),0.0,0.0,0.0,0.0,0,0,13 Dec 125.00 (IBM1327X125-B),0.0,0.0,0.0,0.0,0,0,
13 Dec 125.00 (IBM1327L125-E),0.0,0.0,58.60,62.40,0,0,13 Dec 125.00 (IBM1327X125-E),0.0,0.0,0.0,0.01,0,0,
"""

import pandas as pd
import numpy as np
x=pd.read_csv('c:/temp/QuoteData.dat',skiprows=2,header='infer')
y=np.array(x)
n=len(y)
print y[0:4]
print y[n-5:n-1]

