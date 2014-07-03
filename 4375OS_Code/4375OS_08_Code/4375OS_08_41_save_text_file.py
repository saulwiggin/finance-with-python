"""
  Name     : 4375OS_08_41_save_text_file.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo
import re
ticker='dell'
outfile=open("c:/temp/dell.txt","w")
begdate=(2013,1,1)
enddate=(2013,11,9)
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
x2= re.sub('[\(\)\{\}\.<>a-zA-Z]','', x)
outfile.write(x2)
outfile.close()