import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import decomposition

df = pd.read_csv('glass.csv')
var_names = list(df.columns)
labels = df.to_numpy('int')[:,-1] 
data = df.to_numpy('float')[:,:-1]
data = preprocessing.minmax_scale(data)
fig, axs = plt.subplots(2,4)
for i in range(data.shape[1]-1):
        axs[i // 4, i % 4].scatter(data[:,i],data[:,(i+1)],c=labels,cmap='hsv')
        axs[i // 4, i % 4].set_xlabel(var_names[i])
        axs[i // 4, i % 4].set_ylabel(var_names[i+1])
plt.show()

pca = decomposition.PCA(n_components = 2)
pca_data = pca.fit_transform(data)
print(sum(pca.explained_variance_ratio_))
print(pca.singular_values_)
plt.scatter(pca_data[:,0],pca_data[:,1],c=labels,cmap='hsv')
plt.title("PCA")
plt.show()

comp=2
while sum(pca.explained_variance_ratio_)<0.85:
        comp+=1
        pca = decomposition.PCA(n_components = comp)
        pca_data = pca.fit_transform(data)
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
print(pca.singular_values_)
fig, axs = plt.subplots(1,comp-1)
for i in range(comp-1):
        axs[i].scatter(pca_data[:,i],pca_data[:,(i+1)],c=labels,cmap='hsv')
plt.show()

inversed_data=pca.inverse_transform(pca_data)
fig, axs = plt.subplots(2,4)
for i in range(inversed_data.shape[1]-1):
        axs[i // 4, i % 4].scatter(inversed_data[:,i],inversed_data[:,(i+1)],c=labels,cmap='hsv')
        axs[i // 4, i % 4].set_xlabel(var_names[i])
        axs[i // 4, i % 4].set_ylabel(var_names[i+1])
plt.show()

pca = decomposition.PCA(n_components = 4,svd_solver='full')
pca_data = pca.fit_transform(data)
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
print(pca.singular_values_)
plt.scatter(pca_data[:,0],pca_data[:,1],c=labels,cmap='hsv')
plt.title("full SVD")
plt.show()

pca = decomposition.PCA(n_components = 4,svd_solver='covariance_eigh')
pca_data = pca.fit_transform(data)
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
print(pca.singular_values_)
plt.scatter(pca_data[:,0],pca_data[:,1],c=labels,cmap='hsv')
plt.title("covariance_eigh SVD")

plt.show()

pca = decomposition.PCA(n_components = 4,svd_solver='arpack')
pca_data = pca.fit_transform(data)
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
print(pca.singular_values_)
plt.scatter(pca_data[:,0],pca_data[:,1],c=labels,cmap='hsv')
plt.title("arpack SVD")
plt.show()

pca = decomposition.PCA(n_components = 4,svd_solver='randomized')
pca_data = pca.fit_transform(data)
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
print(pca.singular_values_)
plt.scatter(pca_data[:,0],pca_data[:,1],c=labels,cmap='hsv')
plt.title("randomized SVD")
plt.show()

kpca = decomposition.KernelPCA(n_components = 2,kernel='linear')
kpca_data = kpca.fit_transform(data)
plt.scatter(kpca_data[:,0],kpca_data[:,1],c=labels,cmap='hsv')
plt.title("Linear kernel PCA")
plt.show()

kpca = decomposition.KernelPCA(n_components = 2,kernel='poly',gamma=2, coef0=1, degree=4)
kpca_data = kpca.fit_transform(data)
plt.scatter(kpca_data[:,0],kpca_data[:,1],c=labels,cmap='hsv')
plt.title("Poly kernel PCA")
plt.show()

kpca = decomposition.KernelPCA(n_components = 2,kernel='poly',gamma=1, coef0=0, degree=5)
kpca_data = kpca.fit_transform(data)
plt.scatter(kpca_data[:,0],kpca_data[:,1],c=labels,cmap='hsv')
plt.title("Poly kernel PCA")
plt.show()

kpca = decomposition.KernelPCA(n_components = 2,kernel='rbf',gamma=1)
kpca_data = kpca.fit_transform(data)
plt.scatter(kpca_data[:,0],kpca_data[:,1],c=labels,cmap='hsv')
plt.title("RBF kernel PCA")
plt.show()

kpca = decomposition.KernelPCA(n_components = 2,kernel='rbf',gamma=2)
kpca_data = kpca.fit_transform(data)
plt.scatter(kpca_data[:,0],kpca_data[:,1],c=labels,cmap='hsv')
plt.title("RBF kernel PCA")
plt.show()

kpca = decomposition.KernelPCA(n_components = 2,kernel='sigmoid',gamma=1, coef0=0)
kpca_data = kpca.fit_transform(data)
plt.scatter(kpca_data[:,0],kpca_data[:,1],c=labels,cmap='hsv')
plt.title("Sigmoid kernel PCA")
plt.show()

kpca = decomposition.KernelPCA(n_components = 2,kernel='sigmoid',gamma=2, coef0=3)
kpca_data = kpca.fit_transform(data)
plt.scatter(kpca_data[:,0],kpca_data[:,1],c=labels,cmap='hsv')
plt.title("Sigmoid kernel PCA")
plt.show()

kpca = decomposition.KernelPCA(n_components = 2,kernel='cosine')
kpca_data = kpca.fit_transform(data)
plt.scatter(kpca_data[:,0],kpca_data[:,1],c=labels,cmap='hsv')
plt.title("Cosine kernel PCA")
plt.show()

spca=decomposition.SparsePCA(n_components=2,alpha=1,method='lars')
spca_data=spca.fit_transform(data)
plt.scatter(spca_data[:,0],spca_data[:,1],c=labels,cmap='hsv')
plt.title("Sparse PCA data")
plt.show()

spca=decomposition.SparsePCA(n_components=2,alpha=0.1,method='cd')
spca_data=spca.fit_transform(data)
plt.scatter(spca_data[:,0],spca_data[:,1],c=labels,cmap='hsv')
plt.title("Sparse PCA data")
plt.show()

fa=decomposition.FactorAnalysis(n_components=2)
fa_data=fa.fit_transform(data)
plt.scatter(fa_data[:,0],fa_data[:,1],c=labels,cmap='hsv')
plt.title("Factor analysis")
plt.show()