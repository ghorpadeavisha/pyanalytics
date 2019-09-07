# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:31:38 2019

@author: Avisha
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,100)
x
np.sin(x)
plt.plot(x,np.sin(x))
plt.savefig('plot2.png')
plt.savefig('F:/pywork/pyprojects/plots/plot1.png')
plt.show(); #import when running from script
# save plots away from repository
plt.plot(x,np.cos(x))
plt.show()


import matplotlib.image as mpimg
img = mpimg.imread('plot2.png')
print(img)
imgplot = plt.imshow(img)
