"""
  Name     : 4375OS_07_05_DuPoint.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

IDs = ["IBM","DELL","WMT","City","MSFT","A","AA"]

N = len(IDs)
property1_1 = numpy.array([1,1,1,0,1,1,1])
property1_2 = numpy.array([0,3,0,2,0,5,0])
property2_1 = numpy.array([1,0,2,0,3,0,4])
property2_2 = numpy.array([0,6,0,7,0,4,0])
property3_1 = numpy.array([10,0,2.3,0,5,0,1])
property3_2 = numpy.array([0,5,0,4,0,3,0])

ind = numpy.arange(N)
width = 0.8
#title("DuPont Identity")
p1 = ax1.bar(ind, property1_1, width, color='red')
p2 = ax1.bar(ind, property2_1, width, color='blue', bottom=property1_1)
p3 = ax1.bar(ind, property3_1, width, color='green', bottom=property1_1 + property2_1)

p4 = ax1.bar(ind-0.2, property1_2, width, color='red')
p5 = ax1.bar(ind-0.2, property2_2, width, color='blue', bottom=property1_2)
p6 = ax1.bar(ind-0.2, property3_2, width, color='green', bottom=property1_2+property2_2)

plt.xticks(ind+width/2., IDs )
plt.show()

