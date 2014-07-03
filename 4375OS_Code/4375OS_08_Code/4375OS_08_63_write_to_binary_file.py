"""
  Name     : 4375OS_08_63_write_to_binary_file.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import array
import numpy as np
outfile = "c:/temp/tmp.bin"
fileobj = open(outfile, mode='wb')
outvalues = array.array('f')
data=np.array([1,2,3])
outvalues.fromlist(data.tolist())
outvalues.tofile(fileobj)
fileobj.close()



