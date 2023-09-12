import math

k = 8987551787.3681764                            # 庫倫常數
a = 10                                            # 邊長
d = 0.1                                           # 間距
L = z = a / 2                                     # 半邊長
r = a / d                                         # 次數 
x = y = -L + d/2                                  # 以每格之中心點值代表
i = j = T = t = 0

for i in range(int(r)-1):                         # 計算與xy平面平行的一面再*6
    for j in range(int(r)-1):
        t = 1/(pow(x,2) + pow(y,2) + pow(z,2))    # 1/r^2 = 1/(rx^2+ry^2+rz^2)
        T = T + t
        x = x + d
        j += 1
        
    y = y + d
    j = 0
    x = -L + d/2
    i += 1

A = 6 * k * 1 * pow(d,2) * T                       # 6*kQ*A^2/r^2
Ans = 1 / A
print('邊長為', a, '間距', d, '相差', (a/d), '倍')
print('E0 =', Ans, '誤差', (100-(Ans * 4 * k * math.pi*100)), '%')
