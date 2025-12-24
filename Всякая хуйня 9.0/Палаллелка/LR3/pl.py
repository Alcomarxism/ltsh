import matplotlib.pyplot as plt
import numpy as np
pNum=[1,2,4,8,16,32]
le=[3 ,30,3000]
pTime=[[0.01,0.01,0.01,0.01,0.4,2.23],
       [0.01,0.01,0.01,0.01,0.34,2.28],
       [0.01,0.01,0.01,0.01,0.49,2.01]
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
