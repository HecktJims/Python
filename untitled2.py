# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:31:52 2021

@author: heckt
"""
import numpy as np
'''
x = np.array(range(0, 13, 1))
x = (x - 6) / 2
print(x)
'''
A = (np.array(range(4))) - 4
B = (np.array(range(0, 21, 1)) - 10) / 20
C = np.array(range(1, 5, 1))

ctr = np.concatenate([A, B, C])
#ctr = np.concatenate([ctr, C])

print (ctr)
