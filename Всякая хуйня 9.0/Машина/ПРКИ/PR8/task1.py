import numpy as np

D = [
    [4,2.9,1],
    [3.5,4,1],
    [2.5,1,-1],
    [2,2.1,-1]
]

Dp=np.array([d[:-1] for d in D if d[-1]==1]).transpose()
Dn=np.array([d[:-1] for d in D if d[-1]==-1]).transpose()
mup=np.mean(Dp,axis=1)
mun=np.mean(Dn,axis=1)
print(mup)
print(mun)
mudelt=np.matrix(mup-mun)
B=np.dot(mudelt.transpose(),mudelt)
print(B)
Sp=len(Dp)*np.cov(Dp,ddof=0)
Sn=len(Dn)*np.cov(Dn,ddof=0)
S=Sp+Sn
print(Sp)
print(Sn)
print(S)
S = S + 1e-6 * np.eye(S.shape[0])
SiB=np.dot(np.linalg.inv(S),B)
eig=np.linalg.eigh(SiB)
print(eig.eigenvalues)
print(eig.eigenvectors)
w=eig.eigenvectors[1]
t=np.dot(w,(mup+mun)/2)
print(t*w)