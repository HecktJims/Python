import math as m
import numpy as np
import matplotlib.pyplot as plt

l = 650 * 10**-9
a = 0.2 * 10**-3
i = j = k = 0
x1 = y1 = x2 = y2 = x3 = y3 = np.array([])

for i in range(10, 2000, 1):
    
    th = i * 10**(-5)
    In = m.sin(a * m.sin(th) / l)**2 * l**2 / (a**2 * m.sin(th)**2)
    #print(th, In)
    x1 = np.append(x1, th)
    y1 = np.append(y1, In)

#print(x1, y1)
plt.figure(1)
plt.plot( x1, y1, '-', label='Intensity')
plt.xlabel( "θ" )
plt.ylabel( "I/I0" )
plt.legend()
plt.show()

fi = 0.2
for j in range(1, 6283):
    
    w = j * 10**-3
    e = m.cos(w) + m.cos(fi + w) + m.cos(2 * fi + w) + m.cos(3 * fi + w) + m.cos(4 * fi + w) + m.cos(5 * fi + w)
    E = e**2
    #print(w, E)
    x2 = np.append(x2, w)
    y2 = np.append(y2, E)
    
    n = 8
    k = m.sin(n * w / 2)**2 / m.sin(w / 2)**2
    x3 = np.append(x3, w)
    y3 = np.append(y3, k)
    
#print(x2, y2)
plt.figure(2)
plt.plot( x2, y2, '-', label='6-slit electric field')
plt.xlabel( "rad" )
plt.ylabel( "Intensity" )
plt.legend()
plt.show()

#print(x3, y3)
plt.figure(3)
plt.plot( x3, y3, '-', label='N-slit interference')
plt.xlabel( "rad" )
plt.ylabel( "I/I0" )
plt.legend()
plt.show()