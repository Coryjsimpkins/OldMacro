import numpy as np
import matplotlib.pyplot as plt

A = 1
th = 0.4
b = 0.96
d = 0.1

i = 0

kss = ((((1-b)/b) + d) / (A*th))**(1/(th-1))
css = A * (kss)**(th) - d * kss

runs = 0

cl = 0
ch = kss

k = []
c = []
k.append(kss/2)
c.append(0)

k[0] = kss/2
done = False 

while(done == False):
    runs += 1
    
    for i in range(5000):
        c[0] = (cl + ch)/2
        if i > 0:
            k.append(k[i-1] - d*k[i-1] + (A * k[i-1]**(th)) - c[i-1])
            c.append(c[i-1] * b * ((A * th * k[i-1]**(th-1)) + 1 - d))
        if np.absolute(c[i] - css) < 10**(-4):
            csolution = c
            ksolution = k
            done = True
            break
        if c[i] > css:
            ch = c[0]
            k = []
            c = []
            k.append(kss/2)
            c.append(0)
            break
        
        if c[i] < c[0]:
            cl = c[0]
            k = []
            c = []
            k.append(kss/2)
            c.append(0)
            break
        
plt.plot(ksolution)
plt.show()

plt.plot(csolution)
plt.show()





A = 1
th = 0.4
b = 0.96
d = 0.1

i = 0

kss = ((((1-b)/b) + d) / (A*th))**(1/(th-1))
css = A * (kss)**(th) - d * kss

runs = 0

cl = 0
ch = 10

k = []
c = []
k.append(kss * 2)
c.append(0)

k[0] = kss * 2
done = False 

while(done == False):
    runs += 1
    
    for i in range(5000):
        c[0] = (cl + ch)/2
        if i > 0:
            k.append(k[i-1] - d*k[i-1] + (A * k[i-1]**(th)) - c[i-1])
            c.append(c[i-1] * b * ((A * th * k[i-1]**(th-1)) + 1 - d))
        if np.absolute(c[i] - css) < 10**(-4):
            csolution = c
            ksolution = k
            done = True
            break
        if c[i] < css:
            cl = c[0]
            k = []
            c = []
            k.append(kss * 2)
            c.append(0)
            break
        
        if c[i] > c[i-1]:
            ch = c[0]
            k = []
            c = []
            k.append(kss * 2)
            c.append(0)
            break
        
plt.plot(ksolution)
plt.show()

plt.plot(csolution)
plt.show()





