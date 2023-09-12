# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:24:44 2018

@author: Jims
"""
import math
import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit

X = Y = np.array([])
x = y = np.array([])

for line in open('graph.txt', 'r', encoding='UTF-8'):

    row = np.asarray(line.split())
    temp = row.astype(np.float)
    
    x = np.append(x, temp[0])   #x-y
    y = np.append(y, temp[1])
plt.plot(x, y, 'ro', markersize=5)

n = 0.01
i = 0
j = n
for i in range(1000):
    
    X = np.append(X, j)
    Y = np.append(Y, math.exp(1) * X[i]**(-0.5))
    i = i + 1
    j = j + n
#    print(i, X)
    plt.plot(X, Y, 'b-')
    