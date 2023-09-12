#import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = X = xdata = np.array([])
y = Y = ydata = np.array([])
R = np.array([])
#tha = thb = 
th0 = np.array([])

for line in open('oval.txt', 'r', encoding='UTF-8'):
    
    row = np.asarray(line.split())
    temp = row.astype(np.float)
    
    x = np.append(x, temp[0])
    y = np.append(y, temp[1])
    
    r = (temp[0]**2 + temp[1]**2)**0.5
    #th = np.arcsin(temp[1] / r)
    th = np.arccos(temp[0] / r)
    
    X = np.append(X, th)
    Y = np.append(Y, r)
      
plt.subplot(221)    
plt.plot(x, y)
plt.subplot(222)  
plt.plot(X, Y)

i = 1               #找端點 算R
for i in range (len(Y) - 1):    
    if Y[i] > Y[i-1] and Y[i] > Y[i+1]:
        
        th0 = np.append(th0, X[i])
        R = np.append(R, Y[i])
        plt.plot(X[i], Y[i], 'ro', markersize=3.5)
        xdata = np.append(xdata, x[i])
        ydata = np.append(ydata, y[i])
        #M = np.matrix((R, th0, xdata, ydata))
'''  
print(R, th0, xdata, ydata)
N = [(R(i), th0(i), xdata(i), ydata(i))for n in np.argsort(R)]
print (N)

s = R.sort()        #排序 算a,b
a = (R[0] + R[1] + R[2] + R[3] + R[4] + R[5] + R[6])/7
b = (R[7] + R[8] + R[9] + R[10] + R[11] + R[12] + R[13])/7

def fun(x, p):
   return ((a * np.cos(p))**2 + (b * np.sin(p))**2 - (x**2))**0.5

#def func(x)
#   return (b * b - (x**2 * b**2 / a**2))**0.5

popt, pcov = curve_fit(fun, x1data, y1data)

plt.subplot(223)
plt.plot(x1data, y1data)
plt.plot(x1data, fun(x1data, *popt), 'r--', label='fitting' )
print(popt)

popt, pcov = curve_fit(fun, x2data, y2data)

plt.subplot(224)
plt.plot(x2data, y2data)
plt.plot(x2data, fun(x2data, *popt), 'r--', label='fitting' )
print(popt)
'''
plt.show()