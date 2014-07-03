"""
  Name     : 4375OS_07_34_math_formulae.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import matplotlib.mathtext as mathtext
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('image', origin='upper')
parser = mathtext.MathTextParser("Bitmap")
r'$\left[\left\lfloor\frac{5}{\frac{\left(3\right)}{4}} y\right)\right]$'
rgba1, depth1 = parser.to_rgba(r' $d_2=\frac{ln(S_0/K)+(r-\sigma^2/2)T}{\sigma\sqrt{T}}=d_1-\sigma\sqrt{T}$', color='blue',fontsize=12, dpi=200)
rgba2, depth2 = parser.to_rgba(r'$d_1=\frac{ln(S_0/K)+(r+\sigma^2/2)T}{\sigma\sqrt{T}}$', color='blue', fontsize=12, dpi=200)
rgba3, depth3 = parser.to_rgba(r' $c=S_0N(d_1)- Ke^{-rT}N(d_2)$', color='red',fontsize=14, dpi=200)
fig = plt.figure()
fig.figimage(rgba1.astype(float)/255., 100, 100)
fig.figimage(rgba2.astype(float)/255., 100, 200)
fig.figimage(rgba3.astype(float)/255., 100, 300)
plt.show()


