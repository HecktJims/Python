# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:54:41 2023

@author: heckt
"""

i = 0
n = 15

for i in range(n):
    i += 1
    if ((i % 3 == 0) and (i %  5 == 0)):
        print(i, 'FB')
    elif(i % 3 ==0):
        print(i, 'F')
    elif(i % 5 ==0):
        print(i, 'B')
    else:
        print(i)
        