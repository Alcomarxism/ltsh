import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mlxtend.preprocessing
import mlxtend.frequent_patterns

all_data = pd.read_csv('dataset_group.csv',header=None)
print(all_data)
unique_id = list(set(all_data[1]))
print(len(unique_id))

items = list(set(all_data[2]))
print(len(items))

dataset = [[elem for elem in all_data[all_data[1] == id][2] if elem in items] for id in unique_id]
te = mlxtend.preprocessing.TransactionEncoder()
te_ary = te.fit_transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)

results = mlxtend.frequent_patterns.apriori(df, min_support=0.3, use_colnames=True)
results['length'] = results['itemsets'].apply(lambda x: len(x)) 
print(results)

results = mlxtend.frequent_patterns.apriori(df, min_support=0.3, use_colnames=True, max_len=1)
print(results)

results = mlxtend.frequent_patterns.apriori(df, min_support=0.3, use_colnames=True)
results['length'] = results['itemsets'].apply(lambda x: len(x))
results = results[results['length'] == 2]
print(results)
print('\nCount of result itemstes = ',len(results))

x=[xx/100 for xx in range(5,100)]
y=[]
lenx=[]
leny=[]
lastmaxlen=0
x.reverse()
for xx in x:
    results = mlxtend.frequent_patterns.apriori(df, min_support=xx, use_colnames=True)
    if len(results)!=0:
        ml=len(results['itemsets'].to_list()[-1])
        if ml!=lastmaxlen:
            lenx.append(xx)
            leny.append(len(results))
            lastmaxlen=ml
    y.append(len(results))
plt.plot(x[70:],y[70:])
plt.scatter(lenx[2:],leny[2:],c='red')
plt.show()
plt.plot(x[:70],y[:70])
plt.scatter(lenx[:2],leny[:2],c='red')
plt.show()
for n in range(len(lenx)):
    print(lenx[n])

results = mlxtend.frequent_patterns.apriori(df, min_support=0.38, use_colnames=True, max_len=1)
new_items = [ list(elem)[0] for elem in results['itemsets']]
new_dataset = [[elem for elem in all_data[all_data[1] == id][2] if elem in new_items] for id in unique_id]
te_ary = te.fit_transform(new_dataset)
df2 = pd.DataFrame(te_ary, columns=te.columns_)

results = mlxtend.frequent_patterns.apriori(df2, min_support=0.3, use_colnames=True)
print(results)

results = mlxtend.frequent_patterns.apriori(df2, min_support=0.15, use_colnames=True)
results=results[results['itemsets'].apply(lambda x: (('yogurt' in x) or ('waffles' in x))and (len(x)>1))]
print(results)

results = mlxtend.frequent_patterns.apriori(df, min_support=0.38, use_colnames=True, max_len=1)
new_items = [ list(elem)[0] for elem in results['itemsets']]
new_dataset = [[elem for elem in all_data[all_data[1] == id][2] if not(elem in new_items)] for id in unique_id]
te_ary = te.fit_transform(new_dataset)
df2 = pd.DataFrame(te_ary, columns=te.columns_)

results = mlxtend.frequent_patterns.apriori(df2, min_support=0.3, use_colnames=True)
print(results)

results = mlxtend.frequent_patterns.apriori(df, min_support=0.15, use_colnames=True)
results=results[results['itemsets'].apply(lambda x: [str[0]for str in x].count('s')>=2)]
print(results)

results = mlxtend.frequent_patterns.apriori(df, min_support=0.1, use_colnames=True)
results=results[results['support'].apply(lambda x: x<=0.25)]
print(results)
