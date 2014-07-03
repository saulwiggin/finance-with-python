"""
  Name     : 4375OS_07_25_insert_an_image.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
image_file = cbook.get_sample_data('c:/temp/python_logo.png')
image = plt.imread(image_file)
plt.imshow(image)
plt.axis('off') 
plt.show()
