import pandas as pd
import numpy as np
from sklearn import cluster
from sklearn import preprocessing
from sklearn import decomposition
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

def plotClusts(scaled_data,clustering):
    pca = decomposition.PCA(n_components = 2)
    pca_data = pca.fit_transform(scaled_data)

    unique_labels = set(clustering.labels_)
    core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = [0, 0, 0, 1]
        class_member_mask = clustering.labels_ == k
        xy = pca_data[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0],xy[:, 1],"o",markerfacecolor=tuple(col),markeredgecolor="k",markersize=8)
        xy = pca_data[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0],xy[:, 1],"o",markerfacecolor=tuple(col),markeredgecolor="k",markersize=4)
    plt.show()

data = pd.read_csv('CC GENERAL.csv').iloc[:,1:].dropna()
print(data)
scaled_data = preprocessing.StandardScaler().fit_transform(data)

clustering = cluster.DBSCAN().fit(scaled_data)
print(set(clustering.labels_))
print(len(set(clustering.labels_)) - 1)
print(list(clustering.labels_).count(-1) / len(list(clustering.labels_)))

eps=[n/1000 for n in range(1,1000,10)]
yp,yc=[],[]
for x in eps:
    clustering = cluster.DBSCAN(eps=x).fit(scaled_data)
    yc.append(len(set(clustering.labels_)) - 1)
    yp.append(list(clustering.labels_).count(-1) / len(list(clustering.labels_))*100)
plt.plot(eps,yc)
plt.xlabel("eps")
plt.ylabel("Количество кластеров")
plt.show()
plt.plot(eps,yp)
plt.xlabel("eps")
plt.ylabel("Процент не кластеризованных наблюдений")
plt.show()

ms=[n for n in range(2,50,1)]
yp,yc=[],[]
for x in ms:
    clustering = cluster.DBSCAN(min_samples=x).fit(scaled_data)
    yc.append(len(set(clustering.labels_)) - 1)
    yp.append(list(clustering.labels_).count(-1) / len(list(clustering.labels_))*100)
plt.plot(ms,yc)
plt.xlabel("min_samples")
plt.ylabel("Количество кластеров")
plt.show()
plt.plot(ms,yp)
plt.xlabel("min_samples")
plt.ylabel("Процент не кластеризованных наблюдений")
plt.show()


clustering = cluster.DBSCAN(eps=2,min_samples=3).fit(scaled_data)
print(len(set(clustering.labels_)) - 1)
print(list(clustering.labels_).count(-1) / len(list(clustering.labels_)))
plotClusts(scaled_data, clustering)

clustering = cluster.OPTICS(min_samples=3, max_eps=3, cluster_method="dbscan").fit(scaled_data)
print(len(set(clustering.labels_)) - 1)
print(list(clustering.labels_).count(-1) / len(list(clustering.labels_)))
plotClusts(scaled_data,clustering)


space = np.arange(len(scaled_data))
reachability = clustering.reachability_[clustering.ordering_]
labels = clustering.labels_[clustering.ordering_]

colors = ["g.", "r.", "b.", "y.", "c."]
for klass, color in enumerate(colors):
    Xk = space[labels == klass]
    Rk = reachability[labels == klass]
    plt.plot(Xk, Rk, color, alpha=0.3)
plt.plot(space[labels == -1], reachability[labels == -1], "k.", alpha=0.3)
plt.plot(space, np.full_like(space, 2.0, dtype=float), "k-", alpha=0.5)
plt.plot(space, np.full_like(space, 0.5, dtype=float), "k-.", alpha=0.5)
plt.ylabel("Достижимое расстояние")
plt.title("График достижимости")
plt.show()

clustering = cluster.OPTICS(min_samples=3, max_eps=3, cluster_method="dbscan",metric='euclidean').fit(scaled_data)
print(len(set(clustering.labels_)) - 1)
print(list(clustering.labels_).count(-1) / len(list(clustering.labels_)))
plotClusts(scaled_data,clustering)

clustering = cluster.OPTICS(min_samples=3, max_eps=3, cluster_method="dbscan",metric='manhattan').fit(scaled_data)
print(len(set(clustering.labels_)) - 1)
print(list(clustering.labels_).count(-1) / len(list(clustering.labels_)))
plotClusts(scaled_data,clustering)

clustering = cluster.OPTICS(min_samples=3, max_eps=3, cluster_method="dbscan",metric='cosine').fit(scaled_data)
print(len(set(clustering.labels_)) - 1)
print(list(clustering.labels_).count(-1) / len(list(clustering.labels_)))
plotClusts(scaled_data,clustering)

clustering = cluster.OPTICS(min_samples=3, max_eps=3, cluster_method="dbscan",metric='cityblock').fit(scaled_data)
print(len(set(clustering.labels_)) - 1)
print(list(clustering.labels_).count(-1) / len(list(clustering.labels_)))
plotClusts(scaled_data,clustering)

clustering = cluster.OPTICS(min_samples=3, max_eps=3, cluster_method="dbscan",metric='l1').fit(scaled_data)
print(len(set(clustering.labels_)) - 1)
print(list(clustering.labels_).count(-1) / len(list(clustering.labels_)))
plotClusts(scaled_data,clustering)
