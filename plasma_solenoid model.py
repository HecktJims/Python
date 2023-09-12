#solenoid model, no E
import numpy as np
import matplotlib.pyplot as plt

#   velocity in lightspeed unit
x = np.array([0., 0., 0.])
vi = np.array([0., 0., -0.6])
dt = 0.001
t = 5
n = t / dt

#   no electric field
E = np.array([0., 0., 0.])

#   solenoid constant magnetic field
def B(p, v):
    R = 1e-2    #   meter
    B = 1e-10    #   T = Wb/m2 
#    unit = v / np.linalg.norm(v)
    trace = np.dot(p, v) / np.linalg.norm(v)
    if (trace > R):
        return 0
    else:
        return B

'''
A_str = vi[1]
B_str = E[1]
C_str = B[2]
'''

#   Lorentz tansform for velocity
def Lor(v):
    r = pow(1 - pow(v, 2), 0.5)
    return r

#   in SI unit
q = -1.602e-19  #   C
m = 9.109e-31   #   kg
c = 299792458   #   m/s
T = [0.]

'''
w = q * np.linalg.norm(B) / m
ro = 1 / w
'''

x0 = Pos = x
v0 = V = vi * c
r0 = Lor(np.linalg.norm(v0 / c))
#r0 = pow(1 - pow(np.linalg.norm(v0), 2), 0.5)

#   Boris method, relativity velocity included
for i in range (int(n)):
    x1 = x0 + v0 * dt / (2 * r0)
    v1 = v0 + q * dt * E/ (2 * m)
    r1 = Lor(np.linalg.norm(v1 / c))
    unit = v0 / np.linalg.norm(v0)
    t = q * dt * B(x0, v0) * unit / (2 * m * r1)
    s = t * 2 / (1 + pow(np.linalg.norm(t), 2))
    v2 = v1 + np.cross((v1 + np.cross(v1, t)), s)
    vf = v2 + q * dt * E/ (2 * m)
    rf = Lor(np.linalg.norm(vf / c))
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

'''
x0 = Pos = x
v0 = V = vi * c
r0 = pow(1 - pow(np.linalg.norm(v0 / c), 2), 0.5)

#   Boris method, relativity velocity included
for i in range (int(n)):
    x1 = x0 + v0 * dt / (2 * r0)
    v1 = v0 + q * dt * E/ (2 * m)
    r0 = pow(1 - pow(np.linalg.norm(v1 / c), 2), 0.5)
    t = q * dt * B / (2 * m * r1)
    s = t * 2 / (1 + pow(np.linalg.norm(t), 2))
    v2 = v1 + np.cross((v1 + np.cross(v1, t)), s)
    vf = v2 + q * dt * E/ (2 * m)
    r0 = pow(1 - pow(np.linalg.norm(vf / c), 2), 0.5)
    xf = x1 + vf * dt / (2 * rf)

    Pos = np.vstack([Pos, xf])
    V = np.vstack([V, vf])
    x0 = xf
    v0 = vf
    r0 = rf
    i = i + 1
    T = np.append(T, i)
'''

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
'''
plt.title("Const. E & B field")
plt.xlabel("vy = %.2E c, Bz = %.2E T, Ey = %.2E V/m" % (A_str, C_str, B_str))

vx_expect = np.linalg.norm(E) / np.linalg.norm(B)
print(w,"\n", ro,"\n", vx_expect)
'''
plt.show()
