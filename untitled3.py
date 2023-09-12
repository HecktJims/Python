import numpy as np
import matplotlib.pyplot as plt

pl = 1 / 179740000  #   charge density, C/m
n = 8              #   define Inf as L = N * 15 r0, prefer 10

k = 8.987e9                 #   Nm^2/C^2
e0 = 1 / (4 * np.pi * k)    #   F/m  

r0 = pl / (2 * np.pi * e0)  #   nominal dist.
L = 10 * r0                 #   z = [-L,L]
dl = r0 / 100
q = pl * dl
#print(q, L)

M1 = (np.array(range(5))) - 5
M2 = (np.array(range(5))) + 1
X = np.concatenate([M1, M2])

Z = (np.array(range(31))) - 15

Char_z = ((np.array(range(2001))) - 1000) * dl

N = int(n * 1500)
Inf_z = ((np.array(range(2 * N + 1))) - N) * dl
#print(Inf_z)

plt.subplot(1, 2, 1)

i = j = k = l = 0
x = z = ex = ez = []
R = np.array([0., 0.])

for i in range(len(X)):
    for j in range(len(Z)):
        Et = 0
        for k in range(len(Char_z)):
            R[0] = r0 * X[i]
            R[1] = r0 * Z[j] - Char_z[k]
            E = k * pl * R / pow(np.linalg.norm(R), 3)
            Et = E + Et
        plt.quiver(X[i], Z[j], Et[0], Et[1], width = 2e-3)

plt.plot(np.zeros(len(Char_z)), Char_z / r0, 'ro', markersize=1)
plt.title("L = 10 r0")
plt.xlabel("x / r0")
plt.ylabel("z / r0")
plt.xticks(range(-6, 7, 1))
plt.yticks(range(-16, 18, 2))

plt.subplot(1, 2, 2)

i = j = k = 0
x = z = ex = ez = []
R = np.array([0., 0.])

for i in range(len(X)):
    for j in range(len(Z)):
        Et = 0
        for k in range(len(Inf_z)):
            R[0] = r0 * X[i]
            R[1] = r0 * Z[j] - Inf_z[k]
            E = k * pl * R / pow(np.linalg.norm(R), 3)
            Et = E + Et
        plt.quiver(X[i], Z[j], Et[0], Et[1], width = 2e-3, color='g')

#plt.plot(np.zeros(len(Inf_z)), Inf_z / r0, 'ro', markersize=1)

plt.title("L = %.1f r0" % (15 * n))
plt.xlabel("x / r0")
plt.ylabel("z / r0")
plt.xticks(range(-6, 7, 1))
plt.yticks(range(-16, 18, 2))

plt.show()