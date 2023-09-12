# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 10:24:07 2021

@author: heckt
"""
import numpy as np
import matplotlib.pyplot as plt
'''
i = 0
dv = 1e-4
U = V = R = []

for i in range(9999):
    v = (i + 1) * dv
    r = pow(1 - pow(v, 2), 0.5)
    u = v * r
    V = np.append(V, v)
    U = np.append(U, u)
    R = np.append(R, r)
    i = i + 1

plt.subplot(1,2,1)
plt.plot(V, U)
plt.subplot(1,2,2)
plt.plot(V, R)
plt.show()
'''
u0 = 0.6
v0 = u0 * pow(1 - pow(u0, 2), 0.5)
print(u0, v0)