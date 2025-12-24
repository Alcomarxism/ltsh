import math
from sklearn import cluster

D = [
    [5, 8],
    [6, 7],
    [6, 5],
    [2, 4],
    [3, 4],
    [5, 4],
    [7, 4],
    [9, 4],
    [3, 3],
    [8, 2],
    [7, 5]
]

def Linf(x,y):
    return max(abs(x[0]-y[0]),abs(x[1]-y[1]))
def Lh(x,y):
    return math.pow(math.sqrt(abs(x[0]-y[0]))+math.sqrt(abs(x[1]-y[1])),2)
def Lmin(x,y):
    return min(abs(x[0]-y[0]),abs(x[1]-y[1]))
def Lpow(x,y):
    return math.sqrt((x[0]-y[0])**2+2*((x[1]-y[1])**2))

eps=2
min_samples=5
metric=Linf
neibs=[sum([1 if metric(d,dd)<=eps and dd!=d else 0 for dd in D]) for d in D]
core=[chr(ord('a')+i) for i in  range(len(neibs)) if neibs[i]>=min_samples ]
print("Core:",core)
clust=cluster.DBSCAN(eps=eps,min_samples=min_samples,metric=metric).fit(D)
bord=[]
for i in range(len(clust.labels_)):
    if clust.labels_[i]>=0 and chr(ord('a')+i) not in core:
        bord.append(chr(ord('a')+i))
print("Border:",bord)
for i in [it+min(clust.labels_) for it in range(len(set(clust.labels_)))]:
    print(i,":",[chr(ord('a')+j) for j in range(len(neibs)) if clust.labels_[j]==i ])


eps=4
min_samples=3
metric=Lh
neibs=[sum([1 if metric(d,dd)<=eps and dd!=d else 0 for dd in D]) for d in D]
core=[chr(ord('a')+i) for i in  range(len(neibs)) if neibs[i]>=min_samples ]
print("Core:",core)
clust=cluster.DBSCAN(eps=eps,min_samples=min_samples,metric=metric).fit(D)
bord=[]
for i in range(len(clust.labels_)):
    if clust.labels_[i]>=0 and chr(ord('a')+i) not in core:
        bord.append(chr(ord('a')+i))
print("Border:",bord)
for i in [it+min(clust.labels_) for it in range(len(set(clust.labels_)))]:
    print(i,":",[chr(ord('a')+j) for j in range(len(neibs)) if clust.labels_[j]==i ])

eps=1
min_samples=6
metric=Lmin
neibs=[sum([1 if metric(d,dd)<=eps and dd!=d else 0 for dd in D]) for d in D]
core=[chr(ord('a')+i) for i in  range(len(neibs)) if neibs[i]>=min_samples ]
print("Core:",core)
clust=cluster.DBSCAN(eps=eps,min_samples=min_samples,metric=metric).fit(D)
bord=[]
for i in range(len(clust.labels_)):
    if clust.labels_[i]>=0 and chr(ord('a')+i) not in core:
        bord.append(chr(ord('a')+i))
print("Border:",bord)
for i in [it+min(clust.labels_) for it in range(len(set(clust.labels_)))]:
    print(i,":",[chr(ord('a')+j) for j in range(len(neibs)) if clust.labels_[j]==i ])

eps=4
min_samples=6
metric=Lpow
neibs=[sum([1 if metric(d,dd)<=eps and dd!=d else 0 for dd in D]) for d in D]
core=[chr(ord('a')+i) for i in  range(len(neibs)) if neibs[i]>=min_samples ]
print("Core:",core)
clust=cluster.DBSCAN(eps=eps,min_samples=min_samples,metric=metric).fit(D)
bord=[]
for i in range(len(clust.labels_)):
    if clust.labels_[i]>=0 and chr(ord('a')+i) not in core:
        bord.append(chr(ord('a')+i))
print("Border:",bord)
for i in [it+min(clust.labels_) for it in range(len(set(clust.labels_)))]:
    print(i,":",[chr(ord('a')+j) for j in range(len(neibs)) if clust.labels_[j]==i ])