import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
import math as m

dt = 0.1
t1 = -5
t2 = 5
t0 = t2-t1
n = 10
T = f = S = D = []
x = symbols('x', communtative = True)

def F(x):
    return 20 * np.cos(pow(x,2) / 2)

l = 0
for l in range(int(t0 / dt)):
    t = t1 + l * dt
    T = np.append(T, t)
    y = F(t)
    f = np.append(f, y)
T = np.append(T, t2)
f = np.append(f, F(t2))

i = j = a = b = 0
#ed = 1000 * (t2 - t1)

c = 1 / t0 * sy.integrate(F, (x, t1, t2))
for i in range(int(t0 / dt)):
    t = t1 + i * dt
    for j in range(n):
        
        a0 = 2 / t0 * sy.integrate(F * np.sin(j * x), (x, t1, t2))
        a = a + a0 * np.sin(j * t)
        b0 = 2 / t0 * sy.integrate(F * np.cos(j * x), (x, t1, t2))
        b = b + b0 * np.cos(j * t)
        S = np.append(S, a + b)
    
            
 
#print(1, F(1))
plt.plot(T, f)
plt.show()