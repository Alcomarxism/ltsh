import matplotlib.pyplot as plt
import numpy as np
pNum=[2,4,8,16,32]
le=[1 ,100,1000]
pTime=[[0.01,0.13,0.34,1.22,1.7],
       [0.01,0.1,0.22,0.32,4.77],
       [0.01,0.13,0.18,0.79,3.6]
        ]
for d in pTime:
    plt.plot(pNum,d)
plt.legend(le)
plt.xlabel("Количество процессов")
plt.ylabel("Время выполнения (мс)")
plt.grid()
plt.show()

pTime2=np.array(pTime).transpose()
for d in pTime2:
    plt.plot(le,d)
plt.legend(pNum,loc='upper left')
plt.xlabel("Количество пересылаемых чисел")
plt.ylabel("Время выполнения (мс)")
plt.grid()
plt.show()

slw=[]
for d in pTime:
    slw.append([d[0]/dd for dd in d[1:]])
for d in slw:
    plt.plot(pNum[1:],d)
plt.legend(le,loc='upper left')
plt.xlabel("Количество процессов")
plt.ylabel("Замедление")
plt.grid()
plt.show()
