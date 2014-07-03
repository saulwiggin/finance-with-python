"""
  Name     : 4375OS_07_35_show.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches

fig, ax = plt.subplots(1,figsize=(6,6))
art = mpatches.Circle([0,0], radius = 0.1, color = 'r')
ax.add_patch(art)
art = mpatches.Circle([0.2,0.2], radius = 0.1, color = 'b')
ax.add_patch(art)
art = mpatches.Circle([0.5,0.2], radius = 0.1, color = 'y')

art = mpatches.Circle([0.3,0.5], radius = 0.1, color = 'r')
ax.add_patch(art)
art = mpatches.Circle([0.8,0.5], radius = 0.1, color = 'b')
ax.add_patch(art)
art = mpatches.Circle([0.4,0.5], radius = 0.1, color = 'y')

ax.add_patch(art)
print ax.patches
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
plt.show()