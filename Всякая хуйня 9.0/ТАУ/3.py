import matplotlib.pyplot as plt
import math
from scipy import signal
import numpy as np

step=0.001
min=10**-1
max=10**1

n1=[0.63]
n2 = [0.54, -1]
n3 = [1.48**2, 2*0.52*1.48, 1]
d1 = [1.03, -1]
d2 = [1.05**2, 2*0.75*1.05, 1]
d3 = [0.94**2, 2*0.37*0.94, 1]
d4=[1,0]
d5=[1,0]

num_total = np.polymul(np.polymul(n1, n2), n3)
den_total = np.polymul(np.polymul(d1, d2), np.polymul(d3, np.polymul(d4, d5)))
system = signal.TransferFunction(num_total, den_total)

w = np.logspace(-1, 1, 1000)
w, A, phi = signal.bode(system, w)
phi=[p-360 for p in phi]
w2=[min,0.68,0.95,0.97,1.06,1.85,max]
A2=[20*math.log10(0.63/(min**2))]
A2.append(A2[-1]-40*math.log10(0.68/min))
A2.append(A2[-1])
A2.append(A2[-1]-40*math.log10(0.97/0.95))
A2.append(A2[-1]-60*math.log10(1.06/0.97))
A2.append(A2[-1]-100*math.log10(1.85/1.06))
A2.append(A2[-1]-80*math.log10(max/1.85))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.semilogx(w,A,color='red',ls=':')
ax1.semilogx(w2,A2,color='red')
ax2.semilogx(w,phi,color='blue')
ax1.semilogx([10**-1,10**1],[0,0],color='black')
ax1.grid()
ax2.grid()
ax1.set_ylim(-40,40)
ax2.set_ylim(-360,0)
ax2.invert_yaxis()

plt.show()


"""
#phi=[p-360 for p in phi]
A=[20*math.log10(0.63)
   +20*math.log10(math.sqrt((0.54**2)*(x**2)+1))
   -20*math.log10(math.sqrt((1.03**2)*(x**2)+1))
   -20*math.log10(math.sqrt((1-(1.05**2)*(x**2))**2+(2*0.75*1.05*x)**2))
   -20*math.log10(math.sqrt((1-(0.94**2)*(x**2))**2+(2*0.37*0.94*x)**2))
   +20*math.log10(math.sqrt((1-(1.48**2)*(x**2))**2+(2*0.52*1.48*x)**2))
    for x in w]

phi=[((
    -math.atan(0.54*x)
    +math.atan(1.03*x)
    -math.atan((2*0.75*1.05*x)/(1-(1.05**2)*(x**2)))
    -math.atan((2*0.37*0.94*x)/(1-(0.94**2)*(x**2)))
    +math.atan((2*0.52*1.48*x)/(1-(1.48**2)*(x**2)))
    )/math.pi*180)
    for x in w]

phi=[p-180 if p>=180 else p for p in phi]
#phi=[p+180 if p<10 else p for p in phi[:700]]+phi[700:]
"""

#ax2.semilogx(w,phi)
