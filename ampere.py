import math

c = 1
I = 1

i = x = y = z = 0
th = 2 * math.pi / 100
l = 2 * math.pi * 1 / 100
Tx = Ty = Tz = 0

for i in range(100):
    
    x = 0 - math.cos(i * th)
    y = 2 - math.sin(i * th)
    z = 0.6 - 0
    r = pow((pow(x,2) + pow(y,2) + pow(z,2)), 0.5)
    bx = (math.cos(i * th)) * z * I * l / pow(r,3)
    by = (math.sin(i * th)) * z * I * l / pow(r,3)
    bz = -(math.sin(i * th) * y + math.cos(i * th) * x) * I * l / pow(r,3)
    
    Tx = Tx + bx
    Ty = Ty + by
    Tz = Tz + bz

print(c * Tx,c * Ty,c * Tz)