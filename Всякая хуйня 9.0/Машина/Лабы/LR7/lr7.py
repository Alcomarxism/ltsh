import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import tree
import matplotlib.pyplot as plt
data = pd.read_csv('iris.data',header=None)
print(data)
X = data.iloc[:,:4].to_numpy()
labels = data.iloc[:,4].to_numpy()
le = preprocessing.LabelEncoder()
Y = le.fit_transform(labels)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.5)

gnb = naive_bayes.GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("GaussianNB:",(y_test != y_pred).sum(),gnb.score(X_test,y_test))

test_size=[s/100 for s in range(5,95,5)]
nc=[]
sc=[]
for ts in test_size:
    gnb = naive_bayes.GaussianNB()
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=ts,random_state=5)
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    nc.append((y_test != y_pred).sum())
    sc.append(gnb.score(X_test,y_test))
plt.plot(test_size,nc)
plt.xlabel("Соотношение обучающей и тестовой выборок ")
plt.ylabel("Количество неправильно классифицированных наблюдений ")
plt.show()
plt.plot(test_size,sc)
plt.xlabel("Соотношение обучающей и тестовой выборок ")
plt.ylabel("Точность классификации")
plt.show()


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.5)
mnb = naive_bayes.MultinomialNB()
y_pred = mnb.fit(X_train, y_train).predict(X_test)
print("MultinominalNB:",(y_test != y_pred).sum(),mnb.score(X_test,y_test))

bnb = naive_bayes.BernoulliNB()
y_pred = bnb.fit(X_train, y_train).predict(X_test)
print("BernoulliNB:",(y_test != y_pred).sum(),bnb.score(X_test,y_test))

gnb = naive_bayes.ComplementNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("ComplementNB:",(y_test != y_pred).sum(),gnb.score(X_test,y_test))


clf = tree.DecisionTreeClassifier()
y_pred = clf.fit(X_train, y_train).predict(X_test)
print('wrong:',(y_test != y_pred).sum())
print('score:',clf.score(X_test,y_test))
print('n leaves:',clf.get_n_leaves())
print('depth:',clf.get_depth())
plt.subplots(1,1,figsize = (10,10))
tree.plot_tree(clf, filled = True)
plt.show()

test_size=[s/100 for s in range(5,95,5)]
nc=[]
sc=[]
for ts in test_size:
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=ts,random_state=5)
    clf = tree.DecisionTreeClassifier()
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

clf = tree.DecisionTreeClassifier(criterion='entropy')
y_pred = clf.fit(X_train, y_train).predict(X_test)
plt.subplots(1,1,figsize = (10,10))
tree.plot_tree(clf, filled = True)
plt.show()

clf = tree.DecisionTreeClassifier(splitter='random')
y_pred = clf.fit(X_train, y_train).predict(X_test)
plt.subplots(1,1,figsize = (10,10))
tree.plot_tree(clf, filled = True)
plt.show()

clf = tree.DecisionTreeClassifier(max_depth=2)
y_pred = clf.fit(X_train, y_train).predict(X_test)
plt.subplots(1,1,figsize = (10,10))
tree.plot_tree(clf, filled = True)
plt.show()

clf = tree.DecisionTreeClassifier(min_samples_split=30)
y_pred = clf.fit(X_train, y_train).predict(X_test)
plt.subplots(1,1,figsize = (10,10))
tree.plot_tree(clf, filled = True)
plt.show()

clf = tree.DecisionTreeClassifier(min_samples_leaf=30)
y_pred = clf.fit(X_train, y_train).predict(X_test)
plt.subplots(1,1,figsize = (10,10))
tree.plot_tree(clf, filled = True)
plt.show()