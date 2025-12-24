import numpy as np
D = np.array([
    [4, 2.9, 1, 0.414],
    [4, 4, 1, 0],
    [1, 2.5, -1, 0],
    [2.5, 1, -1, 0.018],
    [4.9, 4.5, -1, 0],
    [1.9, 1.9, -1, 0],
    [3.5, 4, 1, 0.018],
    [0.5, 1.5, -1, 0],
    [2, 2.1, -1, 0.414],
    [4.5, 2.5, 1, 0]
])

w=np.sum([x[:2]*x[2]*x[3]for x in D],axis=0)
b=1/D[0][2]-np.dot(w,D[0][:2])
print(w[0],w[1],b)
dist=abs(w[0]*D[5][0]+w[1]*D[5][1]+b)/np.sqrt(w[0]**2+w[1]**2)
print(dist)
print(abs(w[0]*D[5][0]+w[1]*D[5][1]+b))
point=[3,3]
h=w[0]*point[0]+w[1]*point[1]+b
print(h)
if h>0:
    print('class +1')
else:
    print('class -1')