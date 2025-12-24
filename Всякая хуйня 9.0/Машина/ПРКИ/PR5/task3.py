import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage

X=[
    [1,0,1,1,0],
    [1,1,0,1,0],
    [0,0,1,1,0],
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,1,1,0,0]
    ]
points = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']

N11=[[sum([1 if x1[i] and x2[i] else 0 for i in range(len(x1))])for x2 in X]for x1 in X ]
N10=[[sum([1 if x1[i] and (not x2[i]) else 0 for i in range(len(x1))])for x2 in X]for x1 in X ]
N01=[[sum([1 if (not x1[i]) and x2[i] else 0 for i in range(len(x1))])for x2 in X]for x1 in X ]
N00=[[sum([1 if (not x1[i]) and (not x2[i]) else 0 for i in range(len(x1))])for x2 in X]for x1 in X ]

SMC=[[1-(N11[i][j]+N00[i][j])/(N11[i][j]+N10[i][j]+N01[i][j]+N00[i][j])for j in range(len(X))]for i in range(len(X))]
JC=[[1-N11[i][j]/(N11[i][j]+N10[i][j]+N01[i][j])for j in range(len(X))]for i in range(len(X))]
RC=[[0 if i==j else(1-N11[i][j]/(N11[i][j]+N10[i][j]+N01[i][j]+N00[i][j]))for j in range(len(X))]for i in range(len(X))]

linkage_rc = linkage(squareform(RC), method='single')
dendrogram(linkage_rc, labels=points)
plt.show()

linkage_smc = linkage(squareform(SMC), method='complete')
dendrogram(linkage_smc, labels=points)
plt.show()

linkage_jc = linkage(squareform(JC), method='centroid')
dendrogram(linkage_jc, labels=points)
plt.show()
