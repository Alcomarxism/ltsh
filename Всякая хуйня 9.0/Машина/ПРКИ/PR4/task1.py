I={'A','B','C','D'}
D=[
    {'A','C','D'},
    {'B','C','D'},
    {'A','C'},
    {'A','B','D'},
    {'A','B','C','D'},
    {'B','C','D'}
    ]

def getSup(st,D):
    sup=0
    for d in D:
        if (st & d)==st:
            sup+=1
    return sup
def getNextC(L,I):
    C=set()
    for l in L:
       for i in I:
            if not(i in l):
                C=C|{(tuple(sorted(l|{i})))}
    C=[set(s) for s in C]
    return C
           
def apriori(D,I,minsup):
    F=[]
    C=[{i}for i in I]
    while C:
        L=[c for c in C if getSup(c,D)>=minsup]
        F.extend(L)        
        C=getNextC(L,I)
    return F

F=apriori(D,I,1)
rm=[]
for f in F:
    for ff in F:
        if f!=ff and getSup(f,D)==getSup(ff,D) and (f&ff)==f:
            rm.append(ff) 
for r in rm:
    F.remove(r)
print(F)