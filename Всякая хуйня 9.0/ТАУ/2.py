import matplotlib.pyplot as plt
import math
from scipy import signal
import numpy as np

step=0.001
min=10**-1
max=10**1

n1=[0.39]
n2 = [0.54, -1]
n3 = [1.48**2, 2*0.52*1.48, 1]
d1 = [0.92, -1]
d2 = [0.65**2, 2*0.46*0.65, 1]
d3 = [1.26**2, 2*0.58*1.26, 1]

num_total = np.polymul(np.polymul(n1, n2), n3)
den_total = np.polymul(np.polymul(d1, d2), d3)
system = signal.TransferFunction(num_total, den_total)

w = np.logspace(-1, 1, 1000)
w, A, phi = signal.bode(system, w)

w2=[min,0.68,0.79,1.09,1.54,1.85,max]
A2=[20*math.log10(0.39)]
A2.append(A2[-1])
A2.append(A2[-1]+40*math.log10(0.79/0.68))
A2.append(A2[-1])
A2.append(A2[-1]-20*math.log10(1.54/1.09))
A2.append(A2[-1]-60*math.log10(1.85/1.54))
A2.append(A2[-1]-40*math.log10(max/1.85))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.semilogx(w,A,color='red',ls=':')
ax1.semilogx(w2,A2,color='red')
ax2.semilogx(w,phi,color='blue')
ax1.semilogx([10**-1,10**1],[0,0],color='black')
ax1.grid()
ax2.grid()
ax1.set_ylim(-60,20)
ax2.set_ylim(-270,90)
ax2.invert_yaxis()

plt.show()