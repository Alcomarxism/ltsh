import numpy as np
import matplotlib.pyplot as plt 
#1
Xa1=[4, 2.5,3.5,4]
Xa2=[2.9,1,4,2.1]

Core=[]
for i in range(4):
    Core.append([])
    for j in range(4):
         Core[i].append((Xa1[i]-Xa1[j])**2+(Xa2[i]-Xa2[j])**2)

for a in Core:
    for b in a:
        print('%.2f' % b,end=' ')
    print()
print()

#2
D=np.array([[8,-20],
            [0,-1],
            [10,-19],
            [10,-20],
            [2,0]])
m=np.mean(D,axis=0)
print('D mean: ',m)
сovMat=np.cov(D.transpose())
print('Covariation matrix:\n',сovMat)
eig=np.linalg.eigh(сovMat)
lam1,lam2=max(eig.eigenvalues),min(eig.eigenvalues)
print('Eigenvalues: %.2f, %.2f'% (lam1,lam2))
print('Corelation matrix:\n',np.corrcoef(D.transpose()))
#3
pc1=eig.eigenvectors[0] if eig.eigenvalues[0]>eig.eigenvalues[1] else eig.eigenvectors[1]
pc2=eig.eigenvectors[1] if eig.eigenvalues[0]>eig.eigenvalues[1] else eig.eigenvectors[0]
print('pc1:',pc1)
print('pc2:',pc2)

print("Residual var for pc1: %.2f"%(sum(np.var(D,axis=0,ddof=1))-lam1))
print("Residual var for pc2: %.2f"%(sum(np.var(D,axis=0,ddof=1))-lam1-lam2))

vlen=10
plt.arrow(m[0],m[1],vlen*pc1[0],vlen*pc1[1],head_width=0.5, head_length=0.7,label='pc1',fc='red')
plt.arrow(m[0],m[1],vlen*pc2[0],vlen*pc2[1],head_width=0.5, head_length=0.7,label='pc2',fc='yellow')
plt.scatter(*D.transpose())
plt.grid()
plt.legend()
plt.xlabel('a1')
plt.ylabel('a2')
plt.show()