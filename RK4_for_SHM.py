import numpy as np
import matplotlib.pyplot as plt

x0 = 2
v0 = 0
#be = 0.3
w0 = 1

q = w0**2

tmin , tmax , dt = 0, 10 , 0.1

t = np.arange(tmin , tmax , dt)

nt = t.size

x = np.zeros(nt)
v = np.zeros(nt)
a = np.zeros(nt)
x[0]=x0
v[0]=v0
a[0]=-q*x0

N = float(input("N="))


while N==1: 

    for i in range(nt-1):
        
        kx1 = v[i]
        kv1 = -q * x[i]
        kx2 = v[i] + kv1 * dt/2
        kv2 = -q * (x[i] + kx1 * dt/2)
        kx3 = v[i] + kv2 * dt/2
        kv3 = -q * (x[i] + kx2 * dt/2)
        kx4 = v[i] + kv3 * dt
        kv4 = -q * (x[i] + kx3 * dt)
        
        x[i+1] = x[i] + dt*(kx1+2*kx2+2*kx3+kx4)/6
        v[i+1] = v[i] + dt*(kv1+2*kv2+2*kv3+kv4)/6
    
    break

    
while N==2:    
    
    for j in range(nt-1):
        x[j+1]=x[j]+v[j]*dt
        v[j+1]=v[j]+a[j]*dt
        a[j+1]=-q*x[j+1]

    break

print(x[1],x[2],x[3],x[4])
print(x, v)
    

fig = plt.figure(figsize=(6, 6), dpi=100)
ax = fig.gca()
plt.title("x - t")
line, = ax.plot(t, x, color='blue', linestyle='-', linewidth=2)
dot, = ax.plot([], [], color='red', marker='o', markersize=7, markeredgecolor='black', linestyle='')
plt.grid(color = 'green', linestyle = '--', linewidth = 1)
ax.set_xlabel('t[sec]', fontsize=14)
ax.set_ylabel('x[m]', fontsize=14)

fig = plt.figure(figsize=(6, 6), dpi=100)
ax = fig.gca()
plt.title("v - t")
line, = ax.plot(t, v, color='blue', linestyle='-', linewidth=2)
dot, = ax.plot([], [], color='red', marker='o', markersize=7, markeredgecolor='black', linestyle='')
plt.grid(color = 'green', linestyle = '--', linewidth = 1)
ax.set_xlabel('t[sec]', fontsize=14)
ax.set_ylabel('v[m/s]', fontsize=14)

plt.show()