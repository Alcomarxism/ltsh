import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import discriminant_analysis
from sklearn import svm
import matplotlib.pyplot as plt


data = pd.read_csv('iris.data',header=None)
print(data)
X = data.iloc[:,:4].to_numpy()
labels = data.iloc[:,4].to_numpy()
le = preprocessing.LabelEncoder()
Y = le.fit_transform(labels)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.5,random_state=5)
lda = discriminant_analysis.LinearDiscriminantAnalysis()
y_pred = lda.fit(X_train, y_train).predict(X_test)
print("LDA:",(y_test != y_pred).sum(),lda.score(X_test,y_test))

test_size=[s/100 for s in range(5,95,5)]
nc=[]
sc=[]
for ts in test_size:
    lda=discriminant_analysis.LinearDiscriminantAnalysis()
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=ts,random_state=5)
    y_pred = lda.fit(X_train, y_train).predict(X_test)
    nc.append((y_test != y_pred).sum())
    sc.append(lda.score(X_test,y_test))
plt.plot(test_size,nc)
plt.xlabel("Соотношение обучающей и тестовой выборок ")
plt.ylabel("Количество неправильно классифицированных наблюдений ")
plt.show()
plt.plot(test_size,sc)
plt.xlabel("Соотношение обучающей и тестовой выборок ")
plt.ylabel("Точность классификации")
plt.show()

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.5,random_state=5)
lda = discriminant_analysis.LinearDiscriminantAnalysis()
y_pred = lda.fit(X_train, y_train).predict(X_test)
X_n_test=lda.transform(X_test)
lda.i
colors = ['red', 'green', 'blue']
for i, color in zip([0, 1,2], colors):
    plt.scatter(
        X_n_test[y_test == i, 0], 
        X_n_test[y_test == i, 1],
        c=color
    )
plt.show()

lda = discriminant_analysis.LinearDiscriminantAnalysis(solver='eigen')
y_pred = lda.fit(X_train, y_train).predict(X_test)
print("LDA + solver=eigen:",(y_test != y_pred).sum(),lda.score(X_test,y_test))

lda = discriminant_analysis.LinearDiscriminantAnalysis(solver='lsqr')
y_pred = lda.fit(X_train, y_train).predict(X_test)
print("LDA + solver=lsqr:",(y_test != y_pred).sum(),lda.score(X_test,y_test))

lda = discriminant_analysis.LinearDiscriminantAnalysis(shrinkage=0.5,solver='eigen')
y_pred = lda.fit(X_train, y_train).predict(X_test)
print("LDA + shrinkage=0.5:",(y_test != y_pred).sum(),lda.score(X_test,y_test))

lda = discriminant_analysis.LinearDiscriminantAnalysis(shrinkage=1,solver='eigen')
y_pred = lda.fit(X_train, y_train).predict(X_test)
print("LDA + shrinkage=1:",(y_test != y_pred).sum(),lda.score(X_test,y_test))

lda = discriminant_analysis.LinearDiscriminantAnalysis(priors=[0.7,0.15,0.15])
y_pred = lda.fit(X_train, y_train).predict(X_test)
print("LDA + prior:",(y_test != y_pred).sum(),lda.score(X_test,y_test))

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.5,random_state=5)
clf = svm.SVC()
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("SVC:",(y_test != y_pred).sum(),clf.score(X_test,y_test))

print(clf.support_vectors_)
print(clf.support_)
print(clf.n_support_)

test_size=[s/100 for s in range(5,95,5)]
nc=[]
sc=[]
for ts in test_size:
    clf=svm.SVC()
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=ts,random_state=5)
    y_pred = clf.fit(X_train, y_train).predict(X_test)
    nc.append((y_test != y_pred).sum())
    sc.append(clf.score(X_test,y_test))
plt.plot(test_size,nc)
plt.xlabel("Соотношение обучающей и тестовой выборок ")
plt.ylabel("Количество неправильно классифицированных наблюдений ")
plt.show()
plt.plot(test_size,sc)
plt.xlabel("Соотношение обучающей и тестовой выборок ")
plt.ylabel("Точность классификации")
plt.show()

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.5,random_state=5)
clf = svm.SVC(kernel='sigmoid')
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("SVC+kernel=sigmoid:",(y_test != y_pred).sum(),clf.score(X_test,y_test))

clf = svm.SVC(kernel='linear')
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("SVC+kernel=linear:",(y_test != y_pred).sum(),clf.score(X_test,y_test))

clf = svm.SVC(kernel='poly',degree=1)
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("SVC+kernel=poly degree=1:",(y_test != y_pred).sum(),clf.score(X_test,y_test))

clf = svm.SVC(kernel='poly',degree=5)
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("SVC+kernel=poly degree=5:",(y_test != y_pred).sum(),clf.score(X_test,y_test))

clf = svm.SVC(max_iter=1)
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("SVC+max_iter=1:",(y_test != y_pred).sum(),clf.score(X_test,y_test))

clf = svm.SVC(max_iter=10)
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("SVC+max_iter=10:",(y_test != y_pred).sum(),clf.score(X_test,y_test))

clf = svm.NuSVC()
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("NuSVC:",(y_test != y_pred).sum(),clf.score(X_test,y_test))

clf = svm.LinearSVC()
y_pred = clf.fit(X_train, y_train).predict(X_test)
print("LinearSVC:",(y_test != y_pred).sum(),clf.score(X_test,y_test))