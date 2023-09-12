# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:48:51 2018

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

theory_R = 1000
theory_L = 0.1
theory_C = 1e-7

theory_decay = theory_R/theory_L/2
theory_resonence_freq = 1/(theory_C *theory_L)**0.5
theory_freq = (theory_resonence_freq**2 -theory_decay**2)**0.5

xdata=np.array([])
ydata=np.array([])
temp=np.array([])

def func(t, amp, decay, freq, phase, offset):
    return amp*np.exp(-decay*t)*np.cos(freq*t +phase) +offset


for line in open('fitting_test.txt', 'r', encoding='UTF-8'):

    row = np.asarray(line.split())
    temp = row.astype(np.float)
    
    xdata = np.append(xdata, temp[0])
    ydata = np.append(ydata, temp[1])

    


plt.plot(xdata, ydata, 'bo', label='data')

#popt, pcov = curve_fit(func, xdata, ydata, bounds=( [0., 0., 5000., -1.5, -0.5], [2., 10000., 10000., 1.5, 0.5]))
popt, pcov = curve_fit(func, xdata, ydata)

plt.plot(xdata, func(xdata, *popt), 'r-', label='fitting' )

theory_parameters = [ 1.25, theory_decay, theory_freq, 0, 0]
plt.plot(xdata, func(xdata, *theory_parameters), 'g--', label='theory' )

print(popt)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()