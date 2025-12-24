import matplotlib.pyplot as plt
import numpy as np
pNum=[1,2,4,8,16,32,64]
m=[10,50,100,200,500,1000]
pTime=[[0.004,0.787,4,35,516,4099],
       [0.045,0.528,3,20,286,2172],
       [0.277,0.783,2,12,162,1277],
       [1.071,1.395,4,12,192,1190],
       [3.327,4.057,4,17,201,1247],
       [8.027,7.766,10,25,217,1693],
       [20.695,30.077,34,80,360,1884]
        ]
pTime2=np.array(pTime).transpose()
for d in pTime2:
    plt.plot(pNum,d)
plt.legend(m)
plt.xlabel("Количество процессов")
plt.ylabel("Время выполнения (мс)")
plt.grid()
plt.show()

for d in pTime:
    plt.plot(m,d)
plt.legend(pNum,loc='upper left')
plt.xlabel("Размерность матрицы")
plt.ylabel("Время выполнения (мс)")
plt.grid()
plt.show()

slw=[]
for d in pTime2:
    slw.append([d[0]/dd for dd in d])
for d in slw:
    plt.plot(pNum,d)
plt.legend(m,loc='upper right')
plt.xlabel("Количество процессов")
plt.ylabel("Ускорение")
plt.grid()
plt.show()
