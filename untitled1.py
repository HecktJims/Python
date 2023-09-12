import numpy as np
import matplotlib.pyplot as plt

d = 1






k = 8.987e9
q = 1.602e-19
R = pow((q / k), 0.5)
A = np.array([0., 0., d/2])
B = np.array([0., 0., -d/2])

ini = -3 * d
pos = np.array([0., 0., 0.])
pos[0] = pos[2] = ini
i = j = 0
for i in range(13):
    
    
    for j in range(13):
        
        a = pos - A
        b = pos - B
        
        
        E = k * q * a / pow(np.linalg.norm(a), 3) + -k * q * b / pow(np.linalg.norm(b), 3)
        plt.quiver([pos[0], pos[2]], E[0], E[2])
        
        plt.plot()
        
        pos[2] = pos[2] + 0.5 * d
        
        
    pos[0] = pos[0] + 0.5 * d
    
    
plt.subplot(2, 2, 1)


plt.subplot(2, 2, 2)


plt.subplot(2, 2, 3)


plt.subplot(2, 2, 4)







'''

plt.subplot(3, 3, 7)
plt.plot(Pos.T[0], Pos.T[1])
'''
plt.show()