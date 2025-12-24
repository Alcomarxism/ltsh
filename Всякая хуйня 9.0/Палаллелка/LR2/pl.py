import matplotlib.pyplot as plt
import numpy as np
pNum=[1,2,4,8,16,32]
le=[5 ,50,5000]
pTime=[[0.01,0.27,0.5,1.03,2.53,5.99],
       [0.01,0.3,0.56,1.2,2.41,6.39],
       [0.01,0.31,0.62,1.23,2.42,6.2]
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
