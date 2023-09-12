import numpy as np

a = 23
b = 109
alt = a * np.pi / 180
Az = b * np.pi / 180
g = 24.970565 * np.pi / 180
w = 121.195618

H = w * np.pi / 180

A = np.sin(g) * np.sin(alt) + np.cos(g) * np.cos(alt) * np.cos(Az)
B = np.arcsin(A)
C = np.sin(g) * np.cos(alt) * np.cos(Az) - np.cos(g) * np.sin(alt)
D = np.arccos(C / np.cos(H))
E = np.sin(Az) * np.cos(alt)
F = np.arccos(E / np.sin(H))

print(B, D, F)
print(B / np.pi * 180, D / np.pi * 180, F / np.pi * 180)