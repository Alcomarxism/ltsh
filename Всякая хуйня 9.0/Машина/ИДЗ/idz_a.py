import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('RT_IOT2022.csv',index_col=0)
print(df)
print(df.describe())
print(df['Attack_type'].value_counts())

print(df.dtypes)
categ_cols=df.select_dtypes(include=['object']).columns.tolist()
num_cols = df.select_dtypes(include=['int64']).columns.tolist()
cont_cols=df.select_dtypes(include=['float64']).columns.tolist()

dfcat=df[categ_cols]
dfnum=df[num_cols]
dfcon=df[cont_cols]

for cat in categ_cols:
    print(cat,set(dfcat[cat].tolist()))

print(dfnum.iloc[:, :10].describe())
print(dfnum.iloc[:, 10:20].describe())
print(dfnum.iloc[:, 20:].describe())

print(dfcon.iloc[:, :10].describe())
print(dfcon.iloc[:, 10:20].describe())
print(dfcon.iloc[:, 20:30].describe())
print(dfcon.iloc[:, 30:40].describe())
print(dfcon.iloc[:, 40:50].describe())
print(dfcon.iloc[:, 50:].describe())

fig, axs = plt.subplots(len(num_cols)//3+1,3)
for i in range(len(num_cols)):
    axs[i//3, i%3].hist(dfnum.to_numpy()[:,i], bins = 10)
    axs[i//3, i%3].set_title(dfnum.columns[i],{'fontsize':10})
plt.show()

fig, axs = plt.subplots(9,3)
for i in range(27):
    axs[i//3, i%3].hist(dfcon.to_numpy()[:,i], bins = 10)
    axs[i//3, i%3].set_title(dfcon.columns[i],{'fontsize':10})
plt.show()

fig, axs = plt.subplots(9,3)
for i in range(27):
    axs[i//3, i%3].hist(dfcon.to_numpy()[:,i+27], bins = 10)
    axs[i//3, i%3].set_title(dfcon.columns[i+27],{'fontsize':10})
plt.show()

fig, axs = plt.subplots(2,2)
for i in range(len(cont_cols)-54):
    axs[i//3, i%3].hist(dfcon.to_numpy()[:,i+54], bins = 10)
    axs[i//3, i%3].set_title(dfcon.columns[i+54],{'fontsize':10})
plt.show()

dfn=df[num_cols+cont_cols]
corrmat=dfn.corr()
plt.matshow(corrmat, cmap='RdBu_r', vmin=-1, vmax=1)
plt.show()

