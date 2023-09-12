import numpy as np
import matplotlib.pyplot as plt

d = 1
k = 8.987e9
q = 1.602e-19
A = np.array([0., 0., d/2])
B = np.array([0., 0., -d/2])

ini = (np.array(range(0, 13, 1)) - 6) * d / 2
'''
M_A = (np.array(range(4))) - 4
M_B = (np.array(range(0, 21, 1)) - 10) / 20
M_C = np.array(range(1, 5, 1))
ctr = np.concatenate([M_A, M_B, M_C])
'''

pos = np.array([0., 0., 0.])
z = np.array([0., 0., 1.])

plt.subplot(2, 2, 1)
i = j = 0
for i in range(13):
    for j in range(13):
        pos[0] = ini[i]
        pos[2] = ini[j]
        a = pos - A
        b = pos - B
        a_val = np.linalg.norm(a)
        b_val = np.linalg.norm(b)
        
        if a_val==0 or b_val==0:
            E_dir = np.array([0., 0., 0.])
        else:
            E_dir = a / pow(a_val, 3) - b / pow(b_val, 3)
        E = k * q * E_dir
        plt.quiver(pos[0] / d, pos[2] / d, E[0], E[2], width = 2e-3)
        
        j = j + 1
    i = i + 1

plt.subplot(2, 2, 2)

i = j = 0
for i in range(13):
    for j in range(13):
        pos[0] = ini[i]
        pos[2] = ini[j]
        
        a = pos - A
        b = pos - B
        a_val = np.linalg.norm(a)
        b_val = np.linalg.norm(b)
        
        if a_val==0 or b_val==0:
            E_dir = np.array([0., 0., 0.])
        else:
            E_dir = a / pow(a_val, 3) - b / pow(b_val, 3)
        E = k * q * E_dir
        plt.quiver(pos[0] / d, pos[2] / d, E[0], E[2], width = 2e-3)
        
        con = k * q * d
        R = np.linalg.norm(pos)
        E_app = k * q * d * (3 * pos[2] / (R**2) * (pos - z)) / (R**3)
        plt.quiver(pos[0] / d, pos[2] / d, E_app[0], E_app[2], width = 2e-3, color='g')
        
        j = j + 1
    i = i + 1

plt.show()