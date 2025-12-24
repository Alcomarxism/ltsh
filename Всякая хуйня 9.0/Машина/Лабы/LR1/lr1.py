import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def plotData(data,n_bins=20):
    fig, axs = plt.subplots(2,3)
    axs[0, 0].hist(data[:,0], bins = n_bins)
    axs[0, 0].set_title('age')
    axs[0, 1].hist(data[:,1], bins = n_bins)
    axs[0, 1].set_title('creatinine_phosphokinase')
    axs[0, 2].hist(data[:,2], bins = n_bins)
    axs[0, 2].set_title('ejection_fraction')
    axs[1, 0].hist(data[:,3], bins = n_bins)
    axs[1, 0].set_title('platelets')
    axs[1, 1].hist(data[:,4], bins = n_bins)
    axs[1, 1].set_title('serum_creatinine')
    axs[1, 2].hist(data[:,5], bins = n_bins)
    axs[1, 2].set_title('serum_sodium')
    plt.show()

def printDataParams(data):
    dtr=data.transpose()
    print("Min:",end=' ')
    for d in dtr:
        print("%0.2f" % np.min(d), end='\t')
    print()
    print("Max:",end=' ')
    for d in dtr:
        print("%0.2f" % np.max(d), end='\t')
    print()
    print("Mean:",end=' ')
    for d in dtr:
        print("%0.2f" % np.mean(d), end='\t')
    print()
    print("STD: ",end=' ')
    for d in dtr:
        print("%0.2f" % np.std(d), end='\t')
    print("\n")

def dataToMinus5toPlus10(data):
    min_max_scaler = preprocessing.MinMaxScaler()
    data_min_max_scaled = min_max_scaler.fit_transform(data)
    data_min_max_scaled*=15
    data_min_max_scaled-=5
    return data_min_max_scaled

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
df = df.drop(columns =['anaemia','diabetes','high_blood_pressure','sex','smoking','time','DEATH_EVENT'])
print(df)
data = df.to_numpy(dtype='float')
print("Before standartization:")
plotData(data)
printDataParams(data)

scaler = preprocessing.StandardScaler().fit(data[:150,:])
data_scaled = scaler.transform(data)
print("After standartization based on the first 150 observations:")
plotData(data_scaled)
printDataParams(data_scaled)

print("Params of scaler:")
print("mean_:",scaler.mean_)
print("scale_:",scaler.scale_)
print()

scaler = preprocessing.StandardScaler().fit(data[:,:])
data_scaled = scaler.transform(data)
print("After standartization based on all data:")
plotData(data_scaled)
printDataParams(data_scaled)

min_max_scaler = preprocessing.MinMaxScaler()
data_min_max_scaled = min_max_scaler.fit_transform(data)
plotData(data_min_max_scaled)
print("min_max_scaler data_min_:",min_max_scaler.data_min_)
print("min_max_scaler data_max_:",min_max_scaler.data_max_)
print()

max_abs_scaler = preprocessing.MaxAbsScaler()
data_max_abs_scaled = max_abs_scaler.fit_transform(data)
plotData(data_max_abs_scaled)

robust_scaler = preprocessing.RobustScaler()
data_robust_scaled = robust_scaler.fit_transform(data)
plotData(data_robust_scaled)

data_Minus5toPlus10=dataToMinus5toPlus10(data)
plotData(data_Minus5toPlus10)

quantile_transformer = preprocessing.QuantileTransformer(n_quantiles = 100,random_state=0).fit(data)
data_quantile_scaled = quantile_transformer.transform(data)
plotData(data_quantile_scaled)

quantile_transformer = preprocessing.QuantileTransformer(n_quantiles = 100,random_state=0,output_distribution='normal').fit(data)
data_quantile_scaled = quantile_transformer.transform(data)
plotData(data_quantile_scaled)

power_transformer = preprocessing.PowerTransformer()
data_power_transformed = power_transformer.fit_transform(data)
plotData(data_power_transformed)

k_bins_discreaser=preprocessing.KBinsDiscretizer(n_bins=[3, 4, 3, 10 ,2 ,4],encode='ordinal')
data_k_bins_discreased=k_bins_discreaser.fit_transform(data)
print(data_k_bins_discreased)
plotData(data_k_bins_discreased)
for atr in k_bins_discreaser.bin_edges_:
    lft=None
    for rgh in atr:
        if lft:
            print('[%.2f;%.2f]'%(lft,rgh),end=' ')
        lft=rgh
    print()