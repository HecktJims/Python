#   curvature & GB drifts, cylindrical, along a circle

import numpy as np
import matplotlib.pyplot as plt

#   velocity in lightspeed unit
x = np.array([0., 0., 0.])
vi = np.array([0., 0., 0.])
dt = 0.1
t = 5
n = t / dt

#   defineed E & B field
E = np.array([0., 0., 0.])
#   in T = Wb/m2
def B(pos, R):
    
    #   remember q magnitude
    B0 = 1e-5   #   Max B at center
    e = 1 / 2   #   decay rate
    
    '''
    #   basic coord. choose_cart.
    x = pos[0]
    y = pos[1] - R* np.cos(theta)
    z = pos[2] - R* np.sin(theta)
    dis = pow(pow(x, 2) + pow(y, 2) + pow(z, 2), 0.5)
    vec = ([0, pos[2], -pos[1]])
    '''
    
    #   basic coord. choose_cylindrical
    x = pos[0]
    y = pos[1]
    z = pos[2]
    r = R - pow(pow(y, 2) + pow(z, 2), 0.5)
    z = x
    dis = pow(pow(r, 2) + pow(z, 2), 0.5)
    
    #   exponential decay
    B = B0 * pow(e, dis)
    
    return B

#   Lorentz tansform for velocity
def Lor(v):
    r = pow(1 - pow(v, 2), 0.5)
    return r

R = 1e5         #   m, radii of curvature line
#   in SI unit
q = -1.602e-19  #   C
m = 9.109e-31   #   kg
c = 299792458   #   m/s
T = [0.]

x0 = Pos = x
v0 = V = vi * c
r0 = Lor(np.linalg.norm(v0 / c))

#   Boris method, relativity velocity included
for i in range (int(n)):
    x1 = x0 + v0 * dt / (2 * r0)
    v1 = v0 + q * dt * E/ (2 * m)
    r1 = Lor(np.linalg.norm(v1 / c))
    
    #   trans. into cylindrical coord.
    rad = pow(pow(x0[1], 2) + pow(x0[2], 2), 0.5)
    if (0 > x1[2]):
        theta = np.arccos(x0[1] / rad)
    else:
        theta = np.arccos(2 * np.pi - x0[1] / rad)
    
    #   unit vector of B, at pos. x1
    vec = ([rad, theta, x1[0]])
    unit = vec / np.linalg.norm(vec)
    t = q * dt * B(x1, R) * unit / (2 * m * r1)
    
    s = t * 2 / (1 + pow(np.linalg.norm(t), 2))
    v2 = v1 + np.cross((v1 + np.cross(v1, t)), s)
    vf = v2 + q * dt * E/ (2 * m)
    rf = Lor(np.linalg.norm(vf / c))
    xf = x1 + vf * dt / (2 * rf)

    Pos = np.vstack([Pos, xf])
    V = np.vstack([V, vf])
    x0 = xf
    v0 = vf
    r0 = rf
    i = i + 1
    T = np.append(T, i)

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
plt.plot(Pos.T[1], Pos.T[2])
plt.subplot(3, 3, 9)
plt.plot(Pos.T[0], Pos.T[2])

plt.show()
