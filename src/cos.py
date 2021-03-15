# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:38:34 2021

@author: mm16j2b
"""

import matplotlib.pyplot as plt
import numpy
x=numpy.linspace(0,5,100)
u=numpy.cos(x)
fig, ax1 = plt.subplots()
ax1.plot(x,u)

plt.show()