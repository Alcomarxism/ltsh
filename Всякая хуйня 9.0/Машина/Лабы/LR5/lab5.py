import pandas as pd
import numpy as np
from sklearn import cluster 
from sklearn import metrics 
from sklearn import preprocessing
from sklearn import decomposition
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
import random
import math

def plotClusters(no_labeled_data,names,k_means_labels,k_means_cluster_centers):
    f, ax = plt.subplots(1, 3)
    colors = ["#784EC5", "#F13434", "#7FFF07"]
    for i in range(len(k_means_cluster_centers)):
        my_members = k_means_labels == i
        cluster_center = k_means_cluster_centers[i]
        for j in range(3):
            ax[j].plot(no_labeled_data[my_members][j],no_labeled_data[my_members][j+1], 'w',markerfacecolor=colors[i], marker='o', markersize=4)
            ax[j].plot(cluster_center[j], cluster_center[j+1], 'o',markerfacecolor=colors[i],markeredgecolor='k', markersize=8)
            ax[j].set_xlabel(names[j])
            ax[j].set_ylabel(names[j+1])
    plt.show()

def plotHierClusters(no_labled_data,labels):
    f, ax = plt.subplots(1, 3)
    colors = ["#0000FF", "#FF0000", "#00FF00","#FF00FF","#FFFF00"]
    for i in range(5):
        my_members = labels == i
        for j in range(3):
            ax[j].plot(no_labeled_data[my_members][j],no_labeled_data[my_members][j+1], 'w',markerfacecolor=colors[i], marker='o', markersize=4)
            ax[j].set_xlabel(names[j])
            ax[j].set_ylabel(names[j+1])
    plt.show()

def plotPCAClusters(pca_data,k_means_cluster_centers):
    h = 0.02  
    x_min, x_max = pca_data[:, 0].min() - 1, pca_data[:, 0].max() + 1
    y_min, y_max = pca_data[:, 1].min() - 1, pca_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = k_means.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(
        Z,
        interpolation="nearest",
        extent=(xx.min(), xx.max(), yy.min(), yy.max()),
        cmap=plt.cm.Paired,
        aspect="auto",
        origin="lower",
    )
    plt.plot(pca_data[:, 0], pca_data[:, 1], "k.", markersize=2)
    centroids = k_means_cluster_centers
    plt.scatter(
        centroids[:, 0],
        centroids[:, 1],
        marker="x",
        s=169,
        linewidths=3,
        color="w",
        zorder=10,
    )
    plt.show()

def plot_dendrogram(model, **kwargs):
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)
    dendrogram(linkage_matrix, **kwargs)


data = pd.read_csv('iris.data',header=None)
names=['sepal length in cm', 'sepal width in cm', 'petal length in cm','petal width in cm']
no_labeled_data=data.drop(4,axis=1)
print(no_labeled_data)

k_means = cluster.KMeans(init='k-means++', n_clusters=3, n_init=15)
k_means.fit(no_labeled_data)
k_means_cluster_centers = k_means.cluster_centers_
print(k_means_cluster_centers)
k_means_labels = metrics.pairwise.pairwise_distances_argmin(no_labeled_data,k_means_cluster_centers)
print(k_means_labels)
plotClusters(no_labeled_data,names,k_means_labels,k_means_cluster_centers)

pca = decomposition.PCA(n_components = 2)
pca_data = pca.fit_transform(no_labeled_data)
k_means = cluster.KMeans(init='k-means++', n_clusters=3, n_init=15)
k_means.fit(pca_data)
k_means_labels = metrics.pairwise.pairwise_distances_argmin(pca_data,k_means.cluster_centers_)
plotPCAClusters(pca_data,k_means.cluster_centers_)

k_means = cluster.KMeans(init='random', n_clusters=3)
k_means.fit(no_labeled_data)
k_means_cluster_centers = k_means.cluster_centers_
k_means_labels = metrics.pairwise.pairwise_distances_argmin(no_labeled_data,k_means_cluster_centers)
plotClusters(no_labeled_data,names,k_means_labels,k_means_cluster_centers)

init_centr = np.array([
    [5,3.5,1.5,0.25],   
    [6,2.5,4.5,1.5],   
    [7,3,6,2]    
])
k_means = cluster.KMeans(init=init_centr, n_clusters=3)
k_means.fit(no_labeled_data)
k_means_cluster_centers = k_means.cluster_centers_
k_means_labels = metrics.pairwise.pairwise_distances_argmin(no_labeled_data,k_means_cluster_centers)
plotClusters(no_labeled_data,names,k_means_labels,k_means_cluster_centers)

X= no_labeled_data.iloc[:,2:].values
wcss=[]
for i in range(1,15):
    kmean = cluster.KMeans(n_clusters=i,init="k-means++")
    kmean.fit_predict(X)
    wcss.append(kmean.inertia_)
plt.plot(range(1,15),wcss)
plt.xlabel("Количество кластеров")
plt.ylabel("Дисперсия")
plt.show()

mb_k_means=cluster.MiniBatchKMeans(n_clusters=3)
mb_k_means.fit(no_labeled_data)
mb_k_means_cluster_centers = mb_k_means.cluster_centers_
mb_k_means_cluster_centers=sorted(mb_k_means_cluster_centers.tolist(),key=lambda x:x[0])
mb_k_means_labels = metrics.pairwise.pairwise_distances_argmin(no_labeled_data,mb_k_means_cluster_centers)
plotClusters(no_labeled_data,names,mb_k_means_labels,mb_k_means_cluster_centers)

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(no_labeled_data)
k_means_cluster_centers = k_means.cluster_centers_
k_means_cluster_centers=sorted(k_means_cluster_centers.tolist(),key=lambda x:x[0])
k_means_labels = metrics.pairwise.pairwise_distances_argmin(no_labeled_data,k_means_cluster_centers)
f, ax = plt.subplots(1, 3)
for j in range(3):
    my_members = [k_means_labels[i]==mb_k_means_labels[i] for i in range(len(k_means_labels))]
    ax[j].plot(no_labeled_data[my_members][j],no_labeled_data[my_members][j+1], 'w',markerfacecolor="#5900FFFF", marker='o', markersize=4)
    my_members = [not (k_means_labels[i]==mb_k_means_labels[i]) for i in range(len(k_means_labels))]
    ax[j].plot(no_labeled_data[my_members][j],no_labeled_data[my_members][j+1], 'w',markerfacecolor="#FF0000FF", marker='o', markersize=4)
    ax[j].set_xlabel(names[j])
    ax[j].set_ylabel(names[j+1])
plt.show()

hier = cluster.AgglomerativeClustering(n_clusters=3, linkage='average')
hier = hier.fit(no_labeled_data)
hier_labels = hier.labels_
plotHierClusters(no_labeled_data,hier_labels)

hier = cluster.AgglomerativeClustering(n_clusters=2, linkage='average')
hier = hier.fit(no_labeled_data)
hier_labels = hier.labels_
plotHierClusters(no_labeled_data,hier_labels)

hier = cluster.AgglomerativeClustering(n_clusters=5, linkage='average')
hier = hier.fit(no_labeled_data)
hier_labels = hier.labels_
plotHierClusters(no_labeled_data,hier_labels)

hier = cluster.AgglomerativeClustering(linkage='average',compute_distances=True)
hier = hier.fit(no_labeled_data)
plot_dendrogram(hier, truncate_mode="level", p=6)
plt.show()

data1 = np.zeros([250,2])
for i in range(250):
    r = random.uniform(1, 3)
    a = random.uniform(0, 2 * math.pi)
    data1[i,0] = r * math.sin(a)
    data1[i,1] = r * math.cos(a)
data2 = np.zeros([500,2])
for i in range(500):
    r = random.uniform(5, 9)
    a = random.uniform(0, 2 * math.pi)
    data2[i,0] = r * math.sin(a)
    data2[i,1] = r * math.cos(a)
data = np.vstack((data1, data2))

hier = cluster.AgglomerativeClustering(n_clusters=2, linkage='ward')
hier = hier.fit(data)
hier_labels = hier.labels_
my_members = hier_labels == 0
plt.plot(data[my_members, 0], data[my_members, 1], 'w', marker='o',markersize=4,color='red',linestyle='None')
my_members = hier_labels == 1
plt.plot(data[my_members, 0], data[my_members, 1], 'w', marker='o',markersize=4,color='blue',linestyle='None')
plt.show()

hier = cluster.AgglomerativeClustering(n_clusters=2, linkage='average')
hier = hier.fit(data)
hier_labels = hier.labels_
my_members = hier_labels == 0
plt.plot(data[my_members, 0], data[my_members, 1], 'w', marker='o',markersize=4,color='red',linestyle='None')
my_members = hier_labels == 1
plt.plot(data[my_members, 0], data[my_members, 1], 'w', marker='o',markersize=4,color='blue',linestyle='None')
plt.show()


hier = cluster.AgglomerativeClustering(n_clusters=2, linkage='complete')
hier = hier.fit(data)
hier_labels = hier.labels_
my_members = hier_labels == 0
plt.plot(data[my_members, 0], data[my_members, 1], 'w', marker='o',markersize=4,color='red',linestyle='None')
my_members = hier_labels == 1
plt.plot(data[my_members, 0], data[my_members, 1], 'w', marker='o',markersize=4,color='blue',linestyle='None')
plt.show()


hier = cluster.AgglomerativeClustering(n_clusters=2, linkage='single')
hier = hier.fit(data)
hier_labels = hier.labels_
my_members = hier_labels == 0
plt.plot(data[my_members, 0], data[my_members, 1], 'w', marker='o',markersize=4,color='red',linestyle='None')
my_members = hier_labels == 1
plt.plot(data[my_members, 0], data[my_members, 1], 'w', marker='o',markersize=4,color='blue',linestyle='None')
plt.show()



