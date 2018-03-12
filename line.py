#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:05:31 2018

@author: ec2017b219
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
plt.plot(x, y, "o")


# draw vertical line from (70,100) to (70, 250)
plt.annotate("",
              xy=(70, 100), xycoords='data',
              xytext=(70, 250), textcoords='data',
              arrowprops=dict(arrowstyle="-",
                              connectionstyle="arc3,rad=0."), 
              )

# draw diagonal line from (70, 90) to (90, 200)
plt.annotate("",
              xy=(70, 90), xycoords='data',
              xytext=(90, 200), textcoords='data',
              arrowprops=dict(arrowstyle="-",
                              connectionstyle="arc3,rad=0."), 
              )

plt.show()