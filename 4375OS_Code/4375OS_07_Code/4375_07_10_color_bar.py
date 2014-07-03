"""
  Name     : 4375OS_07_10_color_bars.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import matplotlib.pyplot as plt
n = 5
menMeans = (2.3, 3.4, 1.3, 1.4, 2.7)
menStd =   (2, 3, 4, 1, 2)
ind = np.arange(n)  # the x locations for the groups
width = 0.35       # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (0.1, 2, 1.5, 2, 2.5)
womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)
ax.set_ylabel('Diluted EPS Excluding Extraordinary Items')
ax.set_xlabel('Year')
ax.set_title('EPS by two firms')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2009', '2010', '2011', '2012', '2013') )
ax.legend( (rects1[0], rects2[0]), ('IBM', 'DELL') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.show()
