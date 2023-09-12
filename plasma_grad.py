#grad B

import numpy as np
import matplotlib.pyplot as plt

#   velocity in lightspeed unit
x = np.array([.1, 0., 0.])
vi = np.array([1e-2, 1e-2, 0.])
dt = 0.001
t = 1
n = t / dt

#   grad B, E = 0
E = np.array([0., 0., 0.])
def B(r):
    B0 = 10
    B = B0 / r
    return B

#   Lorentz tansform for velocity
def Lor(v):
    r = pow(1 - pow(v, 2), 0.5)
    return r

#   in SI unit
q = -1.602e-19  #   C
m = 9.109e-31   #   kg
c = 299792458   #   m/s
T = [0.]
W = []

x0 = Pos = x
v0 = V = vi * c
r0 = Lor(np.linalg.norm(v0 / c))

#   Boris method, relativity velocity included
x1 = x0 + v0 * dt / (2 * r0)
v1 = v0 + q * dt * E/ (2 * m)
r1 = Lor(np.linalg.norm(v1 / c))

dis = pow(pow(x1[0], 2) + pow(x1[1], 2), 0.5)
b = np.array([0., 0., B(dis)])
w = q * B(dis) / (m * c)
k = np.abs(w) / dt
i = j = 0
print(w)
W = np.append(W, w)
    
while j in range(int(k)):
    
    x2 = x1 + v1 * dt / (2 * r1)
    v2 = v1 + q * dt * E/ (2 * m)
    r2 = Lor(np.linalg.norm(v2 / c))
    t = q * dt * b / (2 * m * r2)
    s = t * 2 / (1 + pow(np.linalg.norm(t), 2))
    v3 = v2 + np.cross((v2 + np.cross(v2, t)), s)
        
    v4 = v3 + q * dt * E/ (2 * m)
    v_abs = np.linalg.norm(v4)
    unit = np([1., 0., 0.])
    vec = 
    mag = m * pow(v_abs, 2) / (2 * q * pow(B(dis), 3))
    vd = 
    
    vf = v3 + q * dt * E/ (2 * m) + vd
    rf = Lor(np.linalg.norm(vf / c))
    
    xd = 
    
    xf = x2 + vf * dt / (2 * rf) + xd
    
    Pos = np.vstack([Pos, xf])
    V = np.vstack([V, vf])
    x1 = xf
    v1 = vf
    r1 = rf
    i = i + 1
    j = j + 1
    T = np.append(T, i)

#   correct time and velocity
T = T * dt
V = V / c

'''
i = 0
#   Boris method, relativity velocity included
for i in range (int(n)):
    
    if (i == 0):
        
        x1 = x0 + v0 * dt / (2 * r0)
        v1 = v0 + q * dt * E/ (2 * m)
        r1 = Lor(np.linalg.norm(v1 / c))
        
    dis = pow(pow(x1[0], 2) + pow(x1[1], 2), 0.5)
    b = np.array([0., 0., B(dis)])
    w = q * B(dis) / (m * c)
    k = np.abs(w) / dt
    j = 0
    print(w)
    W = np.append(W, w)
    
    for j in range(int(k)):
    
        x2 = x1 + v1 * dt / (2 * r1)
        v2 = v1 + q * dt * E/ (2 * m)
        r2 = Lor(np.linalg.norm(v2 / c))
        t = q * dt * b / (2 * m * r2)
        s = t * 2 / (1 + pow(np.linalg.norm(t), 2))
        v3 = v2 + np.cross((v2 + np.cross(v2, t)), s)
        
#        vd = 
        vf = v3 + q * dt * E/ (2 * m)
        rf = Lor(np.linalg.norm(vf / c))
 #       xd = 
        xf = x2 + vf * dt / (2 * rf)
    
        Pos = np.vstack([Pos, xf])
        V = np.vstack([V, vf])
        x1 = xf
        v1 = vf
        r1 = rf
        i = i + 1
        j = j + 1
        T = np.append(T, i)

#   correct time and velocity
T = T * dt
V = V / c
'''

#   plot
i = 0
j = 0
for i in range(3):
    plt.subplot(3, 3, i+1)
    plt.plot(T, Pos.T[i])
    plt.title("x %d to t" % (i+1))
    i = i + 1
for j in range(3):
    plt.subplot(3, 3, i+1)
    plt.plot(T, V.T[j])
    plt.title("v %d to t" % (j+1))
    i = i + 1
    j = j + 1

plt.subplot(3, 3, 7)
plt.plot(Pos.T[0], Pos.T[1])
plt.subplot(3, 3, 8)
plt.plot(Pos.T[1], Pos.T[2])
plt.subplot(3, 3, 9)
plt.plot(Pos.T[0], Pos.T[2])

print(len(W))

plt.show()