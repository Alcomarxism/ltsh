import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import metrics
from sklearn import tree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import metrics
from sklearn import preprocessing

df = pd.read_csv("RT_IOT2022.csv",index_col=0) 

data = df.drop(columns=['Attack_type','bwd_URG_flag_count']) 
labels=df['Attack_type']

categ_cols=data.select_dtypes(include=['object']).columns.tolist()
for cat in categ_cols:
    le = preprocessing.LabelEncoder()
    data[cat]= le.fit_transform(data[cat])

le = preprocessing.LabelEncoder()
labels= le.fit_transform(labels)

data_split=[None,None,None]
labels_split=[None,None,None]
data_split[0], data_split[1], labels_split[0], labels_split[1] = model_selection.train_test_split(data, labels, test_size=1/3)
data_split[0], data_split[2], labels_split[0], labels_split[2] = model_selection.train_test_split(data_split[0], labels_split[0], test_size=0.5)

for i in range(3):
    data_test=data_split[i]
    labels_test=labels_split[i]
    data_train = pd.concat(data_split[:i]+data_split[i+1:], axis=0)
    labels_train = np.concatenate(labels_split[:i]+labels_split[i+1:], axis=0)

    clf = tree.DecisionTreeClassifier(max_depth=10,criterion='entropy')
    labels_pred = clf.fit(data_train,labels_train).predict(data_test)

    print(metrics.classification_report(labels_test, labels_pred,target_names=le.classes_))

    cm = metrics.confusion_matrix(labels_test,labels_pred)
    cmdplot = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
    cmdplot.plot(cmap='Blues', text_kw={'color': 'Green'},xticks_rotation=90)
    cmdplot.im_.set_clim(vmin=0, vmax=5)
    plt.title('Матрица несоответствий')
    plt.show()