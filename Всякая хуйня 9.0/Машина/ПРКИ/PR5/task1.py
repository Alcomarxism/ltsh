import numpy as np

D=[2, 4, 10, 12, 3, 20, 30, 11, 25]
startM=[2, 4, 6]

def kMeans(D,startM,iters):
    M=startM
    for i in range(iters):
        clust=[[] for j in range(len(M))]
        for d in D:
            delt=[(d-m)**2 for m in M]
            clust[delt.index(min(delt))].append(d)
        M=[float(np.mean(cl)) for cl in clust]
    return (clust,M)

clust,M=kMeans(D,startM,1)
print(clust)
print(M)