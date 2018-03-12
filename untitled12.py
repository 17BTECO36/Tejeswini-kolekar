#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:43:19 2018

@author: ec2017b219
"""

# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
 
# setting the x - coordinates
x = np.arange(0, 2*(np.pi), 0.1)
# setting the corresponding y - coordinates
y = np.sin(x)
 
# potting the points
plt.plot(x, y)
 
# function to show the plot
plt.show()