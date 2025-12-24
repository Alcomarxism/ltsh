import matplotlib.pyplot as plt
import numpy as np
pNum=[2,4,8,16,32]
le=[10,100,1000]
pTime=[[0.48, 1.05, 2.41, 4.65, 9.78],
       [0.45, 1.03, 2.33, 4.36, 9.43],
       [0.47, 1.11, 2.37, 4.42, 9.32]
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
plt.xlabel("Длинна сообщения")
plt.ylabel("Время выполнения (мс)")
plt.grid()
plt.show()

slw=[]
for d in pTime:
    slw.append([d[0]/dd for dd in d])
for d in slw:
    plt.plot(pNum,d)
plt.legend(le,loc='upper left')
plt.xlabel("Количество процессов")
plt.ylabel("Замедление")
plt.grid()
plt.show()
