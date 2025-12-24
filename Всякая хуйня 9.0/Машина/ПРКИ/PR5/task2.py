import math
X=[
    (2,[0.9,0.1]),
    (3,[0.8,0.1]),
    (7,[0.3,0.7]),
    (9,[0.1,0.9]),
    (2,[0.9,0.1]),
    (1,[0.8,0.2]),
    ]
k=2
M=[sum(x[0]*x[1][kit]for x in X)/sum([x[1][kit] for x in X]) for kit in range(k)]
print(M)

x=5
M=[2,7]
std=[1,1]
C=[0.5,0.5]
f=[(1/(math.sqrt(2*math.pi)*std[kit]))*math.exp(-pow(x-M[kit],2)/(2*std[kit]**2)) for kit in range(k)] 
P=[f[kit]*C[kit]/sum(f[kk]*C[kk]for kk in range(k))for kit in range(k)]
print(P)