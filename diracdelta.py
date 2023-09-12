import math as m
import numpy as np
import matplotlib.pyplot as plt
t = 0.4
I = 10000
J = 1000

F = S = x = []
for j in range(0, J+1, 1):
    for i in range(0, I+1, 1):
       
        i0 = i / I
        p = m.pi
        
        a = 2
        b = m.sin(i0 * p * j)
        c = m.sin(t * i * p * j)
    
        y = a * b * c
        F = np.append(F, y)
           
    if j <= 0:
        T = np.matrix(F)
    else:
        T = np.insert(T, 0, F, 0)
    F = []

S = T.sum(0)
s = np.append([], S)

for k in range(0, I+1, 1):
    k0 = k / I
    x = np.append(x, k0)

#print(x)
plt.title('N = 1000', fontsize='large', fontweight='bold')
plt.plot(x,s)
plt.show()