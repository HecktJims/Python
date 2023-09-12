import numpy as np
import matplotlib.pyplot as plt

#   velocity in lightspeed unit
x = np.array([0., 0., 0.])
vi = np.array([1e-2, 0., 0.])
dt = 0.001
t = 10
n = t / dt

#   constant E & B field
E = np.array([0., 1e2, 0.])
B = np.array([0., 0., 1e2])

A_str = vi[1]
B_str = E[1]
C_str = B[2]

'''
def E
def B
'''

'''
q = -1          #   e
m = 5.486-4     #   amu
T = [0.]

#   in cgs unit
q = -1 * 3e9
m = 9.109e-28
T = [0.]
'''

#   in SI unit
q = -1.602e-19  #   C
m = 9.109e-31   #   kg
c = 299792458   #   m/s
T = [0.]

'''
#   Lorentz tansform for velocity
def Lor(v):
    r = pow(1 - pow(v, 2), 0.5)
    return r

#   Boris method
def Boris(x0, v0, r0, dt, q, m):
    x1 = x0 + v0 * dt / (2 * r0)
    v1 = v0 + q * dt * E / (2 * m)      -
    r1 = Lor(np.linalg.norm(v1))
    t = q * dt * B / (2 * m * r1)       -
    s = t * 2 / (1 + pow(np.linalg.norm(t), 2))
    v2 = v1 + np.cross((v1 + np.cross(v1, t)), s)
    vf = v2 + q * dt * E / (2 * m)      -
    v_avg = (v0 + vf) / (2 * r1)
    
    rf = Lor(np.linalg.norm(vf))
    xf = x1 + vf * dt / (2 * Lor(rf))
    return 
'''
x0 = Pos = x
v0 = V = vi * c
#r0 = Lor(np.linalg.norm(v0))
r0 = pow(1 - pow(np.linalg.norm(v0 / c), 2), 0.5)

for i in range (int(n)):
    x1 = x0 + v0 * dt / (2 * r0)
    v1 = v0 + q * dt * E / (2 * m)
#    r1 = Lor(np.linalg.norm(v1))
    r1 = pow(1 - pow(np.linalg.norm(v1 / c), 2), 0.5)
    t = q * dt * B / (2 * m * r1)
    s = t * 2 / (1 + pow(np.linalg.norm(t), 2))
    v2 = v1 + np.cross((v1 + np.cross(v1, t)), s)
    vf = v2 + q * dt * E / (2 * m)
#    rf = Lor(np.linalg.norm(vf))
    rf = pow(1 - pow(np.linalg.norm(vf / c), 2), 0.5)
    xf = x1 + vf * dt / (2 * rf)
#    print(x0, "\n", x1, "\n", xf, "\n\n", v0, "\n", v1, "\n", v2, "\n", vf, "\n\n",
#          r0, "\n", r1, "\n", rf, "\n\n\n")
    
    Pos = np.vstack([Pos, xf])
    V = np.vstack([V, vf])
    x0 = xf
    v0 = vf
    r0 = rf
    i = i + 1
    T = np.append(T, i)

#   correct time and velocity
T = T * dt
#V = V / c
#print(T)
#print(Pos, "\n\n", V)

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

'''
plt.subplot(3, 3, 1)
plt.plot(T, Pos.T[0])
plt.subplot(3, 3, 2)
plt.plot(T, Pos.T[1])
plt.subplot(3, 3, 3)
plt.plot(T, Pos.T[2])

plt.subplot(3, 3, 4)
plt.plot(T, V.T[0])
plt.subplot(3, 3, 5)
plt.plot(T, V.T[1])
plt.subplot(3, 3, 6)
plt.plot(T, V.T[2])
'''

plt.subplot(3, 3, 7)
plt.plot(Pos.T[0], Pos.T[1])
plt.subplot(3, 3, 8)
plt.plot(V.T[0], V.T[1])
plt.subplot(3, 3, 9)
plt.plot(Pos.T[2], V.T[2])
plt.title("Const. E & B field")
plt.xlabel("vy = %.2E c, Bz = %.2E T, Ey = %.2E V/m" % (A_str, C_str, B_str))

plt.show()
