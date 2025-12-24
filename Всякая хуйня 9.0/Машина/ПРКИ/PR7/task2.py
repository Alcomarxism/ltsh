import scipy.stats
m1=[1, 3]
m2=[5, 5]
cov1=[[5, 3],
      [3, 2]]
cov2=[[2, 0],
      [0, 1]]

point=[3,4]
Pc1=0.5
Pc2=0.5
c1=scipy.stats.multivariate_normal(m1,cov1)
c2=scipy.stats.multivariate_normal(m2,cov2)
PpointInc1=c1.pdf(point)*Pc1
PpointInc2=c2.pdf(point)*Pc2
print(PpointInc1,PpointInc2)
if(PpointInc1>PpointInc2):
    print("Класс с1")
else:
    print("Класс с2")