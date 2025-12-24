import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
import mlxtend.frequent_patterns as fp
import networkx as nx

all_data = pd.read_csv('groceries - groceries.csv')
#print(all_data)
np_data = all_data.to_numpy()
np_data = [[elem for elem in row[1:] if isinstance(elem,str)] for row in np_data]

unique_items = set()
for row in np_data:
    for elem in row:
        unique_items.add(elem)
#print(unique_items)
print(len(unique_items))

te = TransactionEncoder()
te_ary = te.fit(np_data).transform(np_data)
data = pd.DataFrame(te_ary, columns=te.columns_)
#print(data)
"""
result = fp.fpgrowth(data, min_support=0.03, use_colnames = True)
result['length'] = result['itemsets'].apply(lambda x: len(x)) 
print(result)
r1 = result[result['length'] == 1]
print(min(r1['support']))
print(max(r1['support']))
r2 = result[result['length'] == 2]
print(min(r2['support']))
print(max(r2['support']))

result = fp.fpmax(data, min_support=0.03, use_colnames = True)
result['length'] = result['itemsets'].apply(lambda x: len(x)) 
print(result)
r1 = result[result['length'] == 1]
print(min(r1['support']))
print(max(r1['support']))
r2 = result[result['length'] == 2]
print(min(r2['support']))
print(max(r2['support']))

result=fp.fpgrowth(data, min_support=0.03, use_colnames = True)
result['length'] = result['itemsets'].apply(lambda x: len(x)) 
result = result[result['length'] == 1]
result=result.sort_values(by='support',ascending=False)[:10]
x=[list(i)[0] for i in result['itemsets']]
y=[s for s in result['support']]
plt.bar(x,y)
plt.xlabel('Товар')
plt.ylabel('Частота')
plt.show()




np_data = all_data.to_numpy()
np_data = [[elem for elem in row[1:] if isinstance(elem,str) and elem in items] for row in np_data]
te = TransactionEncoder()
te_ary = te.fit_transform(np_data)
data2 = pd.DataFrame(te_ary, columns=te.columns_)
print(data2)

result = fp.fpgrowth(data2, min_support=0.03, use_colnames = True)
result['length'] = result['itemsets'].apply(lambda x: len(x)) 
print(result)
r1 = result[result['length'] == 1]
print(min(r1['support']))
print(max(r1['support']))
r2 = result[result['length'] == 2]
print(min(r2['support']))
print(max(r2['support']))

result = fp.fpmax(data2, min_support=0.03, use_colnames = True)
result['length'] = result['itemsets'].apply(lambda x: len(x)) 
print(result)
r1 = result[result['length'] == 1]
print(min(r1['support']))
print(max(r1['support']))
r2 = result[result['length'] == 2]
print(min(r2['support']))
print(max(r2['support']))

maxn=4
X=[sup/1000 for sup in range(50,260)]
Y=[]
for i in range(maxn):
    Y.append([])
for x in X:
    result= fp.fpgrowth(data,x, use_colnames = True)
    result['length'] = result['itemsets'].apply(lambda x: len(x)) 
    for i in range(maxn):
        Y[i].append(len(result[result['length'] == i+1]))
for i in range(maxn):
    plt.plot(X[:50],Y[i][:50])
plt.legend(range(1,maxn+1))
plt.xlabel("Минимальный уровень потдержки")
plt.ylabel("Количество наборов")
plt.show()

for i in range(maxn):
    plt.plot(X[50:],Y[i][50:])
plt.legend(range(1,maxn+1))
plt.xlabel("Минимальный уровень потдержки")
plt.ylabel("Количество наборов")

plt.show()

"""

items = ['whole milk', 'yogurt', 'soda', 'tropical fruit', 'shopping bags','sausage',
'whipped/sour cream', 'rolls/buns', 'other vegetables', 'root','vegetables',
'pork', 'bottled water', 'pastry', 'citrus fruit', 'canned beer', 'bottled beer']
np_data = all_data.to_numpy()
np_data = [[elem for elem in row[1:] if isinstance(elem,str) and elem in items] for row in np_data]
np_data = [row for row in np_data if len(row) > 1]
te = TransactionEncoder()
te_ary = te.fit(np_data).transform(np_data)
data = pd.DataFrame(te_ary, columns=te.columns_)
result = fp.fpgrowth(data, min_support=0.05, use_colnames = True)
#print(result)
rules = fp.association_rules(result, min_threshold = 0.3)
r1=rules.copy()
r2=rules.copy()
r1=r1.drop(['representativity',  'leverage',  'conviction',  'zhangs_metric',   'jaccard',  'certainty',  'kulczynski'],axis=1)
r2=r2.drop(['antecedent support', 'consequent support', 'support', 'confidence', 'lift' ],axis=1)
print(r1)
print(r2)

rules = fp.association_rules(result, min_threshold = 0.08, metric='support')
r1=rules.copy()
r1=r1.drop(['representativity',  'leverage',  'conviction',  'zhangs_metric',   'jaccard',  'certainty',  'kulczynski'],axis=1)
print(r1)

rules = fp.association_rules(result, min_threshold = 1.1, metric='lift')
r1=rules.copy()
r1=r1.drop(['representativity',  'leverage',  'conviction',  'zhangs_metric',   'jaccard',  'certainty',  'kulczynski'],axis=1)
print(r1)

rules = fp.association_rules(result, min_threshold = 0.008, metric='leverage')
r1=rules.copy()
r1=r1.drop(['representativity',  'lift',  'confidence',  'zhangs_metric',   'jaccard',  'certainty',  'kulczynski'],axis=1)
print(r1)

rules = fp.association_rules(result, min_threshold = 1.04, metric='conviction')
r1=rules.copy()
r1=r1.drop(['representativity',  'lift',  'confidence',  'zhangs_metric',   'jaccard',  'certainty',  'kulczynski'],axis=1)
print(r1)

rules = fp.association_rules(result, min_threshold = 0.3)
for r in rules:
    if(isinstance(rules[r][0], float)):
        print(r+": mean: %.2f median %.2f std %.2f"%(rules[r].mean(),rules[r].median(),rules[r].std(ddof=1)))


"""
rules = fp.association_rules(result, min_threshold = 0.4, metric='confidence')
print(rules)
G=nx.DiGraph()
for i,r in rules.iterrows():
    G.add_edges_from([(list(r['antecedents'])[0],list(r['consequents'])[0],{'support': r['support'],'confidence': "%.2f"%r['confidence']})])
pos = nx.spring_layout(G) 
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
sup = [G[u][v].get('support', 1)*10 for u, v in G.edges()]
nx.draw_networkx_edges(
    G, pos,
    edgelist=G.edges(),
    width=sup,
    arrows=True,
    arrowsize=25,
    arrowstyle='->')
nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, 'confidence')) 
plt.show()
