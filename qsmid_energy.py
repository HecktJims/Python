import numpy as np
import matplotlib.pyplot as plt

G = 6.6743e-11   #   m3/kg s2
h = 6.626e-34    #   Js
me = 9.109e-31   #   kg
mp = 1.673e-27   #   kg
c = 299792458
Ms = 2e30
'''
G = 6.6743   #   m3/kg s2
h = 6.626    #   Js
me = 9.109   #   kg
mp = 1.673   #   kg

a = b = c = d = []

M = 1e54

i = 0
for i in range(1, 100, 1):
    #k = pow(2, i)
    k = 0.01 * i
    R = 1 * k
    UG = -3 * G * pow(M, 2) / (5 * R)
    Ug = UG * 1e-11
    a = np.append(a ,Ug)
    
    UK = 0.0088 * pow(h, 2) * pow(M, (5/3)) / (me * pow(mp, (5/3)) * pow(R, 2))
    Uk = UK * 1e8
    b = np.append(b ,Uk)
    
    T = Ug + Uk
    c = np.append(c ,T)
    d = np.append(d ,R)

plt.plot(d, a)
plt.plot(d, b)
plt.plot(d, c)

plt.plot(d, -np.log(-a))
plt.plot(d, np.log(b))
plt.plot(d, np.log(c))

plt.show()
'''
#Ans = pow((h * c / (2 * np.pi * G)), (3/2)) / (pow(mp, 2))
#Ans = pow(Ans, (3/2))
Ans = 0.029 * pow(h, 2) / (G * me * pow(mp, (5/3)) * pow(Ms, (1/3)))
Ans = 3 * Ms / (4 * np.pi * pow(Ans, 3))

print(Ans)
