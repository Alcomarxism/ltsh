import numpy as np
import math
from sklearn import cluster
D=[
    [5, 8],
    [10, 8],
    [11, 8],
    [6, 7],
    [10, 7],
    [12, 7],
    [13, 7],
    [5, 6],
    [10, 6],
    [13, 6],
    [6, 5],
    [9, 4],
    [11, 5],
    [14, 6],
    [15, 5],
    [2, 4],
    [3, 4],
    [5, 4],
    [6, 4],
    [7, 4],
    [15, 4], 
    [3, 3],
    [7, 3],
    [8, 2],
]

eps=2
minPts=3
dist=[[math.sqrt((d[0]-dd[0])**2+(d[1]-dd[1])**2) for dd in D] for d in D]
neibs=[sum([1 if ds<=eps and ds>0 else 0 for ds in dst])for dst in dist]
core=[chr(ord('a')+i) for i in  range(len(neibs)) if neibs[i]>=minPts ]
print(core)
clust=cluster.DBSCAN(eps=eps,min_samples=minPts,metric="euclidean").fit(D)
for i in range(len(set(clust.labels_))):
    print(i,":",[chr(ord('a')+j) for j in range(len(neibs)) if clust.labels_[j]==i ])
