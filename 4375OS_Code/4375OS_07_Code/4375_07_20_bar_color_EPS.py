"""
  Name     : 4375OS_07_20_bar_color_EPS.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

A_EPS = (5.02, 4.54,4.18, 3.73)
B_EPS = (1.35, 1.88, 1.35, 0.73)

ind = np.arange(len(A_EPS))  # the x locations for the groups
width = 0.40                 # the width of the bars
fig, ax = plt.subplots()
A_Std=B_Std=(2,2,2,2)
rects1 = ax.bar(ind, A_EPS, width, color='r', yerr=A_Std)
rects2 = ax.bar(ind+width, B_EPS, width, color='y', yerr=B_Std)
ax.set_ylabel('EPS')
ax.set_xlabel('Year')
ax.set_title('Diluted EPS Excluding Extraordinary Items ')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2012', '2011', '2010', '2009') )
ax.legend( (rects1[0], rects2[0]), ('W-Mart', 'DELL') )
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.show()
