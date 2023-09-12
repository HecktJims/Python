import numpy as np
import matplotlib.pyplot as plt

g = 9.8
L = 1
m = 1
phi = 90
omega = 2*np.pi/17
dt = 0.0005

time = np.array([0.])

y1 = np.array([0.,0.,0.,0.,0.])
y2 = np.array([0.,0.,0.,0.,0.])
y3 = np.array([0.,0.,0.,0.,0.])
y4 = np.array([0.,0.,0.,0.,0.])

posx = np.array([0.1])
posy = np.array([0.])
vx = np.array([0.])
vy = np.array([(0.28)])
print('L, posx, vy', L, posx, vy)

i=0
while (time[i] < 8):

    y1[1] = vx[i]
    y2[1] = 2*omega*vy[i]*np.sin(phi)-(g/L)*posx[i]
    y3[1] = vy[i]
    y4[1] = -2*omega*vx[i]*np.sin(phi)-(g/L)*posy[i]
    
    y1[2] = vx[i]+y2[1]*dt/2
    y2[2] = 2*omega*(vy[i]+y4[1]*dt/2)*np.sin(phi)-(g/L)*(posx[i]+y1[1]*dt/2)
    y3[2] = vy[i]+y4[1]*dt/2
    y4[2] = -2*omega*(vx[i]+y2[1]*dt/2)*np.sin(phi)-(g/L)*(posy[i]+y3[1]*dt/2)

    y1[3] = vx[i]+y2[2]*dt/2
    y2[3] = 2*omega*(vy[i]+y4[2]*dt/2)*np.sin(phi)-(g/L)*(posx[i]+y1[2]*dt/2)
    y3[3] = vy[i]+y4[2]*dt/2
    y4[3] = -2*omega*(vx[i]+y2[2]*dt/2)*np.sin(phi)-(g/L)*(posy[i]+y3[2]*dt/2)
    
    y1[4] = vx[i]+y2[3]*dt
    y2[4] = 2*omega*(vy[i]+y4[3]*dt)*np.sin(phi)-(g/L)*(posx[i]+y1[3]*dt)
    y3[4] = vy[i]+y4[3]*dt
    y4[4] = -2*omega*(vx[i]+y2[3]*dt)*np.sin(phi)-(g/L)*(posy[i]+y3[3]*dt)
   
    y1[0] = (y1[1]+2*y1[2]+2*y1[3]+y1[4])/6
    y2[0] = (y2[1]+2*y2[2]+2*y2[3]+y2[4])/6
    y3[0] = (y3[1]+2*y3[2]+2*y3[3]+y3[4])/6
    y4[0] = (y4[1]+2*y4[2]+2*y4[3]+y4[4])/6
    
    posx = np.append(posx, posx[i] + y1[0]*dt)
    posy = np.append(posy, posy[i] + y3[0]*dt)
    vx = np.append(vx, vx[i] + y2[0]*dt)
    vy = np.append(vy, vy[i] + y4[0]*dt)
    
    time = np.append(time, time[i] +dt)
    
    i = i+1
    
    
'''
sampling_rate = int(1/0.0005)
fft_size = len(posx)
ydata_fft = np.fft.rfft(posx) 
freqs_x1 = np.linspace(0, sampling_rate/2, fft_size/2 +1)
'''
plt.figure(1)
plt.plot( posx, posy, '-', label='Simulation')
plt.xlabel( "Position_x (m)" )
plt.ylabel( "Position_y (m)" )
plt.legend()
plt.show()
'''
plt.figure(2)
plt.plot( time, posx, '-', label='Simulation')
plt.xlabel( "Time (t)" )
plt.ylabel( "Position_x (m)" )
plt.legend()
plt.show()

plt.figure(3)
plt.plot( time, posy, '-', label='Simulation')
plt.xlabel( "Time (t)" )
plt.ylabel( "Position_y (m)" )
plt.legend()
plt.show()

plt.figure(4)
plt.plot( freqs_x1[0:80], ((ydata_fft.real[0:80]/fft_size)**2), '-', label='w1')
plt.xlabel("Frequency (Hz)")
plt.ylabel("(fft.x posisiton)^2")
plt.legend()
plt.show()

plt.figure(5)
plt.plot( freqs_x1[0:80], (ydata_fft.real[0:80]/fft_size), '-', label='w1')
plt.xlabel("Frequency (Hz)")
plt.ylabel("fft.x posisiton (mm)")
plt.legend()
plt.show()

np.savetxt('1.txt',time)
np.savetxt('2.txt',posx)
np.savetxt('3.txt',(ydata_fft.real[0:80]/fft_size)**2)
np.savetxt('4.txt',freqs_x1[0:80])
'''