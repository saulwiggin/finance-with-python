"""
  Name     : 4375OS_08_37_crsp_cheadfile_pickle.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
colspecs = [(0, 6), (7, 13),(13,21), (22, 53), (54, 58), (60,62),(63,71),(72,80)]
df = pd.read_fwf("c:/temp/cheadfile.dat", colspecs=colspecs, header=None, index_col=0)
df.columns = ['PERMCO','CUSIP','NAME','TICKER','EX','BEGDATE','EGDDATE']
df.to_pickle('c:/temp/crspInfo.tickle')


