#   figure-8

import numpy as np
import matplotlib.pyplot as plt

#   velocity in lightspeed unit
x = np.array([.1, .1, 0.])
vi = np.array([0., 1e-3, 0.])
dt = 1e-4
#t = 100

#   defineed E & B field
E = np.array([0., 0., 0.])
#   in T = Wb/m2
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

#R = 1e5         #   m, radii of curvature line
rad = pow(pow(x[0], 2) + pow(x[1], 2), 0.5)
w = q * B(rad) / (m * c)
n = w / dt

x0 = Pos = x
v0 = V = vi * c
r0 = Lor(np.linalg.norm(v0 / c))
theta = radi = np.array([0., 0., 0.])

#   Boris method, relativity velocity included
i = 0
for i in range (int(n)):
    x1 = x0 + v0 * dt / (2 * r0)
    v1 = v0 + q * dt * E/ (2 * m)
    r1 = Lor(np.linalg.norm(v1 / c))
    
    #   unit vector of B, at pos. x1
    rad = pow(pow(x0[0], 2) + pow(x0[1], 2), 0.5)
    theta[0] = x0[1] / rad
    theta[1] = -x0[0] / rad
    radi[0] = x0[0] / rad
    radi[1] = x0[1] / rad
    vd1 = m * pow(np.dot(v1, theta), 2) * radi / rad
    
    t = q * dt * B(rad) * theta / (2 * m * r1)
    s = t * 2 / (1 + pow(np.linalg.norm(t), 2))
    v2 = v1 + np.cross((v1 + np.cross(v1, t)), s)
    
    vd2 = m * pow(np.dot(v1, theta), 2) * radi / (B(rad) * rad)
    
    vf = v2 + q * dt * E/ (2 * m) - vd1 - vd2
    rf = Lor(np.linalg.norm(vf / c))
    xf = x1 + vf * dt / (2 * rf)

#    w = q * B(rad) / (m * c)
    Pos = np.vstack([Pos, xf])
    V = np.vstack([V, vf])
    x0 = xf
    v0 = vf
    r0 = rf
    i = i + 1
    T = np.append(T, i)
#    print(w)

#   correct time and velocity
T = T * dt
V = V / c

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
plt.plot(Pos.T[0], Pos.T[2])
'''
plt.subplot(3, 3, 9)
plt.plot(Pos.T[0], Pos.T[2])
'''
plt.show()
