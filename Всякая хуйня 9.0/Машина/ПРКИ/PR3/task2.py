I={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
D=[
    {2,3,7,6},
    {1,3,4,8,11},
    {3,9,11},
    {1,5,6,7},
    {1,3,8,10,11},
    {3,5,7,9,11},
    {4,6,8,10,11},
    {1,3,5,8,11}
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

for d in D:
    if ({2,3,4}&d)!=set():
        d|={12}
    if ({8,9,10}&d)!=set():
        d|={13}
    if ({12,5}&d)!=set():
        d|={14}
    if ({7,13,14}&d)!=set():
        d|={15}

print(apriori(D,I,7))