# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:00:07 2018

@author: Jims
"""
import numpy as np
import math
import matplotlib.pyplot as plt

a = 1/5
b = 1
X = []
Y = []
th = 0
for th in range(100000):
    
    th0 = th/10
    r = a * math.cos(b * th0)
    x = r * math.cos(th0)
    y = r * math.sin(th0)
    X = np.append(X ,x)
    Y = np.append(Y ,y)
    th += 1
    
plt.plot(X ,Y)